# Integral homotopy and full arm-symmetry modules of matching complexes of arbitrary spider trees

## Finding
Let \(a\ge3\), let \(\ell_1,\ldots,\ell_a\ge1\), and join one endpoint of paths of these *edge* lengths at a common center to form the spider tree \(T\). Let \(K=\mathsf M(T)\) be the simplicial matching complex: its vertices are the edges of \(T\), and a face is any set of pairwise vertex-disjoint edges. Set
\[
s=\sum_{i=1}^{a}\left\lfloor\frac{\ell_i}{3}\right\rfloor,\quad
q=\#\{i:\ell_i\equiv2\pmod3\},\quad
r=\#\{i:\ell_i\equiv1\pmod3\}.
\]
Then the **integral homotopy type**, without unstated size bounds, is
\[
K\simeq
\begin{cases}
* & q\ge2\text{ or }(q=0,r=1),\\
S^s &q=1,\\
S^{s-1}&q=r=0,\\
\bigvee^{r-1}S^s&q=0,r\ge2.
\end{cases}
\]
The full automorphism group (because \(a\ge3\)) is \(G=\prod_{t\ge1}\mathfrak S_{I_t}\), where \(I_t=\{i:\ell_i=t\}\). Write \(R=\{i:\ell_i\equiv1\pmod3\}\), let \(\mathbb Z[R]\) be the integral permutation lattice, and define the one-dimensional integral character
\[
\chi(g)=\prod_{t\ge1}\operatorname{sgn}(g|_{I_t})^{\lfloor t/3\rfloor}.
\]
All reduced homology vanishes outside the unique indicated degree. In the three noncontractible regimes, the **complete integral \(\mathbb Z[G]\)-module** in that degree is respectively
\[
\begin{array}{c|c}
q=1&\mathbb Z_\chi \ (j=s)\\
q=r=0&\mathbb Z_\chi \ (j=s-1)\\
q=0,\ r\ge2&\mathbb Z_\chi\otimes\ker(\mathbb Z[R]\xrightarrow{\sum}\mathbb Z) \ (j=s).
\end{array}
\]
For example, lengths \((1,1,4,4,7,7)\) give \(s=6\), \(r=6\), \(q=0\), and a wedge of five six-spheres carrying a nontrivial \(S_2^3\)-integral representation. These formulas include arbitrary mixtures of short and long arms.

## Assumptions and scope
All graph edges are simple and unweighted, all arm lengths count edges rather than internal vertices, and all homology is reduced over \(\mathbb Z\). A point denotes contractibility. The formal augmented complex \(\{\emptyset\}\) is assigned sphere dimension \(-1\) only as the join unit; all displayed final spheres have nonnegative dimension. For \(s=0\) in the last case, a wedge of \(r-1\) copies of \(S^0\) means a discrete space with \(r\) points. Since the center is the unique vertex of degree greater than two, no automorphisms beyond independent permutations of equal-length arms exist. The homotopy equivalences are nonequivariant; the module identifications are integral and equivariant.

## Proof
**Path calculation.** Let \(P_n\) be a path on \(n\) vertices, and write \(J_n=\operatorname{Ind}(P_n)\), with \(J_0=\{\emptyset\}\). For \(n\ge3\), delete the penultimate path vertex. Its deletion complex contains the last vertex as an isolated graph vertex, hence is contractible, while its link is \(J_{n-3}\). The deletion–link cofibration therefore gives \(J_n\simeq\Sigma J_{n-3}\). Starting at \(J_0=S^{-1}\), \(J_1=*\), \(J_2=S^0\), induction yields
\[
J_{3k}\simeq S^{k-1},\quad J_{3k+1}\simeq *,\quad J_{3k+2}\simeq S^k,
\]
with the first identity interpreted formally at \(k=0\).

**Star-of-cones decomposition.** Denote the edge incident to the center on arm \(i\) by \(c_i\), and its remaining edges by \(d_{i,1},\ldots,d_{i,\ell_i-1}\). The edges \(c_i\) are mutually incompatible, while within an arm two edges are incompatible precisely when consecutive. Define \(A_i=J_{\ell_i-1}\), \(B_i=J_{\ell_i-2}\) if \(\ell_i\ge2\), and \(A_i=B_i=J_0\) when \(\ell_i=1\). These are complexes on the appropriate tails, with the natural inclusion \(B_i\hookrightarrow A_i\). Then, as an exact simplicial union,
\[
X=\bigast_{i=1}^{a}A_i,\qquad
L_i=B_i*\bigast_{j\ne i}A_j,\qquad
K=X\cup\bigcup_{i=1}^{a}(c_i*L_i).
\]
Each distinct pair of added cones intersects only inside \(X\); thus \(K\) is obtained by simultaneous mapping cones on \(L_i\hookrightarrow X\). The relative boundary map in integral homology is the sum of these inclusion maps, with each cone given the orientation induced by its apex.

**Residue classification and homotopy.** If \(\ell_i=3k\), then \(A_i\simeq S^{k-1}\) and \(B_i\) is contractible. If \(\ell_i=3k+1\), both \(A_i\) and \(B_i\) are \(S^{k-1}\) up to homotopy and the inclusion \(B_i\to A_i\) is a homotopy equivalence: for \(k=0\) it is the identity of \(J_0\); for \(k\ge1\), its cofiber is \(\Sigma J_{3k-2}\), which is contractible, so the inclusion induces an integral homology isomorphism between spaces each homotopy equivalent to the same sphere, hence is a homotopy equivalence. If \(\ell_i=3k+2\), then \(A_i\) is contractible and \(B_i\simeq S^{k-1}\).

For \(q\ge2\), at least two factors \(A_i\) are contractible; hence \(X\) and every \(L_i\) are contractible, so successively coning off these contractible subcomplexes leaves a contractible complex. For \(q=1\), \(X\) is contractible and all links except that corresponding to the unique residue-two arm are contractible. The exceptional link is a join of spheres of dimension \(s-1\); its cone contributes \(\Sigma S^{s-1}=S^s\). For \(q=0\), \(X\simeq S^{s-1}\); only the \(r\) residue-one arms have links homotopy equivalent to \(X\), and all of their maps \(L_i\to X\) are homotopy equivalences. Attaching no such cone preserves \(X\); attaching one makes it contractible; attaching \(r\ge2\) gives a wedge of \(r-1\) suspensions of \(X\), namely \(\bigvee^{r-1}S^s\). This last statement follows by identifying the common base with the first mapping cone (contractible) and attaching the other cones along maps which become nullhomotopic in that contractible space. The zero-dimensional case also follows directly from the ordinary star's disconnected matching complex.

**Integral symmetry and signs.** The group \(G\) acts by permuting the equal-length joins and added cones. Each noncontractible path factor of length \(3k\), \(3k+1\), or \(3k+2\) has reduced generator in degree \(k-1\); its suspended join degree is \(k\). Swapping two equal factors therefore contributes the Koszul sign \((-1)^{k^2}=(-1)^k\). This gives precisely the character \(\chi\), without using rational coefficients. If \(q=r=0\), the generator of the join \(X\) is \(\mathbb Z_\chi\). If \(q=1\), the unique exceptional link is fixed as an index and its reduced generator also transforms by \(\chi\), giving the same rank-one module after coning. Finally, if \(q=0,r\ge2\), choose each link generator so that its inclusion maps to the same integral orientation of \(\widetilde H_{s-1}(X)\). Then the relative long exact sequence has the natural \(G\)-equivariant segment
\[
0\longrightarrow\widetilde H_s(K;\mathbb Z)\longrightarrow
\mathbb Z_\chi\otimes\mathbb Z[R]
\xrightarrow{\,\operatorname{id}\otimes\sum\,}\mathbb Z_\chi
\longrightarrow\widetilde H_{s-1}(K;\mathbb Z)\longrightarrow0.
\]
The augmentation is surjective, so the asserted top homology lattice is its kernel, with no torsion. When \(s=0\), the same statement is interpreted using reduced degree-zero homology, and follows immediately by identifying the \(r\) isolated matching-complex vertices. This proves every displayed case over \(\mathbb Z\).

## Verification
Two standalone standard-library scripts reproduce finite checks from the literal spider edge sets. Run `python3 check_spider.py` and `python3 check_equivariant.py` in the same directory. The first enumerates all edge-disjoint subsets, constructs augmented simplicial boundary matrices and reduces them over \(\mathbb F_2\) for 765 arm-length profiles with at most four arms and total edge count at most 17. The second independently computes signed fixed-simplex traces under 146 arm permutations (114 equal-length, 32 mixed-length group actions) and checks the predicted integral-action characters against Lefschetz traces. Their actual outputs are included in `verification_output.txt`. These finite computations do **not** substitute for the infinite proof or determine integral torsion; integrality is proved by the explicit mapping-cone long exact sequence.

## Relationship to prior work
Jelić Milutinović, Jenne, McDonough and Vega (2019), arXiv:1905.10560, established general tools and exact sphere counts for caterpillar trees, but arbitrary spiders with three long arms need not be caterpillars. Donovan and Scoville (2022), arXiv:2207.13780, established the ordinary **Morse** complex of certain extended stars; via the subdivision correspondence between a tree's Morse complex and its subdivision graph's ordinary matching complex, this already covers some special spider profiles (notably uniform four-edge arms) nonequivariantly. A published integral arm-permutation calculation for precisely that special Morse-complex family also exists in the published-finding corpus corpus, and is **not** claimed as new here. Bayer, Jelić Milutinović and Vega (2024), arXiv:2411.04601, establish a general wedge-of-spheres result for outerplanar matching complexes and recall a three-edge path-contraction/suspension technique; the general fact of being a sphere wedge, and the possibility of simplifying individual long arms, are not new. The contribution here is the all-positive-length **closed phase classification**, exact sphere counts and dimensions for arbitrary *mixed* length profiles, together with the full integral equal-arm permutation module in every regime. The cited general contraction does not itself state or calculate the integral \(G\)-module or the global residue-zero/one/two interaction. Equivalent but unindexed literature, or a further implication of published reductions, remains possible.

## Limitations
No statement about a general graph or tree with multiple branching vertices, about geometric fixed spaces, or about equivariant homotopy equivalence is made. The low-order finite verification covers only specified parameters. The primary literature comparisons were made against recoverable full texts and statements; absence of an indexed match is not a proof of global uniqueness. Independent external auditing has not been performed.

## References
1. M. Jelić Milutinović, H. Jenne, A. McDonough and J. Vega, *Matching complexes of trees and applications of the matching tree algorithm*, arXiv:1905.10560v1, 25 May 2019. https://arxiv.org/abs/1905.10560
2. C. Donovan and N. A. Scoville, *Star clusters in the Matching, Morse, and Generalized Morse complex*, arXiv:2207.13780v1, 27 July 2022, especially Theorem 15. https://arxiv.org/html/2207.13780v1
3. M. Bayer, M. Jelić Milutinović and J. Vega, *Matching Complexes of Outerplanar Graphs*, arXiv:2411.04601v1, 7 November 2024. https://arxiv.org/abs/2411.04601
4. *Integral branch-permutation homology of extended-star Morse complexes*, published-finding corpus research record, 11 October 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-integral-branch-permutation-homology-of-extended-star-morse-comp--348812728b63
