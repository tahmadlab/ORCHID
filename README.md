<div align="center">
 
## ORCHID: ORal Cancer Histology Image Dataset

[![Project](http://img.shields.io/badge/Project%20Page-3d3d8f.svg)](https://ai-orchid.github.io/ORCHID-web/)
[![Paper](http://img.shields.io/badge/Paper-arxiv.1001.2234-B31B1B.svg)](#)
<!--[![Demo](http://img.shields.io/badge/Demo-9acbff.svg)](https://huggingface.co/spaces/lukemelas/deep-spectral-segmentation)
[![Conference](http://img.shields.io/badge/CVPR-2022-4b44ce.svg)](#)-->

</div>

### Description
This code accompanies the ORCHID (ORal Cancer Histology Image Dataset) and contains the information on the technical validation of the dataset.

### Abstract

Oral cancer is a global health challenge with a difficult histopathological diagnosis. The accurate histopathological interpretation of oral cancer tissue samples remains difficult. However, early diagnosis is very challenging due to a lack of experienced pathologists and inter-observer variability in diagnosis. The application of artificial intelligence (deep learning algorithms) for oral cancer histology images is very promising for rapid diagnosis. However, it requires a quality annotated dataset to build AI models. We present ORCHID (ORal Cancer Histology Image Database), a specialized database generated to advance research in AI-based histology image analytics of oral cancer and precancer. The ORCHID database is an extensive multicenter collection of 300,000 image patches, encapsulating various oral cancer and precancer categories, such as oral submucous fibrosis (OSMF) and oral squamous cell carcinoma (OSCC). Additionally, it also contains grade-level sub-classifications for OSCC, such as well-differentiated (WD), moderately-differentiated (MD), and poorly-differentiated (PD). Furthermore, the database seeks to bolster the creation and validation of innovative artificial intelligence-based rapid diagnostics for OSMF and OSCC, along with subtypes.

### How to run   

#### Dependencies
The minimal set of dependencies is listed in `requirements-ORCHID.txt` please ensure you create a conda environment with ```Python 3.9.*```. Running this code on CPU is extensively time consuming, and hence we have employed the use of an Nvidia A5000 GPU. In order to install GPU related dependencies, along with the requirements, we have created the ```initialise.sh``` script that you can run (After activating your conda enviroment to install all required dependencies).

#### Data
You must place the entirety of the Data in a location on your machine storage and provide the absolute path of this data to the ```build_dataframe.sh```, the ```train-normal-oscc-osmf.sh```, and the ```train-wd-pd-md.sh``` files. The data must be placed as shown below:
```
|Dataset
|-ORCHID-TRS-TR-NORMAL
|-ORCHID-TRS-TR-OSMF
|-ORCHID-TRS-TR-OSCC-WD
|-ORCHID-TRS-TR-OSCC-PD
|-ORCHID-TRS-TR-OSCC-MD
```
(Note: the data is supplied in as compressed tar files, they must be uncompressed before being placed in the above format.)

#### Running the training workflows
We are feeding the data into our pipeline through a three-fold cross-validation system. To generate the required dataframes to do so, you must first run the ```build_dataframe.sh``` command. This will generate a directory ```model_metadata``` in the same directory as the data, and will contain the required files (Note: The data generators have been seeded ti ensure replicability of work across).

Following this, you may use the  ```train-normal-oscc-osmf.sh``` or the ```train-wd-pd-md.sh``` to run your model of choice. The resulting models, model history, and all supplimentary information will be stored in a directory named ```models``` fold-wise.


