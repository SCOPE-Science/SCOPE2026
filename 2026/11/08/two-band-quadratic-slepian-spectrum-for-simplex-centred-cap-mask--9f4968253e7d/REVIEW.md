# Scientific review

## Correctness — PASS

For probability-normalized surface measure the global quadratic-harmonic norm is \(2\operatorname{tr}(AA^\ast)/[d(d+2)]\). The cap fourth moment decomposes into a scalar Frobenius term, the \(Av\) term, and the coefficient \(b_d(a)(v^{\mathsf T}Av)^2\). A directly differentiated zonal quartic primitive gives the stated explicit factor \(a(1-a^2)^{(d-1)/2}(a^2-3/(d+4))\). The regular-simplex tight-frame identity removes the \(Av\) anisotropy, while the trace-free projectors of the vertices have Gram spectrum \(0\) once and \((d^2-1)/d^2\) exactly \(d\) times. The spherical harmonic addition theorem fixes the common scalar, yielding both eigenvalues and exact multiplicities. Comparing the quartic zero with the disjointness threshold proves the tetrahedral-only interior isotropy; Funk--Hecke integration verifies the stated nonzero cubic moment. The symbolic/algebraic and independent cap-quadrature program in check.py replayed with 260 successful checks. The finite program supports, but does not replace, the dimension-uniform proof.

## Originality — PASS (provisional historical comparison)

The general arbitrary-region spherical Slepian eigenproblem and the axisymmetric single-cap analysis were already established by Simons, Dahlen, and Wieczorek (arXiv:math/0408424, particularly Sections 4–5). The incomplete-region construction of Roddy and McEwen (arXiv:2106.02023, Sections II and IV) supplies motivating context but not the explicit two-band simplex-cap calculation. Pasqual (DOI:10.1016/j.jsv.2014.05.006, Sections 3–5) treats an actual tetrahedral array of nonoverlapping spherical cap diaphragms and studies its spherical-harmonic acoustic radiation amplitudes; it does not calculate the self-adjoint degree-two restriction Gram spectrum or its scalar-isotropy aperture. Published research on simplex-cap overlap and degree-two global harmonic norms addresses different operators. The asserted contribution is specifically the dimension-uniform exact eigenvalues, the unique tetrahedral interior coalescence, and the surviving cubic moment. Historical priority is not proved by any failed search, and an implicit older formula remains possible.

## Mathematical value — PASS

Slepian concentration eigenvalues quantify the best- and worst-observed angular modes of a spatial mask. An explicit two-sector spectrum for a non-axisymmetric union of caps gives an exact sharp concentration range, not just an asymptotic or a numerical eigenanalysis. More strikingly, at one nontrivial tetrahedral aperture **all five quadratic harmonic modes have exactly equal energy fraction**, while a cubic harmonic has a provably nonzero mask integral. The dimension-four boundary resonance and dimension-at-least-five exclusion identify the sharp geometry-dependent transition, making the exact angular threshold mathematically meaningful rather than an arbitrary parameter choice. A direct conditional-fourth-moment calculation and simplex rank reduction are needed; this is neither a single-cap substitution nor merely a table lookup.

## Limitations and closest literature

The result does not extend to low-pass multi-degree Slepian spaces, overlapping caps, unequal cap radii, other simplex-like configurations, or finite/noisy recovery. The closest full texts inspected were the arbitrary-region Slepian foundations, the 2021 spherical Slepian-wavelet construction, and the 2014 tetrahedral spherical loudspeaker-array harmonic analysis. None of the inspected claims is the presented exact compression spectrum; other unlocated harmonic/tensor literature may still affect historical novelty. The checker includes numerical quadrature and cannot certify all dimensions by itself.

Self-review: passed. Independent audit: not yet performed.
