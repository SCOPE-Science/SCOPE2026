# Cross-polytope skeletal distances recover the point orbit and have a joint gamma-log limit

## Finding

Let \(C_d=\{x\in\mathbb R^d:\sum_{i=1}^d|x_i|\le1\}\) be the regular cross-polytope, where \(d\ge2\). For \(1\le j\le d\), let \(S_{d,j-1}\) denote the union of all closed faces of dimension at most \(j-1\), and define \(R_j(x)=\operatorname{dist}_2(x,S_{d,j-1})\). Write \(a_1\ge\cdots\ge a_d\ge0\) for the sorted absolute coordinates of \(x\), \(s_j=\sum_{i=1}^j a_i\), and \(q=\sum_{i=1}^d a_i^2\). Then, **simultaneously for all** \(x\in C_d\) and \(1\le j\le d\),
\[
R_j(x)^2=q-\sum_{i=1}^j a_i^2+\frac{(1-s_j)^2}{j}.
\]
Moreover,
\[
R_j(x)^2-R_{j+1}(x)^2=\frac{(1-s_j+j a_{j+1})^2}{j(j+1)}\quad(1\le j<d).
\]
The complete profile \((R_1(x),\dots,R_d(x))\) determines \((a_1,\dots,a_d)\) uniquely, and therefore determines \(x\) up to signed coordinate permutation.

If \(X_d\) is uniform by \(d\)-dimensional Lebesgue volume in \(C_d\), let \(Q_{d,j}=R_j(X_d)^2\). Its mean is given exactly by the finite harmonic expression in the proof below. More importantly, for each fixed positive integer \(m\), the first \(m\) skeleton levels have the joint limit, as \(d\to\infty\) through \(d\ge m\),
\[
\left(d\left(\frac1j-Q_{d,j}\right)-2\log d\right)_{j=1}^m
\ \Longrightarrow\ (Z_j)_{j=1}^m,
\qquad Z_j=-2-\frac2j\sum_{i=1}^j\log T_i,
\]
where \(T_i=E_1+\cdots+E_i\) and \(E_1,E_2,\ldots\) are independent exponential random variables of mean one. For each \(j\), the limit has the independent factorization
\[
Z_j\ \stackrel{d}{=}\ -2\log G_j+\frac2j H_{j-1}-2,
\]
where \(G_j\sim\operatorname{Gamma}(j,1)\), \(H_{j-1}\sim\operatorname{Gamma}(j-1,1)\) are independent (\(H_0=0\)). In this display only, \(H_{j-1}\) denotes a gamma variable, not the harmonic number used below. Consequently, for \(t<j/2\),
\[
\mathbb E e^{tZ_j}=e^{-2t}\frac{\Gamma(j-2t)}{\Gamma(j)}\left(1-\frac{2t}{j}\right)^{-(j-1)}.
\]
The joint law across skeleton levels is *not* a product law: all levels are driven by the same exponential arrival process.

## Assumptions and scope

Distances are **ambient Euclidean distances**, not intrinsic paths on the boundary. A \((j-1)\)-skeleton means all faces of dimension at most \(j-1\); in particular \(j=1\) is the vertex set and \(j=d\) is the boundary. The closed unit cross-polytope is fixed; the only random object is its volume-uniform interior point. Statements including faces, zero coordinates, coincident coordinate magnitudes, and the center are valid without genericity assumptions. The asymptotic statements hold for each fixed finite set of skeleton levels, not for \(j\) proportional to \(d\).

## Proof

**1. Metric projection onto all faces.** By reflection symmetry, fix \(x\) with nonnegative coordinates. Every \((j-1)\)-face is the convex hull of \(j\) signed coordinate vectors. For a selected coordinate set \(I\) and signs agreeing with \(x\), minimizing squared Euclidean distance over that face amounts to minimizing \(\sum_{i\in I}(x_i-u_i)^2\) over \(u_i\ge0\), \(\sum_{i\in I}u_i=1\). Since \(\sum_{i\in I}x_i\le1\), the unconstrained affine minimizer \(u_i=x_i+(1-\sum_{I}x_i)/j\) lies in the face. Replacing an opposite sign by the agreeing sign cannot increase the distance. Hence the minimal squared distance to the selected face is
\[
q-\sum_{i\in I}x_i^2+\frac{(1-\sum_{i\in I}x_i)^2}{j}.
\]
Replacing a selected smaller coordinate \(b\) by an unselected larger coordinate \(a\) weakly decreases this expression: with \(s\) the sum of the other selected coordinates, the difference (new minus old) is
\[
-(a-b)\left(a+b+\frac{2(1-s)-(a+b)}{j}\right)\le0,
\]
since \(1-s\ge a+b\). Therefore a minimizing face uses the largest \(j\) coordinates, proving the claimed exact formula. Subtract the formulas at successive levels and complete a square to obtain the displayed gap identity.

**2. Rigidity of the distance signature.** From the final entry obtain the residual \(u=\sqrt d\,R_d(x)=1-\sum_{i=1}^d a_i\). Define \(g_j=\sqrt{j(j+1)(R_j(x)^2-R_{j+1}(x)^2)}\) for \(j<d\). Nonnegativity ensures the positive root equals \(1-s_j+j a_{j+1}\), and hence
\[
g_j=u+(j+1)a_{j+1}+\sum_{r=j+2}^d a_r.
\]
Recover coordinates backward via \(a_d=(g_{d-1}-u)/d\) and \(a_{j+1}=(g_j-u-\sum_{r=j+2}^d a_r)/(j+1)\). Finally \(a_1=1-u-\sum_{r=2}^d a_r\). This explicit inverse works even at degenerate points. Signed permutations preserve every skeleton, so no finer identification is possible.

**3. Exact finite-dimensional mean.** In the positive orthant, the absolute-coordinate vector \((|X_{d,1}|,\ldots,|X_{d,d}|)\) is uniform in the simplex of nonnegative vectors with sum at most one. Thus
\[
(|X_{d,1}|,\ldots,|X_{d,d}|)\stackrel d= (Y_1/T,\ldots,Y_d/T),\quad T=Y_0+\cdots+Y_d,
\]
with independent mean-one exponentials \(Y_0,\ldots,Y_d\). The normalized ratios are independent of \(T\sim\operatorname{Gamma}(d+1,1)\). For ordinary harmonic numbers \(h_n=\sum_{r=1}^n1/r\) and \(h_n^{(2)}=\sum_{r=1}^n1/r^2\), put \(h_0=h_0^{(2)}=0\), and define
\[
b_i=h_d-h_{i-1},\quad c_i=h_d^{(2)}-h_{i-1}^{(2)},\quad
\mu_j=\sum_{i=1}^j b_i,\quad \nu_j=\sum_{r=1}^d\frac{\min(j,r)^2}{r^2}.
\]
The \(i\)-th largest exponential has mean \(b_i\) and variance \(c_i\). The sum of the \(j\) largest has variance \(\nu_j\) by the independent exponential-spacing representation. Because \(\mathbb E T=d+1\) and \(\mathbb E T^2=(d+1)(d+2)\), homogeneous first and second moments of the normalized coordinates are obtained by dividing corresponding exponential moments by these values. In particular \(\mathbb E q=2d/((d+1)(d+2))\). Substitution into the exact projection identity gives
\[
\boxed{\mathbb E Q_{d,j}=\frac1j+\frac{2d}{(d+1)(d+2)}-\frac{2\mu_j}{j(d+1)}
+\frac{(\mu_j^2+\nu_j)/j-\sum_{i=1}^j(b_i^2+c_i)}{(d+1)(d+2)}.}
\]
This also gives the checks \(\mathbb E Q_{d,1}=1+2d/((d+1)(d+2))-2h_d/(d+1)\) and \(\mathbb E Q_{d,d}=2/[d(d+1)(d+2)]\).

**4. Joint limit.** For each fixed \(m\), the upper \(m\) order statistics of \(Y_1,\ldots,Y_d\), minus \(\log d\), converge jointly to the decreasing points \((-\log T_i)_{i=1}^m\) of a Poisson point process with intensity \(e^{-z}dz\). This follows directly from \(d\Pr(Y>\log d+z)=e^{-z}\) and convergence of binomial exceedance counts to independent Poisson increments. The strong law gives \(T/d\to1\), and its fluctuations imply \((d/T-1)\log d\to0\) in probability. Meanwhile \(dq\to2\), by the law of large numbers for \(Y_i^2\). The squared terms in the first \(m\) ordered coordinates, after multiplication by \(d\), converge to zero. The projection formula therefore yields the stated *joint* limit by continuous mapping.

**5. Gamma-log factorization and moments.** Conditional on \(T_j\), the previous arrival times \(T_1,\ldots,T_{j-1}\), divided by \(T_j\), are the ordered values of \(j-1\) independent uniform variables. Their product has the law of the product of the unordered uniforms. Thus \(-\sum_{i=1}^j\log T_i\) has the law \(-j\log G_j+H_{j-1}\), with independent \(G_j\sim\operatorname{Gamma}(j,1)\) and \(H_{j-1}\sim\operatorname{Gamma}(j-1,1)\). This proves the transform. Writing \(\gamma\) for Euler's constant, each limit has
\[
\mathbb E Z_j=2\gamma-2h_{j-1}-\frac2j,\quad
\operatorname{Var}(Z_j)=4\left(\frac{\pi^2}{6}-h_{j-1}^{(2)}+\frac{j-1}{j^2}\right).
\]
Since, for \(i\le k\), the beta-gamma identity makes \(T_i/T_k\) independent of \(T_k\),
\[
\operatorname{Cov}(Z_j,Z_k)=\frac4{jk}\sum_{i=1}^j\sum_{r=1}^k
\left(\frac{\pi^2}{6}-h_{\max(i,r)-1}^{(2)}\right).
\]
These limiting covariances are finite and strictly positive. The exact finite-dimensional mean above supplies a separate, independently checkable statistic; the displayed distributional convergence alone makes no claim of convergence of higher moments. The covariance formula refers to the *joint* limit and does not assume independent skeleton levels.

## Verification

Run `python verify.py` with Python 3 and NumPy. It exhaustively compares the exact face-projection formula against projections onto all signed faces for random points in dimensions 2 through 5, reconstructs the sorted coordinates from the complete distance signature, checks the exact harmonic mean against directly sampled points, and independently tests the gamma-log marginal moments and joint covariances. The program also samples directly from a dimension-1200 cross-polytope to corroborate the limiting centering. It prints `CROSSPOLYTOPE_SKELETON_SIGNATURE_JOINT_GAMMA_LIMIT_OK` when its assertions succeed. Finite tests do not prove the all-dimensional identities or distributional limit.

## Relationship to prior work

The regular cross-polytope and coordinate-extreme methods are classical. The known classification of face-rank orbits under invertible contractions concerns a different equivalence relation and does not reconstruct a point from its Euclidean distances to face skeletons. Gravin, Lasserre, Pasechnik and Robins [1] reconstruct an unknown **polytope** from moment data; this is a different inverse problem from reconstructing an unknown **point orbit** within a fixed polytope from all skeletal distances. Ambrus [2] investigates intrinsic volumes and Gaussian widths of orthogonal cross-polytopes rather than point-to-face distances. Mijatović and Vysotsky [3] prove asymptotics for the maximum of sums of *consecutive* uniform spacings. Their exponential representation is relevant background, but their maximal-consecutive-spacing theorem neither states the geometric projection identity nor the gamma-log limit for sums of the largest individual spacings. Classical order-statistics identities are used, not claimed as new.

## Limitations

The inverse determines a signed-permutation orbit, not the signs or ordering of coordinates. Fixed-level asymptotics do not cover skeleton dimensions growing with ambient dimension. The exact random law is proved for volume-uniform points; other sampling schemes are not addressed. The novelty comparison is provisional and does not rule out all older literature on polytope skeletal clearances, uniform spacings or related transforms. No independent mathematical or historical validation is claimed.

## References

[1] N. Gravin, J. Lasserre, D. Pasechnik and S. Robins, *The inverse moment problem for convex polytopes*, arXiv:1106.5723, first submitted 2011-06-28. https://arxiv.org/abs/1106.5723

[2] G. Ambrus, *Extremal cross-polytopes and Gaussian vectors*, arXiv:1208.5923, first submitted 2012-08-29. https://arxiv.org/html/1208.5923v2

[3] A. Mijatović and V. Vysotsky, *On the weak limit law of the maximal uniform k-spacing*, arXiv:1508.00944, first submitted 2015-08-05. https://arxiv.org/abs/1508.00944
