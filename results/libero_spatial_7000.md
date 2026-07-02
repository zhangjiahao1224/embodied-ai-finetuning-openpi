# LIBERO Spatial Evaluation: pi0_libero_low_mem_finetune @ 7000 steps

## Setup

- Model config: `pi0_libero_low_mem_finetune`
- Experiment name: `pi0_libero_4090_lora`
- Checkpoint: `7000`
- Benchmark: `libero_spatial`
- Trials: 5 rollouts per task
- Total tasks: 10
- Total episodes: 50

## Result

| Metric | Value |
|---|---:|
| Successes | 32 |
| Episodes | 50 |
| Total success rate | 64% |

## Per-task success rate

| Task | Success rate |
|---|---:|
| pick up the black bowl between the plate and the ramekin and place it on the plate | 80% |
| pick up the black bowl next to the ramekin and place it on the plate | 100% |
| pick up the black bowl from table center and place it on the plate | 60% |
| pick up the black bowl on the cookie box and place it on the plate | 80% |
| pick up the black bowl in the top drawer of the wooden cabinet and place it on the plate | 40% |
| pick up the black bowl on the ramekin and place it on the plate | 60% |
| pick up the black bowl next to the cookie box and place it on the plate | 40% |
| pick up the black bowl on the stove and place it on the plate | 60% |
| pick up the black bowl next to the plate and place it on the plate | 20% |
| pick up the black bowl on the wooden cabinet and place it on the plate | 100% |
