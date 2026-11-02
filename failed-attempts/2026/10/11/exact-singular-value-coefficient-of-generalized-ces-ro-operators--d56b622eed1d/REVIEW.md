# Independent mathematical audit

## correctness

PASS

For fixed 0<=t<1, C_t=D(I-tS)^(-1), D=diag(1/(n+1)), and D is compact with singular sequence 1/n. For every finite cutoff A_m=sum_{r=0}^m t^r S^r, the printed block decomposition of DA_m is valid: P0DA_m finite rank; within-block diagonal error trace class by summing (r+1)/(kB)^2; each cross-boundary strip has rank <=m and norm <=M/(kB+1), giving epsilon N(epsilon,R)<=mM/B; block direct sum Q_B/(kB) gives the exact coefficient ||Q_B||_1/B; Q_B differs from a circulant by rank <=m and the normalized trace norm tends to the Fourier-symbol modulus mean. Sending B to infinity and the Ky Fan perturbation tolerance to zero yields epsilon N(epsilon,DA_m) -> c_m. The analytic-symbol tail has s_n(D(A-A_m))<=t^(m+1)/((1-t)n); Ky Fan inequalities let m tend to infinity, yielding epsilon N(epsilon,C_t)->c(t). The standard monotone counting inversion yields n s_n(C_t)->c(t)>0. The integral equals 2 K(2 sqrt(t)/(1+t))/(pi(1+t)), with K modulus convention; checked at t=0 and by independent quadrature and 240x240 singular-value calculations for t=0.3,0.7. Thus log partial sums, membership S_{1,infty} and all S_q (q>1), and nonmembership S_1 follow. Finite sections only corroborate; all fixed t<1 and the real/complex versions are proved, not uniform t->1 or t=1.

## originality

FAIL

FAIL by specific mathematically decisive prior coverage, not lack of evidence: Pushnitski arXiv:1710.02652v1 Theorem 1.2 already proves the same sharp symbol-average first-order singular-value asymptotic for all compact finite-band power-decaying matrices. The operators D sum_{r=0}^m t^r S^r directly satisfy its gamma=1 hypotheses; the full C_t is obtained from these by the elementary S_{1,infty} geometric tail estimate and the prior article Section 2.2 Ky Fan coefficient continuity. This gives exactly the claimed integral for every fixed 0<=t<1 without any unproved new lemma. The elliptic evaluation is a standard half-angle substitution, and Schatten and logarithmic-trace consequences follow from s_n~c/n. The older same-family literature did not give this coefficient explicitly, but that does not defeat implication by a stronger matrix theorem.

## value

FAIL

The compact generalized Cesaro family is motivated and the exact elliptic coefficient is a useful reference benchmark. Nonetheless this precise coefficient, its logarithmic partial trace and sharp weak-Schatten endpoint are a routine specialization of Pushnitski’s much broader spectral law, using the elementary geometric-tail weak-S1 estimate, a standard elliptic substitution and harmonic-series summation. No independently unknown exact invariant, new qualitative or extremal phenomenon, sharp second-order asymptotic, nontrivial structural lemma or distinct classification survives. Correctness and a convenient closed form do not rescue value as a new research result; it can remain a pedagogical corollary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
