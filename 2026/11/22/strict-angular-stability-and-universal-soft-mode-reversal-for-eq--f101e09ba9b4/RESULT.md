# Strict angular stability and universal soft-mode reversal for equiradial finite Blaschke products

## Finding
Fix any integer \(n\ge5\) and radius \(0<r<1\). For a degree-\(n\) finite Blaschke product whose zeros are \(a_j=r e^{i\theta_j}\), define the squared boundary-speed variance
\[
\mathcal V_{n,r}(\theta)=\frac1{2\pi}\int_0^{2\pi}\left(|B'(e^{it})|-n\right)^2\,dt.
\]
At the equally spaced configuration \(\theta_j^*=2\pi j/n\), the value is exactly
\[\mathcal V_{n,r}(\theta^*)=\frac{2n^2r^{2n}}{1-r^{2n}}.\]
Let \(u=r^2\), and for \(0\le k<n\) define
\[
A_{n,k}(u)=u^k\left[\frac{k^2}{1-u^n}+\frac{2knu^n}{(1-u^n)^2}+\frac{n^2u^n(1+u^n)}{(1-u^n)^3}\right].
\]
For an arbitrary small real angular perturbation \(\varepsilon\), set
\[\widehat\varepsilon_k=\frac1{\sqrt n}\sum_{j=0}^{n-1}\varepsilon_j e^{-2\pi i jk/n}.\]
The **full local quadratic spectrum**, modulo simultaneous rotation, is
\[
\mathcal V_{n,r}(\theta^*+\varepsilon)
=\mathcal V_{n,r}(\theta^*)+\sum_{k=1}^{n-1}\kappa_{n,k}(u)|\widehat\varepsilon_k|^2+O_{n,r}(\|\varepsilon^\circ\|_2^3),
\qquad \boxed{\kappa_{n,k}(u)=n\bigl(A_{n,k}(u)+A_{n,n-k}(u)-2A_{n,0}(u)\bigr)>0},
\]
where \(\varepsilon^\circ=\varepsilon-n^{-1}(\sum_j\varepsilon_j)(1,\ldots,1)\). Thus the configuration is a **strict local minimizer up to common rotation**, with a sharp local quadratic constant given by \(\min_{1\le k<n}\kappa_{n,k}(u)\). (The actual real Hessian eigenvalues are \(2\kappa_{n,k}\), not \(\kappa_{n,k}\).)

The entire modal hierarchy has two opposite limiting regimes. For \(1\le k\le\lfloor n/2\rfloor\), as \(u\downarrow0\),
\[
\kappa_{n,k}(u)\sim
\begin{cases}
 n k^2u^k,&2k<n,\\
 2n k^2u^k,&2k=n.
\end{cases}
\]
Consequently the **unique least-curved frequency**, up to the conjugate pair, is \(k=\lfloor n/2\rfloor\) for sufficiently small \(u\). In contrast, as \(u\uparrow1\),
\[\boxed{\kappa_{n,k}(u)=\tfrac12 k^2(n-k)^2(1-u)+O_n((1-u)^2)},\]
so the **unique least-curved frequency**, again up to conjugacy, is \(k=1\) for all sufficiently large \(u<1\). For every \(n\ge5\), continuity therefore forces at least one genuine change of the least-curved angular Fourier mode at an intermediate radius. No uniqueness or explicit location of this transition is asserted.

## Assumptions and scope
The zeros have exactly the same modulus \(r\) and may move only in angle. An overall unimodular factor multiplying \(B\) is irrelevant. The boundary measure is normalized Lebesgue angular measure. All angular perturbations are real and sufficiently small so the zeros remain distinct. The discrete Fourier transform is unitary. The zero Fourier mode represents joint rotation. The spectral theorem concerns local conditioning, not radial perturbations or unrestricted zero placement. It covers \(n\ge5\) only; a separate record treats the degree-four local spectrum. The primary classification is MSC2020 \(30J10\), finite Blaschke products.

## Proof
**Reduction to Poisson power sums.** For \(|z|=1\), the covering speed of a finite Blaschke product is the sum of the Poisson kernels centered at its zeros:
\[
|B'(e^{it})|=\sum_{j=0}^{n-1}\frac{1-r^2}{|e^{it}-re^{i\theta_j}|^2}
=\sum_{j=0}^{n-1}\sum_{m\in\mathbb Z}r^{|m|}e^{im(t-\theta_j)}.
\]
Put \(S_m(\theta)=\sum_j e^{im\theta_j}\). Parseval, including the vanishing mean of the centered speed, gives the absolutely and smoothly convergent formula
\[\mathcal V_{n,r}(\theta)=2\sum_{m\ge1}u^m|S_m(\theta)|^2.\]
At the regular configuration \(S_m=n\) when \(n\mid m\) and zero otherwise, giving \(2n^2u^n/(1-u^n)\). The series and all its angular derivatives converge uniformly for each fixed \(u<1\).

**The exact Hessian and normalization.** Write \(\theta=\theta^*+s\varepsilon\) and assume \(\sum_j\varepsilon_j=0\), since the functional is invariant under a common angular shift. At the regular configuration, the coefficient of \(s^2\) in \(|S_m|^2\) is
\[
m^2\left[\left|\sum_j e^{2\pi imj/n}\varepsilon_j\right|^2
-\mathbf 1_{n\mid m}\,n\sum_j\varepsilon_j^2\right].
\]
The residue-class sums of \(m^2u^m\) are exactly
\[\sum_{\ell\ge0}(\ell n+k)^2u^{\ell n+k}=A_{n,k}(u)\quad(1\le k<n),\qquad
\sum_{\ell\ge1}(\ell n)^2u^{\ell n}=A_{n,0}(u).\]
Parseval for the discrete transform, followed by pairing the conjugate frequencies (the perturbations are real), yields
\[
[s^2]\,\mathcal V_{n,r}(\theta^*+s\varepsilon)
=\sum_{k=1}^{n-1}n\left(A_{n,k}+A_{n,n-k}-2A_{n,0}\right)|\widehat\varepsilon_k|^2.
\]
This is the claimed expansion and identifies the **half-Hessian coefficients**. The first derivative vanishes by cyclic symmetry and rotation invariance. Analyticity in angles gives the cubic remainder in the orthogonal complement of rotations.

**Strict positivity for every radius and degree.** Write \(u=e^{-x}\), \(t=nx/2\), \(a=k/n\in(0,1)\) and define
\[G_a(t)=\frac{\sinh(at)\sinh((1-a)t)}{\sinh t}.
\]
The two-sided residue sums satisfy the exact identity
\[
\frac{e^{-kx}+e^{-(n-k)x}-1-e^{-nx}}{1-e^{-nx}}=-2G_a(t).
\]
Differentiating twice with respect to \(x\) is legitimate for all \(x>0\); the left side's second derivative is \(A_{n,k}+A_{n,n-k}-2A_{n,0}\). Hence
\[\kappa_{n,k}(u)=-\frac{n^3}{2}G_a''(t).\]
To prove \(G_a''(t)<0\), observe the **parallel-sum identity**
\[
G_a(t)=F(\tanh(at),\tanh((1-a)t)),\qquad F(v,w)=\frac{vw}{v+w}.
\]
For positive \(v,w\), the map \(F\) is jointly concave and strictly increasing in each variable: its Hessian is
\[
D^2F(v,w)=-\frac2{(v+w)^3}
\begin{pmatrix}w^2&-vw\\-vw&v^2\end{pmatrix},
\]
which is negative semidefinite, and \(\partial_vF=w^2/(v+w)^2>0\), \(\partial_wF=v^2/(v+w)^2>0\). Since both \(\tanh(at)\) and \(\tanh((1-a)t)\) have strictly negative second derivatives for \(t>0\), the chain rule shows \(G_a''(t)<0\). Thus every \(\kappa_{n,k}(u)>0\) for all \(0<u<1\).

**End regimes and compulsory mode switching.** For \(k\in\{1,\ldots,\lfloor n/2\rfloor\}\), the rational formula has first positive terms \(A_{n,k}=k^2u^k+O_n(u^{k+n})\), \(A_{n,n-k}=(n-k)^2u^{n-k}+O_n(u^{2n-k})\), and \(A_{n,0}=O_n(u^n)\). This gives the stated small-\(u\) asymptotics, including the factor two at the even Nyquist index. As there are only finitely many frequencies at fixed \(n\), the central one is strictly least curved for all sufficiently small \(u\).

For \(t\downarrow0\), ordinary hyperbolic Taylor expansions yield
\[
G_a(t)=a(1-a)t-\frac{a^2(1-a)^2}{3}t^3+O_a(t^5),\qquad
G_a''(t)=-2a^2(1-a)^2t+O_a(t^3).
\]
Substituting \(t=-(n/2)\log u\) produces
\[\kappa_{n,k}(u)=\frac{k^2(n-k)^2}{2}(-\log u)+O_n((\log u)^3)
=\frac{k^2(n-k)^2}{2}(1-u)+O_n((1-u)^2).\]
The function \(k\mapsto k(n-k)\) is strictly increasing on the integer range \(1\le k\le\lfloor n/2\rfloor\), establishing the near-boundary first-mode minimum. For \(n\ge5\), the two minimizing mode sets differ. Continuous eigenvalues on \((0,1)\) cannot change their minimizing index without at least one tie between distinct real Fourier mode types. The result claims existence, not uniqueness, of such a crossing.

## Verification
Run the standalone standard-library script `check_hessian.py` using `python3 check_hessian.py` beside this file. It checks the rational spectral formula, positivity, conjugate-pair symmetry, the regular-polygon variance, and angular finite differences of the independent pairwise Poisson-autocorrelation formula. A package-local run passed 1,399 finite diagnostics for sizes \(5\le n\le17\). The strict infinite-parameter positivity and asymptotic ordering are proven symbolically above; finite tests do not certify infinitely many cases.

## Relationship to prior work
The minimizing configuration itself is covered by Cohn and Kumar's universal-optimality theorem for sharp spherical configurations. Indeed, summing the Poisson series with parameter \(u=r^2\) gives
\[
\mathcal V_{n,r}(\theta)=\sum_{i,j} f_u(|e^{i\theta_i}-e^{i\theta_j}|^2)-n^2,\qquad f_u(s)=\frac{1-u^2}{(1-u)^2+us}.
\]
The diagonal terms are constant, and \(f_u\) is strictly completely monotone in squared chordal distance. A regular \(n\)-gon on \(S^1\) has \(\lfloor n/2\rfloor\) distinct nonzero distances and is an \((n-1)\)-design, so it is sharp in the sense of that theorem. This gives global energy minimality for distinct equiradial zeros. The contribution here is the exact radius-dependent quadratic spectrum and the reversal of the least-curved mode, not the minimizing configuration. Global minimality alone does not give the spectrum or the frequency comparison.

Kovalev and Yang (arXiv:2007.09760v1, 2020) investigate minimum and maximum boundary derivatives and classify extremizers by hypergeometric polynomials. Gluchoff and Hartmann (2013) study Hardy means and derivative integral estimates; the available transcription of their Section 4 concerns means of \(1-|B(\rho e^{it})|^2\) for degrees two and three. Neither comparison addresses the same fixed-equiradial boundary variance spectrum. A separate degree-four result gives the spectrum and uniqueness of that case's stiffness crossover. The theorem here concerns \(n\ge5\) and does not assert uniqueness of a crossover.

The results *Full Fourier Hessian spectrum and sharp local stability for equispaced Bergman poles* and *Nyquist-mode softening of the cubically weighted Bergman pole Hessian* concern **boundary-pole weighted Bergman norms**, not the boundary-speed variance of finite Blaschke products with interior equiradial zeros. Their coefficient sequences are algebraically decaying Bergman moments, rather than the present geometric Poisson sequence \(u^m\); in particular their discrete-convexity proof does not apply to \(m^2u^m\), which changes discrete curvature.

## Limitations
The quantitative result concerns equal-radius angular perturbations for each fixed \(n\ge5\) and \(0<r<1\); neither the number nor the exact locations of intermediate modal crossings are determined. The displayed asymptotics are for fixed \(n\) and are not uniform in growing \(n\). Older circular-potential energy literature and the available 2013 transcription remain historical-priority risks for the exact spectral result.

## References
- H. Cohn and A. Kumar, *Universally optimal distribution of points on spheres*, J. Amer. Math. Soc. 20 (2007), 99–148, §1, https://arxiv.org/abs/math/0607446.
- *A unique angular stiffness crossover for four equiradial Blaschke zeros*, Resultary record a712e5339c70.
1. L. V. Kovalev and X. Yang, *Extreme values of the derivative of Blaschke products and hypergeometric polynomials*, arXiv:2007.09760v1, first public 2020-07-19, https://arxiv.org/abs/2007.09760 (primary MSC 30J10).
2. A. Gluchoff and F. Hartmann, *Hardy Means of a Finite Blaschke Product and Its Derivative*, Fields Institute Communications 65 (2013), DOI:10.1007/978-1-4614-5341-3_9.
3. *Full Fourier Hessian spectrum and sharp local stability for equispaced Bergman poles*, Resultary record 9aca32c3cb4f.
4. *Nyquist-mode softening of the cubically weighted Bergman pole Hessian*, Resultary record efc85019d6aa.
