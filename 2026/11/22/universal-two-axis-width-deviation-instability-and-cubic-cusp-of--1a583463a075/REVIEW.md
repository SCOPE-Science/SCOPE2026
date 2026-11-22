# Review of the two-axis orthodiagonal width-deviation theorem

## Correctness
**PASS.** The claim uses genuine convex quadrilaterals with fixed perpendicular diagonal lengths and uniform directional width, and its normalization is the squared coefficient of variation. The exact four-vertex support maximum reduces each angular quadrant to one local crossover. Explicit triangular integration establishes the complete quadratic and coupled absolute-cubic terms, including a uniform fourth-order remainder for each fixed aspect ratio. The universal sign follows from two elementary, exhaustive bounds on \(\arctan t\). The resulting negative definite two-axis quadratic term proves local strictness, not an unsupported global extremum. A direct-vertex standalone numerical checker completed 203 regression tests. It is corroboration, not an infinite proof.

## Originality
**PASS with historical-priority risk.** Akiyama and Kamae's *Width deviation of convex polygons* (arXiv:2201.06736v1, 2022-01-18) formulates the objective, develops general moments, and explicitly singles out the unresolved four-gon case. A published exact random-width density for all **kites** (2026) gives stronger one-axis information than our intermediate one-axis formulas; these alone are therefore not claimed as new. The decisive new assertion concerns **generic non-kite orthodiagonal quadrilaterals** with both independent offsets, including the coupled \(|ts+h|^3+|ts-h|^3\) term and strict local instability over the complete fixed-diagonal two-parameter class. Neither inspected source supplies these claims; in particular, two separate one-axis kite calculations cannot determine the coupled cubic term. An earlier triangular-truncation variation concerns a different parent polygon. Indexed records and relevant primary text were compared by implication, not titles alone. Unindexed equivalent work remains possible.

## Mathematical value
**PASS.** The motivating gap is the unsolved four-vertex width-deviation minimization problem. The complete two-mode local response excludes every rhombus from being a local minimizer, retains both diagonals and area exactly, and identifies the two crossover ridges that distinguish genuinely non-kite perturbations. A third-order anisotropic profile and a universal negative-definiteness theorem provide more mathematical structure than a single perturbative example. This is a local theorem within a natural complete two-parameter subclass, not a global quadrilateral classification or a proven global minimizer.

## Closest literature and limitations
- S. Akiyama and T. Kamae, *Width deviation of convex polygons*, https://arxiv.org/html/2201.06736v1, especially Sections 1 and 7. The full publicly available preprint was inspected.
- *Three spectral singularities reconstruct asymmetric kites from random widths*, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-three-spectral-singularities-reconstruct-asymmetric-kites-from-r--0fca3299603f. Full RESULT.md inspected; its all-kite density dominates any one-axis kite moment calculation, but excludes the generic two-axis family.
- A prior triangle-truncation width-variation theorem describes a triangular rather than rhombic parent. A three-dimensional rhombic-dodecahedron width-variance record concerns a different body and invariant constraints.

The proof is local with a fixed aspect ratio; it does not give a global optimum or uniform neighborhood over degenerating rhombi. Numerical tests are finite. Publicly accessible sources do not rule out unindexed historical equivalents.

Self-review: passed. Independent audit: not yet performed.
