# embodied-ai-finetuning-openpi

Fine-tuning Physical Intelligence π-series models on LIBERO with RTX 4090.

## Hardware

- GPU: NVIDIA GeForce RTX 4090 24GB
- OS: Ubuntu 22.04
- Training mode: openpi JAX low-memory / LoRA fine-tuning

## Current Result

| Benchmark | Model Config | Checkpoint | Episodes | Successes | Success Rate |
|---|---|---:|---:|---:|---:|
| LIBERO Spatial | `pi0_libero_low_mem_finetune` | 7000 | 50 | 32 | 64% |

## Rollout Videos

Success and failure rollout videos are included under `assets/videos/libero_spatial_7000/`.

## Repository Scope

This repository tracks the fine-tuning workflow, evaluation results, and small rollout videos.

Large files such as full checkpoints, datasets, Weights & Biases runs, and training caches are not stored here.

## Status

- [x] Set up openpi on Ubuntu 22.04
- [x] Download LIBERO LeRobot dataset
- [x] Compute normalization statistics
- [x] Fine-tune `pi0_libero_low_mem_finetune`
- [x] Evaluate checkpoint `7000` on `libero_spatial`
- [x] Save success/failure rollout videos
