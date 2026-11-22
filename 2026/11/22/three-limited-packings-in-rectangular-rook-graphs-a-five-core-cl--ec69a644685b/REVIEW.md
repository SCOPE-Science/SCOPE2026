# Self-review

## Correctness (PASS)

The exact identity \(|S\cap N[(i,j)]|=d_i+e_j-\mathbf1_{(i,j)\in S}\) applies to all cells, selected or not. It forces the maximum selected row and column degrees to sum to at most four; in the equality case all intersections of maximum-degree rows and columns must be selected. The only possible exceptional components are a three-star, three-edge path, four-edge path, or four-cycle. Every other selected edge is an isolated matching edge. This proves a disjoint all-set classification and the displayed coefficient formula, including the factor-of-two orientation correction for ordinary matchings. Every domain restriction and sharpness construction for \(L_3\) is accounted for.

Direct enumeration of every subset in eight small boards using exact closed neighborhoods agrees with the formula. A separate C++ implementation also checks the wider boards \(3\)-by-\(6\), \(3\)-by-\(7\), and \(4\)-by-\(6\). An independent selected-bipartite-component checker verifies the classification in five instances. The code outputs are included and reproducible. The general theorem rests on the proof, not on the experiments.

## Originality (PASS, provisional historical priority)

The 2023 paper by Ahmadi, Soltankhah and Samadi, arXiv:2308.16837v1, develops packing partitions principally for capacity two. The product bounds in Ahmadi and Soltankhah, arXiv:2405.03237v1, concern capacity two (closed and total), not this all-set capacity-three rook enumeration. Public research-record searches also returned three-independent rook-graph enumerators and general complete-multipartite limited packing, but those neither have the same three-limited property on this Cartesian product nor establish its stated polynomial. The claim is distinct in parameter, condition and counting level; no known covering result was identified after the described searches. This does not amount to a proof of absolute historical novelty. Priority risks include hard-to-index specialized product literature, unpublished calculations and a potentially unrecognized derivation from a general result.

## Value (PASS)

Three-limited packings are a natural local capacity condition for facility placement. Unlike an arbitrary finite census, the theorem provides a complete structural and exact all-cardinality solution on an infinite canonical graph family. The one-exceptional-component rigidity yields the sharp three-regime capacity law \(\max\{s+2,\min(2s,\ell)\}\) and identifies the entire optimum class in the sufficiently rectangular regime. In particular, at square aspect ratio capacity three allows only two more placements than a matching, whereas at width at least twice the height it permits two placements per row. Those structural differences explain why generic product upper bounds are far from universally sharp.

## Sources and limitations

Public primary sources inspected: https://arxiv.org/abs/2308.16837 (v1, 2023-08-31) and https://arxiv.org/abs/2405.03237 (v1, 2024-05-06). Additional broader context: https://arxiv.org/abs/1501.01833. The theorem does not cover arbitrary Cartesian factors, capacity greater than three or all inclusion-maximal packing configurations. Historical priority remains provisional and requires independent review.

Self-review: passed. Independent audit: not yet performed.
