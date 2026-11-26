# Independent mathematical audit

## correctness

PASS

The exact mixture has variance a+(b−a)u. Normalization follows by integrating the two terms in h: multiplying the shifted beta integrals by c gives 1/R₁ and 1/R₂ respectively, so the total is r_H(1/r₁+1/r₂)/2=1. The mixture endpoints have coefficients H₋ and H₊. With L=log N and w=Lu or L(1−u), the standardized threshold in Gumbel units tends to y−k₋w or y+k₊w. Mills' inequality gives a hazard at least z at positive normal argument z; integrating it bounds the lower conditional CDF by exp(−C exp(cw)) and the upper exceedance by C exp(−cw) on fixed near-endpoint intervals. Splitting the complementary interval off before rescaling handles any singularity of the mixing density at the opposite endpoint. These bounds justify dominated convergence with all R_j>0, including insertion of bounded continuous test functions. At the literal upper edge the exceedance is uniformly asymptotic to N times the Gaussian survival probability, and sqrt(L) times that tail tends to exp(−k₊w)/sqrt(4π); integration yields (UE). At the literal lower edge Mills' ratio gives N times the tail asymptotic to exp(k₋w)/sqrt(4πL), uniformly on w=O(log L). Cutoffs (1±ε)log L/(2k₋) sandwich the effective mass, with the upper remainder negligible by monotonicity. Integrating the density to these cutoffs and taking ε down to zero gives (LE), without using a fixed-y limit for moving y. The numerical example has H₋=2/3, H₊=4/3, k₋=1, k₊=1/2, as needed. For these parameters an independent quadrature at L=80,120,400,1200 corroborated both profiles, both literal edges, and a conditional test function on each side. At L=1200 the fixed-y=0 normalized probabilities were 0.147745 and 2.120507 versus 0.146256 and 2.124266; the literal lower ratio to the asymptotic was 1.203 (down from 1.412), and the literal upper probabilities were 1.8000e−5 versus 1.8096e−5. The quadrature used a Poisson approximation at the largest L, with negligible binomial error in the contributing region; it is not an exact finite-N certificate. Replay: python3 /workspace/branches/b1eea16d-5842-484c-9829-0b8d0a13629e/independent_edge_check.py.

## originality

FAIL

The distinct indexed record bbe0ae7a3ed5 covers the entire mathematical claim in the same stationary model: both profiles, both conditional weak limits, both literal edge constants and exponents. Its fixed-argument result is even locally uniform in the centering argument. This is an exact coverage finding, not an attribution of priority to the later-dated indexed record. The primary 2023 switching-trap paper supplies the mixture and leading law but is not, on its own, the reason for the failure.

## value

FAIL

The logarithmic asymmetry and environment selection are meaningful physics and mathematics in their own right. This frozen record does not establish a distinct useful contribution beyond the exact matching theorem: its different choice of dimensionless boundary coordinate is a substitution, and the illustrative rates are a direct evaluation. No additional threshold behaviour or independently useful invariant remains after the comparison.

The dated certificate retains the supplied scientific assessment, sources and limitations.
