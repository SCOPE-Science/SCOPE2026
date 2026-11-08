# Scientific review

## Correctness — PASS

The final theorem gives a complete partition of all two-leader placements into six automorphism classes, including the class that requires at least four vertices in the smaller bipartition. The unperturbed grounded biclique is inverted exactly using a two-block Schur complement; the one added edge has either a diagonal or difference-vector rank-one effect, allowing exact Sherman--Morrison trace reductions. The strict domination of four classes leaves just two, whose difference is exactly the rational function with numerator \(P_{p,q}(t)\). Its denominator is positive and its quadratic sign yields all cases and equality boundaries. The arithmetic is directly reproduced by the included standard-library exact-rational verifier: 2,696 independent grounded-matrix pair comparisons and 2,610 parameter/polynomial comparisons. The checker is finite supporting evidence, not the proof for arbitrary positive real weights.

## Originality — PASS on inspected evidence

The closest identified frameworks are the noise-free inverse-trace leader formulation of Lin, Fardad and Jovanović (arXiv:1302.0450), the two-leader joint-centrality expression of Fitch and Leonard (arXiv:1407.1569), and the resistance-distance formulations of Patterson, Yi and Zhang (arXiv:1708.06873). These give general objective expressions and special solved graph classes but not a stated exact optimizer transition for a biclique with one weighted added edge inside a part. The weighted-path and ring results of Patterson, McGlohon and Dyagilev (arXiv:1412.6595) address different topology. Zhou and collaborators (arXiv:2309.17019) optimize the *smallest eigenvalue* by edge addition for a given grounded set, not the inverse trace by changing the leader pair for a fixed edge. Searches for equivalent graph descriptions and broader results did not identify a direct implication or precomputed optimizer table. General-purpose formulas permit an independent derivation but do not give this evaluated classification without substantial case and inequality work. Residual risk: equivalent unindexed literature or overlooked specialized work on defective bicliques.

## Value — PASS

The result provides an all-size, all-positive-conductance exact design law for two leaders in a minimally augmented dense two-community network. It proves an unexpectedly restricted switching region: only smaller-part sizes 3, 4 or 5, and only above exact imbalance cutoffs, admit moving the second leader across communities at high chord conductance. A precise positive threshold, optimizer multiplicities, closed objective expressions and equality cases make the result directly reusable in network design and benchmark construction. The phenomenon is not determined by the unmodified bipartite limit or by general monotonicity of adding an edge.

## Limitations and risks

The theorem assumes exactly two noise-free leaders, only one intrapart edge insertion, unit crossing weights, and \(3\le p\le q\). No result is claimed for larger leader budgets, joint selection of edge location and weight, or noise-corrupted leaders. The primary-text comparisons were targeted to the relevant theorems and applications; exhaustive unindexed-paper coverage is unavailable. No external independent audit or publication-priority certification is claimed.

Self-review: passed. Independent audit: not yet performed.
