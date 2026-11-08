# Mathematical review: price-ordered star pinning

## Correctness — PASS

For a pinned star, eliminating its positive leaf diagonal block yields the necessary and sufficient inequalities \(t_i>0\), \(t_i\ge 1-\lambda\) and \(u_0\ge \lambda-m+\sum_i t_i^{-1}\). Minimize the priced gains subject to these inequalities. Strict feasibility proves strong convex duality; the leaf minimizers of \(p_i t+\alpha/t\) are \(t_i=\max\{1-\lambda,\sqrt{\alpha/p_i}\}\), and the hub multiplier is in \((0,p_0]\). The dual derivative identifies the unique scalar root or endpoint. Positive Perron eigenvectors exclude different optimal gains; the convex epigraph yields concavity of the budget-to-rate curve. Fixed-price activation follows from monotonicity in the rate, and the full-activation affine formula follows by substitution. No finite enumeration is used to prove this all-parameter claim. The provided source script reproduces 14,549 supplemental rational and numerical checks; it cannot provide independent verification or substitute for the proof.

## Originality — PASS on inspected evidence, with qualification

The strongest matching antecedent is Li–Duan–Chen, *Cost and Effects of Pinning Control for Network Synchronization* (arXiv:0710.2716, 2007-10-15), whose public text gives star gain-cost criteria for a pinned hub or uniform leaf gains. Those specialized controls do not give an optimum over all independent gains with arbitrary positive per-vertex prices, and do not imply the present price-sorted phase classification. Zhou et al., *Enhancing speed of pinning synchronizability* (Scientific Reports 5, 17459, 2015), give an LMI approach to choosing pinning gains, so the general SDP is known; the full readable public text was limited, and possible exact special-case overlap remains a priority risk. Shafi–Arcak–El Ghaoui, *Graph Weight Allocation to Meet Laplacian Spectral Constraints* (IEEE TAC 2012), was inspected in full, including its mathematical optimization constraints: it varies edge weights and node masses rather than additive diagonal independent pinning gains. Orouskhani–Jalili–Yu, *Optimizing Dynamical Network Structure for Pinning Control* (2016), optimize an eigenratio and graph structure. Boyd (ICM 2006) provides the general convex spectral-design framework; this is expressly prior work. The 2007 Sorrentino et al. pinning-controllability paper gives general motivation, but only its abstract was materially inspected. No inspected source proves the precise arbitrary-price star theorem; publication priority still requires specialist verification.

## Mathematical value — PASS

The all-positive-price, all-budget and all-star-size classification solves a natural constrained spectral design problem. It replaces an SDP by nested scalar roots, proves uniqueness, specifies irreversible price-sorted leaf activation, separately tracks hub activation, and gives the exact high-budget linear regime and closed-form two-price transitions. These are useful structural design rules beyond the known fixed-hub or all-leaves strategies, not simply a single-instance calculation. The restriction to fixed stars and scalar pinned consensus limits the conclusion's generality appropriately.

## Limits and residual risks

The result does not cover directed, signed or non-unit spoke networks, gain caps, generalized masses, nonlinear plant models or general graphs. General convex SDP pinning allocation is already known. Access to a complete high-resolution rendering of the Zhou et al. article was limited, leaving a concrete specialist-priority risk. The finite verifier is not an independent audit.

Self-review: passed. Independent audit: not yet performed.
