import os
import pandas as pd
import sys

def build_df(path, setseed=42):
    # path = "/Users/mraoaakash/Documents/research/research-nisha/ORCHID_data/ORCHID_data/ORCHID_TRS_working" #enter the path to the folder where the data is stored
    save_path = os.path.join(path, "model_metadata")
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    for data_type in [1,2]:
        filetype=""
        label = ""
        labels = []
        paths = []
        filetypes = []

        for mainfile in os.listdir(path):
            if ".DS_Store" in mainfile or "metadata" in mainfile or "model" in mainfile:
                continue
            print(mainfile)
            if "TT" in mainfile:
                filetype = "test"
            elif "TR" in mainfile:
                filetype = "train"
            if data_type == 1:
                if "WD" in mainfile:
                    label = "WDOSCC"
                elif "MD" in mainfile:
                    label = "MDOSCC"
                elif "PD" in mainfile:
                    label = "PDOSCC"
            elif data_type == 2:
                if "OSCC" in mainfile:
                    label = "OSCC"
            if "NORMAL" in mainfile:
                if data_type == 1:
                    continue
                label = "NORMAL"
            if "OSMF" in mainfile:
                if data_type == 1:
                    continue
                label = "OSMF"
            
            print(filetype, label)
            for subfile in os.listdir(os.path.join(path, mainfile)):
                if ".DS_Store" in subfile or "metadata" in subfile:
                    continue
                subpath = os.path.join(path, mainfile, subfile)
                for file in os.listdir(subpath):
                    if ".DS_Store" in file:
                        continue
                    filepath = os.path.join(subpath, file)
                    # print("----",file_relative)
                    labels.append(label)
                    filetypes.append(filetype)
                    paths.append(filepath)

        df = pd.DataFrame({"label":labels, "filename":paths, "split":filetypes})
        print(df.head())
        adder = "_OSCC" if data_type==1 else ""
        df.to_csv(f"{save_path}/model_tr{adder}.csv", index=False)

        # print(df.head())
        df = df[df["split"] == "train"]
        df = df.drop(columns=["split"])
        classes = df["label"].unique()
        print(classes)
        df = df.sample(frac=1, random_state=1).reset_index(drop=True)
        print(len(df)//3)
        for i in range(3):
            df_split = df.iloc[i*len(df)//3:(i+1)*len(df)//3]
            print(len(df_split))
            df_split.to_csv(f"{save_path}/model_tr{adder}_fold_{i}.csv", index=False)
    
if __name__ == "__main__":
    # taking in argument
    try:
        path  = sys.argv[1] 
        setseed = sys.argv[2] 
    except:
        print("Please provide path to the data folder and setseed")
        sys.exit(1)
    print(path)
    build_df(path, setseed)



            
        

