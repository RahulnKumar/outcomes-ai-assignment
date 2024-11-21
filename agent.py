import json
from src.utils import invoke_llm
from src.prompts import system_prompt, user_prompt


patient_id = input("Please provide the patient ID \n")
instructions = input("Is there any specific data you want for this patient or just summary \n")



with open(f"patients/patient_{patient_id}_cleaned.json", 'r') as f:
    patient_json_data = json.load(f)


def charting_agent(physician_instructions_prompt):
    messages = [
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role":"user",
                    "content" : user_prompt.format(patient_json_data=patient_json_data,
                                                   physician_instructions_prompt=physician_instructions_prompt)
                }
                    ]
    response = invoke_llm(messages)
    return response


summary = charting_agent(instructions)

print(summary)



