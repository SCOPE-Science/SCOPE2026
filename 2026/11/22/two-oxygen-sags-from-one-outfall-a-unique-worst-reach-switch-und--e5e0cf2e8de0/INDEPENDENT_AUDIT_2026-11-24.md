# Independent mathematical audit

## correctness

PASS

The Finding is unchanged; the repaired proof corrects the direction of approach in frozen Step 4. At a finite endpoint, t2(d) approaches d_end from below, not from above. For t>=d the weighted slope is G(d,t)=exp(cd)[f(d)-cU(d)]+integral_d^t exp(cs)f'(s)ds. It decreases strictly in t, and at fixed t its d derivative is c(b-c)exp(cd)U(d)>0. Thus G(d,d_end)<0<G(d,d) in the two-peak regime with finite endpoint and d<t2(d)<d_end; the limiting height is f(d_end)/c=U(d_end)<U(t0). On constant-rate reaches the weighted derivative crosses zero at most once and f, U and the downstream solution vanish at infinity. The lag integral for U/f has a positive expanding domain and nondecreasing integrand by nondecreasing hazard, giving strict monotonicity, all right-derivative regimes, and no extra extremum at either boundary. Moving the interface later strictly lowers the profile after the later interface, hence strictly lowers the downstream peak. At t0 the peak is higher than the reference; at an infinite endpoint the upper bound U(d)+f(d)/c tends to zero. Continuity then proves the unique tie and full global-maximizer comparison. The explicit example and exact bracket were independently checked with rational Simpson error bounds for log(3) and range-reduced alternating bounds for exp(-2d); the residual is negative at 1.091575 and positive at 1.091576, and strictly increasing there. Replay: python3 /workspace/branches/b4bc7ca9-790d-426b-8018-e800fe183a83/independent_bracket.py. Frozen verification code was inspected but not executed; its sampled checks are not the theorem's proof.

## originality

PASS

The supported claim is the joint hazard-general one-interface phase diagram and unique worst-site switch, not the Streeter–Phelps equation, multi-reach modeling, or the existence of double sags by other mechanisms. The repaired finite-endpoint proof does not change this comparison. No inspected distinct result gives equivalent coverage; priority remains qualified.

## value

PASS

Separates the existence of a second oxygen minimum from its becoming the global worst location in a natural continuous one-outfall model. The result identifies both thresholds and distinguishes finite from persistent two-sag regimes; the exponential example shows the latter can still have a unique global switch. This is an exact idealized model result, not a prediction for a field river.

The dated certificate retains the supplied scientific assessment, sources and limitations.
