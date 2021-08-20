# 运行前的准备
ps: 本仓库对运行所需要的东西做了一定的修改.更好的能够运行.
# Reqirements
### The code environments is running on:
- CUDA 9, cuDNN 7
- Tensorflow==1.13.0
- python==3.6 

### Sub-modules:
- netdef_models: https://github.com/lmb-freiburg/netdef_models
- lmbspecialops: https://github.com/lmb-freiburg/lmbspecialops
- netdef_slim: https://github.com/lmb-freiburg/netdef_slim

### 文件夹tree:

- external/netdef_models/lmbspecialops
- external/netdef_models/netdef_slim
  
### data部分的文件夹:
```
data
├── 2d_mots_vis
│   └── 0002
├── 3d_mots_vis
│   └── 0002
├── KITTI_tracking
│   ├── test
│   └── train
│       └── images
│           └── 0002
│               ├── image_2
│               └── image_3
└── out
    ├── 2D_tracking_result
    │   └── 0002
    ├── 3D_tracking_result
    │   └── 0002
    ├── detections
    │   └── 0002
    ├── flow_disp_netdef
    │   └── 0002
    ├── point_imgs
    │   └── 0002
    ├── poses_orbslam
    │   └── 0002
    └── segmentations
        └── 0002
```

## 数据集:


# `precompute.py` 文件
该文件作用是运行生成`main.py`所需要的mask,光流等.


# `main.py`文件
运行生成