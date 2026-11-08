# Scientific review

**Claim reviewed.** For an unweighted simple wheel \(K_1\vee C_n\), \(n\ge3\), binary conformist/rebel responses have the four exact pure-equilibrium and strict-equilibrium count formulas stated in `RESULT.md`, with either all rim players rebels or exactly one rim conformist.

## Correctness — PASS
Every rim player has odd degree three, so its binary best response is uniquely determined by its neighbors. With a fixed hub action, an all-rebel rim is in equilibrium precisely when its zero vertices form a maximal independent set of the cycle. A transfer-matrix trace establishes the classical Perrin enumeration; the hub's own best response reduces to the half-size bound on the independent set. In the one-defect rim, a conformist at the designated position is forced to oppose the hub, forcing a length-four distinguished gap and leaving ordered two-/three-step internal gaps, which proves the composition formula and strictness. The edge cases with three and four rim vertices are explicitly resolved. The verifier directly implements the local decision inequalities and checks 52 type/size cases (524,224 profiles) plus the rational cycle-count identity. The all-size theorem rests on the analytic proof, not the finite checks.

## Originality — PASS (qualified)
The recent full-text works by Cao, Sánchez and Zhang (arXiv:2607.05932) and Pei, Cao and Zhang (arXiv:2607.10997) establish general network game frameworks and existence tests but do not state the wheel multiplicity/strictness phase table. Earlier full-text fashion-game work by Cao and Yang, and the 2019 dynamic matching-pennies analysis of Cao et al., treat different graph classes and/or limit-cycle behavior. Bisdorff and Marichal's cycle maximal independent-set/Perrin identity is expressly prior art and covers the all-rebel rim enumeration step alone, not the hub or defect cases. Searches of accessible semantic research records and overlapping mathematical results found no dominating equivalent claim. Plausible Shen–Lin graph/planar-fashion primary manuscripts were available only at abstract level, so priority is not established exhaustively; the accessible material did not reveal a decisive counterclaim.

## Mathematical value — PASS
The four exact cases form a natural complete classification of a hub-mediated network coordination/anti-coordination problem with a controlled single-vertex type perturbation. Its sharp disappearance of all equilibria with a conformist hub on even wheels, versus strictly stable rebel-hub equilibria whenever its composition count is positive, is an informative structural sensitivity boundary. The infinite-family counts and strictness distinctions go beyond a routine standalone cycle Perrin enumeration.

## Closest literature and limitations
The original pure-network fashion-game model and 2026 heterogeneous extensions provide the scientific setting; the Perrin count on isolated cycles is known. The theorem is confined to binary actions, uniform weights, one or zero rim conformists and pure equilibria. Unindexed equivalences and the unread full texts of Shen–Lin (2020; 2022) remain risks. No claim is made about arbitrary type words, behavior over time, or mixed equilibria.

Self-review: passed. Independent audit: not yet performed.
