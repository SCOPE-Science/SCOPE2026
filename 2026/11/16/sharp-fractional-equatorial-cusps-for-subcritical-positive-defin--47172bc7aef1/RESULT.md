# Sharp fractional equatorial cusps for subcritical positive-definite Legendre spectra

## Finding
Fix any \(1<s<3/2\) and put \(\alpha=s-1/2\). A positive-definite spherical covariance with Schoenberg weights \(a_j=A(j+1)^{-s}+O((j+1)^{-s-\delta})\) on degrees \(4j+1\), where \(A,\delta>0\), has the universal fractional equatorial law
\[
\Phi(\pi/2+h)=-A C_s\operatorname{sgn}(h)|h|^{\alpha}+o(|h|^{\alpha}),\quad C_s=\frac{4^{\alpha}\Gamma(1-\alpha)\sin(\pi\alpha/2)}{\sqrt{2\pi}\,\alpha}>0.
\]
The complete subcritical interval \(1<s<3/2\) therefore produces every exact equatorial Hölder exponent in \((1/2,1)\), even though all the kernels are positive definite. This is a pointwise *sharp exponent* result, not simply an upper Hölder estimate.

## Assumptions and scope
Here \(P_n\) is the Legendre polynomial normalized by \(P_n(1)=1\). Let \((a_j)_{j\ge0}\) be any real nonnegative sequence with \(a_j=A(j+1)^{-s}+O((j+1)^{-s-\delta})\); the implicit constant is arbitrary and finitely many coefficients may be modified while retaining nonnegativity. Set \(\Phi(\theta)=\sum_{j\ge0}a_j P_{4j+1}(\cos\theta)\) for \(0\le\theta\le\pi\). Since \(s>1\), the series converges uniformly. Schoenberg's coefficient criterion yields an isotropic positive-semidefinite zonal kernel on \(S^2\), with no assertion of strict positive definiteness (all active degrees are odd). The coefficient mass is not required to be one; dividing by \(\sum a_j>0\) gives a normalized kernel. The index restriction \(4j+1\) makes \(\Phi(\pi/2)=0\) and \(\Phi(\pi/2-h)=-\Phi(\pi/2+h)\).

## Proof
Write \(\alpha=s-1/2\in(1/2,1)\). On any fixed compact neighborhood of the equator contained in \((0,\pi)\), the classical interior Legendre asymptotic, with its once-differentiated remainder, is
\[
P_n(\cos\theta)=\sqrt{\frac{2}{\pi n\sin\theta}}\cos((n+1/2)\theta-\pi/4)+E_n(\theta),
\quad \sup|E_n|=O(n^{-3/2}),\quad \sup|E_n'|=O(n^{-1/2}).
\]
The derivative estimate follows by differentiating the standard interior asymptotic expansion including its smooth next term; it is used only away from the poles. For \(n=4j+1\), \(j\ge1\), the cosine phase at \(\theta=\pi/2+h\) is \(-\sin((4j+3/2)h)\). The amplitude equals \((2\pi j)^{-1/2}(1+O(j^{-1})+O(h^2))\). The total change of the errors between the equator and \(\pi/2+h\) is \(O(|h|)\), since \(\sum_j a_j j^{-1/2}<\infty\); the \(j=0\) term and the changes in phase offsets and leading amplitudes contribute \(O(|h|)\) or smaller. Consequently
\[
\Phi(\pi/2+h)=-\frac1{\sqrt{2\pi}}\sum_{j\ge1}a_jj^{-1/2}\sin(4jh)+O(|h|).
\]
For the coefficient perturbation, use \(|\sin u|\le\min(|u|,1)\). Splitting the sum at \(j=|h|^{-1}\) bounds its effect by \(O(|h|^{\min(1,\alpha+\delta)}\log(2/|h|))\), which is \(o(|h|^{\alpha})\). Likewise replacing \((j+1)^{-s}\) by \(j^{-s}\) changes only an \(O(|h|)\) term. For \(h>0\), the main sum becomes
\[
\sum_{j\ge1}j^{-1-\alpha}\sin(4jh)\sim(4h)^\alpha I_\alpha,
\quad I_\alpha=\int_0^\infty t^{-1-\alpha}\sin t\,dt
=\frac{\Gamma(1-\alpha)\sin(\pi\alpha/2)}{\alpha}.
\]
The equivalence is the Riemann-sum limit after scaling \(t=4jh\), dominated near zero by \(t^{-\alpha}\) and at infinity by \(t^{-1-\alpha}\). The integral identity follows by integration by parts and the standard Euler sine-transform integral. For \(h<0\), oddness gives the stated signed limit. Positivity of \(C_s\) makes the quotient by \(|h|^\alpha\) approach a nonzero number on both sides. For any higher Hölder exponent \(\beta>\alpha\), the corresponding quotient diverges, while the displayed asymptotic proves local Hölder behavior of order \(\alpha\) at the equator. In particular the difference quotient is unbounded because \(\alpha<1\).

## Verification
A standalone script `check.py` evaluates the exact Legendre polynomial recurrence on two subcritical exponents at shrinking scales and compares with the displayed closed coefficient. The ratios converge toward one in the observed direction; they are checks on normalization and signs, not a substitute for the analytic asymptotic. The proof also checks the three boundaries: \(s>1\) ensures a summable positive-type expansion; \(s<3/2\) ensures \(\alpha<1\); \(s=3/2\) is excluded and has a different logarithmic law.

## Relationship to prior work
Greco and Marinucci (2026) motivate sparse isotropic spherical spectral models. Ge (2026), Section 4, established qualitative equatorial nondifferentiability for the critical \(s=3/2\) coefficients, not this open subcritical fractional range with its explicit gamma-function amplitude and robustness. Livermore (2012) treats the spectral signatures of *given* algebraic spherical singularities, whereas the present statement reconstructs a signed local singularity from a prescribed sparse nonnegative Schoenberg tail. The classical Darboux/Hilb and Abelian tools are acknowledged; originality is limited to the particular sharp synthesis in this positive-type family, not those tools or the general correspondence between spectral decay and regularity.

## Limitations
No claim is made for \(s\le1\) (the assumed tail ceases to be summable), for the logarithmic endpoint \(s=3/2\), for all possible sparse sets of degrees, or for global Hölder regularity away from the equator. Strict positive definiteness is not asserted without additional even-degree coefficients. An older equivalent converse Abelian theorem specialized to sparse Legendre series could subsume this result; the available source comparison does not establish such coverage. Independent validation has not been performed.

## References
1. G. Greco and D. Marinucci, *Sparsity for isotropic spherical random fields*, arXiv:2601.21535, first publicly posted 2026-01-29, https://arxiv.org/abs/2601.21535.
2. Y. Ge, *Optimal differentiability of isotropic positive definite functions on even-dimensional spheres*, arXiv:2608.26092, first publicly posted 2026-08-26, https://arxiv.org/abs/2608.26092.
3. P. W. Livermore, *The spherical harmonic spectrum of a function with algebraic singularities*, J. Fourier Anal. Appl. 18 (2012), 1146–1166, https://doi.org/10.1007/s00041-012-9236-3.
4. NIST Digital Library of Mathematical Functions, §18.15 (classical interior asymptotics for Legendre polynomials), https://dlmf.nist.gov/18.15.
