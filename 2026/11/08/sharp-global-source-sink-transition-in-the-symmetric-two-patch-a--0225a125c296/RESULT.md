# Sharp global source–sink transition in the symmetric two-patch Allee model

## Finding

For the two-patch cubic Allee model of Kang and Lanchier at the symmetric Allee threshold \(\theta=1/2\), define the dimensionless dispersal \(u=\mu/r>0\). The sharp critical value is \(u_c=1/12\). If \(0<u<1/12\), there are exactly **nine** nonnegative equilibria, four of them asymptotically stable: extinction, full establishment, and a pair of distinct asymmetric source–sink states. If \(u\ge1/12\), the only asymptotically stable equilibria are extinction and full establishment. In fact, at and above this sharp threshold the global outcome from every nonnegative initial state off the invariant divider is decided by the *initial sum alone*:

\[
 x(0)+y(0)>1\Longrightarrow (x(t),y(t))\to(1,1),\qquad
 x(0)+y(0)<1\Longrightarrow(x(t),y(t))\to(0,0).
\]

On \(x+y=1\) the trajectory remains on the divider and approaches an equilibrium there. The number of equilibria is exactly nine for \(0<u<1/12\), five for \(1/12\le u<1/8\), and three for \(u\ge1/8\). At \(u=1/12\), the two asymmetric divider states are nonhyperbolic, but are **not** asymptotically stable in the full plane. The separate threshold \(u=1/8\) is the collision of these two remaining divider equilibria with the symmetric half-occupancy equilibrium; it does not determine loss of the asymmetric attractors.

## Assumptions and scope

The deterministic continuous-time dynamics are
\[
\dot x=r x(x-\tfrac12)(1-x)+\mu(y-x),\qquad
\dot y=r y(y-\tfrac12)(1-y)+\mu(x-y),
\]
with \(r>0\), \(\mu>0\), and any initial \((x(0),y(0))\in[0,\infty)^2\). Both patches have identical local demographic parameters and symmetric linear dispersal. Solutions are global and bounded. Only this exact symmetric Allee threshold is classified; nothing is asserted for unequal thresholds, asymmetric dispersal, environmental noise, or a demographic stochastic analogue. The biological terminology “extinction” and “establishment” denotes the deterministic limits \((0,0)\) and \((1,1)\).

## Proof

**1. Exact reduction and equilibrium classification.** Rescale time by \(\tau=rt\), put \(u=\mu/r\), \(z=x+y-1\), and \(d=x-y\). Direct polynomial expansion gives the exact system
\[
\frac{dz}{d\tau}=-\frac{z}{4}(3d^2+z^2-1),\qquad
\frac{dd}{d\tau}=-\frac{d}{4}(d^2+8u+3z^2-1).
\tag{1}
\]
For \(d=0\) there are the three constant states \((x,y)=(0,0),(1/2,1/2),(1,1)\). For \(z=0\) and \(d\ne0\), there are the two equilibria
\[
(x,y)=\frac12\bigl(1\pm\sqrt{1-8u},\ 1\mp\sqrt{1-8u}\bigr),\qquad 0<u<1/8,
\tag{2}
\]
with the limiting coincident symmetric point at \(u=1/8\). For \(zd\ne0\), the two equations in (1) give
\[
 z^2=\frac{1-12u}{4},\qquad d^2=\frac{1+4u}{4}.
\tag{3}
\]
There are exactly four sign combinations when \(0<u<1/12\), each with \(x=(1+z+d)/2\) and \(y=(1+z-d)/2\) in \((0,1)\). The conditions \(z=0\), \(d=0\), and \(zd\ne0\) exhaust all equilibria. At \(u=1/12\), (3) merges into (2), giving five distinct equilibria. At \(u=1/8\), (2) merges into the symmetric half-occupancy state, giving three.

**2. Stability.** In the \((z,d)\) coordinates, the Jacobian is symmetric:
\[
 J=\begin{pmatrix}
 (1-3z^2-3d^2)/4&-3zd/2\\
 -3zd/2&(1-3z^2-3d^2)/4-2u
 \end{pmatrix}.
\]
Both \((0,0)\) and \((1,1)\) have strictly negative eigenvalues \(-1/2\) and \(-1/2-2u\). The half-occupancy equilibrium has eigenvalues \(1/4\) and \(1/4-2u\), so it is never attracting. The off-divider equilibria of (3) have
\[
\det J=\frac{(1+4u)(12u-1)}8<0,
\]
and are saddles. At the divider equilibria of (2), the two eigenvalues are exactly \(6u-1/2\) and \(4u-1/2\). Therefore they are attracting for \(0<u<1/12\) and saddles for \(1/12<u<1/8\). At the equality \(u=1/12\) one eigenvalue is zero and the other equals \(-1/6\). Writing \(d_0=\pm1/\sqrt3\), the smooth local center manifold through \((z,d)=(0,d_0)\) obeys
\[
 d^2=\frac13-3z^2+O(z^4),\qquad
 \frac{dz}{d\tau}=2z^3+O(z^5).
\tag{4}
\]
The positive cubic coefficient proves that these critical equilibria repel transversely to the invariant line \(z=0\); their local stable sets lie on that line. This proves the sharp stable-source–sink cutoff including equality.

Writing \(w=d^2\), its equation at \(u=1/12\) is \(dw/d\tau=-w(w-1/3+3z^2)/2\). A center manifold tangent to the \(z\)-axis has \(w=1/3+az^2+O(z^4)\). Since its first equation gives \(dz/d\tau=O(z^3)\), differentiating the center manifold gives \(dw/d\tau=O(z^4)\), whereas the exact equation for \(w\) has quadratic coefficient \(-(a+3)/6\). Thus \(a=-3\), and substitution gives the positive cubic drift in (4). The invariant line \(z=0\) is the one-dimensional strong-stable manifold; positive cubic drift on the center manifold excludes off-divider convergence to either critical point.


**3. Global convergence and exact divider.** The nonnegative quadrant is forward invariant, since on \(x=0\) the first derivative equals \(\mu y\ge0\) and similarly on \(y=0\). Every closed square \([0,M]^2\) with \(M\ge\max\{1,x(0),y(0)\}\) is forward invariant: on each top/right face, the local cubic is nonpositive and migration points inward. Define \(f(v)=v(v-1/2)(1-v)\) and the polynomial potential
\[
\Phi(x,y)=\int_0^x f(v)\,dv+\int_0^y f(v)\,dv-\frac u2(x-y)^2.
\]
The rescaled vector field is \(\nabla\Phi\). Consequently \(d\Phi/d\tau=(dx/d\tau)^2+(dy/d\tau)^2\ge0\), with equality only at an equilibrium. LaSalle's invariance argument confines every bounded omega-limit set to the finite equilibrium set found above. Since an omega-limit set of a bounded continuous trajectory is connected, each trajectory converges to one equilibrium; no recurrent nonconstant orbit remains.

The exact first equation in (1) preserves the strict sign of \(z\). For \(u>1/12\), any divider equilibrium with \(z=0\) is repelling in the \(z\)-direction: at \((z,d)=(0,0)\), the \(z\)-eigenvalue is \(1/4\); at the asymmetric divider states (when present), it is \(6u-1/2>0\). Thus no orbit with \(z(0)\ne0\) can converge to the divider. For \(u=1/12\), the same conclusion holds at the asymmetric divider states by (4); at the central state the \(z\)-eigenvalue remains \(1/4\). All other equilibrium points for \(u\ge1/12\) are \((0,0)\) with \(z=-1\) and \((1,1)\) with \(z=1\). Their basins from the open half-planes are therefore exactly \(z<0\) and \(z>0\), respectively. For \(0<u<1/12\), the additional pair of attracting equilibria has open basins, including initial conditions with \(z\ne0\); hence this universal initial-sum rule fails below the threshold.

## Verification

The included standalone `verify.py` runs using only the Python standard library. It checks the transformed polynomial dynamics, Jacobian characteristic invariants, closed-form equilibrium branches, eigenvalue identities and exact critical cubic coefficient using rational arithmetic where possible; high-precision checks independently evaluate all real branch coordinates. The observed execution reports 1,292 checks passed. These checks reinforce, but do not replace, the exact calculations and dynamical arguments above. Run from the extracted files with `python verify.py`.

## Relationship to prior work

Kang and Lanchier introduced the cubic symmetric two-patch Allee model in a publicly posted 2010 preprint, subsequently published in 2011. Their Theorems 2.1–2.4 give sufficient large-dispersal conditions, weak-dispersal equilibrium bounds, and numerical bifurcation evidence; they do not state the exact \(\theta=1/2\) global basin threshold \(\mu/r=1/12\) or the complete 9–5–3 equilibrium classification. In particular, their large-dispersal condition at \(\theta=1/2\) is \(\mu/r>1/8\), which is sufficient but not sharp for the global initial-sum basin divider proved here. The ecological strong Allee effect and diffusive-coupling framework are prior art, and the potential/gradient-flow method is standard. The contribution is the complete, sharp parameter-specific classification and global basin criterion, not an original general principle of gradient dynamics.

Chen, Liu and Chen (first published 2021) study an *additive* Allee model with one sink and one source and asymmetric migration, not the identical cubic equations analyzed here. General Allen–Cahn and graph-gradient theory supports the use of a potential but does not, in the inspected sources, specify this ecological threshold and full equilibrium diagram. No claim of exhaustive historical priority is made.

## Limitations

The theorem is confined to \(\theta=1/2\), identical patches, cubic deterministic dynamics, and positive symmetric dispersal. The critical point requires a standard local center-manifold reduction; without that calculation the equality case would not follow from linearization alone. The result does not yield stochastic fixation probabilities, finite-time extinction distributions, or an ecological management prescription. Uninspected older literature on two coupled bistable units could contain an equivalent rescaling or stronger theorem; independent priority assessment remains outstanding.

## References

1. Y. Kang and N. Lanchier, *Expansion or extinction: deterministic and stochastic two-patch models with Allee effects*, publicly posted February 27, 2010, arXiv:1003.0121, https://arxiv.org/abs/1003.0121 ; journal version, *Journal of Mathematical Biology* **62** (2011), 925–973, https://doi.org/10.1007/s00285-010-0359-3.
2. L. Chen, T. Liu and F. Chen, *Stability and bifurcation in a two-patch model with additive Allee effect*, *AIMS Mathematics* **7** (2022), 536–551, first published October 14, 2021, https://doi.org/10.3934/math.2022034.
