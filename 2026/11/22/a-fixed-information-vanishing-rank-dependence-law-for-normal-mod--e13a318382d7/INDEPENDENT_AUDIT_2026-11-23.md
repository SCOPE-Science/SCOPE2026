# Independent mathematical audit

## correctness

PASS

The mixed derivative is bounded by 1±theta with uniform margins. Under the uniform reference, each of the m or n half-waves maps to the same arcsine law after reflection, so the entire likelihood-ratio distribution is mode-independent. This proves invariance of every finite density-value integral in the stated sense, not of arbitrary dependence measures. TV is one half theta times (2/pi)^2; chi-square is theta^2/4. Symmetry kills odd cosine-product moments in the uniformly absolutely convergent expansion of (1+x)log(1+x) on |x|≤theta<1. The jth even moment is the square of the central-binomial factor, giving the stated KL series and its strictly positive first term. The conditional CDF given U deviates from v by theta cos(m pi u) sin(n pi v)/(n pi). Its squared average, divided by the uniform-response normalization integral ∫v(1−v)dv=1/6, gives 3theta²/(2n²pi²); exchanging coordinates gives the other direction. Both classical concordances contain the factor (1−(−1)^m)(1−(−1)^n); in the Kendall formula the quadratic term is separately zero. The copula-CDF supremum is exact because each sine can independently attain absolute value one. Along the even-even sequence the divergence argument is fixed and strictly positive, so a positive lower calibration fails at that value even with common uniform density bounds. An independent 120-by-120 Gauss–Legendre calculation in /workspace/branches/6b723482-3a63-4963-b98f-7a2ea90253ee/independent_check.py gives KL 0.0320392688664850 and the two coefficients 0.002374715242 and 0.009498860966 at (m,n,theta)=(2,4,1/2). The finite check does not prove the universal formulas; the supplied midpoint checker was inspected read-only. At theta=1 strict positivity would fail and derivative bounds do not persist uniformly in mode; neither case is asserted.

## originality

PASS

Best-of-knowledge pass for the exact joint information-versus-directional-rank frequency law and separation, not for the model, concordance cancellation, or definition of xi. The ingredients are elementary once juxtaposed; no inspected result states the same quantitative comparison or entails it without the specific additional mode analysis.

## value

PASS

The construction refutes a plausible positive lower calibration of both directional xi coefficients by TV or mutual information, at exactly the same likelihood-ratio law across modes rather than just bounded-away alternatives. It also separates which axis controls which direction and shows why a uniformly positive, smooth density may still exhibit arbitrarily small conditional-CDF variance. The conclusion is operationally meaningful at the population level and does not purport to be a sample-power theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
