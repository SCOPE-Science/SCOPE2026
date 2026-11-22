# Universal regular-polygon D-optimality and global stability for weighted annular Szegő sampling

## Finding
Let \(0<q<\rho<1\), \(r>0\), and \(N\ge2\) be arbitrary. On the annulus \(\mathbb A_q=\{q<|z|<1\}\), consider the weighted Hardy reproducing kernel
\[
S_{q,r}(z,w)=\sum_{m\in\mathbb Z}\frac{(z\overline w)^m}{1+r q^{2m}}.
\]
For \(N\) distinct nodes \(z_j=\rho e^{i\theta_j}\) on the prescribed circle, form their Hermitian Gram matrix \(G=(S_{q,r}(z_i,z_j))_{i,j=1}^{N}\). Then **\(\det G\) is uniquely maximized, modulo rotation and permutation, by the regular \(N\)-gon**, for every choice of the annulus, circle radius, and positive boundary-weight parameter. The same is true for the normalized Gram determinant because all diagonal entries are equal.

Set
\[
a_m=\frac{\rho^{2m}}{1+r q^{2m}},\qquad A_j=\sum_{m\equiv j\pmod N}a_m,\qquad A=\sum_{m\in\mathbb Z}a_m.
\]
Each sum converges and \(A_j>0\). The exact optimal raw and normalized determinants are
\[
\max\det G=N^N\prod_{j=0}^{N-1}A_j,\qquad
\max\det\bigl(G/A\bigr)=\frac{N^N}{A^N}\prod_{j=0}^{N-1}A_j.
\]
The optimizing Gram eigenvalues are exactly \(N A_j\), \(0\le j<N\).

There is also a **global, explicit, strictly positive angular stability bound**. Write the nodes in counterclockwise order, extend \(\theta_{j+N}=\theta_j+2\pi\), and put \(s_{i,k}=\theta_{i+k}-\theta_i\) for \(1\le i\le N\), \(1\le k<N\). Let
\[
L=-\log(q^2),\qquad a=-\log(\rho^2),\qquad
c_{q,\rho}=\frac{8\pi^2}{L^2}\frac{1-\cos(2\pi a/L)}{\sinh(2\pi^2/L)}>0.
\]
Then
\[
\log\frac{\det G_{\mathrm{reg}}}{\det G}
\ge\frac{c_{q,\rho}}4\sum_{k=1}^{N-1}\sum_{i=1}^{N}
\left(s_{i,k}-\frac{2\pi k}{N}\right)^2.
\]
The bound is strict for every nonregular configuration; its coefficient is explicit but is **not claimed to be best possible**. The maximizing geometry and this coefficient are independent of \(r\).

## Assumptions and scope
All statements concern the exactly specified weighted Szegő kernel above; no boundary limit \(\rho=q\) or \(\rho=1\) is included, and no multi-radius or nonuniform node-weight claim is made. The determinant is the determinant of the positive definite complex Hermitian matrix of point evaluation kernels. The boundary-weight parameter \(r\) is arbitrary and strictly positive. The only equivalences among optimizers are common rotation and permutation. All Fourier sums over integers converge absolutely since \(q<\rho<1\).

## Proof
**1. Elliptic determinant reduction.** Put \(p=q^2\), \(R=\rho^2\), and define the multiplicative theta function
\[
\vartheta(z;p)=(z;p)_\infty(p/z;p)_\infty,
\quad (z;p)_\infty=\prod_{m\ge0}(1-zp^m).
\]
Ramanujan's bilateral summation identifies \(S_{q,r}\) with the Jordan–Kronecker theta quotient (up to a parameter-dependent positive scalar). Frobenius's elliptic Cauchy determinant formula, applied with \(x_i=z_i\), \(y_j=\overline{z_j}\), and theta parameter \(-r\), gives
\[
\det G=C_{q,r,\rho,N}\prod_{1\le i<j\le N}
\left|\frac{\vartheta(e^{i(\theta_j-\theta_i)};p)}
{\vartheta(R e^{i(\theta_j-\theta_i)};p)}\right|^2,
\]
where \(C_{q,r,\rho,N}>0\) depends only on the displayed parameters, not on any angle. Indeed, the extra Frobenius theta factor is \(\vartheta(-rR^N;p)\), independent of angular positions; its denominator is \(\vartheta(-r;p)\). The diagonal factors are \(\vartheta(R;p)\), and the offdiagonal denominator factors pair into squared moduli. The strict positivity follows alternatively from the strictly positive Laurent coefficients \(a_m\), which separate distinct points.

**2. Strict concavity of the annular interaction.** For \(0<t<2\pi\), put
\[
v(t)=\log\left|\frac{\vartheta(e^{it};p)}{\vartheta(R e^{it};p)}\right|^2.
\]
The theta product yields, with \(L=-\log p\), \(a=-\log R\), and \(0<a<L\), the absolutely convergent differentiated identity
\[
v'(t)=\sum_{m\in\mathbb Z}\left[
\frac{\sin t}{\cosh(mL)-\cos t}-
\frac{\sin t}{\cosh(mL+a)-\cos t}\right].
\]
For \(0<t<2\pi\), the Fourier transform in \(x\) of \(P_t(x)=\sin t/(\cosh x-\cos t)\) is
\[
\widehat P_t(\xi)=2\pi\frac{\sinh((\pi-t)|\xi|)}{\sinh(\pi|\xi|)},
\]
with the continuous value \(2(\pi-t)\) at \(\xi=0\). To verify the transform, expand \(P_t(x)=2\sum_{j\ge1}e^{-j|x|}\sin(jt)\) for \(x\ne0\), Fourier transform each exponential using Abel regularization, and apply the explicit sine-series identity \(\sum_{j\ge1} j\sin(jt)/(j^2+\xi^2)=(\pi/2)\sinh((\pi-t)|\xi|)/\sinh(\pi|\xi|)\), obtained by the elementary Dirichlet Green function on \(0,2\pi\). Poisson summation of the difference of the two \(L\)-periodizations cancels the zero Fourier mode and gives
\[
v'(t)=\frac{4\pi}{L}\sum_{h=1}^\infty
\left[1-\cos\left(\frac{2\pi h a}{L}\right)\right]
\frac{\sinh\left(\frac{2\pi h(\pi-t)}{L}\right)}
{\sinh\left(\frac{2\pi^2 h}{L}\right)}.
\]
Termwise differentiation is legitimate on compact subintervals of \((0,2\pi)\). Therefore
\[
-v''(t)=\frac{8\pi^2}{L^2}\sum_{h=1}^\infty
h\left[1-\cos\left(\frac{2\pi h a}{L}\right)\right]
\frac{\cosh\left(\frac{2\pi h(\pi-t)}{L}\right)}
{\sinh\left(\frac{2\pi^2h}{L}\right)}
\ge c_{q,\rho}>0.
\]
The \(h=1\) summand proves the uniform bound because \(0<a<L\). In particular \(v\) is strictly concave throughout \((0,2\pi)\), not merely monotone on a semicircle.

**3. Cyclic Jensen argument and stability.** Extend the angles by \(\theta_{i+N}=\theta_i+2\pi\) and define \(s_{i,k}\) as in the finding. Since \(v(2\pi-t)=v(t)\), the determinant reduction reads
\[
\log\det G=\log C_{q,r,\rho,N}
+\frac12\sum_{k=1}^{N-1}\sum_{i=1}^{N}v(s_{i,k}).
\]
For each \(k\), the mean of the \(N\) arcs is exactly \(2\pi k/N\). The strictly concave estimate
\[
v(x)\le v(y)+v'(y)(x-y)-\frac{c_{q,\rho}}2(x-y)^2
\]
for all \(x,y\in(0,2\pi)\), summed over those arcs, proves the stated global stability inequality. It also proves the unique maximum: the \(k=1\) term can attain equality only when every consecutive angular gap equals \(2\pi/N\).

**4. Spectral value.** For the regular polygon \(\theta_j=\theta_0+2\pi j/N\), Fourier orthogonality makes \(G\) circulant. Its discrete Fourier modes have eigenvalues \(N A_j\) because only Laurent exponents congruent to \(j\pmod N\) survive. Taking their product gives the exact maximal determinant, and dividing by \(A^N\) gives the normalized value.

## Verification
A standalone numerical checker, `check_annular_design.py`, reproduces (i) a high-precision comparison of the theta-logarithm derivative with its Poisson-summation series, (ii) its negative second derivative, (iii) a Frobenius determinant ratio against direct Laurent Gram evaluation, and (iv) the precise regular-polygon eigenvalue formula and strict advantage over perturbed configurations. The analytic proof applies to all parameters, including values that cannot be exhaustively tested; no finite computation is used as an infinite theorem certificate.

## Relationship to prior work
Katori and Shirai (first public 2020) give the weighted annular Szegő kernel, theta quotient, and Frobenius elliptic Cauchy determinant identity, and study Gaussian Laurent zero correlations. Their explicit determinant factorization supplies the starting point but their inspected theorems do not optimize configurations of a fixed-radius sampling circle or give the strictly concave theta ratio and its global angular stability modulus. Gafai, Murid and Wahid (2022) give product formulas and annular kernel zeros, not circular determinant design. Dubickas and Pritsker (2019) solve a different weighted Vandermonde Fekete problem with one-point external field. General circle-energy rearrangements can yield regularity once strict potential concavity has been shown; the new point here is the all-annulus Poisson-strip proof of that concavity and the exact weighted-kernel determinant/stability consequence. Potential equivalent formulations in classical elliptic energy or theta-function design literature remain a research priority risk.

## Limitations
This is a single-circle, equal-evaluation-weight, fixed-radius D-optimality theorem, not a general multi-radius Fekete theorem. It does not assert E-optimality or optimal condition number. The displayed global stability coefficient is explicit rather than claimed sharp. The argument uses established Ramanujan and Frobenius identities as background and proves the requisite strict concavity and angular optimization. Historical priority is assessed at best knowledge only; equivalence to classical elliptic-energy theorems has not been conclusively excluded.

## References
- M. Katori and T. Shirai, *Zeros of the i.i.d. Gaussian Laurent series on an annulus: weighted Szegő kernels and permanental-determinantal point processes*, arXiv:2008.04177, first posted 2020-08-10. https://arxiv.org/abs/2008.04177 ; open full text https://link.springer.com/article/10.1007/s00220-022-04365-2 (especially Proposition 2.2, §3.2 and Lemma 3.4).
- N. S. Gafai, A. H. M. Murid and N. H. A. A. Wahid, *Infinite Product Representation for the Szego Kernel for an Annulus*, arXiv:2202.09114, first posted 2022-02-18. https://arxiv.org/abs/2202.09114 ; https://onlinelibrary.wiley.com/doi/10.1155/2022/3763450.
- A. Dubickas and I. Pritsker, *Weighted Fekete points on the real line and the unit circle*, arXiv:1902.08348, first posted 2019-02-22. https://arxiv.org/abs/1902.08348.
- Frobenius elliptic Cauchy determinant identity as stated with original references in Katori–Shirai, §3.2, equation (3.3).
