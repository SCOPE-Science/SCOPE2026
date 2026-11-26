# Independent mathematical audit

## correctness

PASS

Re-audited /workspace/repairs/4/RESULT.md. The frozen claim of almost-surely no comparison ties is false: i=j+1 on the cycle shares the Y value, and equal Bernoulli halves, of probability 1/2, then force a tie. The repaired scope describes these ties and retains the strict inequality, under which they contribute zero; the theorem's formulas are unchanged. Subtracting the unpermuted strict count yields the signed quadratic identity with a cyclic-ascent diagonal. Conditional on the Y ranks the Rademacher pair products are orthogonal, and each coefficient C_ik has second moment 1/2, including at adjacent indices and for n=3. The ascent count has expectation n/2 and variance n/12 (covariance -1/12 per adjacent unordered pair); total variance yields the claimed exact moments. For the limit, bounded finite-rank eigenfunctions give a one-dependent joint CLT with identity covariance after removing the single seam; sign-pair orthogonality bounds the non-overlapping tail by the squared Hilbert–Schmidt norm and the overlapping tail by O(1/n) at each fixed rank. The shift is -1/4. On antisymmetric functions the square of K gives the stated ODE and boundary constraints, and their converse recovers each eigenfunction. The cosine frequencies and tangent equation each give simple modes; coordinate exchange pairs the opposite eigenvalues of K. The repaired product argument excludes nonreal zeros by positivity of K^2 and uses evenness and order one to fix the product. Taylor coefficients or the paired chi-square cumulants give variance 1/16 and excess kurtosis 10/3. Replay: python3 /workspace/independent_checks.py 4 independently enumerates exact comparisons, ties and finite moments for n=3,4,5. It is not a spectral or limit certificate; those were checked analytically. Frozen check.py inspected only.

## originality

PASS

Final claim only: the strict cyclic statistic is prior, and the earlier authors already explain that additive CDF transforms cause first-order degeneracy. The particular additive score's tie-aware exact moments, second-order spectrum and explicit characteristic function are the distinct contribution; a Gaussian-chaos theorem alone does not evaluate these. No exact independent cover was found in the reasonable bounded comparisons. The repair does not introduce a different statistic or a new priority claim.

## value

PASS

This is an explicit nontrivial two-coordinate score in the defining test's additive exception. It shows what replaces first-order Gaussian calibration for the strict statistic, with a finite-size correction, a genuinely non-Gaussian boundary law and a computable characteristic function. Recognizing structural cross-list ties matters at the same order as the fluctuation. This is a boundary example, not a general result for trained classifiers or estimated calibration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
