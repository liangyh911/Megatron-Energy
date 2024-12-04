#!/bin/bash

docker run --ipc=host --shm-size=512m --gpus all -it --rm -v ./DeepSpeed:/workspace/deepspeed -v ./Megatron-DeepSpeed:/workspace/megatron-deepspeed -v ./Megatron-LM:/workspace/megatron -v ./data:/workspace/dataset -v ./checkpoints:/workspace/checkpoints nvcr.io/nvidia/pytorch:24.02-py3

# pip install deepspeed
cd deepspeed
pip install . 

cd ../
pip install transformers
cd megatron-deepspeed
pip install -e . 

pip install nltk
python -c "import nltk; nltk.download('punkt_tab')"
pip install zeus-ml
pip uninstall pynvml
pip install nvidia-ml-py

cd examples_deepspeed/rebase/output
rm -r *
cd ../
bash ds_pretrain_gpt_125M.sh

cd examples_deepspeed/rebase
rm -r ./output/checkpoint ./output/tensorboard ./output/log
bash ds_pretrain_gpt_125M.sh

cd examples_deepspeed/bert_with_pile
bash ds_pretrain_bert.sh
