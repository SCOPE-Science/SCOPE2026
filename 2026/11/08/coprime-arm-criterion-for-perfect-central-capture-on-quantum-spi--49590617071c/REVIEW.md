# Scientific review: Coprime-arm criterion for perfect central capture on quantum spiders

## Correctness — PASS

The infinite-family proof is analytic and self-contained. Every undamped state is exactly a zero-amplitude-at-hub eigenvector of the Hermitian adjacency Hamiltonian, because the orthogonal complement is strictly dissipative. Dirichlet arm spectra are indexed by reduced fractions \(a/b\), and equality of two arm eigenvalues requires the same reduced fraction. In each spectral sector, the hub equation removes exactly the normalized inverse-square-root-length direction. This yields the totient dimension, complete-capture criterion, full projector, and site-probability formula. The proof explicitly requires a nonzero uniform hopping, one center absorber of strictly positive rate, a uniform on-site shift, and finite arms.

Exact integer walk-matrix ranks checked 145 spider graphs; an independent full eigenspace projector implementation checked 145 graphs and every vertex, with a maximum diagonal discrepancy below \(10^{-14}\). Twelve direct lossy propagations at finite time also agreed within specified tolerance. The infinite result does not rely on sampling or on numerical extrapolation. See `verify_arithmetic.py`, `verify_projector.py`, and `VERIFICATION.md`.

## Originality — PASS on examined evidence, provisional

The general invariant-subspace method of Caruso et al. (arXiv:0901.4454) is prior work and is not claimed as new. Yalouz and Pouthier (DOI:10.1103/PhysRevE.97.022304) examine a two-generation symmetric dendrimer-like star, which has a different network construction from arbitrary unequal linear arms. Vieira and Amorim (arXiv:2404.04094) study weighted equal-length spiders and short-time root-occupation suppression, not the permanent survivor projector under irreversible loss. Their inspected material does not imply the displayed all-arm gcd criterion and every-site formula. The elementary Dirichlet path spectrum and spectral PBH-style argument are standard and likewise not claimed as new. No equivalent of the combined unequal-arm classification was found in the comparison of source texts and available mathematical records.

Residual priority risk remains: an equivalent formulation could occur under vertex controllability, quantum network observability, or discrete-tree eigenspace terminology, including sources not available in full text. No absolute novelty or independent-priority certification is asserted.

## Mathematical value — PASS

Single-site coherent trapping on branched transport networks has a natural design question: exactly when does symmetry or eigenfrequency coincidence protect a nonzero excitation subspace? The answer for **all** unequal-length spiders is an elementary arithmetic criterion with no finite-size exceptions, and it gives the exact dimension and the location-dependent leakage probability. Pairwise-coprime augmented arm lengths give perfect capture, whereas a single shared divisor creates a dark mode. This is a complete natural infinite-family classification, not an arbitrary small-graph enumeration. It also explains the known equal-arm limit and shows how asymmetry can remove all protected modes without adding any absorbers.

## Closest sources and boundaries

- Caruso et al., 2009, arXiv:0901.4454: general local-trap dark-state analysis; not an unequal-arm star arithmetic classification.
- Yalouz and Pouthier, 2018, DOI:10.1103/PhysRevE.97.022304: two-generation dendrimer-like extended star; not this graph family.
- Vieira and Amorim, 2024 original posting, arXiv:2404.04094: symmetric weighted spider, transient root occupation; not this permanent-capture classification.
- Dáger, 2004, DOI:10.1137/S0363012903421844: continuum strings with boundary control, not the discrete uniform-adjacency irreversible trap. Full text was not verified and transferable priority remains a limited residual risk.

The result does not address finite-time optimality, nonuniform arm couplings, onsite disorder, multiple traps, or decoherence. Independent validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
