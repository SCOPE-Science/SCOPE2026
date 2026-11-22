# Scientific review: two-coloured permutation-cycle fixed-set convolution

## Correctness — PASS

The claim is an exact theorem for every \(n\ge1\). The cycle-count partition function is \((n+1)!\). Prescribing \(j\) particular fixed points forces \(j\) coloured singleton cycles, leaving a cycle-coloured permutation on \(n-j\) labels; character inclusion–exclusion therefore gives exactly \(\Lambda_{n,k}\), with no independence assumptions. The difference identity \(\Lambda_{n,k}-\Lambda_{n,k+1}=4\Lambda_{n-1,k}\) and integration-by-parts recurrence \(M_{n+1}=(n-2)M_n+4nM_{n-1}\) are proved directly, including boundary indices. Explicit spectra for \(1\le n\le8\), followed by induction from \(M_8=15744\), \(M_9=71936\), establish every sign, zero, and extremal eigenvalue. Dominated convergence of the exact binomial sum proves the asymptotic limit. The extracted exact-arithmetic verifier passed 17890 assertions, including complete character transforms of weighted permutation enumerations through \(n=7\). Enumeration is evidence of finite consistency only.

## Originality — PASS (bounded prior comparison)

The classic uniform-permutation fixed-position statistic and Ewens normalizing formulas are explicitly credited. In Diaconis–Fulman–Guralnick, arXiv:0708.2643v1, the inspected opening and fixed-point/derangement discussion concern ordinary and generalized permutation fixed-point counts, not the binary incidence-convolution's exact weight-shell signs. In Hughes–Najnudel–Nikeghbali–Zeindler, arXiv:1109.5010v1, the inspected Sections 2 and 3 develop generalized Ewens measures, characteristic polynomials and multiplicative class-function statistics; Section 2 contains the normalizing identity used here, but not the new sharp Boolean Walsh inertia classification. Indexed comparisons of equivalent Gamma shifted moments, two-colour cycles, Ewens-parameter-two Fourier kernels and exact 12928 eigenvalues gave no dominating result in the inspected records. Published comparable signed matching, uniform fixed-point and Ewens covariance results use different objects or do not determine this full character spectrum. Historical priority remains uncertain particularly for special-function tables of shifted Gamma moments and an unindexed Krawtchouk analogue; no unqualified novelty-certification claim is made.

## Value — PASS

The two-colour cycle model is an elementary, canonical unweighted realization of the Ewens parameter-two measure, and fixed-position profiles are a natural binary observable. The resulting convolution is information-preserving in every dimension except three yet positive definite only at six and from eight onward: the failure of monotonicity between orders six, seven and eight is a structural boundary not detectable from eventual asymptotics. Its smallest eigenvalues and exact condition numbers give sharp quantitative Fourier recovery, tending to a finite limiting ratio \(e^4\). This is an infinite-family theorem, not a routine finite-table computation; the Gamma recurrence provides the non-enumerative mechanism.

## Limits and comparison risk

The entire proof is restricted to two cycle colours and \(\ell^2\) conditioning. No claim concerns all Ewens parameters or coordinatewise inversion norms. The closest original literature establishes the input distribution, not an independent uniqueness guarantee; earlier equivalent arithmetic inequalities could exist without appearing in the inspected sources. The review is not an independent expert audit.

Self-review: passed. Independent audit: not yet performed.
