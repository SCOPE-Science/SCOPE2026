# Self-review

## Correctness — PASS

The scalar projected row step has the exact reset identity \(u_{k+1}=d_{I_k}/s_{I_k}\). This makes the distribution independent of the initial feasible coordinate after one update. The exact absolute-moment sum is maximized in all observation errors by saturation. The subcritical divergence and critical upper bound follow directly. In the supercritical case strict Jensen concavity reduces an arbitrary set of row magnitudes to a one-parameter problem, and a strictly decreasing derivative sign expression certifies one global maximizer and every equality case. The complete matrix witness has a rank-one Gram update, explicit singular values and an exact two-atom iterate distribution. The checker replays exact-rational identities and a large finite sample of candidate geometry comparisons; the proof, not finite sampling, establishes all real exponents.

## Originality — PASS, with stated residual risk

Sun et al. (2026) establish projected randomized iterative methods on trusted subspaces. Lok and Rebrova (2023) already establish the projected squared-norm Kaczmarz rule and a mean-square error horizon for noisy data; those results are credited. The new scientific object is the **all-real-order sharp uniform moment profile across normalized deterministic projected rows**, including its unique maximizing geometry, critical exponent and exact single-corruption tail. The closest publicly indexed Gaussian-noisy-coefficient moment result uses a different probability model and threshold, while the cited noise-horizon theory does not provide this quantified minimax classification. The original 2023 source was inspected at its update, noisy theorem, and proof, not only by title. Unindexed equivalent stronger results or uninspected sections of other specialist papers remain possible; absence from a search is not taken as a proof of priority.

## Value — PASS

Classical squared-norm sampling is useful precisely because it damps weak projected rows. The theorem identifies its exact high-moment limit and gives a complete calibration criterion for any requested moment order, plus the worst coefficient geometry when the criterion holds. The embedded three-equation example has one bounded corrupted measurement and a uniformly well-conditioned original matrix, so the amplified tail cannot be dismissed as ordinary global matrix ill-conditioning. The structural minimax equality and the sharp tail are useful independently of a generalization to higher-dimensional free spaces.

## Scope and limitations

The scientific claim covers independent norm-power row draws and one remaining free coordinate, with exact arithmetic, finite fixed row count, and deterministic bounded response errors. It does not cover adaptive residual filtering, null-step rejection, or arbitrary-dimensional constrained Kaczmarz dynamics. Independent verification remains outstanding.

Self-review: passed. Independent audit: not yet performed.
