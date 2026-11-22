# Scientific review: radial Bergman diagonal Markov spectral outliers

## Correctness — PASS

For each admissible radial weight, Panja's Kraus formula gives precisely the inhomogeneous pure-birth operator \((P_wx)_n=(\delta_n/d)x_{n+1}+(1-\delta_n/d)x_n\). Strict moment log-convexity and boundary support imply \(\delta_n\downarrow1\). The operator is a compact perturbation on \(\ell^\infty\) of \((1-1/d)I+(1/d)B\); direct Fredholm analysis of the backward shift gives its essential circle and index. The eigenvector recurrence proves the entire closed disk is point spectrum; a tail inverse followed by finite back-substitution exhausts the exterior spectrum. For beta weights, both right and left eigenvectors are computed explicitly, with the left vector in \(\ell^1\), and the rank-one projection's exact norm follows from a hypergeometric sum. Its critical asymptotic is a genuine limit, not a finite experiment. The packaged rational/float diagnostic provides supplementary consistency checks, not an infinite-dimensional proof.

## Originality — PASS, qualified

The precise claim is the full spectrum of the new channel's canonical diagonal restriction, the moment-ratio outlier criterion, and the beta-weight exact spectral-projection/merger exponent formulas. Panja [1] supplies the unital completely positive channel and fixed-point characterization but does not investigate its diagonal restriction's spectrum or projections. Trefethen, Contedini and Embree [2] investigate random iid bidiagonal matrices and a general resolvent mechanism, not the deterministic monotone moments or hypergeometric Riesz-projection asymptotics. Ordinary compact-perturbation shift Fredholm theory is a known ingredient, explicitly acknowledged. Searches of existing mathematical records and the accessible related literature did not identify a statement subsuming the complete claim; absence of hits does not prove novelty. A previous deterministic bidiagonal eigenprojection theorem might still dominate some portion of the result.

## Mathematical value — PASS

Panja's diagonal subalgebra is canonical and invariant; spectral data there distinguish radial weights despite the universal geometry of the essential circle. The precise condition \(\delta_j>2\) counts nonnormal isolated modes for arbitrary admissible radial weights, and for classical beta weights the count is \(\max(0,\lceil\alpha\rceil)\). More substantially, the exact Riesz-projection norms have sharply different odd-order blow-ups at consecutive merger thresholds, quantifying a spectral-conditioning instability invisible to the fixed-point classification or ordinary spectral set alone. This is a natural spectral invariant of a newly defined operator, not an arbitrary finite slice.

## Closest work and limits

[1] Samir Panja, arXiv:2611.09731v1 (2026-11-06), https://arxiv.org/html/2611.09731v1 .

[2] L. N. Trefethen, M. Contedini and M. Embree, *Spectra, pseudospectra, and localization for random bidiagonal matrices* (2001), https://people.maths.ox.ac.uk/trefethen/publication/PDF/2001_96.pdf .

The theorem does not describe the whole completely positive superoperator. The projection formula is specialized to beta weights. Independent bibliographic comparison may still find an older general Riesz-projection calculation in a deterministic bidiagonal framework.

Self-review: passed. Independent audit: not yet performed.
