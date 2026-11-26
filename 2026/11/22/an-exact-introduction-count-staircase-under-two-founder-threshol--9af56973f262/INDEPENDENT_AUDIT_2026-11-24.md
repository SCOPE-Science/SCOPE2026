# Independent mathematical audit

## correctness

PASS

For the abstract probability model, independence and the Poisson zero- and one-count masses give q_s(x)=1−s+s(1+x)e^(−x) and total failure q_s(B/m)^m. Taking the negative log gives B f_s(B/m), with f_s(x)=ℓ_s(x)/x and ℓ_s=−log q_s. Differentiation gives ℓ_s'=sx e^(−x)/q_s, and the sign of ℓ_s'' is that of (1−s)(1−x)+s e^(−x), strictly decreasing from 1 through its only zero above 1. Therefore N=xℓ_s'−ℓ_s starts at 0, rises, then falls strictly to log(1−s)<0 and has exactly one positive zero ξ_s; f_s'=N/x². The monotone sides of the peak imply strict adjacent-integer bracketing after clamping at one. At B=jξ_s the j-count wins and at B=(j+1)ξ_s the (j+1)-count wins; between these endpoints the two per-budget values are respectively strictly decreasing and increasing, so there is one crossing, with no nonadjacent ties. The brackets are disjoint, establish the complete step order, and give the claimed asymptotic and strict count error. For the first tie, put A=e^t−1−t at B=2t. Expansion gives P₂−P₁=s e^(−2t)[(1−s)A²−t²], so A/t=1/√(1−s); A/t increases strictly from zero to infinity. The stated degenerate s=0 and s=1 cases also check. These are equal expected trial sizes, not fixed total counts or unequal splitting. Replay: frozen RESULT.md lines 30–55; VERIFICATION.md and check.py were inspected, not executed.

## originality

PASS

The supported distinction is the exact all-budget adjacent-crossing law and first transition for this equal-mean, independently gated Poisson at-least-one objective. Qualitative intermediate optima and a related count staircase are not claimed as new. The closely matching per-site law with unequal splits and the closely matching staircase with an expected-number objective were compared separately. Older ecological priority remains provisional given access limits.

## value

PASS

In the abstract equal-mean stochastic trial problem, a continuous intermediate optimum alone cannot tell which integer trial count wins at a given budget. Strictly ordered unique switches, the complete equality classification, and the exact first transition answer that finite-budget question without having to check arbitrarily many counts. The result is a mathematical benchmark for the independent model, not advice for real-world introductions or a claim about unequal allocations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
