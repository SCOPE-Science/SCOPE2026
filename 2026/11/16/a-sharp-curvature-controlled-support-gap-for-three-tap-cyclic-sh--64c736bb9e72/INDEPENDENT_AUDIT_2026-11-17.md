# Independent mathematical audit

## correctness

PASS

Active translation rows are indexed by S-{0,1,2}; m>=min(N,s+2) and sum row support sizes=3s. Factoring frequency monomials yields Z<=3s-m+B for endpoint-only rows B<=s, hence |supp V_gf|>=(N+1)m-3s-B. The proof handles s>=3 and N=6 edge cases separately and correctly enforces >=4N; 826 support subsets for N=6..9 were independently checked against these exact row-counting bounds. For s=2, separated supports have >=5N-2 or 6N, while adjacent supports have four rows and exactly two possible one-root cancellations. Their ratio cosets C1=-bar a/bar b mu_N and C2=-bar b/bar c mu_N coincide iff ac/b² in mu_N. Independent direct N=6 composite-cycle complex Fourier sums confirm 4N-2 vs 4N-1 and singleton 3N. Finite checks are illustrative, not a proof for all N.

## originality

PASS

The Krahmer-Pfander-Rashkov universal two-by-three lower bound 4N-2 (prime case) is acknowledged. Its inequality and existing two-sparse-pair trichotomy do not imply the curvature/root-of-unity phase distinction or all-signal sharp second level on composite cycles.

## value

PASS

Sharp forbidden support levels and complete extremizers for a physically natural shortest nontrivial three-tap STFT window give a useful all-orders finite-uncertainty boundary not determined by the coarse general uncertainty lower bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
