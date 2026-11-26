# Independent mathematical audit

## correctness

PASS

The frozen decimal expansion of η* was incorrect at the printed precision (the supplied checker substituted a machine float into the gain formula). The exact definition and all preferences survive. The repair corrects the expansion in RESULT.md and SLOGAN.txt, and supplies exact rational bounds in verification.py and VERIFICATION.md. Independently integrating the bridge kernel gives the stated squared-covariance gains and baseline 1/30. The position derivative changes sign once until its stationary branch reaches 1 at η=11/336, with t=1 uniquely optimal at equality. The velocity stationary condition has a strictly increasing noise map on the interval from the noiseless optimum to √6−2. The optimized log-gain ratio has strictly negative derivative, including across the position endpoint stage by the unique-optimizer envelope identity: Vp≤1/12<6/25<Vv at the velocity optimum. Exact comparisons at 11/336 and 1/25 give opposite signs; velocity stationarity and gain equality give (Jp(1)−Jv)Vv′=(Vp(1)−Vv)Jv′. This gives the stated polynomial, with opposite endpoint signs and all seven derivative Bernstein coefficients in (−53,−52). Monotonicity of Jv,Vv on the narrow rational time enclosure bounds the gain-equality quotient and places η* strictly between 0.03486395077318212468 and 0.03486395077318212469. This certifies the corrected digits; independent replay uses no packaged code. The corrected final statement has exactly the two stated tie designs at η*, one elsewhere.

## originality

PASS

The final corrected claim is the joint two-mode decision and its two thresholds. Integrated-bridge covariances, the Gaussian design criterion, and even the same bridge's derivative-only time classification are not claimed as new. The closest joint-modality result concerns a different process and scalar loss. The correction to the numeric expansion does not create new priority.

## value

PASS

With a resource limit of one observation, sensor choice and timing need not optimize the same feature of the prior. The exact terminal-placement stage and later jump to an interior velocity reading answer that joint decision for every positive noise level. The observation-variance separation explains why the crossover cannot recur and provides a reusable design argument, not just a fitted crossing number. Correcting the decimal leaves this contribution intact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
