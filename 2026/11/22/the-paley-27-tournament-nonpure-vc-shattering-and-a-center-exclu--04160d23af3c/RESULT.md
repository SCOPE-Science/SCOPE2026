# The Paley-\(27\) tournament: nonpure VC shattering and a center-exclusion gap

## Finding
Let \(F=\mathbb F_{27}\), let \(Q=\{u^2:u\in F^\times\}\), and consider the Boolean concept class \(\mathcal H=\{c+Q:c\in F\}\) on the domain \(F\). The zero difference is negative, and an ordinary VC trace may be witnessed by **any** center, including a center in the query support. Its exact shattered-support polynomial is
\[
\boxed{\Phi(z)=1+27z+351z^2+2925z^3+5967z^4.}
\]
Thus \(\operatorname{VCdim}(\mathcal H)=4\). All triples are shattered, but only 5967 of the 17550 four-point supports are. The shattered four-point supports consist of seven orbits under the specified affine semilinear group, of sizes \(1053,1053,1053,1053,1053,351,351\).

If a trace on \(T\) must instead be realized by a center \(c\notin T\), the entire corresponding off-support shattering polynomial is
\[
\boxed{\Phi_{\mathrm{off}}(z)=1+27z+351z^2+2925z^3.}
\]
The resulting center-excluded dimension is three: no four-point support realizes all sixteen traces with its center outside the support. This distinction does not alter the ordinary VC-dimension definition.

The ordinary shattering complex is **nonpure**. Besides its 5967 four-vertex facets, exactly 351 three-vertex supports are maximal. These 351 exceptional triples form one affine-semilinear orbit and, as blocks on the 27 vertices, a simple \(2\)-\((27,3,3)\) design. Its complete nonzero reduced homology over \(\mathbb F_2\) is
\[
\boxed{\widetilde\beta_2=351,\qquad\widetilde\beta_3=3718.}
\]

## Assumptions and scope
Write \(F=\mathbb F_3[u]/(u^3-u+1)\). The polynomial has no root in \(\mathbb F_3\), so it is an irreducible cubic. Encode \(a+bu+cu^2\), for \(a,b,c\in\{0,1,2\}\), by the integer \(a+3b+9c\). These labels are **not** residues in \(\mathbb Z/27\mathbb Z\). Multiplication is reduced by \(u^3=u-1\). There are 13 nonzero squares, and \(-1\) is nonsquare, so \(x\to y\) iff \(y-x\in Q\) defines the Paley tournament.

For any support \(T\subseteq F\), define its realized trace family
\[
\mathcal T(T)=\{(c+Q)\cap T:c\in F\}.
\]
Ordinary shattering means \(\mathcal T(T)=2^T\). For the **different**, off-support version use \(\mathcal T_{\mathrm{off}}(T)=\{(c+Q)\cap T:c\in F\setminus T\}\); this is full off-support shattering only if \(\mathcal T_{\mathrm{off}}(T)=2^T\).

The named symmetry group is
\[
G=\{x\longmapsto ax^{3^j}+b:a\in Q,\ b\in F,\ j\in\{0,1,2\}\},\qquad |G|=13\cdot27\cdot3=1053.
\]
Every such map preserves the concepts, all ordinary traces, and the off-support constraint. No claim about the full automorphism group is needed. Homology is ordinary simplicial homology with coefficients in \(\mathbb F_2\), reduced in degree zero. No integral homotopy type is asserted.

## Proof
**1. Exhaustive trace criterion and a dimension ceiling.** Fix distinct queried vertices \(t_1,\ldots,t_k\). For every \(c\in F\) form the binary integer \(m_c=\sum_{i=1}^k 2^{i-1}\mathbf 1[t_i-c\in Q]\). A support is shattered precisely when \(\{m_c:c\in F\}=\{0,\ldots,2^k-1\}\). Restricting the centers to \(F\setminus T\) gives the off-support criterion. Because there are only 27 concepts, no support of size at least five is shattered (\(2^5=32>27\)). Therefore exhaustive tests for supports of sizes at most four settle the entire polynomial; no untested larger supports are involved.

**2. Small supports and the complete orbit certificate.** Directly applying the stated trace criterion to every support of size one, two, three and four yields respectively \(27,351,2925,5967\) shattered nonempty supports. The off-support counts are \(27,351,2925,0\). The 22 rows of `orbit_table.csv` classify **every** four-point support under \(G\): each row gives an integer-coordinate representative, its full orbit size, the number of distinct ordinary traces, and the number of off-support traces. The row sizes sum to \(\binom{27}{4}=17550\). Precisely seven rows have sixteen ordinary traces, with representatives
\[
\begin{gathered}
\{0,1,2,18\},\ \{0,1,3,4\},\ \{0,1,3,9\},\\
\{0,1,3,15\},\ \{0,1,3,16\},\ \{0,1,3,20\},\ \{0,1,3,23\}.
\end{gathered}
\]
The first five have orbit size 1053; the last two size 351. **All 22 rows have strictly fewer than sixteen off-support traces**, which proves the sharp center-exclusion gap without assuming an untested higher-dimensional obstruction. As a concrete ordinary four-point witness, \(T=\{0,1,2,18\}\) realizes patterns \(0,1,\ldots,15\) using respective centers
\[
6,2,0,19,13,18,25,3,8,10,12,21,1,23,20,5.
\]
For this support, the pattern with binary mask \(1\) can only be realized by center \(2\in T\); it has no off-support realization. The standalone verifiers rebuild the entire table from field arithmetic and do not trust stored tables as input.

**3. Nonpurity and the design of exceptional triples.** Every three-point support is shattered. A triple is maximal in the shattering complex if no shattered quadruple contains it. The complete incidence census yields exactly 351 such triples; they are the orbit of \(\{0,1,10\}\) under \(G\). Each pair of vertices belongs to exactly three of these exceptional triples: the group \(G\) acts transitively on unordered pairs (for an unordered difference, exactly one sign is square), so the pair multiplicity is constant; double counting gives \(3\cdot351/\binom{27}{2}=3\). There are 5967 four-point facets and no larger ones. Hence the complex is nonpure with facet sizes three and four, and the exceptional triples form a \(2\)-\((27,3,3)\) design.

**4. Mod-two boundary ranks.** All vertices, edges and triangles are faces, hence the two-skeleton is the full two-skeleton on 27 vertices. It has boundary ranks \(\operatorname{rank}\partial_1=26\) and \(\operatorname{rank}\partial_2=\binom{26}{2}=325\) over \(\mathbb F_2\) (as follows from the chain complex of a full simplex). The four-vertex faces contribute 5967 tetrahedra. Represent the boundary of each tetrahedron as the 2925-bit indicator of its four triangular faces and perform exact binary column elimination. Both separately implemented complete verifiers return \(\operatorname{rank}\partial_3=2249\). Thus
\[
\begin{aligned}
\widetilde\beta_0&=0,\quad \widetilde\beta_1=0,\\
\widetilde\beta_2&=2925-325-2249=351,\\
\widetilde\beta_3&=5967-2249=3718.
\end{aligned}
\]
There are no simplices in higher dimensions. The independent Euler characteristic check is \(3718-351=3367\).

## Verification
Run `python3 verify_python.py` and `g++ -O2 -std=c++17 -Wall -Wextra -pedantic verify_cpp.cpp -o paley27_check && ./paley27_check`. Both require only standard Python or C++ facilities. The Python program builds \(\mathbb F_3[u]/(u^3-u+1)\) using direct nonzero squaring and independently enumerates all 17550 quadruples, 2925 triples, and all 1053 group maps. The C++ program uses the distinct irreducible polynomial \(t^3-t-1\), Euler's criterion to identify squares, and different elimination and orbit procedures. Both reconstruct the same face counts, strict off-support counts, 351 exceptional triples, seven top-face orbits, and boundary rank 2249. The CSV is regenerated by the Python program. `python_output.txt` and `cpp_output.txt` are representative exact successful outputs, not substitutes for executing the source.

## Relationship to prior work
McDonald, Sahay and Wyman, *The VC-dimension of quadratic residues in finite fields*, first publicly posted 2022-10-07 (arXiv:2210.03789), define quadratic-residue translate shattering and prove large-field estimates. Their §4 numerical experiments explicitly restrict to **prime** fields, and they discuss an additional center-exclusion convention when handling the zero character. The present result enumerates the first nonprime field order congruent to three modulo four, compares the two explicitly defined trace conventions there, and gives the full ordinary polynomial, exceptional-triple design, orbit spectrum and mod-two homology. Neither their asymptotic inequalities nor their prime-field tables imply these finite coefficients.

Pham, Senger, Tait and Nguyen, *VC-dimension and pseudo-random graphs* (first posted 2023-03-14; arXiv:2303.07878), give general sufficient conditions for small lower bounds in graph-neighborhood classes, not an exact Paley-27 enumeration. Published Paley-tournament extension-property classifications include exact **minimum** off-support witness multiplicities for triples, giving in particular the three-point off-support property at order 27; this covers that lower-dimensional constituent of the current result but does not give the 5967 ordinary quadruples or the 351 exceptional maximal triples. A rank-five genericity threshold for Paley tournaments tests **every** four-point support for off-support witnesses and fails at order 27; that universal failure alone does not establish that **no** four-point support is off-support shattered.

The existing Paley-25 shattering polynomial concerns an **undirected** Paley graph in characteristic five, and its counts do not determine the oriented 27-vertex example. The Paley-23 common-out-neighborhood complex is the downward closure of individual positive neighborhoods; it is not the complex of supports realizing *all* Boolean traces, so its homology cannot be substituted for the homology above.

## Limitations
This is an exact finite result **only** for the field of order 27 and the specified open-neighborhood convention. The finite programs exhaust all relevant supports but do not prove an all-field-order formula, an integral homology classification, or a homotopy-type statement. Symmetry is asserted only for the explicitly given group. Off-support shattering is carefully kept distinct from ordinary VC shattering. Some historical literature or computational tables may be unindexed; independent mathematical and priority review has not been performed.

## References
- B. McDonald, A. Sahay, E. L. Wyman, *The VC-dimension of quadratic residues in finite fields*, arXiv:2210.03789 (first submission 2022-10-07), https://arxiv.org/abs/2210.03789.
- T. Pham, S. Senger, M. Tait, N. Thu-Huyen, *VC-dimension and pseudo-random graphs*, arXiv:2303.07878 (first submission 2023-03-14), https://arxiv.org/abs/2303.07878.
- *A sharp rank-five genericity threshold for finite Paley tournaments*, publicly indexed mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-sharp-rank-five-genericity-threshold-for-finite-paley-tourname--981ee7b69845.
- *Sharp four-variable deletion thresholds for Paley tournaments*, publicly indexed mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-four-variable-deletion-thresholds-for-paley-tournaments--9f37c0d19d9b.
- *The exact Paley-25 shattering polynomial and its exceptional triples*, publicly indexed mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-the-exact-paley-25-shattering-polynomial-and-its-exceptional-tri--d709a1a3fcdd.
- *The Paley-23 out-neighborhood complex: a mixed sphere wedge and affine homology character*, publicly indexed mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-the-paley-23-out-neighborhood-complex-a-mixed-sphere-wedge-and-a--d2e37276ff47.
