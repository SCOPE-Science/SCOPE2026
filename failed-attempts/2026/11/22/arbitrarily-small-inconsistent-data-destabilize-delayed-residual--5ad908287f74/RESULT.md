# Arbitrarily small inconsistent data destabilize delayed-residual descent

## Finding
For every nonzero column \(a\in\mathbb R^m\) with \(m\ge2\), every datum \(b=ax_\star+z\) with \(a^{\mathsf T}z=0\) and \(z\ne0\), and every initial scalar iterate \(x_0\ne x_\star\), consider the **literal unextended** delayed-residual (DR) and residual-difference (RD) gradient updates defined below, both initialized by one full-residual surrogate step. Put
\[
\lambda=\|a\|_2^2,\qquad q=\|z\|_2^2/\lambda>0,
\qquad e_k=x_k-x_\star.
\]
The DR iteration is well-defined at every finite step and exhibits the following exact dichotomy:

- If \(|e_0|=\sqrt q\), it lies on the nonoptimal period-two orbit \(e_k=(-1)^k e_0\).
- If \(|e_0|\ne\sqrt q\), its error has **both** \(\liminf_{k\to\infty}|e_k|=0\) and \(\limsup_{k\to\infty}|e_k|=+\infty\). In particular it does not converge to the unique least-squares minimizer, and its data-residual norm has unbounded excursions despite returning arbitrarily close to the optimal residual norm.

For the very same first step and every permitted \(x_0\), RD instead reaches the exact least-squares minimizer on its **second** update. The instability persists for arbitrarily small but nonzero inconsistent-data components; at \(z=0\), the common warm-start step solves the one-column problem exactly.

## Assumptions and scope
Let \(m\ge2\), \(a\in\mathbb R^m\setminus\{0\}\), and \(b=ax_\star+z\), where \(x_\star\in\mathbb R\), \(z\in\ker(a^{\mathsf T})\setminus\{0\}\). Thus \(x_\star\) is the unique minimizer of \(\frac12\|ax-b\|_2^2\), not a solution of \(ax=b\). Given \(x_0\ne x_\star\), set \(r_k=b-ax_k\), \(g_k=a^{\mathsf T}r_k\), and
\[
\alpha_k^{\mathrm R}=\frac{\|r_k\|_2^2}{\|a^{\mathsf T}r_k\|_2^2}.
\]
Both algorithms use \(x_1=x_0+\alpha_0^{\mathrm R}g_0\). Subsequently, DR is precisely
\[
x_{k+1}=x_k+\alpha_{k-1}^{\mathrm R}g_k\quad(k\ge1).
\]
The competing RD method uses at its next update
\[
\alpha_1^{\mathrm{RD}}=
\frac{\|r_1-r_0\|_2^2}{|a^{\mathsf T}(r_1-r_0)|^2},
\qquad x_2=x_1+\alpha_1^{\mathrm{RD}}g_1.
\]
These are **unmodified formal step-size formulas** applied to fixed inconsistent data. No claim is made that their consistent-system convergence guarantees extend to such data. The RD method is terminated when its normal-equation residual vanishes.

## Proof
Orthogonality gives exact identities, at every \(e_k\ne0\):
\[
r_k=z-ae_k,\quad g_k=-\lambda e_k,\quad
\|r_k\|_2^2=\|z\|_2^2+\lambda e_k^2,
\quad \alpha_k^{\mathrm R}=\frac1\lambda\left(1+\frac q{e_k^2}\right).
\]
The warm step hence gives \(e_1=-q/e_0\). For DR, substituting its *previous* residual weight into the scalar gradient direction yields, exactly,
\[
\boxed{e_{k+1}=-\frac{q e_k}{e_{k-1}^2}\quad(k\ge1),
\qquad e_1=-\frac q{e_0}.}
\]
All iterates are nonzero by induction, so no denominator vanishes at a finite index. In particular signs alternate.

Write \(u_k=\log(|e_k|/\sqrt q)\). The recurrence becomes
\[
u_1=-u_0,\qquad u_{k+1}=u_k-2u_{k-1},
\]
whose exact solution is
\[
\boxed{
 u_k=u_0(\sqrt2)^k\left[\cos(k\theta)-\frac3{\sqrt7}\sin(k\theta)\right],
\quad \cos\theta=\frac1{2\sqrt2},\quad 0<\theta<\pi.}
\]
Indeed, its characteristic roots are \((1\pm i\sqrt7)/2=\sqrt2e^{\pm i\theta}\); the displayed expression satisfies both initial values. When \(u_0=0\), all \(u_k=0\), and the alternating signs give the exact two-cycle.

When \(u_0\ne0\), note that \(\theta/\pi\) is irrational: otherwise \(2\cos\theta=1/\sqrt2\) would be an algebraic integer, being the sum of two roots of unity, but its minimal polynomial \(2X^2-1\) is not monic over the integers (equivalently its algebraic norm is \(-1/2\)). Consequently the phases \(k\theta\bmod2\pi\) are dense and visit fixed open arcs where the bracketed trigonometric factor is respectively greater than a positive constant and less than its negative infinitely often. Since \((\sqrt2)^k\to\infty\), \(u_k\) has subsequences tending to \(+\infty\) and \(-\infty\). Exponentiating gives the stated limsup and liminf. Also \(\|r_k\|_2^2=\|z\|_2^2+\lambda e_k^2\), proving the data-residual assertion.

Finally \(r_1-r_0=-a(e_1-e_0)\), with \(e_1-e_0=-(q+e_0^2)/e_0\ne0\). Therefore
\[
\alpha_1^{\mathrm{RD}}=
\frac{\lambda(e_1-e_0)^2}{\lambda^2(e_1-e_0)^2}=\frac1\lambda,
\qquad e_2=(1-\lambda\alpha_1^{\mathrm{RD}})e_1=0.
\]
This proves the two-step termination. If \(z=0\), then \(\alpha_0^{\mathrm R}=1/\lambda\), so the warm start already terminates. For every fixed nonzero \(e_0\) and arbitrarily small \(\|z\|_2>0\), one can choose \(q\ne e_0^2\), demonstrating the sharp discontinuity at consistency.

## Verification
Run `python3 verify.py` using the Python standard library. It independently computes the residual and both step sizes in rational arithmetic for three column geometries, two least-squares solutions, five initial errors, and eleven DR steps each, comparing direct updates to the closed recurrence. It also checks RD termination, the logarithmic recurrence coefficients, and exact period-two balanced starts. Output on the packaged source is `VERIFY_OK 1457 exact-rational assertions; infinite assertions use analytic proof`.

## Relationship to prior work
Xin Xu's *Two-point residual step size gradient methods for linear systems* (2026), Section 3, introduces the DR and RD formulas and analyzes consistent systems with two singular values. The fixed inconsistent residual \(z\) adds a nonzero constant \(\|z\|_2^2\) to the DR numerator but cancels from RD's residual difference. In particular, under inconsistency the DR formula is **not** the usual BB1 secant step for the least-squares quadratic, whereas RD still reduces to its BB2 secant step. The present finding establishes the consequences of that distinction in the minimal inconsistent setting.

The earlier *Relaxation bifurcation and false two-cycles of residual surrogate-hyperplane projection* treats the **undelayed** full-residual update on inconsistent data. Its unit-relaxation map has a bounded exact two-cycle, in contrast to the generic unbounded excursions of the **lagged** update here. Earlier work on extended Kaczmarz for inconsistent data introduces extra correction stages; its convergence guarantees do not apply to the literal unextended DR formula. In fact, Xu's equations (25)–(27) explicitly derive the **same second-order logarithmic recurrence and complex characteristic roots** for the spectral residual ratio in a consistent positive-two-singular-value model, and Xu's Lemmas 3.2–3.4 prove the same irrational-angle/dense-phase ingredient. **None of those recurrence facts is claimed as new.** Their hypotheses exclude a fixed nonzero residual in the nullspace of the adjoint, whereas the present boundary case turns the log oscillation into arbitrarily large absolute least-squares errors and contrasts this with exact two-step RD termination. Extending the recurrence algebra to a zero singular mode is elementary; the claimed mathematical boundary is the resulting complete inconsistency-induced DR/RD dynamical separation, not a new method for solving recurrences.

## Limitations
The finding is exact-arithmetic and limited to a full-column-rank scalar unknown, fixed inconsistent data, and the literal unextended rules after the specified warm start. It does not predict finite-precision overflow or solve the higher-dimensional noisy problem; no inference about a safeguarded, extended, normalized-residual or reweighted method is justified. A prior general nonlinear-recursion analysis might imply the logarithmic dichotomy; no claim is made to invent that recurrence or classical irrational-rotation theory. Independent verification beyond the displayed proof and finite exact checks has not been performed.

## References
- X. Xu, *Two-point residual step size gradient methods for linear systems*, arXiv:2611.02743v1, publicly submitted 2026-11-02. https://arxiv.org/html/2611.02743v1
- *Relaxation bifurcation and false two-cycles of residual surrogate-hyperplane projection*, published research note (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-relaxation-bifurcation-and-false-two-cycles-of-residual-surrogat--7761fe4ad60a
- S. Dai and J. Zhang, *Residual-based surrogate hyperplane double and triple Kaczmarz algorithms for solving extended normal equations*, Mathematica Numerica Sinica 48 (2026), 123–140. https://doi.org/10.12286/jssx.j2025-1306
- Z. Wang and J.-F. Yin, *A surrogate hyperplane Kaczmarz method for solving consistent linear equations*, Applied Mathematics Letters 144 (2023), 108704. https://doi.org/10.1016/j.aml.2023.108704
