# Exact planar contact law and a dimension ladder for proportional Brownian resetting

## Finding
Consider isotropic Brownian motion in Euclidean dimension \(d\geq 1\), with generator \(D\Delta\), interrupted by independent Poisson events of rate \(r>0\) at which the entire position vector is replaced by \(aX\), where \(-1<a<1\) and \(a\ne 0\). Set \(b=|a|\). The stationary law has a unique, bounded, infinitely differentiable density \(p_{d,b}\). Denote its value at the origin by \(P_d(b)=p_{d,b}(0)\).

**Exact dimension ladder.** For every integer \(d\geq1\) and every \(0<b<1\),
\[
P_{d+2}(b)=\frac{r}{2\pi Dd}\bigl(b^{-d}-1\bigr)P_d(b).
\]
The two-dimensional anchor is an exact elementary logarithm for the **entire** contraction range:
\[
P_2(b)=\frac{r}{2\pi D}\log\frac1b.
\]
Consequently, in every even dimension \(d=2n\), \(n\geq1\),
\[
P_{2n}(b)=\left(\frac rD\right)^n
\frac{2\pi^n}{\Gamma(n)(2\pi)^{2n}}
\log\frac1b\prod_{j=1}^{n-1}\bigl(b^{-2j}-1\bigr).
\]
The empty product for \(n=1\) equals one.

**Sharp almost-complete-reset singularity in every dimension.** Define
\[
C_d=\frac{2\pi^{d/2}}{\Gamma(d/2)(2\pi)^d}.
\]
As \(b\downarrow0\),
\[
P_{2n}(b)\sim\left(\frac rD\right)^n C_{2n}
 b^{-n(n-1)}\log\frac1b\qquad(n\geq1),
\]
whereas
\[
P_{2n+1}(b)\sim\left(\frac rD\right)^{n+1/2}
 C_{2n+1}\frac\pi2 b^{-n^2}\qquad(n\geq0).
\]
Thus every nonzero strict contraction regularizes the reset-point Green-kernel singularity, but its regularization breaks down according to a precise dimension-dependent power/logarithm hierarchy as \(b\to0\). The odd-dimensional integrals satisfy the additional exact relation \(I_{2n+1}(b)=I_1(b)\prod_{j=0}^{n-1}(b^{-(2j+1)}-1)\), where \(I_1\) is defined in the proof. The one- and three-dimensional limiting cases are included for completeness; the new dimensional statement is the exact planar anchor and the complete higher-dimensional ladder and hierarchy, not a priority claim for the already-established three-dimensional special case.

## Assumptions and scope
Here \(d\) is any fixed positive integer, \(D,r\) are arbitrary positive reals, the Brownian covariance is \(2DtI_d\), and every Poisson event acts synchronously on all coordinates by the scalar map \(X\mapsto aX\). All formulas concern the unique invariant law. When \(a<0\), central inversion does not alter that invariant law because the Brownian increments are symmetric. For \(b=0\), the canonical density is the resolvent of free Brownian motion at an exponential age; its limit at the origin is infinite in each \(d\geq2\). The formulas for \(b>0\) are not assigned a finite value at \(b=0\).

## Proof
**1. Existence, characteristic function, and regularity.** Take a two-sided stationary Poisson reset clock. Brownian increments on successive independent exponential intervals produce independent isotropic random vectors \(Z_j\) with characteristic functions
\[
\mathbb E e^{i k\cdot Z_j}=\bigl(1+D|k|^2/r\bigr)^{-1}.
\]
At a stationary observation instant the position has the convergent \(L^2\) representation \(X\overset{d}=\sum_{j=0}^{\infty}a^j Z_j\): the sum converges because \(|a|<1\) and \(\mathbb E|Z_j|^2=2dD/r\). Coupling processes with a common Brownian path and reset clock multiplies any initial displacement by \(a^{N_t}\), which tends to zero almost surely. This proves uniqueness. Symmetry of each \(Z_j\) makes the stationary law depend on \(a\) only through \(b=|a|\).

After changing Fourier variables by \(\sqrt{D/r}\), its radial characteristic function is
\[
\Phi_b(u)=\prod_{j=0}^{\infty}\frac{1}{1+b^{2j}u^2},
\qquad \Phi_b(bu)-\Phi_b(u)=u^2\Phi_b(u).
\]
The product converges uniformly on compact sets. For any integer \(m\), bounding it by its first \(m\) factors gives \(\Phi_b(u)=O_m(u^{-2m})\) as \(u\to\infty\). Fourier inversion therefore yields a bounded \(C^\infty\) density in every fixed dimension and permits all the radial moments used below.

**2. Dimension recurrence.** The exact central density is
\[
P_d(b)=\left(\frac rD\right)^{d/2}C_d I_d(b),\qquad
I_d(b)=\int_0^{\infty}u^{d-1}\Phi_b(u)\,du.
\]
Multiplying the characteristic-function identity by \(u^{d-1}\), integrating, and substituting \(v=bu\), gives
\[
I_{d+2}(b)=\int_0^{\infty}u^{d-1}
  [\Phi_b(bu)-\Phi_b(u)]\,du
 =(b^{-d}-1)I_d(b).
\]
Since \(C_{d+2}/C_d=1/(2\pi d)\), the asserted exact dimension ladder follows.

**3. Exact planar anchor.** The function \(\Phi_b\) is differentiable, positive and strictly decreasing from \(1\) to \(0\). By the identity in Step 1, Tonelli's theorem and the fundamental theorem of calculus,
\[
I_2(b)=\int_0^\infty\frac{\Phi_b(bu)-\Phi_b(u)}u\,du
=-\int_0^\infty\Phi_b'(v)\left(\int_v^{v/b}\frac{du}{u}\right)dv
=\log\frac1b.
\]
(The inner range \(v\leq u\leq v/b\) follows from \(bu\leq v\leq u\).) The exact \(P_2\) formula now follows from \(C_2=1/(2\pi)\), and successive applications of Step 2 establish the even-dimensional product without approximation.

**4. Odd-dimensional sharp coefficient.** For \(d=2n+1\), \(n\geq0\), the recurrence in Step 2 yields the **exact** formula
\[
 I_{2n+1}(b)=I_1(b)\prod_{j=0}^{n-1}\bigl(b^{-(2j+1)}-1\bigr).
\]
The integrand for the one-dimensional anchor obeys \(0<\Phi_b(u)\leq (1+u^2)^{-1}\). For fixed \(u\), the factors with index \(j\geq1\) converge uniformly as \(b\downarrow0\) to one, so \(\Phi_b(u)\to(1+u^2)^{-1}\). Dominated convergence gives \(I_1(b)\to\int_0^\infty(1+u^2)^{-1}du=\pi/2\). Because the sum of the odd integers from \(1\) to \(2n-1\) equals \(n^2\), the product has asymptotic \(b^{-n^2}\), proving the odd-dimensional coefficient. The even-dimensional asymptotic follows from the exact finite product. All limits are for fixed integer \(d\), \(D>0\), \(r>0\); no uniform-in-dimension estimate is claimed.

## Verification
Run `python3 verify.py` in the directory containing this document. The pure-standard-library checker numerically integrates the direct Fourier-product radial inversion in logarithmic frequency, tests the exact planar contact law, verifies the dimension recurrence and even-dimensional products in several dimensions and contraction regimes, and compares the small-contraction asymptotics. Its 38 deterministic comparisons passed. Numerical quadrature is corroboration only; the exact identities and infinite-dimensional limits follow from the preceding algebra and dominated-convergence proof.

## Relationship to prior work
Biroli, Feld, Hartmann, Majumdar and Schehr (arXiv:2406.08387, first posted 12 June 2024) establish the one-dimensional stationary law for positive or negative rescaling and explicitly point to higher dimensions as a future problem. Pierce (arXiv:2204.07215, first posted 14 April 2022) treats the one-dimensional proportional-reset advection-diffusion and its moments. The present result does not claim the one-dimensional Fourier product as new. Three-dimensional Bessel resetting has a published small-contraction contact asymptotic with reset rate tied to contraction; the special \(d=3\) consequence here is consistent with it and is not separately claimed as new. The asserted distinction is the exact dimension-shift identity, the full planar logarithmic law, the all-even-dimensional closed forms, and the sharp all-dimensional parity hierarchy at arbitrary fixed reset rate.

## Limitations
No claim concerns target hitting times, angularly anisotropic contractions, non-Poisson reset clocks, dimensions growing with the contraction limit, or uniform error bounds for the asymptotics. Positive central density is a local diagnostic, not a proof of complete radial stochastic ordering. Prior results sharing the same basic Fourier product may permit alternative shorter derivations; publication priority remains subject to broader literature verification. Independent validation has not been performed.

## References
1. M. Biroli, Y. Feld, A. K. Hartmann, S. N. Majumdar and G. Schehr, *Resetting by rescaling: exact results for a diffusing particle in one-dimension*, arXiv:2406.08387 (first public version 12 June 2024), https://arxiv.org/abs/2406.08387.
2. J. K. Pierce, *An advection-diffusion process with proportional resetting*, arXiv:2204.07215 (first public version 14 April 2022), https://arxiv.org/abs/2204.07215.
3. M. Kolb and A. Wübker, *Brownian Motion With Partial Resetting Conditioned to Stay Positive*, *Bulletin of the London Mathematical Society* (2026), DOI 10.1112/blms.70314, https://doi.org/10.1112/blms.70314. Its three-dimensional Bessel special case is acknowledged rather than assigned new priority.
