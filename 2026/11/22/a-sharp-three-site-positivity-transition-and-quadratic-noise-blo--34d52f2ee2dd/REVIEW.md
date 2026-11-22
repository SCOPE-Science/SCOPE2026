# Review of the three-site Fourier quadrature transition

## Correctness (C): PASS

The claim is exact for every odd grid size \(N\ge3\) and every strictly separated displacement \(0\le u<1\). The Fourier cardinal-function update computes the complete quadrature weights with a positive denominator. Strict convexity and reflection of the cosecant function show that all weights except the middle one stay positive. A strict monotonicity argument gives the unique middle-weight crossing. Taylor expansion at the crossing proves the second-order large-grid correction, and a separate fixed-grid expansion at triple coalescence proves quadratic divergence with its exact coefficient. The reproducibility program passed 7,820 numerical consistency assertions, and selected cases were compared against direct Fourier-Vandermonde inversion. These finite computations supplement, not replace, the proof. The coalesced endpoint itself is excluded.

## Originality (O): PASS, best-knowledge

Austin's thesis [1], Chapter 3.5.2, and Austin–Trefethen [2] study quadrature over perturbed periodic grids; neither inspected section contains this sharp all-odd-grid two-moving-site classification. Yu–Townsend [3], Theorem 4.1 and Appendix B, establishes negativity through alternating perturbation of many sites; its estimates neither imply that exactly one weight changes sign for this local deformation nor evaluate the present threshold and quadratic collision coefficient. A published study of an adjacent-pair inward collision [4] gives *opposite* positivity behavior, but for only two coalescing observations and a different geometry. The published three-node random-jitter quadrature law [5] covers the general three-point positivity criterion; accordingly, the smallest-grid instance by itself is **not** claimed new. The assessed contribution is the complete all-odd-grid structural classification and exact large-grid/collision laws. Potential older special-function formulas and unpublished parameter studies remain a priority risk.

## Value (V): PASS

Positive quadrature weights give optimal norm-one stability against bounded sample errors, so the exact point where positivity disappears is a natural and useful numerical invariant, not an arbitrary parameter slice. Changing only two nodes, and leaving the middle one fixed, isolates the first local three-site crowding mechanism. The theorem determines which weight becomes negative, proves a sharp universal limit \(1-1/\sqrt2\) with finite-resolution correction, and quantifies an exact quadratic instability that contrasts with the stable double-collision geometry. This has intrinsic value as a sharp boundary in nonuniform Fourier sampling; no broader interpolation convergence theorem is asserted.

## Prior sources and limitations

[1] A. P. Austin, *Some New Results on and Applications of Interpolation in Numerical Computation*, Oxford thesis (repository deposit 2016-12-08), Chapter 3.5.2. https://personal.math.vt.edu/apaustin/pubs/DPhilThesis.pdf

[2] A. P. Austin and L. N. Trefethen, *Trigonometric Interpolation and Quadrature in Perturbed Points*, arXiv:1612.04018v1 (2016-12-13), Sections 1–2. https://arxiv.org/pdf/1612.04018

[3] A. Yu and A. Townsend, *On the Stability of Unevenly Spaced Samples for Interpolation and Quadrature*, arXiv:2202.04722v1 (2022-02-09), Sections 4.1–4.2 and Appendix B. https://arxiv.org/pdf/2202.04722

[4] *Positive Fourier quadrature survives symmetric pair collision with a sharp singular-value law*, public mathematical finding (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-positive-fourier-quadrature-survives-symmetric-pair-collision-wi--92a65f43a0d4

[5] *Sharp positivity and logarithmic noise barrier in three-node perturbed trigonometric quadrature*, public mathematical finding (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-sharp-positivity-and-logarithmic-noise-barrier-in-three-node-per--fd84114e8959

Self-review: passed. Independent audit: not yet performed.
