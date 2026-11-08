# Scientific review — cycle stable-set vertex covariance

## Correctness — PASS

For each integer \(n\ge3\), all stable-set indicator vectors are vertices. The independent-set transfer matrix counts \(L_n\) vertices, and a two-site deletion argument gives the exact circulant second-moment kernel \(q_k=F_{k-1}F_{n-k-1}/L_n\). Binet summation determines every nonconstant Fourier eigenvalue. Two derivatives of the same partition function determine the constant mode. The proof gives strict ordering of all eigenvalue types, with explicit separate even and odd cases, and a limiting condition number of \(5\). The standalone checker enumerates all stable sets for \(3\le n\le16\), checks exact rational moment entries, and tests Fourier eigenvalues; it does not substitute for the general proof. Risk: transcription of a transfer-matrix identity was checked against the independent enumeration, but no external proof review was performed.

## Originality — PASS, historical priority provisional

The accessible full text of Davis–Kohl (arXiv:2207.14759, 2022) develops stable-set polynomial and Ehrhart material, not the proposed covariance spectrum. The accessible full text of Oriolo–Stauffer (2022) studies facets of circular-interval stable-set polytopes, not second moments. Ehrenborg's cyclic graph-polytope work was identifiable via its abstract, which concerns Ehrhart and face polynomials; the publisher full text remained inaccessible for a complete comparison. Closely related classical one-dimensional hard-core-model two-point correlations may imply parts of the spectral calculation after Fourier transformation; the new assessed statement includes the complete spectrum, sharp principal-axis classification, and all-dimensional strict least-eigenvalue proof. Searches of mathematical finding records for cyclic stable sets, vertex covariance, Fourier spectra, aliases and relevant related geometric invariants returned no claim that implied the complete assertion; this is not proof of global novelty. Residual risk: an unlocated statistical-mechanics structure-factor identity or inaccessible full text may cover a significant portion.

## Mathematical value — PASS

Uniform vertex sampling is an intrinsic discrete geometric statistic of a canonical convex-hull realization; its inertia axes are not determined by the known Ehrhart or facial data. The exact covariance and strict identification of its smallest and largest eigen-directions give a natural complete classification across every dimension, with a nontrivial sharp condition-number limit \(5\). In particular the least-variance vector is uniform, although local anti-correlation might tempt an alternating guess. Risk: part of the spectrum follows from standard transfer-matrix manipulations; the value assessment is anchored in the complete spectral and extremal-direction classification, not mere rephrasing of the independence polynomial.

## Closest sources and scope

- Davis–Kohl, arXiv:2207.14759 (2022), stable-set polytope and polynomial background, accessible arXiv full-text material.
- Oriolo–Stauffer, DOI 10.1007/s10479-021-04449-7 (2022), accessible full text on cyclic stable-set facets.
- Ehrenborg, DOI 10.1016/j.ejc.2023.103906 (2024), cyclic graph-polytope Ehrhart/face invariants; abstract only inspected, not full document.
- Classical hard-core ring transfer matrices are inputs, not newly claimed mathematics.

Self-review: passed. Independent audit: not yet performed.
