# Review: central-window degree law for random permutation graphs

## Correctness — PASS

For iid continuous vertex scores, the inversion-graph degree has an exact decomposition into a full-sample empirical-count difference plus a short prefix correction. Two half-sample empirical processes converge to a single standard Brownian bridge; deleting finitely many marked scores makes the process asymptotically independent of their iid uniform ranks. Because the marked positions are within order \(\sqrt n\) of the center, the prefix correction involves only order \(\sqrt n\) Bernoulli terms, with standard deviation of order \(n^{1/4}\); after division by \(\sqrt n\) it vanishes. The deterministic correction tends to \(t(1-2U)\). The exact probability kernel of one bridge gives variance \(1/6+t^2/3\) and covariance \(1/12\). The packaged standard-library verifier passed 186 finite assertions and the proof separately justifies the infinite limit.

## Originality — PASS, with residual priority risk

Bhattacharya–Mukherjee, arXiv:1503.03582 (2015), prove the one-point central degree limit and independent macroscopic degree proportions, not the joint central-window dependence theorem; Corollary 3.3, Theorem 3.4, and their proofs were read. Gürerk–Işlak–Yıldız, arXiv:1901.06678 (2019), independently give the one-point central limit and exact variance, not the joint marked limit; relevant theorem/proof sections were read. A published result on the incidence covariance and precision of inversion indicators (published-finding corpus 2026/10/4) implies finite degree covariances after aggregation, but not this non-Gaussian joint limiting law; its full result was read. Meaning-based published-finding and primary-literature searches did not identify a theorem with equivalent hypotheses and conclusion. An earlier under-indexed empirical-process coupling remains a reasonable historical-priority risk: absence of a hit alone is not priority proof.

## Value — PASS

The one-point central result does not measure cross-vertex dependence; covariance alone cannot identify a non-Gaussian joint limit. The theorem resolves the natural critical positional window where macroscopically separated labels have independent first-order limits but several near-central degrees share \(\sqrt n\)-scale fluctuations. A single common Brownian bridge yields an explicit and tractable joint sampling law for finitely many vertex degrees, with universal off-diagonal covariance and offset-dependent drift. This is a structural extension rather than a routine re-expression of a one-point formula.

## Limitations and closest literature

The number of marked vertices and the offsets are fixed. No process-level tightness for all window indices, no rate of convergence, and no nonuniform permutation analogue are claimed. The full historic literature cannot be exhaustively ruled out; the cited 2015 and 2019 preprints and the comparison-vector covariance record are the primary inspected nearest results. Independent expert validation remains outstanding.

Self-review: passed. Independent audit: not yet performed.
