srun -K --ntasks=1 --gpus-per-task=1 -N 1 --cpus-per-gpu=10 -p A100-IML --mem=50000 \
  --container-mounts=/netscratch/naeem:/netscratch/naeem,/home/iqbal/Mask2Former:/home/iqbal/mask2former \
  --container-image=/netscratch/enroot/nvcr.io_nvidia_pytorch_24.08-py3.sqsh  \
  --container-save=/netscratch/naeem/mask2former_24.08.sqsh \
  --time=00-02:00 \
  --pty /bin/bash
