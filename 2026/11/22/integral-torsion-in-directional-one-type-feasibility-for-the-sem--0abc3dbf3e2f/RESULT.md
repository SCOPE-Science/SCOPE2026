# Integral torsion in directional one-type feasibility for the semigeneric digraph

## Finding
Let \(A\) be any **nonempty** finite induced substructure of the countable semigeneric homogeneous complete multipartite directed graph. Individually name its \(n\) vertices, which lie in \(k\geq1\) nonadjacency classes. Write \(\mathcal T(A)\) for its complete nonalgebraic one-point types and define the **directed feasibility matrix**
\[
M_A(\tau,\sigma)=\begin{cases}1,&\text{if distinct realizations }x\models\tau,\ y\models\sigma\text{ satisfy }x\to y,\\0,&\text{otherwise.}\end{cases}
\]
This is an integer square matrix that is generally not symmetric. It has order
\[
N=k2^{k-1}+2^n.
\]
For every such \(A\), the **complete integer Smith normal form** is
\[
\boxed{\operatorname{SNF}_{\mathbb Z}(M_A)=\begin{cases}
\operatorname{diag}(I_2,0_{N-2}),&k=1,\\
\operatorname{diag}(I_4,3,0_{N-5}),&k=2,\\
\operatorname{diag}(I_{2k+1},2I_{k^2-2k-1},2(k+1),0_{N-k^2-1}),&k\ge3.
\end{cases}}
\]
Thus the positive rational rank is \(2\) for \(k=1\), \(5\) for \(k=2\), and \(k^2+1\) for \(k\ge3\). For \(k\ge3\), rank in characteristic two drops to \(2k+1\); in odd characteristic \(p\), it drops by precisely one from the rational rank exactly when \(p\mid(k+1)\). At \(k=2\), characteristic three lowers the rank from five to four. All these invariants depend **only on the number of named nonadjacency classes**, even though \(N\) also depends on the total base size and the orientations of the base may vary.

## Assumptions and scope
The semigeneric class consists of finite simple digraphs in which nonadjacency (including equality) is an equivalence relation; between different classes every pair supports exactly one directed edge; and the four cross-edges of any rectangle formed by two vertices in each of two distinct classes have even parity when counted in one chosen direction. Its Fraïssé limit is homogeneous and realizes exactly the finite admissible diagrams. A nonalgebraic one-type requires the new vertex to differ from every individually named parameter. Existence of an arc, not uniqueness or a prescribed entire two-type, defines \(M_A\).

Choose one old representative \(a_i\) in each class \(i\in\{1,\dots,k\}\), and set \(b_{ij}=1\) if \(a_i\to a_j\) for \(i\ne j\). There are exactly \(2^{k-1}\) types in which the new vertex joins each particular old class \(i\): a type is represented by \((i,\alpha)\), with one independent bit \(\alpha_j\) per \(j\ne i\), where \(\alpha_j\) measures the orientation of the new vertex toward \(a_j\) relative to \(a_i\to a_j\). There are exactly \(2^n\) further types whose new point belongs to an entirely new nonadjacency class, one per arbitrary orientation to all old vertices. These are distinct complete types by homogeneity.

## Proof
**1. Exact realizability.** The rectangle law is equivalent to the fact that, between any two classes, the cross-orientation matrix over \(\mathbb F_2\) has the form \(r_u+c_v\). This proves the above classification of one-point types: extension inside old class \(i\) can independently flip its row relative to \(a_i\) toward each other old class, while a singleton new class participates in no rectangle with the old base. For two types \((i,\alpha)\) and \((j,\beta)\) with \(i\ne j\), the four-corner rectangle with \(a_i,a_j,x,y\) forces
\[
\mathbf1_{x\to y}=b_{ij}\oplus\alpha_j\oplus\beta_i.
\]
Here \(\oplus\) is addition modulo two. For two types joining the same old class no arc is possible. For a pair involving a fresh-class type, the desired directed arc is always possible: choose a distinct fresh class for that vertex (and two distinct fresh classes if necessary), so no rectangle contains two vertices in the relevant fresh class. Hence every fresh-type row and column of \(M_A\) consists entirely of ones. Universality realizes each allowed finite diagram.

For each unordered pair of old classes, a simultaneous relabelling of all bit patterns inside the relevant old classes can normalize the representative orientation \(b_{ij}\) to the canonical orientation \(b_{ij}=1\) for \(i<j\), without changing any integral Smith factor. Thus all base orientations give row-and-column permutation-equivalent matrices. The \(2^n\) duplicate fresh rows and columns split as one row/column plus \(2^n-1\) zero rows/columns by integral elementary operations.

**2. Integral difference reduction.** For a fixed old class \(i\), regard its \(2^{k-1}\) row indices as the Boolean cube on \(\{1,\dots,k\}\setminus\{i\}\). Replace standard basis vectors by the finite-difference vectors
\[
v_T=\sum_{U\subseteq T}(-1)^{|T|-|U|}e_{\mathbf1_U}.
\]
This is a triangular integer-unimodular change of basis. Each off-diagonal matrix block depends on only one row bit and one column bit, hence every difference with \(|T|\ge2\) gives an identically zero row and column. What remains has \(k\) indices per old class: a base vector \(p_i=v_\varnothing\) and \(k-1\) first differences \(d_{ij}=v_{\{j\}}\), plus one fresh vector \(f\). Its order is \(k^2+1\).

Write \(s_{ij}=1-2b_{ij}\in\{\pm1\}\). In this reduced matrix, all entries involving \(f\) and a base vector \(p_i\) equal one, \(M(f,f)=1\), and entries between \(f\) and any difference \(d_{ij}\) are zero. For distinct \(i,j\), the only nonzero entries involving \(d_{ij}\) are
\[
M(d_{ij},p_j)=s_{ij},\qquad M(d_{ij},d_{ji})=-2s_{ij},
\]
and likewise \(M(p_i,d_{ji})=s_{ij}\). The entries \(M(p_i,p_j)\) equal \(b_{ij}\) when \(i\ne j\), and zero when \(i=j\).

Pivot on the unit \(M(f,f)=1\). This replaces the \(p_i,p_j\) entry by \(b_{ij}-1\) for distinct indices and by \(-1\) on the diagonal, leaving the difference entries unchanged. Interpreting the rows as cokernel relations on column generators, the row \(d_{ij}\), divided by its unit sign, gives the **primitive** relation
\[
p_j-2d_{ji}=0\qquad(i\ne j).
\]

**3. Full integral cokernel.** If \(k\ge2\), for each \(j\) choose another class \(\rho(j)\ne j\) and put \(u_j=d_{j\rho(j)}\). Eliminate the generators \(p_j=2u_j\). Define differences \(t_{ji}=d_{ji}-u_j\), where \(i\ne j,\rho(j)\). The remaining difference relations say exactly \(2t_{ji}=0\). There are \(k(k-2)\) such torsion generators. The row \(p_i\) reduces, with no denominators, to
\[
u_i+\sum_{j=1}^{k}u_j=\sum_{j\ne i}s_{ij}t_{ji},
\]
where \(t_{j\rho(j)}\) denotes zero.

For \(k=2\), no \(t\)'s remain and the two relations have coefficient matrix
\[
\begin{pmatrix}2&1\\1&2\end{pmatrix},
\]
whose Smith factors are \(1,3\). Together with the pivot on \(f\) and the two primitive eliminations of \(p_j\), this gives \(I_4,3\).

For \(k\ge3\), choose \(\rho(1)=2\) and \(\rho(j)=1\) for \(j\ge2\). No torsion generator appears in the \(i=1\) row. Each of the rows \(i=2,\dots,k\) contains at least one **distinct** torsion generator with coefficient \(\pm1\), and no such generator occurs in any other row. Use these \(k-1\) unit coefficients to eliminate one torsion generator per row. The remaining \(k^2-3k+1\) torsion generators are independent of the \(u\)'s and have order two. The residual \(u\)-relations are
\[
H_1(u)=0,\qquad 2H_i(u)=0\ (i=2,\dots,k),\qquad H_i(u)=u_i+\sum_j u_j.
\]
Set \(v_i=u_i-u_1\) for \(i\ge2\). Subtracting the first relation from each of the others gives \(2v_i=0\), while the first becomes
\[
(k+1)u_1+\sum_{i=2}^k v_i=0.
\]
A unimodular change among the \(v_i\)'s takes their sum as one basis generator, which can be eliminated using the displayed primitive relation. This leaves \(2(k+1)u_1=0\), alongside \(k-2\) independent order-two generators. Combining with the earlier \(k^2-3k+1\) order-two generators gives the finite cokernel
\[
(\mathbb Z/2\mathbb Z)^{k^2-2k-1}\oplus\mathbb Z/[2(k+1)]\mathbb Z.
\]
Since \(2\) divides \(2(k+1)\), these are already invariant-factor ordered. Counting primitive pivots and zero rows gives the asserted Smith form. If \(k=1\), the matrix has one old-type index, all entries in the fresh block are one, and the remaining \(2\times2\) matrix \(\bigl(\begin{smallmatrix}0&1\\1&1\end{smallmatrix}\bigr)\) is unimodular. This proves all cases.

## Verification
The accompanying `VERIFY.py` constructs the normalized \((k2^{k-1}+1)\)-index feasibility matrix and computes its exact integer Smith factors for \(k=1,\dots,5\) using SymPy. Independently, for eight different finite parameter examples (including bases with nonsingleton old classes), it enumerates every one-point extension diagram directly, checks **all** four-corner parity constraints for every proposed directed pair-extension, compares every feasibility entry against the proved formula, and computes the exact Smith form of each uncompressed matrix. These examples comprise \(4130\) pair-entry tests. The verifier terminates with `VERIFY_OK`. Finite tests corroborate, but do not replace, the preceding proof for every \(k,n\).

## Relationship to prior work
The semigeneric digraph and its parity condition belong to Cherlin's classification. Jasiński, Laflamme, Nguyen Van Thé and Woodrow (arXiv:1310.6466, Section 10) already identify the \(2^{k-1}\) bit-pattern classes per old class and recover each interclass edge through the rectangle parity rule. Coskey and Ellis (arXiv:1509.04222, Section 4, Lemma 4.1) supply the known two-class row-plus-column factorization. Those ingredients and the one-point type counts are **not claimed as new**.

A previously published exact Stirling-layer semigeneric orbit profile (`5135d85e91a6`) counts labelled diagrams and tuple orbits; an earlier indexed result (`520d06f8-2950-42dd-98f5-aaa04053834e`) counts all ordered injective extension types over named bases; a two-class symmetry-character result (`03514b39812a`) counts finite orientation symmetries. These numerical profiles and fixed-point counts do not determine the **integral directed feasibility matrix or its Smith factors**. The new claim is the all-parameter-base arithmetic classification and explicit prime-characteristic rank obstructions, obtained from an integral Boolean-difference decomposition and a torsion-presentation reduction. Possible unindexed equivalent integer-matrix results remain a priority risk.

## Limitations
The result concerns the **existence** of an arc between realizations of two one-point types in the semigeneric digraph. It does not count individual complete two-point types over a specified pair, classify simultaneous three-point realizations, or determine ordinary eigenvalues. Orientation is directed, so no real inertia is claimed. The novelty assessment is based on specified inspections, not a proof of historical uniqueness. Independent mathematical review has not been performed.

## References
1. J. Jasiński, C. Laflamme, L. Nguyen Van Thé, R. Woodrow, *Ramsey precompact expansions of homogeneous directed graphs*, arXiv:1310.6466, first posted 2013-10-24, Section 10. https://arxiv.org/abs/1310.6466
2. S. Coskey, P. Ellis, *The conjugacy problem for automorphism groups of homogeneous digraphs*, arXiv:1509.04222, first posted 2015-09-14, Section 4; later *Contributions to Discrete Mathematics* 12 (2017), 62–73. https://cdm.ucalgary.ca/article/view/62551
3. M. Hamann, *Countable connected-homogeneous digraphs*, arXiv:1311.6016, first posted 2013-11-23, Section 6.3. https://arxiv.org/abs/1311.6016
4. *Exact Stirling-layer orbit profile of the semigeneric complete multipartite digraph*, published mathematical result, identifier `5135d85e91a6` (2026).
5. *Cycle-parity symmetry character for two-part semigeneric digraphs*, published mathematical result, identifier `03514b39812a` (2026).
