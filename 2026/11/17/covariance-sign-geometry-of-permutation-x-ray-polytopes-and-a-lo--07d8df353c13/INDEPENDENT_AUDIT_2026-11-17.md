# Independent mathematical audit

## correctness

PASS

PASS: Reconstructed the permutation-cell indicator covariance (delta_row-1/k)(delta_col-1/k)/(k-1) and summed it over anti-diagonal row intervals to obtain [k^2 m_t 1_{s=t}-2k h_st+m_s m_t]/[k^2(k-1)]. Nested same-side row intervals force strictly negative off-diagonal numerators; for opposite-side intervals h=max(0,a+b-k), yielding N=ab-2k max(0,a+b-k) and exact hyperbola sign criterion in both a+b regimes. Positive b counts are ceil(2k(k-a)/(2k-a))-1 per left a; bounded ceiling error permits the Riemann integral 2-2 log2 divided by 2 asymptotic unordered pairs. At most one b per a gives zero. Variance kernel: the zero-variance linear statistic is constant across permutations; swapping two rows and two columns enforces all second differences zero, so only span{1,t}, with k=2 included. Trace follows from sum m_t^2=(2k^3+k)/3. Direct independent exhaustive permutation enumeration k=2..6 confirmed rational covariances/signs/trace; finite enumeration is not an all-k proof.

## originality

PASS

PASS qualified: The underlying Birkhoff anti-diagonal X-ray polytope, affine hull and facet structure are established; the result concerns a distinct canonical pushforward *probability law* (multiplicity retained), not uniform interior volume or distinct X-rays. Classic permutation X-ray enumerations and modern facet/diameter theorems do not directly entail the complete dependence-sign geometry and logarithmic limiting fraction. Historical Brualdi–Fritscher Hankel/Toeplitz full text remained inaccessible; matching a general covariance identity alone is not coverage of the exact new classification.

## value

PASS

PASS: The source measure on Birkhoff vertices produces a natural stochastic statistic for a well-studied projected polytope. Despite two conservation laws, the sign diagram has a curved positive-correlation region occupying a nontrivial universal density 1-log2, separating same-side anticorrelation and opposite-side mixed signs. The complete all-k exact sign/count limit is useful beyond facet or diameter geometry; no arbitrary parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
