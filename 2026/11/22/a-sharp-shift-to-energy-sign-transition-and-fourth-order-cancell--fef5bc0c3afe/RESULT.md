# A sharp shift-to-energy sign transition and fourth-order cancellation for quartic midpoint SAV

## Finding

Let \(C>0\), \(a>0\), and set
\[
 F(x)=\frac{x^4}{4},\qquad f(x)=\sqrt{C+F(x)},\qquad
 s=\sqrt{1+\frac{a^4}{4C}}.
\]
Apply the midpoint lifted scalar auxiliary-variable method defined below to the scalar gradient flow \(\dot x=-x^3\), with \(x_0=a\) and \(r_0=f(a)\). For all sufficiently small fixed stepsizes \(h>0\), the positive monotone numerical branch exists for every step, \(x_n\downarrow0\), and \(r_n\downarrow r_\infty(h)>0\). Its **long-time auxiliary constraint defect** has the asymptotic expansion
\[
 r_\infty(h)-\sqrt C=h^2\,\mathcal A(a,C)+O(h^4),\qquad
 \mathcal A(a,C)=-\frac{C^{3/2}(s-1)^2(3s^2-4s-2)}{3s^3}.
\]
For \(a>0\), the leading coefficient changes sign exactly at the natural dimensionless energy-to-shift ratio
\[
 \boxed{\frac{F(a)}{C}=\frac{5+4\sqrt{10}}9.}
\]
It is positive below this ratio and negative above it. Precisely at equality, the long-time defect is \(O(h^4)\) rather than generically \(O(h^2)\). The modified-energy discrepancy \(r_\infty(h)^2-C\) has the same signs, with leading coefficient \(2\sqrt C\,\mathcal A(a,C)\). This is a statement about long-time auxiliary consistency, not a fourth-order state approximation.

## Assumptions and scope

The quartic gradient system is \(\dot x=-x^3\) on \(\mathbb R\), with initial state \(a>0\). Its exact solution tends to zero and its lifted auxiliary variable \(r=f(x)\) tends to \(\sqrt C\). Given positive \(h\), use the self-adjoint midpoint SAV equations
\[
 \begin{aligned}
 x_{n+1}-x_n&=-h\,\frac{\bar r_n}{f(\bar x_n)}\bar x_n^3,\\
 r_{n+1}-r_n&=f'(\bar x_n)(x_{n+1}-x_n),\\
 \bar x_n&=\frac{x_n+x_{n+1}}2,\qquad \bar r_n=\frac{r_n+r_{n+1}}2.
 \end{aligned}
\]
These are the midpoint lifted discrete-gradient/SAV equations with zero unsplit energy, quartic SAV energy, scalar mobility one, and all SAV coefficients evaluated at the midpoint. The scheme is *defined by the displayed equations*; no assertion is made about alternate SAV variants, predictive variants, or arbitrary finite stepsizes. The limit is taken first as \(n\to\infty\) at fixed \(h\), then as \(h\downarrow0\), keeping \(a,C\) fixed.

## Proof

**1. Exact energy law and scalar elimination.** Write \(\Delta_n=x_{n+1}-x_n\). Because \(2f'(u)=u^3/f(u)\), the two defining equations give
\[
 r_{n+1}^2-r_n^2=2\bar r_n f'(\bar x_n)\Delta_n
 =\frac{\bar r_n\bar x_n^3}{f(\bar x_n)}\Delta_n
 =-\frac{\Delta_n^2}{h}.
\]
Eliminating the auxiliary endpoint gives the exact one-dimensional equation
\[
 \Delta_n=-\frac{h r_n\bar x_n^3}{f(\bar x_n)+(h/2)f'(\bar x_n)\bar x_n^3}.
\]
On the compact interval \([0,a]\), the function \(u^3/f(u)\) is strictly increasing for \(u>0\); its derivative is positive because \(u f'(u)/f(u)<2<3\). For sufficiently small \(h\), so is the perturbed quotient in the eliminated equation. Consequently, provided \(r_n>0\) and bounded, the equation has a unique root \(\bar x_n\in(x_n/2,x_n)\), corresponding to \(0<x_{n+1}<x_n\). The implicit-function and endpoint estimates are uniform for \(0<x_n\le a\) once \(h\) is sufficiently small.

**2. Uniform closeness to the constraint manifold.** Define \(d_n=r_n-f(x_n)\), so \(d_0=0\). Symmetric Taylor expansion with bounded fifth derivative gives, uniformly for \(0\le x_{n+1}\le x_n\le a\),
\[
 d_{n+1}-d_n=-\frac{f'''(\bar x_n)}{24}\Delta_n^3+O(|\Delta_n|^5).
\]
The scalar equation and compactness imply \(|\Delta_n|\le K h\) while \(r_n\) is bounded and positive. Summing the disjoint positive decrements \(-\Delta_n\) gives \(\sum_n|\Delta_n|\le a\) and
\[
 |d_n|\le K_1(\max_j|\Delta_j|)^2\sum_j|\Delta_j|
 \le K_2h^2.
\]
For sufficiently small \(h\), this inequality bootstraps \(r_n=f(x_n)+d_n\ge\sqrt C/2\) and \(r_n\le f(a)+K_2h^2\) at every step, so the positive branch continues globally. Its decreasing state must tend to zero: a positive limit would force a uniformly nonzero step decrement by the eliminated equation. The auxiliary is positive and decreases by the exact energy law, so \(r_n\downarrow r_\infty(h)>0\). In particular, \(d_\infty=r_\infty(h)-\sqrt C\).

**3. Global leading defect.** Uniform \(d_n=O(h^2)\), midpoint Taylor expansion of \(f\), and \(\Delta_n=O(h)\) imply
\[
 \frac{\bar r_n}{f(\bar x_n)}=1+O(h^2),\qquad
 \Delta_n=-h\bar x_n^3(1+O(h^2))
\]
uniformly over all steps. Thus, since \(\sum_n|\Delta_n|\le a\), the symmetric Taylor remainders and this ratio yield
\[
 d_\infty=
 \frac{h^2}{24}\sum_{n\ge0}f'''(\bar x_n)\bar x_n^6(x_n-x_{n+1})+O(h^4).
\]
Composite midpoint quadrature over the partition \(a=x_0>x_1>\cdots\to0\) has error \(O((\max|\Delta_n|)^2)=O(h^2)\) for the smooth integrand \(f'''(u)u^6\). Therefore
\[
 d_\infty=\frac{h^2}{24}\int_0^a f'''(u)u^6\,du+O(h^4).
\]
Direct differentiation gives
\[
 f'''(u)=\frac{24Cu(4C-u^4)}{(4C+u^4)^{5/2}}.
\]
Substituting \(t=u^4/(4C)\) converts the coefficient to
\[
 \frac{1}{24}\int_0^a f'''(u)u^6\,du
 =\frac{C^{3/2}}2\int_0^{a^4/(4C)}\frac{t(1-t)}{(1+t)^{5/2}}\,dt
 =-\frac{C^{3/2}(s-1)^2(3s^2-4s-2)}{3s^3}.
\]
Finally, \(3s^2-4s-2\) has exactly one zero in \(s>1\), namely \((2+\sqrt{10})/3\). Since \(s>1\), this establishes the unique sign switch and cancellation. The expansion for \(r_\infty^2-C\) follows by factoring the difference of squares. □

## Verification

The companion `check_quartic_sav.py` uses only the Python standard library. It checks the polynomial identity behind the exact integral, the quartic-radical threshold, the discrete energy law at each computed step, signs on both sides of the threshold, and convergence of scaled defects toward the predicted coefficients for two step sizes. It also checks finite-step fourth-order scaling near the cancellation shift. Run `python check_quartic_sav.py` after extracting this finding's embedded files. The numerical tests are regression diagnostics; the infinite-step and small-step statements are established by the proof, not numerical extrapolation.

## Relationship to prior work

Celledoni, Martín de Diego, Owren, and Vaquero introduced the unified DG–SAV framework and a second-order midpoint variant (arXiv:2607.27795, released 2026-07-30); their accessible abstract describes structure preservation and examples rather than this quartic long-time coefficient. Russo, Ducceschi, and Bilbao analyzed auxiliary-variable convergence and sensitivity to potential shifts in different nonlinear conservative string systems (2026); their open full article does not state the quartic dissipative midpoint sign law. Classical SAV convergence analyses establish error bounds, not an exact opposite-sign transition for this observable. The derivation here credits the SAV method and uses the familiar midpoint quadrature-error mechanism; it claims the displayed complete threshold and cancellation result, not the general SAV or midpoint ideas.

## Limitations

This is a scalar quartic test problem, on the positive branch, for sufficiently small fixed stepsizes and an initially consistent auxiliary variable. It is not a uniform statement over all stepsizes, other potentials, all split energies, or arbitrary dissipative systems. The proof establishes \(O(h^4)\) at cancellation, not a nonzero fourth-order constant or a higher-order bound on the complete state. The preprint's complete full text was not accessible during the literature comparison; published-priority exclusion is consequently qualified, and independent mathematical review remains to be done.

## References

- E. Celledoni, D. Martín de Diego, B. Owren, M. Vaquero, *A Unified Discrete Gradient-SAV Framework for Structure-Preserving Integration*, arXiv:2607.27795 (first public release 2026-07-30), https://arxiv.org/abs/2607.27795.
- R. Russo, M. Ducceschi, S. Bilbao, *Numerical convergence of the scalar auxiliary variable method applied to nonlinear stiff string models*, *Nonlinear Dynamics* 114, article 857 (2026), https://doi.org/10.1007/s11071-026-12708-0.
- J. Shen, J. Xu, *Convergence and Error Analysis for the Scalar Auxiliary Variable (SAV) Schemes to Gradient Flows*, *SIAM Journal on Numerical Analysis* 56 (2018), https://doi.org/10.1137/17M1159968.
