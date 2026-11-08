# Scientific review

## Correctness — PASS

The energy-normalized mean-zero evaluation functional has the centered Kirchhoff Green representer. Its diagonal is exactly the integrated effective resistance divided by total arclength, less half the double resistance integral divided by squared total arclength. Every cactus block lies on a tree of blocks and carries either an interval resistance or a circle resistance. Pushing arclength onto each block produces the explicitly integrated pointwise potentials and double integrals, with no missing cross terms. Bridge profiles have second derivative \(2\); cycle profiles between consecutive positive-mass attachments have second derivative \(-2M/\ell\). These signs, the upward derivative jump at attachments, and the branch-derivative sum eliminate all excluded maxima. The finite candidate formula covers every case, including trees and the pure circle. The non-antipodal example checks exactly with \(F_{\max}=2341/75\), \(J=4033/10\), and \(T=15\). A separately implemented numerical-method formulation solved with **exact rational** matrices reproduced 264 pointwise instances across eight sample cactus geometries. This computation is corroborative, not a proof in all sizes.

## Originality — PASS (qualified)

Solomyak (arXiv:math/0206235, §§1–3) proves graph-independent approximation bounds, not this sharp cactus Green-diagonal optimization. Baker–Faber (arXiv:math/0407428, Theorem 9 and Exercise 12) supply the **known** resistance series/cut-vertex laws and piecewise-quadratic regularity; these are used as prerequisites, not claimed as new. Wang–Pan (arXiv:1511.03080, §§1–3) optimize a *discrete vertex-pair Kirchhoff index* over unit-edge combinatorial cacti, not continuous mean-zero Sobolev point evaluation. Earlier exact cactus subfamilies give antipodes or pendant endpoints, and do not cover arbitrary multi-anchor cycle localization. Research-record searches using the exact objects, candidate formulas and equivalent Green terminology did not find a statement determining the full sharp constant, all norming points, and their non-antipodal behavior. This is best-knowledge originality rather than a proof of absence: an old general Green-function framework could conceal a closely equivalent corollary, and unindexed literature remains a risk.

## Mathematical value — PASS

The object is an exact sharp embedding norm over the natural infinite class of metric cactus graphs with arbitrary positive real edge lengths. The block correction is not merely a qualitative upper bound: it supplies a finite **closed quadratic envelope** that computes the entire norming set and equality functions for each graph. The non-antipodal global extremizer on a three-loop network demonstrates genuinely new localization relative to one-anchor rose and linked-loop patterns. This makes the exact invariant useful for evaluating and comparing connected graph geometries and for selecting point-observation locations without continuous optimization. The claim does not depend on a paper-sized downstream theorem.

## Closest literature and residual limitations

The closest general foundation is the metrized-graph resistance calculus of Baker–Faber (2004/2005), and the nearest cactus-specific optimization is Wang–Pan's discrete Kirchhoff-index problem (2015). Specific previous sharp evaluations for trees, roses and linked loops are contained as boundary cases, not independently claimed. The theorem does not cover overlapping cycles, nonconstant edge densities, vertex atoms or other Sobolev exponents. Priority requires independent literature review. The exact checker does not certify the universal proof.

Self-review: passed. Independent audit: not yet performed.
