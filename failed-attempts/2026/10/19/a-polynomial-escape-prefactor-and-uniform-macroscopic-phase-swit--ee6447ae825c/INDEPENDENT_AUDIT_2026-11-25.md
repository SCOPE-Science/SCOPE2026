# Independent mathematical audit

## correctness

PASS

The five disjoint cell images verify the stated adjacency and slope 2, so each itinerary of n observations has mass 2^(1−n) times its last cell length. Endpoints and all their preimages are null. The rational resolvent and the root formula agree exactly; a separately written rational interval replay agrees for n=1,…,8, including p_8=299/768 and an exact decomposition by first switch or no switch at n=8 (independent_replay.py in /workspace/branches/008fffad-6afa-493c-a019-e6af79698cef/). No reliance on the larger timed-out replay or on execution of the uploaded checker. The two primitive blocks have the same positive simple Perron root γ with strict subleading modulus. The cross term uses the only edge A→B, so bulk indices have mass 2^(1−n)γ^(n−2)c, up to a geometrically decaying relative error in distance from the ends. Perron normalization gives c=11/120+√5/24 and 2c/γ²=(2+√5)/30. Pure-phase and bounded end-window masses are smaller by a factor of order 1/n after conditioning. The Riemann sum gives weak, not exact finite-horizon, uniformity. The leading upstream mass vector is proportional to (γ,1), yielding the stated initial weights.

## originality

FAIL

The evaluated formulas do not appear verbatim in the inspected prior passages. Nonetheless, the earlier same-hole graph already specifies the full Lebesgue survival generating function by direct cell-length weighting and elimination, as reconstructed below. The macroscopic law and initial localization are direct two-class consequences of the published reducible-chain power asymptotic, after an elementary disjoint refinement of the same interval coding. Thus neither the polynomial order nor the stated conditional laws establish a distinct structural claim beyond these prior inputs. The different-system indexed analogues alone would not establish coverage.

## value

FAIL

The same-hole conditional question is naturally motivated, but the leading coefficient and entire survival sequence are routine evaluations from an already specified interval graph. The two conditional claims use the ordinary no-return Markov conditioning identity with the known power asymptotic; they require no additional dynamical mechanism or nontrivial new estimate for this example. The evaluated numbers are convenient, but no independent mathematical gain beyond that exact extraction and the direct corollaries survives.

The dated certificate retains the supplied scientific assessment, sources and limitations.
