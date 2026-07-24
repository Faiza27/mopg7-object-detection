# mopg7-object-detection
Official repository for "MOPG-7", featuring Google Colab training pipelines and validation benchmarks (YOLOv8, YOLOv9, YOLOv11) for multi-clinic dental panoramic radiograph object detection.
# MOPG-7 — Multi-Clinic Panoramic Radiograph Object Detection Benchmark

This repository contains the official evaluation code, hyperparameter logs, and technical validation benchmarks for the **MOPG-7 Dataset**, as presented in our manuscript:  
> **"MOPG-7 — A multi-clinic dataset of 2,095 dental panoramic radiographs with expert bounding-box labels for object detection"** (Submitted to *Scientific Reports*)

---

## 📌 Dataset Access
The complete dataset consisting of 2,095 high-resolution anonymized dental panoramic radiographs (OPGs) and their corresponding 7-class regional bounding box annotations (`labelIMG` / YOLO format) is openly available on our repository platform:
🔗 **https://data.mendeley.com/preview/r43v452t29?a=c468fdbf-7def-4d6c-8374-8793fe5f9efe**

---

## 🗂️ Repository Structure
This repository preserves the raw, native directory output generated directly by the Ultralytics YOLO framework to guarantee absolute transparency and untampered verification during peer review.

```text
mopg7-object-detection/
├── README.md                 # Project documentation & benchmark matrices
├── mopg7_validation.ipynb    # Google Colab notebook for end-to-end training
├── configs/
│   └── data.yaml             # YOLO configuration file mapping the 7 classes
└── output/                   
    └── sa_yolov8m/           # Native YOLO run folder 
        ├── args.yaml         # Training hyperparameters and logging constraints
        ├── results.csv       # Epoch-by-epoch tracking metrics (Loss, mAP)
        ├── results.png       # Plotted optimization training curves
        ├── confusion_matrix_normalized.png # Normalized multi-class error matrix
        ├── BoxPR_curve.png   # Precision-Recall curve across all classes
        ├── labels.jpg        # Spatial anchor dataset distribution profile
        ├── train_batch*.jpg  # Visual logging of augmentation training batches
        ├── val_batch*_labels.jpg # Expert clinical ground-truth bounding boxes
        ├── val_batch*_pred.jpg   # Trained model inference validation previews
        └── weights/          
            ├── best.pt       # Top-performing checkpoint weights for evaluation
            └── last.pt       # Final training epoch checkpoint weights
    └── sa_yolov10m/           # Native YOLO run folder 
            ├── args.yaml         # Training hyperparameters and logging constraints
            ├── results.csv       # Epoch-by-epoch tracking metrics (Loss, mAP)
            ├── results.png       # Plotted optimization training curves
            ├── confusion_matrix_normalized.png # Normalized multi-class error matrix
            ├── BoxPR_curve.png   # Precision-Recall curve across all classes
            ├── labels.jpg        # Spatial anchor dataset distribution profile
            ├── train_batch*.jpg  # Visual logging of augmentation training batches
            ├── val_batch*_labels.jpg # Expert clinical ground-truth bounding boxes
            ├── val_batch*_pred.jpg   # Trained model inference validation previews
            └── weights/          
                ├── best.pt       # Top-performing checkpoint weights for evaluation
                └── last.pt       # Final training epoch checkpoint weights
    └── sa_yolov11m/           # Native YOLO run folder 
            ├── args.yaml         # Training hyperparameters and logging constraints
            ├── results.csv       # Epoch-by-epoch tracking metrics (Loss, mAP)
            ├── results.png       # Plotted optimization training curves
            ├── confusion_matrix_normalized.png # Normalized multi-class error matrix
            ├── BoxPR_curve.png   # Precision-Recall curve across all classes
            ├── labels.jpg        # Spatial anchor dataset distribution profile
            ├── train_batch*.jpg  # Visual logging of augmentation training batches
            ├── val_batch*_labels.jpg # Expert clinical ground-truth bounding boxes
            ├── val_batch*_pred.jpg   # Trained model inference validation previews
            └── weights/          
                ├── best.pt       # Top-performing checkpoint weights for evaluation
                └── last.pt       # Final training epoch checkpoint weights
```

---

## 🏷️ Class Mapping & Clinical Annotation Matrix
The regional bounding box labels generated via `labelIMG` map 7 specialized dental conditions balancing active pathologies with historical post-treatment restorations:
*   `0`: Impacted Wisdom
*   `1`: Missing Teeth
*   `2`: Filling
*   `3`: Root Canal with Filling
*   `4`: Root Canal with Dental Crown
*   `5`: Root Canal
*   `6`: Broken down

---

## 🚀 How to Reproduce the MOPG-7 Benchmarks

### 1. Google Colab Environment Setup
* Open the provided `mopg7_validation.ipynb` notebook directly in Google Colab.
* Ensure your runtime environment is connected to a hardware accelerator (GPU instance: T4, V100, or A100).

### 2. Dataset Initialization & Training
* Run the initialization cells to install the requisite `ultralytics` environment.
* Download and extract the raw images and labels zip archives directly into your workspace.
* Point the pipeline to the `configs/data.yaml` setting to load your class anchors.
* Execute the training workflows using standard vanilla checkpoints to audit the data's learnability.

---

## 📊 Technical Validation Baseline Metrics
*The performance metrics below represent the baseline validation profiles across a strict, patient-stratified 70:10:20 dataset split to eliminate data leakage:*

| Architecture | Precision | Recall | mAP@0.5 | mAP@0.5:0.95 |
| :--- | :--- | :--- | :--- | :--- |
| **YOLOv8m** | *[0.XX]* | *[0.XX]* | *[0.XX]* | *[0.XX]* |
| **YOLOv10m** | *[0.XX]* | *[0.XX]* | *[0.XX]* | *[0.XX]* |
| **YOLOv11m** | *[0.XX]* | *[0.XX]* | *[0.XX]* | *[0.XX]* |

*(Note: Please fill in the placeholder `[0.XX]` values using the top scores recorded in your respective `results.csv` files).*

---

## 📜 Open-Source License & Citations
The pipeline code, configurations, and evaluation assets in this repository are released under the open-source **MIT License**. If you utilize the MOPG-7 dataset or our benchmarking code in your research, please cite our paper:

```bibtex
@article{mopg7_2026,
  title={MOPG-7 — A multi-clinic dataset of 2,095 dental panoramic radiographs with expert bounding-box labels for object detection},
  author={Faiza, et al.},
  journal={Scientific Reports},
  year={2026},
  publisher={Nature Portfolio}
}
```
