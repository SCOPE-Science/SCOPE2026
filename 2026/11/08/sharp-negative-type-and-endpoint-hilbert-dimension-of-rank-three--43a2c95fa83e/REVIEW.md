# Scientific assessment: rank-three bilinear-form negative type

## Correctness — PASS

The domain is all \(m\)-by-\(3\) matrices over any prime-power finite field, with \(m\ge3\); there is no hidden odd-characteristic assumption. The direct Gaussian-subspace character calculation in `RESULT.md` yields all three nonconstant powered-distance eigenvalues. The positive derivative of the rank-two eigenvalue, together with explicit negative bounds for rank-one and rank-three eigenvalues through the crossing, establishes the exact if-and-only-if negative-type interval. The rank-two frequency count and double-centering give the minimum Hilbert realization dimension, not just an upper bound. The asymptotic limits use the verified derivative scale and mean-value theorem. The attached checker independently counts Fourier coefficients in characteristic two, three and four. These computations do not certify infinite parameter ranges; the displayed proof covers them.

## Originality — PASS, with bounded historical risk

The primary predecessor, Delsarte (1978), develops the bilinear-forms association scheme, matrix-rank valencies and generalized Krawtchouk eigenmatrix. Its full 16-page text and appendix do not state the powered-distance conditional-negative-type threshold or critical embedding dimension. Li and Weston (2009) prove general strictness/interval principles and Sánchez (2011) a general finite-metric determinant criterion, with applications of a different type. Those principles are background, not an explicit calculation of the rank-two crossing or the competing-sector signs. A published general theorem or an unpublished specialization could still subsume the calculation; no exhaustive priority assertion is made. Nearby Fourier-frame, Grassmannian and rank-two-convolution statements concern different kernels or spaces and do not alone imply the present formulas.

## Mathematical value — PASS

The rank metric on full rectangular matrix spaces is a canonical translation-invariant metric underlying bilinear-forms graphs and rank-metric coding. The exact generalized roundness is a global Hilbert-embeddability invariant, not a routine eigenvalue at one arbitrarily chosen parameter. The theorem identifies the only Fourier rank that becomes singular, computes the resulting sharp drop in Euclidean embedding dimension, and determines two independent all-field/all-length scaling regimes. These facts distinguish the rank-three metric from previously studied Grassmannian, alternating, and Hermitian metrics and have immediate use for spectral/metric geometry of bilinear-forms graphs.

## Closest literature and limitations

- P. Delsarte, *Bilinear forms over a finite field, with applications to coding theory*, JCTA 25 (1978), DOI `10.1016/0097-3165(78)90015-8`: source of the classical matrix-rank association scheme and generalized Krawtchouk character table.
- H. Li and A. Weston, *Strict p-negative type of a metric space*, arXiv:`0901.0695`: general negative-type strictness/interval framework.
- S. Sánchez, *On the supremal p-negative type of a finite metric space*, arXiv:`1108.0451`: general finite negative-type computation criterion and bipartite-graph application.

The restriction to three columns is essential in the elementary formulas; no dimension-independent theorem for arbitrary matrix ranks is proved. The four exhaustive field/dimension computations are supporting checks, not independence or universal proof. A prior theorem whose statements are presented in an equivalent distance-regular association-scheme language may still imply the result and would require an external priority assessment.

Self-review: passed. Independent audit: not yet performed.
