# Scientific review: three-block cyclic Ehrhart period

## Correctness — PASS

The exact lattice-point enumerator is reduced to block-sum heights using the composition weight \(w_a(r)=\binom{r+a-1}{a-1}\). Since the maximum of the three pair sums is the total minus the minimum, the finite geometric-series identity gives a precise decomposition into a simplex series and positive minimum-height layers. Expanding the layers as a polynomial in their height proves a rational series with poles only at \(\pm1\). The top height coefficient at \(z=-1\) is nonzero, giving the exact pole order \(3a-2\) and Laurent coefficient \((3a-3)!/(2^{3a+1}((a-1)!)^3)\). The pole at \(1\) has order \(3a+1\) by full-dimensional Ehrhart theory. These prove the claimed denominator and alternating coefficient for every integer \(a\ge2\). The standalone checker passed 110 exact assertions; finite checks support but do not replace the analytic argument.

## Originality — PASS (historical priority provisional)

The motivating preprint arXiv:2607.22008 explicitly supplies exact vertex denominator two and only an *upper bound* of two for the quasiperiod, and formulates further odd-cycle questions. The new result rules out period collapse and evaluates the first oscillatory term in every block dimension. The exact scalar triangle case in arXiv:math/0606163 is prior work and is not included in the asserted new parameter range. The graph fractional stable-set model of arXiv:1603.09613 uses individual edge inequalities, not these pairwise block-sum inequalities for \(a\ge2\). The historical research records checked did not show a dominating result. Unindexed equivalent formulations remain a priority risk; this is not independent certification.

## Value — PASS

The minimum quasiperiod of a rational polytope can be smaller than its vertex denominator. The motivating work leaves that distinction unresolved even for odd cyclic block models. The exact denominator, nonvanishing of the parity oscillation, its precise order, and the all-parameter coefficient settle a natural infinite family in dimensions \(6,9,12,\ldots\). This is a structural Ehrhart theorem rather than an arbitrary small enumeration or restatement of the period-two upper bound.

## Boundaries

Only three equal-sized blocks are treated. No claim of a full odd-cycle classification or independence from all earlier mathematical literature is made. The computer checks are finite; they are not independent mathematical verification.

Self-review: passed. Independent audit: not yet performed.
