# Independent mathematical audit

## correctness

PASS

PASS. Randomized plane-normal orientation is required to avoid angular ordering bias. Affine sphere Blaschke-Petkantschin for the first 3 vertices has height density (3/4)(1-h²) and circle-angle density proportional to triangle area T with E0[T]=3/(2pi). Given first plane, X4 latitude U=N⋅X4 is uniform [-1,1] and its azimuth independent uniform. Set z=(1-h²)T(U-h)/(3t), so V<t iff |z|<1 with physical latitude cutoff; Jacobian 3t/[(1-h²)T] cancels the area-biased density, proving the EXACT finite-t identity P(V<t)=3pi t μ0(E_t) and conditioned marks μ0(.|E_t). TV distance exactly 1-μ0(E_t). Near poles the outward rejection solves δ²(2-δ)<(3t/T)|z|, giving conditional rejection asymptotic √(t/(6T))? With both sign factors the integrated limit is (1/3)√(3/(2T)), and the inward contribution is O(t/T). Uniform bound sqrt(3/T) and circular Selberg/Dyson identity E0[T^-1/2]=2Γ(1/4)/Γ(3/4)^3 give c*=sqrt(6)Γ(1/4)/(3Γ(3/4)^3)≈1.6087333276801397. Thus P(V<t)=3πt-πsqrt(6)Γ(1/4)/Γ(3/4)^3 t^(3/2)+o(t^(3/2)). Full law and rate follow analytically by dominated convergence, not Monte Carlo.

## originality

PASS

PASS bounded. Classical Miles 1971 scalar volume moments in principle determine the scalar distribution; the leading 3πt and qualitative unmarked chord weak limit were previously published. The surviving claim is the exact EVERY-positive-threshold marked uniform rejection identity and the sharp explicit sqrt(t) total-variation rate. These are not mathematical consequences of a weak limit alone. Unavailable classical original full texts prevent ruling out an earlier equivalent marked disintegration: acknowledged risk, not automatic failure. Oxford institutional retrieval of Miles 1971 returned VPN disconnected after arXiv and lawful OA efforts.

## value

PASS

PASS. Near-coplanar random simplices are a natural rare-event geometry; providing an exact efficiently samplable conditional representation and quantified sharp nonanalytic total-variation correction for the WHOLE marked configuration is substantially stronger than the already-known scalar moments and qualitative weak convergence. Its exact coefficient comes from an integrable negative half-moment rather than arbitrary simulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
