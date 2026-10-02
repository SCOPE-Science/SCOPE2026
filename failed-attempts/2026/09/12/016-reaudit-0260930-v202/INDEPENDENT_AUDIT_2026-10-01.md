# Mathematical audit — 2026-10-01

## Final claim

CFN triangle-versus-sunlet ideals differ via the split minor q0000 q1111 - q0011 q1100

## Correctness — PASS

PASS. Direct substitution into the stated CFN Fourier parameterizations gives exact factorization of the split minor on the single-triangle model. At the explicit stochastic 4-sunlet point, fresh exact arithmetic gives q0000=1, q1111=23/28800, q0011=1/120, q1100=11/240 and hence f0=1/2400, so the polynomial is not in the 4-sunlet ideal. This proves the two vanishing ideals are unequal.

## Originality — FAIL

FAIL. The scientific implication is already covered by established split-invariant and level-1 CFN machinery. Cummings, Hollering and Manon reduce CFN level-1 invariants to sunlets and determine all quadratic sunlet invariants; the toric-fiber-product/cut-edge formalism makes the displayed determinant a standard 12|34 split minor on the triangle side. Thus an explicit nonzero evaluation on the 4-sunlet is a witness for a distinction supplied by prior invariant theory, not a new mathematical result.

## Scientific value — PASS

PASS. An explicit low-degree stochastic separator between a single-triangle quarnet and a 4-sunlet is useful for model diagnostics and is naturally motivated by phylogenetic identifiability. The record is rejected scientifically only because the distinction and the split-minor mechanism are already covered.

## Sources inspected

- J. Cummings, B. Hollering, C. Manon, Invariants for level-1 phylogenetic networks under the Cavender-Farris-Neyman model — https://arxiv.org/abs/2102.03431: BROADER_COVERAGE. Primary abstract/result description: reduction of CFN level-1 invariant problems to sunlets and determination of all quadratic sunlet invariants.
- E. Gross, R. Krone, S. Martin, Dimensions of Level-1 Group-Based Phylogenetic Networks — https://doi.org/10.1007/s11538-024-01314-z: MECHANISM_COVERAGE. Primary full-text sections on toric fiber products and cut-edge decompositions for group-based network ideals.

## Residual risks

- The exact numerical witness 1/2400 may not be printed in prior work; originality fails because the mathematical distinction and split-minor mechanism are already implied.
- The result remains correct as a reproducible example despite scientific rejection.

## Disposition

**failed**
