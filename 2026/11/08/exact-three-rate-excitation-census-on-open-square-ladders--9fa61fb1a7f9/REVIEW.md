# Scientific assessment: open-ladder three-rate excitation census

## Correctness
**PASS.** The paper's published finite-graph activity theorem [Gravner–Lyu–Sivakoff, arXiv:1610.07320v1, Theorem 3] is applied on a connected finite graph and uses the cycle mean of the signed initial-color form. The CCA-to-GHM factor three follows from an explicitly given vertex potential. Every simple cycle in the open ladder is a rectangle spanning consecutive squares; its winding is the sum of their charges. An adjacent equal nonzero face-charge pair gives a six-edge cycle of mean one; without such a pair, a run of \(k\) charges contains at most \(\lceil k/2\rceil\) positive contributions, bounding all means by \(3/4\). The exact transfer matrices and their rational generating functions prove the all-size population recurrences.

All exact symbolic rational-function equalities were reproduced, and independent direct simulation checked both update rules at every initial coloring through five rungs. Brute initial-color enumeration and integer transfer verified another rung and transfer recurrence values through 30 rungs. Finite checks do not establish the infinite theorem by themselves; all-size deductions use the preceding structural proof and finite-matrix identities.

## Originality
**PASS, with historical-priority qualification.** The two relevant general primary papers give arbitrary-graph cycle criteria but do not evaluate the three-phase distribution and its two rational generating functions for \(P_n\square K_2\). A related earlier open-ladder count concerns initial primitive period-three states; an initial period-three count does not determine the eventual excitation rate of an arbitrary state. Other graph-specific excitation censuses concern different graph families or conditions.

Equivalent terms checked include Greenberg–Hastings, graph GHCA, CCA, cycle-density, winding, adjacent charged faces, transfer matrices and ladder strips; no covering ladder-specific enumeration was identified. Search coverage is necessarily imperfect, particularly for unpublished or unindexed sources. No absolute first-discovery claim is made.

## Value
**PASS.** The result provides a natural all-size activity phase diagram, an exact initial-color census and a sharp *local two-square witness* for global maximal activity. It separates the strict initial-period-three question from eventual excitation basins and proves that, despite every individual square supporting only rate \(3/4\), two adjacent squares can sustain rate \(1\), which becomes overwhelmingly likely on long ladders. The exact exponential survival tail makes a quantitative prediction for random initial conditions without requiring numerical dynamics.

## Limits and closest literature
Gravner–Lyu–Sivakoff (arXiv:1610.07320v1), Theorem 3 and proof, provides the general rate and synchronization theorem; Doba (DOI 10.25088/ComplexSystems.27.2.101), Sections 6–7, gives an independent GHM maximum-cycle-density characterization. Neither provides the evaluated open-ladder recurrences in the inspected relevant material. Results for immediate period-three states and for cyclic ladders do not imply these all-initial-coloring phase probabilities. The exact entry-time law, primitive periods of eventual orbits and historical priority remain unresolved; independent external verification is outstanding.

Self-review: passed. Independent audit: not yet performed.
