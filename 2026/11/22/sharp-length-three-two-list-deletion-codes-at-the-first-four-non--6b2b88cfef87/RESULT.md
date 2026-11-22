# Sharp length-three two-list deletion codes at the first four non-Steiner alphabet sizes

## Finding

Let \(X_q=\{0,\ldots,q-1\}\) be a labeled alphabet. For a code \(C\subseteq X_q^3\), the one-deletion receiver list at \(y\in X_q^2\) is \(\{w\in C:y\text{ is obtained by deleting one position of }w\}\). Write \(M_2(q,3,1)\) for the maximum possible size of a code with every receiver list of size at most two. Then

\[
\boxed{M_2(q,3,1)=q+\left\lfloor\frac{2q^2}{3}\right\rfloor\quad\text{for }q\in\{4,5,6,8\}.}
\]

Consequently, the four capacities, in increasing alphabet order, are \(14,21,30,50\). The four alphabet sizes are the smallest nontrivial representatives of the four residue classes \(4,5,0,2\pmod 6\), respectively, outside the classical Steiner triple-system existence classes \(1,3\pmod6\).

There are additional structural witnesses: an optimum at \(q=6\) is invariant under cyclic translation of all alphabet symbols and has exactly two candidate codewords for **every** receiver word. The displayed optima at \(q=5\) and \(q=8\) cannot be partitioned into two uniquely single-deletion-decodable subcodes. At \(q=4,5,8\), no optimum can be invariant under cyclic translation of alphabet symbols, by a free-orbit divisibility obstruction.

## Assumptions and scope

The channel deletes exactly one of the three transmitted symbol positions, and received words retain the original order. Distinct deletion positions producing the same two-symbol word are counted **once** for that transmitted codeword. The list bound concerns distinct codewords, not deletion histories. There is no additional substitution, insertion, or restriction on codeword composition. A construction is claimed only for the four stated alphabet sizes; nothing is asserted about all other non-Steiner sizes.

## Proof

**Universal bound.** For each word \(w\), let \(D(w)\) be its set of distinct two-symbol one-deletion outputs. Partition any admissible code into \(A\) words of the form \(aaa\), \(B\) words with exactly two outputs, and \(C_3\) words with three outputs; the same letters also denote the corresponding cardinalities. Exactly-two-output words are precisely those with the first two equal or the last two equal but not all three equal. Such a word has a diagonal output \(aa\), as does every constant triple. The \(q\) diagonal outputs collectively support at most \(2q\) codewords, so

\[
A+B\le 2q,\qquad A\le q.
\]

Counting codeword–receiver incidences across all \(q^2\) ordered receiver words gives

\[
E=A+2B+3C_3\le 2q^2.
\]

It follows that

\[
3|C|=3(A+B+C_3)=E+2A+B
\le 2q^2+(A+B)+A\le2q^2+3q.
\]

Since the code size is integral, \(|C|\le q+\lfloor2q^2/3\rfloor\). This holds for every \(q\ge2\).

**Explicit constructions.** In each line below, each space-separated three-digit token is one entire codeword over the indicated alphabet (not a decimal integer):

- \(q=4\): `000 003 032 111 113 120 122 130 201 222 231 233 302 333`.
- \(q=5\): `000 004 012 022 033 104 111 130 132 211 222 230 240 243 314 333 342 403 421 441 444`.
- \(q=8\): `000 012 041 044 072 075 105 111 112 133 146 167 206 214 222 235 237 247 260 300 315 333 342 364 370 403 421 444 455 463 510 532 536 540 547 555 562 603 625 651 661 666 677 706 713 722 731 745 764 777`.

For \(q=6\), use modular arithmetic in \(\mathbb Z/6\mathbb Z\). For every \(a\in\mathbb Z/6\mathbb Z\), include the five triples

\[
(a,a,a),\quad(a,a,a+2),\quad(a,a+1,a+2),\quad
(a,a+4,a+3),\quad(a,a+5,a+3).
\]

All additions are reduced modulo six. These are thirty distinct triples, manifestly closed under adding one to every symbol. Their codeword–receiver incidences are exactly twice every one of the thirty-six possible ordered receiver pairs; this is verified exhaustively by the standalone checker. The three other explicit codebooks similarly have every receiver list of size one or two, with precisely two size-one lists. In the four cases the code sizes attain the universal bound; hence they are optimal.

**Rigidity and nondecomposability.** When \(q=6\), attaining the upper bound means equality in each displayed inequality. Therefore every optimum contains all six constant triples, has exactly six two-output triples and eighteen three-output triples, and saturates every receiver output to list size two. (Every three-output triple in such an optimum necessarily has three distinct letters, because the diagonal receivers are already saturated.) The modular example attains this structure.

For \(q=5\), the three codewords `230`, `240`, `243` have pairwise intersecting deletion-output sets: their common outputs for the three respective pairs include `20`, `24`, `23`. For \(q=8\), the analogous triangle `403`, `463`, `603` has three respective shared outputs `43`, `63`, `03`. Each triangle is an odd cycle in the conflict graph joining codewords with at least one common deletion output. A union of two uniquely deletion-decodable subcodes would yield a bipartite conflict graph. Thus these two explicitly optimal codes admit no such partition.

Lastly, simultaneous translation of every symbol by one modulo \(q\) acts freely on three-letter words: no nonzero group element fixes any word. Every invariant code therefore has cardinality divisible by \(q\). The optimal cardinalities \(14,21,50\) are not divisible by \(4,5,8\), respectively, so no cyclic-translation-invariant optimum exists at those alphabet sizes.

## Verification

The attached `verify.py` independently constructs the cyclic six-letter code and directly computes the set of deletion descendants of every listed codeword. It checks, for each \(q\in\{4,5,6,8\}\), every one of the \(q^2\) possible ordered receiver words, the number of distinct source codewords producing it, codebook size and distinctness, the three deletion-shadow-size strata, and total incidence counts. Its exact output is stored in `verify_output.txt`.

The receiver-list histograms are: \(q=4\), fourteen outputs with list size two and two with size one; \(q=5\), twenty-three and two; \(q=6\), thirty-six with size two; \(q=8\), sixty-two and two. No output has an empty or larger-than-two list in any of the four constructions. The checker also tests cyclic invariance of the six-letter construction and the explicit conflict triangles. No numerical optimizer, random experiment, exhaustive search over **all** possible codebooks, or unverified computation is needed to conclude optimality: the general proved upper bound and the fully checked constructions are sufficient.

## Relationship to prior work

List-decodable deletion codes and their achievable-rate bounds are treated by Kiah, Wei, and Zeng (2026), including arbitrary alphabet-size converses and fixed list allowances. The sharp values here are finite-block extremal capacities, not consequences of the asymptotic rate expressions. Song, Cai, and Nguyen (2022) study binary list-two codes robust to a deletion and a substitution, a different alphabet/error regime. Chee, Ge, and Ling (2010), especially their Section 6 and Table 6.1, determine the spectrum of **perfect uniquely** deletion-correcting length-three codes. Their capacity and exact-cover notions demand at most one codeword per output and do not directly yield the present list-two packing optima or the explicit non-bipartite optimum examples. Dawson, Seberry, and Skillicorn (1984) study directed packings with no repeated symbols per block and a different incidence constraint, not this repeated-symbol list-two setting.

Steiner triple systems exist in the classical congruence classes \(1,3\pmod6\), making the four omitted classes mathematically natural cases to test. The result gives a sharp, verified first representative in each such class; it makes no unproved general completion claim.

## Limitations

Only four alphabet sizes are determined. The two explicit odd-cycle certificates prove nondecomposability of the **displayed** optima, not of every optimum for those alphabets. The construction checker proves its finite incidence assertions by exhaustive checks; it does not prove that any analogous construction works at unexamined alphabet sizes. Though relevant published exact-cover and asymptotic list-decoding results were compared, a concealed earlier two-fold directed-packing specialization or an unindexed equivalent short-block table is a remaining originality risk. No independent external audit has been carried out.

## References

1. H. M. Kiah, H. Wei, and R. Zeng, *Constant-List Insertion--Deletion Codes: New Bounds and an Improvement of Levenshtein's Lower Bound*, arXiv:2609.21395, first submitted 2026-09-18. https://arxiv.org/abs/2609.21395
2. W. Song, K. Cai, and T. T. Nguyen, *List-decodable Codes for Single-deletion Single-substitution with List-size Two*, arXiv:2201.02013, first submitted 2022-01-06. https://arxiv.org/abs/2201.02013
3. Y. M. Chee, G. Ge, and A. C. H. Ling, *Spectrum of Sizes for Perfect Deletion-Correcting Codes*, SIAM Journal on Discrete Mathematics 24 (2010), 33--55, DOI:10.1137/090751311. Lawful preprint: https://arxiv.org/abs/1008.1343
4. J. E. Dawson, J. Seberry, and D. B. Skillicorn, *The Directed Packing Numbers*, Combinatorica 4 (1984), 121--130. https://documents.uow.edu.au/~jennie/WEBPDF/097_1984.pdf
