# Run this from ImageCaptioning.pytorch root directory
python scripts/prepro_labels.py --input_json /gpfs/data/ceickhof/imageclef/data/dataset_imageclef.json --output_json /gpfs/data/ceickhof/imageclef/data/imagecleftalk.json --output_h5 /gpfs/data/ceickhof/imageclef/data/imagecleftalk

python scripts/prepro_images.py --input_json /gpfs/data/ceickhof/imageclef/data/dataset_imageclef.json --output_h5 /gpfs/data/ceickhof/imageclef/data/imagecleftalk --images_root /gpfs/data/ceickhof/imageclef/data/CaptionTraining2018


