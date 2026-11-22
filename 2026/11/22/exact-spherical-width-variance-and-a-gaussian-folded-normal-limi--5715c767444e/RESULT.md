# Exact spherical-width variance and a Gaussian–folded-normal limit for isocanted cubes

## Finding
For every integer \(d\ge2\) and every \(a,b>0\), consider the Euclidean zonotope
\[
Z_d=[-b/2,b/2]^d+[-a/2,a/2]\mathbf1,
\qquad \mathbf1=(1,\ldots,1)\in\mathbb R^d.
\]
This is the standard isocanted alcoved cube of coordinate bounding length \(\ell=a+b\) and cant \(a\), up to translation. Let \(U_d\) be Haar-uniform on the unit sphere and let \(W_d=h_{Z_d}(U_d)+h_{Z_d}(-U_d)\) be its Euclidean directional width. Set
\[
c_d=\frac{\Gamma(d/2)}{\sqrt\pi\,\Gamma((d+1)/2)},\qquad
K(\rho)=\frac2\pi\left(\sqrt{1-\rho^2}+\rho\arcsin\rho\right).
\]
The **exact all-dimensional first and second moments** are
\[
\boxed{\ \mathbb EW_d=c_d(bd+a\sqrt d)\ },
\]
\[
\boxed{\begin{aligned}
\operatorname{Var}(W_d)
={}&b^2\left[1+\frac{2(d-1)}\pi-d^2c_d^2\right]
+a^2\left[1-dc_d^2\right]\\
&+2ab\sqrt d\left[K(d^{-1/2})-dc_d^2\right].
\end{aligned}}
\]
For fixed \(a,b>0\), let \(N,Z\) be independent standard real Gaussians and put \(\mu=\sqrt{2/\pi}\). Then
\[
\boxed{\ W_d-\mathbb EW_d\ \Longrightarrow\
b\sqrt{1-3/\pi}\,N+a(|Z|-\mu).\ }
\]
Convergence also holds for the first three centered moments, and therefore
\[
\boxed{\lim_{d\to\infty}\operatorname{Var}(W_d)=
b^2(1-3/\pi)+a^2(1-2/\pi),\qquad
\lim_{d\to\infty}\mathbb E(W_d-\mathbb EW_d)^3
=a^3\mu(4/\pi-1)>0.}
\]
The limiting centered law is non-Gaussian for every positive cant. The cube boundary \(a=0\) has a Gaussian limiting law. In particular, although widths are of leading order \(\sqrt d\), the diagonal generator leaves a persistent, strictly skewed angular fluctuation. Its strength \(a\) is recoverable from the limiting third moment; the box length \(b\) is independently determined by the leading scaled mean.

## Assumptions and scope
The Euclidean metric is the coordinate Euclidean metric on \(\mathbb R^d\); directions are uniform on \(S^{d-1}\), **not** unnormalized Gaussian vectors. The diagonal has full Euclidean length \(a\sqrt d\), although its coordinate shift is \(a\). Width is support plus antipodal support, not half-width. In the asymptotic statements \(a,b>0\) remain fixed as dimension increases. The limiting law extends continuously to \(a=0\), but that point is a cube and not a positive-cant isocanted polytope. The all-dimensional formulas hold for \(d\ge2\).

## Proof
**1. Width identity.** The support function is Minkowski-additive, and a centered segment with displacement vector \(v\) has directional width \(|\langle v,u\rangle|\). Thus, for every unit \(u\),
\[
W_d(u)=b\sum_{i=1}^d|u_i|+a\left|\sum_{i=1}^du_i\right|.
\tag{1}
\]
This fixes both the Euclidean normalization and the coefficient of the diagonal term.

**2. Exact first and second moments.** By rotational invariance, for each unit vector \(v\), \(\mathbb E|\langle U_d,v\rangle|=c_d\). Taking the diagonal unit vector \(d^{-1/2}\mathbf1\) gives the stated mean. Write \(A_d=\sum|U_{d,i}|\), \(B_d=|\sum U_{d,i}|\). For any unit \(v,w\) with inner product \(\rho\), the standard Gaussian representation \(U_d=G/\|G\|_2\) and independence of Gaussian radius and direction give
\[
\mathbb E\left|\langle U_d,v\rangle\langle U_d,w\rangle\right|
=\frac1d\,K(\rho).
\tag{2}
\]
Indeed \(\mathbb E\|G\|_2^2=d\), while the absolute bivariate Gaussian moment is \(K(\rho)\). For distinct coordinates, \(K(0)=2/\pi\), and the diagonal unit vector has inner product \(d^{-1/2}\) with each coordinate axis. Therefore
\[
\mathbb EA_d^2=1+\frac{2(d-1)}\pi,\quad
\mathbb EB_d^2=1,\quad
\mathbb EA_dB_d=\sqrt d\,K(d^{-1/2}).
\tag{3}
\]
Subtracting \((\mathbb EA_d)^2=(dc_d)^2\), \((\mathbb EB_d)^2=dc_d^2\), and \(\mathbb EA_d\mathbb EB_d=d\sqrt d\,c_d^2\) gives the exact variance identity. Notice that the cross term is not dropped at finite dimension.

**3. Joint spherical central limit theorem.** Let \(G_1,\dots,G_d\) be independent \(N(0,1)\). Define
\[
X_d=d^{-1/2}\sum_i(|G_i|-\mu),\quad
Y_d=d^{-1/2}\sum_i(G_i^2-1),\quad
T_d=d^{-1/2}\sum_iG_i.
\]
The multivariate independent-summand CLT gives a centered Gaussian limit \((X,Y,T)\). Direct one-coordinate moments yield
\[
\operatorname{Var}(X)=1-\mu^2,\quad
\operatorname{Var}(Y)=2,\quad
\operatorname{Cov}(X,Y)=\mu,
\]
whereas \(\operatorname{Cov}(T,X)=\operatorname{Cov}(T,Y)=0\) by odd parity, and \(\operatorname{Var}(T)=1\). Hence \(T\) is independent of the pair \((X,Y)\) in the joint Gaussian limit. The norm expansion is
\[
\frac{\sqrt d}{\|G\|_2}
=1-\frac{Y_d}{2\sqrt d}+o_{\mathsf P}(d^{-1/2}).
\]
Using (1),
\[
A_d-\mu\sqrt d=X_d-\frac\mu2Y_d+o_{\mathsf P}(1),\qquad
B_d=\frac{\sqrt d}{\|G\|_2}|T_d|=|T_d|+o_{\mathsf P}(1).
\]
Therefore the centered width limit is \(b(X-\mu Y/2)+a(|T|-\mu)\). Its first Gaussian variance is
\[
\operatorname{Var}(X-\mu Y/2)
=1-\mu^2+\frac{\mu^2}{2}-\mu^2=1-3/\pi,
\]
and this component is independent of \(T\). The exact gamma-ratio asymptotic \(c_d=\mu d^{-1/2}(1+O(d^{-1}))\) shows \(\mathbb EW_d=b\mu\sqrt d+a\mu+o(1)\), justifying exact-mean centering.

**4. Centered moments and nonnormality.** Both functions \(A_d\) and \(B_d\) on the unit sphere are \(\sqrt d\)-Lipschitz. Standard spherical concentration bounds their deviations from their means by dimension-uniform sub-Gaussian tails, hence their centered absolute moments of each fixed order are uniformly bounded. This supplies uniform integrability for the limiting third moment, not just weak convergence. The exact variance may alternatively be passed to the limit using the formulas in Step 2. Since \(\mathbb E|T|=\mu\), \(\mathbb E|T|^2=1\), and \(\mathbb E|T|^3=2\mu\), its third centered moment is
\[
2\mu-3\mu+2\mu^3=\mu(4/\pi-1)>0.
\]
A centered Gaussian has zero third moment, and independence makes the other mixed third terms vanish. Thus the limiting law is nonnormal for every \(a>0\). Finally the leading mean identifies \(b\), and this strictly positive limiting third moment identifies \(a\).

## Verification
Run `python verify_width.py` with Python 3.10+ and NumPy. The checker enumerates every sign-choice corner in 240 random finite instances (dimensions two through seven) and compares the exact maximum-minus-minimum with (1). It separately evaluates 65,536 deterministic circle directions to validate both first and second moment identities in dimension two for two parameter pairs, checks finite-dimensional spherical Monte Carlo means and variances in dimensions 8, 64, and 256, and checks convergence of the exact variance at dimension 20,000. Its final success marker is `ISOCANTED_ANGULAR_WIDTH_EXACT_PASS`. The moment and limit theorems are proved in Steps 1–4, not inferred from finite numerical tests.

## Relationship to prior work
De la Puente and Clavería [1, Corollary 3.16] introduced and established the cube-plus-diagonal Minkowski representation, and the same paper classifies combinatorial faces; that representation is background. Kabluchko, Prochno and Thäle [2] explain earlier Gaussian projection-width CLTs for cubes and study multi-norm CLTs; their theorem does not contain a nonzero diagonal generator or the resulting independent folded-normal correction. A published bounded-degree graphical-zonotope width CLT [3] uses a degree-restricted graph family and a Gaussian law; the present long diagonal direction lies outside that regime. Published isocanted-cube uniform **interior-volume** covariance work [4] concerns a different sampling measure and not random support widths. These comparisons do not claim that standard Gaussian CLT, spherical moment formulas, or the Minkowski representation themselves are new.

## Limitations
The non-Gaussian limiting law assumes positive cant fixed with dimension. It is not a rate of convergence nor a uniform theorem for dimension-dependent cant ratios; the finite-dimensional exact mean and variance remain valid for all positive \(a,b\). The proof concerns one random direction and its marginal width, not the joint law of several correlated directions. The mathematical originality comparison covers the inspected primary sources and indexed records; an inaccessible or unindexed equivalent analysis could change priority. Independent review has not been carried out.

## References
1. María Jesús de la Puente and Pedro Luis Clavería, *Isocanted alcoved polytopes*, arXiv:2009.13858, first public submission 2020-09-29, https://arxiv.org/html/2009.13858v1, especially Corollary 3.16.
2. Zakhar Kabluchko, Joscha Prochno and Christoph Thäle, *High-dimensional limit theorems for random vectors in \(\ell_p^n\)-balls*, arXiv:1709.09470, 2017, https://arxiv.org/pdf/1709.09470, Introduction and Theorem 1.1.
3. *Gaussian universality for random widths of bounded-degree graphical zonotopes*, published research record, 2026-10-25, https://github.com/published-finding corpus/2026/blob/main/2026/10/25/SCOPE-gaussian-universality-for-random-widths-of-bounded-degree-graphi--7b346228232c/RESULT.md.
4. *Uniform-volume covariance and latent interval law for isocanted cubes*, published research record, 2026-10-25, https://github.com/published-finding corpus/2026/blob/main/2026/10/25/SCOPE-uniform-volume-covariance-and-latent-interval-law-for-isocanted--da9911a588e4/RESULT.md.
