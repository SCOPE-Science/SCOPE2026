# Independent mathematical audit

## correctness

PASS

The final repaired claim concerns only the sharp failure exponent, its all-m bound and the uniform exponent example. Ordinary LS gives the intercept weights (Q−SX_i)/(mQ−S²); the denominator is positive almost surely for m≥2 by atomlessness. An extreme node detects the negative numerator, with the sign of S choosing the relevant endpoint, and S=0 gives weights 1/m. Replacing the extremes by ±R bounds the event by the two scalar left tails with equal probabilities under symmetry. The tilt log moment is strictly convex, starts with negative derivative and tends to +∞, so its minimum lies at a unique positive tilt and gives I_ν in (0,∞). Conversely, designate one independent node in [R−δ,R]; its positive probability incurs no per-sample exponential cost for fixed δ. A sum of the other nodes' X²−(R−δ)X below −2R² forces Q<(R−δ)S and S>0, hence failure. The Cramér lower bound uses open intervals around fixed negative means, eventually contained in this changing-threshold event, then continuity at zero lets those means approach zero. The positive/negative support follows from the positive mean and mass in a compact subinterval of (0,R). On that subinterval Y_δ is uniformly negative for all small δ, trapping the scalar optimizers in one compact interval; uniform convergence of the moments then passes the rate to δ=0. This verifies the final lower and upper bounds in both directions without replacing the random maximum by a deterministic endpoint in the lower bound. Completing the square and independently integrating the moment and its derivative verify the uniform exponent and minimizer to the displayed precision. The removed uniform three-node number is mathematically correct but is prior work, not an error in probability calculation.

## originality

PASS

This PASS applies only to the repaired finding. The frozen finding separately presented the exact three-node calibration as a contribution; that component has exact prior coverage for the same rule and was rejected on originality. The repair removes that theorem and its proof, credits the earlier record in related work, and retains the distinct endpoint-tilted large-deviation exponent. The closest inspected comparisons establish weight construction, sufficient positivity bounds, or finite-size probabilities and stability tails; none supplies the sharp bounded-symmetric exponent or mechanically yields a matching lower bound for this sign event. This is a bounded best-of-knowledge assessment, not a priority guarantee.

## value

PASS

For the standard unpruned rule, the probability of a wrong weight sign controls a practical distinction between typical accuracy and positive quadrature. The exact exponential cost sharpens known sufficient positivity estimates and distinguishes the scale of rare failure across sampling laws. The rate also explains why an inexpensive near-endpoint draw can realize the adverse tilt mechanism; a generic concentration bound cannot identify that cost. The uniform exponent is a useful numerical instance of the surviving theorem, not a claimed independently new recalibration of three samples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
