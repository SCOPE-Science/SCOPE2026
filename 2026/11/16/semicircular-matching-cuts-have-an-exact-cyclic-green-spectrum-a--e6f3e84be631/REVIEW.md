# Independent mathematical audit

## correctness

PASS

For a uniform matching of 2m fixed labeled sites, pair indicators satisfy p=1/(2m-1), q=1/[(2m-1)(2m-3)] for disjoint edges and zero for incident distinct edges. Centered equal-half cut vectors lie in the kernel of unsigned vertex-edge incidence, so the line-graph adjacency acts as -2 and edge-covariance as gamma=(2m-2)/[(2m-1)(2m-3)]. Counting edges crossing both two cuts separated by d gives d²+(m-d)²; centering subtracts m³/(2m-1). The resulting circulant quadratic kernel has constant Fourier eigenvalue gamma*m*h_m and nonconstant gamma*m*csc²(pi j/m); all positive. The cycle Laplacian plus constant projection inverts these modewise, including the parallel-edge m=2 convention. Comparing h_m with csc²(pi/m) using the stated monotone h_t/t² and t sin(pi/t) functions gives constant maximum iff m>=5; nearest-alternating minimum for m>=4, exact small m condition ratios and kappa/m²→1/6. Independently enumerated full pairings m=2..5 and checked exact rational covariance; checked the actual verify.py logic and boundary m=2. The analytic Fourier and monotonicity proof, not finite enumeration, handles all m>=2.

## originality

PASS

The closest fully read published prefix-cut Green-kernel theorem gives nonstationary counts across nested *linear prefixes* and tridiagonal precision; it does not imply that rotating equal-size semicircle cuts have a circulant covariance, explicit full Fourier spectrum, rank-one-corrected cycle precision, or mode crossover exactly at m=5. Global chord crossings and length histograms are different observables. The same pairing indicator covariance input is standard; the cyclic sampling and sharp extremal classification are the substantive original remainder on a natural chord matching ensemble.

## value

PASS

A natural repeated equal-half observational family on random chord diagrams has an exact covariance kernel, its local precision inverse and a nontrivial finite cutoff where the statistically dominant Fourier mode changes from oscillatory to constant. These formulas supply usable spectral conditioning and interpolation information for this concrete model, not a gratuitous isolated numeric table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
