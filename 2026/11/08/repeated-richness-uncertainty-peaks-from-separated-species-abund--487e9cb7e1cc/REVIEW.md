# Independent mathematical audit

## correctness

PASS

Occupancy-indicator covariance yields V_n=sum_i(q_i^n-q_i^(2n))+2sum_ij[(1-p_i-p_j)^n-(q_i q_j)^n]. For m=1 variance zero; m=2 K_n=1+Bernoulli(1-p^n-(1-p)^n) and success probability increases, so at most one strict local maximum. For m>=3 choose p0=1-sum_(j=1)^(m-1)epsilon^j, pj=epsilon^j. At n_j~(log2)/epsilon^j, K distribution converges to j+Bernoulli(1/2), variance to 1/4; between scales at epsilon^(-j-1/2) K concentrates at j+1 and V to zero. Finite separated intervals each have an interior maximum; transcendental sufficiently small epsilon excludes every adjacent equality because V_(n+1)-V_n is a nonzero polynomial with leading epsilon coefficient. Independent exact subset-DP checks for (7,7,1)/15 confirm strict peaks at n=3 and n=9 and all four quoted rational differences; numerical finite tests are not proof of all-m existence. No m-1 upper bound is asserted.

## originality

PASS

Best-of-knowledge PASS for the sharp finite iid-with-replacement three-species double-peak threshold and every m>=3 m-1 separated near-1/4 strict peaks. Existing exact occupancy covariance identities and infinite-box oscillatory variance theory cover ingredients and possibly some existence after truncation, not the finite cardinality, strict peak placement and deep-valley theorem. Earlier 13-individual rarefaction result uses sampling without replacement, so the thresholds are not equivalent.

## value

PASS

PASS: Variance of accumulated species richness is a directly relevant finite-community uncertainty statistic. The sharp m=3 first double peak, unbounded multiplicity as richness grows, and near-1/4 isolated heights separated by arbitrarily deep valleys correct a tempting single-hump intuition; strict peaks are genuine integer effects rather than plotting artifacts. No unsupported empirical universality is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
