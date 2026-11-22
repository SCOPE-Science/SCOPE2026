# Critical square-root escape and logarithmic phase delay in a symmetric sine-offset map

## Finding

At the resonant coupling \(a=-1\) of the planar sine-offset map of Ge, Li, Li, Zhang and Tao (2023), there is an exact global alternative between one-step capture by a line of fixed points and universal subballistic escape. Every escaping orbit has the same sharp square-root drift, and its contracting phase carries a logarithmic second-order correction.

Let \(u_0=x_0+y_0\). If \(\sin u_0=0\), the orbit lands on the fixed line after at most one step. Otherwise put \(s=\operatorname{sgn}(\sin u_0)\). Then

\[
\lim_{n\to\infty}n u_n^2=3,\qquad
\lim_{n\to\infty}\left(\frac{1}{u_n^2}-\frac n3-\frac15\log n\right)=C(u_0)\in\mathbb R.
\]

Moreover, for a finite constant \(L=L(x_0,u_0)\),

\[
x_n=2s\sqrt{3n}+L+O\!\left(\frac{\log n}{\sqrt n}\right),\qquad
y_n=-2s\sqrt{3n}-L+O\!\left(\frac{\log n}{\sqrt n}\right).
\]

Exactly the initial lines \(x_0+y_0\in\pi\mathbb Z\) have bounded forward orbits. Every periodic point is fixed, and every invariant Borel probability measure is supported on the line of fixed points.

## Assumptions and scope

The state space is \(\mathbb R^2\), with exact real arithmetic. The governing map is

\[
F_a(x,y)=(x+\sin(x+y),\,a x),
\]

and the parameter is fixed at the singular offset-resonance \(a=-1\). Here \(n\ge0\) is the iterate index, \(u_n=x_n+y_n\), and \(\operatorname{sgn}\) means the sign of a nonzero real number. Constants in the asymptotic remainder may depend on the initial state. No compactification of escaping orbits is used. The map is well defined for all initial states.

## Proof

**1. Exact reduction and exceptional states.** With \(a=-1\), direct substitution gives

\[
u_{n+1}=x_{n+1}+y_{n+1}=\sin u_n,\qquad
x_{n+1}=x_n+u_{n+1},\qquad y_{n+1}=-x_n.
\]

If \(\sin u_0=0\), then \(u_1=0\), so \(x_n=x_1\), \(y_n=-x_1\) for every \(n\ge1\). These initial conditions are exactly \(u_0\in\pi\mathbb Z\). Points on the fixed line \(u=0\) are fixed. If \(\sin u_0\ne0\), then \(u_1\in[-1,1]\setminus\{0\}\), and the inequality \(0<|\sin t|<|t|\) for \(0<|t|\le1\) shows that the sign of \(u_n\) is fixed and \(|u_n|\searrow0\). The only possible limit is zero.

**2. The critical phase and the logarithmic term.** For \(n\ge1\) define \(v_n=u_n^{-2}\). The expansion of the analytic function \(\csc^2 t-t^{-2}\) at zero is

\[
\frac1{\sin^2t}-\frac1{t^2}=\frac13+\frac{t^2}{15}+O(t^4).
\]

Therefore \(v_{n+1}-v_n=\frac13+\frac1{15}u_n^2+O(u_n^4)\). Since \(u_n\to0\), Cesàro averaging first yields \(v_n/n\to1/3\), hence \(u_n^2\sim3/n\). Summing the refined increments gives \(v_n=n/3+O(\log n)\), so

\[
u_n^2=\frac3n+O\!\left(\frac{\log n}{n^2}\right).
\]

Consequently the successive differences of \(v_n-n/3-(\log n)/5\) are \(O((\log n)/n^2)\): indeed \(u_n^2/15=1/(5n)+O((\log n)/n^2)\), and \(\log(n+1)-\log n=1/n+O(n^{-2})\). The differences form an absolutely summable series, proving convergence to a finite \(C(u_0)\). Taking square roots also gives

\[
u_n=s\sqrt{\frac3n}+O\!\left(\frac{\log n}{n^{3/2}}\right).
\]

**3. Escape, finite drift constant, and invariant probabilities.** Telescoping the first-coordinate update gives \(x_n=x_0+\sum_{j=1}^{n}u_j\). By the final estimate, the series \(\sum_{j\ge1}(u_j-s\sqrt{3/j})\) is absolutely convergent. In addition the limit

\[
c_{1/2}=\lim_{n\to\infty}\left(\sum_{j=1}^n j^{-1/2}-2\sqrt n\right)
\]

exists by integral comparison. Thus the finite number

\[
L=x_0+s\sqrt3\,c_{1/2}+\sum_{j=1}^{\infty}\left(u_j-s\sqrt{\frac3j}\right)
\]

satisfies \(x_n-2s\sqrt{3n}\to L\). Integral remainder estimates for the two convergent series sharpen the error to \(O((\log n)/\sqrt n)\). Since \(y_n=-x_{n-1}\), the corresponding formula for \(y_n\) follows. The first coordinate therefore tends to infinity with sign \(s\), proving that every nonexceptional orbit is unbounded and nonrecurrent.

The only recurrent points are the fixed line \(u=0\): nonexceptional points escape, while exceptional points outside the fixed line reach it in one step and never return. Poincaré recurrence for invariant probability measures implies every invariant Borel probability is supported on the fixed line. Conversely, any Borel probability concentrated there is invariant, since the map fixes every point on that line. All periodic points consequently are fixed.

## Verification

The identity \(u_{n+1}=\sin u_n\) is exact, and the logarithmic coefficient \(1/5\) follows from the explicit Taylor coefficient \(1/15\) and \(u_n^2\sim3/n\). The proof, not finite iteration, establishes all infinite-time statements. Reproducible numerical and symbolic diagnostics are supplied in `sine_resonance_checker.py`; run using `python sine_resonance_checker.py` in a standard Python environment, optionally with SymPy. These diagnostics compare several orbits at 50,000, 100,000 and 200,000 iterates, but their finite nature does not substitute for the proof.

## Relationship to prior work

Ge et al. introduced the sine-offset map and studied offset boosting, coexistence, bifurcations, implementation and pseudorandom sequences. Their parameter-oriented shift formula divides by \(a+1\); the present result instead treats the excluded resonant value \(a=-1\) and proves an all-initial-state orbit classification, sharp escape exponent, logarithmic phase correction and stationary-measure classification. The sine-recursion Taylor expansion is a standard local analytic tool, not claimed as a new method. A 2022 work by Li et al. studies related self-reproducing sinusoidal hyperchaotic maps; its abstract was available, but its full text was not compared and remains a priority risk.

## Limitations

The statement is confined to the full real plane at \(a=-1\) and exact real arithmetic; floating-point trajectories near the exceptional lines can appear escaping because a rounded multiple of \(\pi\) need not have exactly zero sine. There are no claims about the hyperchaotic regimes \(a\ne-1\), parameter stability, typical physical attractors there, or cryptographic security. Publication priority relative to inaccessible or unindexed literature is not established. No independent review is represented.

## References

1. X. Ge, C. Li, Y. Li, C. Zhang, C. Tao, *Multiple Alternatives of Offset Boosting in a Symmetric Hyperchaotic Map*, Symmetry **15** (2023), 712, published 13 March 2023, https://doi.org/10.3390/sym15030712 .
2. Y. Li, C. Li, S. Zhang, G. Chen, Z. Zeng, *A Self-Reproduction Hyperchaotic Map With Compound Lattice Dynamics*, IEEE Trans. Industrial Electronics **69** (2022), 10564–10572, https://doi.org/10.1109/TIE.2022.3144592 .
