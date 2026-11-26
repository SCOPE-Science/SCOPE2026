# A complete Poisson activation staircase on finite and infinite \(B_2\) Fourier spectra

## Finding

Let \(E=\{n_0,n_1,\ldots\}\subseteq\mathbb N_0\) be finite with at least two elements or countably infinite, strictly increasing with \(n_0=0\). Assume \(E\) is a \(B_2\) set: equality \(n_i+n_j=n_u+n_v\) for indices in \(E\) implies equality of the unordered index pairs. On the probability circle \(\mathbb T\), let \(T_\rho(z^n)=\rho^n z^n\), \(0<\rho<1\), be Poisson damping on the analytic Fourier space supported in \(E\). Define
\[
\mathcal K_E(\rho)=\sup_{0\ne f\in H_E}\frac{\|T_\rho f\|_{L^4(\mathbb T)}^4}{\|f\|_{L^2(\mathbb T)}^4},\qquad
H_E=\overline{\operatorname{span}}^{L^2}\{z^{n_i}:n_i\in E\}.
\]
Thus \(\mathcal K_E(\rho)\) is the **fourth power** of the operator norm, not the operator norm itself.
Put \(w_i=\rho^{2n_i}\). There is a unique \(t=t(\rho)>0\) satisfying the **finite** sum equation
\[
\sum_{i:w_i>t}\left(1-\frac{t}{w_i}\right)=\frac12.
\]
Define \(D=\sum_{i:w_i>t}(w_i-t)/w_i^2\). Then
\[
\boxed{\mathcal K_E(\rho)=\frac{t}{D},\qquad
\frac{|\widehat f(n_i)|^2}{\|f\|_2^2}=\frac{(w_i-t)_+}{w_i^2D}.}
\]
Every maximizer has precisely these squared Fourier magnitudes, and **all phases on its nonzero coefficients are free**. In particular, every maximizer at \(\rho<1\) has finite spectral support, even if \(E\) is infinite.

There is a strictly increasing sequence of sharp mode-activation radii \(\rho_k\in(0,1)\) for \(1\le k<|E|\), each uniquely determined by
\[
\boxed{\sum_{i=0}^{k-1}\rho_k^{\,2(n_k-n_i)}=k-\frac12.}
\]
For \(\rho_{k-1}<\rho\le\rho_k\), where \(\rho_0=0\), the maximizing support is exactly \(\{n_0,\ldots,n_{k-1}\}\). Beyond the final threshold of finite \(E\), all its frequencies are active. Every threshold creates **exactly one** new mode, never several. For countably infinite \(E\), the radii satisfy \(\rho_k\uparrow1\); hence the unique magnitude profile activates infinitely many modes, one at a time, but finitely many at each \(\rho<1\).

At each activation the new squared amplitude vanishes linearly. More explicitly, put
\[
G_k(\rho)=\sum_{i<k}\rho^{2(n_k-n_i)}-\left(k-\frac12\right),\qquad
D_k=\sum_{i<k}\frac{w_i(\rho_k)-w_k(\rho_k)}{w_i(\rho_k)^2}.
\]
Then \(D_k>0\), and for \(\rho\downarrow\rho_k\) from above,
\[
\frac{|\widehat f(n_k)|^2}{\|f\|_2^2}
=\frac{G_k'(\rho_k)}{w_k(\rho_k)(k+\tfrac12)D_k}(\rho-\rho_k)
+O((\rho-\rho_k)^2).
\]
Consequently the coefficient *amplitude* has a square-root onset. If \(E\) is infinite, \(\mathcal K_E(\rho)\uparrow2\) as \(\rho\uparrow1\), but the endpoint sharp constant \(2\) at \(\rho=1\) is **not attained**. For finite \(E\) of size \(N\), \(\mathcal K_E(1)=2-1/N\), uniquely attained in magnitude by equal-energy coefficients.

## Assumptions and scope

The circle uses normalized Haar measure. Only nonnegative integer analytic frequencies are considered, with \(0\in E\). The unordered two-sum uniqueness condition is essential; midpoint resonances in non-\(B_2\) sets add phase-sensitive convolution terms. All input coefficients are complex, with no sign or phase constraints. For countably infinite \(E\), \(n_i\to\infty\); \(T_\rho\) is defined by its Fourier multipliers and convergence in \(L^2\), as well as in \(L^4\) for \(\rho<1\). No assertion is made about other exponents or arbitrary non-\(B_2\) spectra.

## Proof

**1. Exact fourth moment and compact attainment.** Write \(f(z)=\sum_i c_i z^{n_i}\) and normalize \(\sum_i|c_i|^2=1\). Set \(p_i=|c_i|^2\). Uniqueness of unordered pair sums and Parseval applied to \((T_\rho f)^2\) give the exact identity
\[
F_\rho(p):=\|T_\rho f\|_4^4
=2\left(\sum_iw_ip_i\right)^2-\sum_iw_i^2p_i^2.
\tag{1}
\]
For an infinite set the identity follows first for finite truncations, then by \(L^4\) convergence. Indeed, uniformly for \(\|f\|_2\le1\),
\[
\left\|\sum_{i\ge J}\rho^{n_i}c_iz^{n_i}\right\|_4
\le\sum_{i\ge J}\rho^{n_i}|c_i|
\le\left(\sum_{i\ge J}\rho^{2n_i}\right)^{1/2}\longrightarrow0.
\]
Thus \(T_\rho\) maps the \(L^2\) unit ball into a relatively compact subset of \(L^4\), with weak-to-strong sequential continuity. Weak compactness of the \(L^2\) ball supplies a maximizer. It lies on the unit sphere by homogeneous scaling. The finite case follows from ordinary compactness.

**2. An exact variational waterline.** On the nonnegative simplex, let \(p\) be any maximizer, and set \(S=\sum_iw_ip_i>0\). The derivative of (1) in coordinate \(i\) is \(4w_iS-2w_i^2p_i\). Transferring infinitesimal mass between an active coordinate and any other gives a common Lagrange multiplier \(\lambda\) at active coordinates and derivatives at most \(\lambda\) at inactive coordinates. Since \(F_\rho\) is homogeneous of degree two,
\[
\lambda=\sum_i p_i\partial_iF_\rho=2F_\rho(p)>0.
\]
Write \(t=\lambda/(4S)>0\). The stationarity and inactive inequalities imply
\[
p_i=2S\frac{(w_i-t)_+}{w_i^2}.
\tag{2}
\]
This holds for infinitely many coordinates as well, by the two-coordinate variations. Because \(w_i\to0\) for infinite \(E\), (2) has only finitely many positive entries. Multiplying (2) by \(w_i\) and summing gives the scalar equation \(\sum_{w_i>t}(1-t/w_i)=1/2\). Its left side is continuous and strictly decreasing on \((0,w_0)\), beginning at at least one and ending at zero (in the infinite case it diverges as \(t\downarrow0\)); therefore it has a unique solution. Summing (2) itself gives \(2SD=1\), hence the claimed unique \(p_i\). Euler's identity gives \(F_\rho=\lambda/2=2St=t/D\). Since an optimizer exists and every optimizer must obey this uniquely solved system, the formula is globally sharp; arbitrary coefficient phases do not affect (1).

**3. Sharp sequential activation.** For an active initial segment of length \(k\), the waterline is
\[
t_k(\rho)=\frac{k-\tfrac12}{\sum_{i<k}w_i^{-1}}.
\]
The boundary of the next frequency is \(t_k=w_k\), exactly the claimed equation for \(\rho_k\). Its left side is a strictly increasing continuous function from zero to \(k\), so each equation has exactly one root in \((0,1)\). At \(\rho_k\),
\[
\sum_{i\le k}\rho_k^{2(n_{k+1}-n_i)}
=\rho_k^{2(n_{k+1}-n_k)}\left(k+\frac12\right)
<k+\frac12,
\]
so \(\rho_{k+1}>\rho_k\). The waterline test and ordering \(w_0>w_1>\cdots\) prove exactly the asserted active supports. In the infinite case, for any fixed \(r<1\),
\[
\sum_{i<k}r^{2(n_k-n_i)}\le\sum_{j=1}^{\infty}r^{2j}=\frac{r^2}{1-r^2},
\]
where strict integer separation gives \(n_k-n_i\ge k-i\). As \(k\to\infty\) the right side is smaller than \(k-1/2\), forcing \(r<\rho_k\). Thus \(\rho_k\uparrow1\).

**4. Nondegenerate onset.** Immediately above \(\rho_k\), the active indices are \(0,\ldots,k\). With \(G_k\) as in the statement, the new waterline obeys the exact identity
\[
w_k-t_{k+1}=\frac{w_kG_k}{k+\tfrac12+G_k}.
\]
At the crossing the normalizing sum in (2) is \(D_k>0\). Since \(G_k(\rho_k)=0\) and \(G_k'(\rho_k)>0\), Taylor expansion yields the stated linear squared-magnitude law, with positive coefficient. Earlier amplitudes vary continuously and no other mode can enter at this radius.

**5. Endpoint distinction.** On finite Fourier sums at \(\rho=1\), (1) gives \(\|f\|_4\le2^{1/4}\|f\|_2\). Applying this bound to differences of truncations shows they converge in \(L^4\) to their \(L^2\) limit, so the identity extends to all \(f\in H_E\). For every nonzero \(f\), \(\|f\|_4^4=2\|f\|_2^4-\sum_i|c_i|^4<2\|f\|_2^4\). For infinite \(E\), flat normalized coefficients on increasingly many frequencies approach the fourth-power ratio two; thus \(\mathcal K_E(1)=2\) and the operator norm is \(2^{1/4}\), unattained. For each fixed finite truncation, \(T_\rho\to I\) as \(\rho\uparrow1\), hence \(\liminf_{\rho\uparrow1}\mathcal K_E(\rho)\ge2-1/N\) for every \(N\). The upper bound two holds throughout, and \(\mathcal K_E\) is nondecreasing because (1), expanded into diagonal and pair terms, has nonnegative coefficients and each weight is nondecreasing in \(\rho\). This proves the asserted limit. For finite \(E\), (1) at \(\rho=1\) is maximized only by \(p_i=1/N\), giving \(\mathcal K_E(1)=2-1/N\) and operator norm \((2-1/N)^{1/4}\).

## Verification

The standalone Python file `check_b2_poisson_activation.py` implements independent exact-rational Fourier convolution and the waterline formula for several finite \(B_2\) spectra, checks the optimality inequality against reproducible rational input coefficient arrays, and verifies normalized energy and multiplier stationarity. It also computes four successive thresholds for \(E=\{0,1,3,9,27\}\) by a transparent bisection diagnostic. The script prints `EXACT_B2_WATERLINE_CHECKS_PASS 1148`, with threshold approximations
\[
0.707106781187,\quad0.943771559156,\quad0.988151286741,\quad0.997188682302.
\]
Finite tests support, but do not prove, the general countable-spectrum claim. The general proof is the compactness and variational argument above.

## Relationship to prior work

Frank and Ivanisvili (2021) give the global Poisson-semigroup hypercontractivity criterion in low sphere dimensions and credit the circle case to Weissler. That global criterion does not determine the operator norm and maximizing Fourier supports above the first restricted threshold for an arbitrary \(B_2\) spectrum. Ciccone and Gonçalves (2022) study sparse arithmetic Fourier supports and sharp \(L^2(\mathbb S^1)\to L^6(\mathbb R^2)\) circle extension under their \(P(3)\) condition; their operator and objective differ from the present \(L^2(\mathbb T)\to L^4(\mathbb T)\) Poisson smoothing problem.

Previously available sharp fourth-moment analysis of finite nonresonant **three-frequency** Poisson spaces implies the one- and two-activation special case and is not claimed as new. Another published result gives exact **unweighted** fourth-moment constants for arbitrary finite lacunary \(B_2\) sets, with equal-energy extremizers; that result corresponds to \(\rho=1\) in the finite setting. The present all-length and countably infinite theorem covers the exact \(0<\rho<1\) waterline, infinitely many individually ordered sharp transitions, the onset law, and the nonattaining infinite endpoint. The searched literature did not establish these stronger weighted statements; priority remains conditional on historical completeness.

## Limitations

The theorem uses a strict \(B_2\) pair-sum hypothesis and analytic Poisson weights \(\rho^{n_i}\). It does not classify general midpoint-resonant sets, other smoothing multipliers without monotone weights, other even moments, or arbitrary Fourier phases when additive collisions occur. No closed form for each threshold polynomial is claimed beyond its unique scalar equation. The most significant originality risk is an older general weighted \(B_2\)-synthesis or diagonal multiplier theorem that implies the waterline argument under a different name.

## References

1. Rupert L. Frank and Paata Ivanisvili, *Hypercontractivity of the semigroup of the fractional laplacian on the n-sphere*, arXiv:2101.06209, first public 2021-01-15, https://arxiv.org/abs/2101.06209 .
2. Valentina Ciccone and Felipe Gonçalves, *Sharp Fourier Extension on the Circle Under Arithmetic Constraints*, arXiv:2208.09441, first public 2022-08-19, https://arxiv.org/abs/2208.09441 .
3. *Two sharp activation thresholds for analytic three-frequency Poisson fourth moments*, https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-two-sharp-activation-thresholds-for-analytic-three-frequency-poi--1425405cb653 . The nonresonant three-frequency case is not claimed as new here.
4. *Resonance-chain phase rigidity in lacunary fourth-moment extremizers*, https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-resonance-chain-phase-rigidity-in-lacunary-fourth-moment-extremi--2b706c80a337 .
5. F. B. Weissler, *Logarithmic Sobolev inequalities and hypercontractive estimates on the circle*, J. Funct. Anal. 37 (1980), 218–234, https://doi.org/10.1016/0022-1236(80)90042-7 .
