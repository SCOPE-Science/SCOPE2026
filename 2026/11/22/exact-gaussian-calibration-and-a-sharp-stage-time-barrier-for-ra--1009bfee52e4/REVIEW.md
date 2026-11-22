# Scientific review

## Correctness — PASS

The step is a random affine Gaussian transition with a **shared** intermediate/end Brownian increment. The identity
\[\mathbb E[P(U)A^{-1}P(U)^\mathsf T+Q(U)]-A^{-1}=h^2A[(1-2m_1)I+h^2m_2A^2]\]
is reconstructed from the joint increment covariance, not from independent-stage noises. Its eigenvalue conditions force isotropy for target covariance. The scalar stage polynomial is strictly positive above the threshold, and at the threshold the only zero becomes a nonergodic identity map. Below the threshold the multipliers are uniformly contracting and both deterministic and nonconstant covariance-calibrated laws exist. Gaussian-mixture fourth moments establish exact-law uniqueness and a strictly positive cumulant for any nonconstant calibrated law. Elementary differentiation proves the unique contraction optimum. Exact rational checks and the independent fourth-moment recursion in `verify.py` passed; see `checks.txt`. No finite sample count is used to justify a universal theorem.

## Originality — PASS, with historical-priority risk

The source algorithm is the uniform-stage overdamped RLMC update in He–Balasubramanian–Erdogdu (arXiv:2011.03176, Section 2), which analyzes ergodicity and stationary bias, but does not give a general stage-law calibration, covariance-impossibility threshold, calibrated fourth cumulant, or finite-step exact Gaussian mixing optimum. Shen–Lee (arXiv:1909.05503) addresses a different underdamped algorithm. Laurent–Vilmart (arXiv:1707.02877) develops invariant-measure order conditions, but these do not state or imply the precise finite-step stage-law classification without a separate computation.

Two highly relevant public comparative results were inspected in detail: *Harmonic equilibrium bias and a one-gradient covariance obstruction for randomized ULMC* treats an underdamped position–momentum map and an order-two small-step obstruction; *Spectral minimax calibration and unavoidable fourth-order dependence in random-order Langevin splitting* treats exact-drift/random-order splitting with different noise maps and cannot imply the present stage-law identity. Similarities in Gaussian-mixture principles and anisotropic impossibility are acknowledged. Searches over aliases, stage moments, invariant covariance, exact tables and stronger schemes disclosed no covering statement. Historical equivalence remains a publication-priority risk, not a certified absence.

## Value — PASS

The Gaussian stationary-law bias of randomized midpoint Langevin discretization is a mathematically motivated algorithm-design problem, rather than an arbitrary numerical slice. The theorem resolves an exact decision for **every** common stage-time distribution: a sharp \(h\lambda<1\) feasible window, a necessary isotropy condition, the unique full-law-preserving stage, and a quantitative demonstration that exact covariance does not ensure a Gaussian invariant law. The optimal per-step contraction \(2-\sqrt2\) identifies the nontrivial interior best tuning within the unbiased family. Its limitations are explicit: general nonlinear samplers and runtime efficiency are not covered.

## Residual limitations and independent review

Relevant general invariant-measure literature may contain an earlier unindexed specialization, and two broad comparison papers were available mainly at the abstract/introduction level. The proof is exact for a narrowly specified family and does not establish general-purpose MCMC superiority. A mathematically independent audit and specialist publication-priority examination have not been performed.

Self-review: passed. Independent audit: not yet performed.
