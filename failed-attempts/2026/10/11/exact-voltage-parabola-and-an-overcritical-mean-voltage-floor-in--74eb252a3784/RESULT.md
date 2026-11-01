# Exact voltage parabola and an overcritical mean-voltage floor in the autonomous Josephson equation
## Finding
Consider the normalized autonomous Josephson equation on the cylinder
\[
\dot\phi=v,
\qquad
\dot v=I-\sin\phi-\gamma v,
\]
with
\[
I>0,
\qquad
\gamma>0.
\]
Here \(I\) is the normalized dc bias, \(v\) is the normalized junction voltage, and \(\gamma\) is the damping coefficient.

Let \(\mu\) be any compactly supported invariant Borel probability measure on
\[
\mathbb S^1\times\mathbb R.
\]
Then the Josephson force has the exact voltage-conditioned regression
\[
\boxed{
\mathbb E_\mu[\sin\phi\mid v]
=
I-\gamma v
}.
\]
Equivalently, for every bounded Borel function \(f\),
\[
\boxed{
\mathbb E_\mu[
f(v)(\sin\phi-I+\gamma v)
]
=
0
}.
\]

Because a conditional expectation of \(\sin\phi\) must lie in the interval
\[
[-1,1],
\]
the voltage satisfies the almost-sure strip
\[
\boxed{
\frac{I-1}{\gamma}
\le
v
\le
\frac{I+1}{\gamma}
}.
\]

A periodic phase test gives the second exact balance
\[
\boxed{
\mathbb E_\mu[v\sin\phi]=0
}.
\]
Writing
\[
m=\mathbb E_\mu[v],
\]
the two identities combine to give the exact dc power law
\[
\boxed{
\gamma\mathbb E_\mu[v^2]
=
Im
}
\]
and hence the voltage-variance parabola
\[
\boxed{
\operatorname{Var}_\mu(v)
=
m\left(
\frac I\gamma-m
\right)
}.
\]

The regression residual is exactly the acceleration:
\[
\sin\phi
=
I-\gamma v-\dot v.
\]
Since
\[
\mathbb E_\mu[\dot v\mid v]=0,
\]
conditional orthogonality gives
\[
\boxed{
\operatorname{Var}_\mu(\sin\phi)
=
\gamma^2\operatorname{Var}_\mu(v)
+
\mathbb E_\mu[\dot v^2]
}
\]
and
\[
\boxed{
\operatorname{Cov}_\mu(v,\sin\phi)
=
-\gamma\operatorname{Var}_\mu(v)
}.
\]

The equilibrium-supported states are exactly the zero-defect endpoint. More precisely, if
\[
m=0
\]
or
\[
\mathbb E_\mu[\dot v^2]=0,
\]
then \(\mu\) is supported on equilibria
\[
v=0,
\qquad
\sin\phi=I.
\]
Conversely, every equilibrium-supported invariant probability measure has both quantities equal to zero.

Therefore every compact stationary state that is not supported on equilibria satisfies
\[
\boxed{
0<m<\frac I\gamma
}.
\]

For overcritical bias
\[
I>1,
\]
there are no equilibria. In that regime every compact stationary state satisfies the stronger universal mean-voltage floor
\[
\boxed{
\frac{I^2-1}{I\gamma}
<
m
<
\frac I\gamma
}.
\]
The lower bound is strictly stronger than the pointwise-strip consequence
\[
m\ge\frac{I-1}{\gamma}.
\]

Finally, every non-equilibrium compact stationary state has
\[
\operatorname{Var}_\mu(v)>0
\]
and
\[
\mathbb E_\mu[\dot v^2]>0,
\]
so the voltage and Josephson current are strictly anticorrelated:
\[
\boxed{
-1
<
\operatorname{Corr}_\mu(v,\sin\phi)
<
0
}.
\]
More precisely,
\[
\boxed{
\operatorname{Corr}_\mu(v,\sin\phi)
=
-
\left(
1+
\frac{\mathbb E_\mu[\dot v^2]}
{\gamma^2\operatorname{Var}_\mu(v)}
\right)^{-1/2}
}.
\]

## Assumptions and scope
The theorem concerns the autonomous resistively and capacitively shunted Josephson equation after the standard nondimensionalization and after taking constant damping. The phase \(\phi\) is an angular variable, so the natural phase space is the cylinder.

Compact support guarantees all moments used below. No ergodicity assumption is needed.

For
\[
0<I<1,
\]
there are two equilibrium phases modulo \(2\pi\). At
\[
I=1,
\]
they merge. For
\[
I>1,
\]
there is no equilibrium, and the overcritical lower bound applies to every compact invariant probability measure.

The source date is 15 April 1968, the verified public date of Stewart's foundational damped-pendulum Josephson model. A modern mathematical study of the Josephson equation lists \(34C07\) first in its Mathematics Subject Classification; that code is used here.

## Proof
Let \(L\) be the flow generator.

For any continuous function \(\psi\) on the compact voltage projection of the support, choose an antiderivative \(G\) satisfying
\[
G'(v)=\psi(v).
\]
Then
\[
LG
=
\psi(v)
\left(
I-\sin\phi-\gamma v
\right).
\]
Invariance yields
\[
\mathbb E_\mu[
\psi(v)
(
I-\sin\phi-\gamma v
)
]
=
0
\]
for every \(\psi\). Hence
\[
\mathbb E_\mu[\sin\phi\mid v]
=
I-\gamma v.
\]

Since
\[
-1\le\sin\phi\le1,
\]
its conditional expectation also lies in that interval. Therefore
\[
-1
\le
I-\gamma v
\le
1
\]
almost surely, proving the voltage strip.

Next use the periodic test
\[
F(\phi)=\cos\phi.
\]
Because
\[
LF=-v\sin\phi,
\]
stationarity gives
\[
\mathbb E[v\sin\phi]=0.
\]

Multiply the conditional regression by \(v\) and average:
\[
0
=
\mathbb E[v\sin\phi]
=
I\mathbb E[v]
-
\gamma\mathbb E[v^2].
\]
Thus
\[
\gamma\mathbb E[v^2]
=
Im.
\]
Subtracting \(m^2\) gives
\[
\operatorname{Var}(v)
=
m\left(
\frac I\gamma-m
\right).
\]

For the variance defect, rewrite the equation as
\[
\sin\phi
=
I-\gamma v-\dot v.
\]
The conditional regression is exactly
\[
\mathbb E[\dot v\mid v]=0.
\]
Thus \(\dot v\) is orthogonal in \(L^2(\mu)\) to every square-integrable function of \(v\). Centering the previous identity therefore yields
\[
\operatorname{Var}(\sin\phi)
=
\gamma^2\operatorname{Var}(v)
+
\mathbb E[\dot v^2]
\]
and
\[
\operatorname{Cov}(v,\sin\phi)
=
-\gamma\operatorname{Var}(v).
\]

Suppose first that
\[
m=0.
\]
The power law gives
\[
\mathbb E[v^2]=0,
\]
so
\[
v=0
\]
on the invariant support. Tangency of the vector field then requires
\[
\dot v=I-\sin\phi=0,
\]
hence the support consists of equilibria.

Now suppose
\[
\mathbb E[\dot v^2]=0.
\]
Then
\[
\dot v=0
\]
on the invariant support, so \(v\) is constant along every support trajectory. If that constant were nonzero, the equation
\[
\dot\phi=v
\]
would make \(\phi\) wind around the circle, while
\[
\sin\phi=I-\gamma v
\]
would have to remain constant. This is impossible. Hence
\[
v=0,
\]
and again
\[
\sin\phi=I,
\]
so the support is equilibrium-supported.

Conversely, equilibrium-supported measures plainly have
\[
m=0
\]
and
\[
\dot v=0.
\]

Every non-equilibrium invariant measure therefore has
\[
\operatorname{Var}(v)>0.
\]
The exact parabola and \(I>0\) then imply
\[
0<m<\frac I\gamma.
\]

It remains to sharpen the lower bound for
\[
I>1.
\]
There are no equilibria, so
\[
\mathbb E[\dot v^2]>0.
\]
The variance defect gives
\[
\gamma^2\operatorname{Var}(v)
<
\operatorname{Var}(\sin\phi).
\]
Because
\[
|\sin\phi|\le1,
\]
\[
\operatorname{Var}(\sin\phi)
\le
1-
\mathbb E[\sin\phi]^2.
\]
The regression gives
\[
\mathbb E[\sin\phi]
=
I-\gamma m.
\]
Using the voltage parabola,
\[
\gamma I m-\gamma^2m^2
<
1-
(I-\gamma m)^2.
\]
After cancellation,
\[
I\gamma m>I^2-1,
\]
which is exactly
\[
m>
\frac{I^2-1}{I\gamma}.
\]

Finally,
\[
\operatorname{Corr}(v,\sin\phi)
=
\frac{-\gamma\operatorname{Var}(v)}
{\sqrt{
\operatorname{Var}(v)
\operatorname{Var}(\sin\phi)
}},
\]
and substitution of the exact variance defect gives the displayed strict correlation formula.

## Verification
The packaged checker uses only the Python standard library and exact rational arithmetic.

It verifies the stationary power-law algebra
\[
\gamma\mathbb E[v^2]
=
I\mathbb E[v]
\]
and its conversion to
\[
\operatorname{Var}(v)
=
m(I/\gamma-m).
\]

It checks the orthogonal-residual formulas
\[
\operatorname{Var}(\sin\phi)
=
\gamma^2\operatorname{Var}(v)
+
\mathbb E[\dot v^2]
\]
and
\[
\operatorname{Cov}(v,\sin\phi)
=
-\gamma\operatorname{Var}(v).
\]

At the exact test parameters
\[
I=\frac32,
\qquad
\gamma=\frac23,
\]
it verifies the overcritical floor
\[
\frac54<m<\frac94
\]
for the test mean
\[
m=2,
\]
and checks the corresponding exact second moment and variance.

The stored checker output is `VERIFY_OK`.

The conditional expectation, equality classification, and overcritical strictness are analytic proofs; no finite orbit simulation is used.

## Relationship to prior work
Stewart's 1968 work models a Josephson junction by a driven damped pendulum and studies dc current-voltage curves, including hysteretic behavior.

Belykh, Pedersen, and Soerensen give a detailed autonomous shunted-junction phase-plane analysis with capacitance, constant bias, and current-voltage characteristics. Their focus is the qualitative decomposition of parameter space and the resulting orbit types and dc response.

Modern global-dynamics work classifies bifurcations and limit-cycle configurations for the Josephson equation on the cylinder. A complete modern study writes
\[
\beta\Phi''+(1+\gamma\cos\Phi)\Phi'+\sin\Phi=\alpha
\]
and proves bounds on the number and configuration of contractible and non-contractible limit cycles.

These works motivate the mean voltage as a central observable but do not implication-wise determine the accepted invariant-measure regression. The identity
\[
\mathbb E[\sin\phi\mid v]
=
I-\gamma v
\]
encodes every weighted relation
\[
\mathbb E[
f(v)(\sin\phi-I+\gamma v)
]
=
0,
\]
and the strict overcritical lower floor additionally uses the residual acceleration energy.

The accepted result does not re-claim the Josephson model, its current-voltage curves, equilibrium threshold, phase portraits, or limit-cycle bifurcations.

## Limitations
The result assumes the autonomous constant-damping Josephson equation and compactly supported invariant probability measures.

The mean-voltage floor is proved for overcritical bias
\[
I>1.
\]
It does not determine a unique current-voltage branch or the full invariant distribution.

The foundational 1968 source was checked from its bibliographic record and abstract; a full-text retrieval attempt did not succeed in the checked route.

A 2020 global-dynamics article was compared from its published abstract and from its detailed use in the complete 2023 study rather than from a complete local full-text copy.

Classical Josephson literature is extensive, and an equivalent short power balance may have appeared implicitly. The originality assessment concerns the combined conditional regression, exact variance parabola, residual-energy defect, equality rigidity, and strict overcritical mean-voltage floor.

## References
1. W. C. Stewart, “Current-Voltage Characteristics of Josephson Junctions,” Applied Physics Letters 12, 277–280 (1968), DOI 10.1063/1.1651991.
2. V. N. Belykh, N. F. Pedersen, and O. H. Soerensen, “Shunted-Josephson-junction model. I. The autonomous case,” Physical Review B 16, 4853–4859 (1977), DOI 10.1103/PhysRevB.16.4853.
3. H. Chen and Y. Tang, “Global dynamics and bifurcations of the Josephson equation,” Journal of Differential Equations (2020), DOI 10.1016/j.jde.2020.03.048.
4. X. Yu, H. Chen, and C. Liu, “The number of limit cycles of Josephson equation,” Discrete and Continuous Dynamical Systems - B 29, 2947–2971 (2024), DOI 10.3934/dcdsb.2023208.
