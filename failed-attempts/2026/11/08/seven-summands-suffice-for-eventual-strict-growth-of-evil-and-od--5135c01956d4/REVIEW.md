# Independent mathematical audit

## correctness

PASS

The mathematical first-difference asymptotic is correct. The parity indicators give F_±=((1-z)^(-1)±T)/2; multiplying F_±^k by (1-z) takes the first difference with zero extension, and the term with no T has coefficient 2^(-k) binom(n+k-2,k-2). Allouche–Shallit quote the uniform full-circle Gelfond bound, which Abel summation at rho=e^(-1/N) transfers to sup |T|=O(N^alpha). Parseval gives the normalized integral of |T|^2 exactly (1-rho^2)^(-1)=O(N). Cauchy's coefficient factor is e on taking N=n, and |1-rho e^(i theta)| is comparable to N^(-1)+|theta|. For 1<=j<=k-3 the uniform bound on T and the weighted angular integral give a saving j(1-alpha) against N^(k-2) (this also independently verifies the record's j=2 case without a split). For j=k-2,k-1 the maximum of the weight, the bound on T^(j-2), and its second moment save (j-2)(1-alpha). The pure T^k term has the harmless factor (1-z) and is O(N^(1+(k-2)alpha)), saving (k-2)(1-alpha)-1. This is positive for k>=7 since 3^5<4^4, and entails the stated common eta_k for both signs and fixed k. The main term gives eventual strict positivity, with no least threshold. No computation is required for the infinite estimate. The frozen VERIFICATION.md records checks through degree 320; the source script was inspected, not executed, and the finite checks are not the proof. The historical claim of newly settled cases is addressed under originality, not credited as a consequence of the asymptotic.

## originality

FAIL

The earlier Resultary record 32f21fdb5b42 proves the analogous sixfold result for these same ordered tuples and supplies a disk sixth-moment lemma that, with classical inputs and the same coefficient expansion, implies the full frozen quantitative claim, not just eventual positivity. For j<k, standard sup and second-moment bounds give saving at least 1-alpha (details under correctness). The indexed sixth-moment bound is integral |T|^6=O(N^beta), beta=log_2 15<4. For j=k>=7, combine it with k-6 uniform Gelfond factors and |1-z|<=2: the coefficient is O(N^(beta+(k-6)alpha)), saving 4-beta+(k-6)(1-alpha)>1-alpha. Thus known bounds give O_k(n^(k-2-(1-alpha))) for every k>=7, at least as strong as the frozen eta_k and strictly stronger at k=7. This uses the earlier proof's moment lemma, not the unsupported claim that the sixfold asymptotic alone propagates every quantitative exponent. The target's use of L2 instead of L6 is a different estimate, not a new bound or unresolved-case theorem.

## value

FAIL

Resolving the monotonicity question or providing a genuinely improved error estimate would be valuable. The frozen finding does neither relative to the indexed sixfold work and its lemma: the claimed cases and quantitative conclusion follow, with a stronger saving at seven, and there is no new least threshold. Using a simpler second-moment argument has expository interest, but it gives a narrower result by replacing the previously available moment estimate with a weaker one, without a separately established useful extension or new theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
