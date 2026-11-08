# Scientific review: cactus metric-graph distance jumps

## Correctness — PASS

The precise theorem is restricted to finite connected cactus metric graphs with positive edge lengths and arclength-uniform independent points. The block–cut tree forces a unique pair of endpoint articulation vertices for points in distinct blocks. Conditional distances then split into a deterministic route length plus independent endpoint-to-uniform-point distances: uniforms with supports equal to full bridge lengths and half cycle circumferences. The same-block law is triangular for bridges and uniform for circles. Differentiating the exact, fully normalized CDF isolates circle-block terms as the **only discontinuous density contributions**. Their jump magnitudes cannot cancel because all are negative. The proof establishes all real lengths, repeated cycle circumferences, pointwise boundary conventions and the tree case, without using enumeration as a proof of the infinite family.

The independent exact-rational replay checks mass, CDF/density correspondence away from knots, four cycle-threshold groups, and the near-zero coefficient. Monte Carlo simulations provide supplementary numerical consistency only. The code does not certify historical originality or all graphs.

## Originality — PASS (provisional)

Closest inspected primary sources:

- Bose et al. (2013 proceedings; later expanded in 2015), *Optimal Data Structures for Farthest-Point Queries in Cactus Networks*: full 2013 primary PDF, definitions and cactus decomposition through query data structures. No global two-point distribution or inverse cycle-length statement is in the inspected material.
- Garijo, Márquez and Silveira, *Continuous Mean Distance of a Weighted Graph* (2021 preprint; 2023 publication): the full available section on cactus graphs (especially Lemma 4.1 and Proposition 4.2) decomposes **the first moment** of random distances. It does not establish the exact CDF, all density jumps, or recovery of arbitrary cycle circumference multiplicities. The present result is not implied by knowing the mean.
- Baptista, Kennedy and Mugnolo, *Mean Distance on Metric Graphs* (2023 preprint; 2024 journal): mean-distance extremal bounds, rather than a complete cactus histogram and its discontinuity spectrum.
- Mémoli and Needham, *Distance Distributions and Inverse Problems for Metric Measure Spaces* (2018 preprint; 2022 journal): the available abstract states a local injectivity result for metric graphs but does not specify the present cactus jump spectrum. The inaccessible full body leaves meaningful historical-priority uncertainty.

Searches for aliases—geodesic-pair-distance histogram, uniform arclength law, cycle-length spectrum, cactus network, and cut-vertex block convolution—found related graph-topology results and mean-distance formulas, not an equivalent theorem. Search nonappearance is not proof of novelty; exact comparisons with accessible material support a provisional assessment only. Related restricted single-cycle attached-arm reconstructions were considered; they do not imply the arbitrary multi-cycle spectrum law.

## Mathematical value — PASS

The multiset of cycle circumferences records the graph's weighted cyclic geometry and the number of independent cycles. A scalar two-point distance histogram is typically lossy, yet the theorem extracts these topological and metric invariants for every finite cactus, independently of complicated tree attachments or repeated lengths. The *absence of any continuous-term cancellation* gives a natural exact boundary between trees and cyclic cacti and furnishes a complete finite formula for all the pair distances. It does not claim the entire graph is determined. This is a geometrically motivated inverse classification of a natural invariant, not an arbitrary hand-picked finite instance or a formal restatement of an expectation formula.

## Remaining limitations

Independent review has not been performed. The Mémoli–Needham full article was unavailable despite attempts via its preprint and lawful publisher access, leaving a genuine published-priority risk. No sampling-noise stability or generalization beyond cactus graphs is proved. The statistical distribution is arclength-uniform over *all edge interiors*, not vertex-counting uniform.

Self-review: passed. Independent audit: not yet performed.
