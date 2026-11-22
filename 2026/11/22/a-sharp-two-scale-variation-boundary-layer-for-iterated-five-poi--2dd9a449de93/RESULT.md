# A sharp two-scale variation boundary layer for iterated five-point biharmonic smoothing

## Finding

Let \(L\) be the discrete nonnegative Laplacian on \(\mathbb Z\), \((Lx)_j=2x_j-x_{j-1}-x_{j+1}\), and let \(T_u=I-uL^2\). Its five coefficients at offsets \(-2,-1,0,1,2\) are respectively \(-u,4u,1-6u,4u,-u\). Fix any real \(\lambda\), and for positive integers \(r\) with \(u_r=1/8+\lambda/r>0\), form \(T_{u_r}^{r}\). Then the **sharp, attained variation-operator norm** has the following limit, uniformly for \(\lambda\) in any fixed compact real interval:

\[
\lim_{r\to\infty}\sup_{\operatorname{Var}(x)>0}\frac{\operatorname{Var}(T_{u_r}^{r}x)}{\operatorname{Var}(x)}
=\mathcal L_4+e^{16\lambda},\qquad
\mathcal L_4=\int_{\mathbb R}|H_4(z)|\,dz>1,
\quad H_4(z)=\frac1{2\pi}\int_{\mathbb R}e^{-s^4+isz}\,ds.
\]

The number \(\mathcal L_4\) is approximately \(1.2373\). Thus the critical limit at \(u=1/8\) is approximately \(2.2373\), whereas for any fixed \(0<u<1/8\) the sharp variation norm tends to \(\mathcal L_4\). For fixed \(u>1/8\), if \(\rho=16u-1>1\), the norm divided by \(\rho^r\) tends to \(1\). Hence the width of the transition between bounded and exponentially growing power norms is \(r^{-1}\), with the explicit crossover profile \(e^{16\lambda}\).

The five-point least-squares quadratic Savitzky–Golay smoother is the interior parameter \(u=3/35\), not the critical parameter. The same operator family is also the forward-Euler discretization of fourth-order lattice diffusion.

## Assumptions and scope

Sequences are real and indexed by every integer; \(\operatorname{Var}(x)=\sum_{j\in\mathbb Z}|x_j-x_{j-1}|<\infty\), and sequences differing by a constant are identified. A nonconstant step belongs to this space. Convolution kernels are real symmetric and finitely supported for each finite iterate. The exponent \(r\) is a positive integer. The parameter \(u_r\) depends on \(r\) and is eventually positive for every fixed \(\lambda\). Uniformity is over compact sets of \(\lambda\), not the whole real line at once.

## Proof

**1. The exact finite-iterate operator norm.** For a finitely supported convolution kernel \(p\), the discrete derivative commutes with convolution: \(\nabla(p*x)=p*(\nabla x)\). Young's inequality gives \(\operatorname{Var}(p*x)\le\|p\|_{\ell^1}\operatorname{Var}(x)\). If \(x_j=\mathbf1_{j\ge0}\), then \(\nabla x=\delta_0\), so equality holds. Accordingly, with \(p_u=\delta_0-uL^2\), the exact norm in the statement is \(\|p_u^{*r}\|_{\ell^1}\), and this is attained by the same step for every \(u,r\).

**2. The two Fourier peaks.** The Fourier symbol is
\[
\Phi_u(\theta)=1-4u(1-\cos\theta)^2,\qquad\theta\in[-\pi,\pi].
\]
At \(u_*=1/8\), its absolute value equals \(1\) only at the torus points \(0\) and \(\pi\). Around the two points, uniformly for bounded \(\lambda\) and \(u_r=u_*+\lambda/r\),
\[
\Phi_{u_r}(s)=1-u_rs^4+O(s^6),\quad
\Phi_{u_r}(\pi+s)=-1-16\lambda/r+s^2+O(s^4+|\lambda|s^2/r).
\]
Choose disjoint smooth periodic cutoffs \(\chi_0,\chi_\pi\) equal to one near their named peaks. The Fourier coefficients of \(\chi_0\Phi_{u_r}^r\), \(\chi_\pi\Phi_{u_r}^r\), and \((1-\chi_0-\chi_\pi)\Phi_{u_r}^r\) are denoted by \(A_{r,j}\), \(B_{r,j}\), and \(E_{r,j}\). Outside the two cutoffs, \(|\Phi_{u_r}|\le q<1\) uniformly for large \(r\) and bounded \(\lambda\). Differentiating the Fourier integrands twice and integrating by parts gives \(\sum_j|E_{r,j}|=o(1)\), indeed exponential decay times a polynomial in \(r\).

**3. Quartic local mass at the zero frequency.** Put \(a_r=(ru_r)^{1/4}\). Inverse Fourier inversion and the change \(s=v/a_r\) give, uniformly for \(j/a_r\) in bounded intervals,
\[
 a_r A_{r,j}-H_4(j/a_r)\longrightarrow0.
\]
The convergence is also uniform in bounded \(\lambda\). This compact-scale estimate can be promoted to \(\ell^1\) convergence of absolute masses. On the cutoff support, \(|\Phi_{u_r}(s)|^r\le Ce^{-crs^4}\) and derivatives through order four have the corresponding scaled bounds, giving \(\|\partial_s^4(\chi_0\Phi_{u_r}^r)\|_{L^1}=O(a_r^3)\). Four integrations by parts yield \(|A_{r,j}|\le Ca_r^3/|j|^4\) for nonzero \(j\), while direct Fourier inversion gives \(|A_{r,j}|\le C/a_r\). In particular \(\sum_{|j|>Ra_r}|A_{r,j}|\le CR^{-3}\). Riemann sums on \(|j|\le Ra_r\), followed by \(R\to\infty\), prove
\[
\sum_j|A_{r,j}|\longrightarrow\mathcal L_4.
\]
All bounds here are uniform over compact \(\lambda\)-sets.

**4. Gaussian local mass at the Nyquist frequency.** Put \(b_r=\sqrt r\). The expansion at \(\pi\), including the sign \((-1)^r\), gives
\[
 b_r(-1)^{r+j}B_{r,j}\longrightarrow e^{16\lambda}H_2(j/b_r),
\qquad H_2(z)=\frac1{\sqrt{4\pi}}e^{-z^2/4},
\]
locally uniformly in \(j/b_r\) and in compact \(\lambda\)-sets. The same scaled derivative argument, now using \(|\Phi_{u_r}(\pi+s)|^r\le Ce^{-crs^2}\), shows \(\|\partial_s^4(\chi_\pi\Phi_{u_r}^r)\|_1=O(b_r^3)\). Hence \(\sum_{|j|>Rb_r}|B_{r,j}|\le CR^{-3}\), and the Gaussian Riemann-sum limit gives
\[
\sum_j|B_{r,j}|\longrightarrow e^{16\lambda}\int_{\mathbb R}H_2(z)\,dz=e^{16\lambda}.
\]
Moreover \(\sup_j|B_{r,j}|=O(r^{-1/2})\), uniformly on the same compact sets.

**5. Separation of spatial scales.** Choose the intermediate radius \(d_r=r^{3/8}\). The Gaussian contribution on \(|j|\le d_r\) has total absolute mass \(O(d_r/\sqrt r)=O(r^{-1/8})\). The quartic contribution on \(|j|>d_r\) has total mass \(O((a_r/d_r)^3)=O(r^{-3/8})\). Thus the two terms become asymptotically disjoint in \(\ell^1\), even though they are Fourier contributions to the same kernel:
\[
\sum_j|A_{r,j}+B_{r,j}|=\sum_j|A_{r,j}|+\sum_j|B_{r,j}|+o(1).
\]
Combining with the remainder proves the claimed sharp crossover limit.

**6. Fixed-parameter phase limits.** If \(0<u<1/8\), zero frequency is the sole absolute-value-one maximum, and the quartic localization of step 3 gives \(\|p_u^{*r}\|_1\to\mathcal L_4\). If \(u>1/8\), the sole modulus-maximizing point is \(\pi\), with modulus \(\rho=16u-1\) and a strictly quadratic local maximum. After dividing by \(\rho^r\), the Gaussian localization of step 4 gives a mass limit of \(1\); all other frequencies are exponentially smaller. At the critical value \(u=1/8\), the main theorem with \(\lambda=0\) gives \(\mathcal L_4+1\).

**7. Strict gain beyond one.** Fourier inversion yields \(\int H_4=1\) and \(\int z^2H_4(z)\,dz=-\partial_s^2 e^{-s^4}|_{s=0}=0\). Since \(H_4\) is a nonzero Schwartz function, it cannot be an almost-everywhere nonnegative probability density with zero second moment. It has a negative part, so \(\mathcal L_4>1\). This also confirms that the limiting BV amplification is nontrivial.

## Verification

The attached program `check_biharmonic_boundary.py` verifies exact rational moment cancellation for the five-tap family; independently compares exact finite convolution powers with Fourier inversion; and compares multiple finite-scale critical powers to the predicted crossover profile. Its observed long-iteration convergence is slow because the competing spatial scales are \(r^{1/4}\) and \(r^{1/2}\). Those computations are corroboration only: the uniform asymptotic statement follows from the localization, derivative tail bounds and disjoint-scale proof above.

## Relationship to prior work

Savitzky and Golay (1964) introduced the least-squares smoothing framework; the five-point quadratic smoother corresponds to \(u=3/35\). Diaconis and Saloff-Coste (2012), especially Proposition 2.4 and Example 2.2, explicitly analyze **the same five-tap family**, including its critical \(u=1/8\) quartic/second-order Fourier contact points. Their results provide fixed-parameter local limits and power boundedness. Randles and Saloff-Coste (2012) develop broader multi-peak local-limit theory. The statement proved here is different: it computes a **sharp global variation-operator norm** for a **moving parameter \(u_r=1/8+\lambda/r\)** and accounts for the Gaussian contribution whose \(r^{-1/2}\) amplitude is invisible to the leading \(r^{-1/4}\) pointwise local limit. It does not claim discovery of the stencil, of the spectral threshold, or of either individual local profile.

## Limitations

This is a bilateral, real, translation-invariant, five-tap result for integer powers. Finite-chain boundary conditions, nonuniform grids, multidimensional stencils and arbitrary variable parameters away from the displayed scaling window are not covered. The sharp BV norm is attained by a step on the full integer line, not claimed for every finite interval. The limiting quartic constant is represented by an exact integral, not a closed elementary formula. Earlier spectral-approximation literature may contain an equivalent global norm asymptotic; the inspected primary statements do not show it.

## References

1. A. Savitzky and M. J. E. Golay, *Smoothing and Differentiation of Data by Simplified Least Squares Procedures*, Analytical Chemistry **36** (1964), 1627–1639. DOI: https://doi.org/10.1021/ac60214a047. First verified public issue date: 1964-07-01.
2. P. Diaconis and L. Saloff-Coste, *Convolution powers of complex functions on Z*, arXiv:1205.6490 (initial submission 2012-05-29), especially Theorems 2.1 and 2.3, Proposition 2.4, Example 2.2. https://arxiv.org/abs/1205.6490.
3. E. Randles and L. Saloff-Coste, *On the convolution powers of complex functions on Z*, arXiv:1212.4700 (initial submission 2012-12-19), especially Sections 2, 5 and 7. https://arxiv.org/abs/1212.4700.
