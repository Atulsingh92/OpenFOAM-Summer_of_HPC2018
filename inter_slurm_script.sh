#!/bin/bash
#SBATCH --time 23:58:00   ###default is 30 minutes
#SBATCH -N 30 --tasks-per-node=16 --mem=110000
#SBATCH -A SoHPC_hpc18
#SBATCH -p gll_usr_prod  ### specify a partition on galileo for running in parallel  (gll_usr_gpuprod for gpu jobs)
#SBATCH --job-name=Ctredd2
#SBATCH -o test-%j.out

module use /galileo/prod/spack/v001/RCM_spack_deploy/deploy/galileo_dev00/insitu01/spack/share/spack/modules/linux-centos7-x86_64
#Dambreak case runs fine for alplawater and velocity with of-catalyst/1806-gcc-7.3.0-kb, not the sou case!!
module load of-catalyst/1806-gcc-7.3.0-3w
#rm -r processor*
#rm -r insitu
#cp -r 0.orig/. 0

START=$(date +%s)
#setFields
#decomposePar
orterun -np 480 interFoam -parallel
END=$(date +%s)
echo $((END-START)) | awk '{print int($1/60)"m:"int($1%60)}'
