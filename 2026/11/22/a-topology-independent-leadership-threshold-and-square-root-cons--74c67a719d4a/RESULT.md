# A topology-independent leadership threshold and square-root consensus relaxation in two-community opinion dynamics

## Finding

In the continuous-time opinion–leadership replicator model defined below, a population with two initially opposed opinion communities has a sharp **three-regime** phase law. If each individual assigns the same total peer weight \(p\in(0,1]\) to the opposite community, and all individuals share the same initial leadership \(\eta\in(0,1)\) and conviction parameter \(\rho>0\), the transition occurs at the exact value
\[
\rho_*=4p^2.
\]
For every finite number of individuals, any nonnegative row-stochastic influence matrix with this cross-community weight, and every initial opinion magnitude \(a\in(0,1]\), the opposed-community solution obeys:
\[
\begin{array}{ll}
0<\rho<\rho_*:& x_i(t)\to0,\quad y_i(t)\to0,\\
\rho=\rho_*:& y_i(t)\equiv\eta,\quad x_i(t)\to s_i\dfrac{a\eta}{2p+(1-2p)\eta},\\
\rho>\rho_*:& x_i(t)\to s_i a,\quad y_i(t)\to1.
\end{array}
\]
Here \(s_i\in\{-1,1\}\) records the community. In the subcritical case, convergence is *algebraic with exact amplitudes*:
\[
\lim_{t\to\infty}\sqrt{t}\,|x_i(t)|
 =\frac{1}{\sqrt{2(4p^2-\rho)}},\qquad
\lim_{t\to\infty}\sqrt{t}\,y_i(t)
 =\frac{2p}{a\sqrt{2(4p^2-\rho)}}.
\]
Thus the leading opinion-decay amplitude is independent of initial opinion magnitude, initial leadership, community sizes, and the detailed within- and across-community wiring. These conclusions hold **on the exact opposed-opinion/equal-leadership invariant family**; they are not assertions of attraction or stability under arbitrary nonsymmetric perturbations.

## Assumptions and scope

Fix any integer \(n\ge2\) and a nonempty partition \(V=V_+\sqcup V_-\). Let \(W=(W_{ij})\) be an arbitrary nonnegative row-stochastic \(n\times n\) matrix satisfying
\[
\sum_{j\in V_{-s_i}}W_{ij}=p\in(0,1]
\quad\text{for every }i,
\]
where \(s_i=1\) on \(V_+\) and \(s_i=-1\) on \(V_-\). The remaining total weight \(1-p\) can be distributed arbitrarily among agents in the same community, including self-weights. In particular, the matrix may be directed and the community sizes may differ. Equivalently, \(Ws=(1-2p)s\).

Let \(a\in(0,1]\), \(\eta\in(0,1)\), and \(\rho>0\). Prescribe fixed initial opinion anchors \(x_i(0)=a s_i\) and initial leadership \(y_i(0)=\eta\). The equations of the model are
\[
\begin{aligned}
\dot x_i&=-(1-y_i)\left(x_i-\sum_jW_{ij}x_j\right)-y_i(x_i-x_i(0)),\\
\dot y_i&=y_i(1-y_i)\left[\rho x_i^2-\left(x_i-\sum_jW_{ij}x_j\right)^2\right].
\end{aligned}\tag{1}
\]
The anchor \(x_i(0)\) is a fixed parameter of the differential equation after the initial time, not a changing initial-condition placeholder. All times are continuous and \(t\ge0\).

## Proof

**1. Exact invariant reduction.** Because \(Ws=(1-2p)s\), the ansatz \(x_i(t)=s_i u(t)\), \(y_i(t)=v(t)\) has \(x_i-\sum_jW_{ij}x_j=2p\,s_i u\) for every agent. Uniqueness of the polynomial initial-value problem makes this ansatz invariant. Put \(c=2p\in(0,2]\), \(\Delta=\rho-c^2\), and \(A(v)=c(1-v)+v\). Equation (1) reduces *exactly* to
\[
\dot u=-A(v)u+av,\qquad
\dot v=\Delta u^2v(1-v),\qquad (u(0),v(0))=(a,\eta).\tag{2}
\]
Here \(A(v)>0\) for \(0\le v\le1\). At \(u=0\), \(\dot u=av\ge0\); at \(u=a\), \(\dot u=-ac(1-v)\le0\). The horizontal edges \(v=0,1\) are invariant, and the vector field is smooth. Thus \([0,a]\times[0,1]\) is forward invariant, with \(0<u(t)\le a\) and \(0<v(t)<1\) at every finite time. The sign of \(\dot v\) is the sign of \(\Delta\) for every \(t\), establishing exact sharpness of the threshold.

**2. Supercritical leadership.** If \(\Delta>0\), \(v\) increases to a limit \(v_\infty\in[\eta,1]\). For an asymptotically constant positive coefficient \(A(v(t))\), the stable linear first equation of (2) gives \(u(t)\to av_\infty/A(v_\infty)>0\). If \(v_\infty<1\), the second derivative approaches a strictly positive constant, a contradiction. Therefore \(v_\infty=1\) and \(u(t)\to a\). Indeed, after sufficiently large time, \(u\ge a/2\) and \(v\ge\eta\), so \((1-v)'=-\Delta u^2v(1-v)\) yields exponential decay of \(1-v\). The equation \((u-a)'=-A(v)(u-a)-ac(1-v)\) then yields exponential convergence \(u\to a\).

**3. Critical partial leadership.** If \(\Delta=0\), the second equation makes \(v(t)=\eta\) exactly. With \(A_\eta=c(1-\eta)+\eta>0\), the first equation has the exact solution
\[
u(t)=\frac{a\eta}{A_\eta}
+\left(a-\frac{a\eta}{A_\eta}\right)e^{-A_\eta t}.
\]
This proves the middle line of the trichotomy and the continuum of distinct limits indexed by \(\eta\).

**4. Subcritical complete followership.** Suppose \(\Delta<0\) and write \(\gamma=c^2-\rho>0\). Then \(v\) decreases to some \(v_\infty\in[0,\eta]\). As in Step 2, \(u(t)\to av_\infty/A(v_\infty)\). If \(v_\infty>0\), the second derivative would converge to a strictly negative number because \(v_\infty\le\eta<1\), impossible. Hence \(v_\infty=0\) and \(u(t)\to0\).

To identify the *exact* algebraic rate, set \(z(t)=u(t)/v(t)\), which is well defined for every finite time. Differentiating (2) gives the scalar linear equation
\[
\dot z=a-\bigl[A(v)-\gamma u^2(1-v)\bigr]z.
\]
The coefficient in brackets tends to \(c>0\). Variation of constants (or comparison with constant-coefficient linear equations) gives \(z(t)\to a/c\). Therefore
\[
\frac{d}{dt}\left(v^{-2}\right)=2\gamma z^2(1-v)
\longrightarrow \frac{2\gamma a^2}{c^2}.
\]
The fundamental theorem of calculus and Cesàro averaging imply
\[
\frac{v(t)^{-2}}t\longrightarrow\frac{2\gamma a^2}{c^2}.
\]
Consequently \(\sqrt t\,v(t)\to c/[a\sqrt{2\gamma}]\), and multiplication by \(z(t)\to a/c\) yields \(\sqrt t\,u(t)\to1/\sqrt{2\gamma}\). These are genuine infinite-time limits, not numerical extrapolations. Substituting \(c=2p\) completes the proof.

## Verification

The self-contained `verify.py` checks the signed-eigenvector reduction with exact rational arithmetic for a directed four-agent, two-community matrix having nonuniform cross-community contacts. It compares full-system and reduced-system numerical solutions for different network sizes, cross-community exposure probabilities and all three phases, and checks the subcritical scaling at a large finite time. Run `python verify.py` with Python, NumPy, and SciPy. Exact arithmetic verifies identities in sampled instances; numerical tests are supplementary, not a proof of the quantified theorem. The preceding analytic argument establishes the full stated result.

## Relationship to prior work

Alutto, Zino, Johansson and Fontan (arXiv:2606.05825, June 4, 2026) introduced the replicator opinion–leadership system (1), established invariance and general equilibrium conditions, and gave sufficient conditions for emergence of individual leaders and followers. The present result is a necessary-and-sufficient three-phase classification **within a particular, naturally motivated two-community invariant family**, with a topology-independent transition and exact algebraic decay. It does not claim an all-state stability theorem or reproduce their sufficient conditions.

An earlier paper by the same authors (arXiv:2603.24381, March 25, 2026) uses the *different* leadership equation \(\dot y_i=\alpha(1-y_i)x_i^2-\beta y_i(x_i-(Wx)_i)^2\). Its signed-mode equilibria and transverse-stability results, including a published exact finding based on that equation, do not imply the replicator trichotomy above. Classical fixed-leader and inter-issue social-power models also have different leadership update laws. These distinctions were checked on the actual equations rather than by title matching.

## Limitations

The result concerns deterministic dynamics and exactly common leadership initialized at \(\eta\), with opposite, equal-magnitude initial community opinions, identical \(\rho\), and a common cross-community row-weight \(p\). It is an invariant-family classification; the limiting complete-follower equilibrium may have different stability under symmetry-breaking disturbances. No assertion is made about arbitrary opinion anchors, unequal leadership parameters, stochastic environments, empirical populations, or critical finite-size fluctuations. Historical originality is limited by the inspectable literature; unindexed or inaccessible mathematical treatments might overlap.

## References

- M. Alutto, L. Zino, K. H. Johansson, A. Fontan, *On Leadership Emergence in Opinion Dynamics on Social Networks*, arXiv:2606.05825v1 (first public June 4, 2026), https://arxiv.org/abs/2606.05825. Model and general equilibrium theory; public full text at https://www.researchgate.net/publication/406039711_On_Leadership_Emergence_in_Opinion_Dynamics_on_Social_Networks.
- M. Alutto, L. Zino, K. H. Johansson, A. Fontan, *On a Co-evolving Opinion-Leadership Model in Social Networks*, arXiv:2603.24381v1 (March 25, 2026), https://arxiv.org/abs/2603.24381. Different, linear-in-leadership feedback law.
- *A sharp transverse stability boundary for polarized co-evolving opinion leadership*, published mathematical finding (November 8, 2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-sharp-transverse-stability-boundary-for-polarized-co-evolving--0a05cce9c49b. Relates to the March 2026 model, not the June replicator equation.
- P. Jia, A. Mirtabatabaei, N. E. Friedkin, F. Bullo, *Opinion Dynamics and the Evolution of Social Power in Influence Networks*, SIAM Review 57 (2015), 367–397, https://doi.org/10.1137/130913250. Distinct inter-issue model.
