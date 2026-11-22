# Finite knot positivity cones for signed periodic Poisson covariances

## Finding
Fix a Poisson radius \(0<r<1\), a harmonic stride \(k\in\mathbb N\), and a degree \(d\in\mathbb N\). Let
\[
P_r(t)=\frac{1-r^2}{1-2r\cos t+r^2}=\sum_{n\in\mathbb Z}r^{|n|}e^{int},\qquad
Q(t)=c_0+2\sum_{j=1}^dc_j\cos(jkt),
\]
with arbitrary **real, signed** coefficients \(c_0,\ldots,c_d\). Define the stationary circle kernel \(K(x,y)=P_r(x-y)Q(x-y)\), its Fourier coefficients \(a_n=\widehat {P_rQ}(n)\), the knot values \(u_j=a_{jk}\) for \(0\le j\le d\), and \(R=r^k\).

**Theorem (exact all-degree positive-type cone).** The kernel \(K\) is positive semidefinite on every finite collection of circle points if and only if the **exactly \(d+1\) inequalities**
\[
\boxed{u_0\ge0,\quad u_1\ge0,\quad\ldots,\quad u_d\ge0}
\]
hold. The map \((c_0,\ldots,c_d)\mapsto(u_0,\ldots,u_d)\) is a real linear isomorphism, so these inequalities are irredundant and the admissible cone is simplicial, with precisely \(d+1\) extreme rays.

Every intermediate Fourier coefficient is a positive linear interpolation of adjacent knots. More precisely, for \(0\le j<d\) and \(0\le s\le k\),
\[
a_{jk+s}=\frac{r^s-r^{2k-s}}{1-r^{2k}}\,u_j
 +\frac{r^{k-s}-r^{k+s}}{1-r^{2k}}\,u_{j+1},
\qquad a_n=r^{n-dk}u_d\quad(n\ge dk),\qquad a_{-n}=a_n.
\]
On the positive-type cone, **finite-site strict positive definiteness holds exactly when \(u_d>0\)**, whereas **uniform density of the reproducing-kernel Hilbert space in \(C(\mathbb T)\)** holds exactly when **all \(u_0,\ldots,u_d>0\)**.

The cone's extreme rays have a complete spectral stratification. For the ray \(u=e_j\), \(0\le j\le d\):
- \(j=0\): the Fourier support is \(\{n:|n|<k\}\), of exact finite rank \(2k-1\);
- \(1\le j<d\): the support is \(\{n:(j-1)k<|n|<(j+1)k\}\), of exact finite rank \(4k-2\);
- \(j=d\): the support is \(\{n:|n|>(d-1)k\}\), infinite-dimensional, strictly positive definite on finite distinct sites, and nonuniversal.

## Assumptions and scope
The circle is \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\); normalized Haar measure gives \(a_n=\int_{\mathbb T}P_r(t)Q(t)e^{-int}\,dm(t)\). Here \(r\) is strictly between zero and one, \(k,d\) are arbitrary **positive** integers, and coefficients \(c_j\) may be positive, zero, or negative; \(Q\) itself need not be positive definite or nonnegative pointwise. Positive semidefiniteness permits repeated sites and all complex coefficient vectors. Strict positive definiteness concerns all **distinct** finite site sets. The finite-rank counts are the ranks of the global Fourier integral operators, not assertions about fixed-size Gram matrices. \(C\)-universality means the RKHS is uniformly dense in the continuous complex-valued functions on the circle. The excluded Poisson endpoints \(r=0,1\) are not classified.

## Proof
**1. Fourier coefficient formula and discrete harmonicity.** Absolute uniform convergence of the Poisson series yields, for \(n\in\mathbb Z\),
\[
a_n=c_0r^{|n|}+\sum_{j=1}^dc_j\bigl(r^{|n-jk|}+r^{|n+jk|}\bigr).
\tag{1}
\]
Fix a gap \(jk\le n\le(j+1)k\), with \(0\le j<d\). Every sequence \(r^{|n-\ell k|}\) occurring in (1) solves the same homogeneous second-order recurrence
\[
a_{n+1}-(r+r^{-1})a_n+a_{n-1}=0
\]
at strictly interior integer positions of this gap, because no source index \(\ell k\) lies there. The unique recurrence solution with boundary values \(a_{jk}=u_j\) and \(a_{(j+1)k}=u_{j+1}\) has the displayed interpolation coefficients. They are nonnegative at \(s=0,k\) and strictly positive for both endpoints when \(0<s<k\). Beyond the final knot, every term of (1) is a scalar multiple of \(r^n\), giving \(a_n=r^{n-dk}u_d\) for \(n\ge dk\). Reflection in (1) gives \(a_{-n}=a_n\). The knot values therefore determine every Fourier coefficient.

**2. Explicit invertibility and irredundancy.** The unique original mask coefficients associated with an arbitrary real knot vector \(u\) are
\[
\begin{aligned}
c_0&=\frac{(1+R^2)u_0-2Ru_1}{1-R^2},\\
c_j&=\frac{(1+R^2)u_j-Ru_{j-1}-Ru_{j+1}}{1-R^2},\qquad1\le j<d,\\
c_d&=\frac{u_d-Ru_{d-1}}{1-R^2}.
\end{aligned}\tag{2}
\]
To verify (2) directly, write the knot transform from (1) as
\[
u_j=c_0R^j+\sum_{\ell=1}^{d}c_\ell\bigl(R^{|j-\ell|}+R^{j+\ell}\bigr),\quad 0\le j\le d.
\]
For interior \(j\), applying the second-difference operator \((1+R^2)u_j-Ru_{j-1}-Ru_{j+1}\) annihilates all the geometric terms except \((1-R^2)c_j\); at the reflected boundary \(j=0\), the analogous expression \((1+R^2)u_0-2Ru_1\) equals \((1-R^2)c_0\). At the final boundary, \(u_d-Ru_{d-1}=(1-R^2)c_d\). Since \(0<R<1\), these are finite, uniquely solvable identities. Thus (2) is the inverse linear map in all degrees, including \(d=1\). Since every knot vector occurs and nonnegative Fourier coefficients are determined by nonnegative knots, this map identifies the admissible coefficient cone with \(\mathbb R_{\ge0}^{d+1}\). Each of its \(d+1\) coordinate inequalities defines a genuine facet and each coordinate basis vector gives a distinct extreme ray.

**3. Positive definiteness.** Bochner's theorem for the compact circle identifies positivity of \(K(x,y)=F(x-y)\) on all finite site sets with nonnegativity of every Fourier coefficient of \(F\). Necessity of the \(d+1\) knot conditions follows immediately. Conversely, nonnegative knots make every coefficient nonnegative by the gap interpolation and final-tail formulas from step 1. This proves the exact finite test.

**4. Extreme-ray support and finite rank.** Substitute \(u=e_j\) in the interpolation formula. For \(j=0\), only the first interpolation gap contributes, with positive coefficients at integer frequencies \(0\le n<k\). For \(1\le j<d\), both adjacent gaps contribute, and exactly the positive indices strictly between \((j-1)k\) and \((j+1)k\) survive. For \(j=d\), the left-adjacent gap and every index \(n\ge dk\) survive. Reflection yields the stated supports and counts \(2k-1\), \(4k-2\), or an infinite tail. This also shows a sharp distinction between the final ray and the other \(d\) rays.

**5. Strictness and universality.** If \(u_d>0\), every \(a_n\) with \(|n|\ge dk\) is strictly positive. Suppose distinct circle sites \(x_1,\ldots,x_M\) and complex numbers \(v_j\), not all zero, gave zero kernel quadratic form. The nonnegative Fourier energy
\[
\sum_{n\in\mathbb Z}a_n\left|\sum_{j=1}^{M}v_je^{inx_j}\right|^2
\]
then forces \(\sum_jv_je^{inx_j}=0\) for all \(n\ge dk\). Taking any \(M\) consecutive such frequencies makes a Vandermonde system on pairwise distinct complex nodes \(e^{ix_j}\), which is invertible; hence every \(v_j=0\), a contradiction. Thus strict finite-site positivity holds. If \(u_d=0\), the positive spectrum is supported in \(|n|<dk\); the RKHS has finite dimension and the Gram matrix is singular for any larger distinct-site set. Finally, if all knots are positive, the interpolation gives \(a_n>0\) for all integers \(n\); the RKHS contains every character \(e^{int}\), and trigonometric polynomials are uniformly dense in \(C(\mathbb T)\). Conversely, if any knot is zero, the corresponding Fourier-character functional vanishes on the RKHS and prevents density. This proves both sharp classifications.

## Verification
The self-contained `checker.py` uses Python 3 standard-library exact rational arithmetic. It checks the inverse map (2), Fourier convolution formula (1), gap interpolation, final-tail equality, and every extreme-ray support profile at three rational radii, strides \(1\le k\le5\), and degrees \(1\le d\le6\). It also checks random signed rational masks and an explicit signed mask with Fourier support only at frequencies \(\pm2\). Executing `python3 checker.py` produced `PASS: 62027 exact-rational assertions`. Finite tests support the algebraic derivations but are **not** proofs for all real radii, arbitrary degrees, or all site configurations; those claims follow from the analytic proof above.

For the explicit signed example choose \(k=1\), \(d=3\), \(r=2/5\), and \(u=(0,0,1,0)\). Formula (2) defines real mask coefficients with at least one negative coefficient, but \(P_r(t)Q(t)=2\cos(2t)\) has nonnegative Fourier coefficients and is positive definite. This illustrates why the established product-of-two-positive-type-kernels criterion does not decide the present signed-mask problem.

## Relationship to prior work
The classical compact-circle Bochner–Herglotz criterion, the elementary geometric Green's function identity, and Vandermonde inversion are used, not claimed as novel. Bonfim, Guella and Menegatto (2018, arXiv:1803.03105, Sections 1–2) characterize strict positive definiteness for products of **two already positive-definite factors** on compact two-point homogeneous spaces; they do not classify signed harmonic masks that may fail positivity separately. Guella, Menegatto and Peron (2015, arXiv:1505.01169, Introduction and strictness results) develop general Fourier-support criteria for products of circles; they do not give these sharp coefficient-space knots, arbitrary-degree facets or extreme-ray spectra.

Related explicit kernel calculations include finite positive-type cones for **character-polynomial Abel kernels on \(SU(2)\)**, where a different compact group and coefficient sequence \((n+1)r^n\) yield an affine tail, not the geometric circle interpolation here; and a nonstationary **sum-coordinate** heat-kernel modulation criterion with Gaussian Fourier multipliers, distinct from the stationary \(P_r(x-y)Q(x-y)\) family. A separate two-dimensional torus mixed-harmonic model gives a two-facet cone with graph-incidence Gram singularities, not the present all-degree one-circle classification. These comparisons establish a mathematical gap between the statements, not absolute priority or uniqueness.

## Limitations
The exact finite certificate relies on the geometric Fourier spectrum \(r^{|n|}\) and a mask supported on the equally spaced harmonics \(0,k,\ldots,dk\). It does not extend as stated to heat multipliers \(e^{-tn^2}\), arbitrary irregular frequency supports, or higher-dimensional spheres. The inverse map is elementary and the proof is self-contained, but an equivalent description may already exist under the terminology of geometric covariance sequences, autoregressive precision matrices, or Toeplitz/Green-function interpolation; published novelty and priority are not independently established. No independent mathematical audit has been performed.

## References
1. Rafaela N. Bonfim, Jean C. Guella and Valdir A. Menegatto, *Strictly Positive Definite Functions on Compact Two-Point Homogeneous Spaces: the Product Alternative*, arXiv:1803.03105, first publicly submitted 22 February 2018, https://arxiv.org/abs/1803.03105.
2. Jean C. Guella, Valdir A. Menegatto and Ana P. Peron, *Strictly positive definite kernels on a product of circles*, arXiv:1505.01169, submitted 5 May 2015, https://arxiv.org/abs/1505.01169.
3. Compact-abelian Bochner–Herglotz theorem and finite Vandermonde interpolation: standard results used as stated.
