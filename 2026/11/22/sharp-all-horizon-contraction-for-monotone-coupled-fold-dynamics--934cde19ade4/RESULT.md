# Sharp all-horizon contraction for monotone coupled-fold dynamics

## Finding

Fix \(0<a\le1\). Let \(h:[0,\infty)\to[0,\infty)\) obey \(h(0)=0\) and, for all \(0\le s\le t\),
\[
a(t-s)\le h(t)-h(s)\le t-s.
\]
Define the coupled-fold map on the closed positive quadrant by
\[
F_h(u,v)=\bigl(|u-h(v)|,\ |v-h(u)|\bigr).
\]
For every integer \(n\ge0\) and all \(u,v\ge0\),
\[
\boxed{\|F_h^n(u,v)\|_\infty\le(1-a^2)^{\lfloor n/2\rfloor}\max\{u,v\}.}
\]
The constant at **every horizon** is best possible simultaneously over this entire class, even restricting to strictly positive starting coordinates (as a supremum). In fact the linear feedback \(h(t)=at\), started at \((1,0)\), attains equality at each \(n\).

For the particular smooth feedback
\[
h_*(t)=\log\!\left(\frac{1+e^t}{2}\right),\qquad t\ge0,
\]
the exact sharp supremum remains
\[
\boxed{\sup_{u,v>0}\frac{\|F_{h_*}^{n}(u,v)\|_\infty}{\max\{u,v\}}=\left(\frac34\right)^{\lfloor n/2\rfloor}\qquad(n\ge0).}
\]
For \(n\ge1\) this supremum is not attained by a strictly positive initial pair. This finite-time worst-case result is distinct from orbitwise asymptotic contraction rates.

## Assumptions and scope

The inequalities on \(h\) are **incremental** on the whole nonnegative half-line. Differentiability is not required. They imply \(at\le h(t)\le t\) and that \(t-h(t)\) is nondecreasing. The parameter \(a\) must be positive; no uniform exponential rate follows from the argument when \(a=0\). The norm is the sup norm relative to the origin, **not** a pairwise Lipschitz contraction inequality between arbitrary starting states. The conclusion is pointwise for every initial condition and simultaneously uniform over the feedback class.

For the two-player maximal-presence map at the critical resource value \(\alpha=2\), let \(x_n,y_n\in[1/2,1)\) denote its two maxima. Define \(u_n=\log(x_n/(1-x_n))\) and \(v_n=\log(y_n/(1-y_n))\). The logarithmic recurrence from [1, Lemma 3] is precisely \((u_{n+1},v_{n+1})=F_{h_*}(u_n,v_n)\). Hence every such orbit, including the diagonal and nonsymmetric initial conditions, has the explicit global bound
\[
\boxed{\max\{x_n,y_n\}-\frac12\le\frac14\left(\frac34\right)^{\lfloor n/2\rfloor}\max\left\{\log\frac{x_0}{1-x_0},\log\frac{y_0}{1-y_0}\right\}.}
\]
This last physical-coordinate inequality is useful as a convergence certificate; only the log-odds envelope is claimed to have the sharp stated constant.

## Proof

**1. Order of the folded image.** Fix \(x\ge y\ge0\). Since \(h(y)\le y\), the first output is \(A=x-h(y)\ge0\); set \(B=|y-h(x)|\). We prove \(A\ge B\). If \(y\ge h(x)\), then
\[
A-B=(x-y)+(h(x)-h(y))\ge0.
\]
If \(y<h(x)\), then
\[
A-B=(x-h(x))+(y-h(y))\ge0.
\]
Thus the larger coordinate is preserved (including ties), and
\[
\|F_h(x,y)\|_\infty=x-h(y)\le x.
\]
The same formula holds after swapping coordinates, so every step is nonexpansive relative to the origin.

**2. Exact two-step formula and contraction.** Applying the ordered-coordinate identity again, now to \((A,B)\), gives the exact identity
\[
\|F_h^2(x,y)\|_\infty
=x-h(y)-h(|y-h(x)|).
\]
The expression on the right is nonnegative by the order lemma (equivalently \(h(B)\le B\le A\)). Also, for any two nonnegative numbers \(y,z\), \(y+|y-z|\ge z\). With \(z=h(x)\),
\[
\begin{aligned}
h(y)+h(|y-h(x)|)
&\ge a\bigl(y+|y-h(x)|\bigr)\\
&\ge ah(x)\ge a^2x.
\end{aligned}
\]
Consequently \(\|F_h^2(x,y)\|_\infty\le(1-a^2)x\). Iterating the two-step bound and then using the one-step nonexpansiveness proves the claimed inequality for every \(n\), with the convention that the exponent zero gives one (including \(a=1\) at \(n=0,1\)).

**3. All-horizon sharpness.** For \(h(t)=at\), a direct calculation gives
\[
F_h(x,0)=(x,ax),\qquad F_h^2(x,0)=((1-a^2)x,0).
\]
Induction proves \(\|F_h^n(x,0)\|_\infty=(1-a^2)^{\lfloor n/2\rfloor}x\) for all \(n\). Continuity of each fixed iterate allows replacing the zero second coordinate by an arbitrarily small positive coordinate, so the same supremum holds over strictly positive starts.

**4. Sharpness for one fixed nonlinear model.** The smooth softplus function \(h_*\) has
\[
h_*'(t)=\frac{e^t}{1+e^t}\in[1/2,1),\quad h_*(0)=0,\quad h_*(t)=t/2+O(t^2)\ \text{as}\ t\downarrow0.
\]
It therefore meets the hypotheses with \(a=1/2\). The maps \(F_{h_*}(\varepsilon u,\varepsilon v)/\varepsilon\) converge locally uniformly as \(\varepsilon\downarrow0\) to \(F_{t/2}(u,v)\). Since absolute value is continuous and each finite iterate of a locally uniformly convergent family also converges on its finite limiting orbit, for every fixed integer \(n\), with initial states \((\varepsilon,\varepsilon^2)\),
\[
\lim_{\varepsilon\downarrow0}
\frac{\|F_{h_*}^n(\varepsilon,\varepsilon^2)\|_\infty}{\varepsilon}
=\left(\frac34\right)^{\lfloor n/2\rfloor}.
\]
This matches the universal upper bound. For \(n\ge2\), \(h_*(x)>x/2\) for every \(x>0\) makes the two-step inequality strict at every nonzero state. For \(n=1\), a strictly positive second input gives strict first-step decrease, and for larger odd \(n\) the strict two-step bound persists. Thus no positive state attains the sharp bound for \(n\ge1\).

**5. Original-coordinate estimate.** The inverse logit \(\sigma(t)=e^t/(1+e^t)\) satisfies \(0\le\sigma(t)-1/2\le t/4\) on \(t\ge0\), because \(0<\sigma'(t)\le1/4\). Apply this to each log-odds coordinate and the preceding estimate.

## Verification

The standalone standard-library program `checker.py` tests the finite-horizon bounds for linear, nonlinear smooth, and piecewise-linear admissible feedbacks, as well as \(h_*\), across randomly sampled states. Exact rational arithmetic verifies the linear extremizers for multiple \(a\) and horizons. Near-origin softplus experiments approach the sharp constant from below. Execute `python3 checker.py`. These finite tests are **not** proofs for infinitely many states or horizons; the proof is the five steps above.

## Relationship to prior work

Satur [1] introduces the planar maxima map, establishes global convergence at the critical parameter, and gives the logarithmic folded-coordinate recurrence. Its Jacobian determinant bound \(|\det DF|\le3/4\) [1, Lemma 3] is an **area** bound, not an upper bound on the sup-norm of an iterate. A related research note [2] obtains the orbitwise asymptotic two-step ratio \(3/4\) for asymmetric states and the asymptotic amplitude with a quadratic correction. Neither of these propositions by itself implies a uniform inequality at **every** finite horizon and every starting state, let alone the optimal rate \((1-a^2)^{\lfloor n/2\rfloor}\) throughout an infinite class of nonlinear feedbacks. The theorem here asserts that stronger, differently quantified finite-horizon guarantee, and does not repackage the known long-run orbitwise ratio as new.

## Limitations

This is a deterministic sup-norm bound toward a common fixed point, not a global contraction between arbitrary pairs, stochastic stability theorem or a claim about off-critical values of the resource parameter. Sharpness is a supremum for the fixed softplus map, approached close to the uniform state; the constant is not attained at any strictly positive finite state for positive time. The result does not reprove the sharper orbit-specific asymptotic amplitudes in [2]. General two-variable nonlinear contraction results could subsume parts of the abstract lemma; historical priority beyond the sources listed has not been independently settled.

## References

[1] O. R. Satur, *From oscillations to symmetry breaking in a two-dimensional piecewise-smooth dynamical system*, arXiv:2611.13318v1, posted 9 November 2026, https://arxiv.org/abs/2611.13318 .

[2] *Nonlinear critical-collapse amplitudes and a quadratic phase law in two-player maxima dynamics*, public research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-nonlinear-critical-collapse-amplitudes-and-a-quadratic-phase-law--8b71d315903b .
