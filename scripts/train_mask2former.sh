#!/usr/bin/env bash
# python3 -m pip install opencv-python-headless==4.8.0.74 pillow==9.5.0 phenobench torchmetrics
python3 train_net_pheno.py --config-file configs/phenobench/mask2former_plants.yaml --num-gpus 1