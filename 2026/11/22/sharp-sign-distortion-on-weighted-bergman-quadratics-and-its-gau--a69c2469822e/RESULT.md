# Sharp sign distortion on weighted Bergman quadratics and its Gaussian limit

## Finding
Fix a real parameter \(\beta>1\). Equip the disk with the probability measure
\[
 d\mu_\beta(z)=\frac{\beta-1}{\pi}(1-|z|^2)^{\beta-2}\,dA(z),
\]
and write \(\|f\|_{4,\beta}^4=\int_{|z|<1}|f(z)|^4d\mu_\beta(z)\). On the three-dimensional complex space \(\mathcal P_2=\{a+bz+cz^2:a,b,c\in\mathbb C\}\), let
\[
 U_\beta=\sup_{0\ne f\in\mathcal P_2}\max_{\sigma_j\in\{-1,1\}}
 \frac{\|\sigma_0a+\sigma_1bz+\sigma_2cz^2\|_{4,\beta}}{\|a+bz+cz^2\|_{4,\beta}}.
\]
For real \(s\), define
\[
 C_\beta=\sqrt{\frac{3(\beta+1)}{2(\beta+2)}},\quad
 A_\beta=\frac{3\beta}{\beta+2},\quad
 B_\beta=\frac{2(\beta+1)}{\beta+3},
\]
\[
 F_\beta(s)=2C_\beta\cosh s+
 \frac12\sqrt{4+A_\beta e^{2s}+B_\beta e^{-2s}}.
\]
The function \(F_\beta\) is strictly convex, tends to infinity at both ends, and has exactly one minimizer \(s_\beta<0\). Set \(\delta_\beta=1/F_\beta(s_\beta)\). Then
\[
 \boxed{\quad U_\beta^4=\frac{1+\delta_\beta}{1-\delta_\beta}.\quad}
\]
Moreover, \(\delta_\beta\) and \(U_\beta\) are strictly decreasing in \(\beta\). Their exact endpoint laws are
\[
 \lim_{\beta\downarrow1}\delta_\beta=\frac{2}{4+\sqrt6},\qquad
 \lim_{\beta\to\infty}\delta_\beta=
 \left[\min_{s\in\mathbb R}\left(\sqrt6\cosh s+
 \frac12\sqrt{4+3e^{2s}+2e^{-2s}}\right)\right]^{-1}.
\]
The latter constant is \(0.2534148054348824\ldots\) and the corresponding limiting sharp multiplier norm is \(1.1382924669654002\ldots\); the former norm limit is \(1.1738972041862846\ldots\). At the unweighted area measure \(\beta=2\), the sharp multiplier norm is \(1.1627952476990222\ldots\).

All norm-ratio maximizing polynomials have nonzero coefficients. Their magnitudes are uniquely determined up to a common positive factor: write
\[
 m_j=\frac{j!}{(\beta)_j},\quad
 t_\beta=\sqrt{\frac{6}{(\beta+1)(\beta+2)}}e^{s_\beta},\quad
 x_\beta=\sqrt{\frac{m_2}{t_\beta^2+4m_2+m_4/t_\beta^2}},
\]
where \((\beta)_j=\beta(\beta+1)\cdots(\beta+j-1)\) and \((\beta)_0=1\). The exact coefficient conditions are
\[
 \frac{|a|}{|b|}=\sqrt{x_\beta t_\beta},\qquad
 \frac{|c|}{|b|}=\sqrt{x_\beta/t_\beta},\qquad
 \frac{ac}{b^2}\in(-\infty,0).
\]
For these coefficients the sharp inequality is attained by any sign pattern with \(\sigma_0\sigma_2=-1\); the middle sign is arbitrary. Conversely, every nontrivial sharp equality arises this way. Independent equiprobable Rademacher signs have the sharp fourth-moment comparisons
\[
 1-\delta_\beta\ \le\ \frac{\|f\|_{4,\beta}^4}{\mathbb E\|\varepsilon_0a+\varepsilon_1bz+\varepsilon_2cz^2\|_{4,\beta}^4}
 \ \le\ 1+\delta_\beta,
\]
with the stated magnitudes and destructive or constructive relative phase, respectively. This is the first three-monomial resonance: on any two of the three monomials, every sign change preserves the fourth norm exactly.

## Assumptions and scope
The weight is the standard positive radial power weight, \(\beta>1\) (equivalently area-weight exponent \(\alpha=\beta-2>-1\)). Coefficients and the polynomial space are complex; sign multipliers are real \(\pm1\), not arbitrary phases, and the degree cutoff is exactly two. All extrema are over nonzero polynomials. The endpoint \(\beta=1\) is the limiting Hardy-circle measure and the \(\beta=\infty\) endpoint is a rescaled Gaussian/Fock limit, not finite members of the asserted disk family.

## Proof
**1. Exact moments and interference.** Rotational orthogonality gives \(\int z^k\overline z^\ell d\mu_\beta=0\) unless \(k=\ell\), and its diagonal entries are \(m_k=k!/(\beta)_k\). For \(f=a+bz+cz^2\), expanding \(f^2\) and using these moments gives
\[
 \|f\|_{4,\beta}^4=H+4m_2\operatorname{Re}(b^2\overline a\,\overline c),
\]
where
\[
 H=|a|^4+4m_1|ab|^2+m_2|b|^4+4m_2|ac|^2
   +4m_3|bc|^2+m_4|c|^4.
\]
The sign multiplier changes only the interference sign, by the factor \(\sigma_0\sigma_2\). Independent signs average the interference to zero. The optimal normalized interference, for coefficient magnitudes, is \(\delta=4m_2|ac||b|^2/H\). The sharp multiplier ratio for those magnitudes is \(((1+\delta)/(1-\delta))^{1/4}\), with destructive input phase and \(\sigma_0\sigma_2=-1\). Any vanished coefficient gives \(\delta=0\), so no sharp optimizer lies on a coordinate face.

**2. Reduction to one strictly convex variable.** Put \(v=|b|^2>0\), \(t=|a|/|c|>0\), and \(x=|ac|/v>0\), so \(|a|^2/v=xt\) and \(|c|^2/v=x/t\). Then
\[
 \frac{H}{v^2x}=\frac{m_2}{x}+4m_1t+\frac{4m_3}{t}
 +x\left(t^2+4m_2+\frac{m_4}{t^2}\right).
\]
The unique minimizing \(x\) is the displayed \(x_\beta\) with \(t\) substituted. Consequently
\[
 \frac1{\delta_\beta}=
 \min_{t>0}\left[\frac{m_1}{m_2}t+
 \frac{m_3}{m_2t}+\frac12\sqrt{\frac{t^2}{m_2}+4+\frac{m_4}{m_2t^2}}\right].
\]
The substitution \(t=\sqrt{6/((\beta+1)(\beta+2))}e^s\) is exactly \(F_\beta(s)\).

**3. Global uniqueness.** The first term \(2C_\beta\cosh s\) is strictly convex and coercive. The square-root term is also strictly convex: it is half the Euclidean norm of the vector \((2,\sqrt{A_\beta}e^s,\sqrt{B_\beta}e^{-s})\). The formula for the second derivative of a vector norm, together with Cauchy–Schwarz, bounds that second derivative from below by a positive multiple of \(A_\beta e^{2s}+B_\beta e^{-2s}\). Thus \(F_\beta\) has a unique global minimizer. For \(\beta>1\), \(A_\beta>B_\beta\) because their difference is \((\beta-1)(\beta+4)/((\beta+2)(\beta+3))\). Therefore \(F_\beta'(0)>0\), and strict convexity forces \(s_\beta<0\). Both the optimizing \(x\) and \(t\) are unique. Strict positivity of the norm implies \(0<\delta_\beta<1\).

**4. Strict weight monotonicity.** The functions \(C_\beta\), \(A_\beta\), and \(B_\beta\) each increase strictly with \(\beta>1\). Hence \(F_{\beta_2}(s)>F_{\beta_1}(s)\) at every \(s\) if \(\beta_2>\beta_1\). Evaluate this strict inequality at the minimizer of \(F_{\beta_2}\), then compare with the minimum of \(F_{\beta_1}\); the minima increase strictly. Hence \(\delta_\beta\) and \(U_\beta\) decrease strictly.

**5. Boundary limits.** At \(\beta\downarrow1\), the parameters converge to \(C_1=A_1=B_1=1\); symmetry and strict convexity give \(s_1=0\) and \(F_1(0)=2+\sqrt6/2\). At \(\beta\to\infty\), the three parameters converge to \(\sqrt{3/2},3,2\), respectively. Coercivity is uniform in \(\beta\ge1\), since \(C_\beta\ge1\). Thus minimizers stay in a common compact interval, every limit minimizes the limiting strictly convex function, and the stated constants follow. A direct rescaling \(z=w/\sqrt\beta\) yields the same limiting Gaussian monomial moments \(j!\), making the second endpoint a genuine Gaussian/Fock sign-distortion constant.

## Verification
The accompanying standard-library program `CHECK.py` is executable with `python CHECK.py`; it validates the fourth-moment expansion and Rademacher sign average by exact fractions at \(\beta=2\), directly evaluates all eight sign patterns for finite inputs, solves the unique stationarity equation by bisection for selected weights, tests the sharp coefficient ratios and both endpoint numerical values, and makes supplemental global grid comparisons. It passed 1,080 finite assertions. The proof, not the finite tests, establishes the all-parameter statements, strict convexity, global optimality, and limits.

## Relationship to prior work
Cheng, Fang and Liu (first public journal appearance 9 April 2021) studied Littlewood-type randomization in analytic Bergman spaces, focusing on membership and norm-continuity theorems. Wang (2023), Section 2, works with weighted Bergman randomization and proves qualitative inclusion and continuity criteria. Neither inspected accessible claim specifies the degree-two, fourth-power, exact two-sided sign-ratio constants or their strict weight monotonicity. Related fourth-moment optimization for weighted Bergman quadratics uses a different denominator (the second norm) and does not by its stated conclusion imply sharp comparison with the Rademacher-averaged fourth norm. The sharpness is a separate positive two-variable minimization. The earlier 2021 article was not available in complete text during the comparison, and priority remains best-knowledge rather than certified.

## Limitations
This result does not determine the full infinite-dimensional unconditional multiplier norm, higher-degree constants, or arbitrary unimodular (non-sign) multipliers. The original 2021 Cheng–Fang–Liu full text and complete repository files of several related fourth-moment results could not be inspected; no novelty beyond the specifically checked literature is certified. Numerical decimals are illustrations, not exact defining statements. There is no independent mathematical audit.

## References
1. G. Cheng, X. Fang and C. Liu, “A Littlewood-Type Theorem for Random Bergman Functions,” *International Mathematics Research Notices* 2022(14), 11056–11091, first published online 9 April 2021, https://doi.org/10.1093/imrn/rnab018.
2. C. Wang, “A Littlewood-type theorem for random weighted Bergman functions and random power series in \(\mathcal L_0^{2,\lambda}\) spaces,” *Filomat* 37(16) (2023), 5215–5224, https://doi.org/10.2298/FIL2316215W. Accessible full text: https://www.pmf.ni.ac.rs/filomat-content/2023/37-16/37-16-4-19486.pdf.
3. Published research records: “Persistent three-mode rigidity and a coalescing-root limit for weighted Bergman quadratics” (2026, published-finding corpus record `2026/10/25/SCOPE-persistent-three-mode-rigidity-and-a-coalescing-root-limit-for-w--1df75c4e4cbb`); “Strict three-mode mixing and the sharp high-weight correction for quadratic Bergman fourth moments” (2026, published-finding corpus record `2026/10/26/SCOPE-strict-three-mode-mixing-and-the-sharp-high-weight-correction-fo--9d0e2b39f308`). Full texts were not accessible in this comparison.
