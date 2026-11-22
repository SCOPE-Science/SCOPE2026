# Self-review

**Claim:** For indexed binary words avoiding any one forbidden factor from `001`, `100`, `110`, or `011`, the two-read one-deletion confusability graph has exact edge and triangle generating functions
\[
E(z)=\frac{z^2(1+z)}{(1-z)(1-z-z^2)^2},\qquad T(z)=\frac{z^4(1+z)}{(1-z)^2(1-z-z^2)^2}.
\]
For every length, \(T_n=\sum_{j=2}^{n-2}E_j\); its asymptotic mean triangle incidence per edge is three.

## Correctness — PASS

The unique alternating difference-interval lemma converts each edge to a block and two contexts. Each phase avoids `001` if and only if the common prefix avoids `001` and is empty or ends in `1` and the suffix avoids `001` and does not start `01`. The resulting context series are \(P=1/(1-z-z^2)\) and \(S=(1+z)/(1-z-z^2)\). In the established unique long-edge triangle decomposition, one splice contains `001` and the other contains `11`, leaving exactly one legal splice per cut. All cases, including lengths below four, follow by coefficient extraction, and reversal/complement covers all four listed patterns. The independent direct deletion-set and structural enumerators passed their full declared checks. Nonstandard structural premises were inspected in the named sources; no finite computation is substituted for the all-length proof.

## Originality — PASS, qualified

The closest unrestricted edge and triangle theorems already give the alternating-interval and unique-splice geometry, so those general principles are expressly **not** claimed as new. The full published triangle-result exposition and the materially relevant primary Type-A sections were compared. The old unrestricted counts do not impose the `001` boundary-context restriction or distinguish the surviving splice. The indexed `010`-avoiding and bounded-run constrained results are different source languages and do not dominate this exact four-pattern-orbit claim. published-finding corpus and available previous-result searches did not retrieve this exact restricted enumeration, but indexing gaps cannot establish novelty.

## Value — PASS

The result provides a complete all-length census of two-way and three-way deletion ambiguity under a natural smallest asymmetric binary forbidden word, with two independent Fibonacci context factors. The exact cumulative edge–triangle identity and limiting mean three edge-triangle incidences make the relation between pairwise and triple ambiguity explicit. No optimal code cardinality, clique count, or alternate channel model is implied.

## Sources and residual limitations

Primary literature: Levenshtein (2001), DOI `10.1006/jcta.2000.3081`; Cai, Kiah, Nguyen, and Yaakobi (2020), arXiv:2001.01376, Definition 8/Proposition 9; Chrisnata, Kiah, and Yaakobi (2022), DOI `10.1109/TIT.2022.3184868`, relevant lemma. Most proximate published full text: *Exact triangle spectrum of the two-read deletion-confusability graph*, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-triangle-spectrum-of-the-two-read-deletion-confusability-g--e753c7b5bfd6. Also compared the published unrestricted edge-count summary and previous constrained claims.

The 2001 source was verified from published abstract/bibliography rather than full text; the 2022 journal source was inspected at its pertinent lemma but not end-to-end. Unindexed older motif-specific analysis is a genuine remaining priority risk. The result concerns a fixed forbidden length-three factor and counts graph edges and triangles, not maximum code sizes.

Self-review: passed. Independent audit: not yet performed.
