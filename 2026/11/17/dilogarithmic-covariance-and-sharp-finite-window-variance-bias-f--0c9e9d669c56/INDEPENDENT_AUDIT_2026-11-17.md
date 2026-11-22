# Independent mathematical audit

## correctness

PASS

The m inverse branches turn covariance into log-integrals J(j). Integration by parts, Li₂(−1/j), and telescoping logs give C(m)=1+m⁻¹Σ_{j=1}^{m−1}jLi₂(−1/j), with C(1)=1. Each r_j=1+jLi₂(−1/j) has a positive decreasing integral representation; averaging establishes C(m)>0 and strict decrease. Dilogarithm expansion of r_j through j⁻³ and Euler–Maclaurin give (.25 log m+B)/m−1/(72m²)+1/(288m³)+O(m⁻⁴); independently evaluated B=1.0102793965954957… and checked high precision residuals. Lag decay O(kb⁻k) justifies absolute convergence and exact pair-count identity Var(S_N)=Nσ²−κ+2Σ_{k≥N}(k−N)C(b^k); geometric j-sum yields N b^(1−N)log b/[2(b−1)²]+O_b(b⁻N). Finite numerical quadrature and N checks are corroborative, not a proof.

## originality

PASS

The exact all-integer-base dilogarithmic covariance and finite-N signed asymptotic variance correction were not supplied by the inspected same-observable Defaveri–Smith paper, which reports doubling variance numerically; more general logarithm singularity deviation results concern different statistics. This is best-of-knowledge, not absence certification.

## value

PASS

Exact quantitative covariance and finite-sample variance bias for a canonical singular observable on a standard chaotic map provide a useful calibration for temporal dependence, numerical fluctuations, and limiting-variance estimates.

The dated certificate retains the supplied scientific assessment, sources and limitations.
