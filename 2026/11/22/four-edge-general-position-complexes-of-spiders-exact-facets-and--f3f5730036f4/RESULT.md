# Four-edge-general-position complexes of spiders: exact facets and signed sphere wedges

## Finding
Let \(T=S(\ell_1,\ldots,\ell_d)\) be a spider with \(d\ge2\) arms of positive integral edge lengths \(\ell_i\), meeting only at a central vertex. Let \(\mathcal K_4(T)\) be the simplicial complex on \(E(T)\) whose faces are subsets \(A\) such that **no geodesic of \(T\) contains four edges of \(A\)**. Write \(s_i=|A\cap E(\text{arm }i)|\), and let \(s_{(1)}\ge s_{(2)}\) be the two largest arm counts (with zero counts retained).

**Classification.** A set \(A\) is a face if and only if \(s_{(1)}+s_{(2)}\le3\). Thus exactly three disjoint types occur: at most one edge per arm; two edges in one arm and at most one edge in each other arm; or three edges in one arm and no selected edges elsewhere.

**Complete enumerators.** If \(P_T(z)=\sum_{A\in\mathcal K_4(T)}z^{|A|}\) includes the empty face, then
\[
P_T(z)=\prod_{i=1}^d(1+\ell_i z)+z^2\sum_{i=1}^d\binom{\ell_i}{2}\prod_{j\ne i}(1+\ell_j z)+z^3\sum_{i=1}^d\binom{\ell_i}{3}.
\]
Let \(F_T(z)\) count inclusion-maximal faces by cardinality. If all arms have length one, \(F_T(z)=z^d\). Otherwise
\[
F_T(z)=z^{d+1}\sum_{i=1}^d\binom{\ell_i}{2}\prod_{j\ne i}\ell_j+z^3\sum_{i=1}^d\binom{\ell_i}{3}.
\]
In particular, \(\mathcal K_4(T)\) is pure exactly when \(d=2\) or \(\max_i\ell_i\le2\). For \(d\ge3\) and \(\max_i\ell_i\ge3\), its maximal faces have **exactly two sizes**, \(3\) and \(d+1\), giving an unbounded purity gap.

**Integral homotopy and symmetry at the first subdivided-star stage.** If every arm has length two, denote the complex by \(\mathcal K_d\). Then, for every \(d\ge2\),
\[
\mathcal K_d\simeq\bigvee^{d-1} S^d,
\qquad
\widetilde H_j(\mathcal K_d;\mathbb Z)=
\begin{cases}\mathbb Z^{d-1},&j=d,\\0,&j\ne d.\end{cases}
\]
Permuting the \(d\) arms, with their near and far edges kept in their respective positions, induces on the *integral* top-homology lattice the exact \(\mathfrak S_d\)-module
\[
\widetilde H_d(\mathcal K_d;\mathbb Z)\cong
\operatorname{sgn}_d\otimes
\ker\left(\mathbb Z^d\xrightarrow{\ \sum\ }\mathbb Z\right).
\]
This is an integral module identification, not merely a rational-character calculation.

## Assumptions and scope
The spider is a finite simple tree with a distinguished center and \(d\ge2\) nonempty internally vertex-disjoint paths starting there. Edge labels distinguish positions on different arms; within-arm edge positions matter as vertices of the complex, although the counting formulas depend only on arm lengths. A geodesic means the unique simple path connecting two tree vertices. The convention for *edge four-general position* is \(|A\cap E(P)|\le3\) for every such path \(P\), matching the edge \(k\)-general-position definition of Manuel–Prabha–Klavžar (2022 preprint, 2025 journal). The topology is that of the geometric realization of the finite abstract simplicial complex.

## Proof
**1. A two-arm path criterion.** Every simple path in a spider uses edges of at most two arms. For any two arms \(i,j\), choose endpoints beyond all selected edges on those arms (the leaves suffice). Their unique connecting path contains precisely the selected edges from arms \(i\) and \(j\), hence \(s_i+s_j\). For a single arm, a center-to-leaf path contains its \(s_i\) selected edges. Therefore the greatest number of selected edges on a geodesic is exactly \(s_{(1)}+s_{(2)}\) (the second count may be zero). The upper bound follows from the two-arm property; the lower bound follows from the selected two arms. This proves the if-and-only-if criterion.

**2. Exhaustive face decomposition.** If every \(s_i\le1\), we obtain \(\prod_i(1+\ell_i z)\). If some \(s_i=2\), the inequality forbids any other count exceeding one; choose the two selected edges in arm \(i\) and independently zero or one edge in the others. If some \(s_i=3\), all other counts vanish; choose three edges in that arm. No count can exceed three. The three cases are disjoint and exhaustive, yielding \(P_T(z)\).

**3. Maximal faces.** If \(\ell_i=1\) for every arm, the whole edge set is legal and is the sole maximal face. Otherwise, a legal set having at most one selected edge per arm can be enlarged, first by filling a vacant arm or (when all arms are occupied) by adding a second edge in any arm of length at least two. A legal set with exactly two edges in arm \(i\) is maximal exactly when each other arm has one selected edge: a vacant arm can otherwise be filled, whereas any further addition to a full configuration makes two largest counts sum at least four. A legal set with exactly three edges in arm \(i\) is already maximal, as a further edge in that arm gives count four and a selected edge in another arm gives counts \(3+1\). Conversely no other maximal cases exist. The two disjoint facet families have cardinalities \(d+1\) and \(3\), with coefficients as displayed. They coexist exactly when \(d\ge3\) and some \(\ell_i\ge3\); in the two-arm case their sizes coincide, and when all arms are length at most two only the first family occurs (apart from the all-length-one simplex). This establishes the purity criterion.

**4. The sphere wedge when each \(\ell_i=2\).** Write the two edge-vertices of arm \(i\) as \(a_i,b_i\), preserving their near/far order. Let \(D_i=\{a_i,b_i\}\) be a simplicial zero-sphere and \(B=D_1*\cdots*D_d\) their join. Thus \(|B|\cong S^{d-1}\), the boundary of the \(d\)-cross-polytope. For each \(i\), put
\[
X_i=\Delta(\{a_i,b_i\})*\mathop{*}_{j\ne i}D_j,
\]
where \(\Delta(\{a_i,b_i\})\) is the one-simplex with its faces. Its geometric realization is a closed \(d\)-ball (an interval joined with \(S^{d-2}\)), and \(\partial X_i=B\). The face classification says precisely that \(\mathcal K_d=X_1\cup\cdots\cup X_d\), while \(X_i\cap X_j=B\) for distinct \(i,j\). Therefore the complex consists of the common \((d-1)\)-sphere with \(d\) closed \(d\)-balls attached along their entire boundary by degree-one maps. Attach the first ball to make a contractible \(d\)-ball; every subsequent attaching sphere maps into this contractible subspace and is nullhomotopic. The resulting CW homotopy type is \(\bigvee^{d-1}S^d\), proving all integral homology assertions.

**5. The actual integral arm-permutation module.** Give \(B\) the orientation represented by the join product \((a_1-b_1)*\cdots*(a_d-b_d)\). Interchanging two factors of dimension zero reverses this orientation. Hence the arm-permutation action on \(\widetilde H_{d-1}(B;\mathbb Z)\cong\mathbb Z\) is \(\operatorname{sgn}_d\). Orient each relative \(d\)-ball class \([X_i,B]\) so that its boundary is the chosen orientation of \(B\). The group permutes these \(d\) relative classes with the same sign twist. Consequently
\[
H_d(\mathcal K_d,B;\mathbb Z)\cong\operatorname{sgn}_d\otimes\mathbb Z^d,
\]
and the connecting homomorphism to \(\widetilde H_{d-1}(B;\mathbb Z)\cong\operatorname{sgn}_d\) is the signed augmentation \((c_i)\mapsto\sum_i c_i\). The long exact sequence of the pair, together with \(H_d(B)=0\) and the homology of the wedge just established, identifies the top integral lattice with the kernel. No splitting over \(\mathbb Z\) is asserted or needed.

## Verification
The companion Python 3 program `verify_spider4.py` independently constructs each spider as a graph, obtains its unique paths by breadth-first search, tests every edge subset against every vertex-pair path, and counts faces and inclusion-maximal faces. It verifies the formulas on 52 unordered positive arm-length tuples, with two through five arms and at most nine edges. For equal two-edge arms with \(d=2,3,4,5\), it builds the entire simplicial chain complex and checks the predicted reduced Betti numbers over fields of characteristics \(2\), \(3\), and \(101\). It independently checks the signed arm-permutation formula on explicit oriented relative top chains under adjacent transpositions. Its expected success line is `VERIFY_OK spider_cases=52 homology_F2_F3_F101_and_integral_signed_permutation_d=2..5`. These finite checks support, but do not replace, the preceding universal proof.

## Relationship to prior work
Manuel, Prabha and Klavžar introduced the ordinary edge general-position invariant, whose forbidden geodesics contain three selected edges; their tree theorem computes only the maximum cardinality, not the higher-arity complex considered here. Their later edge \(k\)-general-position work defines the four-edge predicate and determines extremal numbers for toroidal networks, hypercubes and Beneš networks, without treating spider face/facet enumerators or their homotopy. Tian, Klavžar and Tan treat extremal *ordinary* edge general-position sets and block-graph bounds. A prior indexed result, *All edge general-position sets of spider trees* (2026), enumerates the ordinary three-edge-forbidden spider complex: its formula does **not** imply the four-edge-forbidden enumerator or the sphere-wedge/symmetry statement. The present theorem concerns a distinct threshold and directly relates the enumeration to integral equivariant topology.

## Limitations
The complete face/facet formulas apply to spiders, not general trees. The homotopy and integral symmetry classification is proved specifically for arms of length exactly two, not arbitrary arm lengths. The proof does not classify edge \(k\)-general-position complexes for all thresholds \(k\). The comparison to indexed and accessible primary literature is not a proof of worldwide publication priority; further indexing or other equivalent simplicial-complex terminology could reveal overlap. The program's finite-field homology tests do not alone exclude torsion, which is instead excluded by the explicit ball-gluing argument. No independent external validation is claimed.

## References
1. P. Manuel, R. Prabha and S. Klavžar, *Edge general position problem*, first posted 2021-05-10, arXiv:2105.04292; Bulletin of the Malaysian Mathematical Sciences Society 45 (2022), 2997–3009, https://doi.org/10.1007/s40840-022-01319-8.
2. P. Manuel, R. Prabha and S. Klavžar, *Generalization of edge general position problem*, first posted 2022-07-15, arXiv:2207.07357; The Art of Discrete and Applied Mathematics 8 (2025), article P1.02, https://doi.org/10.26493/2590-9770.1745.5f4.
3. J. Tian, S. Klavžar and E. Tan, *Extremal Edge General Position Sets in Some Graphs*, Graphs and Combinatorics 40 (2024), article 40, https://doi.org/10.1007/s00373-024-02770-z.
4. *All edge general-position sets of spider trees*, indexed mathematical finding, 2026-10-04, identifier `96369ffaa123`; covers the ordinary three-edge-forbidden condition.
