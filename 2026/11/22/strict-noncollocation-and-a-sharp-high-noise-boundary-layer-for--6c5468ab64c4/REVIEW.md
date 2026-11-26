# Independent mathematical audit

## correctness

PASS

Independently integrated the two Brownian covariance sections, inverted the noisy two-observation matrix and reproduced all boundary derivative identities and the cubic expansion by symbolic algebra (python /workspace/review-evidence/check_brownian_algebra.py). A measurement at zero is pure noise and an extra positive-time observation yields a strictly positive integrated reduction; the ordered split derivative and terminal inward directions eliminate every remaining boundary point, including (1,1). Compactness and uniform convergence of the gain divided by ε=1/η localize every maximizer at (1,1). Uniform Hessian control near that corner makes the ordered gain strictly concave for small ε and thus gives global uniqueness in that regime. At the interior stationary point, the derivatives of the order-ε² term at the corner are −1 and −1/3, while A′(t)=2t(1−t), yielding endpoint deficits ε/2 and ε/6 with O(ε²) errors. The cubic gain coefficient is 8/3+u−u²+v/3−v² for bounded rescaled deficits u,v; substituting those asymptotics gives 53/18. On the diagonal a single observation of variance η/2 is sufficient; differentiating 2εA(t)/(1+2εt) gives the optimal deficit ε/3+O(ε²) and the coefficient 26/9. Their difference is 1/18, comparing optimized designs rather than a fixed replication benchmark. Uniform analytic remainders and the localization justify using the corner expansion at the optima.

## originality

PASS

Best-of-knowledge pass for the fixed-two-sensor Brownian theorem, with the general Gaussian design criterion credited. Related results change the covariance, the sensor count, the target, or the observation/noise regime; their verified statements do not imply the joint conclusion.

## value

PASS

The design question has a nontrivial competition: at leading order maximal noise drives both measurements to the same endpoint, but for every finite noise the exact optimum is distinct and strictly interior. The sharp split, uniqueness in the singular regime and optimized cubic risk gap quantify the limits of replication rather than simply computing an objective at a few locations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
