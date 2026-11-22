# A sharp mixed-root gap for maximal square subsequences

## Finding
Let \(S\) be a finite binary word and let \(\mathcal R(S)\) be the set of nonempty words \(X\) such that the concatenated square \(XX\) is a scattered subsequence of \(S\). Order \(\mathcal R(S)\) by scattered-subsequence containment of its roots. A root is *maximal* if it is not properly contained in any other root in \(\mathcal R(S)\), and *maximum* if its length is largest in \(\mathcal R(S)\). A root is *mixed* if both binary symbols occur in it.

**Sharp initial obstruction.** The smallest binary host length permitting a mixed maximal square root that is strictly shorter than a maximum root is **seven**. Exactly **eight** seven-symbol hosts have this property:

`0010101`, `0101001`, `0101011`, `0110101`, `1001010`, `1010100`, `1010110`, `1101010`.

In the first four the deficient maximal root is `10`; in the last four it is `01`. Each has a longest root of length three and a deficient mixed maximal root of length two. The eight hosts split into exactly two orbits of four under reversal and binary complementation.

**Unbounded size separation with a mixed root.** For every integer \(m\ge3\), define
\[
W_m=0^m\,1\,0\,1\,0^m.
\]
The root `10` is a mixed maximal square root of \(W_m\) with length two, whereas the maximum root length is exactly \(m\), attained by the pure-zero root \(0^m\). Consequently the ratio of the longest root length to the length of some mixed maximal root is \(m/2\), unbounded even over the fixed binary alphabet. This is a statement about *possible maximal solutions*, not a performance guarantee or failure claim for any particular algorithm.

## Assumptions and scope
A scattered subsequence uses strictly increasing source positions, not necessarily consecutive positions. Distinct roots are words, not embeddings. The two copies of a square occur in order as the concatenated word \(XX\); shuffle interleavings do not qualify. Only nonempty roots are considered. Comparisons of square subsequences are by the usual subsequence relation on complete squares; the following lemma shows this is exactly the subsequence relation on the respective roots. The alphabet is labeled \(\{0,1\}\), and parameters are integers satisfying \(m\ge3\).

## Proof
**1. Root-order lemma.** For arbitrary words \(X,Y\),
\[
XX\preccurlyeq YY\quad\Longleftrightarrow\quad X\preccurlyeq Y,
\]
where \(\preccurlyeq\) means scattered-subsequence containment. The reverse implication follows by duplicating an embedding \(X\preccurlyeq Y\). Conversely, consider an embedding of \(XX\) into \(YY\). If the first copy of \(X\) ends in the first copy of \(Y\), it embeds there. Otherwise the first \(X\) crosses the junction, so the entire second copy of \(X\) embeds in the second copy of \(Y\). Thus \(X\preccurlyeq Y\). The equivalence independently reproduces the root-order principle used in Gong--Liyanage--Sopp--Zhu, Lemma 3.1.

**2. Sharp lower bound of seven.** A mixed binary root has length at least two. If a mixed maximal root is shorter than a maximum one, the maximum root has length at least three and hence any host has length at least six. At length six, a maximum square root \(Y\) of length three occupies the whole host, so \(S=YY\). Any other square \(XX\preccurlyeq S=YY\) has \(X\preccurlyeq Y\) by step 1 and is not maximal when \(|X|<3\). Therefore no host of length at most six has the stated obstruction.

**3. All equality hosts at length seven.** There the maximum-root length must be exactly three and the deficient mixed maximal root must be either `10` or `01`. If `10` is maximal, any feasible longer root \(Y\) is a three-letter word not containing `10` as a scattered subsequence. Such roots are `000`, `001`, `011`, `111`. The unary choices would force at least six copies of one letter in the seven-position host, leaving at most one copy of the other letter, which is incompatible with the square `1010`. Thus \(Y\in\{\texttt{001},\texttt{011}\}\). Complementation gives \(Y\in\{\texttt{100},\texttt{110}\}\) for a maximal `01`.

Since \(|YY|=6\), each length-seven host arises by inserting **exactly one** binary symbol into \(YY\). Enumerating the at most sixteen insertion sites and symbols for each of the four possible longer roots, retaining only hosts containing \(XX\) and no one-letter extension of \(X\), yields the exhaustive table:

| Deficient root | Longer root | All qualifying hosts |
| --- | --- | --- |
| `10` | `001` | `0010101`, `0101001` |
| `10` | `011` | `0101011`, `0110101` |
| `01` | `100` | `1001010`, `1010100` |
| `01` | `110` | `1010110`, `1101010` |

Every entry directly exhibits the required two roots and passes the no-extension test. Conversely the preceding restrictions and complete single-insertion enumeration exclude every other length-seven host. Reversal and symbol complementation preserve the predicate and group the eight entries into orbits
\[
\begin{aligned}
&\{\texttt{0010101},\texttt{0101011},\texttt{1010100},\texttt{1101010}\},\\
&\{\texttt{0101001},\texttt{0110101},\texttt{1001010},\texttt{1010110}\}.
\end{aligned}
\]

**4. Infinite family and maximum length.** For \(W_m=0^m1\,0\,1\,0^m\), the scattered square `1010` is present: take the first marked one, the unique intervening zero, the second one, and a zero from the last run. Any square root containing both symbols must contain exactly one `1` in each of its two copies because the host has precisely two ones. Write such a root as \(Y=0^a1\,0^b\), \(a,b\ge0\). Embedding \(YY\) requires at least \(a+b\) zeros **between** the two marked ones of the host: \(b\) after the first root's one, and \(a\) before the second root's one. There is exactly one such zero, so \(a+b\le1\) and \(|Y|\le2\). In particular, a longer root containing `10` cannot exist, proving its maximality.

The host contains \(2m+1\) zeros and exactly two ones. A purely zero root has length at most \(\lfloor(2m+1)/2\rfloor=m\), attained by \(0^m\). A purely one root has length at most one; every mixed root has length at most two by the preceding central-gap argument. Since \(m\ge3\), the global maximum is \(m\). The ratio is therefore exactly \(m/2\) for this particular deficient root and diverges as claimed.

## Verification
The standalone programs `check_exhaustive.py` and `check_extension.py` implement independent finite checks. The first enumerates **all 255 binary words of lengths zero through seven** (including the empty word) and all feasible roots; for every root it compares against all longer feasible roots using the scattered-subsequence relation. The second generates roots independently by taking subsequences of every prefix/suffix cut, and uses the one-letter extension characterization of maximality. Both give zero qualifying hosts before seven and exactly the displayed eight at length seven, including their symmetry orbits.

For the infinite family, the second program checks absence of every single-letter extension of `10` for \(3\le m\le40\), and exhaustively enumerates all candidate square roots for \(3\le m\le8\). These bounded checks are not the proof for arbitrary \(m\); step 4 is the all-parameter argument. The exact commands and observed outputs are in `VERIFICATION.md`.

## Relationship to prior work
Gong, Liyanage, Sopp and Zhu (arXiv:2601.12200v1, January 18, 2026) introduced an efficient algorithm for computing **some maximal** square subsequence of an arbitrary word and gave the root-order lemma. Their definitions, construction, proof, appendices and concluding discussion do not state the sharp seven-letter mixed-root obstruction, its complete equality set, or this unbounded mixed-root maximal-versus-maximum separation. The present result studies extremal structural coexistence, not algorithm runtime.

Kosowski (SPIRE 2004) and Inoue, Inenaga and Bannai (arXiv:2006.00216) optimize the **longest** square subsequence over arbitrary inputs; their optimization algorithms do not directly classify the collection of inclusion-maximal roots. Previously published exact square-subsequence spectra of cyclic permutation powers concern a different periodic host family and enumerate **all square roots by length**, not the root-containment-maximal elements of arbitrary binary hosts. Published longest-repeated-subsequence formulas for binary two-run powers also optimize repeated-root length in a different family. A related two-marker **shuffle-square** result uses interleaved equal copies rather than concatenated scattered squares and does not imply the present statement. None of these covers the two-component boundary theorem by a matching statement or a stronger implication identified in the inspected material.

## Limitations
The finite equality classification is specific to binary hosts of length seven. The unbounded family demonstrates a possible poor **maximal** output but makes no statement about the selection rule or approximation ratio of any particular maximal-subsequence algorithm. More generally, this theorem does not enumerate all maximal roots for arbitrary words or claim a sharp all-length worst-case ratio. An unindexed earlier example or an equivalent observation in other literature remains a priority risk.

## References
1. M. Gong, A. Liyanage, B. Sopp, B. Zhu, *Computing Maximal Repeating Subsequences in a String*, arXiv:2601.12200v1, first public January 18, 2026. https://arxiv.org/html/2601.12200v1
2. A. Kosowski, *An Efficient Algorithm for the Longest Tandem Scattered Subsequence Problem*, SPIRE 2004, pp. 93--100. https://doi.org/10.1007/978-3-540-30213-1_13
3. T. Inoue, S. Inenaga, H. Bannai, *Longest Square Subsequence Problem Revisited*, arXiv:2006.00216, first public May 30, 2020. https://arxiv.org/abs/2006.00216
4. *Square-subsequence spectra of cyclic permutation powers*, publicly accessible mathematical result. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-square-subsequence-spectra-of-cyclic-permutation-powers--0d48ff0900f8
5. *Exact longest repeated subsequences of binary two-run powers*, publicly accessible mathematical result. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-longest-repeated-subsequences-of-binary-two-run-powers--d0386f1167a3
6. *Complete root-multiplicity spectrum of two-marker binary shuffle squares*, publicly accessible mathematical result. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-complete-root-multiplicity-spectrum-of-two-marker-binary-shuffle--ee8a475fe7fb
