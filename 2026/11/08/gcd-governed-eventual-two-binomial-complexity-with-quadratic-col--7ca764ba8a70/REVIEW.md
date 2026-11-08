# Scientific review

## Correctness

PASS. For binary words of fixed length, the count of ones and scattered `01` count determine all six nonempty pattern counts of length at most two. The decomposition into complete cyclic periods and a residue tail is exact. Its phase-profile collision equation separates phases with unequal full-period pair counts beyond the stated bound. Equal full-period pair counts are classified by a gcd intersection; the unique possible matching tail one-count has strictly different pair count. The explicit delayed-collision construction satisfies the same pair equation with equality. The standalone checker independently enumerates small cases and corroborates all key identities. The bound is sufficient, not an asserted optimal per-parameter cutoff.

## Originality

PASS on inspected evidence, with bibliographic risk. The closest primary results concern binomial complexity of Thue--Morse and generalized Thue--Morse words, characterization of morphic and Sturmian complexity families, and general Parikh matrices of powers. Their inspected results do not imply the specific two-run periodic gcd law or the quadratic transient family. The power-matrix formula is a relevant computational antecedent but does not solve cyclic phase collision classification. Vivion (arXiv:2509.11172, Theorem 1) covers the binary 1-balanced case, including the boundary subfamily with \(\min(a,b)=1\), but for \(a,b\ge2\) the host has both length-two factors `00` and `11` and is not 1-balanced. The nontrivial gcd deficits and quadratic transients are not implied by that sufficient theorem. Research-record and accessible prior-claim comparisons uncovered no exact or stronger equivalent. Unindexed equivalents cannot be excluded.

## Value

PASS. A complete explicit eventual complexity law for a natural two-parameter periodic test family identifies precisely when a second-order scattered-subsequence statistic reconstructs every cyclic starting phase, with a gcd-governed obstruction. The quadratic-delay family shows that even this elementary periodic class can exhibit a long reconstruction transient, making a subquadratic general cutoff impossible. The result supplies structural insight rather than only numerical values or a general boundedness assertion.

## Related literature and limitations

Rigo--Stipulanti--Whiteland (arXiv:2201.04603) motivates binomial reconstruction; Lü--Chen--Wen--Wu (arXiv:2112.05347) and Lejeune--Leroy--Rigo (arXiv:1812.07330) analyze different aperiodic sources; Atanasiu--Poovanandran--Teh (arXiv:1808.04102) provides power-matrix identities, while Vivion (arXiv:2509.11172) studies equality of binomial and ordinary factor complexity in special broad classes. No exact formula for every short length is asserted. Unindexed or inaccessible equivalent literature remains a residual originality risk.

Self-review: passed. Independent audit: not yet performed.
