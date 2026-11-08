# Reentrant transverse stability on an antisymmetrically coupled logistic ray

## Finding
For the two-site, oppositely signed interaction slice of a coupled logistic map, the inherited logistic two-cycle is *reentrantly attracting* in the coupling strength. The exact loss/recovery boundary is a pair of transverse-flip curves meeting at one algebraic cusp. Three explicit parameter choices give a physically unsaturated attracting–saddle–attracting sequence even when the original map is clipped to the unit square.

Let \(r_0\in(3,1+\sqrt6)\) be the unique root of \(r^3-3r^2-4=0\). The transition begins exactly at \(r_0\), approximately \(3.3553013976\). For \(r_0<r<1+\sqrt6\), put
\[
d_\pm(r)=\frac{r(r+1)\pm\sqrt{(r+1)(r^3-3r^2-4)}}{r^2+1}.
\]
The two-cycle is a hyperbolic attracting cycle when \(1+\varepsilon^2<d_-(r)\) or \(1+\varepsilon^2>d_+(r)\), and a hyperbolic saddle cycle between these values. In particular, these boundaries concern *transverse* stability; the logistic return multiplier stays strictly inside the unit disk in the stated growth-rate interval.

## Assumptions and scope
Fix \(r>0\) and \(0<\varepsilon<1\). Define the polynomial map
\[
F_{r,\varepsilon}(x,y)=\bigl(r x(1-x+\varepsilon y),\;r y(1-y-\varepsilon x)\bigr).
\]
It is a deterministic two-site realization of the interaction form in Baron and Galla [1], with zero diagonal interaction and off-diagonal coefficients \(a_{12}=\varepsilon\), \(a_{21}=-\varepsilon\). It is *not* a generic sample of their independent random-interaction ensemble. Their physical map applies the componentwise clipping \(H(u)=0\) for \(u\leq0\), \(H(u)=u\) for \(0\leq u\leq1\), and \(H(u)=1\) for \(u\geq1\). Results for that clipped map are explicitly restricted below to two-cycles strictly inside the unit square, where clipping is inactive in a neighborhood of the cycle.

Write \(d=1+\varepsilon^2\), and introduce linear coordinates
\[
t=\frac{d}{1+\varepsilon}x,\qquad z=y-\frac{1-\varepsilon}{1+\varepsilon}x.
\]
An invariant ray is the positive portion of \(z=0\); on it \(x=(1+\varepsilon)t/d\), \(y=(1-\varepsilon)t/d\). For each \(3<r<1+\sqrt6\), define
\[
t_\pm=\frac{r+1\pm\sqrt{(r-3)(r+1)}}{2r},\qquad
P_\pm=\left(\frac{1+\varepsilon}{d}t_\pm,\frac{1-\varepsilon}{d}t_\pm\right).
\]
These are distinct positive points of least period two for the polynomial map, and for the clipped map whenever \((1+\varepsilon)t_+/d<1\). No assertions are made about other coexisting orbits.

## Proof
**Exact invariant-ray reduction.** Direct substitution gives the following *full two-dimensional* coordinate expression, not merely a linearization:
\[
t'=r t(1-t+\varepsilon z),\qquad
z'=r z\left(1-\frac{2t}{d}-z\right).
\]
Thus \(z=0\) is invariant, and the restricted map is \(g_r(t)=rt(1-t)\). Its primitive period-two points for \(r>3\) are the displayed \(t_\pm\), with
\[
t_++t_-=(r+1)/r,\qquad t_+t_-=(r+1)/r^2.
\]
For \(3<r<1+\sqrt6\), both belong to \((0,1)\).

**Exact Floquet spectrum.** In these fixed linear coordinates the one-step Jacobian at \((t,0)\) is triangular:
\[
\begin{pmatrix}r(1-2t)&r\varepsilon t\\0&r(1-2t/d)\end{pmatrix}.
\]
Consequently the two-step return Jacobian at either cycle point has eigenvalues
\[
\Lambda_\parallel=r^2(1-2t_+)(1-2t_-)=-r^2+2r+4,
\]
\[
\Lambda_\perp=r^2(1-2t_+/d)(1-2t_-/d)
=r^2-\frac{2r(r+1)}d+\frac{4(r+1)}{d^2}.
\]
The first is strictly between \(-1\) and \(1\) for \(3<r<1+\sqrt6\).

**Sharp reentrance.** For fixed \(3<r<1+\sqrt6\), consider the transverse multiplier as a function of \(1<d<2\). Differentiation gives
\[
\frac{\partial\Lambda_\perp}{\partial d}
=\frac{2(r+1)(rd-4)}{d^3}.
\]
Its unique minimum occurs at \(d=4/r\in(1,2)\) and equals \(r^2(3-r)/4\). Moreover \(\Lambda_\perp(1)=\Lambda_\parallel<1\) and \(\Lambda_\perp(2)=1\); hence \(\Lambda_\perp(d)<1\) throughout the open interval. The minimum is \(-1\) exactly when \(r^3-3r^2-4=0\). This cubic increases strictly for \(r>3\), is negative at \(r=3\), and positive at \(r=1+\sqrt6\), so the required root \(r_0\) exists and is unique.

To locate the crossings, multiply \(\Lambda_\perp+1\) by \(d^2>0\):
\[
Q_r(d)=(r^2+1)d^2-2r(r+1)d+4(r+1).
\]
Its discriminant is \(4(r+1)(r^3-3r^2-4)\). For \(r_0<r<1+\sqrt6\), the minimum is negative, whereas \(Q_r(1)>0\) and \(Q_r(2)>0\). Since the minimizer lies in \((1,2)\), both roots are strictly inside \((1,2)\), and they are exactly \(d_\pm(r)\). The transverse multiplier is less than \(-1\) strictly between these roots and lies in \((-1,1)\) outside. Together with the longitudinal multiplier this gives the claimed sink–saddle–sink partition. At the root curves the return multiplier \(-1\) makes the cycle nonhyperbolic; no nonlinear classification is asserted there. At \(r=r_0\), the two crossings coalesce into one nonhyperbolic tangency.

**Exact unsaturated examples.** Put \(r=17/5\). Then
\[
t_\pm=\frac{11\pm\sqrt{11}}{17},\qquad
\Lambda_\parallel=-\frac{19}{25}.
\]
At \(\varepsilon=1/10,1/4,3/5\), respectively, the transverse multipliers are
\[
-\frac{206711}{255025},\quad -\frac{1459}{1445},\quad -\frac{6679}{7225}.
\]
The first and third are in \((-1,1)\), while the middle is strictly below \(-1\), so the corresponding cycles are a sink, saddle, and sink. All six population coordinates lie strictly in \((0,1)\). Indeed \(0<t_-<t_+\), \(0<1-\varepsilon<1+\varepsilon\), and for these three couplings
\[
\frac{1+\varepsilon}{1+\varepsilon^2}\leq\frac{20}{17},
\quad\frac{20}{17}t_+=\frac{20(11+\sqrt{11})}{289}<\frac{860}{867}<1,
\]
where the strict inequality uses \(\sqrt{11}<10/3\). Clipping therefore changes neither the cycle nor its local linear type.

## Verification
The accompanying `verify.py` checks the exact coordinate transformation, the two multiplier formulas, the discriminant and minimizer identities, and the three rational witness multipliers with exact symbolic arithmetic. It also checks the strict clipping margin by exact inequalities and tests the map action directly at the six witness points. Run `python verify.py` in an environment with Python 3 and SymPy; successful completion prints `VERIFY_OK`. These checks corroborate the displayed algebra. The infinite-parameter theorem follows from the written proof, not from finite numerical sampling.

## Relationship to prior work
Baron and Galla [1] introduced the many-component disordered logistic map with clipping and investigated its disorder-averaged fixed-point stability and large-population transitions. Our result concerns a structured, deterministic two-site antisymmetric interaction: its embedded scalar logistic dynamics, transverse two-cycle cusp and reentrant stability do not follow from a large-system spectral analysis. The textbook logistic two-cycle already supplies the longitudinal points and multiplier; the *transverse* stability law is the additional assertion. Mareno and English [2] analyzed fixed-point flip and Neimark–Sacker bifurcations for a different two-parameter coupled-logistic model. Their fixed-point classification does not imply the present two-cycle multiplier and algebraic saddle window. The precise statements were compared with related public findings about other coupled maps, replicator maps and Duffing maps; no equivalent or stronger covering statement was located. This is a best-evidence originality comparison, not a definitive assertion of historical priority.

## Limitations
The interaction matrix is a special antisymmetric two-site matrix, not a typical random matrix; the result says nothing about the thermodynamic limit or generic disorder. For the clipped map, the full open stability diagram applies only at cycle points strictly inside the unsaturated unit square; the three explicit examples meet this requirement. Some intermediate couplings in the polynomial stability diagram may place a point outside that square and are therefore not automatically physical orbits of the clipped map. The theorem classifies only the stated invariant-ray prime-two cycle, not all periodic points, global basins or chaotic attractors. At the transverse \(-1\) curves and at the longitudinal endpoint, nonlinear stability is left open. Independent scientific validation and exhaustive historical priority checks have not been performed.

## References
[1] J. W. Baron and T. Galla, *The disordered logistic map*, arXiv:2609.24402v1, first submitted 2026-09-21; https://arxiv.org/html/2609.24402 . Relevant material: original equation (1), its clipping convention and the fixed-point stability and large-population sections and supplementary material.

[2] A. Mareno and L. Q. English, *Flip and Neimark–Sacker Bifurcations in a Coupled Logistic Map System*, Discrete Dynamics in Nature and Society (2020), article 4103606; https://doi.org/10.1155/2020/4103606 .
