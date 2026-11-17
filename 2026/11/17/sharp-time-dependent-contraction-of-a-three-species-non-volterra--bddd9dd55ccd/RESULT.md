# Sharp time-dependent contraction of a three-species non-Volterra quadratic flow

## Finding
For the symmetric three-component quadratic differential system below, the globally best Euclidean Lipschitz constant of the **nonlinear flow map** has the closed form
\[
\operatorname{Lip}(\Phi_t)=\frac{16e^{2t}}{(1+3e^{2t})^2},\qquad t\geq0.
\]
In particular it is strictly below \(1\) for positive times, has initial logarithmic slope \(-1\), and is asymptotic to \((16/9)e^{-2t}\). The constant is optimal for **each** nonnegative time, not merely as a uniform exponential estimate. The almost-extremizing initial pairs approach a simplex vertex along the median to the barycenter.

## Assumptions and scope
Let \(\Delta=\{(x_0,x_1,x_2)\in[0,1]^3:x_0+x_1+x_2=1\}\), with its ordinary Euclidean distance inherited from \(\mathbb R^3\). The autonomous ODE is
\[
\dot x_i=\frac{x_j^2+x_k^2}{2}+2x_jx_k-x_i,\qquad\{i,j,k\}=\{0,1,2\}.
\]
The right-hand side preserves \(\sum_i x_i=1\), and points inward on every boundary face; hence its solution flow \(\Phi_t:\Delta\to\Delta\) is defined for every \(t\ge0\). The Lipschitz constant means the supremum of \(\|\Phi_t(p)-\Phi_t(q)\|_2/\|p-q\|_2\) over distinct \(p,q\in\Delta\). No claim is made for unconstrained initial points outside the simplex.

## Proof
Set
\[
 u=3(x_0+x_1)-2,\qquad v=x_0-x_1,\qquad z=u+i\sqrt3\,v.
\]
The simplex maps bijectively onto an equilateral triangle whose vertices are \(-2,1+i\sqrt3,1-i\sqrt3\). For every pair of simplex points, \(|z(p)-z(q)|^2=6\|p-q\|_2^2\); thus flow Lipschitz ratios are unchanged. Direct expansion of the quadratic vector field gives
\[
 \dot u=-2u-\frac{u^2}{4}+\frac{3v^2}{4},\qquad
 \dot v=-2v+\frac{uv}{2},\qquad
 \dot z=-2z-\frac{\overline z^{\,2}}4.
\]
For \(r=|z|>0\), using the upper Dini derivative at the origin if necessary,
\[
 \dot r=-2r-\frac{r^2}{4}\cos(3\arg z)
 \le -2r+\frac{r^2}{4}.
\]
All simplex initial data have \(r(0)\le2\). Scalar comparison with the solution started at \(2\) yields the **uniform sharp radial envelope**
\[
 r(t)\le R(t)=\frac{8}{1+3e^{2t}}.
\]
Now consider any two solutions \(z_1,z_2\) and their difference \(w=z_1-z_2\). Its equation factors exactly:
\[
 \dot w=-2w-\frac{\overline{z_1}+\overline{z_2}}4\overline w.
\]
For nonzero \(w\), taking the real inner product with \(w/|w|\) gives
\[
 \frac{d}{dt}|w|\le\left(-2+\frac{|z_1|+|z_2|}{4}\right)|w|
 \le\left(-2+\frac{R(t)}2\right)|w|.
\]
The same inequality holds through coincidences by continuity. Integration provides
\[
 |w(t)|\le e^{-2t}\exp\!\left(\int_0^t\frac{4}{1+3e^{2s}}\,ds\right)|w(0)|
 =\frac{16e^{2t}}{(1+3e^{2t})^2}|w(0)|.
\]
To prove **optimality**, restrict the flow to the median \(z=-r\), \(0\le r\le2\). The scalar equation is \(\dot r=-2r+r^2/4\), with the exact solution for initial value \(r_0\):
\[
 r(t;r_0)=\frac{8r_0}{r_0+(8-r_0)e^{2t}}.
\]
The derivative in \(r_0\) at the endpoint \(r_0=2\) equals
\[
 \left.\partial_{r_0}r(t;r_0)\right|_{r_0=2}
 =\frac{16e^{2t}}{(1+3e^{2t})^2}.
\]
Taking initial points on this median at \(r_0=2\) and \(r_0=2-\varepsilon\), then letting \(\varepsilon\downarrow0\), attains the upper bound as a supremum. This also holds at \(t=0\). This proves the stated exact profile for every \(t\ge0\).

## Verification
The standalone `proof_check.py` verifies symbolically the coordinate reduction and metric factor, the sharp scalar radial solution and its endpoint derivative, and the algebraic identity for the integrated Lipschitz coefficient. It also integrates the original three-species ODE for several random simplex pairs to check the inequality numerically. Numerical tests are corroboration, not substitutes for the analytic comparison and sharpness proof.

## Relationship to prior work
Rasulov (2022) introduced and studied this continuous-time strictly non-Volterra quadratic stochastic operator, its invariant simplex, equilibria, and explicit solutions on symmetry lines. The 2022 discussion does not give the optimal time-dependent Lipschitz norm of its nonlinear flow. The later Rasulov (2026) article addresses analytic solutions and convergence for a class of such systems; its accessible abstract does not state this sharp all-initial-pair contraction profile. The exact profile uses, but is not implied numerically by, the known diagonal solution alone: the global inequality and attainment of its supremum are both necessary. General convex-gradient contraction principles alone give the weaker \(e^{-t}\) estimate, not the exact optimal function.

## Limitations
The theorem concerns the continuous-time flow on the **closed** probability simplex with Euclidean distance, not a discrete quadratic operator, its extension to all of \(\mathbb R^3\), or other metrics. The supremum for positive times is obtained as a limit of pairs, not asserted to be attained by distinct points. The 2026 follow-up's full text was inaccessible and could contain related estimates; publication priority therefore warrants further expert review. No independent validation has been performed.

## References
- X. R. Rasulov, “Qualitative analysis of strictly non-Volterra quadratic dynamical systems with continuous time,” *Communications in Mathematics* **30** (2022), 239–250; arXiv:2211.06186, first posted 2022-11-11; DOI: 10.46298/cm.10528. Primary full text: https://cm.episciences.org/10528/pdf .
- X. R. Rasulov, “On the Analytical Solution of a Class of Strictly Non-Volterra Quadratic Stochastic Operators with Continuous Time,” *Differential Equations* **62** (2026), 318–339, DOI: 10.7868/S3034503026030038; accessible abstract: https://journals.rcsi.science/0374-0641/article/view/427038 .
