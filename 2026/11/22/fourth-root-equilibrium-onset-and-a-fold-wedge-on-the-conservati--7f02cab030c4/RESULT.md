# Fourth-root equilibrium onset and a fold wedge on the conservative sine-flow cylinders

## Finding

For the conservative unforced Ramar sine flow
\[
\dot x=-kyz,\qquad \dot y=b\sin x+xz,\qquad \dot z=gxy,
\qquad b,g,k>0,
\]
there are two smooth first integrals on the complement of the invariant axis \(x=z=0\). Their differentials are independent precisely at the non-equilibrium points in that domain. The first integral \(P=gx^2+kz^2\) has invariant cylinders \(P=R^2>0\), circular in the scaled \((\sqrt g\,x,y,\sqrt k\,z)\) coordinates.

Fix \(b,k>0\), and write \(g_0=kb^2/3\), \(\delta=g-g_0\), \(\varepsilon=R^2-kb^2\), \(h=2kb^2/45\). The following equilibrium counts and types hold locally near the lower pole and near \((\delta,\varepsilon)=(0,0)\).

* At \(\delta=0\), small \(\varepsilon>0\) gives exactly one symmetric off-axis saddle pair, with
  \[
  x_\pm=\pm\left(\frac{45\varepsilon}{2kb^2}\right)^{1/4}
  (1+O(\varepsilon^{1/2})),\qquad
  z_\pm=-b+\frac b6 x_\pm^2+O(x_\pm^4),\qquad y_\pm=0.
  \]
  For \(\varepsilon<0\) there is no nearby off-axis pair.
* For small \(\delta<0\), the two symmetry-related saddle–center collisions occur at the same fold value
  \[
  \varepsilon_f(\delta)=-\frac{45}{8kb^2}\delta^2+O(|\delta|^3).
  \]
  Below it there are no nearby off-axis equilibria. At the fold there is one degenerate pair. For \(\varepsilon_f(\delta)<\varepsilon<0\) there is one inner center pair and one outer saddle pair. For \(\varepsilon>0\) there is one saddle pair.
* For small \(\delta>0\), \(\varepsilon>0\) gives one nearby saddle pair and \(\varepsilon<0\) gives none.

All types refer to dynamics on the specified invariant cylinder. The axial equilibrium \((0,0,-R/\sqrt k)\) is a saddle for \(R<b\sqrt k\), a center for \(R>b\sqrt k\), and nonhyperbolic at equality. The upper axial equilibrium \((0,0,R/\sqrt k)\) is a center for every \(R>0\).

## Assumptions and scope

This is the \(a=c=d=0\) limit of \(\dot x=ax-kyz,\ \dot y=b\sin x+xz,\ \dot z=gxy-cz+d\). The local counts concern only the negative-\(z\) half of the cylinder, in a fixed small interval of \(x\). The parameter neighborhood can be chosen jointly for \(\delta,\varepsilon\); all asymptotics fix \(b,k>0\). The cylinder label \(R\) is constant along a trajectory, not a third dynamical variable of the reduced system.

## Proof

**Integrals and pole types.** Differentiation gives \(\dot P=0\). On \(P=R^2>0\), let \(x=R\cos\theta/\sqrt g\) and \(z=R\sin\theta/\sqrt k\). The first and third equations imply \(\dot\theta=\sqrt{gk}\,y\), so \(\ddot\theta=F_R(\theta)\), where
\[
 F_R(\theta)=b\sqrt{gk}\sin\!\left(\frac R{\sqrt g}\cos\theta\right)+R^2\sin\theta\cos\theta.
\]
Put \(J_R(\theta)=\int_0^\theta\sin((R/\sqrt g)\cos u)\,du\). The integrand is antiperiodic under a shift of \(\pi\), hence \(J_R\) is \(2\pi\)-periodic. The function
\[
 H=\frac{gk}{2}y^2-b\sqrt{gk}\,J_R(\theta)-\frac{R^2}{2}\sin^2\theta
\]
is single-valued and smooth for \(R=\sqrt P>0\), and \(\dot H=0\). There \(dP\ne0\), and the restriction of \(dH\) to the cylinder is \(gk y\,dy-F_R(\theta)\,d\theta\). This restriction vanishes exactly when \(y=0=F_R(\theta)\), the cylinder equilibria. This gives the stated locus of independence, in particular excluding the axial poles. The angular potential is bounded at fixed \(R\), so energy bounds \(y\); together with \(P\) this bounds each trajectory and implies completeness. The degenerate axis consists of equilibria. On each positive-radius cylinder every connected regular level component of \(H\) is compact and carries a periodic orbit: it is a circle, and the reduced vector field has no zero there.

The cylinder linearization has \(\lambda^2=F_R'(\theta)\) at an equilibrium. A positive derivative gives a hyperbolic saddle; a negative one makes the conserved energy have a nondegenerate local minimum, whose small surrounding levels give a nonlinear center. At \(3\pi/2\) the derivative is \(R(b\sqrt k-R)\), while at \(\pi/2\) it is \(-R(b\sqrt k+R)\). These yield the stated axial types without using linearization to decide the equality case.

**Off-axis equation.** Use \(s(x)=\sin x/x\), with \(s(0)=1\), and \(z_R(x)=-\sqrt{(R^2-gx^2)/k}\). Locally \(s(x)>0\), \(z_R(x)<0\), and an off-axis equilibrium requires \(y=0\) and \(z_R(x)=-bs(x)\). Thus it is equivalent to
\[
 R^2=\Phi(x)=gx^2+kb^2s(x)^2.
\]
The Taylor series \(s(x)^2=1-x^2/3+2x^4/45-x^6/315+O(x^8)\) yields, in \(t=x^2>0\),
\[
 \varepsilon=G(t;\delta)=\delta t+ht^2-\frac{kb^2}{315}t^3+O(t^4).
\]
The analytic function \(G\) has \(G(0;\delta)=0\), \(G_t(0;\delta)=\delta\), and \(G_{tt}>h\) on a small fixed interval \([0,t_*]\). After shrinking the parameter neighborhood, \(G(t_*;\delta)>\varepsilon\). For \(\delta\ge0\), strict increase on \((0,t_*]\) gives one positive root at \(\varepsilon>0\) and none at \(\varepsilon<0\). At \(\delta=0\), inverting \(\varepsilon=ht^2(1+O(t))\) gives the fourth-root expansion in \(x\); \(z=-bs(x)\) gives the expansion in \(z\).

For \(\delta<0\) sufficiently small, the implicit-function theorem at \((t,\delta)=(0,0)\) gives the unique local minimum at \(t_f=-\delta/(2h)+O(\delta^2)>0\). Its value is \(-\delta^2/(4h)+O(|\delta|^3)\). Strict decrease before and strict increase after this minimum, together with \(G(0;\delta)=0\), give the claimed root counts. Every positive root produces precisely two values \(x=\pm\sqrt t\). Since \(G_{tt}(t_f;\delta)>0\) and the equilibrium equation has nonzero derivative with respect to \(\varepsilon\), the positive root at the minimum is a nondegenerate fold of the scalar equilibrium equation, occurring at both signs of \(x\).

**Off-axis types.** Set \(Q(x)=b\sin x+xz_R(x)\). Rationalizing \(bs(x)+z_R(x)\) gives
\[
 Q(x)=\frac{x(\Phi(x)-R^2)}{k(bs(x)-z_R(x))}.
\]
At a nonzero equilibrium this implies \(Q'(x)=x^2G_t(x^2;\delta)/(kb s(x))\). The relation \(F_R(\theta)=\sqrt{gk}\,Q(x(\theta))\) holds locally, with \(dx/d\theta>0\) on the lower half. The sign of \(F_R'\) is therefore the sign of \(G_t\): saddles on the increasing branch and centers on the decreasing branch. The fold equilibria have \(F_R'=0\).

## Verification

The unchanged companion `check.py` checks the pole derivatives, the off-axis slope identity, and the Taylor coefficients, and gives finite numerical diagnostics for the two leading asymptotics. The functional independence locus, uniform local counts, and equilibrium types follow from the analytic proof above, not from finite diagnostics.

## Relationship to prior work

The full sine-driven system is due to Ramar [1]. The result here specifies the local saddle–center diagram on the invariant cylinders at the unforced conservative boundary. In particular, the fold law locates the simultaneous creation of a center and saddle on each side of the lower pole. The general one-degree-of-freedom Hamiltonian criterion and scalar fold argument are standard; the locus and coefficients here use the specific sine coupling.

## Limitations

The equilibrium diagram is local, not a global census. Its stability statements are restricted to a fixed invariant cylinder. No continuation into nonzero damping, growth or forcing, or conclusion about chaos, is asserted. The two displayed integrals do not have independent differentials at equilibria.

## Reference

1. R. Ramar (2023), “Design of a New Chaotic System with Sine Function: Dynamic Analysis and Offset Boosting Control,” *Chaos Theory and Applications* **5**(2), 118–126. [DOI:10.51537/chaos.1223766](https://doi.org/10.51537/chaos.1223766).
