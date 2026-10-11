# Exact delayed-feedback regression and variance defect in the Mackey–Glass equation
## Finding
Consider the deterministic Mackey–Glass delay equation
\[
\dot x(t)
=
-\gamma x(t)
+
\beta f(x(t-\tau)),
\]
with
\[
f(u)
=
\frac{\theta^n u}{\theta^n+u^n},
\qquad
\beta,\gamma,\theta,\tau>0,
\qquad
n>1.
\]

Let
\[
\mathcal C_+
=
C([-\tau,0],(0,\infty))
\]
be the positive history space and let \(\mu\) be a compactly supported invariant Borel probability measure for the solution semiflow.

For a history \(\varphi\), write
\[
X_0(\varphi)=\varphi(0),
\qquad
X_{-\tau}(\varphi)=\varphi(-\tau).
\]
Then the delayed production term has the exact stationary regression
\[
\boxed{
\mathbb E_\mu[
\beta f(X_{-\tau})
\mid
X_0
]
=
\gamma X_0
}.
\]

Invariance also gives equality of the one-time marginals
\[
(X_{-\tau})_\#\mu=(X_0)_\#\mu.
\]
Therefore
\[
\boxed{
\beta^2
\operatorname{Var}_\mu(f(X_0))
-
\gamma^2
\operatorname{Var}_\mu(X_0)
=
\mathbb E_\mu[\dot x(0)^2]
}.
\]

The right-hand side vanishes exactly for probability measures supported on constant equilibrium histories. Every genuinely time-dependent compact stationary state therefore satisfies the strict variance inequality
\[
\beta^2
\operatorname{Var}_\mu(f(X_0))
>
\gamma^2
\operatorname{Var}_\mu(X_0).
\]

Let the one-time support of \(\mu\) be contained in
\[
[m,M]\subset(0,\infty)
\]
and set
\[
L_{m,M}
=
\sup_{u\in[m,M]}|f'(u)|.
\]
Every non-equilibrium compact stationary state obeys the necessary slope condition
\[
\boxed{
\beta L_{m,M}>\gamma
}.
\]
Equivalently, the convex hull of its one-time amplitude range must meet
\[
\left\{
u>0:
|f'(u)|>\frac{\gamma}{\beta}
\right\}.
\]

For the classical normalized parameters
\[
\beta=2,
\qquad
\gamma=1,
\qquad
\theta=1,
\qquad
n=9.65,
\]
the equation
\[
|f'(u)|=\frac12
\]
has three positive roots
\[
u_1\approx0.735633145,
\qquad
u_2\approx0.845794468,
\qquad
u_3\approx1.324883761.
\]
Hence no non-equilibrium compact stationary state can have its entire one-time amplitude interval contained in either
\[
[u_1,u_2]
\]
or
\[
[u_3,\infty).
\]

## Assumptions and scope
The result concerns the deterministic positive Mackey–Glass semiflow on the continuous-history space. Compact support is assumed for the invariant measure so that all displayed observables and generator tests are integrable.

The theorem is a statement about invariant measures on history space, not merely about a single periodic orbit. It applies to periodic-orbit measures, invariant measures on chaotic compact sets, equilibrium atoms, and convex mixtures of such invariant measures whenever they are supported in the positive history space.

The one-time support interval
\[
[m,M]
\]
means the convex hull of the support of the evaluation observable
\[
X_0.
\]
The local slope obstruction is support-dependent and therefore can be sharper than a global Lipschitz estimate.

The original Mackey–Glass paper was published on 15 July 1977. Modern rigorous work treats the same equation as a scalar delay-differential equation on a continuous history-space semiflow and classifies it under delay-equation MSC codes including \(34K18\) and \(34K13\).

## Proof
Let \(S_t\) denote the solution semiflow on \(\mathcal C_+\).

Take a continuously differentiable scalar function \(H\) on the compact one-time range and define the cylinder observable
\[
\Phi(\varphi)=H(\varphi(0)).
\]
Its generator along solutions is
\[
L\Phi(\varphi)
=
H'(X_0)
\left[
-\gamma X_0
+
\beta f(X_{-\tau})
\right].
\]

For every continuous test function \(h\) on the one-time range, choose \(H\) with
\[
H'=h.
\]
Invariance gives
\[
0
=
\int L\Phi\,d\mu
=
\mathbb E_\mu
\left[
h(X_0)
\left(
-\gamma X_0+\beta f(X_{-\tau})
\right)
\right].
\]
Because this holds for every continuous \(h\),
\[
\mathbb E_\mu[
\beta f(X_{-\tau})
\mid
X_0
]
=
\gamma X_0.
\]

We next prove the equality of the delayed and current marginals. Advancing a history by one full delay gives
\[
X_{-\tau}(S_\tau\varphi)
=
X_0(\varphi).
\]
Since
\[
(S_\tau)_\#\mu=\mu,
\]
the laws of
\[
X_{-\tau}
\quad\text{and}\quad
X_0
\]
under \(\mu\) coincide.

Set
\[
A=\beta f(X_{-\tau}),
\qquad
B=\gamma X_0.
\]
The conditional regression says
\[
\mathbb E[A\mid X_0]=B.
\]
Hence
\[
\mathbb E[A]=\mathbb E[B]
\]
and
\[
\mathbb E[AB]=\mathbb E[B^2].
\]
Since
\[
A-B=\dot x(0),
\]
expansion yields
\[
\mathbb E[\dot x(0)^2]
=
\operatorname{Var}(A)
-
\operatorname{Var}(B).
\]
Using the equality of one-time marginals gives
\[
\operatorname{Var}(A)
=
\beta^2\operatorname{Var}(f(X_0)),
\]
so
\[
\beta^2
\operatorname{Var}(f(X_0))
-
\gamma^2
\operatorname{Var}(X_0)
=
\mathbb E[\dot x(0)^2].
\]

Suppose equality holds. Then
\[
\dot x(0)=0
\]
for \(\mu\)-almost every history. Invariance implies the same for
\[
\dot x(t)
\]
at every nonnegative rational time along \(\mu\)-almost every trajectory. Continuity of the derivative then gives
\[
\dot x(t)=0
\]
for every
\[
t\ge0.
\]
Thus the future trajectory is constant. After time \(\tau\), its entire history segment is constant. Because \(\mu\) is invariant under \(S_\tau\), \(\mu\) itself is supported on constant histories. Such histories are exactly the equilibria satisfying
\[
\gamma r=\beta f(r).
\]
The converse is immediate.

For the slope obstruction, assume \(\mu\) is not equilibrium-supported. Then
\[
\mathbb E[\dot x(0)^2]>0
\]
and
\[
\operatorname{Var}(X_0)>0.
\]
Therefore
\[
\beta^2
\operatorname{Var}(f(X_0))
>
\gamma^2
\operatorname{Var}(X_0).
\]
If
\[
f
\]
is \(L_{m,M}\)-Lipschitz on \([m,M]\), an independent-copy argument gives
\[
\operatorname{Var}(f(X_0))
\le
L_{m,M}^2
\operatorname{Var}(X_0).
\]
Consequently
\[
\beta^2L_{m,M}^2>\gamma^2,
\]
which is
\[
\beta L_{m,M}>\gamma.
\]

For the Hill-type Mackey–Glass feedback, putting
\[
v=\frac{u}{\theta}
\]
gives
\[
f'(u)
=
\frac{
1+(1-n)v^n
}{
(1+v^n)^2
}.
\]
The classical numerical thresholds are the three positive solutions of
\[
\left|
\frac{
1+(1-n)u^n
}{
(1+u^n)^2
}
\right|
=
\frac12
\]
with
\[
n=9.65.
\]

## Verification
The accompanying checker verifies the variance algebra and computes the classical slope thresholds by deterministic bisection using only the Python standard library.

It verifies that the conditional-moment consequences
\[
\mathbb E[A]=\mathbb E[B],
\qquad
\mathbb E[AB]=\mathbb E[B^2]
\]
imply
\[
\mathbb E[(A-B)^2]
=
\operatorname{Var}(A)-\operatorname{Var}(B).
\]

For
\[
n=9.65
\]
it evaluates
\[
f'(u)
=
\frac{
1+(1-n)u^n
}{
(1+u^n)^2
}
\]
and isolates the three positive roots of
\[
|f'(u)|=\frac12.
\]
The stored values agree with
\[
0.735633145,\qquad
0.845794468,\qquad
1.324883761
\]
to better than
\[
10^{-9}.
\]

The stored checker output is `VERIFY_OK`.

The invariant-measure regression, equality of delayed/current marginals, and equilibrium-rigidity argument are analytic statements on the history-space semiflow and are not inferred from finite simulation.

## Relationship to prior work
Mackey and Glass introduced the physiological delay equation in 1977 and exhibited periodic and apparently chaotic behavior.

A modern authoritative account writes the Mackey–Glass equation in the same delayed-feedback form and emphasizes its role as an archetypal scalar delay equation with periodic and chaotic regimes.

Bartha, Krisztin, and Vígh rigorously construct stable periodic orbits for the classical Mackey–Glass equation and formulate the natural positive phase space as a continuous-history semiflow. Their work focuses on return maps, limiting nonlinearities, and periodic-orbit existence and stability.

Duruisseaux and Humphries give a detailed bifurcation analysis of the same equation, including period-doubling cascades, bistability, crises, chaotic attractors, and attractor dimension. Targeted searches of the accessible article text did not locate invariant-measure, variance, or stationary-average formulations of the regression proved here.

Rigorous integration work for delay equations proves periodic orbits in Mackey–Glass through computer-assisted Poincaré maps. Those results provide existence and stability certificates for particular recurrent trajectories but do not imply an exact conditional delayed-feedback law for every compact invariant probability measure.

The accepted theorem is therefore complementary to bifurcation and orbit-existence results: it gives a universal stationary relation between present cell concentration and delayed production, and converts it into an exact fluctuation budget and a support-dependent slope obstruction.

## Limitations
The theorem assumes compact support in the positive continuous-history phase space. It does not prove that every positive solution is bounded or that a physical invariant measure exists for every parameter choice.

The local slope condition
\[
\beta L_{m,M}>\gamma
\]
is necessary for a non-equilibrium compact stationary state, not sufficient for oscillation or chaos.

The classical numerical intervals are consequences of the slope obstruction only. They are not asserted to coincide with Hopf, period-doubling, or crisis thresholds.

The original 1977 article is used for model provenance and date rather than a whole-document noncoverage claim. A short equivalent stationary identity could remain in unindexed delay-equation literature.

## References
1. M. C. Mackey and L. Glass, “Oscillation and Chaos in Physiological Control Systems,” Science 197, 287–289 (1977), DOI 10.1126/science.267326.
2. L. Glass and M. C. Mackey, “Mackey-Glass equation,” Scholarpedia 5, 6908 (2010), DOI 10.4249/scholarpedia.6908.
3. F. A. Bartha, T. Krisztin, and A. Vígh, “Stable periodic orbits for the Mackey–Glass equation,” Journal of Differential Equations 296, 15–49 (2021), DOI 10.1016/j.jde.2021.05.052.
4. V. Duruisseaux and A. R. Humphries, “Bistability, bifurcations and chaos in the Mackey-Glass equation,” Journal of Computational Dynamics 9, 421–450 (2022), DOI 10.3934/jcd.2022009.
5. R. Szczelina and P. Zgliczyński, “Algorithm for Rigorous Integration of Delay Differential Equations and the Computer-Assisted Proof of Periodic Orbits in the Mackey–Glass Equation,” Foundations of Computational Mathematics 18, 1299–1332 (2018), DOI 10.1007/s10208-017-9369-5.
