# Scientific review: Parity-forced omission and a complete optimizer face for Kaczmarz sampling on endpoint-anchored paths

## Correctness — PASS

The universal bound follows from the tent-profile Rayleigh quotient, saturated by every noncentral comparison and both anchors. Explicit formulas yield a normalized distribution and an exact positive eigenvector. The ground-state sum of squares proves this eigenvalue is minimal, including at boundary distributions with an omitted row. Equality in the Rayleigh upper bound determines the full even singleton or odd one-dimensional optimizer set, rather than only symmetric samples. Asymptotics follow from the exact squared-tent sum. The exact Q(sqrt(2)) companion checker returned `VERIFY_OK 495` for dimensions 2 through 100 and five admissible odd-split choices; preliminary numerical/symbolic checks returned 71. The proof, not the finite checks, bears the all-order quantifier.

## Originality — PASS on inspected evidence, with risks

Strohmer–Vershynin (2007) analyzes row-norm sampling and general convergence. Gower–Richtárik (2015), Section 5.1, formulates an abstract one-step optimal sampling SDP; its formulas do not specify the optimal face for this anchored overdetermined path. Agaskar–Wang–Lu (2014), full paper Section 3, optimizes a different exact annealed MSE exponent via Kronecker-projection SDP, with random Gaussian examples. The 2014 ranking-design work of Osting–Brune–Osher concerns unanchored Laplacian connectivity. An indexed published-finding corpus theorem on inverse-positive SPD coordinate sampling establishes unique probabilities for square inverse-positive systems, which could encompass a *single*-anchored square subdesign, but neither the extra competing measurement nor the full odd optimizer segment. Generality and source comparisons are documented in `AUDIT.json`.

**Residual risks:** Unindexed equivalent literature remains possible; the closest square-design published-finding corpus item was accessible by indexed claim summary rather than entire source; relevant PDF text was read but requested page screenshots timed out. These caveats do not establish novelty by absence; they bound the evidence supporting the specific new claim.

## Value — PASS

For consistent sparse comparisons plus two absolute endpoint calibrations, an all-order exact E-optimal sampling law avoids repeated semidefinite optimization. The parity-dependent change in optimizer support is substantive: an even chain must omit its central row, whereas an odd chain has a complete one-parameter optimal face and can retain every row. The precise worst-direction one-step decrease scales as \(6/n^3\), with a transparent proof and implementation-ready weights.

## Limitations

Exact one-step fixed iid expected squared-error contraction only, not the exact annealed exponent or finite-horizon multi-step optimum; no noisy, adaptive, unequal-cost or block variants. Scientific literature overlap is not mathematically decidable from the checked sources. No independent validation was performed.

Self-review: passed. Independent audit: not yet performed.
