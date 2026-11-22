# Homothetic John and Löwner ellipsoids of the sporadic regular-matroid polytope

## Finding
Let \(D\in\mathbb R^{5\times5}\) be the symmetric circulant matrix with \(D_{ii}=-1\) and \(D_{i,i+1}=D_{i,i-1}=1\), indices modulo five, and other entries zero. Let \(M=[I_5\mid D]\) and let
\[
P=\operatorname{conv}\{\pm m_j:1\le j\le10\}\subset\mathbb R^5,
\qquad A=2(MM^T)^{-1}.
\]
This is the generalized symmetric-edge polytope in the displayed, standard integral realization of the exceptional ten-element regular matroid \(R_{10}\). Its unique Löwner (minimum-volume containing) ellipsoid and John (maximum-volume contained) ellipsoid are **homothetic**:
\[
E_{\mathrm L}=\{x:x^TAx\le1\},\qquad
E_{\mathrm J}=\{x:5x^TAx\le1\},\qquad E_{\mathrm L}=\sqrt5 E_{\mathrm J}.
\]
Every one of its 20 vertices contacts \(E_{\mathrm L}\), and precisely its 12 facets contact \(E_{\mathrm J}\). Its polar has precisely the twelve vertices
\[
\{\pm\mathbf1\}\;\cup\;
\{\pm\sigma^k(1,1,1,-1,-1):0\le k<5\},
\]
where \(\sigma\) cyclically rotates five coordinates. In particular, the homothety constant exactly attains the sharp symmetric John containment factor \(\sqrt d\) at \(d=5\) for a non-graphic, non-cographic regular-matroid example with neither cubical nor crosspolytopal combinatorics.

The explicit positive-definite matrix is
\[
A=\frac13\begin{pmatrix}
3&1&-1&-1&1\\
1&3&1&-1&-1\\
-1&1&3&1&-1\\
-1&-1&1&3&1\\
1&-1&-1&1&3
\end{pmatrix}.
\]
It has eigenvalues \(1\) (once) and \(1\pm\sqrt5/3\) (twice each), so the ratio of the longest to shortest principal semiaxes of either ellipsoid is \((3+\sqrt5)/2\). The Löwner volume equals \(6\pi^2/5\), and \(\operatorname{vol}(E_{\mathrm L})/\operatorname{vol}(E_{\mathrm J})=5^{5/2}\).

## Assumptions and scope
All lengths, polarity, ellipsoids and volumes use the fixed standard Euclidean inner product on \(\mathbb R^5\). The columns of \(M\) are the five coordinate unit vectors and the five columns of \(D\); each is included with both signs. The matrix \(M\) is totally unimodular, as can also be checked exhaustively by its 3,002 nonempty square minors; the exceptional matroid identification follows Oxley's explicit \(R_{10}\) representation. The geometric claim is **not** asserted invariant under arbitrary unimodular changes of realization, which need not be Euclidean isometries. Polar means \(P^\circ=\{y:y\cdot x\le1\text{ for all }x\in P\}\).

## Proof
**Step 1 (outer contacts and covariance).** Write \(S=MM^T=I_5+D^2\). Direct exact multiplication gives the displayed \(A=2S^{-1}\) and \(\det A=16/81\). For each of the ten unsigned columns \(m_j\), \(m_j^TAm_j=1\). Set \(u_j=A^{1/2}m_j\), a unit vector. Their second-moment identity is
\[
\sum_{j=1}^{10}u_ju_j^T=A^{1/2}SA^{1/2}=2I_5.
\]
Thus the twenty signed unit vectors \(\pm u_j\), each with coefficient \(1/4\), form an isotropic centered contact measure: their weighted outer-product sum is \(I_5\) and their weighted vector sum is zero. By the equality/contact characterization of the unique minimum-volume enclosing ellipsoid, the unit Euclidean ball is the Löwner ellipsoid of \(A^{1/2}P\). Pulling back proves the stated \(E_{\mathrm L}\). Since each column is on the strictly convex ellipsoid boundary, all 20 signed columns are genuine distinct vertices.

**Step 2 (exact polar vertices).** The polar is
\[
Q=P^\circ=\{y: |y_i|\le1,\; |(Dy)_i|\le1\ (i=1,\ldots,5)\}.
\]
At a vertex, five linearly independent tight inequalities give an integer solution: the active-normal matrix is a square nonsingular submatrix of the totally unimodular \(M^T\) with determinant \(\pm1\). Hence every polar vertex lies in \(\{-1,0,1\}^5\). All \(3^5=243\) candidates can be checked exhaustively, with *integer* evaluations of \(|M^Ty|\le\mathbf1\), and exact rational rank of the columns of \(M\) whose inequalities are tight. The complete support/rank count of feasible candidates (nonzero coordinates, active-normal rank) is
\[
(0,0):1;\quad(1,4):10;\quad(2,4):20;\quad(3,4):20;\quad(4,4):10;\quad(5,5):12.
\]
It follows by the full-rank vertex criterion that precisely the twelve all-sign coordinates are extreme. The explicit list in the finding exhausts them; the included checker reproduces the entire finite enumeration, not a sampled subset.

**Step 3 (dual outer contacts).** For these twelve vectors \(v\in\operatorname{vert}(Q)\), direct exact arithmetic gives the two identities
\[
\frac1{12}\sum_v vv^T=A,\qquad v^TA^{-1}v=5\quad\text{for every }v.
\]
Consequently the vectors \(w_v=5^{-1/2}A^{-1/2}v\) all have norm one and
\[
\sum_v\frac5{12}w_vw_v^T=I_5,\qquad \sum_v\frac5{12}w_v=0.
\]
The same Löwner contact criterion proves that \(\{y:y^TA^{-1}y\le5\}\) is the unique minimum-volume ellipsoid containing \(Q\). Polar duality between centered John and Löwner ellipsoids then yields \(E_{\mathrm J}=\{x:5x^TAx\le1\}\). The polar-vertex classification proves there are twelve facets of \(P\), each tangent because \(\max_{x\in E_{\mathrm J}}v\cdot x=\sqrt{v^TA^{-1}v/5}=1\).

**Step 4 (spectra and volume).** The displayed circulant \(A\) diagonalizes in the five Fourier modes and has eigenvalues \(1,1+\sqrt5/3,1+\sqrt5/3,1-\sqrt5/3,1-\sqrt5/3\). Its determinant is \(16/81\); multiplying the five-ball volume \(8\pi^2/15\) by \(1/\sqrt{\det A}=9/4\) gives \(6\pi^2/5\). Scaling by \(1/\sqrt5\) in five dimensions gives the stated volume ratio and sharp homothety.

## Verification
Run `python verify_r10_ellipsoids.py` with Python 3 and SymPy. It checks all 3,002 square minors of \(M\), the exact matrix \(A\), the ten quadratic outer-contact identities, all 243 polar lattice candidates, the 12 full-rank polar vertices, the exact polar covariance/contact equalities, and the eigenvalues and determinant. The expected final marker is `R10_ELLIPSOIDS_EXACT_PASS`. All arithmetic is symbolic and exact; the enumeration is exhaustive within the proven \(\{-1,0,1\}^5\) reduction, not empirical evidence for an unbounded conjecture.

## Relationship to prior work
Oxley's matroid survey explicitly gives the matrix representation of the exceptional \(R_{10}\). D'Alì, Juhnke-Kubitzke and Koch (arXiv:2307.04933, first posted July 10, 2023) establish the generalized symmetric-edge-polytope construction for regular matroids, its representations, facets, Ehrhart theory and triangulations; their paper does not give this exact pair of Euclidean extremal ellipsoids. Standard John–Löwner contact/equivalence criteria are used as previously known proof tools, not asserted as new. Closely related ellipsoid results for graphic/cographic symmetric edge polytopes concern different matroid classes and do not imply these ten explicit contact vectors and twelve polar vertices. Search and statement comparison support a provisional priority claim, not a proof that no equivalent result exists.

## Limitations
The classification applies specifically to the displayed five-dimensional Euclidean realization of \(R_{10}\) and the natural dual pair; it does not classify all regular matroids or all unimodular representatives. The result is an exact finite theorem, with no asymptotic statement. Mathematically equivalent published results missed by searches or inaccessible full text remain a residual originality risk. Independent expert validation has not been performed.

## References
1. J. Oxley, *What is a Matroid?*, revised survey, June 28, 2007, §6 (explicit totally unimodular representation of \(R_{10}\)): https://people.math.binghamton.edu/zaslav/Oldcourses/580.S13/oxley.what-is-matroid.survey4.2007.pdf .
2. A. D'Alì, M. Juhnke-Kubitzke, and M. Koch, *On a generalization of symmetric edge polytopes to regular matroids*, arXiv:2307.04933 (first public July 10, 2023): https://arxiv.org/abs/2307.04933 .
3. F. John, *Extremum problems with inequalities as subsidiary conditions*, 1948 (classical maximal-volume ellipsoid contact theorem and the symmetric containment factor).
