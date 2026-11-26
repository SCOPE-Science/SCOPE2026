# Independent mathematical audit

## correctness

PASS

For n>=3 the admissible upper indices are exactly 1<=k<=floor(beta n). With t={n alpha}, s_k={k alpha}, the identities alpha^2=beta and v(k)=2k+floor(k alpha) give {v(k)alpha}=beta s_k. Lower Beatty membership is {t-beta s_k}>beta. For t<beta this is the wrap condition s_k>t/beta, for beta<t<2beta it is s_k<(t-beta)/beta, and for t>2beta it holds for all k. Neither breakpoint occurs by irrationality. On length-q Fibonacci convergent blocks a translated rational q-grid differs by less than one grid spacing; only O(1) points near interval endpoints can change membership. Decomposing any length into O(log n) such blocks proves the uniform interval discrepancy. Hence Y_n is within O(log n/n) of the piecewise-linear tent-with-plateau profile, and equals one exactly on the plateau. On each dyadic block and uniformly in y<1, indicator disagreement is confined to at most two nonplateau intervals of total length O(log n/n); discrepancy gives O(log n) possible indices there. Summation proves the uniform log-squared estimate. Taking y up to 1 from below at fixed X and using the same uniform error immediately gives the stated exact-saturation count, independently of the separate proof of that count. Weak convergence and convergence of the stated moments follow. A new check compared 1798 direct pair counts with interval-certified rotation counts (python3 /workspace/branches/recompute_frozen.py); it does not certify the asymptotics.

## originality

FAIL

The 10/13 indexed Wythoff rotation-profile record baee5a907c94 already states the same weak limit after deterministic rescaling. Its proof supplies the exact circle-interval rule and uniform Fibonacci rotation discrepancy. Together these imply the exact plateau saturation and the uniform O(log^2 X) CDF and exact-saturation counting errors by a direct threshold estimate. This is established equivalent and implied coverage, not an inference from source titles, dates alone or inaccessible literature.

## value

PASS

The mathematical question is substantive: it distinguishes a limiting atom from actual finite-count saturation and controls thresholds uniformly just below the jump for this natural representation count. That usefulness does not make the covered result a distinct contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
