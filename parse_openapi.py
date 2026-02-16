#!/usr/bin/env python3
"""Parse OpenAPI 3.1.0 spec and extract all endpoint information."""

import json
import sys

def main():
    with open("/Users/incit/Downloads/openapi.json", "r") as f:
        spec = json.load(f)

    # 1. API Info
    info = spec.get("info", {})
    print("=" * 80)
    print("API INFO")
    print("=" * 80)
    print(f"Title: {info.get('title', 'N/A')}")
    print(f"Version: {info.get('version', 'N/A')}")
    print(f"Description: {info.get('description', 'N/A')}")
    
    # Servers
    servers = spec.get("servers", [])
    if servers:
        print(f"\nServers:")
        for s in servers:
            print(f"  - {s.get('url', 'N/A')}: {s.get('description', '')}")

    # Security schemes
    security_schemes = spec.get("components", {}).get("securitySchemes", {})
    if security_schemes:
        print(f"\nSecurity Schemes:")
        for name, scheme in security_schemes.items():
            print(f"  - {name}: type={scheme.get('type')}, scheme={scheme.get('scheme', 'N/A')}, in={scheme.get('in', 'N/A')}, name={scheme.get('name', 'N/A')}")

    # Tags
    tags = spec.get("tags", [])
    if tags:
        print(f"\nTags:")
        for t in tags:
            desc = t.get('description', '')
            if desc and len(desc) > 200:
                desc = desc[:200] + "..."
            print(f"  - {t.get('name', 'N/A')}: {desc}")

    # 2. All Paths/Endpoints
    print("\n" + "=" * 80)
    print("ENDPOINTS")
    print("=" * 80)
    
    paths = spec.get("paths", {})
    endpoint_count = 0
    
    for path, path_item in sorted(paths.items()):
        for method in ["get", "post", "put", "patch", "delete", "head", "options", "trace"]:
            if method not in path_item:
                continue
            
            endpoint_count += 1
            op = path_item[method]
            
            print(f"\n{'─' * 70}")
            print(f"[{endpoint_count}] {method.upper()} {path}")
            print(f"  Tags: {', '.join(op.get('tags', ['N/A']))}")
            print(f"  Summary: {op.get('summary', 'N/A')}")
            print(f"  OperationId: {op.get('operationId', 'N/A')}")
            
            desc = op.get('description', '')
            if desc:
                if len(desc) > 300:
                    desc = desc[:300] + "..."
                print(f"  Description: {desc}")
            
            # Parameters
            params = op.get('parameters', [])
            # Also check path-level parameters
            path_params = path_item.get('parameters', [])
            all_params = path_params + params
            
            if all_params:
                print(f"  Parameters ({len(all_params)}):")
                for p in all_params:
                    if '$ref' in p:
                        print(f"    - $ref: {p['$ref']}")
                        continue
                    req = "required" if p.get('required', False) else "optional"
                    p_desc = p.get('description', '')
                    if p_desc and len(p_desc) > 150:
                        p_desc = p_desc[:150] + "..."
                    
                    schema_info = ""
                    schema = p.get('schema', {})
                    if schema:
                        schema_type = schema.get('type', '')
                        schema_format = schema.get('format', '')
                        schema_default = schema.get('default', '')
                        schema_enum = schema.get('enum', '')
                        parts = []
                        if schema_type:
                            parts.append(f"type={schema_type}")
                        if schema_format:
                            parts.append(f"format={schema_format}")
                        if schema_default != '':
                            parts.append(f"default={schema_default}")
                        if schema_enum:
                            parts.append(f"enum={schema_enum}")
                        if parts:
                            schema_info = f" [{', '.join(parts)}]"
                    
                    print(f"    - {p.get('name', 'N/A')} (in: {p.get('in', 'N/A')}, {req}){schema_info}: {p_desc}")
            
            # Request Body
            req_body = op.get('requestBody', None)
            if req_body:
                print(f"  Request Body: required={req_body.get('required', False)}")
                content = req_body.get('content', {})
                for ct, ct_val in content.items():
                    schema = ct_val.get('schema', {})
                    schema_str = ""
                    if '$ref' in schema:
                        schema_str = schema['$ref']
                    elif 'type' in schema:
                        schema_str = schema.get('type', '')
                        if schema.get('properties'):
                            props = list(schema['properties'].keys())
                            schema_str += f" with properties: {props}"
                    print(f"    Content-Type: {ct}, Schema: {schema_str}")
            
            # Responses
            responses = op.get('responses', {})
            if responses:
                print(f"  Responses:")
                for code, resp in responses.items():
                    resp_desc = resp.get('description', 'N/A')
                    if len(resp_desc) > 100:
                        resp_desc = resp_desc[:100] + "..."
                    resp_content = resp.get('content', {})
                    content_types = list(resp_content.keys()) if resp_content else []
                    
                    # Get response schema info
                    schema_info = ""
                    for ct, ct_val in resp_content.items():
                        schema = ct_val.get('schema', {})
                        if '$ref' in schema:
                            schema_info = f" -> {schema['$ref']}"
                        elif 'type' in schema:
                            if schema['type'] == 'array' and 'items' in schema:
                                items = schema['items']
                                if '$ref' in items:
                                    schema_info = f" -> array of {items['$ref']}"
                                else:
                                    schema_info = f" -> array of {items.get('type', '?')}"
                            else:
                                schema_info = f" -> {schema.get('type', '?')}"
                    
                    print(f"    {code}: {resp_desc} [{', '.join(content_types) if content_types else 'no content'}]{schema_info}")

            # Security
            security = op.get('security', [])
            if security:
                sec_names = []
                for s in security:
                    sec_names.extend(s.keys())
                print(f"  Security: {', '.join(sec_names)}")

    print(f"\n\nTotal endpoints: {endpoint_count}")

    # 3. Schema Names
    print("\n" + "=" * 80)
    print("SCHEMAS (components/schemas)")
    print("=" * 80)
    
    schemas = spec.get("components", {}).get("schemas", {})
    for name, schema in sorted(schemas.items()):
        schema_type = schema.get('type', 'N/A')
        desc = schema.get('description', '')
        if desc and len(desc) > 150:
            desc = desc[:150] + "..."
        
        props = schema.get('properties', {})
        required_fields = schema.get('required', [])
        
        enum_vals = schema.get('enum', [])
        
        print(f"\n  {name} (type: {schema_type})")
        if desc:
            print(f"    Description: {desc}")
        if enum_vals:
            print(f"    Enum values: {enum_vals}")
        if props:
            prop_names = list(props.keys())
            print(f"    Properties ({len(prop_names)}): {prop_names}")
            if required_fields:
                print(f"    Required: {required_fields}")
            # Print property details
            for pname, pval in props.items():
                p_type = pval.get('type', '')
                p_desc = pval.get('description', '')
                p_ref = pval.get('$ref', '')
                p_format = pval.get('format', '')
                p_enum = pval.get('enum', '')
                
                parts = []
                if p_ref:
                    parts.append(f"$ref={p_ref}")
                if p_type:
                    parts.append(f"type={p_type}")
                if p_format:
                    parts.append(f"format={p_format}")
                if p_enum:
                    parts.append(f"enum={p_enum}")
                if p_desc:
                    if len(p_desc) > 120:
                        p_desc = p_desc[:120] + "..."
                    parts.append(f"desc={p_desc}")
                
                req_marker = "*" if pname in required_fields else ""
                print(f"      - {pname}{req_marker}: {', '.join(parts)}")

    print(f"\nTotal schemas: {len(schemas)}")

if __name__ == "__main__":
    main()
