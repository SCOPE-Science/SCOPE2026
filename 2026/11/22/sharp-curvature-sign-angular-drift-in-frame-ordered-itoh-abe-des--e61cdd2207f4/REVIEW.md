# Scientific review

## Correctness — PASS
The claim uses the genuine centered Riemannian Itoh–Abe quotient from Zhou's equations (20)–(21), with center equal to the old point. On a constant-curvature surface the exact Hessian eigenvalues of the squared radial distance are \(1\) and \(rS_K'(r)/S_K(r)\). Expansion of the two coordinate quotients gives the lower-triangular half-Hessian map and a transverse defect \(r(1-q_K(r))\sin(2\theta)h^2/4\). The discrete polar geometry and radius recurrence convert the local transverse error into an explicit Riemann sum; an exact total derivative gives the announced fixed-time coefficient. The symmetric order average has half the Hessian and vanishing transverse term; at the bisector, the two path corners reflect and have equal radial energy, giving an exact radial midpoint step. The exact symbolic and finite numerical diagnostics passed; these finite experiments are not the proof. The proof explicitly restricts to a uniquely selected small-step branch.

## Originality — PASS (qualified)
The 2026 primary paper's entire accessible text, including statements and appendices, covers the method and broad curvature-aware convergence but not the signed asymptotic angle coefficient. The 2018 dissipative paper establishes the original Riemannian Itoh–Abe method. Critically, the 2018 energy-preserving paper ALREADY establishes endpoint-reversal symmetrization, which equals order averaging at the same fixed exponential center. Therefore neither that construction nor generic symmetry order improvement is claimed new. The distinctive complete claim comprises the sharp curvature-sign/frame-orientation law and exact bisector radial midpoint realization. Relevant indexed mathematical records were compared by scientific implication and no covering result was found, but a search cannot prove historical novelty. Related curvature or Riemannian optimizer claims that do not analyze the same discrete-gradient normal-coordinate error are not covering. Residual risk: an unindexed numerical-analysis treatment of this specific test may have derived a similar formula.

## Value — PASS
The geodesic squared-distance problem is the canonical strongly geodesically convex test objective within the spherical convex hemisphere and on Hadamard space forms. The result isolates a frame-dependent *directional* bias not described by generic energy descent or function-value rates and reveals an orientation achieving worst signed bias. The exact bisector identity supplies a meaningful, curvature-independent design/verification benchmark and distinguishes energy preservation, angular fidelity, and exact radial flow. It is a precise motivated error law, not an arbitrary numerical counterexample.

## Closest literature and limits
- Zhou, 2026, arXiv:2608.21862v1, §§5–6 and appendices: method and general curvature-aware rates; no explicit polar phase coefficient.
- Celledoni et al., 2018, arXiv:1804.08104, §3.1: base Itoh–Abe Riemannian optimization scheme, no space-form angular law.
- Celledoni et al., 2018, arXiv:1805.07578, §3.2: **pre-existing symmetrized Itoh–Abe**, acknowledged and not treated as novel.
- Riis et al., DOI:10.1007/s10208-020-09489-2: rotated-direction and nonsmooth discrete-gradient optimization, but not a constant-curvature angular defect.

No independent mathematical audit was performed. General variable-curvature laws and nonlinear implicit-branch global uniqueness remain unproved.

Self-review: passed. Independent audit: not yet performed.
