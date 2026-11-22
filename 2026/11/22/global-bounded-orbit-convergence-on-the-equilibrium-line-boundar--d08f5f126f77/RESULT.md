# Global bounded-orbit convergence on the equilibrium-line boundary of a quadratic jerk family

## Finding

For the polynomial differential equation
\[
\dot x=y,\qquad \dot y=z,\qquad \dot z=-a x-y-\frac{11}{10}z-\alpha z^2+xy,
\]
set \(a=0\) and allow **every** \(\alpha\in\mathbb R\). Every forward solution with bounded image in \(\mathbb R^3\) exists for all positive times and converges to **one** point of the equilibrium line \(\{(\xi,0,0):\xi\in\mathbb R\}\).

Consequently, the only compactly supported invariant Borel probabilities are probability distributions on that equilibrium line; no nonstationary periodic orbit or other non-equilibrium compact recurrent dynamics occurs at \(a=0\), for any \(\alpha\).

## Assumptions and scope

All variables, parameters and initial conditions are real. The coefficient of \(z\) is fixed at \(-11/10\), as in the originating family. Solutions are maximal classical solutions of this polynomial vector field. "Bounded forward solution" means the entire forward image is contained in a bounded subset of \(\mathbb R^3\). This assumption is not removed: the theorem does **not** claim all initial conditions lead to bounded trajectories. An invariant measure is taken with respect to the complete flow on its compact invariant support.

## Proof

**Step 1 (dissipation identity).** Define
\[
W(x,y,z)=z+\frac{11}{10}y+x-\frac{x^2}{2}.
\]
Differentiating along the original vector field at \(a=0\) cancels the linear \(y,z\) terms and the quadratic \(xy\) term, giving the exact polynomial identity
\[
\frac{dW}{dt}=-\alpha z^2. \tag{1}
\]
There are two cases.

**Step 2 (nonzero curvature coefficient).** If \(\alpha\ne0\), \(W\) is monotone on every trajectory, with either sign allowed. For a bounded forward trajectory it is bounded and hence has a finite limit. A bounded polynomial-ODE trajectory cannot terminate in finite time, and its nonempty compact omega-limit set \(\Omega\) is connected and invariant. Because \(W\) has the same limiting value on all of \(\Omega\), every complete trajectory in \(\Omega\) has \(\dot W=0\). Equation (1) forces \(z=0\) throughout \(\Omega\).

If a complete trajectory stays within \(z=0\), then \(\dot y=z=0\), so \(y(t)\) is constant, \(x(t)=x_0+y_0t\), and the remaining equation is \(0=\dot z=y_0(x(t)-1)\). It holds for all time only if \(y_0=0\). Thus the largest invariant subset of \(\{z=0\}\) is the equilibrium line; \(\Omega\) lies on it.

On the equilibrium line \(W(\xi,0,0)=\xi-\xi^2/2\). The equation \(\xi-\xi^2/2=\lim W\) has at most two real solutions. Since \(\Omega\) is nonempty and connected but contained in this finite set, it is a singleton. The bounded trajectory therefore converges to that equilibrium.

**Step 3 (the integrable boundary \(\alpha=0\)).** Now equation (1) says \(W\equiv K\) along each trajectory. From the definition of \(W\),
\[
z=K-\frac{11}{10}y-x+\frac{x^2}{2}.
\]
The projected dynamics is the damped mechanical system
\[
\dot x=y,\qquad\dot y=K-\frac{11}{10}y-x+\frac{x^2}{2}.
\]
Its exact energy
\[
H_K(x,y)=\frac{y^2}{2}+\frac{x^2}{2}-\frac{x^3}{6}-Kx
\]
satisfies
\[
\dot H_K=-\frac{11}{10}y^2. \tag{2}
\]
On a bounded orbit, the energy has a finite limit and the invariant omega-limit set lies in \(\{y=0\}\). Staying in this set requires \(z=\dot y=0\), so the limit set lies on the equilibrium line. Since \(W=K\) restricts its \(x\) coordinate to at most two roots of \(\xi-\xi^2/2=K\), connectedness again makes it a single equilibrium. This proves the assertion for \(\alpha=0\).

**Step 4 (stationary probabilities).** For any compactly supported invariant Borel probability \(\mu\) at \(a=0\), integrate the Lie derivative of the smooth function \(W\). For \(\alpha\ne0\), \(0=\int\dot W\,d\mu=-\alpha\int z^2\,d\mu\), hence \(\mu\) is supported on \(\{z=0\}\). The support is invariant, and the argument of Step 2 reduces it to the equilibrium line. For \(\alpha=0\), use the globally defined polynomial \(H=\tfrac12 y^2+\tfrac12x^2-\tfrac16x^3-Wx\); \(\dot H=-\tfrac{11}{10}y^2\) since \(\dot W=0\). Integrating forces support on \(\{y=0\}\), and invariance forces \(z=0\). Conversely, every probability distribution supported on the equilibrium line is invariant, completing the classification.

## Verification

The companion standalone script `check.py` uses exact symbolic differentiation to verify (1), (2), and the transverse characteristic polynomial. The omega-limit and invariant-measure arguments above are analytic; the symbolic identities alone are not a substitute for those proofs.

## Relationship to prior work

Mei Liu, Bo Sang, Ning Wang and Irfan Ahmad introduced this quadratic jerk family and established a nonchaotic region for \(\alpha=0\), \(a\le0\) (Theorem 2). For \(a=\alpha=0\), they explicitly identify the conserved polynomial \(W\). The theorem here identifies the **whole** coefficient line \(a=0\), \(\alpha\in\mathbb R\), including \(\alpha\ne0\), and supplies convergence to one equilibrium and a complete compact stationary-measure classification. This is not entailed merely by the cited exclusion of bounded chaos or the conserved quantity at its single integrable point.

Related quadratic-jerk recurrence results concern other vector fields and do not imply this statement; general LaSalle principles provide the method but not the parameter-specific dissipation identities.

## Limitations

The theorem is conditional on forward boundedness. It provides no quantitative convergence rate, basin partition, classification of unbounded trajectories, or assertion at \(a\ne0\). General planar damping and omega-limit theorems are established background; historical priority of this exact combination has not been independently audited.

## References

- M. Liu, B. Sang, N. Wang and I. Ahmad, *Chaotic Dynamics by Some Quadratic Jerk Systems*, *Axioms* 10(3), 227 (2021), https://doi.org/10.3390/axioms10030227 ; Sections 3–4, equations (16) and (21), Theorem 2, Remark 1. Public preprint precursor: https://www.researchgate.net/publication/353923644_The_routes_to_chaos_in_some_quadratic_jerk_systems (uploaded August 16, 2021).
- Standard LaSalle invariance and omega-limit connectedness principles for finite-dimensional autonomous flows; used with the explicit formulas proved above.
