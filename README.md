# multitasks based on openmmlab
## 文件树说明
```bash
.
├── configs # 配置文件
│   ├── det
│   ├── det3d
│   └── seg
├── demo    # 演示
│   ├── det
│   ├── det3d
│   └── seg
├── mtl # 多任务
│   ├── apis        # 接口
│   ├── datasets    # 数据集
│   ├── engine      # 引擎
│   ├── evaluation  # 评估
│   ├── __init__.py # 初始化
│   ├── model       # 模型
│   ├── registry    # 注册
│   ├── utils       # 工具
│   └── version.py  # 版本
├── plugin   # 插件
│   ├── __init__.p      # 初始化
│   ├── mmdet3d_plugin  # 3d检测源码
│   ├── mmdet_plugin    # 2d检测源码
│   └── mmseg_plugin    # 分割源码
├── projects    # 项目
│   ├── det     # 2d检测
│   ├── det3d   # 3d检测
│   └── seg     # 分割
├── README.md
├── requirements    # 依赖
├── requirements.txt
├── setup.py    # 安装
├── tests   # 测试
│   ├── det     # 2d检测
│   ├── det3d   # 3d检测
│   └── seg     # 分割
└── tool    # 工具
    ├── det     # 2d检测
    ├── det3d   # 3d检测
    └── seg     # 分割
```

## Requirements
- CUDA=11.8
- Pytorch=2.0.0
- mmcv=2.0.0
- mmdet=2.0.0
- mmseg=1.0.0


## 环境搭建
### pytorch安装
```bash
conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia
```
### mmcv和mmengine安装
- mim安装
    ```bash
    pip install -U openmim
    mim install mmengine
    mim install mmcv==2.0.0
    ```
- pip安装    
    ```bash
    pip install mmcv==2.0.0 -f https://download.openmmlab.com/mmcv/dist/cu118/torch2.0/index.html
    ```
### mmdet安装
- pip安装    
*如果你将 mmdet 作为依赖或第三方 Python 包*
    ```bash
    mim install mmdet==2.0.0
    ```
- 源码安装    
*在需要修改源码时要用源码安装*   
    ```bash
    git clone https://github.com/open-mmlab/mmdetection.git
    cd mmdetection
    pip install -v -e .
    # "-v" 指详细说明，或更多的输出
    # "-e" 表示在可编辑模式下安装项目，因此对代码所做的任何本地修改都会生效，从而无需重新安装。
    ```

### mmseg安装   
- pip安装   
    *如果你将 mmseg 作为依赖或第三方 Python 包*
    ```bash
    pip install "mmsegmentation==1.0.0"
    ```
- 源码安装   
*在需要修改源码时要用源码安装*   
    ```bash
    git clone -b main https://github.com/open-mmlab/mmsegmentation.git
    cd mmsegmentation
    pip install -v -e .
    # '-v' 表示详细模式，更多的输出
    # '-e' 表示以可编辑模式安装工程，因此对代码所做的任何修改都生效，无需重新安装
    ```

### 验证安装
```bash
python -c 'import torch;print(torch.__version__);print(torch.version.cuda);print(torch.cuda.is_available())'
python -c 'import mmcv;print(mmcv.__version__)'
python -c 'import mmdet;print(mmdet.__version__)'
python -c 'import mmseg;print(mmseg.__version__)'
```

## 自定义模型


## 项目结构
