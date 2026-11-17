# A two-to-five selective relaxation resonance in a quadratic stochastic population map

## Finding
Consider the non-Volterra quadratic stochastic map on the closed probability simplex
\[
\Delta_2=\{(x_1,x_2,x_3):x_i\geq0,\ x_1+x_2+x_3=1\}
\]
defined by
\[
V(x_1,x_2,x_3)=\left(c x_3^2+2x_2x_3,\ d x_3^2+2x_1x_3,\ (x_1+x_2)^2+\tfrac14x_3^2\right),
\qquad c,d\geq0,\quad c+d=\tfrac34.
\]
Write \(\delta=c-d\), and set
\[
p_*=(\tfrac3{10}+\tfrac{2\delta}{45},\ \tfrac3{10}-\tfrac{2\delta}{45},\ \tfrac25),
\qquad K=-\tfrac{28\delta}{9}.
\]
The point \(p_*\) is the unique fixed point. For every initial state \(p_0\in\Delta_2\) with \(x_{3,0}\ne2/5\), let \(p_n=V^n(p_0)\) and \(\sigma=\operatorname{sgn}(x_{3,0}-2/5)\). Then
\[
\boxed{\lim_{n\to\infty}(-1)^n\sqrt n\,(p_n-p_*)
=\sigma\frac4{5\sqrt2}\left(\frac{K-1}{2},\frac{-K-1}{2},1\right).}
\]
There is also an exact universal second-order *transverse* limit:
\[
\boxed{\lim_{n\to\infty}n\left[(x_{1,n}-x_{2,n})-\frac{4\delta}{45}
-K\left(x_{3,n}-\frac25\right)\right]=\frac{160\delta}{81}.}
\]
These formulas yield a sharp, selective relaxation transition. At the feasible coefficient ratio \(c:d=2:5\), namely \((c,d)=(3/14,15/28)\), the first population coordinate loses its order-\(n^{-1/2}\) oscillation and instead satisfies
\[
\boxed{\lim_{n\to\infty}n\left(x_{1,n}-x_{1,*}\right)=-\frac{20}{63}.}
\]
At the exchanged coefficient ratio \(c:d=5:2\), namely \((c,d)=(15/28,3/14)\), the corresponding law holds for the second coordinate:
\[
\boxed{\lim_{n\to\infty}n\left(x_{2,n}-x_{2,*}\right)=-\frac{20}{63}.}
\]
The two special ratios are the **only** admissible ratios at which the respective peripheral coordinate lacks the order-\(n^{-1/2}\) term. All other peripheral coordinates have a nonzero alternating order-\(n^{-1/2}\) coefficient. For the exceptional initial hyperplane \(x_{3,0}=2/5\), all three coordinates converge geometrically (the third is already fixed), and the preceding nonzero algebraic constants are not asserted.

## Assumptions and scope
The map uses the boundary values \(a=\alpha=0\) and the critical parameter \(e=1/4\) of the Hardin–Rozikov family. Parameters \(c,d\) are arbitrary nonnegative real numbers with fixed sum \(3/4\); thus \(\delta\in[-3/4,3/4]\). All initial simplex states, including boundary points, are allowed. Iteration count \(n\) is the original discrete-generation clock. The generic sharp limits require exactly \(x_{3,0}\ne2/5\), without restrictions on the other initial coordinates. The theorem makes no claim about other values of \(e\) or about the full four-parameter family.

## Proof
**1. Triangular coordinates and fixed point.** Put \(t_n=x_{3,n}\) and \(s_n=x_{1,n}-x_{2,n}\). Using \(x_{1,n}+x_{2,n}=1-t_n\), the original quadratic update is exactly
\[
t_{n+1}=1-2t_n+\tfrac54t_n^2,
\qquad s_{n+1}=\delta t_n^2-2t_n s_n.
\]
At \(t_*=2/5\), the unique fixed value of the second recurrence is \(s_*=4\delta/45\), giving \(p_*\). Uniqueness of the scalar fixed point on \([0,1]\) follows by solving \(t=1-2t+5t^2/4\); its two real roots are \(2/5\) and \(2\), of which only the first lies in the physical interval. The fixed-point equation for \(s\) then has a unique solution.

**2. Uniform global critical clock.** Set \(y_n=t_n-2/5\), \(a=5/4\). The *exact* scalar recurrence is
\[
y_{n+1}=-y_n+a y_n^2=-y_n(1-a y_n),
\quad y_n\in[-2/5,3/5].
\]
On this interval \(1-a y_n\ge1/4>0\), so any nonzero \(y_n\) changes sign at every step and cannot become zero. A second iteration gives
\[
y_{n+2}=y_n-2a^2y_n^3+a^3y_n^4
=y_n[1-a^2y_n^2(2-a y_n)].
\]
For every nonzero \(y\in[-2/5,3/5]\), the bracket lies strictly between zero and one: the factor removed from one is positive and is at most \(45/64<1\) on that entire interval. Consequently the even subsequence retains its initial sign, decreases in absolute value, and tends to zero; the odd subsequence also tends to zero. This proves global convergence of \(t_n\) without an unverified local-basin assumption.

For the nonzero even subsequence put \(w_m=y_{2m}^{-2}\). The exact two-step equation shows
\[
w_{m+1}-w_m
=y_{2m}^{-2}\left([1-a^2 y_{2m}^2(2-a y_{2m})]^{-2}-1\right)
\longrightarrow4a^2=\tfrac{25}{4}.
\]
By Cesàro averaging, \(w_m/m\to25/4\). As the odd and even absolute values are asymptotically equal, this yields
\[
\lim_{n\to\infty}n y_n^2=\frac{1}{2a^2}=\frac8{25},\qquad
\lim_{n\to\infty}(-1)^n\sqrt n\, y_n
=\sigma\frac4{5\sqrt2}.
\]
These identities are for all physical initial \(t_0\ne2/5\), with no numerical extrapolation.

**3. Stable transverse response with its exact next coefficient.** Write \(z_n=s_n-s_*\). Direct substitution, with the fixed-point equation removed, gives
\[
z_{n+1}=-(\tfrac45+2y_n)z_n+\tfrac{28\delta}{45}y_n+\delta y_n^2.
\]
Choose \(K=-28\delta/9\), uniquely determined by cancelling the linear forcing after subtracting \(K y_{n+1}\), and put \(r_n=z_n-Ky_n\). An *exact polynomial identity*, not a formal asymptotic expansion, is
\[
\boxed{r_{n+1}=-(\tfrac45+2y_n)r_n+\tfrac{100\delta}{9}y_n^2.}
\]
Since \(y_n\to0\), eventually the absolute value of the first coefficient is at most a fixed \(\rho<1\). The forcing is \(O(1/n)\) by step 2; a geometric convolution therefore proves \(r_n=O(1/n)\). To determine the sharp constant, multiply the last recurrence by \(n+1\). The bounded sequence \(u_n=nr_n\) obeys an asymptotically stable affine recurrence whose multiplier tends to \(-4/5\) and whose forcing tends to \((100\delta/9)(8/25)\). Elementary contraction of differences from the unique limiting affine fixed point gives
\[
\lim_{n\to\infty}nr_n
=\frac{(100\delta/9)(8/25)}{1+4/5}
=\frac{160\delta}{81}.
\]
Combining \(z_n=K y_n+r_n\) and
\[
x_{1,n}-x_{1,*}=\frac{z_n-y_n}{2},\qquad
x_{2,n}-x_{2,*}=\frac{-z_n-y_n}{2}
\]
proves the full vector limit and the transverse second-order limit. No higher-order expansion of the scalar critical orbit is used.

**4. Exactly two selective cancellations.** The first coordinate's leading coefficient is \((K-1)/2\), which vanishes precisely when \(K=1\), equivalently \(\delta=-9/28\) or \((c,d)=(3/14,15/28)\). Its remaining difference is then exactly \(r_n/2\); hence
\[
\lim_{n\to\infty}n(x_{1,n}-x_{1,*})=\frac12\cdot\frac{160(-9/28)}{81}=-\frac{20}{63}.
\]
The second coordinate's leading coefficient vanishes precisely when \(K=-1\), equivalently \(\delta=9/28\) or \((c,d)=(15/28,3/14)\). Its remaining difference is exactly \(-r_n/2\), and the same constant follows. For all other admissible coefficients the leading coefficient is nonzero, proving sharpness of the order-\(n^{-1/2}\) rate.

**5. Exceptional initial hyperplane.** If \(t_0=2/5\), then \(t_n=2/5\) identically and \(s_n-s_*=(-4/5)^n(s_0-s_*)\). This proves geometric relaxation, including the fixed-point initial state, and completes the boundary cases.

## Verification
Run `python verify.py` with Python 3 and SymPy installed. The checker verifies the triangular and transverse polynomial identities with exact symbolic arithmetic, checks the exact rational coefficients, and tests both selective ratios with long finite trajectories. Its success marker is `QUASI_NONVOLTERRA_SELECTIVE_RESONANCE_OK`. Finite trajectories corroborate only; all infinite-time conclusions follow from the analytic steps above. The checker evolves the reduced coordinates to avoid spurious floating-point drift away from the probability simplex.

## Relationship to prior work
Hardin and Rozikov introduce this quasi-strictly non-Volterra operator, and prove qualitative convergence at \(e=1/4\) for the \(a=\alpha=0\) subfamily (their Theorem 3 and Section 4). Their work does not state an original-generation sharp vector limit, the specific transverse \(n^{-1}\) coefficient, or the two admissible ratio cancellations. The general quadratic flip normal form already explains the scalar square-root decay mechanism, and that familiar mechanism alone is not the novelty claim here. The new part is its exact lift through asymmetric inheritance, followed by the unique, feasible two-to-five coefficient ratios at which one species has a strictly faster convergence power with an explicit nonzero constant. Khamrayev's 2019 quasi-strictly non-Volterra study concerns the different map \(V(x,y,z)=(x^2+(y+z)^2,2xz,2xy)\), so its fixed/periodic orbit classification cannot directly establish the stated coefficient-resolved result. Analogous critical Ricker-competition relaxation concerns exponential population updates rather than this polynomial stochastic operator.

## Limitations
The universal constants are special to \(e=1/4\) and \(a=\alpha=0\). When \(x_{3,0}=2/5\), the nonzero algebraic limits are replaced by geometric convergence, as explicitly proved. No uniform error estimate over arbitrary parameter sequences approaching the cancellation ratios is asserted. Similar scalar parabolic-flip asymptotics are standard, and priority for a fully general transverse normal-form theorem is not ruled out; the claimed contribution is the **specific exact coefficient and feasible ratio classification in this population operator**. The proof and reproducibility checks have not undergone independent mathematical validation.

## References
1. A. J. M. Hardin and U. A. Rozikov, *A quasi-strictly non-Volterra quadratic stochastic operator*, arXiv:1808.00229v1, first public 2018-08-01, https://arxiv.org/abs/1808.00229 ; later in *Qualitative Theory of Dynamical Systems* 18 (2019), 1013–1029, DOI:10.1007/s12346-019-00325-9.
2. A. Yu. Khamrayev, *On the dynamics of a quasistrictly non-Volterra quadratic stochastic operator*, *Ukrainian Mathematical Journal* 71 (2019), 1273–1281, https://umj.imath.kiev.ua/index.php/umj/article/view/1502 ; studied operator (6) differs from the operator here.
3. *Exact finite-time susceptibility crossover at a quadratic flip threshold*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-finite-time-susceptibility-crossover-at-a-quadratic-flip-t--acec857a2ec3 ; canonical scalar flip reference for comparison, not a same-system three-population theorem.
4. *Asymmetric critical synchronization and logarithmic relaxation in planar Ricker competition*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-asymmetric-critical-synchronization-and-logarithmic-relaxation-i--fbde7aa617eb ; analytically related critical relaxation in a different model.
