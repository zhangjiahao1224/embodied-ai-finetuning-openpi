# LIBERO Spatial Quick Evaluation: pi0_libero_low_mem_finetune @ 5000 steps

## Setup

- Model config: `pi0_libero_low_mem_finetune`
- Experiment name: `pi0_libero_4090_lora`
- Checkpoint: `5000`
- Benchmark: `libero_spatial`
- Trials: 1 rollout per task
- Total tasks: 10
- Seed: 7
- Rendering backend: GLX

## Result

| Metric | Value |
|---|---:|
| Successes | 4 |
| Episodes | 10 |
| Total success rate | 40% |
| Evaluation time | 1m 29s |

## Per-task result

| Task | Result |
|---|---|
| pick up the black bowl between the plate and the ramekin and place it on the plate | Success |
| pick up the black bowl next to the ramekin and place it on the plate | Success |
| pick up the black bowl from table center and place it on the plate | Failure |
| pick up the black bowl on the cookie box and place it on the plate | Failure |
| pick up the black bowl in the top drawer of the wooden cabinet and place it on the plate | Failure |
| pick up the black bowl on the ramekin and place it on the plate | Failure |
| pick up the black bowl next to the cookie box and place it on the plate | Success |
| pick up the black bowl on the stove and place it on the plate | Failure |
| pick up the black bowl next to the plate and place it on the plate | Success |
| pick up the black bowl on the wooden cabinet and place it on the plate | Failure |

## Interpretation

This is a smoke test with only one rollout per task. It verifies that checkpoint 5000 loads and runs end-to-end, but the 40% result should not be treated as a statistically reliable comparison with the 7000-step evaluation, which used five rollouts per task.
