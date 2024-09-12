srun -K --ntasks=1 --gpus-per-task=1 -N 1 --cpus-per-gpu=20 -p A100-40GB --mem=50000 \
  --container-mounts=/netscratch/naeem:/netscratch/naeem,/home/iqbal/Mask2Former:/home/iqbal/mask2former \
  --container-image=/netscratch/naeem/mask2former_24.08.sqsh \
  --mail-type=END --mail-user=naeem.iqbal@dfki.de --job-name=mask2former_pheno \
  --container-workdir=/home/iqbal/mask2former \
  --time=02-00:00 \
  bash ./scripts/train_mask2former.sh
