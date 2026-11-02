# Exact stationary height parabola and slab-crossing law for the Yang–Chen flow
## Finding
For the Yang–Chen flow \(\dot x=a(y-x)\), \(\dot y=x(c-z)\), \(\dot z=xy-bz\) with \(a,b,c>0\), every compactly supported invariant probability measure \(\mu\) satisfies \(\int x^2\,d\mu=b\bar z\), \(\int z^2\,d\mu=c\bar z\), and \(\operatorname{Var}_\mu(z)=\bar z(c-\bar z)\), where \(\bar z=\int z\,d\mu\). Thus \(0\le\bar z\le c\); the lower endpoint is only the origin measure and the upper endpoint is supported on the two outer equilibria. Consequently every non-equilibrium ergodic compact invariant measure has \(0<\bar z<c\), \(\int x^2\,d\mu<bc\), positive height variance, and positive mass both in \(0<z<c\) and in \(z<0\) or \(z>c\). In particular, any nonconstant periodic orbit with \(z(t)>0\) for all \(t\) visits both \(0<z<c\) and \(z>c\).

At the source parameter set \(a=35\), \(b=3\), \(c=35\), every non-equilibrium ergodic compact recurrent state therefore has \(0<\bar z<35\), \(\int x^2\,d\mu=3\bar z<105\), and \(\operatorname{{Var}}_\mu(z)=\bar z(35-\bar z)\). At \(a=10\), \(b=8/3\), \(c=16\), the corresponding bound is \(\int x^2\,d\mu<128/3\).

## Assumptions and scope
The system is
\[
\dot x=a(y-x),\qquad \dot y=x(c-z),\qquad \dot z=xy-bz,
\]
with \(a,b,c>0\). The measure \(\mu\) is a Borel probability measure invariant under the flow and supported on a compact invariant set. Compact support ensures that all polynomial observables used below and their Lie derivatives are integrable. No hyperbolicity, physical-measure property, or numerical approximation is assumed.

The source article studies this same Yang–Chen system, including its dynamics at infinity, Jacobi stability, periodic behavior, and chaotic parameter regimes. Its listed primary classifications are 34D20 and 34D45.

## Proof
For every continuously differentiable observable \(f\), invariance on compact support gives \(\int L_F f\,d\mu=0\), where \(L_F\) is the Lie derivative along the vector field. Apply this to four elementary observables.

First,
\[
L_F\!\left(\frac{x^2}{2}\right)=a(xy-x^2),
\]
so \(\int xy\,d\mu=\int x^2\,d\mu\). Second,
\[
L_F z=xy-bz,
\]
so, with \(\bar z=\int z\,d\mu\),
\[
\int x^2\,d\mu=\int xy\,d\mu=b\bar z.
\]
Third,
\[
L_F\!\left(\frac{y^2}{2}\right)=cxy-xyz,
\]
and fourth,
\[
L_F\!\left(\frac{z^2}{2}\right)=xyz-bz^2.
\]
Their invariant averages give \(c\int xy\,d\mu=\int xyz\,d\mu=b\int z^2\,d\mu\). Using \(\int xy\,d\mu=b\bar z\) and \(b>0\),
\[
\int z^2\,d\mu=c\bar z.
\]
Therefore
\[
\operatorname{{Var}}_\mu(z)=\int z^2\,d\mu-\bar z^2=\bar z(c-\bar z).
\]
Nonnegativity of variance and \(c>0\) imply \(0\le\bar z\le c\).

If \(\bar z=0\), then both \(\int z^2\,d\mu=0\) and \(\int x^2\,d\mu=0\), so the support lies in \(x=z=0\). The only invariant subset there is the origin, because \(\dot x=ay\); hence \(\mu\) is the origin Dirac measure.

If \(\bar z=c\), zero variance gives \(z=c\) on the support. Invariance of that plane along the support requires \(xy=bc\). Since \(\dot y=x(c-z)=0\), \(y\) is constant along each supported orbit. Because \(bc>0\), the constraint \(xy=bc\) forces \(x\) to be constant as well; then \(\dot x=a(y-x)=0\), so \(x=y\) and \(x^2=bc\). Thus the support is contained in the two equilibria \((\pm\sqrt{{bc}},\pm\sqrt{{bc}},c)\).

Finally,
\[
\int z(z-c)\,d\mu=0.
\]
The maximal invariant subset of \(z(z-c)=0\) consists only of the three equilibria just described. Hence a non-equilibrium ergodic invariant measure cannot have \(z(z-c)=0\) almost surely. Since its mean is zero, the observable \(z(z-c)\) must take both signs on sets of positive measure. The negative region is exactly \(0<z<c\); the positive region is exactly \(z<0\) or \(z>c\). If a periodic orbit has \(z(t)>0\) throughout, continuity then forces visits on both sides of \(z=c\).

## Verification
The accompanying script `verify_yang_chen.py` symbolically reconstructs the four Lie derivatives, eliminates the stationary moments, verifies the variance factorization, and checks the equilibrium algebra. Executed from the packaged source path, it returns `VERIFY_OK`.

The argument itself is exact. It uses no finite-time sampling, no Lyapunov-exponent estimate, and no numerical inference about an attractor.

## Relationship to prior work
Liu, Huang, and Wei analyze the same Yang–Chen equations through Poincaré compactification and Kosambi–Cartan–Chern/Jacobi stability. Their full text identifies the three finite equilibria and discusses periodic and chaotic dynamics, but the inspected material does not state the stationary moment identities above. The original Yang–Chen article emphasizes equilibria, bifurcations, periodic windows, and chaotic parameter regions. Liao and collaborators later establish Lagrange/Lyapunov stability and global attracting-set results. Those results motivate compact recurrence but do not, in the inspected material, supply this invariant-measure parabola or its slab-crossing consequence.

Database searches for Yang–Chen stationary moments, mean-square balances, invariant measures, and the factor \(z(z-c)\) returned related balance laws for other dynamical systems but no same-system statement implying this claim. A particularly close structural analogue is a stationary variance parabola for a different four-dimensional Aziz–Merie flow; it has different equations and does not imply the Yang–Chen identity.

## Limitations
The result constrains compact invariant statistics; it does not prove existence, uniqueness, ergodicity, physicality, or stability of a chaotic attractor or periodic orbit. The claim does not identify whether a general recurrent state escapes the slab through \(z<0\), through \(z>c\), or both. A full-text inspection of the 2017 Lagrange-stability paper and of every older citation was not available in this run, so an unindexed equivalent formulation in older literature remains a residual bibliographic risk. No such equivalent was found in the targeted searches, the original-paper material inspected, or the full text of the 2020 source article inspected here.

## References
1. Y. Liu, Q. Huang, and Z. Wei, “Dynamics at infinity and Jacobi stability of trajectories for the Yang-Chen system,” Discrete and Continuous Dynamical Systems - B 26 (2021), 3357–3380. DOI: 10.3934/dcdsb.2020235. Early access: 2020-08-03.
2. Q. Yang and G. Chen, “A chaotic system with one saddle and two stable node-foci,” International Journal of Bifurcation and Chaos 18 (2008), 1393–1414. DOI: 10.1142/S0218127408021063.
3. X. Liao, G. Zhou, Q. Yang, Y. Fu, and G. Chen, “Constructive proof of Lagrange stability and sufficient–necessary conditions of Lyapunov stability for Yang–Chen chaotic system,” Applied Mathematics and Computation 309 (2017), 205–221. DOI: 10.1016/j.amc.2017.03.033.
