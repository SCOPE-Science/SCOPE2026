# Maximal square-zero linear subalgebras of the four-by-four nilradical

## Finding
Let \(k\) be any field and \(N=\mathfrak n_4(k)\) the associative algebra of strictly upper-triangular \(4\times4\) matrices. An *admissible space* is a \(k\)-linear subspace \(W\subseteq N\) such that \(X^2=0\) for every \(X\in W\). Maximality means maximal under inclusion among admissible linear subspaces, not merely maximal dimension.

**Classification.** Every inclusion-maximal admissible space is automatically an associative (nonunital) subalgebra. Exactly one has dimension four, namely
\[
 W_0=\{X\in N:X_{12}=X_{34}=0\}=\operatorname{span}_k(E_{13},E_{14},E_{23},E_{24}).
\]
Every other maximal admissible space has dimension three. Define
\[
 X=\begin{pmatrix}0&a&b&c\\0&0&d&e\\0&0&0&f\\0&0&0&0\end{pmatrix},\qquad
 M(X)=\begin{pmatrix}a&b\\-f&e\end{pmatrix}.
\]
For each projective column \([p]\in\mathbb P^1(k)\) and projective row \([r]\in\mathbb P^1(k)\), define
\[
\begin{aligned}
 W^{\mathrm{col}}_{[p]}&=\{X:d=0,\ M(X)=p\ell^{\mathsf T}\text{ for some }\ell\in k^2,\ c\in k\},\\
 W^{\mathrm{row}}_{[r]}&=\{X:d=0,\ M(X)=vr^{\mathsf T}\text{ for some }v\in k^2,\ c\in k\}.
\end{aligned}
\]
The full list comprises \(W_0\), every \(W^{\mathrm{col}}_{[p]}\), and all \(W^{\mathrm{row}}_{[r]}\) except \(W^{\mathrm{row}}_{[(0,1)]}\), which is properly contained in \(W_0\). These spaces are pairwise distinct.

**Exact finite-field incidence and algebra types.** For every prime power \(q\), there are exactly \(2(q+1)\) such maximal spaces in \(\mathfrak n_4(\mathbb F_q)\): one of dimension four, and \(2q+1\) of dimension three. Make a simple graph on these spaces by joining distinct \(W,W'\) when \(\dim(W\cap W')=2\). This graph is exactly \(K_{q+1,q+1}\); every nonadjacent distinct pair has intersection dimension one. The bipartition consists of \(W_0\) together with the \(q\) retained row spaces, opposite the \(q+1\) column spaces.

Precisely \(q-1\) maximal spaces have **nonzero multiplication**; all are three-dimensional column spaces and have a basis \(x,y,z\) with \(xy=z\), \(yx=-z\), and every other basis product zero. The other \(q+3\) spaces are zero-product algebras (one four-dimensional, \(q+2\) three-dimensional). Thus in odd characteristic the \(q-1\) nonzero-product spaces are noncommutative, whereas in characteristic two *every* maximal square-zero space is commutative, though \(q-1\) still have nonzero multiplication.

**Point incidence.** The square-zero locus has \(2q^4-q^2\) elements. Every element of \(kE_{14}\) lies in all \(2(q+1)\) maximal spaces; every square-zero element with \(d\ne0\) lies only in \(W_0\); and every other square-zero element outside \(kE_{14}\) lies in exactly two maximal spaces. The cardinalities of these three disjoint strata are, respectively, \(q\), \(q^3(q-1)\), and \(q^4+q^3-q^2-q\).

## Assumptions and scope
The field \(k\) is arbitrary for the classification and the automatic-subalgebra assertion. The counting, graph, and point-incidence statements use \(k=\mathbb F_q\), where \(q\ge2\) is any prime power. No restriction on characteristic is imposed. Every inclusion is an inclusion of embedded linear spaces in the fixed flagged matrix algebra, not a classification modulo general linear conjugacy. Dimensions are over \(k\). In characteristic two, \(-z=z\) in the multiplication table above.

## Proof
**1. Square-zero equations and the compulsory center.** Direct multiplication gives
\[
 X^2=adE_{13}+(ae+bf)E_{14}+dfE_{24}.
\]
The line \(Z=kE_{14}\) annihilates \(N\) on both sides, so any maximal admissible \(W\) must contain \(Z\). A useful elementary fact over any field (including \(\mathbb F_2\)) is: if linear functionals \(\lambda,\mu\) on a vector space obey \(\lambda(v)\mu(v)=0\) for every \(v\), then one of the functionals is zero. Indeed, if they are proportional and nonzero, evaluate on a vector with nonzero value; if independent, choose a vector on which both equal one.

**2. Dichotomy by the middle coefficient.** If the functional \(d|_W\) is nonzero, the equations \(ad=df=0\) and the preceding fact force \(a|_W=f|_W=0\). Thus \(W\subseteq W_0\). The space \(W_0\) has dimension four and all its products vanish, hence is admissible and is the unique maximal one with nonzero middle functional. Otherwise \(d|_W=0\), and only the scalar quadratic equation \(ae+bf=0\) remains.

**3. All subspaces of the determinantal cone.** On the slice \(d=0\), quotient by \(Z\) and identify the other four coordinates with \(M(X)\in M_2(k)\). The equation \(ae+bf=0\) becomes \(\det M(X)=0\). Every linear subspace of \(M_2(k)\) consisting of singular matrices has dimension at most two, and every two-dimensional such subspace has either a fixed one-dimensional column image or a fixed one-dimensional row span. For completeness, take a nonzero rank-one matrix in the subspace and transform it by invertible left/right multiplication into \(E_{11}\). Each other matrix then has the form \(\begin{psmallmatrix}x&y\\z&0\end{psmallmatrix}\), since its determinant and that of its sum with \(E_{11}\) both vanish. Its determinant also gives \(yz=0\). Applying the linear-functional fact to \(y,z\) on the subspace forces either all \(y=0\), or all \(z=0\), yielding the asserted common row or column. Conversely, all such two-dimensional fixed-row/fixed-column spaces consist of rank-at-most-one matrices. Their parameters are distinct points of \(\mathbb P^1(k)\).

Lifting these planes with the free \(c\)-coordinate gives precisely the two projective-line families displayed in the finding. The row plane \(r=(0,1)\) has \(a=f=d=0\) and so lies in \(W_0\); every other plane includes a vector with \(a\ne0\) or \(f\ne0\), preventing containment in \(W_0\), and cannot be enlarged within \(d=0\) by the dimension bound. Thus the list is exhaustive and inclusion-maximal. The four-dimensional \(W_0\) itself cannot be extended, because any super-space would have nonzero \(d\) and still be contained in \(W_0\).

**4. Algebra structure.** Products of matrices with \(d=0\) are central:
\[
XY=(a_Xe_Y+b_Xf_Y)E_{14}.
\]
Therefore every listed three-space, which contains \(Z\), is automatically closed under multiplication. The four-space \(W_0\) has zero product. For fixed-row matrices \(M(X)=v_Xr^{\mathsf T}\), the coefficient of \(XY\) vanishes identically. For fixed-column matrices \(M(X)=p\ell_X^{\mathsf T}\), it equals
\[
 p_1p_2(\ell_{X,1}\ell_{Y,2}-\ell_{X,2}\ell_{Y,1}).
\]
It is nonzero for some pair exactly when both coordinates of \([p]\) are nonzero. Over \(\mathbb F_q\) this occurs at \(q-1\) of the \(q+1\) projective columns. Normalizing a pair of independent \(\ell\)-vectors gives the stated multiplication table, valid in every characteristic. In characteristic two the table becomes commutative, as also follows directly by polarizing \(X^2=0\).

**5. Intersections and complete bipartite graph.** Distinct fixed-column planes of rank-one matrices meet only at zero, as do distinct fixed-row planes. Any fixed-column plane and any fixed-row plane intersect in exactly the one-dimensional line spanned by their common outer product. Lifting adds the central line \(Z\), so intersections are dimension one in the same family and dimension two across the families. The excluded fixed-row plane has image \(W_0\cap\{d=0\}\); its intersection with another row plane is \(Z\), and with a column plane has dimension two. Replacing that excluded row plane by \(W_0\) therefore preserves the bipartite incidence rule. This proves the \(K_{q+1,q+1}\) statement and all pairwise dimensions.

**6. Square-zero point incidence.** The number of singular \(2\times2\) matrices over \(\mathbb F_q\) is \(1+(q^2-1)^2/(q-1)=q^3+q^2-q\). Hence the \(d=0\) slice of the square-zero locus has \(q(q^3+q^2-q)\) elements. The other component \(W_0\) has \(q^4\) elements, and their intersection has \(q^3\). Inclusion-exclusion gives \(2q^4-q^2\). Every nonzero singular matrix belongs to exactly two rank-one maximal planes, one of each ruling. If it lies in the exceptional row plane, replace that row plane by \(W_0\); otherwise use the two unmodified planes. All noncentral elements with \(d=0\) therefore lie in exactly two listed spaces, while \(d\ne0\) forces membership only in \(W_0\). The central line is contained in every maximal space. The stated stratum sizes follow immediately.

## Verification
The standalone Python 3 program `verify.py` uses exact modular arithmetic and enumerates all reduced-row-echelon linear subspaces of dimensions three, four, five and six inside \(\mathbb F_q^6\) for \(q=2,3\). It applies the literal matrix-square equations and polarization to test every listed subspace without relying on the classification. It then checks all inclusion-maximal subspaces, their dimensions, exact intersection graph, multiplication types, and containment multiplicities for every square-zero matrix in these two fields. Run `python3 verify.py` from the folder containing the program; expected stdout is in `verify_output.txt`. These finite checks corroborate, but do not replace, the all-fields proof.

## Relationship to prior work
Zhao, Wang and Wang's 2008-online paper studies invertible **linear preservers** of the square-zero locus in triangular matrix algebras; its abstract does not state a maximal-linear-subspace incidence classification. The complete full text was not accessible during this comparison, so an unexamined supporting lemma remains a priority risk. De Seguins Pazzis's 2011 first-version work on linear spaces with a sole eigenvalue proves global *nilpotent-space dimension* bounds, with extremal spaces of dimension six in the four-by-four niltriangular case; it does not identify the inclusion-maximal spaces of **square-zero** matrices. Its accessible full text was inspected (introduction and principal classification). A separately published 2026 research record *Three determinantal components of commuting square-zero pairs in the four-by-four nilradical* was also read in full: it classifies a variety of **ordered pairs** and records the single-matrix quadratic equations, not the maximal linear subspaces, their two-ruling incidence graph or multiplication types. The present proof separately establishes these features through a rank-one-pencil classification. The previously known square-zero equations and rank-one matrix geometry are not claimed as independently new.

## Limitations
The size is fixed at four-by-four; no generalization to higher matrix orders is asserted. The classification concerns embedded rational linear subspaces and their finite-field incidence, not the full Hilbert/Fano scheme with a possible nonreduced structure. No statement on automorphism-conjugacy orbits is made. The originality conclusion is a best-knowledge comparison, not independent global priority certification. The 2008 preserver paper's full text could not be inspected, and broader general theorems on singular matrix pencils or square-zero preservers could potentially subsume some classification details.

## References
- Y. Zhao, D. Wang and X. Wang, *Maps preserving square-zero matrices on the algebra consisting of all upper triangular matrices*, Linear and Multilinear Algebra 58 (2010), 121–136. First published online 2008-12-29. DOI: https://doi.org/10.1080/03081080802531770
- C. de Seguins Pazzis, *Spaces of matrices with a sole eigenvalue*, arXiv:1105.1872v1, first posted 2011-05-10, https://arxiv.org/html/1105.1872v3 (full accessible revision inspected). Primary MSC 15A30.
- *Three determinantal components of commuting square-zero pairs in the four-by-four nilradical*, published-finding corpus (published 2026-11-08), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-three-determinantal-components-of-commuting-square-zero-pairs-in--d2968257cb40 .
