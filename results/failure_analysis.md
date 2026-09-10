# Qualitative failure analysis

This note separates the statistically stronger checkpoint-7000 measurements from qualitative observations made from checkpoint-5000 smoke-test videos.

## Quantitative signal from checkpoint 7000

The full evaluation completed five rollouts for each of ten tasks. Performance was strongest when the bowl was next to the ramekin or on the wooden cabinet (100%) and weakest when it was next to the plate (20%). The top-drawer and next-to-cookie-box conditions both reached 40%.

This distribution suggests sensitivity to local geometry rather than a complete failure to understand the instruction: the same pick-and-place goal can be solved reliably in some initial arrangements and inconsistently in others.

## Observations from checkpoint 5000 rollouts

Six of the ten smoke-test rollouts failed. Visual inspection of the recorded trajectories suggests three recurring patterns:

| Failure pattern | Visual evidence | Example conditions |
|---|---|---|
| Approach without a stable grasp | The gripper reaches the bowl area but does not establish or maintain a usable grasp before the horizon ends. | Table center, top drawer, stove |
| Contact that displaces the object | The end effector contacts the bowl or its support and changes the scene without transitioning into a controlled lift. | Cookie box, wooden cabinet |
| Incomplete transport or placement | The policy manipulates or moves the target but does not complete placement on the plate within the episode. | Ramekin and some displaced-object cases |

These labels are trajectory-level interpretations, not automated failure annotations. Each checkpoint-5000 condition has only one rollout, so they should be used to form debugging hypotheses rather than to estimate failure frequencies.

## Most useful next experiments

1. Record gripper state and end-effector pose alongside the videos to distinguish missed grasps from unstable lifts.
2. Re-run the three lowest checkpoint-7000 tasks with more initial states to determine whether the weakness is systematic.
3. Compare action replanning intervals while keeping checkpoint, seed set, and initial states fixed.
4. Track failure stage explicitly: approach, grasp, lift, transport, and placement.

