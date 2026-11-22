# Sharp integrated BV error of normalized fractional integration and its logarithmic jump retreat

## Finding
For every real order \(\alpha>0\), consider the constant-preserving Riemann–Liouville average
\[
(A_\alpha f)(x)=\frac{\alpha}{x^\alpha}\int_0^x (x-t)^{\alpha-1}f(t)\,dt,\qquad 0<x<1.
\]
Its exact optimal integrated approximation coefficient on the canonical real BV class defined below is
\[
C_\alpha=\sup_{V(f)>0}\frac{\|f-A_\alpha f\|_{L^1(0,1)}}{V(f)}=1-(1-s_\alpha)^\alpha,
\]
where \(s_\alpha\in(0,1)\) is the **unique** solution of
\[
\alpha\int_0^{1-s_\alpha}\frac{u^{\alpha-1}}{1-u}\,du=1.
\]
Equality holds **exactly** for the functions \(f(x)=c+d\mathbf 1_{[s_\alpha,1]}(x)\), with \(c\in\mathbb R\), \(d\ne0\), subject to the endpoint convention below. The two order limits are
\[
\lim_{\alpha\downarrow0}s_\alpha=\tfrac12,\quad
\lim_{\alpha\downarrow0}\frac{C_\alpha}{\alpha}=\log2,
\]
and, as \(\alpha\to\infty\), with \(W\) the nonnegative Lambert function satisfying \(W(z)e^{W(z)}=z\),
\[
\alpha s_\alpha=W(\alpha)+O((\log\alpha)^{-1}),\qquad
\alpha(1-C_\alpha)=W(\alpha)+1+O((\log\alpha)^{-1}).
\]
In particular, the single worst jump retreats to the initial boundary at scale \((\log\alpha)/\alpha\) while the maximum integrated error approaches one with a logarithmically enhanced deficit. At \(\alpha=1\), \(s_1=C_1=e^{-1}\).

## Assumptions and scope
Work with real functions on \([0,1]\) possessing a canonical right-continuous BV representation \(f(x)=c+\mu((0,x])\) for \(0\le x<1\), where \(\mu\) is a finite signed Borel measure on \((0,1)\); define \(f(1)=c+\mu((0,1))\). Let \(V(f)=|\mu|((0,1))\). Thus neither endpoint carries an uncounted jump and the representative at each interior jump is fixed. Integrals are Lebesgue integrals. The parameter \(\alpha\) is any positive real number, including integer orders. This normalized operator equals \(\Gamma(\alpha+1)x^{-\alpha}I_{0+}^\alpha\), not the unnormalized fractional integral; it preserves constants, which is essential for the variation seminorm bound.

## Proof
**Step response and BV reduction.** For \(0<s<1\), write \(e_s=\mathbf1_{[s,1]}\). For almost every \(x\in(0,1)\), direct integration gives
\[
(e_s-A_\alpha e_s)(x)=K_\alpha(x,s):=\mathbf1_{\{x>s\}}\left[1-(1-s/x)^\alpha\right]\ge0.
\]
Tonelli–Fubini applied to the signed measure decomposition yields
\[
f(x)-A_\alpha f(x)=\int_{(0,1)}K_\alpha(x,s)\,d\mu(s)
\]
for almost every \(x\). The triangle inequality gives
\[
\|f-A_\alpha f\|_1\le\int_{(0,1)}h_\alpha(s)\,d|\mu|(s)
\le\left(\sup_{0<s<1}h_\alpha(s)\right)V(f),
\]
where \(h_\alpha(s)=\int_s^1[1-(1-s/x)^\alpha]dx\). A unit jump attains its own response integral, so the supremum is exact. Nonnegative kernels ensure no cancellation can improve it.

**Unique maximizing location.** Substitution \(u=1-s/x\) followed by integration by parts gives
\[
h_\alpha(s)=1-s-(1-s)^\alpha+\alpha s\int_0^{1-s}\frac{u^{\alpha-1}}{1-u}\,du.
\]
Differentiation yields
\[
h_\alpha'(s)=-1+\alpha\int_0^{1-s}\frac{u^{\alpha-1}}{1-u}\,du,\qquad
h_\alpha''(s)=-\frac{\alpha(1-s)^{\alpha-1}}s<0.
\]
The derivative decreases from \(+\infty\) as \(s\downarrow0\) to \(-1\) as \(s\uparrow1\). Both endpoint values of \(h_\alpha\) vanish, so its strict interior maximizer \(s_\alpha\) is unique. Substitution of its stationarity equation into the expression for \(h_\alpha\) gives \(C_\alpha=1-(1-s_\alpha)^\alpha\). If equality holds in the BV bound, positivity and uniqueness of the maximizing \(s\) force \(|\mu|\) to be supported on the singleton \(\{s_\alpha\}\). Conversely any nonzero signed atom there attains equality, proving the entire equality classification.

**Near-zero order.** Put \(v=1-s\) and decompose
\[
\alpha\int_0^v\frac{u^{\alpha-1}}{1-u}\,du
=v^\alpha+\alpha\int_0^v\frac{u^\alpha}{1-u}\,du
=1+\alpha\log\frac{1-s}{s}+o(\alpha)
\]
for each fixed \(s\in(0,1)\), uniformly on compact subintervals. Strict monotonicity of the left-hand side in \(s\), and opposite signs of the first-order term on either side of \(1/2\), imply \(s_\alpha\to1/2\). The exact norm formula then gives \(C_\alpha/\alpha\to\log2\).

**Large order and logarithmic boundary layer.** Set \(q_\alpha=\alpha s_\alpha\). The stationarity equation becomes
\[
1=\alpha\int_{q_\alpha}^{\alpha}\frac{(1-y/\alpha)^{\alpha-1}}{y}\,dy.
\]
For \(q\asymp\log\alpha\), comparison with the exponential integral \(E_1(q)=\int_q^\infty e^{-y}dy/y\), splitting at \(\alpha/2\) and using \(\log(1-z)=-z+O(z^2)\) for \(z\le1/2\), gives the *uniform* estimate
\[
\alpha\int_q^\alpha\frac{(1-y/\alpha)^{\alpha-1}}y\,dy
=\alpha E_1(q)\left[1+O\!\left(\frac{(q+1)^2}{\alpha}\right)\right].
\]
The elementary bounds \(E_1(q)\sim e^{-q}/q\), applied first at \(q=(1\pm\varepsilon)\log\alpha\) for any fixed \(\varepsilon\in(0,1)\), and monotonicity of the left side, establish \(q_\alpha\sim\log\alpha\). Reapplying the uniform estimate and the integration-by-parts expansion
\[
E_1(q)=\frac{e^{-q}}q\left(1-\frac1q+O(q^{-2})\right)
\]
therefore gives \(q_\alpha+\log q_\alpha=\log\alpha+O(1/q_\alpha)\). Since \(W(\alpha)+\log W(\alpha)=\log\alpha\) and the derivative of \(q+\log q\) is at least one, \(q_\alpha=W(\alpha)+O(1/\log\alpha)\). Furthermore the same equation yields \(\alpha e^{-q_\alpha}=q_\alpha+1+O(1/q_\alpha)\). Finally
\[
\alpha(1-C_\alpha)=\alpha(1-q_\alpha/\alpha)^\alpha
=\alpha e^{-q_\alpha}\left[1+O(q_\alpha^2/\alpha)\right]
=W(\alpha)+1+O((\log\alpha)^{-1}).
\]
The estimates follow from elementary integral bounds and do not rely on a finite-degree extrapolation.

## Verification
Execute `python checks/fractional_bv_check.py` with Python, NumPy, and SciPy. The independently evaluated step-response integrals, critical equations, strict-optimum perturbations, signed-multijump BV bounds, and representative small-/large-order checks passed 211 finite tests. These are consistency checks only: the proof above establishes the global all-order and asymptotic statements.

## Relationship to prior work
Fu, Lu, and Yuan (2012) study weighted Riemann–Liouville/Hardy operators with sharp central-Morrey, BMO, and commutator bounds. Xiao (2001) establishes \(L^p\) and BMO norms for general weighted Hardy–Littlewood averages. These are different norms and do not directly compute the exact \(BV/V\to L^1\) identity defect. Verma and Liang (2020) prove bounded variation preservation for the unnormalized fractional integral on continuous data; they do not identify a sharp integrated identity-error norm or extremal jump position. Almoneef and coauthors (2025) derive fractional Euler–Maclaurin quadrature inequalities on BV data, rather than the norm of the constant-preserving operator used here. The normalization, the single-jump equality classification, and the logarithmic large-order localization are the new comparison targets; historical equivalence outside inspected material remains a risk.

## Limitations
The exact sharp coefficient is for Lebesgue integrated error on \((0,1)\), the normalized left-sided power kernel, and canonical scalar real BV data with no endpoint atoms. It is not a universal statement for arbitrary weighted Hardy kernels, unnormalized Riemann–Liouville integrals, multidimensional domains, other error norms, or pointwise representatives with uncounted endpoint jumps. Independent verification of historical priority remains outstanding.

## References
1. Z. W. Fu, S. Z. Lu, and W. Yuan, *A Weighted Variant of Riemann–Liouville Fractional Integrals on* \(\mathbb R^n\), Abstract and Applied Analysis (2012), Article 780132, first public 12 September 2012, https://doi.org/10.1155/2012/780132.
2. J. Xiao, *Lp and BMO Bounds of Weighted Hardy–Littlewood Averages*, J. Math. Anal. Appl. 262 (2001), 660–666, https://doi.org/10.1006/jmaa.2001.7594.
3. S. Verma and Y. S. Liang, *Effect of the Riemann–Liouville Fractional Integral on Unbounded Variation Points*, 2020, https://arxiv.org/abs/2008.11113.
4. A. A. Almoneef et al., *Weighted fractional Euler–Maclaurin inequalities for convex and bounded variation functions via Riemann–Liouville integrals*, Journal of Inequalities and Applications (2025), https://doi.org/10.1186/s13660-025-03333-3.
