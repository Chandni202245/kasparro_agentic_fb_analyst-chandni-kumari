
import json, datetime, os
def write_log(path, payload):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path,'w') as f:
        json.dump(payload, f, indent=2, default=str)
