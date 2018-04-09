# ImageCLEF: Brown University

## Installation on CCV
```
# Make sure Anaconda is loaded 
module load anaconda/2-4.3.0
conda create -n caption 
source activate caption
conda install pytorch
conda install -c soumith torchvision
conda install h5py
```

## To train 
Request GPU node. Activate virtual environment. Go into ImageCaptioning.pytorch and run:

```
python train.py \
--id imageclef-topdown \
--caption_model topdown \
--input_json /gpfs/data/ceickhof/imageclef/data/imagecleftalk2.json \
--input_image_h5 /gpfs/data/ceickhof/imageclef/data/imagecleftalk_image.h5 \
--input_label_h5 /gpfs/data/ceickhof/imageclef/data/imagecleftalk_label.h5 \
--batch_size 10 --finetune_cnn_after 10 --learning_rate 5e-4 \
--learning_rate_decay_start 0 --scheduled_sampling_start 0 \
--checkpoint_path log_imageclef-topdown \ # make sure this directory exists
--save_checkpoint_every 6000 \
--cnn_model resnet101 \
--cnn_weight /gpfs/data/ceickhof/imagenet_weights/resnet101.pth \
--val_images_use 10000 \
--max_epochs 25
```
