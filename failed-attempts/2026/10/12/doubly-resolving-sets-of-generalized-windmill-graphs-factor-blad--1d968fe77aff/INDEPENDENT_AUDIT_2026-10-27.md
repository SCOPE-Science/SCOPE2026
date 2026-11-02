# Independent mathematical audit

## correctness

PASS

For k,m>=2, omitted two same-blade vertices are true twins with identical distances to all landmarks, establishing necessity. Conversely each blade supplies >=m-1>=1 selected vertex, and at least two blades are present. Every same-blade pair has different distance differences from a selected endpoint and another blade; a cross-blade pair is separated by one selected vertex from each blade with opposite-sign differences; center–blade pairs are separated using the blade and a different blade. The center may be chosen or omitted. Independent multiplication of m choices of omission or full blade and optional center gives (1+z)(m*z^(m-1)+z^m)^k, min degree k(m-1), and m^k minimum sets. Excluded k=1 and m=1 boundaries do have counterexamples. An independent BFS-based program exhaustively checked 9 parameter pairs, 20768 vertex subsets, every polynomial coefficient, and both excluded boundary counterexamples. These finite checks corroborate, not prove, unbounded k,m.

## originality

FAIL

FAIL: The claim is already a direct special case/corollary of Nie and Xu (2024), Lemmas 5.1(ii), 5.3, Theorem 5.4 on ALL noncomplete block graphs. W_{k,m} is a block graph with exactly k nontrivial clique blocks, km non-cut vertices and no leaves. Theorem 5.4 yields psi=k(m-1). Lemma 5.1 gives necessary <=1 omission per blade; the construction and its proof in Lemma 5.3 allow any omitted vertex per block, giving sufficiency; upward closure gives ALL permitted S. The whole polynomial and m^k minimum count are then a routine independent product count. Prior coverage is decisive even though exact generating polynomial is not printed in the prior paper.

## value

FAIL

FAIL: Generalized windmills and doubly resolving sets are natural, but here the entire exact set classification is already implicit constructively in a stronger theorem for the natural encompassing class of all block graphs. The remaining generating polynomial is direct bookkeeping of independent options once Lemma 5.3 is specialized. There is no non-implied invariant, new structural distinction, nonroutine boundary, or precise new fact that could independently motivate a research result. The self-contained elementary case proof and reproducibility do not confer independent research value on already covered content.

The dated certificate retains the supplied scientific assessment, sources and limitations.
