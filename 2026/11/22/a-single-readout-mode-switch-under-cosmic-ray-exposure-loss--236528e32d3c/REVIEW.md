# Independent mathematical audit

## correctness

PASS

The known-variance Gaussian and a parameter-independent hit flag give clean information t²/(bt+σ²), weighted by exp(−λt); dividing by t+h gives the stipulated wall-time rate. The stationarity function strictly decreases from infinity to zero. Pointwise ordering of t²+st+p proves dominance/equivalence; evaluating stationarity at 1/λ gives the exact λ²p test, and λt<2. I independently checked the switch by setting T=(p1−p2)/(s2−s1) in the crossed case. Mode 1 is pointwise better exactly when t>T. At a tie the two optimizing times must bracket T, strictly: equality would imply a common optimizer by uniqueness, but the two log-time derivatives differ at T. Thus the envelope derivative of log(F1/F2) is t2−t1<0 at every zero. The low-hazard optimizer of mode 2 tends to infinity, and the high-hazard optimizer of mode 1 tends to zero, so the rate ratio lies above and below one at the respective ends. This gives existence, uniqueness and the downward jump without relying on the endpoint expansions. Independent Newton evaluation gave λ*=1.098884851672255, t1=1.358587148822112, t2=0.954820016525674. The adaptive extension uses conditional score orthogonality and bounds information divided by expected total completed cycle time, not a fixed-window stopping objective. The attached check.py and VERIFICATION.md were inspected, not executed. Overheads are fixed per mode, not necessarily equal; with equal overhead only dominance or identity is possible.

## originality

PASS

The supported distinct claim is the exact all-hazard classification for two separately optimized, whole-exposure-rejection modes: when there is a switch, it is unique and the preferred duration jumps downward. The inspected sources cover detector-specific readout optimization, partially salvageable ramps, hit detection, or switches of a different objective. No inspected statement supplies the same classification or a sufficient stronger result. This is a best-of-knowledge comparison, not priority certification.

## value

PASS

It answers a concrete design comparison not settled by finding a single-mode optimum: sums determine the low-hazard winner, products the high-hazard winner, and crossed rankings force exactly one abrupt downward change in duration despite smooth within-mode optima. The all-rate classification and the no-switch cases give a usable benchmark and do not depend on chosen example numbers. Value is for the stated background-dominated, whole-exposure-loss model, not empirical operating guidance or a claim about partially salvaged read ramps.

The dated certificate retains the supplied scientific assessment, sources and limitations.
