import os
from mask2former.data.datasets.register_phenobench_panoptic_annos_semseg import register_pheno_panoptic_separated, get_metadata, get_metadata_leaves
def register_phenobench():
    
    root_dir = "/home/niqbal/datasets/phenobench/"
    register_pheno_panoptic_separated(name="phenobench_train", 
                        metadata=get_metadata(),
                        image_root=os.path.join(root_dir, "train/images/"),
                        panoptic_root=os.path.join(root_dir, "plants_panoptic_train"),
                        panoptic_json=os.path.join(root_dir, "plants_panoptic_train.json"),
                        sem_seg_root=os.path.join(root_dir, "plants_panoptic_semseg_train"),
                        #    instances_json="/mnt/e/datasets/phenobench/plants_panoptic_train.json",
                        )
    register_pheno_panoptic_separated(name="phenobench_val", 
                        metadata=get_metadata(),
                        image_root=os.path.join(root_dir, "val/images/"),
                        panoptic_root=os.path.join(root_dir, "plants_panoptic_val"),
                        panoptic_json=os.path.join(root_dir, "plants_panoptic_val.json"),
                        sem_seg_root=os.path.join(root_dir, "plants_panoptic_semseg_val"),
                        #    instances_json="/mnt/e/datasets/phenobench/plants_panoptic_val.json",
                        )
    
def register_synthetic_pheno():
    root_dir = "/home/niqbal/datasets/sugarbeet_syn_v6"
    register_pheno_panoptic_separated(name="syn_train", 
                        metadata=get_metadata(),
                        image_root=os.path.join(root_dir, "images"),
                        panoptic_root=os.path.join(root_dir, "plants_panoptic_train"),
                        panoptic_json=os.path.join(root_dir, "plants_panoptic_train.json"),
                        sem_seg_root=os.path.join(root_dir, "plants_panoptic_semseg_train")
                        )
    root_dir = "/home/niqbal/datasets/sugarbeets_leaves"
    register_pheno_panoptic_separated(name="syn_train_leaves", 
                        metadata=get_metadata_leaves(),
                        image_root=os.path.join(root_dir, "images"),
                        panoptic_root=os.path.join(root_dir, "leafs_panoptic_train"),
                        panoptic_json=os.path.join(root_dir, "leafs_panoptic_train.json"),
                        sem_seg_root=os.path.join(root_dir, "leafs_panoptic_semseg_train")
                        )