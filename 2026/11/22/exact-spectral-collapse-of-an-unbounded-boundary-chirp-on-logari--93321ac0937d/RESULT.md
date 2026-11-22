# Exact spectral collapse of an unbounded boundary chirp on logarithmic Bergman space

## Finding

Fix \(1/2<a<1\), let \(\gamma=a-1/2\), and put \(c>0\). Let \(\mathcal H_a\) be the analytic subspace of the radial probability space on the open unit disk with measure
\[
d\mu_a(z)=\frac{[-\log(|z|^2)]^{a-1}}{\Gamma(a)}\,d(|z|^2)\,\frac{d\theta}{2\pi},\qquad z=|z|e^{i\theta}.
\]
On analytic polynomials define the radial Toeplitz compression \(T_c f=P_a(\psi_c f)\), where \(P_a\) is the orthogonal analytic projection and
\[
\psi_c(z)=[-\log(|z|^2)]^{-\gamma}\exp\!\left(\frac{ic}{-\log(|z|^2)}\right).
\]
The value at the single point \(z=0\) is immaterial. Despite \(|\psi_c|\) being unbounded near the unit circle, each \(T_c\) extends uniquely to a compact normal operator in every Schatten class \(\mathcal S_p\), for every \(p>0\). Its complete monomial eigenvalue list is
\[
\boxed{\lambda_n(c)=\frac{\sqrt\pi}{\Gamma(a)}(n+1)^\gamma\exp\!\big[-\sqrt{2c(n+1)}+i\sqrt{2c(n+1)}\big],\quad n=0,1,2,\ldots.}
\]
Put \(A_a=\sqrt\pi/\Gamma(a)\). The sharp weak-oscillation limits are, for every fixed \(p>0\),
\[
\boxed{\lim_{c\downarrow0}c^{\gamma+1/p}\|T_c\|_{\mathcal S_p}=A_a\left[\frac{2^{-p\gamma}\Gamma(2p\gamma+2)}{p^{2p\gamma+2}}\right]^{1/p},}
\]
and
\[
\boxed{\lim_{c\downarrow0}c^\gamma\|T_c\|=A_a(2\gamma^2)^\gamma e^{-2\gamma}.}
\]
In contrast, the Toeplitz compression of the pointwise modulus has diagonal entries \(A_a(n+1)^\gamma\) and is unbounded. Thus any positive chirp strength yields an all-Schatten operator, whereas zero chirp strength yields an unbounded positive operator, with exact norm blow-up rates.

## Assumptions and scope

The radial variable is \(t=|z|^2\in(0,1)\), with \(u=-\log t\); no extension is asserted for boundary values of the symbol. The Gaussian radial measure is a probability measure because \(\int_0^\infty u^{a-1}e^{-u}\,du=\Gamma(a)\). The analytic Hilbert space has complete orthonormal basis \(e_n(z)=(n+1)^{a/2}z^n\), because \(\|z^n\|^2=(n+1)^{-a}\). Its reproducing kernel is the polylogarithmic series \(K_a(z,w)=\sum_{n\ge0}(n+1)^a(z\overline w)^n\) for \(|z|,|w|<1\).

Since \(\int|\psi_c|^2d\mu_a=\Gamma(1-a)/\Gamma(a)<\infty\), multiplication by \(\psi_c\) sends every polynomial into \(L^2(\mu_a)\). The initially densely defined Toeplitz compression therefore exists without distributional-symbol conventions. The operator at \(c=0\) is considered on this same initial polynomial domain and is not claimed bounded.

## Proof

**1. Exact diagonalization.** Rotation invariance makes distinct monomials orthogonal after radial multiplication. For \(N=n+1\), using the normalized monomial \(e_n\),
\[
\langle T_c e_n,e_n\rangle=\frac{N^a}{\Gamma(a)}\int_0^\infty u^{a-1-\gamma}\exp(-Nu+ic/u)\,du.
\]
Since \(a-\gamma=1/2\), the integrand has the integrable factor \(u^{-1/2}\) near zero. The familiar Gaussian-Laplace identity, valid for \(N>0\) and \(\operatorname{Re}\beta>0\), is
\[
\int_0^\infty u^{-1/2}e^{-Nu-\beta/u}\,du=\sqrt{\frac\pi N}\,e^{-2\sqrt{N\beta}}.
\]
For completeness, set \(u=x^2\), differentiate the resulting integral \(F(b)=\int_0^\infty e^{-Nx^2-b^2/x^2}dx\) in \(b>0\), and substitute \(x\mapsto b/(\sqrt N x)\) to obtain \(F'(b)=-2\sqrt N F(b)\). The value \(F(0)=\sqrt\pi/(2\sqrt N)\) gives the identity for real \(\beta=b^2>0\); holomorphic continuation gives it for \(\operatorname{Re}\beta>0\). Taking \(\beta=\varepsilon-ic\), then \(\varepsilon\downarrow0\), is justified by dominated convergence since \(u^{-1/2}e^{-Nu}\) is integrable. The principal square root \(\sqrt{-icN}=(1-i)\sqrt{cN/2}\) yields the displayed eigenvalues exactly.

**2. Compactness and Schatten membership.** The compression on polynomials equals the diagonal map on the orthonormal monomials; its eigenvalues have moduli
\[
|\lambda_n(c)|=A_a N^\gamma e^{-\sqrt{2cN}}.
\]
For each \(c>0\) these numbers tend to zero and have finite \(p\)-sum for every \(p>0\). Therefore the diagonal map extends uniquely to a compact normal operator and lies in every Schatten quasi-ideal, with its exact nonzero singular-value multiset given by these moduli. This requires no assumption that the displayed values are already sorted by magnitude.

**3. Sharp small-chirp laws.** Exactly,
\[
\|T_c\|_{\mathcal S_p}^p=A_a^p\sum_{N=1}^\infty N^{p\gamma}e^{-p\sqrt{2cN}}.
\]
Set \(x=cN\). Continuity, integrability at zero (since \(p\gamma>0\)), and exponential decay at infinity justify the Riemann-sum limit
\[
\lim_{c\downarrow0}c^{1+p\gamma}\sum_{N\ge1}N^{p\gamma}e^{-p\sqrt{2cN}}
=\int_0^\infty x^{p\gamma}e^{-p\sqrt{2x}}dx
=\frac{2^{-p\gamma}\Gamma(2p\gamma+2)}{p^{2p\gamma+2}}.
\]
The discrete supremum obeys the analogous lattice-to-continuum maximum principle. The function \(x^\gamma e^{-\sqrt{2x}}\) is continuous on \([0,\infty)\), vanishes at both ends, and has its unique maximum at \(x=2\gamma^2\), with value \((2\gamma^2)^\gamma e^{-2\gamma}\). This proves both limit constants.

**4. The modulus contrast.** Repeating the radial moment calculation with \(|\psi_c|=u^{-\gamma}\) gives
\[
\langle P_a(|\psi_c|e_n),e_n\rangle=\frac{N^a}{\Gamma(a)}\int_0^\infty u^{-1/2}e^{-Nu}du=A_aN^\gamma\longrightarrow\infty.
\]
Consequently its compression on polynomials has no bounded extension. At \(c=0\), the original symbol equals this modulus. No property of a putative bounded extension at zero is being assumed.

## Verification

The included `checker.py` numerically verifies the damped Gaussian integral independently by Simpson quadrature in logarithmic coordinates for nine complex parameters, checks monomial normalization and modulus moments, compares 15 explicit complex eigenvalues with their phase-radius factors, and tests four small-\(c\) Schatten asymptotic constants and the operator-norm constant. It reports 37 passed finite checks. The infinite spectral and norm statements follow from the preceding exact integral and convergence arguments, not from the finite checks.

## Relationship to prior work

Hagger, Liu, Taskinen and Virtanen (first preprint 9 November 2020, arXiv:2011.04699) prove general sufficient criteria for bounded/compact Toeplitz operators with locally integrable, possibly violently oscillatory symbols, and exhibit radial examples whose modulus grows arbitrarily fast. This establishes the qualitative cancellation phenomenon as known. The claim here is the exact complex monomial spectrum and every sharp small-chirp Schatten/quasi-Schatten constant for the specified logarithmic radial measure, neither of which follows quantitatively from those general criteria.

Karapetyants and Taskinen (2022) treat radial Toeplitz symbols on broad analytic function spaces. Their general framework motivates distinguishing the known diagonal-moment mechanism from the particular spectral evaluation and singular-parameter limits here. Its publisher abstract is available, but the author manuscript could not be accessed in this comparison; a possible exact overlap not visible in the abstract remains a priority risk. Earlier radial Toeplitz results and nearby Gaussian-Fock and ordinary Bergman boundary-chirp spectra do not directly yield the present logarithmic-weight formulas or the sharp \(c\downarrow0\) constants.

## Limitations

The exact elementary identity uses the linked exponents \(\gamma=a-1/2\) and \(1/2<a<1\); neither a classification for arbitrary radial symbols nor analogous formulas for all \(a>0\) are claimed. These are same-author mathematical checks only; there has been no independent mathematical validation or historical-priority certification. The 2022 general-analytic-space full text and some specialized published spectra were not completely accessible, so originality is asserted only against the materially inspected and indexed sources.

## References

- R. Hagger, C. Liu, J. Taskinen, J. A. Virtanen, *Toeplitz operators on the unit ball with locally integrable symbols*, arXiv:2011.04699 (first public 9 November 2020); *Integral Equations and Operator Theory* **94** (2022), 17. https://arxiv.org/abs/2011.04699 ; https://doi.org/10.1007/s00020-022-02695-3
- A. Karapetyants, J. Taskinen, *Toeplitz Operators with Radial Symbols on General Analytic Function Spaces*, *Complex Analysis and Operator Theory* **16** (2022), 110. https://doi.org/10.1007/s11785-022-01294-9
- J. Taskinen, J. A. Virtanen, *Toeplitz operators on Bergman spaces with locally integrable symbols*, *Revista Matemática Iberoamericana* **26** (2010), 693–706. https://doi.org/10.4171/RMI/614
