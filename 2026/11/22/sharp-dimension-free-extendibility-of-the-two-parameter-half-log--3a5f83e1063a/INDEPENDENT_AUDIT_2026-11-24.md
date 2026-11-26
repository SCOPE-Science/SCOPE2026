# Independent mathematical audit

## correctness

PASS

Solving the fractional-linear relation in exp(θu) gives Ψ^(-1)(z)=θ^(-1)log((1+αqz)/(1-qz)), with q=(exp(θ)-1)/(exp(θ)+α) in (0,1). For 0<α<=1 the two logarithmic series converge absolutely up to z=1; their combined coefficients w_k have the stated odd/even signs and sum to Ψ^(-1)(1)=1. Conditional product CDFs Ψ^k therefore give valid copulas with uniform mixture margins for every d. For α>1 the inverse is still smooth and H(t)=Ψ^(-1)(exp(-t)) has H''(t)>0, since each log term contributes positively to that derivative; H is decreasing and hence gives a bivariate copula. For the all-dimensional obstruction choose T>max(0,log(αq)). The absolutely convergent coefficients of H(T+s) give a finite signed atomic Laplace measure with mass w_2 exp(-2T)<0 at 2. If H were completely monotone, Bernstein–Widder would give a positive measure, whose exponential tilt would represent this same shifted transform; uniqueness rules that out. This does not rely on the series converging at t=0 for α>1, and the classical all-dimensional criterion only concerns the canonical construction. Differentiating the inverse shows -θH'''(0)=-1414190/27818127 at (α,exp θ)=(100,3); continuity gives a strict interior violation of the necessary 3-monotonicity. The θ→0 limit is independence since q~θ/(1+α) and H(t)→exp(-t). Replay: python3 /workspace/branches/independent_checks.py 5. An independent exact rational product check of the exponentiated three-dimensional rectangle volume (using generator-coordinate endpoints 99/100 and 199/200) gives a negative volume at α=100 and positive at α=1 when exp θ=3. The supplied script was read, not executed; that finite check is not the proof of the full threshold.

## originality

PASS

Credit the exact all-canonical-dimension boundary and its constructive weight law for this specified half-logistic family. Bivariate validity, the original generator, classical complete-monotonicity criteria and Laplace uniqueness are antecedents, not claimed discoveries. The closest indexed integer-frailty result concerns a different distortion and no inspected prior source specifies or implies this classification without the family-specific signed coefficient and tail argument.

## value

PASS

Bivariate validity of an existing family leaves open its legitimately usable canonical dimensions. The exact threshold resolves that question for every positive θ, and the constructive normalized frailty law gives a direct sampling and consistency mechanism. The trivariate witness shows that failure outside the range can be seen in a genuinely small dimension, while the signed-measure argument proves failure somewhere even when a low-order check does not.

The dated certificate retains the supplied scientific assessment, sources and limitations.
