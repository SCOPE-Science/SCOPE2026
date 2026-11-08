# Sharp critical slowdown at the velocity-regularized kinetic two-cycle

## Finding

For the two-dimensional velocity-regularized kinetic map at its symmetry-breaking threshold, the symmetric period-two orbit is **nonhyperbolic but locally asymptotically attracting**. Its generic local relaxation is algebraic, with a sharp momentum-dependent coefficient. This resolves the nonlinear behavior exactly at the parameter where the known Floquet criterion becomes inconclusive.

Define
\[
\varphi(s)=\frac{s}{1+s^2},\qquad
\kappa=\frac{1-b}{1+b},\qquad a=\frac4\kappa,
\]
and
\[
T(v,y)=\left(bv+(1-b)y,\quad y-a\varphi(bv+(1-b)y)\right).
\]
For every fixed \(b\in[0,1)\), the points \(P=(1,-1/\kappa)\) and \(-P\) form a prime two-cycle. The two-step map \(F=T^2\) has a unit center multiplier and a stable multiplier \(b^2\) at either point. Nevertheless, both points are locally asymptotically stable as fixed points of \(F\).

There is a one-dimensional local strong-stable manifold \(W^{ss}_{\mathrm{loc}}(P)\) (possibly degenerate when \(b=0\)). For every sufficiently nearby initial state outside that manifold, with \((v_{2n},y_{2n})=F^n(v_0,y_0)\),
\[
\lim_{n\to\infty}\sqrt n\,|y_{2n}+\kappa^{-1}|
=\lim_{n\to\infty}\sqrt n\,|v_{2n}-1|
=\sqrt{\frac{1-b}{8(1+b)}}.
\]
The same statement holds near \(-P\) after changing both signs. This limit is measured in actual pairs of map steps; it is not a continuous-time rate.

## Assumptions and scope

The state space is the entire real plane in the fixed coordinate order \((v,y)\). The momentum parameter satisfies \(0\le b<1\). The gain is fixed exactly at \(a=4(1+b)/(1-b)\); neither a small-parameter approximation nor a limiting value of \(b\) is intended. The nonlinear map is real analytic. Each local attracting neighborhood may depend on \(b\). The initial state may lie on either side of the center direction. The exceptional strong-stable manifold contains the periodic point and consists of initial data with faster-than-algebraic approach; its transverse rate is governed locally by \(b^2\), with finite-time collapse possible at \(b=0\).

## Proof

**1. Exact cycle and linearization.** Since \(\varphi(1)=1/2\), direct substitution gives \(T(P)=-P\) and \(T(-P)=P\). Oddness yields \(T(-X)=-T(X)\). At either cycle point, \(\varphi'(\pm1)=0\), so in \((v,y)\) coordinates
\[
DT(P)=DT(-P)=\begin{pmatrix}b&1-b\\0&1\end{pmatrix}.
\]
Consequently \(DF(P)\) has eigenvalues \(b^2\) and \(1\), and the neutral direction is tangent to \((1,1)\).

**2. Local sign-reflected map.** Set \(R=-T\). Since \(T\) is odd, \(R^2=T^2=F\), and \(R(P)=P\). Write \(v=1+p\), \(y=-\kappa^{-1}+q\), and \(u=bp+(1-b)q\). The exact coordinate formulas are
\[
p'=-u,\qquad q'=-q+\frac4\kappa\left[\frac12-\varphi(1-u)\right].
\]
Expansion of the displayed rational function, which is regular at \(u=0\), gives
\[
\varphi(1-u)=\frac12-\frac14u^2-\frac14u^3+O(u^4),\qquad
q'=-q+\kappa^{-1}(u^2+u^3)+O(u^4).
\]
The derivative of \(R\) has multipliers \(-1\) (center) and \(-b\) (strong stable). In particular, a smooth local center manifold tangent to \(p=q\) exists for each fixed \(b\in[0,1)\).

**3. Critical center-manifold coefficient.** Write that center manifold as \(p=h(q)=q+Aq^2+Bq^3+O(q^4)\). Invariance under \(R\), coefficient by coefficient, gives
\[
A=-\frac1{1-b},\qquad
B=\frac{3(1+b)}{(1-b)^2}.
\]
Indeed \(u=q+bAq^2+bBq^3+O(q^4)\). Substitution into the previous formulas gives the reduced one-step map
\[
q'=-q+c_2q^2+c_3q^3+O(q^4),\qquad
c_2=\frac{1+b}{1-b},\quad
c_3=\frac{(1+b)(1-3b)}{(1-b)^2}.
\]
The quadratic terms cancel in the second iterate, while direct composition yields
\[
q_{n+1}=q_n-2(c_3+c_2^2)q_n^3+O(q_n^4)
=q_n-\underbrace{\frac{4(1+b)}{1-b}}_{K_b>0}q_n^3+O(q_n^4).
\]
This is a strict, two-sided parabolic attraction law on the center manifold, not merely a neutral Floquet statement.

**4. Full local dynamics and exact rate.** The other eigenvalue of \(F\) is \(b^2<1\), so local center-stable reduction gives asymptotic stability of \(P\), a one-dimensional local strong-stable curve, and exponentially decaying transverse displacements. Off this curve the center displacement is eventually nonzero, of fixed sign, and obeys the displayed scalar parabolic recurrence up to exponentially small transverse terms. For any nonzero such sequence tending to zero, the identity
\[
\frac1{q_{n+1}^2}-\frac1{q_n^2}=2K_b+o(1)
\]
implies \(nq_n^2\to1/(2K_b)\) by summation. The center graph has \(p=q+O(q^2)\); exponentially small transverse errors do not change this limit. Therefore both physical coordinate displacements have the stated common limit \(1/\sqrt{2K_b}=\sqrt{(1-b)/[8(1+b)]}\). The result at the opposite phase follows from oddness.

## Verification

The accompanying `VERIFY.py` requires only the Python standard library and can be run with `python3 VERIFY.py`. It exactly verifies the two-cycle and center-reduction cubic coefficient for four rational momentum values using `fractions.Fraction`, checks the rational Taylor coefficients, and compares four full nonlinear trajectories after 120,000 two-step iterations with the predicted critical rate. The mathematical proof is analytic and valid for all fixed \(b\in[0,1)\); these finite tests are supplementary.

## Relationship to prior work

Itin's October 2026 analysis derives this map as a reduced kinetic optimizer, identifies the symmetric period-two orbit, classifies its *strict linear* stability and proves the appearance of asymmetric two-cycles above the symmetry-breaking value. Its Theorem 1 and Proposition 8 locate the equality parameter but leave the nonlinear attraction and exact critical-time law at equality unstated. The present theorem treats precisely that boundary, computes its cubic center coefficient for all momentum values, and obtains the actual discrete-time asymptotic constant. It does not claim discovery of the existing period-two orbit or of the symmetry-breaking threshold. Standard center-manifold methods are classical (see Kuznetsov).

## Limitations

All stability and asymptotic statements are local and concern the reduced autonomous kinetic map, not a complete neural-network optimizer with stochastic gradients, clipping, changing curvature or a moving preconditioner. There is no global basin classification. The result is pointwise in \(b\); no convergence is asserted uniformly as \(b\uparrow1\). Different center-manifold parametrizations can change intermediate coefficients, but the final limits are expressed in the original physical coordinates. The strong-stable curve is characterized locally, not by a global closed form.

## References

- A. Itin, *Physics-Inspired Optimizers beyond the Edge of Stability: Period-Two Orbits and Delayed Instability*, arXiv:2610.27321v1 (first posted 2026-10-19), especially Section 3 and Appendix A, Proposition 8; https://arxiv.org/abs/2610.27321.
- Y. A. Kuznetsov, *Elements of Applied Bifurcation Theory*, 3rd edition, Springer, 2004, chapters on discrete-time bifurcations and invariant manifold methods; https://doi.org/10.1007/978-1-4757-3978-7.
