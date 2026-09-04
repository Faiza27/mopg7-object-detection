# MOPG-7 — Multi-Clinic Panoramic Radiograph Object Detection

Official repository for **MOPG-7**, providing reproducible YOLO-based object detection benchmarks for multi-clinic dental panoramic radiographs.

---

## 📦 Dataset

**2,095** anonymized high-resolution dental panoramic radiographs with **7-class bounding-box annotations**.

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
|   6 | Healthy Teeth     |

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
| YOLOv8m  | **0.719** |     0.706 | **0.729** |        0.333 | **1.9 ms** |
| YOLOv10m |     0.660 | **0.742** |     0.724 |    **0.344** |     3.4 ms |
| YOLOv11m |     0.709 |     0.716 |     0.717 |        0.335 |     4.2 ms |

Results use a **80:10:10 split** to minimize data leakage.

---

---

## 🔬 Inter-Annotator Agreement (IAA)

An independent inter-annotator agreement (IAA) analysis was performed on **419 OPG images (20.0% of the complete dataset)** to assess annotation consistency between two clinical annotators.

The analysis evaluated all seven bounding-box classes using **Intersection over Union (IoU)**. One-to-one spatial correspondence between annotations was established using the Hungarian assignment algorithm, with an IoU threshold of **0.50**. Unmatched annotations were retained in the analysis and assigned an IoU of 0 for the full-data agreement calculation. Class-level agreement was evaluated for spatially corresponding annotations, while unmatched annotations were treated as disagreements. :contentReference[oaicite:1]{index=1}

### IAA Summary

| Metric | Result |
|---|---:|
| IAA subset | 419 OPG images (20.0%) |
| Dr. Jinia bounding boxes | 1,879 |
| Dr. Afrina bounding boxes | 1,923 |
| Total bounding boxes | 3,802 |
| Matched bounding-box pairs | 1,854 |
| Total unmatched boxes | 94 |
| IoU ≥ 0.50 (all boxes) | **97.53% (3,708/3,802)** |
| IoU < 0.50 (all boxes) | **2.47% (94/3,802)** |
| IoU ≥ 0.80 (all boxes) | **95.63% (3,636/3,802)** |
| IoU < 0.80 (all boxes) | **4.37% (166/3,802)** |
| Mean IoU (all boxes) | **0.8941** |
| Median IoU | **0.9224** |
| Class agreement (all boxes) | **97.00%** |
| Macro Precision (7 classes) | **0.9580** |
| Macro Recall (7 classes) | **0.9843** |
| Macro F1-score (7 classes) | **0.9704** |
| Disagreement records | **104** |
| Images requiring clinical review | **57** |
| Quality-control issue records | **18** |
| Duplicate bounding-box pairs | **0** |

The analysis identified **94 unmatched bounding boxes** and **10 class-level disagreements among spatially matched pairs**, resulting in **104 disagreement records** across the 419-image subset. A total of **57 OPG images** contained at least one disagreement and were identified for clinical review. :contentReference[oaicite:2]{index=2}

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

## 📌 Citation

```bibtex
@article{mopg7_2026,
  title={MOPG-7 — A multi-clinic dataset of dental panoramic radiographs with expert bounding-box labels for object detection},
  author={Faiza, et al.},
  journal={Scientific Data},
  year={2026},
  publisher={Nature Portfolio}
}
```

---

## 📄 License

Released under the **MIT License**.
