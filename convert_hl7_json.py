import base64, os, json
from pathlib import Path

files = os.listdir('data/')
output_folder = "output/"
master_json={}

for f in files:
    with open("data/{}".format(f), 'r') as fin:
        lines = [line.strip('\n') + '\r' for line in fin]
        msg = ''
        for ln in lines:
            msg += ln 
        sample_string_bytes = msg.encode("ascii")
        base64_bytes = base64.b64encode(sample_string_bytes)
        hl7_row = { "message": {"data": "{}".format(base64_bytes.decode("utf-8"))}}
        file_name = Path("data/{}".format(f)).stem        
        master_json[file_name] = hl7_row

for key, value in master_json.items():
    file_name = output_folder +key +".json"
    with open(file_name, 'w+') as f:        
        f.write(json.dumps(value))
        f.close()