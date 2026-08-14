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

Results use a **patient-stratified 80:10:10 split** to minimize data leakage.

---

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
