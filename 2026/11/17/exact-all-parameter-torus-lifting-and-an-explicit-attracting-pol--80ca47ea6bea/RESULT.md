# Exact all-parameter torus lifting and an explicit attracting polynomial basin

## Finding

Consider the three-dimensional construction
\[
\dot x=-y,\qquad \dot y=x+\varepsilon yP(x^2+y^2,z),\qquad \dot z=2\varepsilon y^2Q(x^2+y^2,z).
\]
For every planar hyperbolic limit cycle \(\Gamma\) of \(\dot u=P(u,z),\ \dot z=Q(u,z)\) lying entirely in \(u>0\), the surface
\[
\mathcal T_\Gamma=\{(x,y,z):(x^2+y^2,z)\in\Gamma\}
\]
is a **fixed, smooth, isolated invariant torus for every \(\varepsilon\ne0\)**. Its location is exactly independent of \(\varepsilon\). If \(\Gamma\) is attracting in the planar system, the torus is locally exponentially attracting for every \(\varepsilon>0\), and locally repelling for every \(\varepsilon<0\); these stability orientations reverse when \(\Gamma\) is planar-repelling. No smallness assumption on \(|\varepsilon|\) is needed. Normal hyperbolicity, uniformity as \(|\varepsilon|\to\infty\), or structural persistence under changes to the vector field are **not** asserted.

A concrete polynomial example has an explicit open attracting region for every \(\varepsilon>0\): put \(u=x^2+y^2\), \(w=u-2\), \(R=w^2+z^2\), and
\[
P(u,z)=-z+w(1-R),\qquad Q(u,z)=w+z(1-R).
\]
Its invariant torus \(R=1\) attracts every initial condition in \(0<R<4\), with exponential decay toward the torus. The region is a proven subset of its basin, not a claimed maximal basin.

## Assumptions and scope

Throughout the general statement \(P,Q\in C^2\) on an open neighborhood of \(\Gamma\), and the planar cycle \(\Gamma\subset\{(u,z):u>0\}\) is a nonstationary, hyperbolic, simple closed orbit. The three-dimensional vector field is considered on a neighborhood of the compact lift; it need not be globally complete away from that neighborhood. A torus is *isolated* in the precise sense of being the maximal invariant set in a sufficiently thin compact toroidal neighborhood. Local exponential attraction and repulsion refer to distance from the torus in original physical time, at each fixed nonzero value of \(\varepsilon\).

## Proof

**Exact projection identity.** Let \(\pi(x,y,z)=(u,z)=(x^2+y^2,z)\). Direct differentiation without approximation gives
\[
\dot u=2x(-y)+2y\bigl(x+\varepsilon yP(u,z)\bigr)=2\varepsilon y^2P(u,z),\qquad
\dot z=2\varepsilon y^2Q(u,z).
\]
Thus every lifted trajectory projects to an oriented orbit of the planar system under the absolutely continuous clock
\[
s(t)-s(t_0)=2\varepsilon\int_{t_0}^{t}y(\tau)^2\,d\tau.
\]
When \(\varepsilon<0\) the planar orientation reverses. Zeroes of \(y\) do not invalidate the identity or create a new planar orbit.

**Why the clock never stops asymptotically on a compact positive-radius set.** Let \(K\) be compact in the physical phase space with \(u\ge c>0\), and suppose a full trajectory stays inside \(K\) during a unit interval. By uniqueness of solutions, if \(\int_t^{t+1}y(\tau)^2d\tau=0\), then \(y\) vanishes identically on that interval; the equations force \(x\equiv0\), contrary to \(u>0\). Continuity of initial-data dependence and compactness of the set of states whose complete unit-length trajectories remain in \(K\) give a common constant \(\delta_K>0\) for this integral. Applying the same argument to reversed unit intervals gives a corresponding positive lower bound. Therefore, along every full trajectory confined to a compact positive-radius set, \(|s(t)|\to\infty\) at least linearly as \(|t|\to\infty\). For trajectories confined only forward in such a set, the same positive lower bound applies for positive times. This argument is valid for each fixed \(\varepsilon\ne0\); its constants may depend on \(\varepsilon\).

**Exact torus and isolation.** Since \(\Gamma\) stays in \(u>0\), \(\pi^{-1}(\Gamma)\cong\Gamma\times S^1\) is a regular embedded compact torus. The projection identity makes it invariant; no flow solution on it can escape. A planar hyperbolic periodic orbit has a small compact annular isolating neighborhood \(N\subset\{u>0\}\) with \(\operatorname{Inv}(N)=\Gamma\). A three-dimensional orbit entirely confined in \(\pi^{-1}(N)\) projects, under the nonstalling clock just proved, to a complete planar orbit confined in \(N\), hence must project to \(\Gamma\). Thus \(\operatorname{Inv}(\pi^{-1}(N))=\pi^{-1}(\Gamma)\), establishing isolation for every nonzero \(\varepsilon\).

**Local stability.** If \(\Gamma\) is planar attracting, choose a forward-invariant compact annular neighborhood of \(\Gamma\) on which the planar normal distance decays as \(C e^{-\lambda s}\) for positive planar time \(s\); this follows from the nonunit Floquet multiplier. For \(\varepsilon>0\), the lift of that neighborhood is forward invariant, and the clock estimate gives \(s(t)\ge c_\varepsilon t-C_0\); consequently the distance of the lifted trajectory to \(\mathcal T_\Gamma\) decays exponentially in physical time. The projection is a smooth submersion there, so planar transverse distance and lifted distance are locally comparable. The opposite sign of \(\varepsilon\) reverses the direction of planar time; the repelling cases follow by time reversal. No assertion about quantitative rates uniform in \(\varepsilon\) is required.

**An explicit polynomial attracting region.** With \(w=u-2\) and \(R=w^2+z^2\), calculate exactly
\[
\frac{dR}{ds}=2wP+2zQ=2R(1-R),\qquad
\frac{dR}{dt}=4\varepsilon y^2R(1-R).
\]
The planar level \(R=1\) is a hyperbolic attracting cycle with angular speed one and planar transverse Floquet multiplier \(e^{-4\pi}\). Its lift is a torus as \(1\le u\le3\). If \(0<R(0)<4\) and \(\varepsilon>0\), the logistic sign rule keeps \(R(t)\) between \(R(0)\) and \(1\). Hence \(u(t)=2+w(t)\ge2-\sqrt{\max\{R(0),1\}}>0\), while \((x,y,z)\) stays bounded. This excludes finite-time blowup, supplies the compact positive-radius trapping set, and forces \(s(t)\to+\infty\), whence \(R(t)\to1\) exponentially in physical time. The zero-radius level \(R=0\) is the distinct rotating core \(u=2,z=0\), so it is correctly excluded from the asserted attraction region.

## Verification

A standalone symbolic identity checker (`checker.py`, Python with SymPy) checks the projection formula in the displayed example, the logistic identity and the planar radial factorization. It prints `EXACT_TORUS_LIFT_IDENTITIES_OK`. The nonstalling clock, isolation, stability, and general all-parameter quantifiers are mathematical arguments above, not conclusions inferred from a finite computation. The symbolic checks were replayed successfully from the prepared file.

## Relationship to prior work

Novaes and Pereira, *A version of Hilbert's 16th Problem for 3D polynomial vector fields: Counting isolated invariant tori* (arXiv:2212.12006, first posted 2022-12-22), introduce exactly the vector field above as Theorem A, Equation (4). They prove existence of normally hyperbolic invariant tori for sufficiently small positive \(\varepsilon\) by averaging, and show convergence to toroidal limits. Their full publicly available preprint (Theorem A and Section 3.2) does **not** state the exact all-nonzero-parameter invariant lift, a parameter-independent surface equation, a compact isolating-set proof, or the explicit all-positive-parameter attracting region above. The newer Arakaki–Novaes–Pereira article on varying torus counts by time reparametrization studies scalar rescalings and Hopf-zero bifurcations, not the present exact projection identity for the degenerate factor \(2\varepsilon y^2\). The current theorem strengthens the parameter range and gives geometric and basin conclusions; it does not claim to improve the prior small-parameter normal-hyperbolicity theorem.

## Limitations

The positive-radius hypothesis is indispensable for the compact nonstalling argument. No theorem is asserted for planar cycles touching \(u=0\), arbitrary invariant compact planar sets, all orbits outside the explicit attraction region, or robustness under perturbations of the constructed three-dimensional vector field. The theorem does not establish normal hyperbolicity at arbitrarily large \(|\varepsilon|\), nor independence from results that may appear in inaccessible revisions or unindexed literature. The explicit attraction region \(0<R<4\) is not claimed maximal.

## References

- D. D. Novaes and P. C. C. R. Pereira, *A version of Hilbert's 16th Problem for 3D polynomial vector fields: Counting isolated invariant tori*, arXiv:2212.12006 (first submitted 2022-12-22), https://arxiv.org/abs/2212.12006; later journal DOI 10.1002/mana.202300568.
- T. Arakaki, D. D. Novaes and P. C. C. R. Pereira, *Variation in the Number of Normally Hyperbolic Limit Tori in 3D Polynomial Vector Fields via Time Reparametrization and Hopf-Zero Bifurcation*, DOI 10.1007/s00030-026-01220-4 (2026), https://link.springer.com/article/10.1007/s00030-026-01220-4.
