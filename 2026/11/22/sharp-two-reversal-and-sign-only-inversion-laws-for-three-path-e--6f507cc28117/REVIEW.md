# Independent mathematical audit

## correctness

PASS

For the corrected final claim in repairs/3/RESULT.md and SLOGAN.txt. The frozen assertion that the position-only inverse becomes ill-conditioned merely because D goes to zero is false for calibrated gaps and position perturbations; the unstructured matrix norm statement in the frozen proof is true, but concerns different perturbations. Set m=(Q₊+Q₋)/2 and d=(Q₊−Q₋)/2. Cramer's two numerators are 2e^(−qm)sinh(qd) and 2e^(pm)sinh(pd), while D=2e^((p−q)m)sinh((p+q)d); cancellation yields positive even analytic ratios with bounded derivatives at each finite coalescence point. Gap sensitivity is O(d) and the limiting ratios satisfy the normalized value and derivative conditions at m. In contrast, for the forward perturbation b−B*=ε the sensitivities of the two switch positions to b diverge like 1/√(2pqB*ε). Strict convexity of H, H'(0)=ap−cq, and the positive limiting growth give the exact two-root window, tangency/no-reversal at b=B*, and the single positive reversal alongside the excluded Q=0 zero at b=a+c in the descending-start case. All other counts follow from the two monotone intervals or a wholly increasing profile. Strict positivity of K preserves signs but need not preserve differentiability: simple zeros are asserted for H−b. Invertibility and positivity of the two coefficients give all-pairs realizability and no absolute scale; any positive gaps can realize the same two thresholds, so calibration matters. At the minimum pL=qJ gives H''=pqB* and H'''=pq(p−q)B*; inversion of the signed square root of the Taylor expansion gives the stated cubic-order remainder and the same second-order displacement on both branches. Equal gaps give exact cosh symmetry. Independent replay: python3 /workspace/branches/independent_checks.py 3 verifies the numerical values of the exact example, stable formulas for six gaps down to 10⁻¹², and six asymmetric-fold roots. This does not prove the analytic extension or test a noise model. Frozen check.py inspected, not executed; its random counts share the phase formulas and are not evidence about structured conditioning.

## originality

PASS

For the repaired modeling claim: a complete positive-discharge amplitude window with a minimal calibrated switch-position recovery and a precise account of which sensitivities are singular. The constituent tools (strict convexity, standard fixed-basis interpolation, divided differences and the simple fold normal form) and the motivating salinity-difference proxy are not claimed as new. No available source establishes the complete specialized benchmark with its structured position-error interpretation.

## value

PASS

The hypothetical weak-overspill benchmark gives a useful low-information identifiability test: it separates when two reversals can exist from what supplied switching locations can identify. The corrected near-fold result prevents a mistaken inference of unbounded sensitivity of amplitudes to position errors from the raw determinant, while keeping the distinct difficulty of resolving switches and the forward fold. The result is conditional on known rates and a specified three-path model, not validation of the model or a guarantee for field measurements.

The dated certificate retains the supplied scientific assessment, sources and limitations.
