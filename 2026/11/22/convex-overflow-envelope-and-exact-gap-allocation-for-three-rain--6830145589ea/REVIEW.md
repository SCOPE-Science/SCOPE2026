# Scientific review

## Correctness — PASS
The exact three-pulse storage recurrence reduces to the four-branch envelope by splitting according to saturation at the second pulse. The envelope's component convexity proves global convexity in retention coordinates. Its switching points and sole smooth interior stationary point exhaust positive-spill minima; a separate pair of storage inequalities gives the full zero-spill optimal interval. The both-overflow regime and the unbounded equal-gap penalty follow by direct substitution. The supplied standalone rational checker corroborates the recurrence, envelope, convexity, boundaries, candidate minimizers, and examples; finite tests are not substituted for proof.

## Originality — PASS (provisional historical priority)
McGrath et al. (2007, public discussion 2006) and Bartlett et al. (2015) derive threshold runoff properties of stochastic rainfall/storage systems, not the fixed-endpoint three-event deterministic optimization. Miralles et al. (2010) use canopy interception modeling, and Xu et al. (2020) optimize active release rather than timing among three fixed natural inflows. The closest compared public exact mathematical results concern the permutation of three **equally spaced periodic pulses**, or the integer cyclic gap between **two equal periodic pulses**. Neither states or implies the present finite-horizon convex-envelope optimization with an initially empty store. Abstract finite-buffer scheduling/rearrangement theory is a residual possible source of stronger coverage; priority is not independently certified.

## Value — PASS
Short rainfall separations matter in saturation-excess models, and fixing both total rain and the overall time horizon isolates the question of allocating dry time. The four-branch envelope supplies a global classification rather than a local numerical schedule, the exact zero-overflow interval explains robustness where timing does not matter, and the interior square-root law identifies a non-obvious regime where balanced marginal drying beats either extreme. The unbounded penalty example rules out a constant-factor guarantee for evenly spaced times. No application to real storm control is asserted.

## Sources and residual limits
Full text of McGrath et al. (2007) was inspected, including its rainfall model, storage-threshold formulas, statistical conclusions, and appendix. Relevant mathematical results on periodic stores were read as complete primary result texts. Online sections and mathematical formulas of Bartlett et al. (2015), Miralles et al. (2010), and Xu et al. (2020) were compared; possible broader finite-buffer scheduling theorems remain a historical-priority risk. The model is scalar, passive, empty initially, and uses fixed positive depths and exponential loss.

Self-review: passed. Independent audit: not yet performed.
