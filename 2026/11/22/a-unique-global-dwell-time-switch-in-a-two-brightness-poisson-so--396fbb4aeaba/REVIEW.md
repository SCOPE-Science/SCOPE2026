# Independent mathematical audit

## correctness

PASS

For the expected two-count detection fraction F, J'=D/(t+h)^2 with D=(t+h)F'−F, D(0)=0, D'=(t+h)F'', D(∞)=−1. The zeros of F'' lie strictly between 1/b and 1/a; their ratio equation has log derivative (b−a)[1/((bt−1)(1−at))−1]. The positive quadratic in the denominator has one maximum (b−a)^2/(4ab), so the ratio has at most two turns and at most three intersections with a positive level. At b/a≤3+2√2 the ratio is strictly increasing even at equality, which gives one positive critical point of J. Rolle from t=0 gives at most three positive zeros of D for arbitrary rates. For the fixed rate pair and unit overhead the two mixture endpoints give (+,−,+,−) at t=(1/20,1/10,1,3); affineness extends the signs to the entire closed interval. The three roots are simple, since a repeated one would add a fourth zero of D' to the three separate Rolle zeros. An independent rational enclosure using degrees 16 and 17 of alternating exp(−x/ceil x), propagated by positive powers, reproduced all eight signs and all decisive finite comparisons. Rounded enclosures for the short upper bound at p=0.22, J(2) lower bound there, J(0.07) lower bound at p=0.28, and the short envelope slope lower bound are respectively 0.2129995194, 0.2277718124, 0.2613469024, and 0.8680849799; the threshold comparisons were exact. The elementary e<49/18 bound handles the long branch at the upper endpoint. The envelope derivative is strictly positive for short minus long because the short contribution exceeds 1/2 and the long contribution is below 1/2. The opposite endpoint height preferences, vanishing boundary yields, and absence of other maxima establish a unique tie with exactly two global optima. Replay: frozen RESULT.md lines 23–77 and check.py lines 17–99 (read, not executed). The switch is unique only on [11/50,7/25]; the provided switch coordinates are diagnostic. No astronomical calibration is established.

## originality

PASS

The supported novelty is the unique mixture-driven global equality and jump of the two Erlang-2-CDF-per-clock-time optima at the stated rates and overhead. Known gamma-density modality and curvature, the count-detection probability, and the idea of survey dwell optimization are not new. The strongest same-day lookalikes were compared at the actual objective and claim level.

## value

PASS

A natural rate-versus-overhead design can have two widely separated global optima at one mixture fraction even though each pure class has one. The monotonic height comparison explains an actual discontinuity of the optimum and why a single local optimizer need not suffice. The chosen rational interval brackets a structurally meaningful switch rather than serving as an arbitrary numerical slice. This is an idealized survey-design benchmark, not a calibrated exposure policy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
