# Colour silence of the symmetric 8-star under the diagonal split: disproof of the diagonally split Ammann-Beenker colour-contrast rigidity claim

## Context

The admitted target asked whether the standard Ammann-Beenker square-rhombus cut-and-project scheme with silver-mean inflation 1+sqrt(2) and regular octagonal window W, split along its main diagonal into colour windows W+ and W-, yields vertex sets that are each pure-point diffractive on a common Bragg module with a positive symmetric 8-star colour frequency gap preserved under one inflation step and normalized second-ring colour Bragg contrast at least 0.12. The target is a conjunction: falsifying any conjunct disproves it.

## Definitions

- Physical directions v_j = (cos(j pi/4), sin(j pi/4)), j = 0..3; internal directions vs_j = (cos(3j pi/4), sin(3j pi/4)).
- Window W = { sum_j (t_j - 1/2) vs_j : t in [0,1]^4 }: regular centred octagon, edge length 1, area 2(1+sqrt(2)) ≈ 4.828427124749.
- Colour split along main diagonal y = x: W+ = W ∩ {x <= y}, W- = W ∩ {x >= y}, each of area 1+sqrt(2) ≈ 2.414213562375.
- Symmetric 8-star: centre vertex with 8 unit edges in directions j pi/4, j = 0..7; internal offsets T = {tau_j = (cos(3j pi/4), sin(3j pi/4))}.
- Acceptance domain D = W ∩ (∩_{j=0..7} (W - tau_j)); D± = D ∩ W±. Standard regular-model-set uniform distribution gives colour-resolved frequency proportional to |D±|/|W|.

## Result

The admitted target conjunction is FALSE. The symmetric 8-fold star has exactly equal W+/W- colour frequencies (gap zero) for the main-diagonal split, so the clause requiring a positive gap preserved under one silver-mean inflation step fails.

Theorem (colour silence): let R(x,y) = (y,x). Then R(W+) = W- and R(W-) = W+ up to a measure-zero seam, R(W) = W by D8 symmetry of the regular octagon, R permutes the offset set T, hence R(D) = D and |D+| = |D-| exactly.

## Proof / evidence

Analytic proof as above, plus a replayable certificate (output/artifacts/verify_target.py, stdlib + numpy, exact convex-polygon clipping): W has 8 vertices, unit edges, centre 0, area 4.828427124749; D is a nonempty open octagon (8 vertices, area ≈ 0.142135623731, hence positive frequency and non-vacuous comparison); |D ∩ R(D)| = |D| with symmetric difference 0.0; |D+| ≈ 0.071067811866, |D-| ≈ 0.071067811866, gap ≈ 7.4e-14 < 1e-9; prints VERIFY_OK. Re-run confirmed independently during audit. Because the identity is a fixed-window geometric fact, sampling patches to any inflation depth samples the same domain D, so no silver-mean inflation step can make the exactly-zero gap positive; the inflation-preservation clause fails with the positivity clause.

## Limitations

The disproof covers the symmetric 8-star under the main-diagonal split of the standard regular-octagon window. It makes no claim about asymmetric patches (which may carry nonzero colour gaps), non-diagonal splits, or isolated second-ring Bragg contrast values; exploratory numerics showed ring- and vector-dependent contrasts, some above 0.12, but they cannot repair a conjunction whose frequency-gap clause is exactly zero. The polygon certificate is float-verified below 1e-9 rather than symbolic interval arithmetic; the exact equality rests on the symmetry theorem.

## Reproducibility

Run `python3 output/artifacts/verify_target.py` (requires numpy only); expect VERIFY_OK and the numbers quoted above.

## References

- M. Baake, U. Grimm, Homometric model sets and window covariograms, arXiv:math/0610411.
- A. Jagannathan, M. Duneau, Properties of the Ammann-Beenker tiling and its square approximants, arXiv:2308.07701v2.
- Tilings Encyclopedia, Ammann-Beenker entry, https://tilings.math.uni-bielefeld.de/substitution/ammann-beenker/
