# Independent mathematical audit

## correctness

PASS

Whitening reduces the Gaussian nodes and the kernel distance to standard coordinates. Completing the square gives q_i=(1+2h)^(−d/2) exp(−h‖z_i‖²/(1+2h)); the Gram inverse has positive denominator and both numerators are positive precisely when |‖z_1‖²−‖z_2‖²|<(1+2h)‖z_1−z_2‖². Orthogonal sum/difference coordinates U,V are independent standard Gaussians. Conditional on V≠0, U·V/‖V‖ has a fixed N(0,1) law independent of V; the ratio is therefore |Z|/χ_d, equivalently |t_d|/√d. Independent chi-square normalization gives the stated beta probability and complementary beta survival function of H=(|Z|/χ_d−1)_+/2. For H>0 exactly one sign changes; H=0 is an atom with no sign change at positive h. The small-beta endpoint gives the stated c_d, and layer cake yields convergence exactly for positive p<d, including logarithmic divergence at p=d. At fixed beta endpoint z, substitution x=z s^(1/b) in the beta integral and the gamma ratio give z^b(1−z)^(−1/2)/√(πb), b=d/2, which checks the dimension asymptotic. Strict monotonicity follows by the positive ratio density and coupling χ²_{d+1}=χ²_d+G². The exact flat-limit checks at d=5 and d=6 are 1/2+4/(3π) and 43/(32√2), on opposite sides of 0.95. The infimum is one-sided because the Gram matrix at h=0 is singular.

## originality

PASS

The distinct claim is the all-dimension law for positivity of both unconstrained finite-shape weights, including the per-pair threshold distribution, tail and reliability cutoff. The inverse-Gram construction, Gaussian kernel means, and Student/beta distributional identities are known ingredients. The closest inspected random Gaussian design reports averaged proportions, not this event's exact law; the related indexed three-node result treats a different, flat-limit Lagrange sign criterion. The available statements neither give the standardized two-node sign reduction nor imply the claimed probability and threshold family by specializing parameters.

## value

PASS

The sign question is motivated for random unconstrained Bayesian quadrature, where prior numerical work measured positivity. This result gives a calibrated exact confidence in the smallest nontrivial design, not just an example of negative weights. The dimension-six uniform cutoff separates designs with and without a 95% guarantee across bandwidths, and the sharp shape-moment frontier identifies when a mean or variance of the required tuning parameter exists. These are independently useful design benchmarks despite the intentionally narrow setting.

The dated certificate retains the supplied scientific assessment, sources and limitations.
