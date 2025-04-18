import json
import os
from totalsegmentator.bin.totalseg_get_phase import get_ct_contrast_phase
import glob

path_to_ex0 = "/home/vankhoa@median.cad/code/heh/hcc_preprocessing/HCC/experiments/experiment0_patient_balance_2"
dataset = "train"

json_files = glob.glob(f"{path_to_ex0}/{dataset}/*.json", recursive=True)

print(f"Found {len(json_files)} JSON files in {path_to_ex0}/{dataset}")

for json_file in json_files:
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    # Extract the CT image path from the JSON data
    ct_image_paths = data.get('image_paths')
    patient_id = data.get('patient_id')
    for phase, ct_image_path in ct_image_paths.items():
        if ct_image_path:
            # Call the get_ct_contrast_phase function with the CT image path
            print(f"Result for {ct_image_path}, Phase: {phase}")
            result_file = f"output/{patient_id}_{phase}.json"
            # result = get_ct_contrast_phase(ct_image_path)
            os.system(f"totalseg_get_phase -i {ct_image_path} -o {result_file}")
            
            # Print or save the result as needed
            
            # print(result)
        else:
            print(f"No CT image path found in {json_file}")