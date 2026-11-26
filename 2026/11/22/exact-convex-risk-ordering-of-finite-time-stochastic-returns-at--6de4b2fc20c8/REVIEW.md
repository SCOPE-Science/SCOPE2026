# Independent mathematical audit

## correctness

PASS

For ell>0, the return is the first passage of drift-a Brownian motion with generator d∂²+a∂ to distance ell. Its inverse-Gaussian mean is ell/a and variance 2d ell/a³. For d2>d1 the likelihood ratio is below one at t=ell/a, and rises to infinity toward either end of (0,infinity), monotonically on each side of that minimum. The +,-,+ density difference gives positive call gaps at the outer strikes by equal mass and mean and positive concave interpolation between the two crossings. Conditioning on the common exploration skeleton keeps the dependence between durations and alarm positions while making the return noises independent. Translation and independent convolution preserve call order, so averaging yields convex order. For any t>0 there is positive probability that the first exploration alarms before t/2 without exit and at a point distinct from x, and the next exits within t/2 before its alarm. On these skeletons the conditional single-return call gap at t-S>0 is strict, making each global positive-strike inequality strict. The second-derivative measure of a strictly convex test charges every nonempty interval of positive strikes, yielding strict test expectations whenever both are finite. A successful episode has positive probability q, attempts are geometric and stopped exploration durations have small exponential moments; bounded return distances and inverse-Gaussian moments suffice for total variance. The skeleton conditional mean is S+W/a² and variance 2dW/a⁴; the work and terminal side are skeleton observables. The killed rate-r resolvent has the stated Dirichlet kernel, and summing expected one-attempt work across renewals gives ar/q times its distance integral, strictly positive. Frozen verify.py was inspected: it is finite corroboration, and its same-formula transform comparisons do not add independent evidence. The conclusion relies on the crossing and conditioning proofs, not on Laplace-order checks.

## originality

PASS

Best-of-knowledge pass for the strict all-positive-deadline convex-risk law of the full two-target completion time under changing only return diffusivity. The parent already gives the exact model and renewal transforms; the mean, work distribution, splitting probabilities and the moment input are not new. The affine variance coefficient is useful supporting structure, also derivable from the earlier model transform; the substantive increment is the strict convex-risk result rather than the moment identity alone or a claim of a new inverse-Gaussian ordering criterion.

## value

PASS

It exposes a controllable source of duration risk in the exact motivating model that mean time, complete switching work statistics and exit-side probabilities cannot detect. Every positive-deadline overrun loss worsens, not just a few transforms or the variance; the latter's coefficient ties the effect to expected work. The conclusion is meaningful at fixed drift with targets inactive on return, and does not imply the same response for a physically coupled change of drift or active return targets.

The dated certificate retains the supplied scientific assessment, sources and limitations.
