_base_ = [
    "_base_/models/hv_pointpillars_secfpn_waymo.py",
    "_base_/datasets/waymoD5-3d-3class.py",
    "_base_/schedules/schedule_2x.py",
    "_base_/default_runtime.py",
]

dataset_type = _base_.dataset_type  + "_waymoD5-3d-3class" 
voxel_size = {{_base_.voxel_size}}  # copy the _base_.voxel_size from the base config file
a = _base_.model
a["type"] = "HVPointPillars"
