"""
Author: Md. Tanvir Hasan
YOLO to COCO Annotation Converter for MOPG-7 Dataset
Converts YOLO .txt bounding boxes to COCO JSON format.
Generates:
  - annotations/instances_train.json
  - annotations/instances_val.json
  - annotations/instances_test.json
"""

from pathlib import Path
import json
import csv
import sys
from collections import defaultdict, OrderedDict
from PIL import Image

IMAGE_DIR = "images"
LABEL_DIR = "labels_yolo"
OUTPUT_JSON = "annotations/instances.json"
SUMMARY_CSV = "conversion_summary.csv"

SPLITS = ["test", "train", "val"]
OUTPUT_JSON_SPLIT = "annotations/instances_{split}.json"
SUMMARY_CSV_SPLIT = "conversion_summary_{split}.csv"

CLASS_NAMES = {
    0: "Missing Teeth",
    1: "Dental Crown",
    2: "Root Canal",
    3: "Caries",
    4: "Broken Down Teeth",
    5: "Wisdom Teeth",
    6: "No Target Findings",
}

DATASET_INFO = {
    "description": "MOPG-7: A Multi-Clinic Dental Panoramic Radiograph Dataset with Expert YOLO Labels",
    "url": "https://creativecommons.org/publicdomain/zero/1.0/",
    "version": "v4.0",
    "year": 2026,
    "contributor": "Faiza Feroz et al.",
    "date_created": "2026",
}

LICENSES = [
    {
        "url": "https://creativecommons.org/publicdomain/zero/1.0/",
        "id": 1,
        "name": "CC0-1.0",
    }
]

IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff", ".webp"}

USE_DEFAULT_IMAGE_SIZE = False
DEFAULT_IMAGE_WIDTH = 1000
DEFAULT_IMAGE_HEIGHT = 1000


def clamp(value, min_val, max_val):
    return max(min_val, min(max_val, value))


def clamp_bbox_to_image(x_min, y_min, bbox_w, bbox_h, img_w, img_h):
    x_max = x_min + bbox_w
    y_max = y_min + bbox_h
    x_min_clamped = clamp(x_min, 0.0, float(img_w))
    y_min_clamped = clamp(y_min, 0.0, float(img_h))
    x_max_clamped = clamp(x_max, 0.0, float(img_w))
    y_max_clamped = clamp(y_max, 0.0, float(img_h))
    return x_min_clamped, y_min_clamped, x_max_clamped - x_min_clamped, y_max_clamped - y_min_clamped


def yolo_to_coco_bbox(x_center, y_center, width, height, img_w, img_h):
    x_min = (x_center - width / 2.0) * img_w
    y_min = (y_center - height / 2.0) * img_h
    bbox_w = width * img_w
    bbox_h = height * img_h
    return x_min, y_min, bbox_w, bbox_h


def main():
    base_dir = Path(__file__).resolve().parent
    image_dir = base_dir / IMAGE_DIR
    label_dir = base_dir / LABEL_DIR
    ann_dir = base_dir / "annotations"
    ann_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 60)
    print("MOPG-7 YOLO -> COCO Annotation Converter (7 Classes)")
    print("=" * 60)

    categories = [
        {"id": cid, "name": CLASS_NAMES[cid], "supercategory": ""}
        for cid in sorted(CLASS_NAMES.keys())
    ]

    image_id_counter = 1
    annotation_id_counter = 1

    for split in SPLITS:
        split_lbl_dir = label_dir / split
        split_img_dir = image_dir / split
        lbl_files = sorted(split_lbl_dir.glob("*.txt"))

        images = []
        annotations = []

        for lbl_path in lbl_files:
            stem = lbl_path.stem
            img_path = split_img_dir / (stem + ".jpg")
            if not img_path.exists():
                for ext in [".jpeg", ".png", ".bmp"]:
                    cand = split_img_dir / (stem + ext)
                    if cand.exists():
                        img_path = cand
                        break

            if not img_path.exists():
                print(f"Warning: Image for label {lbl_path.name} not found!")
                continue

            with Image.open(img_path) as im:
                img_w, img_h = im.size

            cur_img_id = image_id_counter
            image_id_counter += 1

            rel_file_name = f"{split}/{img_path.name}"
            images.append({
                "id": cur_img_id,
                "file_name": rel_file_name,
                "width": img_w,
                "height": img_h,
            })

            lines = [l.strip() for l in lbl_path.read_text(encoding="utf-8").splitlines() if l.strip()]
            for line in lines:
                parts = line.split()
                cid = int(float(parts[0]))
                xc = float(parts[1])
                yc = float(parts[2])
                bw = float(parts[3])
                bh = float(parts[4])

                x_min, y_min, box_w, box_h = yolo_to_coco_bbox(xc, yc, bw, bh, img_w, img_h)
                x_min_c, y_min_c, box_w_c, box_h_c = clamp_bbox_to_image(x_min, y_min, box_w, box_h, img_w, img_h)

                bbox = [round(x_min_c, 3), round(y_min_c, 3), round(box_w_c, 3), round(box_h_c, 3)]
                area = round(bbox[2] * bbox[3], 2)

                annotations.append({
                    "id": annotation_id_counter,
                    "image_id": cur_img_id,
                    "category_id": cid,
                    "bbox": bbox,
                    "area": area,
                    "segmentation": [],
                    "iscrowd": 0,
                })
                annotation_id_counter += 1

        split_coco = OrderedDict()
        split_coco["info"] = DATASET_INFO
        split_coco["licenses"] = LICENSES
        split_coco["images"] = images
        split_coco["annotations"] = annotations
        split_coco["categories"] = categories

        out_path = ann_dir / f"instances_{split}.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(split_coco, f, indent=2, ensure_ascii=False)

        print(f"  [{split:5s}] -> {len(images):4d} images, {len(annotations):5d} annotations -> {out_path.name}")

    print("\nConversion finished successfully.")


if __name__ == "__main__":
    main()
