# Self-review

**Correctness — PASS.** The proof establishes a positive edge resolvent via the tridiagonal \(M\)-matrix structure, obtains weighted column contraction from \(w^{\mathsf T}B\ge0\), factors arbitrary smooth convex two-input proximal differences by nonnegative divided differences, and handles finite nonsmooth convex energies by approximation. The gradient flow follows by an edge-space cooperative evolution or repeated implicit steps. One-edge quadratic data show sharp necessity; exact-rational checks in `check.py` supplement the proof.

**Originality — PASS with priority qualification.** The closest published tree-heat criterion has precisely the same path weight inequality for linear heat; that *linear* specialization is not claimed as new. The new assertion universally quantifies over every finite convex edge interaction and both proximal and nonlinear flow maps, including nonsmooth potentials, which is not stated or directly implied by the linear theorem. The inspected archival papers of Barbero–Sra (arXiv:1411.0589) and Kolmogorov–Pock–Rolínek (arXiv:1502.07770) give algorithms and formulation, not a sharp pairwise BV stability theorem. A possibly equivalent older nonlinear comparison result remains a residual risk.

**Value — PASS.** The result gives a practical local criterion for choosing *independent* variation metrics that resist perturbation amplification under all 1D convex edge denoisers/diffusions; exact necessity and the nonconstant admissible-weight example make it a complete structural classification rather than a routine single-operator bound.

**Limitations.** Finite real open paths, positive masses, positive variation weights and finite separable convex edge energies only. No infinite-path, tree/cycle, nonseparable or other-metric extension is claimed. The numerical checks cannot alone establish the universal theorem.

Self-review: passed. Independent audit: not yet performed.
