# Scientific review

## Correctness — PASS

The supplied proof reduces shortest-path changes to adjacent swaps and a single forbidden two-block facet, derives connectivity by monotone cross-inversion growth, and counts edges through a one-to-one facet-boundary matching. At an extreme Hamming layer, target-order insertion sorting never creates the forbidden first/last coordinate, and uses exactly Kendall distance. At every interior layer, fixed pairwise relations force a geodesic to pass through the forbidden facet; an explicit valid six-step route and parity prove exact distance six between a pair of Kendall distance four. Small cases and boundaries are included. The `verify.py` checker reconstructs both permutation graphs and cube route changes, performs exhaustive extreme-layer metric tests through length six, and verifies witness distances through length eight. Finite checks corroborate rather than establish the infinite proof.

## Originality — PASS (subject to historical-priority limits)

The closest full-text sources are Asplund et al. (2017), Proposition 27, and Gajjar et al. (2021/2022/2024), Theorem 5: both address the intact hypercube rather than deletion of one intermediate vertex and the resulting induced facet complement. The permutahedral non-leaving-face theorem concerns vertices *inside* a face, not outside it. The classical faulty-cube path-length theorem concerns endpoint routing, not reconfiguration of shortest routes. Relevant publication and indexed-result searches found no direct proof or stronger result implying this sharp weight threshold. Lack of hits cannot certify novelty; historical priority remains the principal uncertainty, particularly from parabolic-facet graph theory.

## Value — PASS

The question arises from fault-tolerant rerouting of equally short paths in hypercube networks. The theorem distinguishes mere reconfiguration connectivity from preservation of optimal update length and identifies the exact fault layer at which this distinction first occurs. The explicit four-letter witness establishes a real minimal detour, while the degree and edge census quantifies the extent of the fault. The result does not infer global maximum detours from its one explicit family.

## Scientific limitations

No exact metric on all interior-layer pairs, diameter formula, or universal excess bound is asserted. The available non-leaving-face primary material did not include the whole publisher PDF, although the relevant theorem and statement were inspected. The fault-tolerant routing comparison used its publisher abstract only. Future independent priority and proof review may identify additional coverage.

Self-review: passed. Independent audit: not yet performed.
