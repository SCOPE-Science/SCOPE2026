# Independent mathematical audit

## correctness

PASS

Backward Poisson spacings at a stationary observation time are independent rate-r exponentials. The sum of those spacings weighted by products of squared multipliers has mean 1/[r(1−m)] and converges in L¹. Conditional on the spacings and marks the independent Brownian increments give exactly the claimed Gaussian mixture, with D in the generator giving variance 2D per unit time. For uniqueness even from an invariant law of unknown moments, the common-noise difference equals the initial difference times a product with expected square exp(−r(1−m)t); truncate the finite initial difference and then use convergence in probability. The affine kernel preserves convex order in the previous clock and in the independent coefficient by conditioning; all stop-loss functions are 1-Lipschitz, hence pass to the L¹ limit. Jensen and the chord from zero to one give the exact coefficient endpoints; Poisson thinning gives the upper clock. Positive and negative half-power tests give the absolute moment and density directions; the latter is integrable since V≥E_0. Conditioning the normal MGF on V and testing exp(Dt²V) gives the common finite domain and sharp envelope. The generator recursion telescopes to the stated factorial product; finite exponential moments locally justify it. Jensen and B²≤B give the sharp kurtosis inequalities with the stated equality conditions; a mixture of the endpoint laws preserves m and interpolates E B². Independent exact replay at D/r=1 and m=1/4 substitutes E B^j=m^j, (1/2)^j/(j+1), or m into the recurrence. The three E X⁴ values are 512/15, 384/11, 128/3 with common E X²=8/3, giving kurtoses 24/5, 54/11, 6. This is a bounded check, not the proof of convex order. The frozen verification describes additional exact and seeded checks; its script was not executed.

## originality

FAIL

A distinct indexed work establishes the same strongest clock comparison and gives the further convex order of squared positions. It uses the same model, hypotheses, clock up to deterministic scaling, and sharp endpoints. The frozen MGF formula and other additions are direct consequences rather than a scientifically distinct remainder. This is a finding of demonstrable coverage in the checked corpus, not a priority ruling based on which date comes first.

## value

FAIL

The comparison is intrinsically useful for separating stationary shape from variance. As a distinct contribution, however, the frozen finding adds only selected transforms, a telescoped recurrence and simple consequences to a verified statement-level equivalent comparison. There is no new observable optimization or different regime in the frozen theorem that supplies independent value beyond that coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
