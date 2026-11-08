# Global convergence and a tunable logarithmic cusp law for a tropical Ludwig map

## Finding

Let \(r,k>0\) and choose a discrete step \(0<\tau<\infty\). The tropical Ludwig population map is
\[
T_{\tau,r,k}(x)=\frac{(1+\tau r)x}{1+\tau\bigl((r/k)x+x/(1+x^2)\bigr)},\qquad x>0.
\]
Every forward orbit from \(x_0>0\) converges monotonically (possibly constantly) to a **positive equilibrium**, for every choice of \(r,k,\tau\). Consequently the map has no nonfixed periodic or recurrent orbit. If \(x_0\) lies below a positive equilibrium and its first iterate increases, the limit is the first equilibrium to its right; the analogous statement holds for decreasing orbits and the last equilibrium to their left. The same conclusions hold for the finite limiting map \(T_{\infty,r,k}(x)=r/(r/k+1/(1+x^2))\).

At the *specific Ludwig cusp*
\[
s=\sqrt3,\qquad r_*=\frac{3\sqrt3}{8},\qquad k_*=3\sqrt3,
\]
the equilibrium \(s\) is unique and attracts every positive initial condition. For any \(x_0>0\) with \(x_0\ne s\), write \(z_n=x_n-s\), \(\sigma=\operatorname{sgn}(z_0)\) and, for a finite positive step,
\[
a_\tau=\frac{\tau\sqrt3}{16(1+\tau r_*)},\qquad
\ell_\tau=\frac34a_\tau-\frac1{12}
=\frac{\tau-16\sqrt3/9}{24(\tau+8\sqrt3/9)}.
\]
Then an initial-condition-dependent finite constant \(C(x_0,\tau)\) exists and
\[
\boxed{\frac1{z_n^2}=a_\tau n-\sigma\sqrt{\frac{a_\tau}{3}}\sqrt n
+\ell_\tau\log n+C(x_0,\tau)+o(1).}
\]
In particular
\[
\lim_{n\to\infty}n z_n^2=\frac{1}{a_\tau}
=\frac{16(1+\tau r_*)}{\tau\sqrt3}.
\]
The logarithmic coefficient changes sign at the **unique positive step**
\[\tau_*=\frac{16\sqrt3}{9},\]
and vanishes exactly there. For \(\tau=\infty\), the identical expansion holds with \(a_\infty=1/6\) and \(\ell_\infty=1/24\), and consequently \(\lim n z_n^2=6\). The sign of \(z_n\) is always \(\sigma\), so the leading signed approach is determined by which side contains the initial condition.

## Assumptions and scope

All parameters \(r,k\) are strictly positive, and the discrete parameter is an arbitrary real \(\tau>0\) or the explicitly defined \(\tau=\infty\) limit. All initial conditions are strictly positive real numbers. The expression \(T_{\infty,r,k}\) denotes a pointwise limit at fixed \(x\), **not** an ultradiscrete max-plus change of variables. The global orbit statement covers the whole parameter family; the explicit inverse-square expansion requires exactly \((r,k)=(r_*,k_*)\). At the fixed initial value \(x_0=s\), the orbit is constant and the inverse-square formula is inapplicable.

A positive equilibrium is a positive solution of
\[
H_{r,k}(x)=r,\qquad H_{r,k}(x)=\frac rkx+\frac{x}{1+x^2},
\]
or, equivalently, a positive root of
\[
\frac rk x^3-rx^2+\left(\frac rk+1\right)x-r=0.
\]
This cubic always has at least one positive root; its possible multiplicities and ordering are permitted without a genericity restriction. The assertions concern the original, dimensionless, deterministic iteration count, not continuous physical time.

## Proof

**1. Strong order preservation.** Direct differentiation and cancellation give the key exact identity
\[
H_{r,k}(x)-xH_{r,k}'(x)=\frac{2x^3}{(1+x^2)^2}>0\quad(x>0),
\]
and hence
\[
T_{\tau,r,k}'(x)
=\frac{(1+\tau r)\bigl(1+2\tau x^3/(1+x^2)^2\bigr)}{\bigl(1+\tau H_{r,k}(x)\bigr)^2}>0.
\]
For every \(x>0\) the map is bounded by \(k(1+\tau r)/(\tau r)\). Furthermore, \(T_{\tau,r,k}(x)/x\to1+\tau r>1\) as \(x\downarrow0\). If the first step increases, every subsequent step increases because \(T\) is strictly increasing; if it decreases, all subsequent steps decrease. A positive orbit is therefore monotone and bounded. Its limit is a fixed point by continuity, and cannot be zero: zero is locally repelling from the right. The fixed point equation is exactly \(H_{r,k}(x)=r\). If an increasing orbit crosses an equilibrium \(e\), strict increase of the map and \(T(e)=e\) would give a contradiction; thus its limit is precisely the least equilibrium above the initial condition. Similarly a decreasing orbit reaches the greatest equilibrium below its initial condition. An orbit already at equilibrium is constant. Any nonconstant periodic orbit would violate monotonicity, and the convergence excludes any nonfixed recurrent orbit.

For the infinite-step map, \(T_{\infty,r,k}\) is strictly increasing on \((0,\infty)\), bounded above by \(k\), and extends continuously to \(0\) with the *positive* value \(rk/(r+k)\). Its positive fixed points obey the same equation. The previous monotone-limit and equilibrium-order arguments apply verbatim.

**2. Exact cubic degeneracy at the cusp.** Set \(H_*=H_{r_*,k_*}\). Direct algebra gives the globally valid factorization
\[
H_*(x)-r_*=\frac{(x-s)^3}{8(1+x^2)}.
\]
It has exactly one positive root \(s\), and the sign of the increment is
\[
T_{\tau,*}(x)-x=-\frac{\tau x(x-s)^3}{8(1+x^2)(1+\tau H_*(x))}.
\]
Thus points below the cusp increase, points above it decrease, and global convergence from step 1 applies. Since the map is strictly increasing and fixes \(s\), no nonfixed positive orbit ever reaches or crosses \(s\): the displacement \(z_n\) keeps its nonzero initial sign.

Writing \(z=x-s\) and \(D_\tau=32+12s\tau\), the preceding rational increment has the exact expression
\[
T_{\tau,*}(s+z)-(s+z)=-\frac{\tau(s+z)z^3}{D_\tau\left(1+\frac s2z+\frac14z^2\right)+\tau z^3}.
\]
The first three relevant terms, with the **quintic term exactly zero**, are
\[
z_{n+1}=z_n-c_\tau z_n^3+d_\tau z_n^4+0\cdot z_n^5+O(z_n^6),
\quad c_\tau=\frac{\tau s}{D_\tau},\quad d_\tau=\frac{\tau}{2D_\tau}=\frac{c_\tau}{2s}.
\]
The disappearance of the fifth-degree coefficient is the critical cancellation needed for the stated logarithmic law; it follows by expanding the displayed exact rational expression, not from a generic cubic normal form. The same identities and limiting coefficients hold at \(\tau=\infty\), with \(c_\infty=1/12\) and \(d_\infty=1/(24s)\).

**3. The signed inverse-square expansion.** Let \(w_n=z_n^{-2}\), let \(\sigma=\operatorname{sgn}(z_0)\), and put \(a=2c_\tau>0\), \(d=d_\tau\). Taylor expansion of the inverse square and the vanishing quintic coefficient give
\[
w_{n+1}-w_n=a-2d\sigma w_n^{-1/2}+3c_\tau^2w_n^{-1}+O(w_n^{-3/2}).\tag{1}
\]
Here \(z_n\to0\) but retains its sign, so \(w_n\to\infty\); the error in (1) is uniform for all sufficiently large \(n\) along the orbit. The increment tends to \(a\), whence \(w_n/n\to a\) by summation. In particular \(w_n=an+O(\sqrt n)\), and substitution into (1) with the elementary sums of \(n^{-1/2}\) and \(n^{-1}\) yields
\[
w_n=an+B\sigma\sqrt n+O(\log n),\qquad B=-\frac{4d}{\sqrt a}=-\sqrt{\frac a3}.
\]
Substituting this sharper estimate into (1) produces
\[
w_{n+1}-w_n=a-\frac{2d\sigma}{\sqrt a\sqrt n}
+\frac{1}{n}\left(\frac{dB}{a^{3/2}}+\frac{3c_\tau^2}{a}\right)
+O\left(\frac{\log n}{n^{3/2}}\right).
\]
The displayed remainder is summable. The coefficient of \(1/n\) is
\[
\ell=\frac{dB}{a^{3/2}}+\frac{3c_\tau^2}{a}
=-\frac{d^2}{c_\tau^2}+\frac32c_\tau=\frac34a-\frac1{12},
\]
because \(d/c_\tau=1/(2s)\). Telescoping and using
\(\sum_{j=1}^{n}j^{-1/2}=2\sqrt n+C_1+o(1)\) and
\(\sum_{j=1}^{n}j^{-1}=\log n+C_2+o(1)\) proves that
\(w_n-an-B\sigma\sqrt n-\ell\log n\) converges to a finite real constant. This is exactly the claimed expansion. Finally \(a_\tau\) increases continuously from zero to \(1/6\) as \(\tau\) increases, so \(\ell_\tau=3a_\tau/4-1/12\) vanishes at exactly \(a_\tau=1/9\), equivalently \(\tau=16s/9\). Its sign is negative below and positive above that step, with the infinite-step value \(1/24\).

## Verification

The accompanying standalone `verify.py` uses exact SymPy expressions to check the derivative identity, the cusp factorization, the complete rational increment, the cubic/quartic/quintic Taylor coefficients, the logarithmic cancellation parameter, and both infinite-step limits. It also checks ten finite positive orbit scenarios with initial conditions on both sides of the cusp and finite and infinite steps. Run it with `python verify.py` and SymPy installed; the expected last line is `VERIFY_OK exact_algebra_plus_finite_checks; asymptotics_require_analytic_proof`. The universal and infinite-time arguments are the analytic proof above; finite computations only detect algebraic or illustrative numerical mistakes.

## Relationship to prior work

Ohmori and Yamazaki, *Piecewise linear cusp bifurcations in ultradiscrete dynamical systems*, arXiv:2506.23451v1 (first submitted 30 June 2025), introduce the same tropical Ludwig map in their equation (17), identify the cusp parameters in (16), and prove the correspondence of local cusp bifurcations for all steps. Their paper also gives the \(\tau\to\infty\) map and analyzes a subsequent max-plus limit. Those structural identifications belong to the source and are not claimed here. Their examined full preprint does not assert the global convergence and basin-selector theorem for arbitrary positive parameters or the exact inverse-square expansion with the step-dependent signed square-root and logarithmic coefficients.

Ohmori and Yamazaki, *Relation of stability and bifurcation properties between continuous and ultradiscrete dynamical systems via discretization with positivity: one dimensional cases*, arXiv:2212.03455v1 (7 December 2022), analyze generic local stability and bifurcations for positivity-preserving tropical schemes. They do not specialize to this Ludwig family or give the global and quantitative cusp conclusions. Published related results on critical slowing for other discrete scalar maps concern different iterations and do not imply the explicit present coefficients by substitution. The general order-preserving-interval convergence principle and parabolic-recursion asymptotic techniques are standard; the new contribution is their exact, global, cusp-specific synthesis and coefficient computation for the studied model.

## Limitations

The global theorem is one-dimensional and assumes all model parameters and initial populations are strictly positive. It does not cover negative states, stochastic forcing, variable timesteps, spatial coupling, the fully ultradiscrete max-plus scaling, or the continuous flow's physical-time rate. The exact expansion is at the single cusp parameter pair; its uniformity under simultaneous variation of \(r,k,\tau\) is not asserted. The expansion's finite additive constant depends on the initial condition and is not given in closed form. No independent audit has been performed. Historical priority is provisional pending broader expert literature review and any later publisher-version changes.

## References

1. S. Ohmori and Y. Yamazaki, *Piecewise linear cusp bifurcations in ultradiscrete dynamical systems*, arXiv:2506.23451v1 (30 June 2025), https://arxiv.org/abs/2506.23451 . Equations (13)–(21), sections 2–4.
2. S. Ohmori and Y. Yamazaki, *Relation of stability and bifurcation properties between continuous and ultradiscrete dynamical systems via discretization with positivity: one dimensional cases*, arXiv:2212.03455v1 (7 December 2022), https://arxiv.org/abs/2212.03455 . Sections 2–4.
3. S. Ohmori and Y. Yamazaki, *Piecewise linear cusp bifurcations in ultradiscrete dynamical systems*, Journal of Mathematical Physics **67** (2026), 022703, https://doi.org/10.1063/5.0288147 . Journal record of reference 1, not a separate first-public date.
