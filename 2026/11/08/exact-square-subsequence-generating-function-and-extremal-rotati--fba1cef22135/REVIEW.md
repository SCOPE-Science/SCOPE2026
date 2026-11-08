# Scientific review

## Correctness
**PASS.** For a root \(V\), greedy matching in a repeated permutation crosses periods precisely on weak descents, giving the exact condition \(1+2d(V)+[\operatorname{last}(V)\ge\operatorname{first}(V)]\le k\). This proves the weighted transfer formula. The matrix determinant and rank-one resolvent identities are expanded and derived in RESULT.md rather than assumed. The parity-constrained extremal bound and the cyclic weak-descent argument classify all maximizers. Independent finite direct-subsequence enumeration agrees with the rational coefficient recurrence in 19 complete configurations and 85 coefficients; there are additionally 11,992 greedy/descents comparisons. The infinite statement rests on the algebraic proof.

## Originality
**PASS, qualified by incomplete bibliographic coverage.** The exact object is the number of **different** words of shape \(VV\) arising as scattered subsequences of \(P^k\), simultaneously for every alphabet size, power and half-length. The full primary articles by Inoue et al. (2018) and Bannai et al. (2022) concern algorithms to find a maximum-length square or periodic subsequence, not an exact all-length enumerator. An algorithm returning one optimum does not imply the proposed bivariate generating function or the number of distinct maximizing roots. Nearby indexed material on subsequence universality, palindromic subsequences and factor squares does not state the same quantity. Searches did not locate an equivalent theorem; negative searches alone cannot establish priority. Unindexed literature and other specialized enumeration methods are residual risks.

## Mathematical value
**PASS.** A general square-subsequence problem requiring nontrivial algorithms collapses here to a compact rational law for a natural infinite family. The result extracts every length stratum rather than only an optimum, and reveals a sharp odd/even rigidity theorem for **all** longest square roots. Direct labels are essential: embeddings and factor squares behave differently. The theorem is a complete classification across unbounded \(q,k,m\), not a finite table or a parameter substitution.

## Closest literature and limitations
- Bannai, I, Köppl (2022), arXiv:2202.07189, §§1–5: longest periodic/subperiodic subsequences, including the square case; full primary text compared.
- Inoue, Inenaga, Hyyrö, Bannai, Takeda (2018), DOI:10.4230/LIPIcs.CPM.2018.15, §§1–4: longest common square-subsequence algorithms; full primary text compared.
- No independent priority review. Special-period enumeration could exist under another term; no theorem for general nonpermutation periods is asserted.

Self-review: passed. Independent audit: not yet performed.
