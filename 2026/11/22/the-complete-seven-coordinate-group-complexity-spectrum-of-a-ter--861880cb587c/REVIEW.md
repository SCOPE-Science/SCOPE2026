# Scientific assessment: seven-coordinate group complexity

## Correctness: PASS
The exact nine-factor language follows by two-superblock localization using the fivefold Fibonacci substitution, since every mapped superblock is longer than seven positions. The intransitive case follows from containment in a full two-block coordinate stabilizer and exactly 63 restricted Parikh-vector comparisons. The exhaustive published classification of transitive groups on seven points reduces the remaining case to seven conjugacy classes; five were checked over every actual conjugate subgroup and the alternating/symmetric cases follow from the repeated-letter parity argument. The standalone checker reproduced the asserted whole-group orbit histograms, and its recorded output ends in `PASS`. Dependence on the published transitive-group classification is explicit.

## Originality: PASS against inspected materials
The July 2026 work of Launer–Puzynina–Voloshinova gives universal group-complexity definitions and an open question about value four in ternary minimal-complexity words. Its Theorem 7 eliminates nontransitive witnesses under specified conditions but not transitive ones, and its paper does not state the exact seven-coordinate spectrum for the Fibonacci ternary image. The ASU and Magma transitive-group lists classify groups, not their action on this factor family. Searches for equivalent statements, particular factors, and the open problem returned no exact or stronger coverage. Remaining risk: an unindexed computation or alternative argument may already settle this special instance.

## Value: PASS
The length seven is the first nontrivial odd length \(\lvert\psi(01001)\rvert\) arising from the standard Fibonacci-word mechanism used to exhibit the difficult intermediate-value case. The exact spectrum resolves that naturally selected finite instance, exhibits an actual forbidden intermediate count despite an abelian-to-ordinary gap of six, and supplies a reusable complete finite-group certificate. The contribution is deliberately narrow: it neither classifies all lengths nor settles the general open problem.

## Closest sources and scope risks
Launer, Puzynina and Voloshinova, arXiv:2607.07620, §§5.2 and 7; ASU *Transitive Subgroups of S7*; Magma *Database of Transitive Groups*. The transitive classification is trusted as prior work, not claimed original. A complete novelty proof is impossible from absence of matching search results; independently verify priority before publication.

Self-review: passed. Independent audit: not yet performed.
