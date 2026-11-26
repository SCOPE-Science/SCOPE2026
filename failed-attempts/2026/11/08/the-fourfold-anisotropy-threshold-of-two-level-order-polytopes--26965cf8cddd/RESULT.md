# The fourfold anisotropy threshold of two-level order polytopes

## Finding

For integers \(2\le p\le q\), let
\[
K_{p,q}=\{(x,y)\in[0,1]^p\times[0,1]^q:x_i\le y_j\text{ for all }i,j\}
\]
be the standard full-dimensional Euclidean order polytope of the ordinal sum of two antichains, and let \(C_{p,q}\) be the covariance of its normalized uniform-volume measure. Put \(n=p+q\), and define
\[
\begin{aligned}
\alpha_p&=\frac{(p+1)(p+2)}{12(n+1)(n+2)},
&\alpha_q&=\frac{(q+1)(q+2)}{12(n+1)(n+2)},\\
v_p&=\frac{(p+1)(p^2+4pq+3p+2q+2)}{12p(n+1)^2(n+2)},
&v_q&=\frac{(q+1)(q^2+4pq+3q+2p+2)}{12q(n+1)^2(n+2)},\\
c&=\frac{(p+1)(q+1)}{4(n+1)^2(n+2)}.
\end{aligned}
\]
Then the **entire covariance matrix**, not merely its spectrum, is
\[
\boxed{
C_{p,q}=\begin{pmatrix}
\alpha_p(I_p-J_p/p)+v_pJ_p &cJ_{p,q}\\
cJ_{q,p}&\alpha_q(I_q-J_q/q)+v_qJ_q
\end{pmatrix}.}
\]
Here \(J\) denotes an all-ones matrix of the indicated size. The eigenvalues are \(\alpha_p\) with multiplicity \(p-1\), \(\alpha_q\) with multiplicity \(q-1\), and the two simple eigenvalues \(\beta_-<\beta_+\) of
\[
B_{p,q}=\begin{pmatrix}pv_p&\sqrt{pq}\,c\\\sqrt{pq}\,c&qv_q\end{pmatrix},
\qquad
\beta_\pm=\frac{\operatorname{tr}B_{p,q}\pm
\sqrt{(pv_p-qv_q)^2+4pq c^2}}2.
\]
The largest eigenvalue is always \(\beta_+\). The smallest positive eigenvalue changes its geometrical eigenspace at a **two-element size imbalance**:
\[
\boxed{
\lambda_{\min}(C_{p,q})=\begin{cases}
\beta_-&q=p\text{ or }q=p+1,\\
\alpha_p&q\ge p+2.
\end{cases}}
\]
Consequently, the standard-Euclidean covariance condition number \(\kappa=\lambda_{\max}/\lambda_{\min}\) has the exact, unattained **fourfold boundary**
\[
\boxed{
\kappa(C_{p,q})<4\quad\Longleftrightarrow\quad q-p\le1,
\qquad
\kappa(C_{p,q})>4\quad\Longleftrightarrow\quad q-p\ge2.}
\]
There is no equality case. If \(p=q=r\ge2\), the two block-constant eigenvalues simplify to \(\beta_+=1/12\), \(\beta_-=(r^2+r+1)/(12(2r+1)^2)\), giving
\[
\boxed{\kappa(C_{r,r})=4-\frac3{r^2+r+1}.}
\]
If \(p\) is fixed and \(q\to\infty\), then \(\kappa(C_{p,q})\sim q^2/((p+1)(p+2))\). The same statements apply, up to orthogonal conjugacy, to the uniform-volume covariance of the complete-bipartite chain polytope by reflecting the upper coordinates.

## Assumptions and scope

Both antichains are nontrivial: \(p,q\in\mathbb Z\), \(2\le p\le q\). Every coordinate uses its standard Euclidean unit, and covariance means \(\mathbb E[(X-\mathbb EX)(X-\mathbb EX)^\mathsf T]\) for \(X\) sampled uniformly by \(n\)-dimensional Lebesgue measure on \(K_{p,q}\), **not** by sampling vertices. This is a full-dimensional polytope, so all covariance eigenvalues are strictly positive. Reversing both layers and complementing all coordinates is an isometry, so the case \(p>q\) is obtained by interchanging the parameters. Standard order-polytope triangulation gives the known volume \(p!q!/n!\); that volume is not presented as new.

## Proof

**1. Uniform linear-extension simplices and moment normalization.** The \(p!q!\) linear extensions of the two-level poset are precisely the permutations of the lower labels followed by permutations of the upper labels. Their order simplices all have Euclidean volume \(1/n!\) and disjoint interiors. Thus choose a pair of independent uniform permutations of these two blocks and independently draw the order statistics \(U_{(1)}<\cdots<U_{(n)}\) of \(n\) iid \(\operatorname{Uniform}(0,1)\) observations. Assign the first \(p\) ranks to the lower block and the remaining \(q\) ranks to the upper block. This is exactly uniform volume on \(K_{p,q}\).

The basic exact moments are
\[
\mathbb E U_{(r)}=\frac r{n+1},\qquad
\mathbb E[U_{(r)}U_{(s)}]
=\frac{\min(r,s)(\max(r,s)+1)}{(n+1)(n+2)}.
\]
They follow by representing the \(n+1\) spacings between successive order statistics and the endpoints as a \(\operatorname{Dirichlet}(1,\ldots,1)\) vector. In particular, the coordinate means are \((p+1)/(2(n+1))\) in the lower block and \((2p+q+1)/(2(n+1))\) in the upper block.

**2. Internal contrasts and block means.** If \(i\ne j\) are in the lower block, their assigned ranks are two distinct uniformly selected elements of \(\{1,\ldots,p\}\). With \(d\) their absolute rank difference, the beta-spacing moments give
\[
\mathbb E[(X_i-X_j)^2\mid d]=\frac{d(d+1)}{(n+1)(n+2)},
\qquad
\mathbb E[d(d+1)]=\frac{(p+1)(p+2)}6.
\]
Since the two coordinates have equal means, their contrast covariance eigenvalue is half their mean squared difference, namely \(\alpha_p\). The same argument gives \(\alpha_q\) in the upper block.

Let \(\bar X=p^{-1}\sum_iX_i\) and \(\bar Y=q^{-1}\sum_jY_j\). The permutation choices drop out of these averages: they are respectively the average of the first \(p\) and last \(q\) order statistics. Using the displayed order-statistic moments and summing gives the exact identities
\[
\operatorname{Var}(\bar X)=v_p,\quad
\operatorname{Var}(\bar Y)=v_q,\quad
\operatorname{Cov}(\bar X,\bar Y)=c.
\]
An alternative direct calculation weights the Dirichlet spacings by their fractions of ranks exceeding each gap, then uses \(\operatorname{Cov}(S_i,S_j)=((n+1)\mathbf1_{i=j}-1)/((n+1)^2(n+2))\).

Permutation invariance in each block forces the covariance to be scalar on its blockwise zero-sum subspace, and constant on each block of entries when restricted to the block means. The three moment identities therefore establish the asserted full matrix. In the orthonormal basis \(\mathbf1_p/\sqrt p,\mathbf1_q/\sqrt q\), the remaining two-dimensional restriction is exactly \(B_{p,q}\). Its determinant simplifies to
\[
\det B_{p,q}
=\frac{(p+1)(q+1)(2pq+p+q+2)}{72(n+1)^2(n+2)^2}>0.
\]
Thus all listed eigenvalues are positive and have the claimed multiplicities.

**3. Exact ordering and switching of the smallest eigenspace.** Since \(c>0\), the larger eigenvalue of \(B_{p,q}\) strictly exceeds each diagonal element. Direct subtraction gives
\[
pv_p-\alpha_p=\frac{pq(p+1)}{4(n+1)^2(n+2)}>0,
\qquad
qv_q-\alpha_q=\frac{pq(q+1)}{4(n+1)^2(n+2)}>0.
\]
Hence \(\beta_+\) is the largest eigenvalue of the full covariance. Since \(p\le q\), also \(\alpha_p\le\alpha_q\). The exact determinant comparisons are
\[
\begin{aligned}
\det(B_{p,q}-\alpha_pI_2)
&=\frac{pq(p+1)(q^2-p^2-3p-3)}{48(n+1)^3(n+2)^2},\\
\det(B_{p,q}-\alpha_qI_2)
&=\frac{pq(q+1)(p^2-q^2-3q-3)}{48(n+1)^3(n+2)^2}<0.
\end{aligned}
\]
Since \(\beta_+>\alpha_q\), the second determinant proves \(\beta_-<\alpha_q\), while the first determines the sign of \(\beta_--\alpha_p\). Its remaining factor is negative at \(q=p\) and \(q=p+1\), and positive for every integer \(q\ge p+2\): at these last two adjacent cases it equals \(-p-2\) and \(p+1\), respectively, and increases strictly with \(q\). Thus the minimum eigenvalue switches at precisely the asserted imbalance. There is no integer equality case.

**4. Exact fourfold condition-number threshold.** The sum of all coordinates under the uniform-volume law has exactly the distribution of the sum of \(n\) independent unit uniform variables: conditioning on which rank permutation respects the poset never changes the unordered order statistics. Hence the unit all-ones direction always has variance \(1/12\), giving \(\beta_+\ge1/12\). When \(p=q=r\), the block symmetry makes that direction an eigenvector. Substitution in \(B_{r,r}\) gives \(\beta_+=1/12\), \(\beta_-=(r^2+r+1)/(12(2r+1)^2)\); the contrast eigenvalue is larger than \(\beta_-\). Therefore \(\kappa=4-3/(r^2+r+1)<4\).

For \(q=p+1\), the minimum is \(\beta_-\). For two positive eigenvalues \(0<\beta_-\le\beta_+\), the inequality \(\beta_+/\beta_-<4\) is equivalent to \(25\det B>4(\operatorname{tr}B)^2\). Substituting \(q=p+1\) gives the **strict exact identity**
\[
25\det B_{p,p+1}-4(\operatorname{tr}B_{p,p+1})^2
=\frac{5p^2+50p+44}{576(p+1)^2(2p+3)^2}>0.
\]
Finally, for every \(q\ge p+2\), the minimum is \(\alpha_p\), and
\[
\alpha_p\le\frac{(p+1)(p+2)}{12(2p+3)(2p+4)}<\frac1{48}.
\]
Together with \(\beta_+\ge1/12\), this implies \(\kappa>4\), strictly. The displayed balanced formula and fixed-\(p\) asymptotic follow immediately from the matrix entries; in the latter regime \(\beta_+\to1/12\) and \(\alpha_p\sim(p+1)(p+2)/(12q^2)\).

**5. Chain-polytope formulation.** The complete-bipartite chain polytope is \(\{(u,v):u_i,v_j\ge0,\ u_i+v_j\le1\}\), and the affine map \((x,y)\mapsto(x,\mathbf1_q-y)\) is an orthogonal isometry from \(K_{p,q}\) onto it. It conjugates the covariance matrix by a sign change on the upper block and preserves all eigenvalues, multiplicities, and condition numbers.

## Verification

Run `python3 artifacts/verify.py` from the containing directory. The standalone Python-standard-library checker exactly enumerates all linear-extension rank assignments for 17 small parameter pairs, compares all 869 rational covariance entries with the stated formulas, then checks exact determinant identities, the all-ones variance, balanced and near-balanced threshold identities, and numerical eigenvalue orderings for 6,084 further parameter pairs. The exact enumeration is independent of the block-moment simplification. Finite computations corroborate the proof but do not establish its all-parameter claims.

## Relationship to prior work

Stanley's order-polytope triangulation supplies the known equal-volume decomposition and known total volume; this result evaluates a different invariant, the full uniform-volume covariance tensor, and proves an exact spectral and anisotropy transition. Ahmad, Fourier and Joswig (arXiv:2309.01626) analyze face normal forms and \(f\)-vector monotonicity for maximal ranked posets, including this two-level family. Freij-Hollanti and Lundström (arXiv:2312.13890) analyze ordinal sums through face vectors; Mori (arXiv:2404.00263) counts triangular faces. These inspected primary results do not calculate or dominate the covariance spectrum or the fourfold threshold. Previously available John and Löwner ellipsoid formulas for two-level order or chain polytopes solve optimization problems over inscribed or containing ellipsoids, not the inertia ellipsoid of the volume measure; those shape matrices are not interchangeable with this covariance. The order and chain realization isometry is known and is not claimed as new.

## Limitations

The theorem concerns the Euclidean uniform-volume covariance of a complete height-two poset, not the vertex-uniform measure, nonstandard coordinate metrics, incomplete interlevel relations, or maximal ranked posets with three or more levels. It does not establish whether analogous thresholds hold in those settings. The arithmetic is a full proof of the stated infinite two-parameter formulas, but the literature comparison cannot establish universal historical priority: a more general published covariance identity for all order polytopes might imply the formulas after a nontrivial specialization and spectral comparison. No independent mathematical audit is claimed.

## References

1. Ibrahim Ahmad, Ghislain Fourier, Michael Joswig, *Order and chain polytopes of maximal ranked posets*, arXiv:2309.01626v1, first submitted 2023-09-04; full text https://arxiv.org/html/2309.01626v2 .
2. Ragnar Freij-Hollanti, Teemu Lundström, *\(f\)-vector inequalities for order and chain polytopes*, arXiv:2312.13890, 2023-12-21; https://arxiv.org/abs/2312.13890 .
3. Aki Mori, *Triangular faces of the order and chain polytope of a maximal ranked poset*, arXiv:2404.00263v1, first submitted 2024-03-30; https://arxiv.org/html/2404.00263v3 .
4. Richard P. Stanley, *Two poset polytopes*, Discrete & Computational Geometry **1** (1986), 9–23. The triangulation is background, not a new contribution.
