# Beta-product subnormality and a sharp commutator threshold for critical power-Fock Volterra shifts

## Finding
For a real exponent \(\alpha>2\), let \(\mathcal F_\alpha\) be the Hilbert space of entire functions with norm
\[
\|f\|_\alpha^2=\int_{\mathbb C}|f(z)|^2e^{-2|z|^\alpha}\,dA(z),
\]
where \(dA\) is planar Lebesgue measure. For each integer \(k\ge1\) let
\[
(V_k f)(z)=\int_0^z k w^{k-1}f(w)\,dw.
\]
The following is a complete classification in this monomial family:

1. \(V_k\) is bounded precisely when \(k\le\alpha\), and compact precisely when \(k<\alpha\).
2. Among the bounded nonzero \(V_k\), subnormality (equivalently, hyponormality) occurs **precisely when** \(\alpha=k=m\) is an integer \(m\ge3\). In that case \(\|V_m\|=1\), and \(V_m\) is a direct sum of \(m\) subnormal unilateral weighted shifts with explicit beta-product Berger measures.
3. For \(\alpha=m=k\ge3\), the positive self-commutator \(D_m=V_m^*V_m-V_mV_m^*\) is trace class, \(\operatorname{tr}D_m=m\), and its singular values obey
\[
s_j(D_m)\sim \frac{m(3m-4)}{2j^2}\quad(j\to\infty).
\]
Consequently \(D_m\in\mathcal S_p\) exactly for \(p>1/2\), including quasi-Schatten exponents \(0<p<1\). The coefficient and cutoff are sharp.

The constant symbol, whose integral operator is zero, is excluded by \(k\ge1\). No assertion is made here for mixed polynomial symbols.

## Assumptions and scope
All Hilbert spaces and operators are complex. The defining integral is first taken on polynomials. The monomials are complete and orthogonal in \(\mathcal F_\alpha\): angular integration separates Taylor coefficients and the norm is the sum of their squared monomial norms. Let \(h_n=\|z^n\|_\alpha\) and \(e_n=z^n/h_n\), for \(n\ge0\). Then
\[
h_n^2=\frac{2\pi}{\alpha}\,2^{-(2n+2)/\alpha}\,\Gamma\!\left(\frac{2n+2}{\alpha}\right).
\]
A bounded operator is *hyponormal* when \(T^*T-TT^*\succeq0\). It is *subnormal* when it admits a normal extension on a larger Hilbert space. The Schatten quasi-ideal \(\mathcal S_p\) consists of compact operators whose singular values have summable \(p\)-th powers.

## Proof
**Monomial shift and critical exponent.** On normalized monomials,
\[
V_ke_n=v_{\alpha,k,n}e_{n+k},\qquad
v_{\alpha,k,n}^2=\frac{k^2}{(n+k)^2}2^{-2k/\alpha}
\frac{\Gamma((2n+2k+2)/\alpha)}{\Gamma((2n+2)/\alpha)}.
\]
All coefficients are positive. The Gamma-ratio asymptotic gives
\[
v_{\alpha,k,n}^2\sim k^2\alpha^{-2k/\alpha}n^{2k/\alpha-2}.
\]
Therefore, \(k>\alpha\) gives an unbounded operator, \(k=\alpha\) gives bounded weights converging to one, and \(k<\alpha\) gives weights tending to zero. A fixed-step weighted shift is compact exactly when its coefficients tend to zero (finite-rank truncation in one direction; orthogonality of images in the other). Thus (1) follows. If \(k<\alpha\), the nonzero compact shift cannot be hyponormal: its self-commutator has diagonal values \(v_{\alpha,k,n}^2-v_{\alpha,k,n-k}^2\) for \(n\ge k\), and hyponormality would require each positive subsequence of squared weights on a residue class to be nondecreasing while tending to zero. This is impossible. If \(k\le\alpha\) and \(k\ne\alpha\), then \(k<\alpha\); hence a necessary condition for subnormality or hyponormality is \(k=\alpha\), which requires integral \(\alpha\).

**Exact critical weights.** Put \(m=k=\alpha\). Since the Gamma arguments differ by two, the functional equation \(\Gamma(x+2)=x(x+1)\Gamma(x)\) gives
\[
q_n:=v_{m,m,n}^2=\frac{(n+1)(n+1+m/2)}{(n+m)^2}.
\]
For \(m\ge3\), each factor \((n+1)/(n+m)\) and \((n+1+m/2)/(n+m)\) lies strictly below one and increases strictly with \(n\), so \(0<q_n<1\), \(q_n\uparrow1\), and the shift is a contraction of norm one. For completeness, the excluded exponent \(m=1\) would give \(q_n=1+1/[2(n+1)]\), which decreases and is not hyponormal; the Gaussian exponent \(m=2\) is the known boundary case and is not claimed new here.

**Normal extensions from beta products.** Each residue subspace \(\mathcal H_r=\overline{\operatorname{span}}\{e_{r+mj}:j\ge0\}\), \(0\le r<m\), reduces \(V_m\). Write
\[
a_r=\frac{r+1}{m},\quad b_r=a_r+\frac12,\quad c_r=1+\frac rm.
\]
The squared weight at the \(j\)-th step of this component is
\[
q_{r+mj}=\frac{(j+a_r)(j+b_r)}{(j+c_r)^2},
\]
so its \(\ell\)-th squared orbit norm, using the rising factorial, is
\[
\gamma_{r,\ell}=\prod_{j=0}^{\ell-1}q_{r+mj}
=\frac{(a_r)_\ell(b_r)_\ell}{(c_r)_\ell^2}.
\]
As \(m\ge3\), both \(c_r-a_r=1-1/m\) and \(c_r-b_r=1/2-1/m\) are positive. Let \(X_r\) and \(Y_r\) be independent beta random variables with parameters \((a_r,c_r-a_r)\) and \((b_r,c_r-b_r)\), respectively. The beta moment formula yields \(\mathbb E[(X_rY_r)^\ell]=\gamma_{r,\ell}\) for every integer \(\ell\ge0\). Let \(\Theta\) be independent and uniform on \([0,2\pi)\); setting \(Z_r=\sqrt{X_rY_r}\,e^{i\Theta}\) produces a rotation-invariant probability measure on the closed disk. In its \(L^2\) space, multiplication by the coordinate is normal, and restriction to the closure of analytic polynomials is the weighted shift with squared weights \(\gamma_{r,\ell+1}/\gamma_{r,\ell}\). This constructs an explicit normal extension of every \(\mathcal H_r\) component, and their finite direct sum extends \(V_m\). Thus (2) is proved without assuming a general classification of rational weighted shifts.

**Self-commutator and the sharp ideal boundary.** In the basis \(e_n\), \(D_m\) is diagonal, with entries
\[
d_n=\begin{cases}q_n,&0\le n<m,\\q_n-q_{n-m},&n\ge m.\end{cases}
\]
Strict increase of \(q_n\) makes every \(d_n\) positive. As \(n\to\infty\), rational expansion gives
\[
q_n=1-\frac{3m/2-2}{n}+O_m(n^{-2}),\qquad
d_n=\frac{m(3m/2-2)}{n^2}+O_m(n^{-3}).
\]
The positive leading coefficient is \(m(3m-4)/2\). Because \(d_n\sim C_m n^{-2}\) with \(C_m>0\), their decreasing rearrangement has the same leading asymptotic \(s_j(D_m)\sim C_mj^{-2}\). Explicitly, for any \(\varepsilon>0\), eventually \((C_m-\varepsilon)n^{-2}\le d_n\le(C_m+\varepsilon)n^{-2}\), and counting entries above a threshold yields the rearrangement asymptotic. The Schatten criterion follows. Finally, diagonal telescoping yields for every integer \(N\ge0\)
\[
\sum_{n=0}^{N+m-1}d_n=\sum_{n=N}^{N+m-1}q_n\longrightarrow m,
\]
proving \(\operatorname{tr}D_m=m\) and completing (3).

## Verification
All critical infinite-dimensional steps above use exact Gamma identities, beta moments, finite-step shift analysis, and asymptotic bounds; none rests on finite enumeration. The standalone \(checker.py\) verifies, in exact rational arithmetic, the beta-moment identities for multiple orders and residue classes, strict weight monotonicity, diagonal self-commutator positivity, and the finite telescoping identity; it also cross-checks selected Gamma ratios numerically. The script's output is supplementary only and is reproduced in \(VERIFICATION.md\).

## Relationship to prior work
Bonet–Mengestie–Worku (2021) study exactly the generalized power-Fock setting and Volterra operators, including boundedness, compactness and dynamics; their Section 3 records the degree threshold. Mengestie–Takele (2023) study broader generalized Fock-type Volterra symbols and Schatten membership, not subnormal monomial classification or the self-commutator's sharp quasi-Schatten boundary. Mengestie (2026) proves subnormality for the classical Gaussian Fock quadratic Volterra symbol and essential normality for all bounded Gaussian symbols. The present theorem's new range is **strictly super-Gaussian** \(\alpha>2\), including every integral \(m\ge3\); it does not claim the Gaussian result. A relevant published 2026 result on Gaussian self-commutator Schatten exponents likewise concerns the Gaussian exponent and does not imply the super-Gaussian beta-product construction.

## Limitations
The theorem concerns monomial \(V_k\) only, not sums of symbols or generalized composition-type Volterra operators. The exact trace and singular-value law concern the critical integer exponents \(m\ge3\). The historical originality assessment is based on the inspected primary publications and indexed research records; further unindexed weighted-shift or special-function treatments could overlap. No independent mathematical audit has been performed.

## References
- J. Bonet, T. Mengestie, M. Worku, *Dynamics of the Volterra-type integral and differentiation operators on generalized Fock spaces*, arXiv:2112.05420v1, public 10 December 2021, https://arxiv.org/html/2112.05420v1.
- T. Mengestie, M. H. Takele, *Integral and Weighted Composition Operators on Fock-type Spaces*, Bulletin of the Malaysian Mathematical Sciences Society 46 (2023), article 80, published 23 February 2023, https://doi.org/10.1007/s40840-023-01476-4.
- Z.-C. Yang, Z.-H. Zhou, *Generalized Volterra-type operators on generalized Fock spaces*, Mathematische Nachrichten 295 (2022), 1641–1662, https://doi.org/10.1002/mana.202000014.
- T. Mengestie, *Normality properties of Volterra-type integral operators on the Fock space*, Advances in Operator Theory 12 (2027), article 1, first published 21 October 2026, https://doi.org/10.1007/s43036-026-00541-6.
