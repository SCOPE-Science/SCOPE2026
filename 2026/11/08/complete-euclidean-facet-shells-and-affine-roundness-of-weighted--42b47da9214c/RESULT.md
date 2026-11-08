# Complete Euclidean facet shells and affine roundness of weighted staircase difference bodies

## Finding

Let \(d\ge 2\), let \(a_1,\ldots,a_d>0\), and write
\[
v_0=0,\qquad v_j=\sum_{i=1}^{j}a_i e_i\quad(1\le j\le d),\qquad P_a=\operatorname{conv}\{v_i-v_j:0\le i,j\le d\}.
\]
This is the difference body of the weighted staircase (orthoscheme) simplex \(\operatorname{conv}\{v_0,\ldots,v_d\}\). In the unweighted case it is, up to translation, the sum of two oppositely ordered Freudenthal--Kuhn staircase simplices.

For each nonempty subset \(T\subseteq[d]\), let \(b_0=0\), and let \(b_i\in\{0,1\}\) change value precisely at the indices of \(T\):
\[
b_i=|T\cap[i]|\bmod 2,\qquad (u_T)_i=\frac{b_i-b_{i-1}}{a_i}.
\]
Then **all** the facets, with no repetition or redundancy, are
\[
|u_T\cdot x|\le1\qquad(\varnothing\ne T\subseteq[d]). \tag{1}
\]
Thus there are \(2(2^d-1)\) facets, and their Euclidean supporting-plane distances from the origin are
\[
\delta_T=\left(\sum_{i\in T}a_i^{-2}\right)^{-1/2}, \tag{2}
\]
with one opposite facet pair for each \(T\ne\varnothing\). Equal distances can occur for distinct subsets; equation (2), not a count of distinct numerical values, is the complete multiset.

The unique minimum enclosing Euclidean ball is centered at \(0\), has radius \(R=(\sum_i a_i^2)^{1/2}\), and contacts precisely the vertices \(\pm(a_1,\ldots,a_d)\). The maximum inscribed Euclidean radius is
\[
r=\left(\sum_i a_i^{-2}\right)^{-1/2}. \tag{3}
\]
**Every** maximum-ball center is described by the explicit nonempty \((d-1)\)-dimensional polytope
\[
\mathcal I_a=\left\{c\in\mathbb R^d: |u_T\cdot c|\le 1-r\|u_T\|_2\ \text{for all}\ \varnothing\ne T\subseteq[d]\right\}. \tag{4}
\]
At \(c=0\), exactly the two facets \(T=[d]\) touch the ball. All other facet pairs have strictly larger slack. Every \(c\in\mathcal I_a\) lies in \(u_{[d]}^\perp\); \(0\) is in the relative interior of the incenter set.

For an affine-invariant comparison, put \(y_i=x_i/a_i\), \(n=d+1\), \(F=\lfloor n^2/4\rfloor\), and
\[
Q_a(x)=y_1^2+\sum_{i=1}^{d-1}(y_i-y_{i+1})^2+y_d^2. \tag{5}
\]
The unique John ellipsoid (greatest-volume inscribed ellipsoid) and Loewner ellipsoid (least-volume enclosing ellipsoid) are respectively
\[
E_{\rm J}=\{Q_a\le n/F\},\qquad E_{\rm L}=\{Q_a\le2\}. \tag{6}
\]
The John ellipsoid touches precisely the facets corresponding to subsets of cardinality \(\lfloor n/2\rfloor\) or \(\lceil n/2\rceil\); every vertex touches the Loewner ellipsoid. More precisely, among opposite facet pairs, the balanced cardinalities give all tangencies (with the facet-indexing subsets of \([n]\) described in the proof).

The sharp affine Banach--Mazur containment factor between \(P_a\) and a Euclidean ball, allowing arbitrary invertible affine coordinate changes, is
\[
\operatorname{dist}_{\rm BM}(P_a,B_2^d)=\sqrt{2F/n}. \tag{7}
\]
Here distance means the multiplicative factor \(\inf\{\lambda\ge1:\exists\text{ an ellipsoid }E\text{ and a translation with }E\subseteq P_a\subseteq\lambda E\}\); it is **not** the logarithmic version of Banach--Mazur distance. Finally,
\[
\frac Rr=\sqrt{\left(\sum_i a_i^2\right)\left(\sum_i a_i^{-2}\right)}\ge d, \tag{8}
\]
with equality exactly when all weights are equal. Consequently, affine roundness is independent of the weights, while Euclidean roundness is uniquely best at constant weights and becomes arbitrarily poor under anisotropic scaling.

## Assumptions and scope

All weights are arbitrary strictly positive real numbers. The ambient norm in (2)--(4) and (8) is the **standard Euclidean norm on \(\mathbb R^d\)**. The ellipsoidal quadratic form in (5) is a separate affine-adapted metric. The polytope is full-dimensional, and a facet means a codimension-one face. No claim about dimension \(d=1\) or zero/negative weights is intended.

## Proof

**1. Linear identification.** Let \(H=\{z\in\mathbb R^n:\sum_{i=0}^{d}z_i=0\}\), and define the invertible linear map \(L:H\to\mathbb R^d\) by
\[
L(z)_k=a_k\sum_{j=k}^{d}z_j\qquad (1\le k\le d).
\]
With \(e_0,\ldots,e_d\) the coordinate basis of \(\mathbb R^n\), the image of \(e_j-e_i\) for \(0\le i<j\le d\) is precisely \(\sum_{k=i+1}^j a_ke_k\). Hence \(P_a=L(K_n)\), where \(K_n=\operatorname{conv}\{e_i-e_j:i\ne j\}\subset H\), the symmetric type-A complete-root polytope. The inverse map is
\[
z_0=-y_1,\qquad z_i=y_i-y_{i+1}\ (1\le i<d),\qquad z_d=y_d.
\]
Therefore \(\|L^{-1}x\|_2^2=Q_a(x)\), establishing the exact normalization in (5).

**2. Facet completeness.** For every nonempty proper \(S\subset[n]=\{0,\ldots,d\}\), one has the valid inequality \(\sum_{i\in S}z_i\le1\) on \(K_n\). Its equality face contains every root \(e_i-e_j\) with \(i\in S\), \(j\notin S\), and has dimension \(n-2=d-1\), since its direction space is the sum of the coordinate-difference spaces within the two nonempty sides. These are the only facets: if \(w\in H\) is a supporting functional, its maximum on roots is \(\max_i w_i-\min_i w_i\). At a facet, the maximizing roots must affinely span dimension \(d-1\), which occurs only if the coordinates of \(w\) take two levels, with nonempty maximizers at each level; hence the functional is proportional to a subset indicator modulo constants. This proves a complete, irredundant system of \(2^n-2\) inequalities.

Choose one representative of each complementary pair by requiring \(0\notin S\), and write \(b_i=\mathbf1\{i\in S\}\). The telescoping inverse formula yields
\[
\sum_{i\in S}z_i=\sum_{k=1}^{d}\frac{b_k-b_{k-1}}{a_k}x_k.
\]
The unique nonempty flip set \(T=\{k:b_k\ne b_{k-1}\}\) gives (1). Since \((b_k-b_{k-1})^2=1\) exactly on \(T\), equation (2) follows. The flip set \(T=[d]\) uniquely maximizes \(\|u_T\|_2\), because all \(a_i>0\).

**3. Balls and all inball centers.** Every vertex of \(P_a\) is an interval vector with one overall sign. Its squared norm is the sum of \(a_i^2\) on that interval, so the unique longest interval gives exactly the two maximizing vertices \(\pm(a_1,\ldots,a_d)\). Central symmetry implies that the minimum enclosing Euclidean ball has center zero: for any center \(c\), the maximum of the squared distances to an antipodal longest pair is \(R^2+\|c\|^2+2|\langle c,(a_i)_i\rangle|\), which exceeds \(R^2\) unless \(c=0\). This proves the enclosing assertion and uniqueness.

The two opposite facet inequalities associated with \(T=[d]\) bound the inradius by \(1/\|u_{[d]}\|_2\), even when its center is free, because the ball must fit between their parallel planes. The centered ball of this radius satisfies all inequalities (1), establishing (3). A ball with center \(c\) and radius \(r\) satisfies (1) exactly when \(|u_T\cdot c|+r\|u_T\|_2\le1\); this proves (4). The tight opposite pair forces \(u_{[d]}\cdot c=0\). For every proper \(T\), strict positivity of \(\sum_{i\in[d]\setminus T}a_i^{-2}\) gives a strict inequality at \(c=0\), so a small relative neighborhood of zero in that hyperplane belongs to (4). Thus its affine dimension is exactly \(d-1\), and only the full-flip facets contact the centered ball.

**4. Optimal ellipsoids and their contacts.** The symmetric group \(S_n\) acts irreducibly on \(H\) by permuting coordinates, preserves \(K_n\), and fixes only scalar positive-definite quadratic forms on \(H\). Uniqueness of the volume-optimal John and Loewner ellipsoids therefore makes both balls centered at zero in \(H\). All root vertices have squared norm \(2\), proving that the Loewner ball is \(\|z\|_2^2\le2\), with every root in contact. The subset facet functional restricted to \(H\) has squared norm \(k(n-k)/n\) when \(|S|=k\), and its hyperplane constant is one. The nearest facet therefore has squared distance \(n/\max_k k(n-k)=n/F\), attained exactly by the balanced-size subsets. Transforming by \(L\) gives (6) and the contact descriptions.

**5. Sharp affine containment factor.** It suffices to consider centered ellipsoids: if \(b+E\subseteq K_n\subseteq b+\lambda E\) for a centered ellipsoid \(E\), central symmetry also gives \(-b+E\subseteq K_n\subseteq-b+\lambda E\). Taking midpoints proves \(E\subseteq K_n\subseteq\lambda E\).

Write \(E=\{z\in H:z^{\mathsf T}B^{-1}z\le1\}\) for an arbitrary positive-definite \(B\) on \(H\). The conditions \(E\subseteq K_n\) and \(K_n\subseteq\lambda E\) are respectively
\[
v_S^{\mathsf T}Bv_S\le1\quad\text{for all proper }S,\qquad (e_i-e_j)^{\mathsf T}B^{-1}(e_i-e_j)\le\lambda^2,\tag{9}
\]
where \(v_S=\mathbf1_S-(|S|/n)\mathbf1\). Average \(B\) over all coordinate permutations. The first inequalities survive by linearity; the second survive by operator convexity of matrix inversion (or its Schur complement characterization). Irreducibility makes the average equal to \(tI_H\). A balanced-subset facet forces \(t\le n/F\), while a root vertex forces \(\lambda^2\ge2/t\ge2F/n\). The John ball itself attains equality; this proves (7), including optimization over all affine positions and ellipsoid shapes.

Finally, (8) is Cauchy--Schwarz applied to \((a_i)\) and \((a_i^{-1})\), with equality iff all \(a_i^2\) coincide.

## Verification

A standalone exact-rational verifier, `verify.py`, enumerates all interval vertices and all explicit facet inequalities for dimensions \(2\le d\le6\), including three different rational weight choices in each dimension (15 configurations total). It checks every facet's supporting property and affine rank, the exact centered inradius inequalities, the unique outer vertices, the root-space quadratic form, and all cardinality bounds used for the ellipsoids. The verifier passed all checks. These are bounded corroborating computations, not a substitute for the unrestricted proof above. Run `python verify.py` with Python 3 and `sympy` installed.

## Relationship to prior work

Qu and Lee's October 2026 papers study facets of Minkowski sums of Freudenthal--Kuhn staircase simplices and associated Cayley constructions; the special opposite pair considered here has normals consistent with their two-summand restrictions. Those results are **prior groundwork**, not a claim that the present facet *directions* alone are new. Beck--De Silva--Dorfsman-Hopkins--Pruitt--Ruiz (2013) connect ordinary (unsigned) complete interval-vector polytopes with type-A positive-root polytopes; the signed difference body, its metric facets, optimal-center locus and ellipsoids are distinct. The type-A complete-root combinatorial identification and general John/Loewner symmetry principles are classical and are used as known tools.

The claimed contribution is the **unified weighted Euclidean classification** for the natural opposite-staircase pair: all explicit supporting-plane distances, an exact high-dimensional incenter set despite only two centered tangencies, the unique two-contact enclosing ball, and its comparison with affine roundness. A related result on the Banach--Mazur distance of equiradial-star transportation spaces potentially subsumes the type-A affine-distance component in isolation; that component is not asserted as independently first discovered here.

## Limitations

Historical priority is provisional. Indexed searches cannot exclude inaccessible or unindexed proofs of equivalent weighted metric statements. The affine Banach--Mazur formula is obtained from standard type-A symmetry and should not be understood as an independent priority claim. No general result for arbitrary pairs of staircase simplices is asserted; the pair must be opposite. The weights are strictly positive; zero weights change dimension and facet structure.

## References

1. Y. Qu and J. Lee, *Facet normals of Minkowski sums of staircase simplices*, arXiv:2610.35689 (first publicly submitted 2026-10-26), Sections 1--3 and Remark 3.7. https://arxiv.org/html/2610.35689v2
2. Y. Qu and J. Lee, *On the facets of the Cayley polytope of Stanley's triangulation*, arXiv:2610.35668 (first publicly submitted 2026-10-26), Sections 1--3. https://arxiv.org/html/2610.35668v2
3. M. Beck, J. De Silva, G. Dorfsman-Hopkins, J. Pruitt, A. Ruiz, *The combinatorics of interval-vector polytopes*, Electronic Journal of Combinatorics 20(3), P22 (2013), arXiv:1211.2039, Sections 1 and 3. https://arxiv.org/abs/1211.2039
4. A. Higashitani, K. Jochemko, M. Michałek, *Arithmetic aspects of symmetric edge polytopes*, Mathematika 65 (2019), 763--784, doi:10.1112/S0025579319000147 (general prior combinatorics of symmetric edge polytopes).
