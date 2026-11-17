# Independent mathematical audit

## correctness

PASS

For W_{m+1}=K_1 join C_m with m>=3, incidence matrix E of all m spokes and m rim edges has reduced Laplacian L=3I-S-S^T and positive Green matrix g_d=[a^d+a^(m-d)]/[sqrt(5)(1-a^m)], a=(3-sqrt5)/2. Matrix-tree/transfer-current differentiation gives edge covariance C=diag(K_ee)-K∘K, K=E^T L^-1 E; it has precisely the fixed-tree-size constant null direction. Three periodic sequences g,h=2g-g_{+1}-g_{-1},q=g-g_{+1} produce the 2x2 Hermitian Fourier blocks, and the infinite-volume branch formula has low-frequency minus branch ~theta^2/(4sqrt5), maximal plus branch 4/(5sqrt5). Thus lambda_min+ ~pi^2/(sqrt5 m^2), max ~4/(5sqrt5), condition ratio ~4m^2/(5pi^2). I independently built E,L,K,C and compared *all 2m eigenvalues* with Fourier blocks for m=3,4,5,6,8,12,24,48,96; at m=96 the rescaled ratio 0.0811509867 approaches 4/(5pi^2)=0.0810569469. The proof uses uniform exponential wrap-around errors, not an inference from finite m.

## originality

PASS

Best-of-knowledge original complete wheel-specific covariance Fourier spectrum and sharp growing anisotropy; general transfer-current determinantal identities, wheel tree totals and matrix-tree theorem are not claimed as new.

## value

PASS

Uniform spanning-tree incidence vectors are the vertices of a canonical graphic matroid base polytope, and their covariance eigenvalues determine intrinsic inertia and conditioning. A sharp m² divergence on wheels despite nonvanishing local edge variance is a nontrivial geometric scale separation. The exact Fourier bands make the invariant reusable for graph-polytope inertia and stochastic edge network fluctuations; no paper-sized generality is needed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
