import nibabel as nib
from totalsegmentator.python_api import totalsegmentator
import os
from pathlib import Path

if __name__ == "__main__":
    input_path = "/home/vankhoa@median.cad/datasets/MedDec/phelicar/LIVER0001_I13S2/scan_portal_raw.nii.gz"
    output_path = "/home/vankhoa@median.cad/code/github/TotalSegmentator/results/portal_raw"
    os.makedirs(output_path, exist_ok=True)

    # option 1: provide input and output as file paths
    # totalsegmentator(input_path, output_path)
    
    # option 2: provide input and output as nifti image objects
    input_img = nib.load(input_path)
    output_img, stats = totalsegmentator(input_img, statistics=True, radiomics=False, output=Path(output_path))
    nib.save(output_img, output_path)

    print(stats)
    print(f"Output saved to {output_path}")