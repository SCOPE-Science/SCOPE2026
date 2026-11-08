# Scientific review

## Correctness — PASS

The full weighted Laplacian is block-diagonalized by the natural clique and independent-part permutation representations, giving eigenvalues \(0\), \(px\), \(qx+py\), and \((p+q)x\) with their exact positive multiplicities. Rayleigh-quotient concavity under automorphism averaging establishes that the two-variable optimization covers the unrestricted rate assignment. The remaining linear program is solved on its feasible lower boundary, including strict inequality and tie cases. Exact-arithmetic recomputation in `verify.py` checks 720 parameter cases and 72,720 rational alternatives, but the infinite proof is analytic.

## Originality — PASS, with priority limitations

The closest established full-text source is Sun–Boyd–Xiao–Diaconis (2006), which sets up the general continuous-time semidefinite program and solves other examples; the present split-graph two-price closed form and critical ratio are not stated there. Jafarizadeh (2015) analyzes other structured continuous-time networks, and Boyd–Diaconis–Xiao (2004) concerns the discrete-time SLEM problem. A related previous complete-split discrete-time SLEM characterization does not determine a continuous-time optimum under two independent rate prices. Mathematical implication, not wording, is the basis of comparison. A domain-specific unindexed exact formula remains a priority risk.

## Value — PASS

Complete split graphs are canonical clique-plus-periphery networks. The exact all-integer, all-positive-price solution identifies when extra clique edges should receive **zero** mixing budget and when investment in them has unbounded relative value as the imbalance grows. The critical ratio and continuum of optimal designs at equality give a natural, closed phase diagram rather than an arbitrary numerical slice.

## Limits and references

This result does not classify nonsymmetric optimal assignments or solve the discrete-time fastest-mixing problem. Principal references: Sun et al., SIAM Review 48(4), 681–699 (2006), DOI:10.1137/S0036144504443821; Boyd et al., SIAM Review 46(4), 667–689 (2004), DOI:10.1137/S0036144503423264; Jafarizadeh, arXiv:1509.05823 (2015).

Self-review: passed. Independent audit: not yet performed.
