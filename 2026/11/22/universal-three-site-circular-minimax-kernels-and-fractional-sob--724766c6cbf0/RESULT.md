# Universal three-site circular minimax kernels and fractional Sobolev trace designs

## Finding

**General kernel principle.** Let \(K:\mathbb T\to\mathbb R\) be a continuous, real, positive-definite, even one-periodic function, strictly decreasing on \([0,1/2]\), with \(K(1/6)+K(1/3)<0\). Put \(k=K(0)\). There is a unique \(d\in(0,1/6)\) with \(K(d)+K(2d)=0\). Write \(p=K(d)=-K(2d)>0\). For every three-point subset \(X=\{x_1,x_2,x_3\}\subset\mathbb T\), let \(G_K(X)=(K(x_i-x_j))_{i,j=1}^3\). Then

\[
\min_{|X|=3}\lambda_{\max}(G_K(X))=k+p.
\]

All minimizers are translates/reflections of \(\{0,d,2d\}\). At each minimizer the Gram eigenvalues are \(k+p,k+p,k-2p\). In particular, equispaced triples are never optimal under the stated hypotheses.

**Entire fractional Sobolev scale.** For each real \(s>1/2\), use the mean-zero periodic Hilbert space \(H^s_0(\mathbb T)\) with squared norm

\[
\|f\|_s^2=\sum_{n\in\mathbb Z\setminus\{0\}}(2\pi|n|)^{2s}|\widehat f(n)|^2.
\]

Its reproducing kernel is

\[
K_s(t)=\frac{2}{(2\pi)^{2s}}\sum_{n=1}^\infty\frac{\cos(2\pi nt)}{n^{2s}}.
\]

For any three distinct sampling sites, define \(C_s(X)^2\) as the smallest constant satisfying

\[
\sum_{j=1}^3|f(x_j)|^2\le C_s(X)^2\|f\|_s^2\quad\text{for every }f\in H^s_0(\mathbb T).
\]

For **every** real \(s>1/2\), the unique optimal geometry up to translation and reflection is \(\{0,d_s,2d_s\}\), where \(d_s\in(0,1/6)\) is the unique root of \(K_s(d_s)+K_s(2d_s)=0\). The sharp squared constant is

\[
\boxed{\min_{|X|=3}C_s(X)^2=\frac{2\zeta(2s)}{(2\pi)^{2s}}+K_s(d_s).}
\]

The optimizing eigenspace has dimension two. The geometry has two sharp limiting laws:

\[
\lim_{s\downarrow1/2}d_s=d_{1/2},\qquad
4\sin(\pi d_{1/2})\sin(2\pi d_{1/2})=1,
\qquad d_{1/2}\in(0,1/6),
\]

\[
\boxed{\lim_{s\to\infty}4^s\left(\frac16-d_s\right)=\frac{1}{3\pi\sqrt3}.}
\]

Write \(C_{s,\mathrm{eq}}^2\) for the squared three-site constant at the equispaced triple and \(k_s=K_s(0)\). The nonuniform design has a sharp, positive high-smoothness improvement:

\[
\boxed{\lim_{s\to\infty}4^s\frac{C_{s,\mathrm{eq}}^2-\min_X C_s(X)^2}{k_s}=\frac23.}
\]

All statements hold for real or complex Fourier Sobolev spaces with the displayed normalization.

## Assumptions and scope

The circle is \(\mathbb T=\mathbb R/\mathbb Z\), with normalized arclength measure. Samples have equal unit weights and distinct locations, without added measurement noise. The squared sampling norm is the largest eigenvalue of the reproducing-kernel Gram matrix. The general principle requires the stated strict decrease and sign condition; positive definiteness ensures Gram nonnegativity. The smoothness parameter is any **real** \(s>1/2\), including nonintegers, the full range in which point evaluation is continuous for this scale.

## Proof

**1. A three-gap spectral lower bound.** By translation and cyclic ordering, the three successive gaps \(g_1,g_2,g_3\) are strictly positive and sum to one. Each unordered pair of sites is joined by one gap, up to the symmetry \(K(t)=K(1-t)\). The two-by-two Gram principal submatrix for gap \(g\) has eigenvalues \(k\pm K(g)\); its larger eigenvalue is \(k+|K(g)|\). Eigenvalue interlacing gives

\[
\lambda_{\max}(G_K(X))\ge k+\max_{1\le i\le3}|K(g_i)|.
\]

By strict decrease, \(F(t)=K(t)+K(2t)\) is strictly decreasing on \([0,1/6]\); \(F(0)=2k>0\) and \(F(1/6)<0\). Its unique zero \(d\) obeys \(K(d)>0\), \(K(2d)<0\), since \(K(d)>K(2d)\). Thus \(K(d)=p=-K(2d)>0\).

Since \(K\) strictly decreases on the half-circle and is symmetric, the exact sublevel set of its absolute value is

\[
\{g\in[0,1]:|K(g)|\le p\}=[d,2d]\cup[1-2d,1-d].
\]

Suppose \(\max_i|K(g_i)|\le p\). The three gaps cannot all be in the short interval, because their sum would be at most \(6d<1\). At least two cannot be in the long interval, because their sum together with the remaining minimal gap is at least \(2(1-2d)+d=2-3d>1\). Exactly one is long; then the three gaps sum to at least \((1-2d)+d+d=1\), with equality only at the cyclic permutation of \((d,d,1-2d)\). Therefore every other triple has \(\max_i|K(g_i)|>p\) and hence \(\lambda_{\max}(G_K(X))>k+p\).

For the special triple, the three off-diagonal entries are \(p,p,-p\). Their sign product is negative; diagonalizing this real symmetric matrix gives exactly \(k+p\) twice and \(k-2p\) once. Because \(p>0\), its largest eigenvalue is \(k+p\). This achieves the lower bound and proves global uniqueness.

**2. Fourier Sobolev kernels meet the hypotheses.** For \(s>1/2\), point evaluations are bounded by Cauchy–Schwarz and the summability of \(\sum_{n\ne0}|n|^{-2s}\). Fourier Riesz representation yields \(K_s\), which is continuous and strictly positive-definite on distinct sites: for coefficients \(c_j\), its Gram quadratic form is a positive constant times \(\sum_{n\ne0}|n|^{-2s}|\sum_jc_je^{2\pi inx_j}|^2\); vanishing for all \(n\ne0\) forces all coefficients to vanish, by the Vandermonde argument applied to three successive positive integers. 

Let \(q=2s-1>0\). On any compact subinterval of \((0,1/2)\), differentiated Fourier series converge uniformly by Dirichlet summation. For \(0<\theta<\pi\),

\[
\sum_{n=1}^\infty\frac{\sin(n\theta)}{n^q}
=\frac1{\Gamma(q)}\int_0^\infty
u^{q-1}\frac{e^{-u}\sin\theta}{1-2e^{-u}\cos\theta+e^{-2u}}\,du>0.
\]

Thus \(K_s'(t)<0\) for \(0<t<1/2\); continuity ensures strict decrease on the closed interval.

Writing \(A_s=2/(2\pi)^{2s}\), grouping Fourier modes modulo six gives the exact identity

\[
K_s(1/6)+K_s(1/3)
=-A_s2^{-2s}\zeta(2s)(1-3^{1-2s})<0.
\]

The kernel principle applies, and by reproducing-kernel duality \(C_s(X)^2=\lambda_{\max}(G_{K_s}(X))\) without any missing norm factors.

**3. Low-smoothness limit.** For \(t\) in a compact subset of \((0,1)\), Dirichlet's test gives locally uniform convergence as \(s\downarrow1/2\) to

\[
K_{1/2}(t)=-\frac1\pi\log(2\sin(\pi t)).
\]

The limiting function \(K_{1/2}(t)+K_{1/2}(2t)\) is strictly decreasing on \((0,1/6]\), tends to positive infinity as \(t\downarrow0\), and has negative value at \(t=1/6\). Its unique root is equivalent to \(4\sin(\pi t)\sin(2\pi t)=1\). Fixing points on opposite sides of that root and using uniform convergence traps \(d_s\) between them, proving \(d_s\to d_{1/2}\).

**4. High-smoothness displacement and strict gain.** Put \(r_s=2^{-2s}=4^{-s}\) and \(H_s(t)=K_s(t)/A_s\). On compact arcs, the Fourier series and its first derivative converge uniformly as \(s\to\infty\) to \(\cos(2\pi t)\) and its derivative. Set \(\Phi_s(t)=H_s(t)+H_s(2t)\). Then \(\Phi_s(1/6)=-r_s\zeta(2s)(1-3^{1-2s})=-r_s(1+o(1))\), and \(\Phi_s'(1/6)=-3\pi\sqrt3+o(1)\). Its limiting zero in \((0,1/6]\) is uniquely \(1/6\); the root \(d_s\) therefore approaches \(1/6\). The mean value theorem now gives

\[
\frac16-d_s=\frac{r_s}{3\pi\sqrt3}(1+o(1)).
\]

At equal spacing \(K_s(1/3)=\frac{A_s}2\zeta(2s)(3^{1-2s}-1)<0\), and so \(C_{s,\mathrm{eq}}^2=k_s-K_s(1/3)\). The exact modulo-six identity above implies \(-K_s(1/3)-K_s(1/6)=A_sr_s(1+o(1))\). Meanwhile \(K_s(d_s)-K_s(1/6)=A_s\pi\sqrt3(1/6-d_s)+o(A_sr_s)=A_sr_s/3+o(A_sr_s)\). Subtracting gives

\[
C_{s,\mathrm{eq}}^2-\min_X C_s(X)^2=\frac23 A_s r_s(1+o(1)).
\]

Finally \(k_s/A_s=\zeta(2s)\to1\), proving the relative improvement law.

## Verification

The included `check.py` implements truncated cosine kernels, bisection of the unique root for multiple fractional/integer smoothness values, independent symmetric-matrix eigenvalue checks and random three-site stress tests. It also checks both large-smoothness limits against their analytic coefficients. The computations are corroboration only: the universal quantifiers, uniqueness and asymptotics are established by the four proof steps above. In particular, no finite Fourier truncation or finite mesh enumeration is used as a proof.

## Relationship to prior work

Wang and Zhang (2012, arXiv:1207.5871) optimize **reconstruction error** from point values in reproducing-kernel spaces, using kernel spans and subspace approximation; their minimized quantity is not the norm of the raw evaluation map, and they do not provide the three-site circular kernel criterion. Novak, Ullrich and Woźniakowski (2013, arXiv:1311.1528) analyze Fourier-coefficient integration error in univariate Sobolev spaces; Novak and Zhang (2016, arXiv:1609.01146) similarly optimize weighted quadrature error. Neither establishes the displayed three-output sampling norm. Krieg and Sonnleitner (2020, arXiv:2009.11275) establish asymptotic sampling-recovery rates via covering geometry, not a fixed three-site spectral-optimal classification. A previously derived \(s=1\) three-point periodic Sobolev trace constant, \((11+\sqrt{21})/150\), with node distance \((9-\sqrt{21})/30\), is a **covered special case**, not a new assertion of priority; it is consistent with the present formulas. The new scope is the abstract kernel principle, every fractional real smoothness above the evaluation threshold, and the two sharp limiting laws, including the high-smoothness gain coefficient.

## Limitations

The geometry is proved for exactly three equally weighted point samples, not for four or more sites, arbitrary sample weights, noise-aware reconstruction, derivative observations or general spatial dimensions. Only the stated class of decreasing circular kernels is covered; arbitrary positive-definite kernels can have oscillations that invalidate the gap argument. The low-smoothness limit concerns node locations, not a bounded evaluation norm at the endpoint, where point evaluation is unbounded. The high-smoothness limit is a limit of different Hilbert norms, not a result at infinite smoothness itself. No independent mathematical validation is asserted.

## References

1. R. Wang and H. Zhang, *Optimal Sampling Points in Reproducing Kernel Hilbert Spaces*, first posted 25 July 2012, https://arxiv.org/abs/1207.5871.
2. E. Novak, M. Ullrich and H. Woźniakowski, *Complexity of Oscillatory Integration for Univariate Sobolev Spaces*, first posted 6 November 2013, https://arxiv.org/abs/1311.1528.
3. E. Novak and S. Zhang, *Optimal Quadrature Formulas for the Sobolev Space* \(H^1\), first posted 5 September 2016, https://arxiv.org/abs/1609.01146.
4. D. Krieg and M. Sonnleitner, *Random Points Are Optimal for the Approximation of Sobolev Functions*, first posted 23 September 2020, https://arxiv.org/abs/2009.11275.
