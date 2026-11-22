# A sharp nonzero-seed tipping point and cubic cusp in cumulative-feedback social contagion

## Finding

For a continuous-time, homogeneous-mixing susceptible–active–recovered adoption process with feedback proportional to *cumulative retired adopters*, the dependence of eventual adoption on the initial active seed has a complete sharp classification. Write \(B=\beta/\mu\in(0,1)\), \(A=\alpha/\mu\geq0\), and \(\varepsilon\in(0,1)\) for the initial active fraction. Define
\[
H(z)=(1-z)\exp\left(Bz+\frac A2z^2\right),\qquad 0\leq z\leq1.
\]
The eventual retired-adopter fraction \(Z(\varepsilon)\) is the **smallest positive root** of \(H(z)=1-\varepsilon\).

Set \(A_*(B)=(1+\sqrt{1-B})^2\). For \(A<A_*\), \(Z\) is continuous and smooth for all positive seeds. At \(A=A_*\), it is continuous but develops a cubic-root singularity at a strictly positive seed. With \(s=\sqrt{1-B}\), the point and coefficient are
\[
z_* =\frac{s}{1+s},\qquad
\varepsilon_* =1-\frac{\exp(s-s^2/2)}{1+s},\qquad
C_* =\left[\frac{3}{(1+s)^2\exp(s-s^2/2)}\right]^{1/3},
\]
\[
Z(\varepsilon)-z_* = C_*\operatorname{cbrt}(\varepsilon-\varepsilon_*)
+o\left(|\varepsilon-\varepsilon_*|^{1/3}\right).
\]
Here \(\operatorname{cbrt}\) denotes the real signed cube root.

For \(A>A_*\), let
\[
u=\frac{A-B-\sqrt{(A+B)^2-4A}}{2A},\qquad
v=\frac{A-B+\sqrt{(A+B)^2-4A}}{2A},
\]
so that \(0<u<v<1\). There is **exactly one discontinuity**, at the positive seed
\[
\varepsilon_c=1-(1-u)\exp\left(Bu+\frac A2u^2\right).
\]
At the threshold \(Z(\varepsilon_c)=u\). The left limit is \(u\), while the right limit is the unique \(w\in(v,1)\) with \(H(w)=H(u)\). Thus the jump \(w-u\) is strictly positive. There is no such jump when \(A\leq A_*\).

At the two critical seeds the approach in physical time is algebraically slow. At \(A=A_*\), \(\varepsilon=\varepsilon_*\),
\[
z_*-R(t)\sim\sqrt{\frac{3}{2\mu A\,t}},
\]
and for \(A>A_*\), \(\varepsilon=\varepsilon_c\),
\[
u-R(t)\sim\frac{2}{\mu A(v-u)t}.
\]
The boundary case \(A=0\) is included in the smooth regime. All claims assume \(0<B<1\) and an exactly specified positive initial seed; they concern the continuous-time homogeneous-mixing model **defined below**, not a discrete network contagion theorem.

## Assumptions and scope

Let \(S(t),I(t),R(t)\) denote susceptible, active and retired fractions, with \(S+I+R=1\). Consider the autonomous system
\[
\dot S=-(\beta+\alpha R)SI,\qquad
\dot I=(\beta+\alpha R)SI-\mu I,\qquad
\dot R=\mu I,
\]
where \(0<\beta<\mu\), \(\alpha\geq0\), \(\mu>0\), and
\[
S(0)=1-\varepsilon,\quad I(0)=\varepsilon,\quad R(0)=0,
\qquad 0<\varepsilon<1.
\]
The incidence coefficient is a **continuous-time hazard**, not a discrete per-edge probability; no artificial probability cap is applied. The parameter domain is an ideal homogeneous-mixing setting, with permanent retirement of adopters, no new entrants and no stochastic finite-size extinction. A seed-fraction threshold is not the same observable as a transition in intrinsic transmissibility.

## Proof

**Invariant and selection of root.** The unit simplex is forward invariant. Since \(I(t)>0\) at every finite time, \(R\) strictly increases. Dividing the susceptible equation by \(\dot R=\mu I\), then integrating, gives
\[
\frac{d\log S}{dR}=-(B+AR),\qquad
S(z)=(1-\varepsilon)e^{-Bz-Az^2/2}.
\]
Consequently \(I(z)=1-z-(1-\varepsilon)e^{-Bz-Az^2/2}\). Since \(R\) is bounded and increasing, its limit \(Z\) exists, and \(I(t)\to0\): if its limiting value were positive, \(\dot R=\mu I\) would contradict boundedness. Along the orbit, \(I(z)>0\) precisely while \(H(z)>1-\varepsilon\). As \(H(0)=1>1-\varepsilon\) and \(H(1)=0\), the orbit stops at the **first** positive intersection with the level \(1-\varepsilon\). The approach may take infinite time when that intersection is multiple, but it cannot pass a zero of \(I\) by uniqueness of the ODE.

**Complete turning-point classification.** Direct differentiation yields
\[
H'(z)=\frac{H(z)}{1-z}q(z),\qquad
q(z)=B-1+(A-B)z-Az^2.
\]
Here \(q(0)=B-1<0\) and \(q(1)=-1\). For \(0\leq A\leq B\) the derivative \(q'\) is nonpositive for nonnegative \(z\), so \(q<0\). For \(A>B\), its vertex is positive, and the vertex exceeds zero precisely when \((A+B)^2>4A\). The two solutions of equality are \((1\pm\sqrt{1-B})^2\). The smaller lies below \(B\), so in the applicable region \(A>B\) the positive-vertex condition is equivalent to \(A>A_*\). At equality \(q(z)=-A(z-z_*)^2\), whereas above threshold it has two simple roots \(u,v\) in \((0,1)\). Thus \(H\) is strictly decreasing for \(A\leq A_*\), and for \(A>A_*\) its three successive intervals are decreasing, increasing, decreasing, with local minimum at \(u\) and local maximum at \(v\). These are its only turning points.

**Seed jump.** For \(A>A_*\), \(H(u)<H(0)=1\), so \(\varepsilon_c=1-H(u)\in(0,1)\). Also \(H(v)>H(u)>0=H(1)\); hence a unique \(w\in(v,1)\) satisfies \(H(w)=H(u)\). For \(\varepsilon<\varepsilon_c\) sufficiently close to the threshold, the smallest crossing lies in \((0,u)\) and approaches \(u\) from below. At equality the first crossing is the double root \(u\). For \(\varepsilon>\varepsilon_c\), \(H(z)>1-\varepsilon\) all the way through \([0,v]\); the first crossing occurs to the right of \(v\), and approaches \(w\) as the seed decreases to the threshold. Away from this minimum level, first crossings vary continuously and smoothly. The local maximum cannot cause a further jump in the *first* crossing since it is preceded by the earlier branch wherever that branch exists. This proves both the jump size and its uniqueness.

**Cubic cusp.** Put \(s=\sqrt{1-B}\) and \(A=A_*=(1+s)^2\). Then \(z_*=s/(1+s)\), \(q(z)=-A(z-z_*)^2\), and direct substitution shows
\[
H(z_*)=\frac{e^{s-s^2/2}}{1+s}.
\]
This number lies strictly between zero and one: the function \(\log(1+s)-s+s^2/2\) is zero at zero and has positive derivative \(s^2/(1+s)\). By the derivative formula,
\[
H(z)=H(z_*)-\frac{H(z_*)A}{3(1-z_*)}(z-z_*)^3
+o(|z-z_*|^3).
\]
Since \(Z\) is the inverse of the strictly decreasing \(H\), this yields the stated signed cubic-root expansion with coefficient \(C_*\), proving that it is neither smooth nor a finite jump.

**Critical time tails.** Use \(\dot R=\mu I(R)\) and the identity
\[
I(z)=e^{-Bz-Az^2/2}\bigl(H(z)-(1-\varepsilon)\bigr).
\]
At the fold seed \(\varepsilon_c\), the Taylor expansion at \(u\) and \(H''(u)=H(u)A(v-u)/(1-u)\) give
\[
\dot R=\frac{\mu A(v-u)}2(u-R)^2+O((u-R)^3).
\]
At the cusp seed \(\varepsilon_*\), the corresponding cubic expansion gives
\[
\dot R=\frac{\mu A}{3}(z_*-R)^3+O((z_*-R)^4).
\]
Separating either scalar asymptotic equation proves the claimed \(t^{-1}\) and \(t^{-1/2}\) laws respectively.

## Verification

The accompanying standalone `verify.py` checks rational discriminants, the precise two-turning-point example, both sides of the discontinuity, the cusp coefficient by numerical inversion, and an independent integration of the original three-compartment ODE against the implicit final-size root. Execute `python verify.py` in an environment with Python 3 and SciPy. The algebraic proof, not the finite numerical checks, establishes the universal quantifiers.

A rational benchmark is \(B=1/2\), \(A=3\), giving \(u=1/3\), \(v=1/2\),
\[
\varepsilon_c=1-\frac23e^{1/3}\approx0.0695917166093,
\quad w\approx0.5742373767357,
\quad w-u\approx0.2409040434024.
\]
A cusp benchmark is \(B=3/4\), \(A=9/4\), with \(z_*=1/3\), \(\varepsilon_*\approx0.0300057235879\) and \(C_*\approx0.9713135232364\). All figures are computational illustrations, not substitutes for proof.

## Relationship to prior work

Xue, Yang, Cui and Di (2025 preprint; 2026 journal article) study a **discrete-time finite-network** adoption process in which per-edge transmission probabilities grow with the recovered-adopter fraction (and are capped at one). They demonstrate localization-dependent reinforcement thresholds and mixed-order transitions when varying intrinsic transmissibility. This source motivates the feedback mechanism but neither its mathematical process nor its transition observable is the homogeneous continuous-time positive-seed final-size problem solved here. The precise analytic seed boundary, jump branch and cubic cusp are therefore **not presented as consequences of** their existing network threshold.

St-Onge and coauthors (2021 preprint; 2022 journal article) analyze nonlinear group contagion on heterogeneous hypergraphs, including tricritical points, bistable endemic states and optimal seeds. Their reinforcement depends on group infection states, and the studied phase diagram concerns persistent endemic states rather than the final size of an irreversible cumulative-retirement process. Such general cusp and bistability phenomena predate this calculation; novelty is claimed **only** for the exact model-specific seed threshold and critical laws here. Earlier critical-mass and catastrophe-theory analyses may give equivalent formulations, and priority should not be assumed from a negative search alone.

## Limitations

The network result in the initiating article is not established by this homogeneous ODE, and quantitative thresholds should not be transferred to it. The event is an infinite-time deterministic final-size discontinuity under variation of a positive initial fraction; at finite time all ODE trajectories depend continuously on initial conditions. Real networks, discrete probabilities, time-varying behavior, imperfect mixing, and stochastic extinction may eliminate or shift this mathematical tipping point. The model's positive cumulative reinforcement is idealized and unbounded as a rate, though bounded on the unit simplex. The result gives no finite-population statistical confidence intervals. Independent mathematical review has not been performed.

## References

1. L. Xue, K.-C. Yang, P.-B. Cui, and Z. Di, *Network localization governs social contagion dynamics with macro-level reinforcement*, arXiv:2512.15371v1, first publicly released 2025-12-17. https://arxiv.org/html/2512.15371v1 ; *Physical Review Research* 8, 013062 (2026), https://doi.org/10.1103/tdz7-r22b.
2. G. St-Onge, I. Iacopini, V. Latora, A. Barrat, G. Petri, A. Allard, and L. Hébert-Dufresne, *Influential groups for seeding and sustaining nonlinear contagion in heterogeneous hypergraphs*, arXiv:2105.07092 (2021), *Communications Physics* 5, 25 (2022). https://arxiv.org/abs/2105.07092 ; https://doi.org/10.1038/s42005-021-00788-w.
