import json
import sys

with open('/Users/incit/Downloads/openapi.json', 'r') as f:
    data = json.load(f)

# Basic info
info = data.get('info', {})
print("TITLE:", info.get('title', ''))
print("VERSION:", info.get('version', ''))
print("---")

# Paths
paths = data.get('paths', {})
for path, methods in paths.items():
    for method, details in methods.items():
        if isinstance(details, dict):
            tags = details.get('tags', [])
            summary = details.get('summary', 'No summary')
            params = details.get('parameters', [])
            param_info = []
            for p in params:
                if isinstance(p, dict):
                    param_info.append({
                        'name': p.get('name', ''),
                        'in': p.get('in', ''),
                        'required': p.get('required', False),
                        'description': p.get('description', '')
                    })
            
            # Request body
            req_body = details.get('requestBody', {})
            
            # Responses
            responses = details.get('responses', {})
            resp_codes = list(responses.keys())
            
            print(f"METHOD: {method.upper()}")
            print(f"PATH: {path}")
            print(f"TAGS: {','.join(tags)}")
            print(f"SUMMARY: {summary}")
            print(f"PARAMS: {json.dumps(param_info)}")
            print(f"HAS_BODY: {'yes' if req_body else 'no'}")
            print(f"RESPONSES: {','.join(resp_codes)}")
            print("---")

# Schemas
schemas = data.get('components', {}).get('schemas', {})
print("SCHEMAS:", ','.join(list(schemas.keys())))
