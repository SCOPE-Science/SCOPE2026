# Review: arithmetic single-vertex sensing on a one-defect diffusion ring

## Correctness

**PASS.** The full theorem covers every integer ring length at least five, every positive exceptional conductance, and every sensor location. The proof reduces the PBH condition to disjoint reflection parities outside the homogeneous case. The even-parity zeros give an exact gcd obstruction. A right-tail Dirichlet/antisymmetric Sturm recurrence gives an exhaustive finite sine-ratio exceptional-weight list for every remaining site. At half conductance on odd rings the odd Jacobi block is exactly Toeplitz Dirichlet, yielding the gcd rank deficiency and totient census. Exact fraction-Krylov checks pass 550 cases, with independent gcd/totient checks; they are supplementary, not a substitute for the proof. Residual correctness risk is that symbolic boundary and exceptional-parameter derivations have received only this mathematical review, not an independent audit.

## Originality

**PASS on the inspected comparisons, with publication-priority risk.** The 2011 uniform-cycle controllability theory proves no single sensor controls a homogeneous cycle, so it does not give an all-site heterogeneous design. Published one-defect results already give the exceptional-edge endpoint Kalman determinant and a complete inward-one-site resonance theorem: these cases are excluded from novelty claims. The new statement concerns every farther-inward location, a permanent reflection-even gcd obstruction, and the exact half-conductance totient census and unbounded rank losses. Grudsky–Maximenko–Soto-González (2022) give explicit eigenvectors of precisely this matrix; their full paper was inspected, including the main eigenvector result and general Chebyshev formulas. Such a spectral formula supplies a route to the present classification, but the inspected material does not state its precise PBH site-weight phase diagram or arithmetic placement count. This close relation is a genuine risk that an unindexed derivative result may already exist. The checked results are not proof of uniqueness or worldwide priority.

## Value

**PASS.** A single edge defect is a natural symmetry-breaking intervention for diffusion and leader selection. The theorem determines *all* viable single-coordinate locations for a fixed ring and edge weight, including countably many exact resonances rather than merely the generic fact that nonunit weights break symmetry. The half-conductance totient law quantifies how many sensors remain effective; the gcd deficiency shows that a single unlucky placement can lose an arbitrarily large number of independent modes even though a one-coordinate placement elsewhere remains fully controllable. These are structural and arithmetic design facts, not a numerically tabulated special case.

## Closest literature and limitations

- Parlangeli and Notarstefano, arXiv:1109.3556v1 (2011): uniform path and cycle observability; full primary article inspected.
- Grudsky, Maximenko and Soto-González, arXiv:2205.12457v1 (2022): the same weighted cycle's spectrum and explicit eigenvectors; full primary article inspected; most important priority risk.
- Public exact reachability-volume factorization on the one-weighted-edge cycle (2026): endpoint case already known; full RESULT.md inspected.
- Public one-vertex-inward resonance classification on the singly weighted cycle (2026): \(j=1\) already known; full RESULT.md inspected.

The result concerns binary noiseless single-coordinate observability/controllability, not Gramian conditioning or uncertain weights. Full publication priority is not independently certified.

Self-review: passed. Independent audit: not yet performed.
