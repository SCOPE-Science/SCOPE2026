# Global Hopf-slope calibration in the FitzHugh–Nagumo oscillator
## Finding
Consider the canonical planar FitzHugh–Nagumo oscillator
\[
\dot v=v-\frac{v^3}{3}-w+I,
\qquad
\dot w=\varepsilon(v+a-bw),
\]
with
\[
\varepsilon>0,
\qquad
b>0.
\]

Every compactly supported invariant Borel probability measure \(\mu\) satisfies the exact global Hopf-slope balance
\[
\boxed{
\mathbb E_\mu\!\left[
(1-\varepsilon b-v^2)\dot v^2
\right]
=0
}.
\]

If \(\mu\) is not supported on equilibria, then
\[
\mathbb E_\mu[\dot v^2]>0.
\]
Therefore, defining the speed-weighted probability measure
\[
d\nu
=
\frac{\dot v^2}{\mathbb E_\mu[\dot v^2]}
\,d\mu,
\]
one obtains
\[
\boxed{
\mathbb E_\nu[v^2]
=
1-\varepsilon b
}.
\]
In particular, every non-equilibrium compact stationary state requires
\[
\boxed{
\varepsilon b<1
}.
\]

The same quantity governs the local Hopf trace. At an equilibrium \((v_*,w_*)\), the Jacobian trace is
\[
\operatorname{tr}J
=
1-v_*^2-\varepsilon b.
\]
Thus the global stationary identity says that the \(\dot v^2\)-weighted average of the local trace coefficient along any compact recurrent state is exactly zero.

Every nonconstant periodic orbit consequently visits both regions
\[
|v|<\sqrt{1-\varepsilon b}
\]
and
\[
|v|>\sqrt{1-\varepsilon b}.
\]
So finite-amplitude recurrence cannot remain entirely on one side of the same voltage threshold that marks trace zero in the linearized equilibrium problem.

There are also two exact stationary nullcline calibrations:
\[
\boxed{
\mathbb E_\mu[w\mid v]
=
v-\frac{v^3}{3}+I
}
\]
and
\[
\boxed{
\mathbb E_\mu[v\mid w]
=
bw-a
}.
\]
Their residuals are exactly the coordinate speeds, hence
\[
\boxed{
\operatorname{Var}_\mu(w)
-
\operatorname{Var}_\mu\!\left(v-\frac{v^3}{3}\right)
=
\mathbb E_\mu[\dot v^2]
}
\]
and
\[
\boxed{
\operatorname{Var}_\mu(v)
-
b^2\operatorname{Var}_\mu(w)
=
\frac{1}{\varepsilon^2}\mathbb E_\mu[\dot w^2]
}.
\]

For the standard Scholarpedia parameters
\[
\varepsilon=0.08,
\qquad
b=0.8,
\]
the speed-weighted voltage law becomes
\[
\mathbb E_\nu[v^2]=0.936,
\]
so the corresponding trace-zero voltage magnitude is
\[
\sqrt{0.936}\approx0.967471.
\]

## Assumptions and scope
The theorem concerns the autonomous two-dimensional FitzHugh–Nagumo model
\[
\dot v=v-v^3/3-w+I,
\qquad
\dot w=\varepsilon(v+a-bw).
\]
The invariant measure \(\mu\) is assumed to have compact support in \(\mathbb R^2\). This guarantees integrability of all polynomial observables and their derivatives.

The parameters \(a\) and \(I\) are unrestricted real numbers. The conditions
\[
\varepsilon>0,
\qquad
b>0
\]
are the standard recovery-rate assumptions and ensure coercivity of the quartic potential used in the proof.

The original FitzHugh article appeared in the July 1961 issue of Biophysical Journal. A public bibliographic record used for the date anchor reports 1 July 1961. A peer-reviewed model account gives the canonical normalization above and the standard numerical values
\[
a=0.7,
\qquad
b=0.8,
\qquad
\varepsilon=0.08.
\]
Same-family mathematical work on FitzHugh–Nagumo oscillations uses primary MSC \(34C15\).

## Proof
Set
\[
f(v)=v-\frac{v^3}{3}.
\]
The equations are
\[
\dot v=f(v)-w+I,
\qquad
\dot w=\varepsilon(v+a-bw).
\]

First derive the two conditional laws.
For any continuous function \(\phi\) on the compact stationary \(v\)-range, choose an antiderivative \(H\) with
\[
H'(v)=\phi(v).
\]
Then
\[
LH
=
\phi(v)(f(v)-w+I).
\]
Invariance gives
\[
\mathbb E_\mu[\phi(v)(f(v)-w+I)]=0
\]
for every such \(\phi\). Therefore
\[
\mathbb E_\mu[w\mid v]=f(v)+I.
\]
Because
\[
w-(f(v)+I)=-\dot v,
\]
conditional orthogonality gives
\[
\operatorname{Var}(w)-\operatorname{Var}(f(v))
=
\mathbb E[\dot v^2].
\]

Similarly, testing antiderivatives of \(w\) gives
\[
\mathbb E_\mu[v\mid w]=bw-a.
\]
Since
\[
v-(bw-a)=\frac{\dot w}{\varepsilon},
\]
one obtains
\[
\operatorname{Var}(v)-b^2\operatorname{Var}(w)
=
\frac1{\varepsilon^2}\mathbb E[\dot w^2].
\]

Now eliminate \(w\). From
\[
w=f(v)+I-\dot v
\]
and
\[
\dot w=f'(v)\dot v-\ddot v,
\]
the recovery equation becomes
\[
\ddot v
+
(\varepsilon b-f'(v))\dot v
+
\varepsilon\left[v+a-bf(v)-bI\right]
=0.
\]
Define
\[
U'(v)=v+a-bf(v)-bI.
\]
An explicit primitive is
\[
U(v)
=
\frac{1-b}{2}v^2
+
\frac{b}{12}v^4
+
(a-bI)v.
\]
Introduce the state function
\[
\mathcal E(v,w)
=
\frac12\dot v^2
+
\varepsilon U(v),
\]
where
\[
\dot v=f(v)-w+I
\]
is understood as the vector-field component. Along trajectories,
\[
\frac{d\mathcal E}{dt}
=
-\left(\varepsilon b-f'(v)\right)\dot v^2.
\]
Since
\[
f'(v)=1-v^2,
\]
this is
\[
\frac{d\mathcal E}{dt}
=
(1-\varepsilon b-v^2)\dot v^2.
\]
Stationarity of \(\mu\) gives
\[
\mathbb E_\mu\left[\frac{d\mathcal E}{dt}\right]=0,
\]
which proves
\[
\mathbb E_\mu[(1-\varepsilon b-v^2)\dot v^2]=0.
\]

If
\[
\mathbb E_\mu[\dot v^2]=0,
\]
then \(\dot v=0\) on every support trajectory, so \(v\) is constant. The fast equation then makes \(w=f(v)+I\) constant, and the recovery equation forces an equilibrium. Thus every non-equilibrium compact stationary state has positive \(\dot v^2\)-energy.

For such a state, division by
\[
\mathbb E_\mu[\dot v^2]
\]
gives
\[
\mathbb E_\nu[v^2]
=
1-\varepsilon b.
\]
The left side is nonnegative. If \(\varepsilon b>1\), this is impossible. At \(\varepsilon b=1\), the stationary identity is
\[
\mathbb E[v^2\dot v^2]=0.
\]
Thus \(v\dot v=0\) on support trajectories, so
\[
\frac{d}{dt}v^2=0.
\]
Hence \(|v|\) is constant; continuity makes \(v\) itself constant, and the trajectory is again an equilibrium. Therefore non-equilibrium compact recurrence requires
\[
\varepsilon b<1.
\]

For a nonconstant periodic orbit, integrate
\[
(1-\varepsilon b-v^2)\dot v^2
\]
over one period. If the orbit stayed entirely in
\[
|v|\le\sqrt{1-\varepsilon b},
\]
the integrand would be nonnegative. Vanishing of its integral would force it to vanish identically; on every open interval where \(\dot v\ne0\), that would force \(|v|\) to remain equal to the boundary value, which is impossible. Thus the orbit enters the outer region. The same argument with the sign reversed shows that it also enters the inner region.

## Verification
The accompanying checker verifies the Lyapunov identity directly from the two-dimensional vector field using exact sparse-polynomial arithmetic.

With
\[
\mathcal E
=
\frac12\dot v^2
+
\varepsilon
\left[
\frac{1-b}{2}v^2
+
\frac{b}{12}v^4
+
(a-bI)v
\right],
\]
it checks
\[
L\mathcal E
=
(1-\varepsilon b-v^2)\dot v^2.
\]

It separately verifies the two residual identities
\[
w-\left(v-\frac{v^3}{3}+I\right)=-\dot v
\]
and
\[
v-(bw-a)=\frac{\dot w}{\varepsilon}.
\]

For
\[
\varepsilon=\frac{2}{25},
\qquad
b=\frac45,
\]
it confirms
\[
1-\varepsilon b
=
\frac{117}{125}
=
0.936.
\]

The stored checker output is `VERIFY_OK`.

The invariant-measure disintegrations and equality-rigidity argument are analytic and are not inferred from finite trajectory simulation.

## Relationship to prior work
FitzHugh introduced the excitable-oscillatory two-state nerve model in 1961 as a reduction of Hodgkin–Huxley dynamics. A modern peer-reviewed model account writes the now-standard normalization used here.

Classical and modern FitzHugh–Nagumo literature extensively analyzes nullclines, excitability, Hopf bifurcation, canard explosion, limit-cycle multiplicity, homoclinic structure, and global stability. In particular, a 2004 paper develops Lyapunov-functional stability regions, and a 2009 paper analyzes the planar model's limit-cycle bifurcations and supplies sufficient conditions for a unique stable cycle. Those sources are the strongest plausible prior coverage of the energy reduction used here.

A six-decade review surveys the large FitzHugh–Nagumo literature and emphasizes the same cubic-nullcline and Hopf geometry. A 1992 singular-Hopf analysis studies the local and perturbative periodic-orbit structure near the Hopf regime.

Published semantic searches were run for invariant measures, exact moments, speed-weighted Hopf balance, the expression
\[
\mathbb E[v^2\dot v^2],
\]
and the threshold
\[
\varepsilon b=1.
\]
No same-object indexed result was found that states the all-invariant-measures identity
\[
\mathbb E[(1-\varepsilon b-v^2)\dot v^2]=0
\]
or the equivalent speed-weighted calibration
\[
\mathbb E_\nu[v^2]=1-\varepsilon b.
\]

The closest indexed structural analogue is a global Hopf-slope balance for the distinct third-order Goodwin feedback oscillator. That theorem does not imply the planar FitzHugh–Nagumo identity because the order, feedback architecture, and energy reduction are different.

## Limitations
The theorem concerns compactly supported invariant probability measures of the autonomous planar model. It does not classify all equilibria or determine which parameter values actually produce a stable limit cycle.

The condition
\[
\varepsilon b<1
\]
is necessary for non-equilibrium compact recurrence, not sufficient.

The 2004 Lyapunov-stability paper and the 2009 dynamical-behavior paper were available in the inspected route only through abstract-level or partial material, so they remain the principal originality risk. The accepted originality claim is therefore restricted to the exact invariant-measure Hopf-slope calibration and its speed-weighted consequence, not to the existence of Lyapunov functions or classical stability regions.

No novelty is claimed for the FitzHugh–Nagumo equations, cubic and linear nullclines, local Hopf trace calculation, canard explosion, or standard limit-cycle regimes.

## References
1. R. FitzHugh, “Impulses and Physiological States in Theoretical Models of Nerve Membrane,” Biophysical Journal 1, 445–466 (1961), DOI 10.1016/S0006-3495(61)86902-6.
2. E. M. Izhikevich and R. FitzHugh, “FitzHugh–Nagumo Model,” Scholarpedia 1, 1349 (2006), DOI 10.4249/scholarpedia.1349.
3. T. Kostova, R. Ravindran, and M. E. Schonbek, “FitzHugh–Nagumo Revisited: Types of Bifurcations, Periodical Forcing and Stability Regions by a Lyapunov Functional,” International Journal of Bifurcation and Chaos 14, 913–925 (2004), DOI 10.1142/S0218127404009685.
4. M. Ringkvist and Y. Zhou, “On the dynamical behaviour of FitzHugh–Nagumo systems: Revisited,” Nonlinear Analysis 71, 2667–2687 (2009), DOI 10.1016/j.na.2009.01.149.
5. S. M. Baer and T. Erneux, “Singular Hopf Bifurcation to Relaxation Oscillations. II,” SIAM Journal on Applied Mathematics 52, 1651–1664 (1992), DOI 10.1137/0152095.
6. D. Cebrián-Lacasa, P. Parra-Rivas, D. Ruiz-Reynés, and L. Gelens, “Six decades of the FitzHugh–Nagumo model: A guide through its spatio-temporal dynamics and influence across disciplines,” Physics Reports 1096, 1–39 (2024), arXiv:2404.11403.
