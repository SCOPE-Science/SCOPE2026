# Independent mathematical audit

## correctness

PASS

For fixed theta in [1/2,1), A=a0>0 and nonincreasing nonnegative rates, I recover both branch laws from Definition 3 of Scott–McCallum–Foster. At r_m=c_theta the ordinary branch adds zero jumps and the alternative binomial would retain all m jumps. Uniformization at rate A bounds exact-chain paths of three or more jumps by O(h^3); P>=3 has the same bound and the active second-stage rate is at most (1-theta)A. Write s=theta A, b0=(1-theta)A, b1=A(r1-c_theta)/(2 theta) when r1>=c_theta. In the ordinary branches the numerical mass at 0 is exp(-Ah), and the h^2 coefficient of the mass at 2 is b0^2/2+s b1+s^2/2=A a1/2; normalization and first-order mass give the exact coefficient at 1. Changing the P=1 outcome to Bernoulli thinning changes the first-order mass at 1 by s(p1-1), with opposite mass at 0. If P=1 is ordinary but P=2 thins, the h^2 perturbation is (s^2/2) times Binomial(2,p) minus unit mass at 2. The given indicator witnesses give strict nonzero coefficients in both unsafe regions. The safe boundary is inclusive, with theta=1/2 allowed and r=1 safe for all admissible theta. Sharpness is over bounded tests, not a claim for each individual test. The result is local from the specified state, not a global convergence claim. Reconstruct from RESULT.md lines 20–65 or the coefficients above. VERIFICATION.md and verify.py were inspected as evidence, not executed; the analytic argument supplies the uniform-in-h tail bounds and quantifiers.

## originality

PASS

Credit the sampling algorithm, earlier weak second-order framework and generic O(h) local error bound to the literature. The supported distinct claim is the sharp unconditional three-regime classification for a bounded nonincreasing pure-birth channel, including explicit defect coefficients and the necessary-and-sufficient second-order boundary. Neither the original article's expansion and bound nor the inspected related same-day record states or mechanically implies this classification. This is a best-of-knowledge comparison, not a claim of historical priority over the distinct same-day result.

## value

PASS

The positivity adjustment changes the generator already at order h in one explicit region and preserves generator consistency but loses order two in another. Exact ratio cutoffs, including when no choice of theta can restore consistency, are useful for choosing or diagnosing the method even in this deliberately simple channel. The sharp witnesses and the transition driven by predictor count two add information beyond a generic local upper bound. No network-wide or global-order conclusion is needed or credited.

The dated certificate retains the supplied scientific assessment, sources and limitations.
