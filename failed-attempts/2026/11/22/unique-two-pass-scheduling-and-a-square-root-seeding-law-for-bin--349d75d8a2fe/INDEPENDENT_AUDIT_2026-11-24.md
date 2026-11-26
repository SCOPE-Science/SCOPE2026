# Independent mathematical audit

## correctness

PASS

The allocation is retained and has the same law under reference and decoder, so forward KL is allocation-averaged conditional KL, not output-only KL. Markov screening at the nearest revealed flanks gives single-site entropy log 2-I_left-I_right+I_span and the joint gap entropy from the transition entropy; one missing flank gives the edge term. Independent marginal-entropy enumeration confirmed the finite formula in 60 cases (L=2,...,6 with endpoints p=0,1 included; maximum discrepancy 3.0e-15). At fixed interior parameters the edge and no-seed contributions vanish per site; sums give (1), with both endpoint costs I_1. Symbolic differentiation confirms the positive curvature of each geometric-information term and the opposite signs of the slopes at 0 and 1/2. Analytic expansion after division by the leading weight lambda²/2 gives endpoint slope 3 lambda²/4+O(lambda⁴) and curvature 4+O(lambda²), hence the stated weak-correlation coefficient. Independently for the strong limit, put delta=1-lambda and H_d=log 2-I_d. The correction to p log 2-H_1 is p times the sum of [2(1-p)-p(d-1)] H_d (1-p)^(d-1). This kernel annihilates d exactly. Insert the small-delta entropy expansion at d≤delta^(-2/3); geometric tails are exponentially small at p=c sqrt(delta) and the remainder is O(delta² p^(-2)(1+|log delta|)), uniformly on compact positive c intervals. The surviving d log(pd) term is a Riemann sum with integral of (2-x)x log(x) exp(-x) equal to -1, so b/sqrt(delta) tends uniformly on those c intervals to c log 2+1/(2c). Strict convexity and left/right secant comparisons with the unique minimizer of this limiting function trap the scaled minimizer, giving both sharp laws in the specified order of limits. Replay: python /workspace/independent_checks.py 2 (SymPy, NumPy, SciPy); frozen check.py and VERIFICATION.md inspected, not executed.

## originality

FAIL

There is demonstrable equivalent indexed coverage of the central frozen claim. The first-wave record has the same source, Bernoulli allocation, forward joint divergence, thermodynamic limit, strict convexity, optimizer interval, and both leading strong-correlation constants. The fixed-round theorem also delivers the strong-correlation laws at m=2. This is not a false theorem or a finding about publication order: the distinct records share the same displayed date, and priority is unresolved. Originality of the frozen combined finding is not established against this exact coverage. The weak-correlation coefficient is a routine Taylor consequence of the already displayed equivalent objective and its unique interior optimizer, not an independently substantial remainder.

## value

FAIL

The rare-wall optimizer and its sharp cost would be meaningful as an uncovered benchmark, but both are already supplied by the directly matching theorem and the fixed-round specialization. The remaining -3/16 coefficient follows by a routine Taylor calculation in the same optimizer equation. The frozen finding identifies no distinct motivated weak-correlation invariant or nonroutine advance that survives the overlap. No substantive valuable repair is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
