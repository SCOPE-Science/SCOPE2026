# Critical coexistence rigidity and an exact prey-fluctuation law in a three-species flow

## Finding
For the positive Samardzija–Greller system
\[
\dot x=x(1-y+cx-a xz),\qquad
\dot y=y(x-1),\qquad
\dot z=z(a x^2-b),
\]
with fixed \(a,b,c>0\), suppose a forward solution eventually remains in a compact subset of the strictly positive octant. Then:

1. **Below the critical ratio, \(b<a\), such a solution cannot exist.** In particular there is no compact invariant set contained in the positive octant.
2. **At the critical ratio, \(b=a\), every such solution converges to one single equilibrium** \((1,Y,Z)\), where \(Y,Z>0\) and \(Y+aZ=1+c\). Every positive compactly supported invariant probability measure is a mixture of atoms on this equilibrium segment; its ergodic invariant probabilities are exactly the point masses on the segment.
3. **Above the critical ratio, \(b>a\), every such solution obeys the universal asymptotic laws**
\[
\lim_{T\to\infty}\frac1T\int_0^T x(t)\,dt=1,\qquad
\lim_{T\to\infty}\frac1T\int_0^T (x(t)-1)^2\,dt=\frac ba-1.
\]
Writing \(m=\liminf_{t\to\infty}x(t)\) and \(M=\limsup_{t\to\infty}x(t)\), it follows that
\[
0<m<1<M,\qquad (M-1)(1-m)\ge\frac ba-1,\qquad
M-m\ge 2\sqrt{\frac ba-1}.
\]
This exact long-time fluctuation budget and the amplitude floor are independent of \(c\), whether the recurrent behavior is periodic, quasiperiodic or otherwise. The assertion is conditional on compact positive persistence and does not assert its existence for \(b>a\).

## Assumptions and scope
Solutions start at arbitrary \((x(0),y(0),z(0))\in(0,\infty)^3\), remain classical and positive on \([0,\infty)\), and for some \(t_0\) obey \(0<\epsilon\le x(t),y(t),z(t)\le R<\infty\) whenever \(t\ge t_0\). For polynomial ODEs, positivity is preserved along a classical solution because every component has a multiplicative factor of its own density; forward existence and boundedness are included explicitly rather than inferred globally. The formulae remain valid under any fixed \(c\) for which the hypotheses hold, but \(c>0\) matches the biological model.

The earliest publicly dated motivating integrability study is Karim, Amen and Aziz, arXiv:2308.13284, posted 2023-08-25. The original Samardzija–Greller ecological model dates to 1988 and is credited separately; the claim is about recurrent time averages and critical convergence, not the discovery of that model or the qualitative location of its old bifurcation diagram.

## Proof
The two logarithmic identities are valid for every positive trajectory:
\[
\frac{d}{dt}\log y=x-1,\qquad
\frac{d}{dt}\left(\log z-2a\log y\right)
=a(x-1)^2+a-b.
\tag{1}
\]
Indeed, subtracting twice \(a\dot y/y\) from \(\dot z/z\) gives \(ax^2-b-2a(x-1)=a(x-1)^2+a-b\). Set \(W(t)=\log z(t)-2a\log y(t)\). Integration gives the exact finite-horizon budgets
\[
\frac1T\int_0^T x(t)\,dt=1+\frac{\log y(T)-\log y(0)}{T},
\]
\[
\frac1T\int_0^T(x(t)-1)^2\,dt
=\frac ba-1+\frac{W(T)-W(0)}{aT}.
\tag{2}
\]
Eventual compact positive containment makes \(W\) and \(\log y\) bounded. Therefore both endpoint terms vanish after division by \(T\). If \(b<a\), (1) instead forces \(W(t)\ge W(0)+(a-b)t\) even without assuming boundedness of \(x\), contradicting eventual boundedness of \(W\). This proves the first claim and the two asymptotic budgets.

If \(b=a\), (1) shows that \(W\) increases and has a finite limit, and that \(\int_0^\infty (x(t)-1)^2\,dt<\infty\). Since the trajectory eventually lies in a fixed compact positive set, the polynomial vector field and its derivatives are bounded there. In particular \(x(t)-1\) is uniformly continuous. A uniformly continuous function with finite square integral converges to zero, so \(x(t)\to1\). Also \(\ddot x(t)\) is bounded, and a differentiable convergent function whose derivative is uniformly continuous has derivative tending to zero; hence \(\dot x(t)\to0\). The first ODE now gives \(y(t)+az(t)\to1+c\). Since \(W(t)\to W_\infty\), the pair \((y(t),z(t))\) must converge to the unique positive solution of
\[
Y+aZ=1+c,\qquad \log Z-2a\log Y=W_\infty.
\]
Uniqueness follows because \(Z=(1+c-Y)/a\) and \(Y\mapsto\log((1+c-Y)/a)-2a\log Y\) is strictly decreasing from \(+\infty\) to \(-\infty\) on \((0,1+c)\). The limit point solves all three ODEs, establishing pointwise convergence.

For the invariant-measure statement at \(b=a\), integrate the continuous bounded derivative \(\dot W=a(x-1)^2\) against a probability measure invariant under the flow and supported on a compact subset of the positive octant: invariance gives \(\int(x-1)^2d\mu=0\). Thus \(x=1\) on its support. Invariance also forces \(\dot x=0\) there, hence \(y+az=1+c\). Conversely each point of this line is fixed, so every probability measure supported on it is invariant, and its ergodic measures are precisely its point masses.

For \(b>a\), the limits from (2) imply \(\overline x=1\) and \(\overline{x^2}=b/a\). Since \(m\) and \(M\) are finite eventual extrema, \((M-x(t))(x(t)-m)\ge0\) asymptotically (with arbitrarily small endpoint enlargements). Averaging and passing to the limit yields \(b/a\le M+m-mM\), i.e. \((M-1)(1-m)\ge b/a-1>0\). The mean constraint forces \(m<1<M\): otherwise bounded one-sided deviations with mean tending to one would have vanishing mean square. Finally the arithmetic–geometric mean inequality gives \(M-m=(M-1)+(1-m)\ge2\sqrt{b/a-1}\). Strict positivity of \(m\) follows from compact positive containment. This completes the proof.

## Verification
A standalone standard-library Python checker, `verify.py`, checks exact rational evaluations of both logarithmic identities at 144 rational parameter/state tuples, checks the critical equilibrium and characteristic-polynomial identities at rational points, and runs a bounded numerical trajectory near a normally attracting point of the critical equilibrium segment. The checker prints `THREE_SPECIES_CRITICAL_BUDGET_OK`. The finite arithmetic and integration tests are diagnostics only; the proof above establishes the quantified statements for all admissible parameters and positive persistent solutions.

The original-time logarithmic identities also give reproducible finite-horizon residual diagnostics: the difference between the measured mean square and \(b/a-1\) must be exactly \((W(T)-W(0))/(aT)\), and the mean-prey error must be exactly \((\log y(T)-\log y(0))/T\).

## Relationship to prior work
Samardzija and Greller (1988) introduced the model and its stability/chaos parameter diagram; the location \(b/a=1\) of a qualitative change is **not** claimed as new. Karim, Amen and Aziz (arXiv:2308.13284, 2023) study algebraic and analytic integrability, especially the absence of several types of first integrals when \(a,c>0\). Their source text does not assert the exact all-orbit prey-variance budget, the global critical interior convergence statement, or the amplitude floor. Fractional-order and controlled versions study different evolution operators and do not entail these identities. Other known predator–prey variance identities concern different equations and cannot imply these particular formulas through parameter relabeling.

## Limitations
Compact positive persistence is required; a bounded positive solution approaching a coordinate plane is not covered by the convergence and long-time average statements. No claim is made that every parameter choice with \(b>a\) has a positive persistent orbit. The original 1988 full paper could not be fully inspected during this comparison, despite an available listing, so an equivalent earlier derivation remains a publication-priority risk. No independent audit or external validation has been performed.

## References
- A. Karim, A. Amen, W. Aziz, *Integrability of a Family of Lotka–Volterra Three Species Biological System*, arXiv:2308.13284, version 1 dated 2023-08-25, https://arxiv.org/abs/2308.13284.
- N. Samardzija and L. D. Greller, *Explosive route to chaos through a fractal torus in a generalized Lotka–Volterra model*, Bulletin of Mathematical Biology 50 (1988), 465–491, https://doi.org/10.1007/BF02458847.
- *Dynamics, Chaos Control, and Synchronization in a Fractional-Order Samardzija–Greller Population System with Order Lying in (0, 2)*, 2018, https://doi.org/10.1155/2018/6719341.
- A. Karim, A. Amen, W. Aziz, *Integrability and Center Analysis of a Family of Lotka–Volterra Three-Species Biological System*, published 2025, https://doi.org/10.1002/mma.11074.
