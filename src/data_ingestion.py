import json
from pathlib import Path
from utils import invoke_llm


with open("/Users/rahul.kumar23/Drive/outcomes-ai-assignment/patients/patient_1.json", 'r') as f:
    data = json.load(f)

patient_data = {}

for node in data:
    node_name = list(node.keys())[0]

    if node_name == "patient":
        print(node)
        patient_data["meta_data"]  = node['patient']

    else:
        # print(node)
        for idx,item in enumerate(node[node_name]):
            # print(item.values())
            system_prompt = f"you are a physician and reviews patient records before consultations. Given below is data for {node_name} of a patient. Your task is to summarize this data in plain english. Just return summarized important data and drop the non-usefull details. Keep the summary short and informative."
            prompt = item.values()
            messages = [
                {
                    "role": "system",
                    "content": f"{system_prompt}"
                },
                {
                    "role":"user",
                    "content" : prompt
                }
                    ]
            # print(messages)
            summary = invoke_llm(messages)
            patient_data[f"{node_name}_{idx}"] = summary
            import time
            time.sleep(10)
            # break


file_path = "/Users/rahul.kumar23/Drive/outcomes-ai-assignment/patients/patient_1_cleaned.json"
with open(file_path, 'w') as json_file:
    json.dump(patient_data, json_file, indent=4) 