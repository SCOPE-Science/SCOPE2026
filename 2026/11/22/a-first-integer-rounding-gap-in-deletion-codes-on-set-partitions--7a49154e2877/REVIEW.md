# Scientific review

## Correctness — PASS

The claim concerns the one-point deletion channel on unlabelled set partitions with block relabeling by first occurrence. A fully specified source recursion enumerates 203 six-point partitions and 52 five-point outputs, checked against a second partition generator and an inverse-insertion incidence generator. The disjoint-shadow code and rational fractional witness are exact finite certificates. The backtracking maximum-clique algorithm is exhaustive: its greedy proper coloring is a valid upper bound at every branch, and it explores every branch not provably unable to improve the incumbent. In the replay it certifies optimum 14 after 452,972 nodes, alongside the smaller instances. The integer-valued length-five covering inequality gives the required first-gap boundary. The checker uses no numerical optimization and ends `VERIFY_OK`. An independent integer-program calculation also gave optimum 14 but is not needed as a proof premise.

## Originality — PASS, qualified

Closest published sources: Chee–Ge–Ling (2010), https://arxiv.org/abs/1008.1343 , on perfect unrestricted finite-alphabet deletion codes; Kulkarni–Kiyavash (2012), https://arxiv.org/abs/1211.3128 , on hypergraph packing and constrained fixed-alphabet word sources; and Campbell et al. (2016), https://arxiv.org/abs/1605.04807 , on restricted-growth patterns. Their inspected definitions and theorem statements do not identify this set-partition standardization channel with an already solved finite optimization problem, nor state the sharp 14-versus-greater-than-15 rounding separation. The ordinary word deletion channel differs because survivor symbols are not renumbered; standardized RGF subword patterns also require care because numeric-label standardization and block-order normalization need not agree. A separate same-source deletion-collision classification does not imply the cross-source packing capacity. Historical priority remains qualified because exact values could exist in unindexed literature or specialized tables.

## Mathematical value — PASS

The object is the classical Bell family of set partitions; a lost ground-set element is a natural unlabeled-structure deletion operation. The capacity is the exact zero-error number of distinguishable partitions, rather than an arbitrary statistic on a selected subfamily. Six is the first size where the standard fractional-packing bound remains at least one integer above the true maximum even after rounding, motivating a genuinely integral obstruction. Explicit codes, fractional weights, and a compact reproducible exact algorithm make the result useful as a small benchmark for reconstruction and deletion-coding relaxations. No generalization to larger sizes is claimed.

## Limitations

The upper bound is a computer-assisted exhaustive finite proof; the full checking procedure and rational witnesses are included. The exact fractional optimum at size six is not determined. Unindexed equivalent work and external independent checking remain outstanding.

Self-review: passed. Independent audit: not yet performed.
