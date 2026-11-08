# Sharp drag-exponent frontier for coefficient-lagged implicit midpoint iteration

## Finding

For the zero-forcing, one-dimensional gas--dust relative-velocity equation with positive drift-dependent drag rate \(\alpha_m(w)=a(1+bw^2)^{m/2}\), coefficient-lagged Picard iteration of the two-stage implicit-midpoint source update has a **sharp exponent dichotomy**. At every positive step size and initial positive relative speed, the iteration converges to the unique nonlinear implicit stage solution when \(0<m\leq1\); when \(m>1\), some sufficiently large positive initial speeds cause the iteration to approach a genuine, nonvanishing two-cycle instead. The Epstein--Baines square-root drift correction corresponds to the globally convergent boundary case \(m=1\).

In the quadratic-rate case \(m=2\), the exact transition is a critical initial speed \(x_c=2A^{3/2}/\sqrt B\), where \(A=1+s\), \(B=sb\) and \(s=h(1+\epsilon)a/2\). Below and at the threshold the iterates converge to the implicit stage; above it, the two limiting stage values are
\[
y_\pm=\frac12\left(\frac{x}{A}\pm\sqrt{\frac{x^2}{A^2}-\frac{4A}{B}}\right),
\]
with strictly attracting two-step multiplier \(4A^3/(Bx^2)\). In particular, the nonlinear stage root remains unique while the coefficient-lagged solver fails to approach it.

## Assumptions and scope

Fix arbitrary \(h>0\), \(\epsilon>0\), \(a>0\), \(b>0\), \(m>0\) and initial relative speed \(x>0\). On a one-dimensional source step assume constant gas and dust densities, no Lorentz force, no external force, and an isothermal or otherwise fixed temperature that leaves the positive parameters fixed. Let \(\epsilon\) be the dust-to-gas mass-density ratio. With \(w=v_{\rm d}-v_{\rm g}\), the source system reduces to
\[
\dot w=-(1+\epsilon)\alpha_m(w)w,\qquad
\alpha_m(w)=a(1+bw^2)^{m/2}.
\]

Choose the two-stage midpoint tableau \(a_{ij}=1/4\) for all four stage entries and output weights \(b_1=b_2=1/2\). Start the two Picard stage guesses at the same initial value \(x\), freeze the two drag coefficients at the current stage guesses, solve the resulting linear stage equations exactly, and update the coefficients from the new stage states. Symmetry and uniqueness of each frozen-coefficient solve keep the stage guesses equal throughout. Write their common value as \(y_k\), with \(y_0=x\), and set
\[
s=\frac{h(1+\epsilon)a}{2},\qquad
D_m(y)=1+s(1+by^2)^{m/2},\qquad
F_x(y)=\frac{x}{D_m(y)}.
\]
The precisely specified coefficient-lagged iteration is \(y_{k+1}=F_x(y_k)\). This is a *stage-solver* claim and is not a convergence claim about a whole dynamical simulation, other GIRK coefficient sets, or a nonlinear Newton solve.

## Proof

**1. Scalar reduction and unique nonlinear root.** The identical midpoint stages have rate \(K=-(1+\epsilon)\alpha_m(y)y\) and stage equation \(y=x+hK/2\). Freezing \(\alpha_m\) at a previous common guess \(z\) gives \(y=x/[1+h(1+\epsilon)\alpha_m(z)/2]=F_x(z)\). The function \(yD_m(y)\) is continuous and strictly increasing from zero to infinity for \(y\ge0\). Hence there is exactly one stage root \(r=r(x)>0\) satisfying \(rD_m(r)=x\), and \(0<r<x\).

**2. Exponent frontier.** Define the logarithmic slope
\[
q_m(y)=\frac{yD_m'(y)}{D_m(y)}
=m\frac{by^2}{1+by^2}
 \frac{s(1+by^2)^{m/2}}{1+s(1+by^2)^{m/2}}.
\]
Each fraction in the product is strictly increasing on \(y>0\), so \(q_m\) strictly increases from \(0\) to \(m\). The logarithmic-coordinate derivative of \(F_x\) is
\[
\frac{d\log F_x(e^t)}{dt}=-q_m(e^t).
\]
All iterates and the root lie in \((0,x]\). If \(0<m\le1\), then \(0<q_m(x)<1\), and the mean-value theorem in logarithmic coordinates gives
\[
\left|\log\frac{y_k}{r}\right|
\le q_m(x)^k\left|\log\frac{x}{r}\right|
\quad(k=0,1,2,\ldots).
\]
Thus the undamped Picard stage iteration converges for *every* finite initial speed and positive step size, with a certified (possibly slow) geometric bound. The boundary exponent \(m=1\) includes the square-root Epstein--Baines drift law.

If \(m>1\), strict monotonicity of \(q_m\) produces a unique \(y_c>0\) with \(q_m(y_c)=1\). Equivalently, with \(t_c=by_c^2>1/(m-1)\),
\[
s(1+t_c)^{m/2-1}((m-1)t_c-1)=1.
\]
Set \(x_c=y_cD_m(y_c)\). For \(x>x_c\), monotonicity of \(yD_m(y)\) implies \(r(x)>y_c\), and
\[
F_x'(r)=-q_m(r)<-1.
\]
Therefore the implicit root is locally repelling under Picard iteration. More strongly, \(F_x\) maps \([0,x]\) continuously and strictly decreasingly into \((0,x)\). Since \(F_x^2\) is increasing and \(F_x^2(x)<x\), the even iterates from \(y_0=x\) decrease and the odd iterates increase; both have positive limits \(L_+\) and \(L_-\) respectively and satisfy \(F_x(L_+)=L_-\), \(F_x(L_-)=L_+\). If the two limits coincided, they would equal \(r\). But \((F_x^2)'(r)=q_m(r)^2>1\), so a nonconstant converging orbit near \(r\) is impossible by the mean-value theorem. Since \(x>r\) and the map is injective, no iterate can equal \(r\). Thus \(L_+>L_-\): a genuine period-two limiting orbit exists, proving the sharpness of the exponent \(1\) as a *uniform-in-input* convergence boundary.

**3. Exact quadratic-rate classification.** For \(m=2\), \(D_2(y)=A+By^2\), with \(A=1+s>1\), \(B=sb>0\). The fixed-point slope \(2Br^2/(A+Br^2)\) equals one when \(r=\sqrt{A/B}\), equivalent to \(x=x_c=2A^{3/2}/\sqrt B\).

If \(y,z>0\) form a period-two orbit, the relations \(z(A+By^2)=x=y(A+Bz^2)\) imply
\[
(z-y)(A-Byz)=0.
\]
For a nontrivial two-cycle, \(yz=A/B\); substituting back gives \(x=A(y+z)\). Therefore the only candidate distinct pair consists of the two positive roots of \(u^2-(x/A)u+A/B=0\). Such a pair exists if and only if \(x>x_c\), and the displayed \(y_\pm\) formula follows. Both identities \(F_x(y_-)=y_+\), \(F_x(y_+)=y_-\) hold exactly. Their two-step multiplier simplifies to
\[
F_x'(y_-)F_x'(y_+)=\frac{4A^3}{Bx^2}\in(0,1).
\]

Every orbit from \(x\) has convergent even and odd subsequences by the monotone-map argument above. When \(x\le x_c\), no distinct two-cycle exists, so both subsequences converge to the unique fixed point (also at the neutral boundary \(x=x_c\)). When \(x>x_c\), the fixed point is repelling, so the two subsequences converge to \(y_+\) and \(y_-\). The threshold and the limiting orbit are therefore **global for the specified initial guess**, not merely local stability statements.

## Verification

Run `python3 verify.py` with Python 3, using no external libraries. The script checks exact-rational period-two identities, direct frozen-stage reductions, finite root and iteration comparisons, logarithmic contraction inequalities, exponent-threshold examples, and the stated two-step multiplier. It prints `VERIFY_OK` if all checks pass. The script's finite tests supplement but do **not** replace the analytic proof of the assertions for all positive parameters and every iteration order.

## Relationship to prior work

Chen, Li, He, Wibking, Krumholz and Bai (2026), arXiv:2610.18979v1, formulate a nonlinear two-stage GIRK gas--dust source integrator, explicitly include the two-stage midpoint tableau, specify Picard freezing of state-dependent source coefficients at stage values, and use the Epstein--Baines square-root drift-dependent stopping time. The present result isolates that prescribed midpoint source step in one pure-drag scalar case and proves an input-uniform Picard convergence theorem, a sharp growth-exponent obstruction and an exact quadratic-rate two-cycle classification that are not asserted in the inspected method sections.

Tedeschi-Prades, Birnstiel, Dolag and Ercolano (2025), arXiv:2511.07562, develop related GIRK drag integration. General one-dimensional fixed-point and flip-bifurcation theory supplies standard proof tools; the finding is the precise coupling of those tools to the physically motivated lagged GIRK stage solve and the sharp coefficient-growth frontier. The quadratic-rate family is a deliberate structural comparison, not a claim that its exponent is the physical Epstein--Baines law.

## Limitations

This is one-dimensional, one dust species, no magnetic field, no forcing, fixed temperature, fixed densities, identical frozen-stage midpoint initialization, and an exact linear solve at every iteration. The full charged-dust GIRK method can choose different coefficients, adapt branches and stop after finitely many iterations. The analysis neither establishes a universal bound on the number of iterations needed to meet a chosen coefficient tolerance nor proves failure of Newton iteration or of a complete time-dependent simulation. Discovery of an older equivalent rational-map calculation would qualify priority for the explicit quadratic-rate corollary. Independent validation has not been performed.

## References

1. M. Chen, H. Li, C.-C. He, B. D. Wibking, M. R. Krumholz and X.-N. Bai, *A Nonlinear General Implicit Runge-Kutta Integrator for Multifluid Charged Dust and Gas*, arXiv:2610.18979v1 (first public version October 13, 2026), https://arxiv.org/abs/2610.18979 . Sections II.4, II.5 and III.3.
2. G. Tedeschi-Prades, T. Birnstiel, K. Dolag and B. Ercolano, *General Implicit Runge-Kutta Integrators for Multifluid Gas-Dust Aerodynamic Drag*, arXiv:2511.07562 (2025), https://arxiv.org/abs/2511.07562 .
3. M. A. Chan and P. Mulet, *Convergence of lagged diffusivity fixed point methods for total variation image restoration*, SIAM Journal on Numerical Analysis 36 (1999), https://doi.org/10.1137/S0036142997327075 . Background on a different coefficient-lagging problem, not an implication of the present specialized threshold.
