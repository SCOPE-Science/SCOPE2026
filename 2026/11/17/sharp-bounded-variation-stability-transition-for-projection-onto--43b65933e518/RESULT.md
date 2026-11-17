# Sharp bounded-variation stability transition for projection onto a discrete total-variation ball

## Finding
Let \(n\ge2\) be an integer and \(R>0\). For \(x\in\mathbb R^n\), put
\[
V_n(x)=\sum_{i=1}^{n-1}|x_{i+1}-x_i|,
\quad
K_{n,R}=\{z\in\mathbb R^n:V_n(z)\le R\},
\quad
P_{n,R}(x)=\operatorname*{argmin}_{z\in K_{n,R}}\frac12\|z-x\|_2^2.
\]
The minimizer exists uniquely. Its exact two-input variation Lipschitz coefficient is
\[
\sup_{V_n(x-y)>0}\frac{V_n(P_{n,R}x-P_{n,R}y)}{V_n(x-y)}
=\begin{cases}1,&n=2,3,\\2,&n\ge4.\end{cases}
\]
The constants are attained by distinct finite pairs, and do not depend on the positive constraint radius \(R\). Thus four sites are exactly the first size at which Euclidean projection onto a path-variation ball can amplify the variation of an input perturbation.

## Assumptions and scope
All vectors are real; fidelity is ordinary unweighted Euclidean squared distance; the seminorm is *nonperiodic path* total variation with unit edge weights; and \(R>0\) is fixed for both inputs. The inequality concerns variation of the **difference between two projected signals**, not variation of a single projected signal. Translation by a constant is respected by \(P_{n,R}\), so the variation quotient is well-defined. At \(R=0\), excluded here, the projector is the constant-mean map and the variation coefficient is zero.

## Proof
Write \((Dz)_i=z_{i+1}-z_i\). The set \(K_{n,R}\) is a polyhedron: it is the inverse image of an \(\ell_1\)-ball under \(D\), times the free constant direction. Its Euclidean nearest-point projector is continuous and piecewise affine. Consequently, to bound its global variation Lipschitz coefficient it suffices to bound the variation norm of its linear part on each affine region. These linear parts are the orthogonal projectors onto directions of faces of \(K_{n,R}\), including the identity on the interior.

Consider a proper face with the nonzero coordinate set \(S\subseteq\{1,\dots,n-1\}\) of \(Dz\) and prescribed signs \(s_i\in\{-1,1\}\) on \(S\), setting \(s_i=0\) elsewhere. The remaining zero edges partition the path vertices into consecutive blocks \(B_1,\dots,B_q\). Let \(A\) be ordinary averaging within each block; it is the Euclidean orthogonal projector onto vectors constant on those blocks. Put \(g=AD^{\mathsf T}s\). The tangent space of the face consists of block-constant \(z\) satisfying \(\langle g,z\rangle=0\). Because \(S\ne\varnothing\), we have \(g\ne0\), and the orthogonal projector onto that tangent space is
\[
H=A-\frac{gg^{\mathsf T}}{\|g\|_2^2}.
\]

First, \(V_n(Ah)\le V_n(h)\) for every \(h\). To see this, expand a vector modulo its constant part into consecutive step indicators, each with coefficient \((Dh)_i\). Block averaging preserves the order of a nondecreasing step and maps its values into \([0,1]\), so its output variation is at most one. The triangle inequality gives the result for arbitrary step coefficients.

Second, index the \(q\) blocks from left to right, let their lengths be \(m_j\), and let \(s_j\) now denote the prescribed sign at the boundary between blocks \(j\) and \(j+1\), with \(s_0=s_q=0\). On block \(j\), the vector \(g\) equals \((s_{j-1}-s_j)/m_j\). Hence at the boundary \(j\),
\[
(Dg)_j=s_j\bigl(m_j^{-1}+m_{j+1}^{-1}\bigr)
-s_{j-1}m_j^{-1}-s_{j+1}m_{j+1}^{-1}.
\]
Every \(s_j(Dg)_j\) is nonnegative, since \(s_j^2=1\) and its two neighboring signs have absolute value at most one. The other within-block differences are zero. Therefore the **exact identity**
\[
V_n(g)=\sum_{j=1}^{q-1}s_j(Dg)_j
=\langle D^{\mathsf T}s,g\rangle
=\langle g,g\rangle=\|g\|_2^2
\]
holds. For every \(h\), because \(A\) is self-adjoint and idempotent,
\[
\begin{aligned}
V_n(Hh)&\le V_n(Ah)+\frac{|\langle g,h\rangle|}{\|g\|_2^2}V_n(g)\\
&=V_n(Ah)+|\langle s,DAh\rangle|\\
&\le 2V_n(Ah)\le2V_n(h).
\end{aligned}
\]
The same bound holds for the interior linear part \(I\). Integration along any input segment across its finitely many affine pieces (or an approximation followed by continuity) proves the uniform global factor two.

For \(n=2\), the only nontrivial affine pieces are identity and projection onto the constant vectors, whose induced one-edge variation norms are one and zero. For \(n=3\), a proper face with only one nonzero adjacent difference has constant-vector tangent and thus variation derivative zero. For a face with both differences nonzero, the induced matrices in the difference coordinates, up to overall sign, are
\[
\frac12\begin{pmatrix}1&-1\\-1&1\end{pmatrix},
\qquad
\frac12\begin{pmatrix}1&1\\1&1\end{pmatrix}.
\]
Both have induced \(\ell_1\)-norm one. Together with the interior identity, these prove the global bound one for two and three sites. A sufficiently small perturbation of a strictly feasible point is unchanged by the projector, so one is attained.

For \(n\ge4\), choose \(R=2(n-2)\), \(x_i=2(i-1)\), a step location \(2\le k\le n-2\), and \(0<\varepsilon<1\). Define \(y_i=x_i+\varepsilon\mathbf1_{\{i>k\}}\). Projection of \(x\) onto the containing halfspace \(\{z:z_n-z_1\le R\}\) shifts its first coordinate up by one and last coordinate down by one; the corresponding halfspace projection of \(y\) shifts its first coordinate up by \(1+\varepsilon/2\) and last coordinate down by \(1+\varepsilon/2\). Both projected vectors have strictly increasing coordinates and total variation exactly \(R\); hence they also are the projections onto the smaller set \(K_{n,R}\). Their difference has adjacent jumps \(-\varepsilon/2\), \(\varepsilon\), and \(-\varepsilon/2\) at edges \(1,k,n-1\), and no others. Thus
\[
V_n(y-x)=\varepsilon,
\qquad V_n(P_{n,R}y-P_{n,R}x)=2\varepsilon.
\]
Scaling the two inputs and \(R\) by the same positive factor carries this exact witness to any other positive radius. This proves sharpness for every \(n\ge4\) and completes the theorem.

## Verification
Run `python check_tv_ball.py`. The standalone checker uses exact rational arithmetic, forms every face-tangent derivative for \(2\le n\le8\), checks its induced variation norm, and independently verifies explicit feasible halfspace-projection witnesses at \(4\le n\le39\). Successful output terminates in `ALL_PATH_TV_BALL_PROJECTION_CHECKS_PASS`. The analytical face argument, not finite enumeration, covers all dimensions and input pairs.

## Relationship to prior work
Combettes and Pesquet (2004) develop image restoration under an upper bound on total variation, emphasizing general convex programming, subgradient projections, and computational recovery. Their exact projection onto the variation constraint is explicitly distinguished from the cheaper subgradient projection. The present theorem instead determines the sharp **input-to-output variation perturbation modulus of the Euclidean nearest-point projection** in the discrete one-dimensional path model. Yang and Barber (2017) characterize contractive seminorms for isotonic regression; that result concerns projection onto a monotonicity cone, not onto a total-variation sublevel set. The known Euclidean nonexpansivity of convex projections controls \(\|Px-Py\|_2\), not the adjacent-variation quotient. Related weighted graph-variation results for *penalized* proximal maps concern a different data-dependent operator; fixing the penalty is not equivalent to fixing a variation radius across two inputs.

## Limitations
The theorem is for one-dimensional unweighted paths and a fixed positive variation budget. It does not assert the same constant for cycles, trees, arbitrary graphs, unequal Euclidean observation masses, weighted variation edges, a radius chosen separately for each input, or penalty-form TV denoisers. Historical priority is provisional: keyword-based searches and accessible primary-text comparisons are not an exhaustive search of all older projection-stability literature. No independent audit has been performed.

## References
1. P. L. Combettes and J.-C. Pesquet, “Image Restoration Subject to a Total Variation Constraint,” *IEEE Transactions on Image Processing* 13(9), 1213–1222 (2004), DOI: https://doi.org/10.1109/TIP.2004.832922 . Open author manuscript: https://pcombet.math.ncsu.edu/ip4.pdf . Online first-publication record: https://openalex.org/W2100108897 (2004-08-16).
2. F. Yang and R. F. Barber, “Contraction and uniform convergence of isotonic regression,” arXiv:1706.01852 (first public 2017-06-06), https://arxiv.org/html/1706.01852v3 .
3. J. Darbon and M. Sigelle, “Image Restoration with Discrete Constrained Total Variation Part I: Fast and Exact Optimization,” *Journal of Mathematical Imaging and Vision* 26, 261–276 (2006), DOI: https://doi.org/10.1007/s10851-006-8803-0 . The paper treats TV minimization with a fidelity constraint, not the nearest-point map onto a TV ball.
