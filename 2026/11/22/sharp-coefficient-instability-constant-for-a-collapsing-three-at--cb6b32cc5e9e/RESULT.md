# Sharp coefficient-instability constant for a collapsing three-atom Fourier Kaczmarz system

## Finding
For \(0<\varepsilon<\pi/2\), put \(\mu_\varepsilon=(\delta_1+\delta_{e^{i\varepsilon}}+\delta_{e^{-i\varepsilon}})/3\) and let \(H_\varepsilon=L^2(\mu_\varepsilon)\). Apply the ordinary, unrelaxed sequential Kaczmarz reconstruction to the unit vectors \(e_n(\zeta)=\zeta^n\), starting at \(n=0\), with auxiliary vectors \(g_0=e_0\) and \(g_n=e_n-\sum_{k<n}\langle e_n,e_k\rangle g_k\), where the inner product is linear in its first entry. Define its optimal **absolute coefficient amplification** by
\[
C(\varepsilon)=\sup_{\|f\|_{H_\varepsilon}=1}\sum_{n=0}^{\infty}|\langle f,g_n\rangle|.
\]
Then \(C(\varepsilon)<\infty\) for every \(0<\varepsilon<\pi/2\), and the sharp collision law is
\[
\boxed{\lim_{\varepsilon\downarrow0}\varepsilon C(\varepsilon)=2\sqrt3.}
\]
Consequently the coefficient amplification diverges precisely at order \(\varepsilon^{-1}\) when the three equally weighted, symmetrically placed sampling atoms coalesce, even though every fixed positive separation gives absolutely convergent reconstruction.

## Assumptions and scope
The three atoms have equal weights \(1/3\); their counterclockwise positions are \(1,e^{i\varepsilon},e^{-i\varepsilon}\). We consider the fixed deterministic order \(e_0,e_1,e_2,\ldots\) of nonnegative Fourier characters, exact observations, and the specific Kaczmarz auxiliary coefficients. The phase-space norm is \(\|f\|^2=(|f_0|^2+|f_+|^2+|f_-|^2)/3\), with \(f_j=f(\zeta_j)\). The claim is a limiting sharp constant, not an exact closed formula for \(C(\varepsilon)\) at finite separation and not a noise-amplification assertion for other algorithms.

## Proof
**Normalized Cauchy coefficients.** Define \(M_f(z)=\frac13\sum_{j\in\{0,+,-\}}f_j/(1-z\overline{\zeta_j})\) and \(M_1=M_{(1,1,1)}\). For the stationary Fourier Kaczmarz system, the standard normalized-Cauchy-transform identity gives \(F_f(z):=M_f(z)/M_1(z)=\sum_{n\ge0}\langle f,g_n\rangle z^n\). It also follows directly from the auxiliary recursion by comparing the coefficients of \(M_1F_f=M_f\). Set \(c=\cos\varepsilon\) and \(a=(1+2c)/3\). Multiplying numerator and denominator by \(P(z)=(1-z)(1-e^{i\varepsilon}z)(1-e^{-i\varepsilon}z)\) gives
\[
 F_f(z)=\frac{N_f(z)}{Q(z)},\qquad Q(z)=1-2az+az^2=(1-a)+a(z-1)^2,
\]
\[
 N_f(z)=\frac13\left[f_0(1-2cz+z^2)+f_+(1-z)(1-e^{i\varepsilon}z)+f_-(1-z)(1-e^{-i\varepsilon}z)\right].
\]
Interchanging \(+\) and \(-\) just interchanges the two modes and does not affect the norm. For \(0<\varepsilon<\pi/2\), \(0<a<1\). The distinct poles are \(z_\pm=1\pm i\sqrt{(1-a)/a}\); let \(\lambda_\pm=1/z_\pm=a\mp i\sqrt{a(1-a)}\), with common modulus \(r=\sqrt a<1\). The partial fraction decomposition has a constant term plus \(A_+(f)/(1-\lambda_+z)+A_-(f)/(1-\lambda_-z)\), where the **exact residues** are
\[
 A_\pm(f)=-\frac{N_f(z_\pm)}{z_\pm Q'(z_\pm)}.
\]
Therefore \(\langle f,g_n\rangle=A_+(f)\lambda_+^n+A_-(f)\lambda_-^n\) for every integer \(n\ge1\), and \(\langle f,g_0\rangle=(f_0+f_++f_-)/3\). The strict inequality \(r<1\) establishes finiteness of the coefficient sum for every positive separation.

**Leading residue geometry.** Since \(1-a=\varepsilon^2/3+O(\varepsilon^4)\), the poles satisfy \(z_\pm=1\pm i\varepsilon/\sqrt3+O(\varepsilon^3)\), and \(r=1-\varepsilon^2/6+O(\varepsilon^4)\). Expanding the numerator at these poles gives, uniformly as a linear functional of \(f\),
\[
 A_\pm(f)=\pm\frac{i\varepsilon}{2\sqrt3}L_\pm(f)+O(\varepsilon^2)\|f\|,
\]
where the sign and the labeling of the plus/minus modes can be jointly reversed without affecting the argument, and one convenient choice is
\[
 L_+(f)=\frac23f_0+\left(-\frac13-\frac1{\sqrt3}\right)f_++\left(-\frac13+\frac1{\sqrt3}\right)f_-,
\]
\[
 L_-(f)=\frac23f_0+\left(-\frac13+\frac1{\sqrt3}\right)f_++\left(-\frac13-\frac1{\sqrt3}\right)f_-.
\]
These two real coefficient vectors are orthogonal in \(\mathbb C^3\) and have ordinary Euclidean squared length \(4/3\). Because the domain norm is the Euclidean norm divided by \(\sqrt3\),
\[
 |L_+(f)|^2+|L_-(f)|^2\le4\|f\|^2,
 \qquad |A_+(f)|^2+|A_-(f)|^2\le(\varepsilon^2/3+O(\varepsilon^3))\|f\|^2.
\]
Equality in the leading inequality can be achieved by a unit vector parallel to either coefficient vector, which annihilates the other leading linear functional.

**Sharp upper bound.** Write \(\lambda_\pm=r e^{\mp i\theta}\) with \(\theta=\varepsilon/\sqrt3+O(\varepsilon^3)\). Weighted Cauchy–Schwarz yields
\[
\sum_{n\ge1}r^n|A_+e^{-in\theta}+A_-e^{in\theta}|
 \le\frac r{1-r}\left((|A_+|^2+|A_-|^2)(1+O(\varepsilon))\right)^{1/2}.
\]
Indeed the mixed term in the squared weighted mean is bounded relative to the diagonal terms by \((1-r)/|1-r e^{2i\theta}|=O(\varepsilon)\). The \(n=0\) term is at most \(\|f\|\). Since \(r/(1-r)=6\varepsilon^{-2}(1+O(\varepsilon^2))\), the uniform estimate gives \(\limsup_{\varepsilon\downarrow0}\varepsilon C(\varepsilon)\le2\sqrt3\).

**Sharp lower bound.** Take the unit-norm real vector \(f=\frac{\sqrt3}{\|\ell_+\|_2}\ell_+\), where \(\ell_+\in\mathbb R^3\) is the coefficient vector defining \(L_+\) and \(\|\ell_+\|_2=2/\sqrt3\). Thus \(|L_+(f)|=2\), \(L_-(f)=0\), and the residues satisfy \(|A_+(f)|=\varepsilon/\sqrt3+O(\varepsilon^2)\), \(|A_-(f)|=O(\varepsilon^2)\). The reverse triangle inequality gives
\[
 \sum_{n\ge1}|\langle f,g_n\rangle|\ge (|A_+(f)|-|A_-(f)|)\frac r{1-r}
 =\frac{2\sqrt3+O(\varepsilon)}\varepsilon.
\]
Combining with the upper bound proves the claimed sharp limit.

## Verification
The standalone `check.py` computes \(F_f=N_f/Q\) independently from the auxiliary recursion, verifies exact pole formulas numerically for several separations and complex test inputs, checks the two leading linear functionals' orthogonality and the normalized extremizing vector, and tests the scaled coefficient-sum limit with explicit geometric tail bounds. Run `python3 check.py` with Python's standard library; the program reports a deterministic test count. Numerical checks supplement the analytic proof; they do not prove the infinite-dimensional or limiting assertions.

## Relationship to prior work
Berner, Herr, and Jorgensen (2026), Theorem 4.1, prove absolute and unconditional Fourier Kaczmarz reconstruction for all fixed finite atomic spectral measures, and their normalized-Cauchy-transform identity supplies the coefficient formula used here. Their result does not quantify the sharp coefficient amplification when the atoms collide. Existing published finite-atomic Fourier Kaczmarz work establishes root-polynomial exponential error rates and regular-polygon finite-step rigidity, but **error contraction is not coefficient \(\ell^1\) amplification**. The published planar Kaczmarz result gives an exact unconditionality and amplification criterion only in dimension two, not for this three-dimensional system. The published weak-bias regular-polygon result studies a growing number of atoms and one finite Kaczmarz cycle, not fixed-three-atom collision or an infinite coefficient sum. The present statement isolates the first genuinely three-dimensional symmetric collision and its sharp \(2\sqrt3\) constant.

## Limitations
Only the equal-mass symmetric three-atom family and the single collision limit are classified. In particular this does not describe arbitrary three-atom geometry, general atomic measures, finite-separation exact optimizers, noise perturbations, or nonstationary sampling. General rational-function and model-space theory provides the underlying tools; equivalence to a more general, less-indexed quantitative theorem remains a bibliographic risk. Independent mathematical review is not yet performed.

## References
1. C. Berner, J. E. Herr, and P. E. T. Jorgensen, *Frame Properties of Effective Stationary Sequences*, arXiv:2611.03358v1, first public 2 November 2026, https://arxiv.org/abs/2611.03358 (especially equation (2.2) and Theorem 4.1 in v2).
2. R. Haller and R. Szwarc, *Kaczmarz algorithm in Hilbert space*, Studia Mathematica 169 (2005), 123–132, https://doi.org/10.4064/sm169-2-2.
3. J. E. Herr and E. S. Weber, *Fourier Series for Singular Measures*, Axioms 6 (2017), 7, https://doi.org/10.3390/axioms6020007.
4. *Regular-polygon finite-step rigidity and an explicit spectral rate for Fourier Kaczmarz recovery*, published-finding corpus, 8 November 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-regular-polygon-finite-step-rigidity-and-an-explicit-spectral-ra--03f0340e1b7f.
5. *Exact unconditionality criterion and critical scales for planar Kaczmarz reconstruction*, published-finding corpus, 17 November 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-exact-unconditionality-criterion-and-critical-scales-for-planar--9be270cea601.
6. *A continuum spectral law for cyclic Fourier Kaczmarz under vanishing one-atom bias*, published-finding corpus, 17 November 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-a-continuum-spectral-law-for-cyclic-fourier-kaczmarz-under-vanis--dc7eecc4fd2f.
