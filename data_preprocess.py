import os 
import numpy as np
import pandas as pd
import shutil

data_origin_path = './ORCHID_data'
patch_output_path = './ORCHID_data/all_patches'
if not os.path.exists(patch_output_path):
    os.makedirs(patch_output_path)

oscc_DF = pd.DataFrame(columns=['filename', 'label'])
standard_DF = pd.DataFrame(columns=['filename', 'label'])

# for Normal
normal_path = os.path.join(data_origin_path, 'Normal')
normal_list = os.listdir(normal_path)
for normal in normal_list:
    patches_path = os.path.join(normal_path, normal, 'patches')
    patches_list = os.listdir(patches_path)
    if "DS_Store" in patches_list:
        patches_list.remove("DS_Store")
    for patch in patches_list:
        shutil.copy(os.path.join(patches_path, patch), os.path.join(patch_output_path, patch))
        # appending new entry to dataframe
        standard_DF = standard_DF.append({'filename': os.path.join(patch_output_path, patch), 'label': 'Normal'}, ignore_index=True)

# for OSMF
osmf_path = os.path.join(data_origin_path, 'OSMF')
osmf_list = os.listdir(osmf_path)
for osmf in osmf_list:
    patches_path = os.path.join(osmf_path, osmf, 'patches')
    patches_list = os.listdir(patches_path)
    if "DS_Store" in patches_list:
        patches_list.remove("DS_Store")
    for patch in patches_list:
        shutil.copy(os.path.join(patches_path, patch), os.path.join(patch_output_path, patch))
        # appending new entry to dataframe
        standard_DF = standard_DF.append({'filename': os.path.join(patch_output_path, patch), 'label': 'OSMF'}, ignore_index=True)

# for OSCC
oscc_path = os.path.join(data_origin_path, 'OSCC')
oscc_list = os.listdir(oscc_path)
for oscc in oscc_list:
    subtype_path = os.path.join(oscc_path, oscc)
    subtype_list = os.listdir(subtype_path)
    if "DS_Store" in subtype_list:
        subtype_list.remove("DS_Store")
    for subtype in subtype_list:
        patches_path = os.path.join(subtype_path, subtype, 'patches')
        patches_list = os.listdir(patches_path)
        if "DS_Store" in patches_list:
            patches_list.remove("DS_Store")
        for patch in patches_list:
            shutil.copy(os.path.join(patches_path, patch), os.path.join(patch_output_path, patch))
            # appending new entry to dataframe
            standard_DF = standard_DF.append({'filename': os.path.join(patch_output_path, patch), 'label': "OSCC"}, ignore_index=True)
            oscc_DF = oscc_DF.append({'filename': os.path.join(patch_output_path, patch), 'label': subtype}, ignore_index=True)

# save dataframe to csv
standard_DF.to_csv(os.path.join(data_origin_path, 'standard_patch.csv'), index=False)
oscc_DF.to_csv(os.path.join(data_origin_path, 'oscc_patch.csv'), index=False)
