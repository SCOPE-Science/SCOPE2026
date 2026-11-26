# Two exact loss thresholds for spatially asymmetric states in the balanced two-patch Allee model

## Finding
Let two identical habitats exchange individuals at rate \(m>0\). The balanced Allee threshold \(1/2\) is the unique threshold at which both local survival wells are symmetric under replacing occupied by vacant density. The deterministic two-patch system has a sharp **attractor-loss** boundary at \(m=1/12\), strictly below the **last-asymmetric-equilibrium** boundary \(m=1/8\). In particular, increasing dispersal can remove both locally persistent mixed-population states while retaining two unstable asymmetric equilibrium configurations throughout \(1/12<m<1/8\).

Precisely, the number of distinct equilibria in the biological square is nine when \(0<m<1/12\), five when \(1/12\le m<1/8\), and three when \(m\ge1/8\). Exactly four equilibria are asymptotically stable for \(0<m<1/12\), and exactly two for every \(m\ge1/12\). Every orbit in that square converges to an equilibrium.

## Assumptions and scope
The densities \(x,y\in[0,1]\) obey
\[
\dot x=x(x-\tfrac12)(1-x)+m(y-x),\qquad
\dot y=y(y-\tfrac12)(1-y)+m(x-y),\qquad m>0.
\]
The unit square is forward invariant: at a zero-density boundary the inward derivative is nonnegative, and at a unit-density boundary it is nonpositive. The model assumes identical habitats, continuous deterministic time, cubic density-dependent local growth, and symmetric density-independent migration. No stochastic or multi-patch conclusion is made. More general growth prefactors \(r>0\) reduce to this normalization with \(m\) replaced by \(m/r\), so both critical migration rates scale linearly with \(r\).

## Proof
Write \(s=(x+y-1)/2\), \(d=(x-y)/2\), so \(x=1/2+s+d\) and \(y=1/2+s-d\). Direct expansion, without dividing by any possibly vanishing factor, gives
\[
\dot s=-s(3d^2+s^2-\tfrac14),\qquad
\dot d=-d(d^2+3s^2+2m-\tfrac14). \tag{1}
\]
A symmetric equilibrium has \(d=0\) and thus \(s\in\{-1/2,0,1/2\}\), giving \((0,0),(1/2,1/2),(1,1)\). Suppose instead that \(d\ne0\). Its equation gives \(d^2+3s^2=1/4-2m\). The first equation in (1) then implies one of two mutually exhaustive families.

**Family A, \(s=0\):** the two points
\[
(x,y)=(\tfrac12\pm\sqrt{\tfrac14-2m},\tfrac12\mp\sqrt{\tfrac14-2m}) \tag{2}
\]
exist as distinct interior points exactly for \(0<m<1/8\). Their Jacobian in \((s,d)\) has eigenvalues \(6m-1/2\) and \(4m-1/2\). Both are negative for \(m<1/12\), and the point is a saddle for \(1/12<m<1/8\).

**Family B, \(3d^2+s^2=1/4\):** substituting in the \(d\)-equation gives
\[
s^2=\frac{1-12m}{16},\qquad d^2=\frac{1+4m}{16}. \tag{3}
\]
There are four distinct interior equilibria exactly for \(0<m<1/12\), comprising both independent signs in (3). They are saddles because the Jacobian determinant, after using (3), equals
\[
\det J=-32s^2d^2=-\frac{(1-12m)(1+4m)}8<0. \tag{4}
\]
At \(m=1/12\), all four family-B descriptions collapse pairwise onto the two family-A points. At \(m=1/8\), the two family-A points in turn collapse onto the symmetric midpoint. Counting distinct points proves the equilibrium totals, including both endpoints.

For completeness, the stability of the three symmetric points follows from local eigenvalues: \((0,0)\) and \((1,1)\) each have eigenvalues \(-1/2\) and \(-1/2-2m\); the midpoint has eigenvalues \(1/4\) and \(1/4-2m\), so it is unstable for every \(m>0\). At \(m=1/12\) the two family-A points have one negative and one zero eigenvalue. Let \(d_0=1/\sqrt{12}\), choose the positive branch, and denote \(d=d_0+h(s)\) on a local center manifold. The center-manifold invariance equation in (1) yields \(h(s)=-3s^2/(2d_0)+O(s^4)\), hence
\[
\dot s=8s^3+O(s^5). \tag{5}
\]
The cubic drift is away from \(s=0\) on both sides, so these nonhyperbolic equilibria are unstable; the negative-\(d_0\) branch has the same conclusion. Thus only the two homogeneous states attract for \(m\ge1/12\).

Finally the vector field is the negative gradient of
\[
E(x,y)=\tfrac14 x^2(1-x)^2+\tfrac14 y^2(1-y)^2+\tfrac m2(x-y)^2,
\]
with \(\dot E=-\dot x^2-\dot y^2\). Every orbit stays in the compact square, and the Lyapunov invariance principle places its omega limit in the finite equilibrium set proved above. Since a trajectory's omega limit is connected, it consists of a single equilibrium, proving convergence for every initial state in the square.

## Verification
The standalone `verification.py` symbolically checks (1), the family-A eigenvalues, the family-B determinant, the gradient identity, the leading repelling cubic coefficient in (5), and exact-rational sample equilibria on every open regime and at both thresholds. Executing `python verification.py` requires Python with SymPy. The exact algebraic proof above, not the finite parameter samples, establishes the parameter-uniform classification.

## Relationship to prior work
Kang and Lanchier introduced precisely this symmetric two-patch cubic Allee ODE with general threshold \(\theta\) and discussed the loss of the heterogeneous attractors; their Theorems 2.3 and 2.4 yield conditional high-dispersal exclusions and qualitative multiplicity but do not state the balanced-threshold split at \(1/12\) and \(1/8\), including the intervening asymmetric saddles and their explicit coordinates. Their sufficient bound for exclusion of nonsymmetric equilibria specializes to \(m>1/8\), while the explicit loss of local asymmetric attractors occurs already at \(m=1/12\). Thus the asserted advance is the *sharp specialized phase diagram*, not the established observation that dispersal destroys heterogeneous Allee attractors.

Gyllenberg, Hemminki and Tammaru had previously demonstrated conservation of spatially heterogeneous states in a symmetric two-patch Allee setting, but using a biparental-reproduction model. The 2023 study by Xia and colleagues treats different nonlinear-dispersal and asymmetric-patch models. General results about two coupled double-well gradient systems are a remaining priority-comparison risk.

## Limitations
The sharp constants rely on the balanced local threshold and symmetric linear coupling; they are not asserted for arbitrary \(\theta\), nonlinear dispersal, patch heterogeneity, demographic noise or spatially extended habitats. Linearized instability is combined with the center-manifold calculation at the nonhyperbolic threshold; the mathematical notion of an attracting density state is not proof of survival in finite populations. Historical priority remains conditional on broader two-site bistable-gradient literature and older full-text material that was not fully accessible.

## References
1. Kang, Y. and Lanchier, N., *Expansion or extinction: deterministic and stochastic two-patch models with Allee effects*, initial arXiv version `arXiv:1003.0121` (2010), https://arxiv.org/abs/1003.0121 .
2. Gyllenberg, M., Hemminki, J. and Tammaru, T., *Allee effects can both conserve and create spatial heterogeneity in population densities*, Theoretical Population Biology 56 (1999), 231–242, https://doi.org/10.1006/tpbi.1999.1430 .
3. Xia, Y., Chen, L., Srivastava, V. and Parshad, R., *Stability and bifurcation analysis of a two-patch model with Allee effect and dispersal* (2023), https://arxiv.org/abs/2310.10558 .
