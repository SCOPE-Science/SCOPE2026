# Scientific review

## Correctness (C): PASS
For positive integers \(a,b,c,d\), the common scattered subsequences of \(0^a1^b\) and \(1^c0^d\) are monochromatic; hence the LCS length is \(s=\max(\min(a,d),\min(b,c))\). Every shortest common supersequence induces a covering pair of embeddings with precisely \(s\) shared positions, divided into zero-sharing and one-sharing alternatives. The forced-outer-block arguments in RESULT.md characterize four disjoint constructive shuffle classes and count distinct output words by binomial coefficients. The sharp fixed-total equality cases follow by strict comparison with the largest binomial coefficient and a complete tie-case partition. Both independent finite checker programs agree with the exact formula, without serving as substitutes for the infinite proof.

## Originality (O): PASS against inspected sources
The general upper bound \(\binom{N-2}{\lfloor(N-2)/2\rfloor}\) and its asymptotic are **already implied** by Alon et al., arXiv:2209.11882v3 (Theorem 3), and are **not new**. Sopp et al., arXiv:2603.22591v1, give general minimal-common-supersequence enumeration algorithms, not the exact four-run *shortest*-output formula or its parameter equality classification. Three inspected published special cases concern equal/mirrored run lengths or opposite permutation *powers*, not four independent run parameters. The specific novel assertion is the complete formula and every equality case restricted to the natural four-parameter family. A pre-existing unindexed formula remains a realistic historical-priority risk, especially the older Fraser–Irving–Middendorf source whose complete text was not inspected.

## Value (V): PASS
Exact output ambiguity, rather than mere length or number of alignment paths, is a natural invariant in two-string shortest-supersequence reconstruction. The formula resolves all four independent run parameters and handles degeneracies at tied longest-common-subsequence modes. The equality classification tells exactly which inputs attain the already-known global central-binomial ceiling, replacing an upper bound with an all-optimizer structural classification in a natural two-run class. This is a nontrivial infinite classification, not a routine small-table computation.

## Scope and residual risks
No assertion is made for more runs, more than two input words, longer deletion-minimal outputs, or independent mathematical audit. The general extremal ceiling, mirrored specializations, and asymptotic are acknowledged as established; finite verification cannot prove the all-parameter theorem. Complete priority verification against older papers is not yet performed.

Self-review: passed. Independent audit: not yet performed.
