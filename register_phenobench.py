import os
from mask2former.data.datasets.register_phenobench_panoptic_annos_semseg import register_pheno_panoptic_separated
def register_phenobench():
    
    root_dir = "/mnt/e/datasets/phenobench"
    register_pheno_panoptic_separated(name="phenobench_train", 
                        metadata={},
                        image_root=os.path.join(root_dir, "train/images/"),
                        panoptic_root=os.path.join(root_dir, "plants_panoptic_train"),
                        panoptic_json=os.path.join(root_dir, "plants_panoptic_train.json"),
                        sem_seg_root=os.path.join(root_dir, "plants_panoptic_semseg_train"),
                        #    instances_json="/mnt/e/datasets/phenobench/plants_panoptic_train.json",
                        )
    register_pheno_panoptic_separated(name="phenobench_val", 
                        metadata={},
                        image_root=os.path.join(root_dir, "val/images/"),
                        panoptic_root=os.path.join(root_dir, "plants_panoptic_val"),
                        panoptic_json=os.path.join(root_dir, "plants_panoptic_val.json"),
                        sem_seg_root=os.path.join(root_dir, "plants_panoptic_semseg_val"),
                        #    instances_json="/mnt/e/datasets/phenobench/plants_panoptic_val.json",
                        )
    from detectron2.data import MetadataCatalog
    # MetadataCatalog.get("phenobench_train").ignore_label = 255
    # MetadataCatalog.get("phenobench_val").ignore_label = 255
    MetadataCatalog.get('phenobench_train').set(
        thing_classes=["crop", "weed"],
        thing_dataset_id_to_contiguous_id={1: 1, 2: 2},
        stuff_classes=["soil"],
        stuff_dataset_id_to_contiguous_id={0: 0},
        thing_colors=[(111, 74, 0), (230, 150, 140)],  # Example colors for visualization
        stuff_colors=[(0, 0, 0)],  # color for background
    )
    MetadataCatalog.get('phenobench_val').set(
        thing_classes=["crop", "weed"],
        thing_dataset_id_to_contiguous_id={1: 1, 2: 2},
        stuff_classes=["soil"],
        stuff_dataset_id_to_contiguous_id={0: 0},
        thing_colors=[(111, 74, 0), (230, 150, 140)],  # Example colors for visualization
        stuff_colors=[(0, 0, 0)],  # Example color for background,
    )