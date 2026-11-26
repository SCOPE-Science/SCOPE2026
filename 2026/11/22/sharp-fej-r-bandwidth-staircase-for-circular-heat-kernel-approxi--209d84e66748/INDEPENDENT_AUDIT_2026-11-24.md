# Independent mathematical audit

## correctness

PASS

For normalized Haar measure, Parseval gives the frozen objective with Fejér squared contribution (N−1)(2N−1)/(3N) after removal of the mean. The cross term is maximized simultaneously at zero phase; its strictly positive first harmonic forces that phase for N>=2, while N=1 is constant. Adjacent subtraction gives Δ_N=2/3−1/[3N(N+1)]−4 sum_(k=1)^N k exp(−tk²)/[N(N+1)]. The k-weighted average of the heat multipliers decreases with N, so Δ_N increases strictly in N and tends to 2/3 at fixed positive t. It increases strictly in t between opposite endpoint signs, giving exactly one root per N, decreasing to zero, and no ties except consecutive orders at those roots. At N=1 this gives log 4. For u=N²t, the normalized sum is I_1(u)+exp(−u)/(2N)+O(N⁻²) uniformly near the limiting root, with I_1(u)=(1−exp(−u))/(2u). Since I_1'(u_*)=−(u_*−2)/(6u_*), the threshold equation gives u_N=u_*−u_*/N+O(N⁻²); bracketing with the adjacent roots gives N_opt sqrt(t)→sqrt(u_*), including both orders at a tie. The limiting squared error is 2 times the integral on [0,∞) of [exp(−x²)−(1−x/c)_+]². Equivalently on the whole line the triangular profile is (1−|x|/c)_+; the omission of the absolute value in the proof's whole-line description is a local notation slip. The integral is strictly positive from its Gaussian tail. Evaluating it at c=sqrt(u_*) using 1−exp(−u_*)=u_*/3 yields the claimed J_*. Independent bisection and Simpson integration of the squared difference (32768 subintervals on each of [0,c_*] and [c_*,10]) give u_*=2.821439372122079, c_*=1.679714074514493 and J_*=0.010154696409760. Rounding the moment-match order leaves N~1/t; the heat and cross terms are O(t⁻¹/²), so the Fejér squared term is dominant and yields 2/(3t) and the stated ratio.

## originality

PASS

Pass for the discrete least-squares staircase and its sharp scaling and comparison, not for the Fejér or heat multipliers, the numerical root in isolation, or the general idea of moment matching. The closest same-day analogues are distinct results and were compared, not treated as priority evidence or discarded by date.

## value

PASS

Gaussian and triangular multipliers are standard and their normalized squared-distance comparison has a practical calibration interpretation. The exact integer selection, including all switching ties, is information not supplied by a continuum limit. The sharp asymptotics also show a quantitatively diverging penalty for the natural first-moment heuristic, not just a marginal improvement over it.

The dated certificate retains the supplied scientific assessment, sources and limitations.
