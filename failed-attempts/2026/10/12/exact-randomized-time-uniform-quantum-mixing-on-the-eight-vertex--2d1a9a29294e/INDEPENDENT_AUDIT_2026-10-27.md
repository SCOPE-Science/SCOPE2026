# Independent mathematical audit

## correctness

PASS

The path eigensystem lambda_k=2cos(k pi/9), v_k(i)=sqrt(2/9)sin(ik pi/9), and k<->9-k reflection give the stated cosine/sine amplitude formulas. The displayed 64 strictly positive integer grid weights sum to 256 and give all 32 exact cosine/sine moments; inserting the orthogonal-sine-projector identities yields E[M_ij]=1/8 in all 64 matrix entries. The q=9 spectral relation lambda1=lambda2+lambda4, lambda3=1 and irreducible minimal polynomial X^3-3X+1 for lambda2 imply rational independence of the three torus base frequencies; the positive-time phase orbit is dense. Each mixing coordinate has only 16 nonconstant phase harmonics; the grid image has rank 16 over F109, hence characteristic-zero affine rank 16, so the positive-grid barycenter is in the full relative interior of the torus convex hull. Dense-orbit convex interior transfer and dimension-16 Caratheodory then give exactly <=17 actual nonnegative observation times. An independently written checker confirmed the 64 positive weights, 32 second moments, mod109 affine rank16, and 64 numerical matrix entries (maximum error 1.67e-16), independently of the source program. This does not purport to explicitly construct physical times.

## originality

FAIL

A result already published on 2026-10-04 establishes exactly uniform randomized-time average mixing on the same P8 adjacency walk with support at most 17 real readout times. M(-t)=M(t) converts negative support to nonnegative support without changing the matrix, eliminating even that superficial domain distinction. The audited 2026-10-12 result employs a different 64-grid algebraic witness but makes no stronger final theorem than the earlier constructive positive-density proof. This is direct decisive prior coverage, not a failed-search novelty inference.

## value

PASS

The existence of exact uniform randomized-time mixing on P8 is a natural motivated unresolved arithmetic case q=9 of the quantum path problem. Its exact (not approximate) convex realization with finite <=17 observation times is mathematically meaningful and could guide work on other dependent spectra. The alternative 64-grid construction independently verifies a related phase-geometry phenomenon, but the intrinsic significance of this now-known fact cannot restore originality to the submitted final theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
