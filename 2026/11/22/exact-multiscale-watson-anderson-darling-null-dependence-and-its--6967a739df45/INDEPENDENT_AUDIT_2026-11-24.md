# Independent mathematical audit

## correctness

PASS

The probability integral transform gives iid uniforms under the fully specified continuous null, and Hwang–Kuriki Theorem 3.3 confirms the 1/n Watson sample-kernel normalization. Splitting the Anderson–Darling kernel integral at the two order statistics gives a(x,y)=-1-log(max(x,y)(1-min(x,y))). Both kernels have zero one-argument averages. The Watson diagonal is constant and all mixed terms except matches of the same off-diagonal unordered pair vanish by conditioning, giving 2(n-1)/n times the mixed kernel inner product. Integrating over a triangular half-square at fixed separation z gives the weight 2(1-z)+4z log z. Monomial integration proves rationality. For the alternate identity one can integrate twice with B_(2m+2)(z)-B_(2m+2)(0); the endpoint terms vanish, the weight's second derivative is 4/z, and Bernoulli reflection symmetrizes it to 2/[z(1-z)]. For the AD moments, the integral of log y times log(1-y) is 2-zeta(2); this gives diagonal variance 4-pi^2/3 and off-diagonal second moment pi^2/3-3 by integration on x<y. Watson's variance follows from orthogonality and its deterministic diagonal. The squared Fourier coefficient of the centered indicator is 2(1-cos(2 pi k t))/(2 pi k)^2, giving the strictly positive mixed series. The normalized covariance in order is proportional to P(s)/sqrt(Q(s)); the P-weights relative to Q-weights have strictly increasing ratio I_k k^(2s-2) for s>=1, so the log-k expectation is strictly larger and the correlation drops. The ratio (n-1)/(2a(n-1)+b) is strictly increasing in n, and first-harmonic dominance yields the explicit positive order limit. A separate exact-fraction/high-precision replay gave kappa_1=1/36 and kappa_2, kappa_3, kappa_4 equal to 7/10800, 41/2540160, 19/46656000. Its sequential order/sample limit was 0.64876433810494, and the large-n order-two correlation 0.66201059607981. Replay: /workspace/branches/a5f3ce4a-737a-47ba-a65d-dfb9fced1699/independent_check.py. The supplied checker was inspected, not executed; these finite checks support the analytic proof and do not extend its null hypotheses.

## originality

PASS

The order-one covariance is already in an earlier Resultary record and is expressly excluded from the novel scope. The checked generalized Watson source fixes the exact kernel and limiting marginal law; the checked components paper provides separate decompositions. Neither checked result gives the higher-order mixed finite-sample covariance or the strict order comparison and positive correlation limit. This distinction is limited to the stated simple null and the inspected sources; plausible older works with inaccessible text remain a priority risk.

## value

PASS

These statistics are often computed from the same null sample; marginal calibrations alone cannot quantify their redundancy. The exact covariance and order monotonicity show how integration changes that dependence, and the first mode gives a positive floor even for arbitrarily high order. This is meaningful beyond the classical normalization check and does not claim a joint law or a calibrated combined test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
