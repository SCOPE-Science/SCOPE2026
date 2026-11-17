# A universal quarter-order Hilbert–Schmidt transition for integer-power Fock compositions

## Finding
For every integer \(m\ge1\), real \(\alpha>0\), real \(0<a<1\), and \(\gamma>0\), define
\[
c=\frac{\alpha(1-a^m)}2,\qquad
\psi_\gamma(z)=\sum_{k=0}^\infty\frac{(cz^m)^k}{\Gamma(k+1+\gamma)}
=\frac1{\Gamma(\gamma)}\int_0^1(1-t)^{\gamma-1}e^{ctz^m}\,dt,
\]
and the weighted composition \((T_\gamma f)(z)=\psi_\gamma(z)f(az)\) on the radial power-weight Fock Hilbert space \(\mathcal F^2_{\alpha,m}\) below. Then every \(T_\gamma\) is compact, but
\[
\boxed{T_\gamma\in\mathcal S_2\ \Longleftrightarrow\ \gamma>\frac14.}
\]
The threshold is independent of the integer power \(m\), including the sub-Gaussian linear radial weight \(m=1\), the Gaussian case \(m=2\), and all higher powers \(m\ge3\).

There is more precise information than Schatten membership. Let \(K_{\alpha,m}\) be the reproducing kernel, and define the exact nonnegative truncated Hilbert–Schmidt energy
\[
H_\gamma(R)=\int_{|z|\le R}|\psi_\gamma(z)|^2K_{\alpha,m}(az,az)\,d\mu_{\alpha,m}(z).
\]
Put
\[
C_{m,\gamma}=\frac{m^2\alpha a^{m-2}}{4\sqrt\pi}\,c^{-2\gamma-1/2}.
\]
For each fixed choice of the parameters, as \(R\to\infty\),
\[
\boxed{\begin{aligned}
0<\gamma<\tfrac14:&\quad H_\gamma(R)\sim\frac{C_{m,\gamma}}{m(\frac12-2\gamma)}R^{m(\frac12-2\gamma)},\\
\gamma=\tfrac14:&\quad H_{1/4}(R)\sim C_{m,1/4}\log R,\\
\gamma>\tfrac14:&\quad H_\gamma(\infty)-H_\gamma(R)\sim\frac{C_{m,\gamma}}{m(2\gamma-\frac12)}R^{-m(2\gamma-\frac12)}.
\end{aligned}}
\]
At the endpoint, \(C_{m,1/4}=m^2\alpha a^{m-2}/(4\sqrt\pi c)\). In addition, the squared Hilbert–Schmidt norm has the sharp parameter pole
\[
\boxed{\lim_{\gamma\downarrow1/4}(\gamma-\tfrac14)\|T_\gamma\|_{\mathcal S_2}^2
=\frac{m\alpha a^{m-2}}{8\sqrt\pi c}.}
\]
These truncated energies are spatial kernel integrals, not finite-rank spectral truncations or singular-value counting functions.

## Assumptions and scope
We use complex entire functions with normalized planar measure
\[
d\mu_{\alpha,m}(z)=\frac{m\alpha^{2/m}}{2\pi\Gamma(2/m)}e^{-\alpha|z|^m}\,dA(z),\qquad
\mathcal F^2_{\alpha,m}=\{f\text{ entire}:\int|f|^2\,d\mu_{\alpha,m}<\infty\}.
\]
The squared monomial norm and radial diagonal kernel are exactly
\[
\|z^n\|^2=\frac{\Gamma((2n+2)/m)}{\alpha^{2n/m}\Gamma(2/m)},\qquad
K_{\alpha,m}(w,w)=\Gamma(2/m)\sum_{n\ge0}\frac{\alpha^{2n/m}|w|^{2n}}{\Gamma((2n+2)/m)}.
\]
The integer assumption on \(m\) makes each power \(z^{mk}\) holomorphic and makes the angular orthogonality exact. \(a\) is strictly between zero and one; \(a=0\) is the unrelated finite-rank case. \(\alpha\), \(a\), \(m\), and \(\gamma\) are fixed when taking large-radius limits. The case \(m=2\) is included to exhibit the common formula, not claimed as a new compact/non-Hilbert–Schmidt existence result.

## Proof
**1. Entire weight and compactness.** The power series has infinite radius of convergence. Its beta-integral representation follows from expanding the exponential and using \(B(k+1,\gamma)=k!\Gamma(\gamma)/\Gamma(k+1+\gamma)\). With \(r=|z|\), the integral implies
\[
|\psi_\gamma(z)|\le e^{cr^m}/\Gamma(\gamma+1),\qquad
|\psi_\gamma(z)|e^{-cr^m}\le\frac1{\Gamma(\gamma)}\int_0^1u^{\gamma-1}e^{-cr^mu}\,du\le(cr^m)^{-\gamma}
\]
for \(r>0\). Since \(2c=\alpha(1-a^m)<\alpha\), the first bound implies \(\psi_\gamma\in\mathcal F^2_{\alpha,m}\). The second shows that the normalized composition profile
\[
|\psi_\gamma(z)|^2e^{\alpha(|az|^m-|z|^m)}=|\psi_\gamma(z)|^2e^{-2cr^m}
\]
is bounded and tends uniformly to zero at infinity. Changing variables gives a bounded embedding \(T_\gamma:\mathcal F^2_{\alpha,m}\to\mathcal F^2_{\alpha,m}\). To prove compactness directly, split the output norm into \(|z|\le R\) and \(|z|>R\). The tail is uniformly small on the input unit ball by the profile bound and the change of variable \(w=az\). On the disk, bounded input sets are relatively compact for the local uniform topology by the reproducing kernel and Montel's theorem; hence the restricted weighted \(L^2\) maps are compact. The full operator is their norm limit, so it is compact. This argument does not assume any Schatten membership.

**2. Hilbert–Schmidt energy and the kernel asymptotic.** Applying Tonelli's theorem to the monomial orthonormal basis yields the extended nonnegative identity
\[
\|T_\gamma\|_{\mathcal S_2}^2=\int_{\mathbb C}|\psi_\gamma(z)|^2K_{\alpha,m}(az,az)\,d\mu_{\alpha,m}(z).
\]
The standard positive-real Mittag–Leffler asymptotic for the displayed kernel (also used in Barik–Sen–Paul) gives, as \(r\to\infty\),
\[
K_{\alpha,m}(ar,ar)\sim\frac m2\Gamma(2/m)\alpha^{(m-2)/m}a^{m-2}r^{m-2}e^{\alpha a^m r^m}.
\]
This is valid for every integer \(m\ge1\), including \(m=1\), where the Mittag–Leffler function reduces to \(\sinh(\alpha ar)/(\alpha ar)\), and \(m=2\), where it reduces to a Gaussian exponential.

**3. An exact angular identity and its sharp saddle point.** Set \(x=cr^m>0\). Angular orthogonality of the mutually distinct monomials \(z^{mk}\) gives
\[
\int_0^{2\pi}|\psi_\gamma(re^{i\theta})|^2d\theta
=2\pi\sum_{k=0}^\infty\frac{x^{2k}}{\Gamma(k+1+\gamma)^2}.
\]
For every fixed \(\gamma>0\), Stirling's formula and a discrete Gaussian saddle at \(k=x\) give
\[
\boxed{e^{-2x}\sum_{k=0}^\infty\frac{x^{2k}}{\Gamma(k+1+\gamma)^2}
\sim\frac{x^{-2\gamma-1/2}}{2\sqrt\pi}.}
\]
For completeness, write \(k=x+y\sqrt x\). Uniformly on \(|k-x|\le x^{1/2+\varepsilon}\) with \(0<\varepsilon<1/6\), Stirling gives the summand multiplied by \(e^{-2x}\) as \((2\pi)^{-1}x^{-2\gamma-1}e^{-y^2}(1+o(1))\). The sum is a Riemann sum of mesh \(x^{-1/2}\), yielding \(\sqrt\pi\sqrt x\). The omitted tails are negligible by the strict convexity of \(k\log(k/x)-k+x\), with the far tail controlled by successive-term ratios \(x^2/(k+1+\gamma)^2\). The argument is uniform for \(\gamma\) in any compact subinterval of \((0,\infty)\).

**4. Integration, the three regimes and the pole.** Combining the kernel and angular asymptotics shows that the radial derivative of the truncated energy is
\[
H_\gamma'(r)\sim C_{m,\gamma}\,r^{m/2-1-2m\gamma}.
\]
The integral near zero is finite by continuity of the entire weight and reproducing kernel. Elementary tail integration therefore gives the three asserted sharp laws and the membership threshold \(\gamma>1/4\). The discrete-saddle estimate and the kernel estimate hold uniformly for \(\gamma\) near \(1/4\), with a power-decaying remainder; splitting the norm integral at a fixed large radius and applying Abelian integration to the tail yields
\[
\lim_{\gamma\downarrow1/4}(\gamma-\tfrac14)H_\gamma(\infty)
=\frac{C_{m,1/4}}{2m}=\frac{m\alpha a^{m-2}}{8\sqrt\pi c}.
\]
This proves the residue as well. None of the finite checks below is used to deduce any infinite-dimensional statement.

## Verification
The independent standard-library `checker.py` reconstructs the exact radial kernel from gamma-weighted monomials and the exact angular sum from the Mittag–Leffler coefficients; it compares their combined radial density against the proved leading coefficient at several powers and endpoint parameters. Run `python3 checker.py` from the package directory. All infinite statements follow from the displayed analytic proof; finite sum truncations and numerical diagnostics do not establish convergence, compactness or nonmembership.

## Relationship to prior work
Barik, Sen and Paul (2026) supply boundedness, compactness and Hilbert–Schmidt criteria for radial power-weight Fock spaces, and explicitly ask whether compactness forces Hilbert–Schmidt membership at a given power. Their general criterion and kernel asymptotic are acknowledged inputs, not claimed as new. Mengestie and Takele (2023) give general weighted-composition Schatten-integrability criteria for a faster-growth Fock-type regime; these also supply prior general membership tests. Neither inspected text evaluates the displayed Mittag–Leffler endpoint family or gives its uniform integer-power threshold and exact three-regime energy constants.

Published Gaussian Fock constructions already give compact non-Hilbert–Schmidt weighted compositions at \(m=2\): in particular, the indexed Fourier-edge theorems of October 18 and November 8, 2026. They are a definite prior for the Gaussian existence claim and its Fourier-endpoint asymptotics. They do **not** imply the exact angular coefficient identity for \(m=1\) or \(m\ge3\), or the new power-independent \(\gamma=1/4\) transition and radius-residue laws for those spaces. The present contribution is this genuinely different Mittag–Leffler integer-power family and the sharp cross-power asymptotic; not an assertion that the Gaussian compact/non-Hilbert–Schmidt phenomenon was unknown. A separate general theorem with an uninspected equivalent evaluation remains a possible bibliographic risk.

## Limitations
Only integer radial exponents \(m\ge1\), positive-real strict dilations and the displayed family are classified. There is no assertion for arbitrary real powers, translations, nonlinear composition maps, or Schatten classes other than \(\mathcal S_2\). The upper and lower spatial-energy asymptotics are not singular-value asymptotics. Constants are exact for the stated normalization; they are not asserted optimal in larger operator families. Scientific priority and proof have not been independently certified.

## References
1. S. Barik, A. Sen, K. Paul, *Weighted composition operators on weighted Fock spaces*, arXiv:2607.17170v1, publicly submitted July 19, 2026, Theorems 1.1–1.4 and Question 7.1. https://arxiv.org/abs/2607.17170
2. T. Mengestie, M. H. Takele, *Integral and Weighted Composition Operators on Fock-type Spaces*, Bulletin of the Malaysian Mathematical Sciences Society 46 (2023), article 80, especially Theorem 3.2. https://doi.org/10.1007/s40840-023-01476-4
3. T. Carroll, C. Gilmore, *Weighted composition operators on Fock spaces and their dynamics*, arXiv:1911.07254, first public November 17, 2019. https://arxiv.org/abs/1911.07254
4. *A compact non-Hilbert–Schmidt weighted composition operator on the Gaussian Fock space: an exact transition*, published October 18, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-a-compact-non-hilbert-schmidt-weighted-composition-operator-on-t--c96f19618671
5. *Fourier-edge compact Fock compositions with a sharp Schatten threshold*, published November 8, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-fourier-edge-compact-fock-compositions-with-a-sharp-schatten-thr--de96b5aa6020
