# A universal sharp logarithmic equatorial cusp for positive-definite Legendre series

## Finding

Fix any \(A>0\) and \(\delta>0\). Suppose \((a_j)_{j\ge0}\) is a sequence of nonnegative reals satisfying
\[
a_j=A(j+1)^{-3/2}+O((j+1)^{-3/2-\delta})\qquad(j\to\infty).
\]
With \(P_n\) the classical Legendre polynomial, normalized by \(P_n(1)=1\), define
\[
\Phi(\theta)=\sum_{j=0}^\infty a_jP_{4j+1}(\cos\theta),\qquad0\le\theta\le\pi.
\]
This is a continuous isotropic positive-definite covariance kernel on the two-sphere. At the equator it has the **sharp two-sided logarithmic cusp**
\[
\boxed{\Phi(\pi/2+h)=-A\sqrt{8/\pi}\;h\log(1/|h|)+O(|h|),\qquad h\to0.}
\]
In particular, it is not Lipschitz at the equator and
\[
\lim_{h\to0}\frac{\Phi(\pi/2+h)-\Phi(\pi/2)}{h\log(1/|h|)}=-A\sqrt{8/\pi}.
\]
For the normalized sequence \(a_j=(j+1)^{-3/2}/\zeta(3/2)\), the coefficient is \(\sqrt{8/\pi}/\zeta(3/2)=0.610849862141250\ldots\). A positive real-analytic Legendre generating kernel can be added to make the covariance **strictly** positive definite, without changing the unnormalized cusp coefficient.

## Assumptions and scope

Only the standard two-sphere \(S^2\) and colatitude \(\theta\) are considered. The error term in the sequence hypothesis may have a constant depending on the sequence. The \(O(|h|)\) constant may depend on \(A,\delta\) and that sequence. The sharpness means the leading quotient is exact for this class; it is not an extremal assertion over all spherical positive-definite functions.

The series is uniformly absolutely convergent since \(|P_n(x)|\le1\) on \([-1,1]\) and \(\sum a_j<\infty\). Nonnegative Legendre coefficients give positive definiteness by the addition theorem. Each \(P_{4j+1}\) is odd, so \(\Phi(\pi/2)=0\) and \(\Phi(\pi/2+h)=-\Phi(\pi/2-h)\).

## Proof

**1. An interior Legendre bound with derivatives.** For \(n\ge1\), the classical Laplace integral representation is
\[
P_n(\cos\theta)=\frac1\pi\int_0^\pi(\cos\theta+i\sin\theta\cos u)^n\,du.
\]
On the fixed interval \(\theta\in[\pi/3,2\pi/3]\), the modulus squared of the integrand's base equals \(1-\sin^2\theta\sin^2u\le1-c\sin^2u\), for some absolute \(c>0\). Differentiating its \(n\)-th power at most three times produces sums with coefficients \(O_k(n^k)\), times powers of the base of order at least \(n-k\). Gaussian endpoint estimates for the integral therefore give, uniformly there,
\[
\left|\frac{d^k}{d\theta^k}P_n(\cos\theta)\right|\le C_k n^{k-1/2},\qquad k=0,1,2,3.
\]
For the finitely many \(n<k\), the same estimate follows by enlarging \(C_k\). This proves all derivative bounds directly without a differentiated asymptotic expansion.

**2. Exact central slope.** Legendre parity gives \(P_{4j+1}(0)=0\). Rodrigues' formula yields
\[
P'_{4j+1}(0)=\frac{(4j+2)!}{2^{4j+1}(2j)!(2j+1)!}=\sqrt{\frac{8j}{\pi}}+O(j^{-1/2})\quad(j\to\infty).
\]
As \(\frac{d}{d\theta}P_{4j+1}(\cos\theta)|_{\theta=\pi/2}=-P'_{4j+1}(0)\), the coefficient assumption implies
\[
a_jP'_{4j+1}(0)=\frac{A\sqrt{8/\pi}}{j}+O\big(j^{-1-\min\{1,\delta\}}\big)\quad(j\ge1).
\]
Consequently,
\[
\sum_{j=0}^{J}a_jP'_{4j+1}(0)=A\sqrt{8/\pi}\log J+O(1).
\]

**3. Uniform control of the Taylor and high-frequency tails.** Put \(J=\lfloor|h|^{-1}\rfloor\) for \(0<|h|<1/10\). Since the odd Legendre terms have zero value and zero second angular derivative at \(\pi/2\), Taylor's theorem and the \(k=3\) bound yield
\[
\sum_{j\le J}a_jP_{4j+1}(\cos(\pi/2+h))=-h\sum_{j\le J}a_jP'_{4j+1}(0)+O\Big(|h|^3\sum_{j\le J}(j+1)\Big).
\]
The remainder is \(O(|h|^3J^2)=O(|h|)\). By the \(k=0\) bound, the remaining tail is
\[
\sum_{j>J}\big|a_jP_{4j+1}(\cos(\pi/2+h))\big|\le C\sum_{j>J}(j+1)^{-2}=O(J^{-1})=O(|h|).
\]
Insert the slope sum from step 2 and use \(\log J=\log(1/|h|)+O(|h|)\). This gives the asserted two-sided expansion and non-Lipschitz sharp limit.

**4. Strict positive definiteness without smoothing the cusp.** For each \(0<s<1\), the zonal kernel
\[
q_s(\theta)=\frac{1-s}{\sqrt{1-2s\cos\theta+s^2}}=(1-s)\sum_{n\ge0}s^nP_n(\cos\theta)
\]
is real analytic near the equator and has strictly positive Schoenberg coefficients at every degree. Hence \(\Phi+\varepsilon q_s\), for \(\varepsilon>0\), is strictly positive definite on \(S^2\). Since \(q_s(\pi/2+h)=q_s(\pi/2)+O(h)\), its cusp coefficient is unchanged. If normalized to value one at zero, divide that coefficient by \(\Phi(0)+\varepsilon\).

## Verification

The accompanying `check.py` recomputes 80 central derivative identities by two independently specified formulas, numerically evaluates finite Legendre expansions at five positive equatorial offsets, checks odd reflection twice, and checks the logarithmic truncated-slope law at three truncation sizes. These 90 finite checks are reproducibility aids, not replacements for the uniform infinite-series proof above.

## Relationship to prior work

Yan Ge, *Optimal differentiability of isotropic positive definite functions on even-dimensional spheres* (arXiv:2608.26092, first posted 2026-08-26), gives the motivating sharp differentiability obstruction, using the sparse degrees \(4j+1\) with coefficients proportional to \((j+1)^{-3/2}\). The original full manuscript (arXiv HTML, Sections 4.1–4.3 and the remaining main theorem proof) establishes the seed series, exact individual central slopes, diverging weighted slope sum, and failure of the first equatorial derivative by Poisson regularization. It does not state the two-sided logarithmic cusp coefficient or its stability under faster-decaying positive coefficient perturbations. Its analytic strict-positive-definiteness modification is an established ingredient, not claimed new here.

Classical interior Legendre estimates (Szegő; NIST DLMF §18.15) and the standard Schoenberg positive-definiteness characterization are established inputs. Their combination with the critical coefficient tail yields the logarithmic constant; the standard asymptotic theory itself is not claimed as new. The theorem is about the exact equatorial modulus and its stability under summably faster coefficient perturbations, not about the known general differentiability bound.

## Limitations

The frequency support is restricted to degrees congruent to one modulo four, with a specified critical positive coefficient tail. No claim is made for arbitrary Legendre spectra, other spheres, a global best Hölder or Lipschitz constant, or optimality among all positive-definite spherical kernels. The closest primary manuscript was inspected in its full public HTML version; an older equivalent Tauberian/spectral result under another name remains an originality risk. Independent mathematical assessment has not occurred.

## References

1. Yan Ge, *Optimal differentiability of isotropic positive definite functions on even-dimensional spheres*, arXiv:2608.26092v1, 2026-08-26. https://arxiv.org/abs/2608.26092
2. NIST Digital Library of Mathematical Functions, §18.15 (Jacobi and Legendre asymptotics). https://dlmf.nist.gov/18.15
3. G. Szegő, *Orthogonal Polynomials*, 4th ed., AMS, 1975, §8.21.
4. I. J. Schoenberg, *Positive definite functions on spheres*, Duke Math. J. 9 (1942), 96–108.
5. P. W. Livermore, *The Spherical Harmonic Spectrum of a Function with Algebraic Singularities*, J. Fourier Anal. Appl. 18 (2012), 1146–1166, as background on singularity/spectral correspondence.
