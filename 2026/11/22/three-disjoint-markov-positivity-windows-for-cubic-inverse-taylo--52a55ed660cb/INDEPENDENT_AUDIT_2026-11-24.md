# Independent mathematical audit

## correctness

PASS

For column distributions 1ᵀQ=0, so the update preserves total mass; its inverse exists since the triangular denominator has diagonal values E(h)/6>0 and 1. The transient block is the evaluation of the scalar inverse D_h(z)^−1 on a nilpotent shift, and the absorbing row is given by column-sum remainders. I independently expanded the finite geometric inverse of D_h as a truncated series and recovered all coefficients and the three displayed P,U,V, with Sturm variations (5,3), (5,5), (7,5). The calculation also recovers square-freeness and exact opposite signs in all four ordered rational isolation intervals. U is strictly positive because it has no nonnegative zero and U(0)>0. For the low-order numerators, RESULT.md line 54 overstates 'strictly positive coefficients': c_4 and T_4 have internal zero coefficients after the positive monomial is extracted. The required fact, as actually tested by check.py, is nonnegative coefficients with at least one positive term, which I verified and which gives strict positivity for h>0. At n≤6 only c_0 through c_4 and tails through T_5 are needed. At n=7 the two remaining sign constraints are exactly P≥0 and V≥0, allowing their roots as endpoints and excluding the interiors of the two negative bands. At h=0 the update is the identity, including for n=1. This proves the unchanged finding; independent exact replay is markov() in /workspace/calculations/algebra_checks.py. The supplied script was inspected but not run. The classification is for this family and exact arithmetic only.

## originality

PASS

The classical rational map, unshifted expansion, and undirected six/seven cutoff are existing results. The supported distinct claim is the full all-step sign classification on a directed absorbing cascade, together with its two active entries and narrow middle recovery interval. Neither the undirected heat result nor positive Taylor coefficients at the origin establish it.

## value

PASS

The homogeneous cascade is a natural nested family for testing whether a classical step transports probability distributions. Exact positivity at every step through six states, followed by two different mechanisms and an exceptionally narrow recovery window at the first failing size, shows why a single positivity threshold or numerical step grid is insufficient. The classification provides a reproducible benchmark without extrapolating to other generators or claiming accuracy on those intervals.

The dated certificate retains the supplied scientific assessment, sources and limitations.
