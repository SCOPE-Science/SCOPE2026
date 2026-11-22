# Sharp two-input Hilbert-to-edge stability of maximal averaging on every finite star

## Finding
Let \(K_{1,m}\) be the unweighted star with one hub \(0\) and \(m\ge1\) leaves, and let \(M\) be its centered Hardy–Littlewood graph-ball maximal operator, with absolute values taken before averaging. For all complex-valued vertex functions \(f,g\), define
\[
\|f-g\|_{2,V}^2=\sum_{i=0}^{m}|f(i)-g(i)|^2,
\qquad
V_2(h)^2=\sum_{i=1}^{m}|h(i)-h(0)|^2.
\]
The exact least constant in the **two-input** inequality \(V_2(Mf-Mg)\le L_m\|f-g\|_{2,V}\) is
\[
\boxed{\displaystyle
L_m^2=\begin{cases}
\frac12,&m=1,\\[3pt]
\frac{m(m+2)+\sqrt{m^2(m+2)^2-4(m+1)}}{2(m+1)},&m\ge2.
\end{cases}}
\]
For each \(m\), the constant is attained by a pair of **strictly positive real functions**, hence the complex-data bound is sharp. For \(m\ge2\), the squared constant is the larger root of
\[
(m+1)z^2-m(m+2)z+1=0.
\]
In particular, \(L_m/\sqrt m\to1\), so the output quadratic edge-gradient perturbation can grow as the square root of the star degree, even though sharp one-input edge-variation inequalities are contractive. The norm concerns the edge gradient of a **difference of maximal outputs** and is not a one-input variation coefficient.

## Assumptions and scope
The graph is finite, simple, unweighted, and equipped with counting measure and graph distance. Each undirected hub–leaf edge is counted exactly once. Distinct hub balls are the singleton and the full graph. A leaf has singleton, hub–leaf pair, and full-graph balls. Functions may be complex because averages act on their pointwise moduli; \(V_2(Mf-Mg)\) is real-valued. The result includes all integers \(m\ge1\), with a separate two-vertex boundary case. No claim is made for weighted or uncentered maximal functions, other graph families, fractional exponents, or other input-output norms.

## Proof
**1. Reduction to nonnegative real inputs.** By definition \(Mf=M|f|\), and pointwise \(\big||f(i)|-|g(i)|\big|\le |f(i)-g(i)|\). Thus a sharp Lipschitz estimate for nonnegative inputs with the vertex Euclidean norm implies the same estimate for complex inputs. Sharpness may be proved using positive real inputs.

Write \(x_0\) for the hub value, \(x_i\) for leaf values, and \(a=(x_0+\sum_{j=1}^m x_j)/(m+1)\). For nonnegative real data,
\[
(Mx)_0=\max\{x_0,a\},\qquad
(Mx)_i=\max\left\{x_i,\frac{x_0+x_i}{2},a\right\}.
\]
The edge-gradient map \(x\mapsto ((Mx)_i-(Mx)_0)_{i=1}^m\) is continuous and piecewise linear. Its global Euclidean Lipschitz constant is bounded by the supremum of the Euclidean operator norms of the linear maps on its open cells: partition a line segment into finitely many affine pieces, apply the triangle inequality, and then use continuity for degenerate segments.

**2. The hub chooses the global average.** Suppose \(a>x_0\). Since \(a>x_0\), a leaf choosing the midpoint average cannot do so strictly: if \(x_i\ge x_0\), its singleton is no smaller than the midpoint; if \(x_i<x_0\), the global mean is larger. Thus each leaf chooses either its own value or \(a\). Put \(\mathbf1=(1,\ldots,1)\in\mathbb R^{m+1}\), and write \(P=I-\mathbf1\mathbf1^{\mathsf T}/(m+1)\). Each edge output row is either the corresponding leaf row of \(P\) or zero; hence this branch's edge-gradient matrix is a row restriction of the orthogonal projection \(P\). Its Euclidean operator norm is at most \(1\).

**3. The hub chooses itself.** Suppose \(x_0>a\), and let \(e_i\) denote the standard basis of \(\mathbb R^{m+1}\). Define
\[
I_i=e_i-e_0,\quad
H=\frac{\sum_{j=1}^m e_j-me_0}{m+1}
=\frac1{m+1}\sum_{j=1}^m I_j.
\]
The edge-gradient matrix has row \(I_i\), \(I_i/2\), or \(H\), according as leaf \(i\) chooses its singleton, its hub–leaf average, or the global average. At most \(m-1\) leaves can strictly select singleton averages: singleton dominance over the midpoint implies \(x_i>x_0\), and if this held for all leaves it would contradict \(x_0>a\).

The exact inner products are
\[
\langle I_i,I_j\rangle=1+\mathbf1_{\{i=j\}},\qquad
\langle I_i,H\rangle=1,\qquad
\langle H,H\rangle=\frac m{m+1}.
\]
All row Gram matrices are entrywise nonnegative. Replacing any half-singleton row \(I_i/2\) by \(H\) **increases every Gram entry**, since its old diagonal is \(1/2\), the new diagonal is \(m/(m+1)>1/2\) for \(m\ge2\); its cross products increase from \(1/2\) to \(1\) against distinct singleton rows, from \(1/4\) to \(1/2\) against distinct half-singleton rows, and from \(1/2\) to \(m/(m+1)\) against global rows. Next replace global rows by their corresponding singleton rows until precisely \(m-1\) singleton rows and one global row remain. Each such replacement also increases every Gram entry: cross products against existing singleton rows remain \(1\), against global rows increase from \(m/(m+1)\) to \(1\), and the diagonal rises from \(m/(m+1)\) to \(2\).

For nonnegative symmetric matrices, the spectral radius is monotone under entrywise enlargement, and equals the largest eigenvalue. Therefore every hub-singleton branch has squared Euclidean operator norm at most that of the matrix with \(m-1\) rows \(I_i\) and one row \(H\). Its row Gram matrix is
\[
G_m=\begin{pmatrix}
J_{m-1}+I_{m-1}&\mathbf1_{m-1}\\
\mathbf1_{m-1}^{\mathsf T}&m/(m+1)
\end{pmatrix}.
\]
On the \(m-2\)-dimensional leaf-contrast subspace, \(G_m\) acts as the identity (the subspace is absent at \(m=2\)). On the two-dimensional symmetric subspace its matrix is
\[
\begin{pmatrix}
m&\sqrt{m-1}\\
\sqrt{m-1}&m/(m+1)
\end{pmatrix},
\]
whose trace is \(m(m+2)/(m+1)\) and determinant is \(1/(m+1)\). Its larger eigenvalue is the displayed \(L_m^2>1\). This dominates the hub-average branches and all other hub-singleton branches.

**4. Attainment with strict branch inequalities.** Fix \(m\ge2\). Set the hub value \(x_0=2\), set the first \(m-1\) leaves to \(2+1/(4m)\), and set the last leaf to \(1\). The hub strictly selects its singleton: \(x_0>a\) because \((m-1)/(4m)<1\). Each of the first \(m-1\) leaves strictly selects its singleton, while the final leaf strictly selects the global average, since \(a>3/2=(x_0+1)/2\). This is precisely the maximizing Gram branch, on an open set of strictly positive inputs.

Let \(\lambda=L_m^2\), let \(b=\lambda-m>0\), and choose the nonzero input direction
\[
v=\sum_{i=1}^{m-1}I_i+bH.
\]
The vector with \(m-1\) unit entries and final entry \(b\) is a positive eigenvector of \(G_m\) for \(\lambda\), so \(v\) is a right singular vector of the branch's edge-gradient matrix. For every sufficiently small positive \(t\), both \(x\) and \(x+tv\) remain in the same strict branch cell and are strictly positive. Consequently,
\[
\frac{V_2(M(x+tv)-Mx)^2}{\|tv\|_{2,V}^2}=\lambda.
\]
This proves exact sharpness without a limiting-only argument.

**5. Two-vertex boundary.** If \(m=1\), the sole output edge difference for nonnegative inputs equals half the original edge difference, independently of ordering. Its two-input Euclidean Lipschitz constant is \(\|e_1-e_0\|_2/2=1/\sqrt2\), attained by positive real perturbations. The modulus reduction of Step 1 extends it to complex inputs.

## Verification
The standalone Python 3 program `verify_star_l2.py` uses only the standard library. Run `python3 verify_star_l2.py`. It checks \(3{,}534\) exact rational inner-product identities and root conditions, \(280{,}270\) exact rational Gram-entry domination comparisons across all formal hub-singleton masks for \(2\le m\le7\), \(22\) strict-positive norming witnesses, and \(6{,}000\) direct random real, signed, and complex input pairs. It separately computes the norming singular direction from the proposed formula. All checks pass in the packaged version. The proof for every \(m\) and every input pair is Steps 1–5; finite checks do not establish those infinite quantifiers.

## Relationship to prior work
Liu, Lian and Wang (arXiv:2611.15377v1, first public 2026-11-11) give sharp finite-graph maximal-function *one-input* variation and \(L^p\) bounds, including star graphs. Their \(\operatorname{Var}_p(Mf)/\operatorname{Var}_p(f)\) and \(\|Mf\|_p/\|f\|_p\) are different from a two-input vertex-\(\ell^2\)-to-edge-gradient modulus. González-Riquelme and Madrid (arXiv:2011.02630v1) calculate the sharp star one-input quadratic-variation coefficient, again with variation in the input denominator. A related publicly available exact theorem for **two-input total-variation-to-total-variation** stability on stars yields \(2m/(m+1)\) on nonnegative inputs. It does not imply the present sharp Hilbert-domain constant, because converting the input total-variation seminorm to vertex \(\ell^2\) incurs a dimension-dependent nonsharp factor. A related fractional-star perturbation estimate for strictly positive fractional exponents establishes asymptotics but no exact finite-size formula, and does not cover the endpoint \(\alpha=0\). The present result identifies the exact spectral mechanism at that endpoint for every star size. These mathematical implication comparisons do not certify global historical priority.

## Limitations
The theorem treats only centered ball averaging on unweighted stars, with input vertex \(\ell^2\) and output quadratic edge variation. The value of \(L_m\) is an exact *global two-input* Lipschitz constant, not a general Sobolev contraction coefficient. No full classification of equality pairs is asserted, although positive exact witnesses are given. Weighted stars, other graphs, fractional \(\alpha>0\), and other \(p\)-norms remain outside the statement. The novelty comparison is best-knowledge relative to specified inspected results; an earlier equivalent Hilbert perturbation theorem could exist.

## References
1. F. Liu, Y. Lian and Y. Wang, *Sharp \(L^p\) and variation inequalities for maximal operators on finite connected graphs*, arXiv:2611.15377v1, first public 2026-11-11. https://arxiv.org/abs/2611.15377
2. C. González-Riquelme and J. Madrid, *Sharp inequalities for maximal operators on finite graphs, II*, arXiv:2011.02630v1, first public 2020-11-05. https://arxiv.org/abs/2011.02630
3. C. González-Riquelme and J. Madrid, *Sharp inequalities for maximal operators on finite graphs*, arXiv:2005.03146v1, first public 2020-05-06. https://arxiv.org/abs/2005.03146
4. C. González-Riquelme, V. Kovač and J. Madrid, *Sharp variational inequalities for the Hardy–Littlewood maximal operator on finite undirected graphs*, arXiv:2603.12462v1, first public 2026-03-12. https://arxiv.org/abs/2603.12462
