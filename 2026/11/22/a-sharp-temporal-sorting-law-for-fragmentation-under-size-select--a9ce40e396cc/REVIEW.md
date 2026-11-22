# Scientific assessment

## Correctness — PASS

For every cap \(J\ge1\), survival profile \(s_j\in(0,1]\), episode fraction \(p\in[0,1]\), and nonnegative initial mass vector, the linear transition is specified in `RESULT.md`. Direct matrix multiplication proves that the sole nonzero entries of the adjacent-swap commutator have value \((p-q)s_{j+1}(s_j-s_{j+1})\). All transitions are nonnegative, so the sign survives multiplication by arbitrary common prefix and suffix products. A finite sequence of adjacent swaps then proves global size-resolved optimality for all schedules. The converse uses initial mass in exactly one class and two episodes; it also covers the constant and nonmonotone cases. The standalone exact-rational verifier passed 28153 checks. Finite checks are corroboration, not the proof.

## Originality — PASS on inspected evidence

Actual comparisons included the full accessible arXiv manuscript arXiv:2307.04162 (especially the model, its inflation discussion, and Appendix A), marine fragmentation-and-transport work from 2022, size-dependent sinking work from 2021, and the prior literature on stochastic rearrangement and killed birth–death chains. Earlier results cover fragmentation recurrence, loss processes, and broad rearrangement techniques, but the inspected statements do not present this precise *componentwise, every-schedule, necessary-and-sufficient* ordering classification for a capped mass cascade. Research-record similarity searches for fragmentation, stochastic matrix interchange, and monotone killing returned no corresponding claim. The older general scheduling paper and some environmental articles could not be inspected completely; mathematical priority remains provisional rather than certain.

## Value — PASS

The theorem makes a structural prediction for coupled breakdown-and-sinking models: when smaller fragments are removed more efficiently, shifting high-fragmentation years later improves the remaining mass in every resolved class, not only the total. The sharp converse identifies exactly which survival patterns support the rule and when an order-independent baseline is valid. This is a meaningful classification of a physically motivated family of models, not a claim about measured pollution or clinical/ecological safety.

## Scientific limitations

This is an expected-mass, homogeneous-within-episode, single-batch, discrete-time model with stationary class-dependent loss and an absorbing lowest size class. Non-monotone retention, new sources, size-dependent break probabilities, interactions and coastal mixing lie outside the proved universal schedule claim. Some relevant older mathematical work is abstract-access only, so independent historical-priority examination remains worthwhile.

Self-review: passed. Independent audit: not yet performed.
