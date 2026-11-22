# Quadratic-character shattering and persistent first cohomology for projective special linear actions

## Finding
Let \(q\ge5\) be an odd prime power, \(P=\mathbb P^1(\mathbb F_q)\), and \(G=\operatorname{PSL}_2(q)\) in its natural action on \(P\). For each \(g\in G\), take the Boolean concept \(C_g=\{(x,gx):x\in P\}\) on the query space \(P\times P\). Then a query support is shattered precisely when it is one of the following:

1. The empty set or a matching of at most two input-output pairs.
2. A matching of three pairs whose unique projective transformation in \(\operatorname{PGL}_2(q)\) has square determinant class.

Here a *matching* means that no two selected cells share a first coordinate or a second coordinate. In particular, the complete shattering polynomial, with coefficients counting all shattered supports, is
\[
\Phi_{q}(z)=1+(q+1)^2z+2\binom{q+1}{2}^{\!2}z^2+3\binom{q+1}{3}^{\!2}z^3,
\qquad \operatorname{VCdim}=3.
\]
Exactly half the three-rook matchings are shattered. The shattering complex is pure of dimension two, and it contains the full one-skeleton of the \((q+1)\)-square chessboard complex, but not its full two-skeleton.

Further, this complex has a canonically defined nonzero first cohomology class over \(\mathbb F_2\), arising from the quadratic character of determinants. Consequently
\[
H^1(\mathcal K_q;\mathbb F_2)\ne0
\quad\text{and}\quad H_1(\mathcal K_q;\mathbb F_2)\ne0
\qquad(q\ge5\text{ odd}).
\]
For the two smallest eligible odd prime fields, exact binary boundary-rank computations give
\[
\begin{array}{c|rrrr|rrr}
q&f_0&f_1&f_2&\operatorname{rank}_{\mathbb F_2}\partial_2&\widetilde\beta_0&\beta_1&\beta_2\\\hline
5&36&450&1200&414&0&1&786\\
7&64&1568&9408&1504&0&1&7904
\end{array}.
\]
For the exceptional odd field \(q=3\), no three-cell support is shattered: \(\Phi_3(z)=1+16z+72z^2\) and \(\operatorname{VCdim}=2\).

## Assumptions and scope
For any finite field \(\mathbb F_q\), \(\operatorname{PGL}_2(q)\) is the group of invertible \(2\times2\) matrices modulo nonzero scalar matrices, acting on one-dimensional vector subspaces of \(\mathbb F_q^2\). In odd characteristic, the determinant's quadratic-character sign is unchanged by scalar rescaling, and its kernel in \(\operatorname{PGL}_2(q)\) is \(\operatorname{PSL}_2(q)\). Write \(\chi:\mathbb F_q^\times\to\{\pm1\}\) for the quadratic character.

A finite set of query cells \(S\subseteq P\times P\) is *shattered* if \(\{C_g\cap S:g\in G\}=2^S\). Write \(\mathcal K_q\) for the simplicial complex of all shattered supports and \(\Phi_q(z)=\sum_{S\in\mathcal K_q}z^{|S|}\). Faces are unordered sets of cells, not ordered triples. All homology and cohomology claims below use coefficients \(\mathbb F_2\); no statement about integral homology or arbitrary fields is asserted.

## Proof
**1. Transitivity and unique positive triples.** Put \(n=q+1\). The action of \(\operatorname{PGL}_2(q)\) on ordered triples of distinct points is sharply three-transitive: any ordered distinct source triple is carried to any ordered distinct target triple by exactly one projective transformation. The subgroup \(G\) has index two in \(\operatorname{PGL}_2(q)\), is two-transitive, has order \(n(n-1)(n-2)/2\), and its stabilizer of an ordered pair has size \((q-1)/2\). A set with two cells sharing a source or target cannot realize the all-positive labeling; hence every shattered support is a matching.

**2. All matching pairs are shattered.** For two compatible cells, the number of transformations realizing both positives is \(|G|/[n(n-1)]\), and the number realizing a specified singleton positive is \(|G|/n\). The numbers realizing exactly one positive and zero positives on the two cells are respectively \(|G|/n-|G|/[n(n-1)]\) and \(|G|(1-2/n+1/[n(n-1)])\), all positive for \(q\ge3\). A single cell likewise realizes both labels. Therefore every matching support of size at most two is shattered (also at \(q=3\)).

**3. Exact triple criterion.** Consider a matching \(T=\{(x_i,y_i):i=1,2,3\}\) and the unique \(h\in\operatorname{PGL}_2(q)\) taking all three sources to their targets. The all-positive trace exists exactly if \(\chi(\det h)=1\). If it exists, its sole witness in \(G\) is \(h\). For any prescribed two positives and one negative, the number of witnesses is \((q-1)/2-1>0\) since \(q\ge5\). For one specified positive and two negatives, inclusion-exclusion gives \(|G|(n-3)/[n(n-1)]+1>0\), while for the zero-positive trace it gives \(|G|(1-3/n+3/[n(n-1)])-1>0\). Thus all eight traces exist, and the criterion is sufficient as well as necessary. If \(q=3\), the two-point stabilizer has size one, so no supported triple realizes a labeling with precisely two positives: there are no shattered triples.

**4. No larger shattered support.** If a matching of four cells had all-positive and three-positive/one-negative traces, those two realizations would agree on three source-to-target equations. Sharp three-transitivity in \(\operatorname{PGL}_2(q)\) forces them to be the same transformation, a contradiction. Any nonmatching has already been excluded. The vertex and edge counts follow from matching enumeration. The number of positive triple matchings is \(|G|\binom n3=3\binom n3^2\): each member of \(G\) gives \(\binom n3\) triple subsets of its graph, and uniqueness prevents double-counting. This also proves the claimed polynomial.

**5. Purity.** Every matching pair extends to a shattered triple. Indeed, first select \(g\in G\) realizing that pair, then add \((x,gx)\) for any third source \(x\). Therefore every vertex and edge extends to a two-face; the complex has no maximal face of smaller size.

**6. The universal cohomology class.** For each projective point \(x\), fix a nonzero representative \(v_x\in\mathbb F_q^2\). On the edge between cells \((x,y)\) and \((x',y')\), define a \(\mathbb F_2\)-valued cochain \(\omega\) by
\[
(-1)^{\omega((x,y),(x',y'))}
=\chi\!\left(\det(v_x,v_{x'})\det(v_y,v_{y'})\right).
\]
Both determinants are nonzero on an edge. Their product is independent of the ordering of the two cells. If a three-face is the graph of \(g\in G\) on three sources, write \(A\in\operatorname{GL}_2(q)\) for a representative. Its edge-sign product around the face equals \(\chi(\det A)^3=1\), because any projective rescaling factors occur twice. Hence \(\delta\omega=0\): \(\omega\) is a cocycle. If the representatives \(v_x\) change, its edge labels change only by a coboundary of a zero-cochain, so its cohomology class is independent of that auxiliary choice.

Choose a nonsquare \(a\in\mathbb F_q^\times\) and take three cells \((\infty,\infty),(0,0),(1,a)\), using the usual affine coordinates of the projective line. They form a triangle in the complete one-skeleton, although not a two-face. Its edge-sign product is \(\chi(a)=-1\); thus \(\omega\) evaluates to one on that closed one-cycle. A coboundary would evaluate to zero on every cycle. Therefore \([\omega]\ne0\) in \(H^1(\mathcal K_q;\mathbb F_2)\), and field duality gives \(H_1(\mathcal K_q;\mathbb F_2)\ne0\).

**7. Exact finite binary homology.** At \(q=5,7\), list all vertices \((x,y)\), all compatible pairs, and all three-rook matchings satisfying the determinant-character condition. Form the binary boundary matrix \(\partial_2\) with one row for each compatible pair and one column for each allowed three-face, with its three boundary edges marked. The independently obtained binary ranks are \(414\) and \(1504\). The one-skeleton is connected, so \(\operatorname{rank}\partial_1=f_0-1\), giving \(\beta_1=f_1-(f_0-1)-\operatorname{rank}\partial_2\) and \(\beta_2=f_2-\operatorname{rank}\partial_2\), as displayed. The complete enumeration and rank algorithms are included in `verify_psl.py` and `verify_character.cpp`.

## Verification
Run `python3 verify_psl.py`, then compile `verify_character.cpp` with `c++ -O2 -std=c++17 verify_character.cpp -o verify_character` and run `./verify_character`. The Python program independently enumerates determinant-one projective transformations and directly tests every Boolean trace on every compatible triple for \(q=3,5,7\). The C++ program uses determinant quadratic characters to construct all allowed triples and independently computes binary boundary ranks and a nontrivial cocycle witness for \(q=5,7\). Both reproduce \(\operatorname{rank}\partial_2=414,1504\), including the exact face and Betti counts. The all-prime-power assertion is proved mathematically in Steps 1–6; finite executions are checks, not substitutes for that proof.

## Relationship to prior work
Behajaina, Maleki and Razafimahatratra (2023) investigate intersection densities and derangement graphs for \(\operatorname{PSL}_2(q)\), including its natural two-transitive projective-line action. Their full text analyzes intersecting subfamilies of group elements and subgroup coset actions, not the shattering of individual point-image queries or the character-twisted subcomplex constructed here. Bayer, Goeckner and Jelić Milutinović (2019) classify ordinary matching complexes that are homology manifolds; their full text explicitly treats the full chessboard matching complex. Here the one-skeleton agrees with the chessboard complex but only one determinant-character half of its two-faces remains, so the ordinary matching-complex classification does not imply these face counts or this cohomology class. Work on the VC dimension of Hamming/Johnson neighborhood systems studies different concepts and query domains. Searches for equivalent terms such as three-rook character subcomplexes, orbit incidence of projective transformations and permutation-group point-image shattering did not locate a covering claim. Absence of a retrieved match is not proof of historical novelty.

## Limitations
No claim is made that \(\beta_1=1\) for all odd prime powers; this equality is established here only at \(q=5,7\). Likewise, no integral homology type, torsion order or general formula for top Betti numbers is asserted. The universal nonvanishing claim is specifically mod two. The exact computations for \(q=5,7\) are finite exhaustive calculations, while the all-field shattering criterion and cohomology obstruction have mathematical proofs. Research-record indexing may omit historically equivalent constructions; an independent expert priority review has not taken place.

## References
1. A. Behajaina, R. Maleki and A. S. Razafimahatratra, *On the intersection spectrum of \(\operatorname{PSL}_2(q)\)*, arXiv:2306.07851, first posted 2023-06-13, https://arxiv.org/abs/2306.07851 .
2. M. Bayer, B. Goeckner and M. Jelić Milutinović, *Manifold Matching Complexes*, arXiv:1906.03328, first posted 2019-06-07, https://arxiv.org/abs/1906.03328 .
3. I. Adler, B. G. Benediktsson and D. Macpherson, *Vapnik–Chervonenkis dimension and density on Johnson and Hamming graphs*, arXiv OA context and Discrete Applied Mathematics 312 (2022), DOI:10.1016/j.dam.2021.09.017, https://eprints.whiterose.ac.uk/id/eprint/178584/ .
