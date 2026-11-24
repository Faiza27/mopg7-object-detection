# Multi-clinic dental panoramic radiograph dataset with expert labels for six conditions and no target findings

Official repository for **MOPG-7**, providing reproducible YOLO-based object detection benchmarks for multi-clinic dental panoramic radiographs.

---

## 📦 Dataset

**1.941** anonymized high-resolution dental panoramic radiographs with **7-class bounding-box annotations**.

Dataset:
https://data.mendeley.com/datasets/r43v452t29/3

---

## 🦷 Classes

|  ID | Class             |
| --: | ----------------- |
|   0 | Missing Teeth     |
|   1 | Dental Crown      |
|   2 | Root Canal        |
|   3 | Caries            |
|   4 | Broken Down Teeth |
|   5 | Wisdom Teeth      |
|   6 | No Target Findings     |

---

## 📁 Repository Structure

```text
mopg7-object-detection/
├── README.md
├── mopg7_validation.ipynb
├── configs/
│   └── data.yaml
└── output/
    ├── sa_yolov8m/
    ├── sa_yolov10m/
    └── sa_yolov11m/
```

Each model folder contains training logs, evaluation plots, validation visualizations, and `best.pt` / `last.pt` checkpoints.

---

## 📊 Baseline Results

| Model    | Precision |    Recall |   mAP@0.5 | mAP@0.5:0.95 |    Latency |
| -------- | --------: | --------: | --------: | -----------: | ---------: |
| YOLOv8m  |     0.679 | **0.744** | **0.705** |    **0.325** |     2.0 ms |
| YOLOv10m |     0.667 |     0.668 |     0.661 |        0.306 | **0.6 ms** |
| YOLOv11m | **0.714** |     0.686 |     0.691 |        0.296 |     3.1 ms |

Results use a **80:10:10 split** to minimize data leakage.

---


## 🔬 Inter-Annotator Agreement (IAA)

An independent inter-annotator agreement (IAA) analysis was performed on **419 OPG images (20.0% of the complete dataset)** to assess annotation consistency between two clinical annotators.

The analysis evaluated all seven bounding-box classes using **Intersection over Union (IoU)**. One-to-one spatial correspondence between annotations was established using the Hungarian assignment algorithm, with an IoU threshold of **0.50**. Unmatched annotations were retained in the analysis and assigned an IoU of 0 for the full-data agreement calculation. Class-level agreement was evaluated for spatially corresponding annotations, while unmatched annotations were treated as disagreements. :contentReference[oaicite:1]{index=1}

### IAA Summary


| Metric | Result |
|---|---:|
| IAA subset | 390 OPG images |
| Dr. Jinia bounding boxes | 1,840 |
| Dr. Afrina bounding boxes | 1,884 |
| Total bounding boxes | 3,724 |
| Matched bounding-box pairs | 1,816 |
| Total unmatched boxes | 92 |
| IoU ≥ 0.50 (all boxes) | **97.53% (3,632/3,724)** |
| IoU < 0.50 (all boxes) | **2.47% (92/3,724)** |
| IoU ≥ 0.80 (all boxes) | **95.60% (3,560/3,724)** |
| IoU < 0.80 (all boxes) | **4.40% (164/3,724)** |
| Mean IoU (all boxes) | **0.8933** |
| Median IoU | **0.9219** |
| Class agreement (all boxes) | **96.99%** |
| Macro Precision (7 classes) | **0.9605** |
| Macro Recall (7 classes) | **0.9848** |
| Macro F1-score (7 classes) | **0.9719** |
| Disagreement records | **102** |
| Images requiring clinical review | 56 |
| Quality-control issue records | 16 |
| Duplicate bounding-box pairs | 0 |


The analysis identified **92 unmatched bounding boxes** and **10 class-level disagreements among spatially matched pairs**, resulting in **102 disagreement records** across the 390-image subset. A total of **56 OPG images** contained at least one disagreement and were identified for clinical review. :contentReference[oaicite:2]{index=2}

### IAA Notebook

The complete reproducible IAA analysis is available in:

👉 **[`IAA_Report.ipynb`](IAA_Report.ipynb)**

The notebook includes annotation validation, one-to-one Hungarian matching, full-data IoU analysis, threshold comparison, class-level agreement analysis, unmatched-box analysis, disagreement identification, and quality-control checks.

## 🚀 Reproduction

1. Open `mopg7_validation.ipynb` in **Google Colab**
2. Enable GPU runtime
3. Install **Ultralytics YOLO** dependencies
4. Configure the dataset in `configs/data.yaml`
5. Run the training and evaluation pipeline

---



## 💻 Software and Hardware Environment

The dataset analysis, annotation, and baseline experiments were conducted using the following software environment:

| Component | Version |
|---|---|
| Python | 3.11.1 |
| LabelImg | 1.8.1 |
| NumPy | 2.1.3 |
| PyTorch | 2.11.0+cu128 |
| Pandas | 2.2.3 |
| SciPy | 1.16.3 |
| Pillow | 11.3.0 |
| tqdm | 4.67.3 |
| Matplotlib | 3.10.0 |
| Seaborn | 0.13.2 |
| scikit-learn | 1.6.1 |
| Ultralytics | 8.4.0 |
| Operating System | Windows 11 Pro |


## 📌 Citation

```bibtex
@article{mopg7_2026,
  title={Multi-clinic dental panoramic radiograph dataset with expert labels for six conditions and no target findings},
  author={Feroz, F., Hasan, M.~T., Samapti, E.~T., Hasan, M.~T., Partho, S.~S., Talukder, Z., Chowdhury, A., Hasan, M.~Z., Bijoy, M.~H.~I., \& Samad, M.~A.,},
  journal={Scientific Data},
  year={2026},
  publisher={Nature Portfolio}
}
```

---

## 📄 License

Released under the **MIT License**.
