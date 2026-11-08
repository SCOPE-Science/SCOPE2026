# Scientific review: Exact critical occupation polynomial of a dodecahedral Potts antiferromagnet

## Correctness — PASS

For the 20-vertex cubic dodecahedron the twelve odd pentagonal faces give the two-state lower bound six; a stated vertex coloring achieves it. Recoloring state 3 increases monochromatic edges by at most one per recolored vertex, so b+k>=6. An explicit 81-state cyclic transfer with weights for exactly the 30 edges and 20 spins is bijective with all 3^20 labelled configurations; exact coefficient extraction at degree six gives the asserted seven integers. An independently coded complete depth-first enumeration matches every coefficient, and a zero-monochromatic-edge transfer gives all proper-coloring sectors. Finally for h=1+x/beta all b+k>=7 contributions are O(e^{-beta+20|x|}), proving locally uniform scaling and the stated occupation moments. Finite testing is a reproducible evaluation of an exact finite recurrence, not a claim to prove an infinite pattern.

The exact count is reproducible with `python3 verify.py` from the delivered source. Both exact-integer transfer and independent vertex recursion yield `(250, 3000, 13800, 30400, 32760, 15840, 2720)`. The analytic limit uses the strictly positive integer energy gap and a finite number of states. These tests do not prove results outside the specified 20-vertex graph.

## Originality — PASS (qualified)

The 2026 source proves the universal subcubic ground-energy law and recoloring structure; these are explicitly credited. The 2010 generalized-field Potts graph partition function already encodes all coefficients implicitly, but its evaluated graph families do not include a dodecahedral critical mixed-sector polynomial. The dodecahedron chromatic polynomial and the proper-coloring total are already tabulated, and not claimed new. The newly isolated claim is the exact seven coefficients for fixed b+k=6 and the resulting occupation scaling function; targeted literature, direct primary-full-text, and indexed mathematical-result searches did not find an explicit equivalent. An unindexed table or a stronger graph-specific external-field calculation remains possible; this is best-knowledge, not an independence or priority certificate.

The nearest prior work is Choi et al. (2026), arXiv:2610.41277v1, which already establishes the energy threshold; Shrock and Xu (2010), arXiv:1009.1182v1, which already give generic field-dependent Potts partition functions; and Chang (2001), doi:10.1016/S0378-4371(01)00157-1, which treats generalized-dodecahedron proper-coloring polynomials. The published chromatic polynomial for the ordinary dodecahedron is also acknowledged. None of those available statements specifies the seven mixed-error/occupation coefficients of this evaluated field-degenerate C20 model. The residual risk of an unlocated equivalent coefficient table is real.

## Value — PASS

The dodecahedron is the canonical smallest fullerene connectivity graph and a natural 20-site frustrated cubic spin cluster. The recent threshold theorem specifies an energy but does not quantify the large mixture of distinct defect-occupation sectors at the threshold. The explicit polynomial gives the finite-size residual entropy log(98770), the full field rounding, and a fixed benchmark for occupation fluctuations and numerical exact partition functions. The seven-sector distribution has nontrivial shape and cannot be recovered from the ground-energy formula or unweighted chromatic count alone. This is a motivated exact finite invariant, not a claim of a macroscopic phase transition or a generic new transfer-matrix method.

The most useful future application is as a stringent exact finite-size benchmark for third-state occupancy, entropy and susceptibility at the field-selection crossing. No extrapolation to a thermodynamic-limit phase transition is justified.

## Limitations and review status

The model is the specific three-state Potts Hamiltonian with a unit monochromatic-edge penalty, not a physically distinct neutral-state interaction. A general result supplies an exact encoding of this invariant, and the precise numerical table may exist elsewhere; the claimed scientific contribution is the graph-specific evaluation and crossover. Full independent validation remains outstanding.

Self-review: passed. Independent audit: not yet performed.
