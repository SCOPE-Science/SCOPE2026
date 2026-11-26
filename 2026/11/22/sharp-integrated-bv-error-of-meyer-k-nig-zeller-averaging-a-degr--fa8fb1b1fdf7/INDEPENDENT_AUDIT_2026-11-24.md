# Independent mathematical audit

## correctness

PASS

With the canonical endpoint traces and right-continuous sampling, integrate step responses against Df to identify the norm with the supremum over steps. In (s_{k−1},s_k] the sampled step is the negative-binomial tail, equivalently the Beta(k,n+1) CDF. Integrating the error on both sides gives E|B−s|. The density is positive on (0,1), so the cell error is strictly convex. Endpoint deviations from the mean k/(n+k+1) have magnitudes |k−n−1|/((n+k−1)(n+k+1)) and k/((n+k)(n+k+1)); each is at most 1/(n+k+1). Adding the exact beta standard deviation bounds the errors by (1+sqrt(n+1))/(n+k+1), making the proposed cutoff sufficient. Separately written exact replay: python3 /workspace/branches/611b221e-0a33-43e9-be8c-635fd8a01c1e/replay_record5.py (output replay_record5.out in the same directory). It exhausts the 326 rational endpoint candidates for degrees 1–7, uniquely selecting (1,left,0) in each, and checks the degree-eight witness E_{3,8}(3/11)=1260269246803/12553713506884>1/10. Thus every actual low-degree step is strictly suboptimal, hence so is any nonzero variation measure. The n=8 replay additionally finds an included winning endpoint 5/13, but the frozen claim correctly does not assert attainment for all n≥8. Integrating the survival polynomial (1−x)^(n+1)[1+(n+1)x+(n+1)(n+2)x²/2] verifies the stated witness formula; the logarithmic derivative of (x/(x+3))^(x+2) is positive and the derivative of the rational threshold is negative (the displayed factorization also checked symbolically), so n=8 proves the inequality for all larger degrees. For k/n→r in (0,∞), the independent gamma ratio CLT and exact variance give uniform integrability and scaled absolute errors sqrt(2/pi) sqrt(r)/(1+r)^(3/2). Every true jump within the cell is within O(1/n) of its mean and endpoint, so has the same subsequential profile. The exact variance and mean-shift bounds make the scaled values vanish if k/n→0 or infinity. The unique maximum of this profile at r=1/2 gives the norm limit and forces every asymptotically norming sequence of jumps to localize at 1/3. The supplied verification files were inspected, not executed.

## originality

PASS

The pointwise Gaussian profile and its maximizer are already visible for the same sampler, and the endpoint optimization mechanism also appears for other Bernstein-type operators. The precise integrated beta endpoint norm, its degree-eight transition with low-degree nonattainment, and the integrated near-norming localization are not supplied by the inspected results.

## value

PASS

The finite cutoff gives an exact degreewise norm benchmark for a standard positive sampler with increasingly dense samples near the right endpoint. The proof pinpoints when a boundary limit stops dominating, distinguishes nonattainment from strict interior improvement, and locates every near-worst single discontinuity at large degree. The degree-seven/eight split is an operator effect, not a floating-point threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
