# Outer-independent two-rainbow polynomials and optimum colorings of \(\operatorname{KG}(n,2)\)

## Finding

**Theorem.** Let \(n\ge5\) be an integer, let \(G_n=\operatorname{KG}(n,2)\) be the Kneser graph on the two-subsets of \([n]\), and let \(P_n(z)=\sum_f z^{w(f)}\) enumerate all outer-independent two-rainbow dominating labelings with two *named* colors. The complete polynomial is the explicit finite star–triangle inclusion–exclusion sum below. Its least exponent and coefficient are
\[
\boxed{\gamma_{oir2}(G_n)=\binom{n-1}{2}},
\]
\[
\boxed{[z^{\binom{n-1}{2}}]P_n(z)
=n\left[2^{\binom{n-1}{2}}-2\left(1+\binom{n-1}{2}+(n-1)(2^{n-2}-n+1)\right)\right].}
\]
Every minimum labeling assigns \(\varnothing\) to the \(n-1\) pairs through exactly one ground element, assigns singleton labels to the remaining pairs, and uses each named color on an edge family in \(K_{n-1}\) **with no common incident vertex**. Conversely every such labeling is minimum. For \(n=5,6,7,8,9\), the respective minimum-labeling counts are \(90\), \(5352\), \(226968\), \(16770480\), and \(2415901302\).

Here is the complete-polynomial formula (not just the minimum coefficient). Put \(E_n=\binom{[n]}2\), \(N=\binom n2\), and, for a pair \(e\in E_n\) and \(A\subseteq E_n\), let
\[
\varepsilon(e,A)=\begin{cases}1,&e\cap a\ne\varnothing\text{ for every }a\in A,\\0,&\text{otherwise.}\end{cases}
\]
The empty family gives \(\varepsilon(e,\varnothing)=1\). For any pairwise-intersecting zero family \(Z\subset E_n\), define the explicit polynomial
\[
\Phi_{n,Z}(z)=\sum_{A,B\subseteq Z}(-1)^{|A|+|B|}
\prod_{e\in E_n\setminus Z}
\left[z\bigl(\varepsilon(e,A)+\varepsilon(e,B)\bigr)
+z^2\varepsilon(e,A\cup B)\right].
\]
Let \(S_s=\{\{1,j\}:2\le j\le s+1\}\) for \(2\le s\le n-1\), and \(T=\{\{1,2\},\{1,3\},\{2,3\}\}\). Then
\[
\boxed{P_n(z)=(2z+z^2)^N
+N\Phi_{n,\{\{1,2\}\}}(z)
+n\sum_{s=2}^{n-1}\binom{n-1}{s}\Phi_{n,S_s}(z)
+\binom n3\Phi_{n,T}(z).}
\]
The sums and products involve finitely many specified subsets; the formula has no implicit graph enumeration, unspecified constants, or recurrence boundary conditions.

## Assumptions and scope

The graph is finite, simple, and labeled. Its vertices are the two-element subsets of \([n]\), with adjacency precisely for disjoint subsets. A valid labeling assigns one of \(\varnothing,\{1\},\{2\},\{1,2\}\) to every vertex. The empty-labeled vertices must be pairwise nonadjacent, and the union of the labels on the *open* neighborhood of each empty vertex must equal \(\{1,2\}\). The weight is the sum of label cardinalities. The colors are named and their interchange produces a different labeling unless the assignments coincide. In \(P_n(z)\), the summation ranges over all valid labelings, not merely minima.

## Proof

**1. Exhaustive classification of possible empty sets.** Two vertices of \(G_n\) are nonadjacent exactly when their ground-set pairs intersect. Thus any empty set \(Z\) is a pairwise-intersecting family of edges of \(K_n\). If all its edges share an endpoint, it is a star subfamily. Otherwise select two distinct edges \(ab,ac\) and another edge avoiding \(a\). To intersect both initial edges, the latter must be \(bc\). Every edge intersecting all three of \(ab,ac,bc\) belongs to this triangle. Thus a non-star pairwise-intersecting family is exactly the three edges of a triangle. A star of size at least two has a unique center, whereas an isolated edge has two possible centers. Consequently the complete disjoint list of empty families consists of the empty family (one), singleton edges (\(N\)), star subsets of size \(s\ge2\) (\(n\binom{n-1}{s}\)), and full triangles (\(\binom n3\)). This proves that the list in the formula is exhaustive and has no double counting.

**2. Fixed-empty-set inclusion–exclusion.** Fix one permissible \(Z\). All vertices outside \(Z\) must receive a nonempty label. For each \(a\in Z\), impose the two requirements that at least one neighboring vertex carries color \(1\), respectively color \(2\). If a chosen subfamily \(A\subseteq Z\) violates the color-\(1\) requirements, any nonempty-labeled vertex \(e\) containing color \(1\) must intersect every \(a\in A\), because disjoint pairs are adjacent in \(G_n\). Similarly a chosen violation subfamily \(B\) constrains color \(2\). For a vertex \(e\notin Z\), the available labels and weights are therefore exactly the three terms
\[
z\varepsilon(e,A),\qquad z\varepsilon(e,B),\qquad z^2\varepsilon(e,A\cup B).
\]
Choices at distinct vertices are independent once these violation events are fixed, hence their product is the weight enumerator for the simultaneous events. Inclusion–exclusion with sign \((-1)^{|A|+|B|}\) over the \(2|Z|\) violation events gives \(\Phi_{n,Z}(z)\). Sum it over the complete list of possible \(Z\) from Step 1. For \(Z=\varnothing\), the unrestricted factor is \((2z+z^2)^N\). This proves the complete polynomial identity for every \(n\ge5\).

**3. The exact minimum and its support geometry.** A pairwise-intersecting family of two-subsets contains at most \(n-1\) edges for \(n\ge5\): a star has at most \(n-1\), while a non-star triangle has three. Equality is possible only for a full star. Thus, since each vertex outside \(Z\) contributes weight at least one,
\[
w(f)\ge N-(n-1)=\binom{n-1}{2}.
\]
Choose a full star as \(Z\). Its complement consists of all edges of the complete graph \(K_{n-1}\) on the noncentral ground elements. Label them with one named color each. On four of those ground elements, color one perfect matching with color \(1\) and a different perfect matching with color \(2\), then color all remaining edges arbitrarily with one of the two colors. For each star vertex \(\{c,i\}\), each chosen color then appears on a disjoint pair of edges, at least one of which avoids \(i\); therefore the empty vertex sees both colors. Equality is attained. Equality in the lower bound forces precisely one full star of empty vertices and singleton labels elsewhere. The more general necessary and sufficient criterion is that **neither color's edge family is contained in any one vertex star** of \(K_{n-1}\), equivalently each color family has no common endpoint.

**4. Exact count of minima.** Set \(m=n-1\ge4\) and \(M=\binom m2\). For one fixed full empty star, the remaining \(M\) edges have \(2^M\) possible assignments of two named singleton colors. A coloring fails for a specified color precisely when all edges of that color lie in some vertex star of \(K_m\). The number of edge subsets contained in some star is
\[
S_m=1+\binom m2+m\sum_{j=2}^{m-1}\binom{m-1}{j}
=1+\binom m2+m(2^{m-1}-m).
\]
The first two terms count the empty set and all singleton edges. Every larger star subfamily has a unique center, justifying the remaining sum. The red-failure and blue-failure events cannot occur together: the union of two vertex stars fails to contain the edge between two vertices outside their centers, which exist since \(m\ge4\). Thus exactly \(2^M-2S_m\) singleton-colorings are valid for each empty star. There are exactly \(n\) full stars. Multiplication establishes the displayed coefficient and the complete optimizer classification.

## Verification

The standalone Python program `verify_formula.py` implements the fixed-zero-set inclusion–exclusion formula and checks the full coefficient profiles for \(n=5,6\), including their least nonzero exponents. The separately implemented C++ program `verify_direct.cpp` enumerates all \(4^{10}=1048576\) four-label assignments for \(n=5\) directly from Kneser adjacency and checks every coefficient. It separately enumerates every singleton-coloring of every full empty star for \(n=5,6,7\) against the original two-color neighborhood condition. The programs agree exactly at all overlapping coefficients; see `verification_output.txt`. The unrestricted identity follows from the preceding proof, not from finite computation. To reproduce, use `python3 verify_formula.py` and `g++ -O2 -std=c++17 verify_direct.cpp -o verify_direct && ./verify_direct` in a directory containing these files.

For illustration, the complete polynomial for the Petersen graph \(\operatorname{KG}(5,2)\) has nonzero coefficients, by increasing exponent, 
\[
(90,2120,13640,42460,80404,103700,97005,68220,36750,15244,4830,1140,190,20,1),
\]
corresponding respectively to weights \(6,7,\ldots,20\). The corresponding lowest coefficients for \(n=6\) and \(n=7\) are \(5352\) and \(226968\).

## Relationship to prior work

Mansouri–Mojdeh (2020) introduce and analyze outer-independent rainbow domination and give general lower and upper bounds and certain graph-family values, but do not state the two-subset Kneser weight polynomial or optimizer count. Cabrera-Martínez (2022) improves general bounds and treats joins, lexicographic and corona products. Samadi–Soltankhah (2022 preprint, 2023 journal) prove a claw-free classification and product bounds; the accessible 13-page primary text contains no Kneser specialization or labeling census. The present proof's elementary classification of intersecting edge families is the two-subset boundary of Erdős–Ko–Rado theory and is not claimed new.

A previously published outer-independent two-rainbow weight enumerator for the **triangular graph** \(L(K_n)\), which is the complement of \(\operatorname{KG}(n,2)\), uses matchings as empty supports. It does not imply this result: complementation changes both which empty sets are independent and which vertices provide rainbow neighborhood coverage. Published ordinary \(k\)-rainbow domination results for \(\operatorname{KG}(n,2)\) with \(k\ge3\) allow adjacent empty vertices and concern the minimum scalar, not the outer-independent two-color polynomial. Similar-sounding domination or polynomial results do not cover the claim without a proved transformation of their admissibility conditions. A published exact equivalent not visible in accessible sources remains a possibility.

## Limitations

The theorem applies to \(\operatorname{KG}(n,2)\) for every integer \(n\ge5\), not to general \(\operatorname{KG}(n,r)\) or arbitrary intersecting hypergraph families. The formula counts named-color functions; it does not quotient by the automorphism group or by interchange of the two colors. Its complete polynomial is an explicit finite inclusion–exclusion sum rather than a short product or recurrence. No independent expert validation or exhaustive historical-priority guarantee is asserted.

## References

1. Z. Mansouri and D. A. Mojdeh, *Outer independent rainbow dominating functions in graphs*, Opuscula Mathematica **40** (2020), 599–615, https://doi.org/10.7494/OpMath.2020.40.5.599 .
2. A. Cabrera-Martínez, *A Note on Outer-Independent 2-Rainbow Domination in Graphs*, Mathematics **10** (2022), 2287, https://doi.org/10.3390/math10132287 .
3. B. Samadi and N. Soltankhah, *Further results on outer independent 2-rainbow dominating functions of graphs*, arXiv:2208.02340 (first public 2022-08-03), https://arxiv.org/abs/2208.02340 ; RAIRO Operations Research **57** (2023).
4. Q. Kang, V. Samodivkin, Z. Shao, S. M. Sheikholeslami, and M. Soroudi, *Outer-independent \(k\)-rainbow domination*, Journal of Taibah University for Science **13** (2019), 883–891, https://doi.org/10.1080/16583655.2019.1655255 .
5. *Outer-independent two-rainbow weight enumerator of triangular graphs*, published public result, 2026-10-26, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-outer-independent-two-rainbow-weight-enumerator-of-triangular-gr--5892cf5f68ec .
6. *Exact multi-rainbow domination of two-subset Kneser graphs*, published public result, 2026-10-13, https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-exact-multi-rainbow-domination-of-two-subset-kneser-graphs--8baf309aa150 .
