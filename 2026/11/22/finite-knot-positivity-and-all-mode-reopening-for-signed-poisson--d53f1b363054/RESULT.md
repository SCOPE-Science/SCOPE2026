# Finite-knot positivity and all-mode reopening for signed Poisson-mixture covariances

## Finding
Let \(d\ge2\) and \(k\ge1\) be integers, and let \(\mu\) be a nonzero finite positive Borel measure with compact support in \((0,1)\) that is **not** concentrated at one point. On the circle \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\), set
\[
P_r(\theta)=\frac{1-r^2}{1-2r\cos\theta+r^2},\quad F_\mu(\theta)=\int P_r(\theta)\,d\mu(r),\quad Q(\theta)=c_0+2\sum_{j=1}^dc_j\cos(jk\theta),
\]
where \(c_0,\ldots,c_d\in\mathbb R\) may have either sign. Write \(K(x,y)=F_\mu(x-y)Q(x-y)\), \(a_n=\int r^{|n|}\,d\mu(r)\), and \(b_n=\widehat{F_\mu Q}(n)\), with Fourier normalization \(\widehat f(n)=(2\pi)^{-1}\int_0^{2\pi}f(\theta)e^{-in\theta}\,d\theta\). Define the \(d+1\) spectral knots \(u_j=b_{jk}\), \(0\le j\le d\).

**Theorem.** The following conditions are equivalent:

1. \(K\) is positive semidefinite on every finite collection of circle sites;
2. \(u_j\ge0\) for every \(0\le j\le d\).

The linear map from \((c_0,\ldots,c_d)\) to \((u_0,\ldots,u_d)\) is invertible, so the entire admissible coefficient set is a simplicial cone with exactly \(d+1\) nonredundant facet inequalities and \(d+1\) extreme rays. For any **nonzero** admissible mask, all Fourier coefficients are strictly positive except precisely those among \(\{0,\pm k,\ldots,\pm dk\}\) whose specified knot is zero. Consequently **every nonzero admissible kernel is strictly positive definite on finite sets of distinct sites**; it is \(C(\mathbb T)\)-universal if and only if all the knots are strictly positive.

This is a complete all-degree positivity classification for nontrivial positive mixtures, not a claim about arbitrary completely monotone Fourier sequences or arbitrary signed mixing measures.

## Assumptions and scope
The compact-support assumption keeps the Poisson mixture analytic and strictly positive on the circle and makes all Fourier series absolutely summable. Both \(\mu\) and the harmonic spacing \(k\) are fixed, while the mask coefficients are unrestricted real numbers. The measure may have finitely or infinitely many scales, but must assign positive mass to at least two distinct scales. The zero mask is positive semidefinite but is neither strictly positive definite nor universal. All claims concern continuous stationary kernels on \(\mathbb T\), not higher-dimensional spheres or unrelated spectral bases.

## Proof
**1. An inverse-convolution maximum principle.** First consider any nonzero compactly supported positive Poisson mixture \(F\) with Fourier coefficients \(a_n\). Put \(y=2-2\cos\theta\). Writing
\[
F(\theta)=S(y),\qquad S(y)=\int\frac{(1-r^2)/r}{y+(1-r)^2/r}\,d\mu(r),
\]
shows that \(S\) is a nonzero Stieltjes function. By the Stieltjes/complete-Bernstein reciprocal theorem [3], \(H(y)=1/S(y)\) admits
\[
H(y)=\alpha+\beta y+\int_{(0,\infty)}\frac{y}{y+t}\,d\sigma(t),\qquad \alpha,\beta\ge0,\quad\sigma\ge0.
\]
The coefficient of \(e^{in\theta}\) in \((t+2-2\cos\theta)^{-1}\) equals \(\rho(t)^{|n|}/\sqrt{t(t+4)}\), where
\[
\rho(t)=\frac{t+2-\sqrt{t(t+4)}}{2}\in(0,1).
\]
Therefore, if \(q_n=\widehat{1/F}(n)\), then for each positive integer \(n\),
\[
q_n=-\beta\mathbf1_{\{n=1\}}-\int\frac{t\rho(t)^n}{\sqrt{t(t+4)}}\,d\sigma(t)\le0.
\]
For a non-point mixing measure all these inequalities are strict: if \(\sigma=0\), then \(1/S\) is affine and \(S\) is one resolvent, which by uniqueness of Stieltjes transforms and strict monotonicity of \(r\mapsto(1-r)^2/r\) forces \(\mu\) to be a point mass. Moreover \(q_{-n}=q_n\), \(q\in\ell^1(\mathbb Z)\) (since \(F\) is positive and analytic), and \(\sum_nq_n=1/F(0)>0\).

Here is the maximum principle that will be used twice. Let \(v\in c_0(\mathbb Z)\) be real, nonnegative on a prescribed nonempty boundary set \(B\), and satisfy \((q*v)_n=0\) for \(n\notin B\). If a negative minimum \(m\) occurs outside \(B\), then at that site
\[
0=(q*v)_n=m\sum_\ell q_\ell+\sum_{\ell\ne0}q_\ell(v_{n-\ell}-m)\le m/F(0)<0,
\]
a contradiction. If all off-diagonal \(q_n\) are negative and some boundary value is positive, then every exterior value is strictly positive: an exterior zero would yield a strictly negative convolution because it couples to that positive boundary value.

**2. Positivity at the coarse spectral knots.** Set \(R=r^k\) and push \(\mu\) forward to a measure \(\nu\) under this map. The subsequence \(a_{jk}=\int R^{|j|}\,d\nu(R)\) is again a compactly supported non-point Poisson mixture. On the coarse integer lattice, the convolution of this sequence with the finite symmetric mask \((c_{-d},\ldots,c_d)\), with \(c_{-j}=c_j\), is exactly \(v_j=b_{jk}\). Its inverse convolution \(q^{(k)}\) has strictly negative off-diagonal coefficients by Step 1. Because the mask vanishes outside \([-d,d]\), we have \((q^{(k)}*v)_j=0\) for \(|j|>d\). Applying the maximum principle with boundary \([-d,d]\) proves that \(u_0,\ldots,u_d\ge0\) force \(b_{jk}\ge0\) for **every** integer \(j\). If any knot is positive, then \(b_{jk}>0\) whenever \(|j|>d\).

**3. Positivity between the knots.** On the original integer lattice, the finitely supported mask has nonzero entries only at \(0,\pm k,\ldots,\pm dk\). Thus \((q*b)_n=c_n=0\) for every \(n\notin k\mathbb Z\). The boundary set is now the entire sublattice \(k\mathbb Z\), on which Step 2 established nonnegativity. The maximum principle yields \(b_n\ge0\) at every other frequency. With at least one positive knot, strict off-diagonal negativity implies \(b_n>0\) for every \(n\notin k\mathbb Z\). Together with Step 2, the only possible Fourier zeros of a nonzero admissible kernel are exactly its zero knots.

The converse is immediate: a continuous stationary positive-semidefinite kernel on the circle must have all Fourier coefficients nonnegative (the circle Bochner criterion). In particular its knots are nonnegative.

**4. Exact cone and stability.** The knot map \(u=Mc\) has entries
\[
M_{j0}=a_{jk},\qquad M_{j\ell}=a_{|j-\ell|k}+a_{(j+\ell)k}\quad(1\le\ell\le d),\qquad 0\le j\le d.
\]
Let \(D=\mathrm{diag}(1,\tfrac12,\ldots,\tfrac12)\). Then \(MD\) is the Gram matrix of \(1,\cos(k\theta),\ldots,\cos(dk\theta)\) in \(L^2(F_\mu(\theta)d\theta/(2\pi))\). It is strictly positive definite because \(F_\mu>0\) and these cosine polynomials are linearly independent. Thus \(M\) is invertible and the cone is linearly equivalent to the positive orthant, proving its exact facet and extreme-ray count.

Every nonzero feasible kernel has \(b_n>0\) for all \(|n|>dk\). At any \(m\) distinct sites, choose \(m\) consecutive such Fourier frequencies; their exponential evaluation matrix is a nonsingular Vandermonde matrix. Hence the kernel Gram matrix is strictly positive definite. The RKHS contains each Fourier character whose \(b_n>0\). By density of trigonometric polynomials and continuity of Fourier coefficient functionals on \(C(\mathbb T)\), its RKHS is uniformly dense in \(C(\mathbb T)\) exactly when every \(b_n>0\), equivalently every knot is positive.

## Verification
A standalone exact-rational checker (`checker.py`) generates the knot matrix and inverts it over \(\mathbb Q\) for several two-, three- and four-scale mixtures, degrees \(2\) through \(6\), and spacings \(1\) through \(4\). It independently verifies the first-knot basis, strict positivity of all tested non-knot modes, and nonnegative-knot superpositions. It also tests pure-scale tail collapse as a contrast. These finitely many assertions are consistency checks, **not a replacement for the infinite maximum-principle proof**.

As one explicit certificate, take \(\mu=\tfrac12\delta_{1/4}+\tfrac12\delta_{3/4}\), \(d=2\), \(k=1\). The mask
\[
(c_0,c_1,c_2)=\left(\frac{317}{195},-\frac{112}{195},-\frac{16}{195}\right)
\]
has knot vector \((u_0,u_1,u_2)=(1,0,0)\), yet \(b_3=b_4=1/30>0\) and **all** subsequent Fourier coefficients are strictly positive. It is an extreme ray that is strictly positive definite while failing uniform universality.

Reproduction: run `python3 checker.py` with the standard Python library. Exact assertions check only finitely many rational cases; neither a numerical FFT nor an automated symbolic package is needed.

## Relationship to prior work
Bonfim–Guella–Menegatto [1], particularly their circle product alternative, characterizes positive-definite products under the assumption that both factors are themselves of positive type. Signed trigonometric masks here need not have that property. Buhmann–Jäger [2] treats harmonic-block positivity criteria, primarily on higher-dimensional spheres; it does not give this finite exact cone for signed masks on arbitrary Poisson mixtures. The standard Stieltjes/complete-Bernstein reciprocity theorem in [3] is an essential analytic ingredient, **not claimed as new**. The new assertion is its combination with a two-stage discrete maximum principle to classify every signed degree-\(d\), spacing-\(k\) modulation of a non-point Poisson mixture, including exact spectral zeros and all-boundary strict positivity. General positive-definite kernel and discrete potential theory may contain an equivalent formulation; independent priority review remains necessary.

## Limitations
Compact support inside \((0,1)\) and positive mixing are assumed. A point-mass mixture can have finite-rank extreme rays, unlike the non-point case; the strict spectral-reopening statement does not extend to such measures. No extension to signed mixing measures, general stationary kernels, noncompact mixing support, or higher-dimensional spheres is asserted. The theorem is mathematically reviewed here but has not received an independent external audit or a publication-priority determination.

## References
[1] R. N. Bonfim, J. C. Guella and V. A. Menegatto, *Strictly Positive Definite Functions on Compact Two-Point Homogeneous Spaces: the Product Alternative*, arXiv:1803.03105, first posted 22 February 2018, https://arxiv.org/html/1803.03105v2.

[2] M. Buhmann and J. Jäger, *Strict Positive Definiteness of Convolutional and Axially Symmetric Kernels on d-Dimensional Spheres*, arXiv:2105.02586, first posted 6 May 2021; *J. Fourier Anal. Appl.* 28 (2022), article 40, https://doi.org/10.1007/s00041-022-09913-x.

[3] R. L. Schilling, R. Song and Z. Vondracek, *Bernstein Functions: Theory and Applications*, second edition, De Gruyter (2012), especially Chapters 6–7 and the reciprocal characterization of Stieltjes functions, https://doi.org/10.1515/9783110269338.
