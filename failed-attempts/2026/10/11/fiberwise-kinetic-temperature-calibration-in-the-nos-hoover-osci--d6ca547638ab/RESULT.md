# Fiberwise kinetic-temperature calibration in the Nosé–Hoover oscillator
## Finding
Consider the classical normalized Nosé–Hoover oscillator
\[
\dot x=-y-xz,
\qquad
\dot y=x,
\qquad
\dot z=\alpha(x^2-1),
\]
with
\[
\alpha>0.
\]

Here \(x\) is the oscillator momentum, \(y\) the position, and \(z\) the thermostat friction variable.

Every compactly supported invariant Borel probability measure \(\mu\) satisfies two exact fiberwise laws:
\[
\boxed{\mathbb E_\mu[x\mid y]=0}
\]
and
\[
\boxed{\mathbb E_\mu[x^2\mid z]=1}.
\]

Thus momentum is centered at every position level, while the squared momentum has exactly the target kinetic temperature on every thermostat-variable level.

The second law is equivalently the infinite family
\[
\boxed{
\mathbb E_\mu[(x^2-1)g(z)]=0
}
\]
for every bounded Borel function \(g\).

Since
\[
\dot z=\alpha(x^2-1),
\]
the same calibration gives the exact thermostat-speed defect
\[
\boxed{
\operatorname{Var}_\mu(x^2)
=
\frac{1}{\alpha^2}
\mathbb E_\mu[\dot z^2]
}.
\]

This defect is strictly positive for every compact invariant probability measure. Therefore every such measure gives positive mass to both regions
\[
|x|<1
\]
and
\[
|x|>1.
\]

Consequently every nonempty compact invariant set of the Nosé–Hoover flow intersects both sides of the thermostat nullcline
\[
|x|=1.
\]
In particular, every periodic orbit and every invariant torus crosses between sub-target and super-target kinetic-energy regions.

The global time-average identity
\[
\mathbb E[x^2]=1,
\]
the vanishing mean thermostat friction, and repeated crossing of the plane
\[
z=0
\]
are established prior phenomena. The finding assessed here is the stronger all-invariant-measures fiberwise calibration
\[
\mathbb E[x^2\mid z]=1
\]
together with its strict variance-defect and \(|x|=1\) crossing consequences.

## Assumptions and scope
The measure \(\mu\) is invariant under the autonomous Nosé–Hoover flow and has compact support in \(\mathbb R^3\). Compact support guarantees integrability of the polynomial observables and arbitrary one-variable antiderivative tests used below.

The parameter
\[
\alpha=\frac1Q
\]
is the reciprocal thermostat mass in the standard normalization.

Hoover's physical-time reformulation of the Nosé thermostat was published on 1 March 1985. In the notation
\[
(q,p,\zeta),
\]
the equations are
\[
\dot q=p,
\qquad
\dot p=-q-\zeta p,
\qquad
\dot\zeta=\frac{p^2-1}{Q}.
\]
The present variables are
\[
x=p,\qquad y=q,\qquad z=\zeta.
\]

A same-object mathematical treatment classifies the Nosé–Hoover equation under MSC \(34C05\) and \(34A34\). The present result is classified under \(34C05\).

No ergodicity assumption is made. The theorem applies separately to periodic-orbit measures, quasiperiodic torus measures, compact chaotic invariant measures, and convex mixtures of compact invariant measures.

## Proof
Let \(L\) denote the generator of the flow.

Fix a continuous function \(\phi\) on the compact \(y\)-range of the support. Choose a continuously differentiable antiderivative \(H\) with
\[
H'(y)=\phi(y).
\]
Then
\[
LH
=
\phi(y)\dot y
=
\phi(y)x.
\]
Invariance gives
\[
\mathbb E_\mu[\phi(y)x]=0
\]
for every such \(\phi\). Hence
\[
\mathbb E_\mu[x\mid y]=0.
\]

Now fix a continuous function \(\psi\) on the compact \(z\)-range and choose an antiderivative \(K\) with
\[
K'(z)=\psi(z).
\]
Then
\[
LK
=
\alpha\psi(z)(x^2-1).
\]
Invariance gives
\[
\mathbb E_\mu[\psi(z)(x^2-1)]=0
\]
for every continuous \(\psi\). Therefore
\[
\mathbb E_\mu[x^2\mid z]=1.
\]
By the usual monotone-class extension, the orthogonality identity holds for every bounded Borel function \(g(z)\).

Taking expectations gives the known global thermostat balance
\[
\mathbb E_\mu[x^2]=1.
\]
Since
\[
x^2-1=\frac{\dot z}{\alpha},
\]
we obtain
\[
\operatorname{Var}_\mu(x^2)
=
\mathbb E_\mu[(x^2-1)^2]
=
\frac1{\alpha^2}\mathbb E_\mu[\dot z^2].
\]

We now prove strictness.

Suppose
\[
\operatorname{Var}_\mu(x^2)=0.
\]
Then
\[
x^2=1
\]
almost surely. Because the support is invariant and the vector field is continuous, every complete trajectory in the support satisfies
\[
x(t)^2=1
\]
for all \(t\). Continuity prevents \(x(t)\) from switching between \(1\) and \(-1\) without passing through zero, so \(x\) is constant on each support trajectory.

But
\[
\dot y=x
\]
then gives
\[
y(t)=y(0)\pm t,
\]
which is unbounded. This contradicts compactness of the invariant support. Therefore
\[
\operatorname{Var}_\mu(x^2)>0
\]
for every compact invariant probability measure.

Since
\[
\mathbb E_\mu[x^2]=1
\]
and \(x^2\) is not almost surely constant, neither inequality
\[
x^2\le1
\]
nor
\[
x^2\ge1
\]
can hold almost surely. Hence
\[
\mu\{|x|<1\}>0
\]
and
\[
\mu\{|x|>1\}>0.
\]

Finally, let \(K\) be a nonempty compact invariant set. The Krylov–Bogolyubov averaging argument supplies an invariant probability measure supported on \(K\). The preceding conclusion rules out
\[
K\subseteq\{|x|\le1\}
\]
and
\[
K\subseteq\{|x|\ge1\}.
\]
Thus every nonempty compact invariant set intersects both
\[
|x|<1
\]
and
\[
|x|>1.
\]

## Verification
The accompanying checker uses only the Python standard library and exact rational arithmetic.

It verifies the pointwise thermostat residual
\[
x^2-1=\frac{\dot z}{\alpha}.
\]

It verifies the abstract variance identity
\[
\operatorname{Var}(X^2)
=
\mathbb E[(X^2-1)^2]
\]
under the stationary mean
\[
\mathbb E[X^2]=1.
\]

It also checks the elementary strict-crossing implication: a nonconstant nonnegative random variable with mean \(1\) must have positive mass on both sides of \(1\) whenever it cannot be supported entirely on one side.

The stored checker output is `VERIFY_OK`.

The conditional-expectation identities and the compact-invariant-set crossing theorem are analytic arguments; they are not inferred from finite numerical trajectories.

## Relationship to prior work
Hoover's 1985 paper derives the physical-time Nosé–Hoover equations and explicitly writes, for a one-dimensional harmonic oscillator,
\[
\dot q=p,
\qquad
\dot p=-q-\zeta p,
\qquad
\dot\zeta=\frac{p^2-1}{Q}.
\]
It also identifies the canonical extended-phase-space density and shows how the thermostat variable controls kinetic temperature.

Posch, Hoover, and Vesely then demonstrate that the oscillator has both regular and chaotic trajectories and is not sufficiently chaotic to reproduce the canonical distribution from a single initial condition.

Mahdi and Valls study the exact same polynomial system from Darboux-integrability theory. Their full open preprint states
\[
\dot x=-y-xz,
\qquad
\dot y=x,
\qquad
\dot z=\alpha(x^2-1),
\]
and proves nonintegrability for
\[
\alpha\ne0
\]
within the specified Darboux classes. Their result concerns first integrals and invariant algebraic surfaces, not invariant-measure conditional moments.

Wang and Yang document extensive families of invariant tori and conservative regions in the same oscillator. Niu and Li later rigorously prove infinitely many invariant tori and quasiperiodic solutions in a small-parameter regime.

The global balance
\[
\langle x^2\rangle=1
\]
is prior and follows immediately from the thermostat equation under bounded long-time averaging. Hoover, Sprott, and Hoover also give moment proofs that the mean thermostat friction vanishes. Han and Yang prove that every invariant set crosses the plane
\[
z=0.
\]
Those facts are therefore excluded from the originality claim.

The accepted statement strengthens the known scalar kinetic-temperature balance to every thermostat-variable fiber:
\[
\mathbb E[x^2\mid z]=1.
\]
This is an infinite family of orthogonality constraints, not a single time average. Its strict variance-defect identity and the forced crossing of
\[
|x|=1
\]
are the new consequences assessed here.

## Limitations
The theorem is restricted to compact invariant probability measures and compact invariant sets. It does not classify unbounded trajectories.

The calibration
\[
\mathbb E[x^2\mid z]=1
\]
determines a conditional first moment of \(x^2\), not the complete conditional distribution of momentum.

The theorem does not imply canonical Gaussian statistics or ergodicity. Indeed, the classical Nosé–Hoover oscillator is well known to admit regular invariant tori and noncanonical dynamics.

The global identities
\[
\mathbb E[x^2]=1
\]
and
\[
\mathbb E[z]=0
\]
and the \(z=0\) crossing theorem are prior and are not claimed as original.

Because the fiberwise argument is short once invariant-measure testing is used, a differently phrased equivalent statement could remain in unindexed thermostat literature.

## References
1. W. G. Hoover, “Canonical dynamics: Equilibrium phase-space distributions,” Physical Review A 31, 1695–1697 (1985), DOI 10.1103/PhysRevA.31.1695.
2. H. A. Posch, W. G. Hoover, and F. J. Vesely, “Canonical dynamics of the Nosé oscillator: Stability, order, and chaos,” Physical Review A 33, 4253–4265 (1986), DOI 10.1103/PhysRevA.33.4253.
3. A. Mahdi and C. Valls, “Integrability of the Nosé–Hoover equation,” Journal of Geometry and Physics 61, 1348–1352 (2011), DOI 10.1016/j.geomphys.2011.02.018.
4. L. Wang and X.-S. Yang, “A vast amount of various invariant tori in the Nosé–Hoover oscillator,” Chaos 25, 123110 (2015), DOI 10.1063/1.4937167.
5. W. G. Hoover, J. C. Sprott, and C. G. Hoover, “The Nosé-Hoover, Dettmann, and Hoover-Holian Oscillators,” Computational Methods in Science and Technology 25, 121–124 (2019), DOI 10.12921/cmst.2019.0000031.
6. Q. Han and X.-S. Yang, “Qualitative Analysis of the Nosé–Hoover Oscillator,” Qualitative Theory of Dynamical Systems 19, article 8 (2020), DOI 10.1007/s12346-020-00340-1.
