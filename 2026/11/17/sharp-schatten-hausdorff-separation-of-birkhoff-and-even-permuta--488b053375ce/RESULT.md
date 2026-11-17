# Sharp Schatten Hausdorff separation of Birkhoff and even-permutation polytopes

## Finding
For each integer \(n\ge4\), remove all odd-permutation vertices from the \(n\)-th Birkhoff polytope, retaining the *even-permutation polytope*. Although exactly half the vertices are removed, the induced Hausdorff loss has the following exact profile for every Schatten index \(1\le p\le\infty\):
\[
d_H^{(p)}(\mathcal B_n,\mathcal E_n)=2(n-1)^{1/p-1},\qquad 1/\infty:=0.
\]
The nearest point in the parity-restricted polytope to any forbidden (odd) permutation matrix \(Q\) is
\[
M_Q=\frac{n-3}{n-1}Q+\frac{2}{n-1}J_n,
\qquad J_n=\frac{\mathbf1\mathbf1^T}{n}.
\]
For \(1<p<\infty\), this nearest point is unique, and the **only** Hausdorff-farthest points are the forbidden permutation vertices. The matrix \(M_Q\) is the barycenter of an exposed simplex face having precisely \(\binom n2\) vertices, all obtained from \(Q\) by composing one transposition.

At the three familiar indices, the exact gaps are \(2\) (nuclear norm), \(2/\sqrt{n-1}\) (Frobenius norm), and \(2/(n-1)\) (operator norm). Thus the defect vanishes in every fixed Schatten norm with \(p>1\), but not in the nuclear norm.

## Assumptions and scope
Work in the real matrix space \(\mathbb R^{n\times n}\). Write \(P_\sigma\) for the permutation matrix of \(\sigma\in S_n\), let \(A_n\) be the alternating subgroup, and define
\[
\mathcal B_n=\operatorname{conv}\{P_\sigma:\sigma\in S_n\},\qquad
\mathcal E_n=\operatorname{conv}\{P_\sigma:\sigma\in A_n\}.
\]
For a matrix \(X\), let \(\|X\|_{S_p}\) be the \(\ell_p\) norm of its singular values, including the largest singular value for \(p=\infty\). The Hausdorff distance is computed in the **unscaled ambient matrix norm**. For sets \(C,D\), use
\[
d_H^{(p)}(C,D)=\max\{\sup_{x\in C}\inf_{y\in D}\|x-y\|_{S_p},\ \sup_{y\in D}\inf_{x\in C}\|y-x\|_{S_p}\}.
\]
Here \(\mathcal E_n\subset\mathcal B_n\), so the second directed distance is zero. The dimension convention \(n\ge4\) ensures both are full-dimensional within the same affine space of doubly stochastic matrices. No volume, facet count, or typical-direction width assertion is made.

## Proof
**1. Odd trace barrier.** Let \(Q\) be an odd permutation matrix. Every even permutation matrix \(P\) satisfies that \(Q^TP\) is odd. An odd permutation cannot have exactly one moved point; it therefore fixes at most \(n-2\) points. Consequently
\[
\langle Q,P\rangle_F=\operatorname{tr}(Q^TP)\le n-2
\]
for each such \(P\), and by convexity for every \(X\in\mathcal E_n\). Equality holds among the even vertices exactly for \(P=QT_{ij}\), where \(T_{ij}\) exchanges labels \(i\) and \(j\).

**2. Sharp dual-norm lower bound.** Every doubly stochastic \(X\) satisfies \(\langle J_n,Q-X\rangle_F=0\). For \(X\in\mathcal E_n\), the trace barrier therefore gives
\[
2\le\langle Q-J_n,Q-X\rangle_F
\le\|Q-J_n\|_{S_q}\|Q-X\|_{S_p},
\qquad \frac1p+\frac1q=1.
\]
The matrix \(Q-J_n\) has singular values \(1\) repeated \(n-1\) times and one zero singular value: multiply on the left by \(Q^T\), obtaining \(I-J_n\), the orthogonal projection onto the zero-sum space. Thus \(\|Q-J_n\|_{S_q}=(n-1)^{1/q}\), proving
\[
\|Q-X\|_{S_p}\ge 2(n-1)^{1/p-1}.
\]
This argument remains valid at both endpoint indices.

**3. An explicit attaining point.** Average all \(\binom n2\) transpositions. Its diagonal entries are \((n-2)/n\), and every off-diagonal entry is \(2/(n(n-1))\). Hence
\[
\frac1{\binom n2}\sum_{i<j}T_{ij}
=\frac{n-3}{n-1}I+\frac2{n-1}J_n.
\]
Left multiplication by the odd \(Q\) converts each transposition into an even permutation, so their barycenter \(M_Q\) belongs to \(\mathcal E_n\). Moreover,
\[
Q-M_Q=\frac2{n-1}(Q-J_n).
\]
Its singular values are \(2/(n-1)\), each with multiplicity \(n-1\), and one zero. This attains the lower bound for every \(p\). For \(1<p<\infty\), strict convexity of Schatten \(p\) norms makes the closest point of a convex set unique.

**4. The exposed contact face.** The trace barrier shows that
\[
F_Q=\{X\in\mathcal E_n:\langle Q,X\rangle_F=n-2\}
=\operatorname{conv}\{QT_{ij}:1\le i<j\le n\}.
\]
The matrices \(T_{ij}\) are linearly independent: the off-diagonal entry in position \((i,j)\) distinguishes the corresponding matrix from all other transpositions. Multiplying by \(Q\) preserves linear independence. Hence their convex hull is a simplex of dimension \(\binom n2-1\). Its equal-weight barycenter \(M_Q\) lies in its relative interior. This is an *exposed face*, not a claim that it is a facet.

**5. Hausdorff maximum and rigidity.** Every \(X\in\mathcal B_n\) is a convex combination of permutation matrices. For each even vertex select itself as a feasible point in \(\mathcal E_n\); for each odd vertex use its matrix \(M_Q\). Combining these choices yields a point of \(\mathcal E_n\) at distance at most \(2(n-1)^{1/p-1}\) from \(X\), by the triangle inequality. Every odd vertex attains this bound, proving the exact Hausdorff formula. For \(1<p<\infty\), the Schatten \(p\) norm is strictly convex. Equality in the triangle inequality among the odd-vertex displacement vectors \(Q-M_Q=2(Q-J_n)/(n-1)\) is possible only when all positive-weight odd vertices are the same permutation matrix; any positive even-vertex weight gives a strict loss because its displacement vanishes. Therefore the farthest points are exactly the odd permutation vertices. □

## Verification
The accompanying executable `check_even_permutation_schatten.py` checks exact rational barycenter and trace identities for orders \(3\) through \(8\), enumerates all even and odd permutations at each order to verify the transposition equality condition, and checks the singular-value formulas at six norm indices. Separately, numerical constrained minimization over **all** even-permutation matrices at orders \(3,4,5\) reproduces squared Frobenius nearest-point distances \(2\), \(4/3\), and \(1\), respectively. The infinite-family result follows from the analytic trace/dual-norm argument, not those finite checks. Run with `python check_even_permutation_schatten.py` (Python 3, NumPy, SciPy).

## Relationship to prior work
The Birkhoff-von Neumann theorem and the even-permutation polytope itself are classical. Baumeister–Haase–Nill–Paffenholz (2007) studies permutation-group polytopes and acknowledges earlier alternating-group work; Cunningham–Wang (2004) studies facets and membership for exactly the even-permutation hull. Bouthat–Mashreghi–Morneau-Guérin (first public version 2023) establishes Schatten-norm geometric results for the *full* Birkhoff polytope, but not the parity-restricted Hausdorff comparison. The present claim is the sharp norm-by-norm **metric comparison between these two different polytopes**, together with exact projection points, complete strict-norm farthest-point classification, and simplex-face geometry. Facets, integrality and permutation-matrix descriptions are cited facts, not new claims.

## Limitations
Historical priority requires further human literature review, particularly of the 1991 and 2004 articles on even doubly stochastic matrices, whose complete texts could not be checked. The existence of equivalent inequalities does not by itself establish the Hausdorff formula, but an equivalent statement could be present in unavailable older sources. The uniqueness of nearest points and full classification of Hausdorff maximizers are proved only for \(1<p<\infty\); no such endpoint uniqueness claim is made. Independent mathematical validation has not been performed.

## References
1. L. Bouthat, J. Mashreghi, F. Morneau-Guérin, *On the Geometry of the Birkhoff Polytope. II. The Schatten p-norms*, arXiv:2310.14043v1 (first public 2023-10-21), https://arxiv.org/html/2310.14043v1 .
2. B. Baumeister, C. Haase, B. Nill, A. Paffenholz, *On permutation polytopes*, arXiv:0709.1615v1 (2007), https://arxiv.org/pdf/0709.1615 .
3. W. H. Cunningham, Y. Wang, *On the even permutation polytope*, Linear Algebra Appl. 389 (2004), 269–281, doi:10.1016/j.laa.2004.03.016 .
4. R. A. Brualdi, B. Liu, *The polytope of even doubly stochastic matrices*, J. Combin. Theory Ser. A 57 (1991), 243–253, doi:10.1016/0097-3165(91)90048-L .
