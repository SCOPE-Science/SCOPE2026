# Independent mathematical audit

## correctness

PASS

The covariance gives conditional velocity N(3u/(2t), k²t/4), so the absolute-velocity Rice intensity at the nonzero level is g(t/τ)/τ with τ=(|u|/k)^(2/3). Rice can be used away from zero (bounded level density on compact positive time intervals and continuously differentiable position), followed by monotone convergence at zero. There is no crossing at the independent cycle endpoint with positive probability. The kernel is bounded, so crossing rewards are integrable for any allowed clock; the renewal reward law is almost sure, including lattice clocks. The unfinished cycle is negligible: integrable iid rewards have N_i/i→0 almost surely, while cycle indices scale linearly in elapsed time. The derivative D=5-2z²-3R is positive for z<=1, strictly decreasing for z>=1 where R<1/3, and negative for z>=√(5/2). Thus g first increases then decreases. Q(s)=s g(s)-H(s) has derivative s g'(s) and tends to -∞ by the logarithmic growth of H, so the positive tangency is unique. The straight tangent from zero joined to H at a is concave, with strict separation on (0,a) and strict curvature beyond a. At mean a or above, the majorant and Jensen equality conditions force the point mass; below a the only potential contacts in the affine interval are 0 and a, with 0 prohibited. The supplied positive two-point construction has exactly the prescribed mean and converges to the bound. Independent quadrature and bisection reproduced a≈2.31788487331918, g(a)≈0.14139329860537, rτ≈0.52032768949327 and Poisson maximum ≈0.10467026210716/τ (gain ≈35.0845%). The Poisson extremum is also unique by the one-sign-change Laplace-transform argument on s g'(s): after scaling its derivative by exp(rτ s_peak), that derivative's scaled value is strictly decreasing in rτ. The supplied script was read, not executed. A separate solve of D=0 gives s_peak≈1.224035815670, about 9e-11 below the illustrative finite-difference value in the record; this does not affect the theorem or tangent/flux constants. The decimal calculations are not interval certificates, and reset jumps are not counted.

## originality

PASS

The free Rice law, unimodality of this free kernel, Poisson formula and best Poisson rate are already covered. The distinct claim supported here is the sharp crossing-rate comparison over all fixed-mean iid positive renewal laws, with its contact constant and attainment classification. Fixed-mean clock envelopes with the same qualitative structure exist for other kernels, but the inspected analogues do not state a general theorem of the needed scope that already covers this crossing objective. The envelope method itself is not new.

## value

PASS

The available clock laws have an operationally meaningful sharp transition not visible to Poisson optimization: an entire short-mean interval shares a supremum but no optimal positive clock, whereas a periodic clock uniquely optimizes at and above the boundary. The contact scale and comparison with best Poisson resetting quantify this gap for a well-studied crossing observable. The burst limit is an idealization permitting arbitrarily small intervals and excluding reset jumps and overhead; neither realistic resetting constraints nor first-passage performance are evaluated.

The dated certificate retains the supplied scientific assessment, sources and limitations.
