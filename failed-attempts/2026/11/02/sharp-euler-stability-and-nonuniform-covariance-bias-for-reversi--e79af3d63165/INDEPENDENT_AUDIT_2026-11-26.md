# Independent mathematical audit

## correctness

PASS

Conjugation by D=diag(1,√λ) gives D(δJS)D⁻¹=√c J; this is the identity needed for the displayed update (the normalization prose at line 58 puts an extra √λ in front of δJS). The diagonal raw moments are forced by 2h(1,λ) and propagated by the nonnegative symmetric T with diagonal squares (1−mh)²,(1−nh)² and off-diagonal 2ch. Its Rayleigh quotient at (1,1) bounds the absolute cross-moment multiplier. On (0,2/m), I−T has positive diagonal entries; det(I−T)/h²=mn(2−mh)(2−nh)−4c² decreases strictly and crosses zero once, at the smaller quadratic root stated. At and above 2/m, irreducibility makes the Perron eigenvalue strictly greater than the already ≥1 first diagonal entry. Positive forcing in the Perron direction proves the exact linear/exponential growth orders from zero and impossibility of any finite-second-moment invariant there. In the stable case the same-noise coupling contracts in mean square after finitely many steps, giving existence and uniqueness in W₂; the invariant mean vanishes as both drift multipliers are strictly inside the unit circle. The two-by-two inverse yields the stated diagonal covariance, and the positive resolvent applied to h²(m²,n²) proves strict inflation. Substitution c=1 gives the fixed-h limits. Writing R=√((1−λ)²+4c²), the gap numerator is 2(λ+c)−4c²/(R+1−λ) near c=0, and 1+λ−(1−λ)²/(R+2c) for c→∞. These yield the three scaling limits; expanding the exact denominator as 4[λ+c(1+λ)]−2mn(m+n)h+(mn)²h² gives 4c(1−t) to leading order at h=t/c². Both variance numerators are asymptotic to 4c. Read verify.py and VERIFICATION.md without executing the uploaded script; its finite samples are supplementary. Interpret the reference to optimized perturbation as the critical continuous-time scaling, not a claim that δ=λ^(−1/2) is a finite-λ maximizer of g; §4.2 Lemma 1 of the cited paper shows the covariance rate is increasing in δ for 0<λ<1.

## originality

FAIL

A distinct Resultary record, 494cc24da1b8, already covers the core result on a larger parameter set: same noise and Itô Euler scheme, identical sharp threshold, boundary/supercritical behavior, exact stationary covariance, strict bias and critical stability and variance limits. The additional power-law trichotomy and persistent-bias limit are direct asymptotic substitutions in those identical closed forms. This is demonstrated equivalent catalog coverage and implication, not a finding that the later catalog label establishes temporal priority or copying.

## value

FAIL

The exact stability frontier and bias are useful numerical facts, but the separate broader record already supplies them. After accounting for that coverage, the remaining c=λ^(1−2α) cases and h=t/c² bias follow by direct leading-term substitution in fully explicit formulas. The joint-limit interpretation is useful as a corollary, not sufficient as a separate exact contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
