# PBC_dataset

## About This Dataset
This dataset is taken from ["A dataset for peripheral blood cell images"](https://data.mendeley.com/datasets/snkd93bnjr/1) gathered in Hospital Clinic de Barcelona.
This dataset contains exactly the same images as the original dataset, but the directory structure is reorganized.

## Discription of the Original Dataset
The dataset contains a total of 17,092 images of individual normal cells, which were acquired using the analyzer CellaVision DM96 in the Core Laboratory at the Hospital Clinic of Barcelona. The dataset is organized in the following eight groups: neutrophils, eosinophils, basophils, lymphocytes, monocytes, immature granulocytes (promyelocytes, myelocytes, and metamyelocytes), erythroblasts and platelets or thrombocytes. The size of the images is 360 x 363 pixels, in format JPG, and they were annotated by expert clinical pathologists. The images were captured from individuals without infection, hematologic or oncologic disease and free of any pharmacologic treatment at the moment of blood collection.

This high-quality labelled dataset may be used to train and test machine learning and deep learning models to recognize different types of normal peripheral blood cells. To our knowledge, this is the first publicly available set with large numbers of normal peripheral blood cells, so that it is expected to be a canonical dataset for model benchmarking.


## Directory Structure Within PBC_dataset.zip
+--othe_types
|   +--basophil       (1218 images)
|   +--erythroblast   (1551 images)
|   +--ig             (2895 images)
|   +--platelet       (2348 images)
+--wbc (4 major types of white blood cells)
|   +--eosinophil     (3117 images)
|   +--lymphocyte     (1214 images)
|   +--monocyte       (1420 images)
|   +--neutrophil     (3329 images)
+--wbc_resized (same images as in ../wbc, but resized to 128 * 128)
|   +--EOSINOPHIL
|   +--LYMPHOCYTE
|   +--MONOCYTE
|   +--NEUTROPHIL
+--resize.py 
   

## Citation
Acevedo, Andrea; Merino, Anna; Alferez, Santiago; Molina, Ángel; Boldú, Laura; Rodellar, José (2020), “A dataset for microscopic peripheral blood cell images for development of automatic recognition systems”, Mendeley Data, V1, doi: 10.17632/snkd93bnjr.1


