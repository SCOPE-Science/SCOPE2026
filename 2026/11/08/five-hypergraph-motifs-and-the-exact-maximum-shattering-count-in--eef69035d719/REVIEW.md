# Scientific review: maximum-size shattered supports in rank-three Johnson graphs

## Correctness

The incidence-vector reduction is exact in both directions: every four-triple support gives a unique fifteen-cell size vector after ordering its four members, and every valid size vector represents actual supports. A three-coordinate center produces exactly the coordinate-intersection counts in the proof; the exhaustive finite recursion enumerates all 862 solutions and tests every pattern against all possible centers using at most three outside coordinates. The verifier gives 40 accepted vectors in five orbits, whose automorphism-weighted counts produce the stated polynomial. An independently constructed graph-trace verifier reproduces the counts for all ambient sizes four through nine. The completeness of the finite case space is proved separately from the computations. No inference from merely small ambient sizes is used.

## Originality

Adler–Benediktsson–Macpherson (arXiv:2007.16042, 2020) established the Johnson open-neighborhood VC bound of four and studied 16 rooted four-support configurations, 8 of them shattered. Those facts and examples are prior work. The assessed statement instead classifies globally unlabeled rank-three hypergraph supports into five types and counts them exactly, including the minimum ambient order and the leading random-support frequency. Accessible prior records and exact-expression searches did not establish this global formula. This remains a qualified self-review, not a proof of novelty: a conversion of the earlier rooted case analysis could yield the same counts, and not every potentially relevant historical source was fully inspected.

## Value

The fourth coefficient is the natural top-degree shattered-support invariant of a rank-three Johnson graph, while VC dimension alone records only existence. The five-type count shows that shattered quadruples grow only with the seventh power of the coordinate-set size, so their fraction among all quadruples decays as the fifth inverse power. The exact threshold at ambient order six and the additional motif transition at seven sharpen a published global dimension bound in a structural rather than a merely numerical way. The result is restricted to the top-degree coefficient.

## Closest literature and limitations

The closest primary source is *Vapnik–Chervonenkis Dimension and Density on Johnson and Hamming Graphs*, arXiv:2007.16042. The 2024 graph-VC computation paper of Coudert et al. is methodologically related. The scope excludes closed neighborhoods, other ranks, and lower polynomial coefficients. Historical-priority uncertainty and the absence of independent audit remain explicit.

Self-review: passed. Independent audit: not yet performed.
