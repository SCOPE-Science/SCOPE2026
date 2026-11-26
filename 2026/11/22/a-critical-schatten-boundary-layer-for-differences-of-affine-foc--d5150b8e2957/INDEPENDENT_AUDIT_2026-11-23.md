# Independent mathematical audit

## correctness

PASS

On the normalized monomial basis the binomial expansion gives one weighted backward shift for each degree drop k, with weights q^m h^k(u^k-v^k)sqrt((m+k)!/m!)/k!. The sum over m of the moduli is its trace norm; applying Cauchy–Schwarz to the two q^(m/2) factors and summing the rising factorial series gives |u^k-v^k| h^(k/2-1)/sqrt(k!). This sums absolutely. The maximal weight bound follows from (m+k)!/m! <= (m+k)^k and maximizing y^(k/2)exp(-delta y), delta=-log q>=h: shifting y=m+k costs at most 2^k for q>=1/2. Thus all k>=2 give an O(1) trace and O(h) operator remainder. Point evaluations are continuous, so the binomial identity on polynomials identifies the resulting bounded operator with the composition difference on the entire space. For each fixed p>=1, sum of singular values to power p is bounded by the trace norm times operator norm to power p-1 for the remainder. Dividing by the leading h^(1/2-1/p) makes the norm error O(sqrt h) on that scale. The nonzero weights of the first shift divided by sqrt h have exact form |u-v| sqrt(hn)q^(n-1); for q near one this is bounded by 2|u-v|sqrt(hn)exp(-hn). This controls tails for the Riemann sums, yields the integral Gamma(1+p/2)/p^(1+p/2), and gives the maximum |u-v|/sqrt(2e). The uniform rescaled singular-value error bounds the count between shifted thresholds, and the strict superlevel length is continuous at every asserted threshold. The Hilbert–Schmidt calculation sums squares on mutually orthogonal matrix diagonals with the binomial series at q^2, giving precisely the three-exponential identity and the |u-v|/2 limit. The checker was read, not run; its two HS sums share the same coefficient routine and are diagnostics, not independent proof. Independently reproducible certificates are the two convergent binomial sums and the one-variable profile integral. The symbols are strict affine contractions, not necessarily contractive operators (C_{q,u}z=qz+hu and exponential kernels distinguish the norms); the theorem itself makes no operator contractivity assumption.

## originality

PASS

Best of checked evidence: fixed-symbol Schatten membership and the first-shift spectral profile are covered and not credited. The surviving contribution is the uniform approximation of the actual non-diagonal coalescing affine difference on both norm extremes, with transferred sharp moving counting law and evaluated exact Hilbert–Schmidt expression. The closest same-date result about coalescing sums was checked at the level of its full symbol hypotheses and is distinct.

## value

PASS

This is a sharp classification of a natural coalescing-family difference, not a new label for fixed-symbol ideal membership. Operator-norm disappearance, a nonzero limiting HS norm, and trace blow-up coexist; the singular count reveals that the mass resides in order h^{-1} singular values of order sqrt(h). Establishing where the established leading profile accurately describes a genuinely non-diagonal operator is mathematically substantive. Scope is fixed distinct centers, one-dimensional Gaussian Fock space, common real slope and fixed p>=1; there is no claim about drifting centers or lower quasi-norm exponents.

The dated certificate retains the supplied scientific assessment, sources and limitations.
