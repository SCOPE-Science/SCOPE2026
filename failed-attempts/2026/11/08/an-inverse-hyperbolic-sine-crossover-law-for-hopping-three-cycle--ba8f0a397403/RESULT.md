# An inverse-hyperbolic-sine crossover law for hopping three-cycles in a sigmoid interval map

## Finding

Let \(\sigma(z)=1/(1+e^{-z})\) and consider the real Euler–Osipov–Söderbacka (EOS) interval map
\[
F_{a,b}(x)=x+b-\sigma(ax),\qquad a>0,\quad 0<b<1.
\]
Put \(\varepsilon_a=e^{-a/6}\), and for \(t\in\mathbb R\) define the detuned parameter
\[
b_a(t)=\frac13+\frac23\varepsilon_a t.
\]
Fix \(T>0\) and take \(a\) large enough that \(b_a(t)\in(0,1)\) for every \(|t|\le T\). Let \(c_0=-1/2\), \(c_1=-1/6\), \(c_2=1/6\).

**Three-cycle crossover theorem.** Uniformly for \(|t|\le T\), there is a unique primitive period-three orbit of \(F_{a,b_a(t)}\) in the three local windows \(|x_j-c_j|\le U/a\), for any fixed \(U>\operatorname{arsinh}(T)+1\) once \(a\) is sufficiently large. The ordered, cyclically labeled points \(x_0<x_1<x_2\) satisfy
\[
\boxed{a(x_j-c_j)=\operatorname{arsinh}(t)+O_T(a\varepsilon_a),\qquad j=0,1,2.}
\]
Its return multiplier \(\Lambda_a(t)=(F_{a,b_a(t)}^3)'(x_j)\) satisfies
\[
\boxed{1-\Lambda_a(t)=2a\varepsilon_a\sqrt{1+t^2}+O_T(a^2\varepsilon_a^2).}
\]
All three single-step derivatives, and hence the full multiplier, lie strictly between zero and one for large \(a\). The orbit is therefore locally attracting.

The points depend differentiably on \(b\) inside the detuning window, and for each \(j\in\{0,1,2\}\),
\[
\boxed{\frac{2a\varepsilon_a}{3}\frac{\partial x_j}{\partial b}\left(a,b_a(t)\right)
=\frac1{\sqrt{1+t^2}}+O_T(a\varepsilon_a).}
\]
In particular the derivative of every orbit coordinate at the rational center grows as
\[
\left.\frac{\partial x_j}{\partial b}\right|_{b=1/3}
\sim\frac{3}{2a}e^{a/6}.
\]
The inverse-hyperbolic-sine response gives a full nonlinear crossover across parameter changes of order \(e^{-a/6}\), not just an exploding derivative at one parameter value.

## Assumptions and scope

All limits take \(a\to+\infty\) at fixed \(T\); the local detuning coordinate \(t\) varies within \([-T,T]\). The theorem is local to the three specified windows about the half-grid. A point \(x_j\) is labeled so that \(F(x_0)=x_1\), \(F(x_1)=x_2\), \(F(x_2)=x_0\). The derivative \(\partial_b x_j\) is taken at fixed \(a\) on this smooth local periodic branch. Uniform constants may depend on \(T\) and on the fixed window radius \(U\), not on \(a\) or \(t\). We make no assertion about arbitrary coexisting cycles outside the windows.

## Proof

Write \(\varepsilon=e^{-a/6}\), \(\delta=(2/3)\varepsilon t\), and parametrize the first point by \(x_0=-1/2+u/a\). On each compact rectangle \(|u|\le U\), \(|t|\le T\), we have
\[
\sigma(ax_0)=O_{T,U}(\varepsilon^3),\qquad
x_1:=F(x_0)=-\frac16+\frac{u}{a}+O_{T,U}(\varepsilon),
\]
and, using the exponential tails of \(\sigma\),
\[
\sigma(ax_1)=\varepsilon e^{u}\bigl(1+O_{T,U}(a\varepsilon)\bigr),
\]
\[
x_2:=F(x_1)=\frac16+\frac{u}{a}+O_{T,U}(\varepsilon),\qquad
1-\sigma(ax_2)=\varepsilon e^{-u}\bigl(1+O_{T,U}(a\varepsilon)\bigr).
\]
These estimates also hold after one derivative with respect to \(u\) or \(t\) (allowing the same \(O_{T,U}(a\varepsilon)\) error). For instance, \(ax_1=-a/6+u+O_{T,U}(a\varepsilon)\), and the normalized logistic tail is analytic in its small exponential argument; differentiating this representation proves the claimed uniform derivative estimates. Moreover \(x_2\) remains positive and the first two points negative for large \(a\), so the itinerary does not change.

The exact three-step displacement, with \(3b-1=2\varepsilon t\), is
\[
F^3(x_0)-x_0=2\varepsilon t-\sigma(ax_0)-\sigma(ax_1)+[1-\sigma(ax_2)].
\]
Consequently the normalized return equation has the uniform \(C^1\) asymptotic
\[
H_a(u,t):=\frac{F^3(-1/2+u/a)-(-1/2+u/a)}{\varepsilon}
=2(t-\sinh u)+O_{T,U}(a\varepsilon).
\]
Its \(u\)-derivative is \(-2\cosh u+O_{T,U}(a\varepsilon)<0\) on the fixed rectangle. Choose \(U>\operatorname{arsinh}(T)+1\). The values \(H_a(-U,t)\) and \(H_a(U,t)\) have opposite signs for every \(|t|\le T\), uniformly for large \(a\). The intermediate value theorem and strict monotonicity produce exactly one root \(u_a(t)\in(-U,U)\), continuously differentiable in \(t\). By the mean value theorem,
\[
u_a(t)=\operatorname{arsinh}(t)+O_T(a\varepsilon),\qquad
\frac{du_a}{dt}=\frac1{\sqrt{1+t^2}}+O_T(a\varepsilon).
\]
All three orbit coordinates follow from the displayed step estimates, and their corrections obey \(a(x_j-c_j)=u_a(t)+O_T(a\varepsilon)\). The three disjoint windows imply primitive period exactly three.

Since \(u=a(x_0+1/2)\), differentiating the normalized return displacement in \(u\) at the root yields
\[
\Lambda_a(t)-1=a\varepsilon\,\partial_uH_a(u_a(t),t)
=-2a\varepsilon\sqrt{1+t^2}+O_T(a^2\varepsilon^2).
\]
At each orbit point the logistic derivative \(F'(x)=1-a\sigma(ax)(1-\sigma(ax))\) is strictly between zero and one for sufficiently large \(a\) because its largest correction is \(O_T(a\varepsilon)\). This establishes attraction.

Finally \(db_a/dt=2\varepsilon/3\) and \(x_0=-1/2+u_a(t)/a\), so
\[
\frac{2a\varepsilon}{3}\frac{\partial x_0}{\partial b}=\frac{du_a}{dt}
=\frac1{\sqrt{1+t^2}}+O_T(a\varepsilon).
\]
For \(x_1=F(x_0)\), the additional partial derivative of \(F\) with respect to \(b\) is exactly one; its scaled contribution is \(O(a\varepsilon)\), and \(F'(x_0)=1+O(a\varepsilon^3)\). The same reasoning for \(x_2=F(x_1)\), with \(F'(x_1)=1+O(a\varepsilon)\), proves the stated limit uniformly for all three coordinates. Setting \(t=0\) gives the exponentially growing central susceptibility.

## Verification

The companion `check_eos_crossover.py` uses 95-digit arithmetic to solve the original three-step equation (not the limiting equation) for 25 pairs \((a,t)\) with \(a\in\{45,60,90,120,180\}\) and \(t\in\{-3,-1,0,1,3\}\). It verifies the original periodic residual, primitive itinerary, local stability and convergence of both the multiplier and the exact implicit-derivative response to the displayed asymptotics. Its successful run prints `VERIFY_OK high_precision_period_three_and_response_cases=25 precision_digits=95`. The finite tests supplement, not replace, the uniform analytic proof.

## Relationship to prior work

Bielawski, Chotibut, Falniowski, Misiurewicz and Piliouras [1] analyze strange EOS bifurcation diagrams and explain why periodic points move unusually rapidly near \(b=1/3\); their reported hopping behavior motivates a quantitative two-parameter asymptotic. Their earlier paper [2] gives existence and near-global attraction for fixed rational rotation parameters, not the present detuning profile. The published note [3] gives the sharp multiplier gap and half-grid displacement at a *fixed* rational \(b=k/n\). Its \(n=3\) case agrees with this theorem at \(t=0\), but it does not imply the uniform nonlinear \(\operatorname{arsinh}(t)\) profile or the full detuned sensitivity function. This finding is restricted to the new two-parameter singular layer and does not present those previously established fixed-parameter results as new.

## Limitations

The crossover is proved on each fixed compact set of rescaled detunings \(t\), not uniformly for \(|t|\to\infty\). Local uniqueness and attraction are established only for the specified half-grid orbit, not every possible periodic orbit. The result does not establish a full parameter window boundary, a global basin-entry time, or behavior for other rational rotation numbers. Comparison with broader work on singularly smoothed rotations may still reveal an equivalent crossover theorem; independent historical-priority review has not been performed.

## References

[1] J. Bielawski, T. Chotibut, F. Falniowski, M. Misiurewicz and G. Piliouras, *Strange bifurcation diagrams*, arXiv:2605.19756v1 (first public May 19, 2026), especially the period-three hopping discussion. https://arxiv.org/abs/2605.19756

[2] The same authors, *Interval maps mimicking circle rotations*, arXiv:2411.01495v1 (first public November 3, 2024), Sections 3–5. https://arxiv.org/html/2411.01495v1

[3] *Singular half-grid selection and exponentially weak attraction in rational EOS maps* (2026), public result and proof, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-singular-half-grid-selection-and-exponentially-weak-attraction-i--b03eb35b1a55
