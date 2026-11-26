# Independent mathematical audit

## correctness

PASS

The original BPL PGF agrees with the factored PGF. Its log gives v_k as claimed; for b≤q all v_k>0 and the log intensities are summable, while b>q forces negative even v_k eventually. Independently, if all thinning PGF quotients P(z)/P(1−c+cz) are PGFs, expansion at c=1 makes the coefficient at z^k (1−c)(v_k−v_{k+1})+O((1−c)^2), so every adjacent difference must be nonnegative. The even-index normalized difference A−UR^k−VT^k increases when b≤q, and later odd ones strictly exceed A−UR²≥0 if d₂≥0. Conversely, when all differences d_k≥0, their sum is v₁, with exponential tail. Integrating the logarithmic derivative along z↦1−exp(−s)+exp(−s)z represents the thinning quotient as the PGF for Poisson batch arrivals surviving independent unit-rate deaths over s in [0,−log c]. This verifies sufficiency and the stationary process interpretation. Independent rational reproduction at θ=1/10 gave the claimed pairs: (−4490/53361,388100/12326391), (137971/5336100,252509699/12326391000), (19226/53361,−479344/4108797). The b=0 point is explicitly an endpoint comparison, not a violation of the stated strict α range; by continuity failure also holds for small positive b. The frozen checker and verification were inspected, not run. Replay: frozen proof §§1–5 or the quotient and batch argument above; the finite grid alone does not decide infinitely many indices.

## originality

PASS

Credit the BPL law and PGF to its primary authors, the general canonical-sequence criterion to prior discrete self-decomposability, and the exact BPL ordinary compound-Poisson boundary and intensities to the distinct indexed overlap when comparing claims. The supported distinct claim is the exact thinning domain within the CP domain, with the two-comparison theorem and explicit creation/destruction witness, not any of these inputs by itself.

## value

PASS

A uniform-in-retention distributional property reduces to two exact coefficient comparisons in a standard statistical count model. The signs locate a finite restoration interval and show that an extra Bernoulli term can create as well as destroy thinning self-decomposability without crossing the CP boundary. The construction of compatible batch immigration gives an explicit process using the criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
