# A universal second-order bias in quasi-static adaptive SIS clearance at the rewiring cusp

## Finding

At the degenerate disease-free onset of the adaptive susceptible–infected–susceptible (SIS) **pair-closure** equations described below, the full three-dimensional flow and its quasi-static fast-variable reduction agree on the leading infection-clearance law but disagree at the next order. For any mean degree \(n>1\) and recovery rate \(\gamma>0\), at the critical parameters
\[
 w_* = \frac{\gamma(n+1)}{n-1},\qquad \tau_* = \frac{2\gamma}{n-1},
\]
all sufficiently close initial conditions with positive prevalence that remain in the local physical domain obey
\[
\begin{split}
 x_{\mathrm{full}}(t)&=\sqrt{\frac{n}{2\gamma(n-1)}}t^{-1/2}
    +\frac{n-2}{2\gamma(n-1)}t^{-1}+O(t^{-3/2}\log t),\\
 x_{\mathrm{qs}}(t)&=\sqrt{\frac{n}{2\gamma(n-1)}}t^{-1/2}
    +\frac{n-3}{4\gamma(n-1)}t^{-1}+O(t^{-3/2}\log t).
\end{split}
\]
Thus the same positive initial prevalence (with fast variables chosen on the quasi-static branch for the reduced equation) leads to the universal asymptotic difference
\[
\boxed{\displaystyle\lim_{t\to\infty}t\bigl(x_{\mathrm{full}}(t)-x_{\mathrm{qs}}(t)\bigr)=\frac1{4\gamma}.}
\]
It is independent of \(n\) and the local initial condition. For \(2<n<3\), the full second-order coefficient is *positive*, whereas the quasi-static coefficient is *negative*; the reduction even gets the correction's direction wrong. For example, at \(n=5/2\) and \(\gamma=1\), they are respectively \(1/6\) and \(-1/12\), despite the shared leading coefficient \(\sqrt{5/6}\).

## Assumptions and scope

Use the adaptive-network pair approximation in Hébert-Dufresne, Simon and Kiss (2026), Appendix 6.2.3. Let \(x\) denote infected-node prevalence, \(p=\langle SI\rangle/\langle I\rangle\) and \(q=\langle II\rangle/\langle I\rangle\) be their conditional pair coordinates; \(n>1\) is mean network degree. The deterministic closure, on a neighborhood of the stated disease-free correlation state with \(0\le x<1\), is
\[
\begin{aligned}
\dot x={}&x(\tau n p-\gamma),\\
\dot p={}&\gamma q+[\tau(n-1)-w]p-\tau n p^2
   +\tau n p(1-3p-q)\frac{x}{1-x},\\
\dot q={}&-\gamma q+2\tau p-\tau n p q
    +2\tau n p^2\frac{x}{1-x}.
\end{aligned}
\]
Here \(\gamma>0\) is recovery, \(w>0\) is adaptive rewiring, and \(\tau>0\) is per-link transmission. At the critical parameters above, the disease-free correlation equilibrium is
\[
 (x,p,q)=\left(0,\frac{n-1}{2n},\frac1n\right).
\]
The theorem is **local**, for every sufficiently near initial state in the model's physical coordinate domain with \(x(0)>0\); it is not a global epidemiological statement. For the quasi-static comparison, let \(p_{\rm qs}(x),q_{\rm qs}(x)\) be the smooth positive branch, continuous at the same disease-free correlation state, obtained by solving \(\dot p=\dot q=0\) while holding \(x\) fixed. The reduced scalar equation is \(\dot x=x(\tau n p_{\rm qs}(x)-\gamma)\). Its solutions start at sufficiently small positive \(x\), independently of the full system's initial fast state. Both asymptotics hold for every such choice.

## Proof

**1. Center and stable directions.** Put \(a=(n-1)/(2n)\) and \(c=1/n\). At \(w=w_*\), \(\tau=\tau_*\), the linearization has one zero eigenvalue and a stable fast block in \((p,q)\):
\[
J_f=\begin{pmatrix}
-\gamma(n+1)/(n-1)&\gamma\\
2\gamma/(n-1)&-2\gamma
\end{pmatrix},\quad
\operatorname{tr}J_f=-\frac{\gamma(3n-1)}{n-1}<0,\quad
\det J_f=\frac{2\gamma^2n}{n-1}>0.
\]
The plane \(x=0\) is invariant and locally equals the strong-stable manifold. The smooth one-dimensional center manifold can be represented as \(p=p(x)\), \(q=q(x)\), tangent to \((1,0,(n-1)/(2n))\). Because the vector field is analytic near \(x=0\), its center-manifold Taylor jets through the required order exist and are uniquely fixed by the invariance equation.

**2. Full-flow invariant graph.** Substitute
\[
\begin{aligned}
p(x)&=a+b_2x^2+b_3x^3+O(x^4),\\
q(x)&=c+\frac{n-1}{2n}x+c_2x^2+c_3x^3+O(x^4)
\end{aligned}
\]
into the *full* invariance equations \(p'(x)\dot x=\dot p\) and \(q'(x)\dot x=\dot q\). The coefficients of \(x^2\) give
\[
 b_2=-\frac{(n-1)^2}{2n^2},\qquad c_2=\frac{(n-1)^2}{2n^2},
\]
and those of \(x^3\) give
\[
 b_3=\frac{(n-2)(n-1)^2}{2n^3},\qquad c_3=\frac{(n-1)^2}{n^3}.
\]
The standalone exact checker reconstructs these from the original two polynomial/rational equations, rather than assuming the result. Substitution into the first equation produces the scalar center flow
\[
\dot x=-Kx^3+Ex^4+O(x^5),\qquad
K=\frac{\gamma(n-1)}n>0,\qquad
E=\frac{\gamma(n-1)(n-2)}{n^2}.
\]
In particular the formerly quadratic damping vanishes *exactly* at the codimension-two point, and cubic damping is strictly negative. On the positive center branch all small trajectories decrease to zero. Stable-manifold contraction brings every sufficiently close positive-prevalence initial state exponentially near a center trajectory, and the only local strong-stable points have \(x=0\); hence the same asymptotics hold for all the initial states stated in the theorem.

**3. Converting the center dynamics to physical time.** More generally, if a positive solution has \(\dot x=-Kx^3+Ex^4+O(x^5)\) with \(K>0\), set \(y=1/x\). Then \(\dot y=K/y-E/y^2+O(y^{-3})\), so integration and inversion give
\[
 t=\frac{y^2}{2K}+\frac{E}{K^2}y+O(\log y),\qquad
 x(t)=(2Kt)^{-1/2}+\frac{E}{2K^2}t^{-1}+O(t^{-3/2}\log t).
\]
The initial condition affects only the integrable time-translation contribution, which enters at order \(t^{-3/2}\), not at either displayed coefficient. Inserting \(K,E\) gives the first formula in the finding.

**4. Quasi-static reduction and its different cubic jet.** The original paper's fast-equilibrium construction (Appendix 6.2.3, equation (83)) states that \(p_{\rm qs}\) solves
\[
 A(x)p^2+B(x)p+C(x)=0,
\]
where
\[
\begin{aligned}
A(x)&=(n\tau)^2\frac{1+x}{1-x},\\
B(x)&=\tau n[\gamma+w-\tau(n-1)+x(\tau-w)],\\
C(x)&=\gamma[w-\tau(n+1)+x(\tau-w)].
\end{aligned}
\]
At the critical parameters, the smooth positive branch through \(p=a\) has
\[
 p_{\rm qs}(x)=a-\frac{(n-1)^2}{2n^2}x^2
 +\frac{(n-3)(n-1)^2}{4n^3}x^3+O(x^4).
\]
It shares the full invariant graph's quadratic jet but not its cubic jet. Accordingly,
\[
\dot x_{\rm qs}=-Kx_{\rm qs}^3+E_{\rm qs}x_{\rm qs}^4+O(x_{\rm qs}^5),\quad
E_{\rm qs}=\frac{\gamma(n-1)(n-3)}{2n^2}.
\]
Applying Step 3 gives the quasi-static formula. Finally
\[
\frac{E-E_{\rm qs}}{2K^2}=\frac1{4\gamma}.
\]
The disagreement occurs because an actual invariant trajectory satisfies \(q'(x)\dot x=\dot q\), whereas quasi-static elimination sets \(\dot q=0\). Their discrepancy first propagates into the transmission-driving variable \(p\) at cubic order, making a nonzero observable \(t^{-1}\) error even though the leading exponent and amplitude agree.

## Verification

Run the included `verify.py` using Python 3 and SymPy; SciPy is optional for the clearly identified numerical diagnostic. It symbolically reconstructs the full fast Jacobian, all center-manifold jets, the full cubic and quartic terms, the separate quasi-static quadratic-root expansion, the rational sign-reversal witness and the exact identity \((E-E_{\rm qs})/(2K^2)=1/(4\gamma)\). It prints `SYMBOLIC_PASS` and `VERIFY_OK`. With SciPy installed, two independent long-time integrations at \(n=5/2\) and \(n=3\) corroborate the leading asymptotic. Finite integrations do **not** certify the asymptotic limits; the analytic center-manifold and scalar-ODE arguments above do.

## Relationship to prior work

Hébert-Dufresne, Simon and Kiss introduce the reduction and give the same original adaptive pair system, its fast-equilibrium quadratic, the known rewiring threshold, and a classification of forward/backward onset. They do **not** supply the full-flow, physical-time two-term critical asymptotic or compare its second-order coefficient against their quasi-static scalar dynamics. Gross, D'Lima and Blasius established the adaptive-network epidemic setting and the phenomena of rewiring-induced transitions and hysteresis; this work does not claim those bifurcations as new. Fang, Zhang and Wang study a nonlinear rewiring modification, including local center-manifold bifurcation calculations, but their different equations do not imply this explicit universal \(1/(4\gamma)\) discrepancy. Other published critical SIS results study different infection/link-response or synergy mechanisms and cannot be substituted for this pair-closure comparison. These are statement-level differences, not a proof against all unindexed earlier literature.

## Limitations

This is a **local deterministic pair-closure** finding for the precise mean-field equations above, not the exact finite stochastic adaptive-network SIS process. It does not assert global attraction, quantitative approximation for moderate prevalence, or a rigorously small fast/slow parameter; the quasi-static reduction is compared as a specified mathematical model, not assumed to be uniformly valid. The result concerns only the degenerate equality point, and the \(O(t^{-3/2}\log t)\) constants may depend on initial states and model parameters. Quasi-static fast equilibria at finite prevalence need not be dynamically invariant. Historical priority cannot be conclusively established without exhaustive access to all related literature.

## References

1. L. Hébert-Dufresne, P. L. Simon and I. Z. Kiss, *Fast-variable reduction to complex contagion unifies epidemic models*, arXiv:2610.05467v1, first public 2026-10-04, especially Appendix 6.2.3 and equations (73)–(91). https://arxiv.org/abs/2610.05467
2. T. Gross, C. J. D. D'Lima and B. Blasius, *Epidemic dynamics on an adaptive network*, arXiv:q-bio/0512037, first public 2005-12-20; Phys. Rev. Lett. 96, 208701 (2006). https://arxiv.org/abs/q-bio/0512037
3. H. Fang, M. Zhang and Z. Wang, *Complex Behaviors of Epidemic Model with Nonlinear Rewiring Rate*, Complexity (2020), article 7310347. https://doi.org/10.1155/2020/7310347
4. *Critical adaptive SIS clearance: exact two-term law and a curvature sign transition* (2026), published mathematical research record. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-critical-adaptive-sis-clearance-exact-two-term-law-and-a-curvatu--3dbf6638e1f1
5. *Exact assortativity threshold and cubic critical decay for a two-degree synergistic SIS system* (2026), published mathematical research record. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-assortativity-threshold-and-cubic-critical-decay-for-a-two--52efeed9346f
