# Equidihedral minimax and volume–angle separation in regular antiprisms

## Finding
For every integer \(n\ge3\), consider the right regular \(n\)-gonal antiprism with equal circumradii \(r>0\), parallel bases separated by \(h>0\), and relative half-step twist \(\pi/n\). All dihedral angles below are **interior**, between the supporting facet halfspaces; let \(\Phi_n(h/r)\) be their maximum. Define \(\theta=\pi/n\), \(c=\cos\theta\), and \(q=1-c\). Then the unique minimizer, up to similarity, is
\[
 t_{\mathrm E}:=\frac{h}{r}=\frac{q\sqrt{1+2c}}{c},\qquad
 \min_{t>0}\Phi_n(t)=\arccos\!\left(-\frac{c}{1+c}\right).
\]
At this and only this aspect ratio, **all \(4n\) edges have the same dihedral angle**. The optimum increases strictly with \(n\) from \(\arccos(-1/3)\) at \(n=3\) to the unattained limiting value \(2\pi/3\).

There are two other natural intrinsic aspect ratios: the unique uniform, all-edges-equal realization has \(t_{\mathrm U}=\sqrt{2q(1+2c)}\), and the unique volume maximizer under a fixed circumsphere radius has \(t_{\mathrm V}=\sqrt2\). At \(n=3\) all three coincide at the regular octahedron, whereas for **every \(n\ge4\)**
\[
 0<t_{\mathrm E}<t_{\mathrm U}<t_{\mathrm V},\qquad
 \Phi_n(t_{\mathrm E})<\Phi_n(t_{\mathrm U})<\Phi_n(t_{\mathrm V}).
\]
The latter two largest angles have the exact forms
\[
\Phi_n(t_{\mathrm U})=\arccos\!\left(\frac{1-4c}{3}\right),\qquad
\Phi_n(t_{\mathrm V})=\arccos\!\left(\frac{q^2-2c}{2+q^2}\right).
\]
The three heights split into different asymptotic scales:
\[
t_{\mathrm E}\sim\frac{\sqrt3\pi^2}{2n^2},\qquad
 t_{\mathrm U}\sim\frac{\sqrt3\pi}{n},\qquad t_{\mathrm V}=\sqrt2,
\]
and the largest interior dihedral angles at both the uniform and volume-maximizing realizations approach \(\pi\), while the minimax one approaches \(2\pi/3\). More precisely, \(\Phi_n(t_{\mathrm U})=\pi-2\pi/(\sqrt3 n)+O(n^{-3})\) and \(\Phi_n(t_{\mathrm V})=\pi-\pi/n+O(n^{-3})\). Thus the limiting angular penalty for either conventional realization is \(\pi/3\).

## Assumptions and scope
The family consists of exactly two congruent regular \(n\)-gons with positive radius in distinct parallel planes, separated by a positive height and twisted by exactly \(\pi/n\). No face-edge equality is assumed when defining the family. The convex hull is a full-dimensional antiprism with exactly two polygonal bases, \(2n\) triangular lateral faces, and \(4n\) edges. Similarities preserve all angles and the ratio \(t=h/r\). In the volume assertion the **common circumsphere radius** is fixed, not the polygon radius or the surface area. No claim is made about arbitrary prismatoids, nonregular polygons, or unconstrained convex polyhedra.

## Proof
1. Scale \(r=1\) and center the two bases at heights \(\pm t/2\). Put \(T_k=(\cos(2k\theta),\sin(2k\theta),t/2)\) and \(B_k=(\cos((2k+1)\theta),\sin((2k+1)\theta),-t/2)\) with indices modulo \(n\). Lateral facets are \(T_kT_{k+1}B_k\) and \(B_kB_{k+1}T_{k+1}\). Their outward normals can be chosen, up to rotation, as \((t,0,q)\) and \((tc, t\sin\theta,-q)\); the polygonal base normals are \(\pm e_3\). Direct substitution shows each of the displayed lateral planes supports all \(2n\) vertices and is nondegenerate when \(t>0\); the rotational copies list all boundary facets.

2. The two types of *exterior* adjacent-normal angles are
\[
 \alpha(t)=\arccos\!\left(\frac q{\sqrt{t^2+q^2}}\right),\qquad
 \beta(t)=\arccos\!\left(\frac{ct^2-q^2}{t^2+q^2}\right).
\]
There are \(2n\) base-to-triangle edges of interior dihedral \(\pi-\alpha(t)\) and \(2n\) triangle-to-triangle edges of interior dihedral \(\pi-\beta(t)\), so \(\Phi_n(t)=\pi-\min\{\alpha(t),\beta(t)\}\).

3. For \(t>0\), \(\alpha(t)\) increases strictly from \(0\) to \(\pi/2\). The fraction inside \(\beta(t)\) has strictly positive derivative with respect to \(t^2\), since \(c+1>0\), so \(\beta(t)\) decreases strictly from \(\pi\) to \(\theta\). Consequently the minimum of the two is uniquely maximized where \(\alpha=\beta\). Write \(s=\sqrt{1+t^2/q^2}>1\). Equality of cosines gives \(s=c(s^2-1)-1\), equivalent to \((s+1)(cs-(c+1))=0\). Thus \(s=(1+c)/c\), whence \(t=q\sqrt{1+2c}/c\) and \(\cos\alpha=c/(1+c)\). This proves the exact minimax value, uniqueness, and equality of **all** interior dihedrals. Since \(n\mapsto c\) increases strictly from \(1/2\) to \(1\), the optimal angle increases strictly from \(\arccos(-1/3)\) to \(2\pi/3\).

4. Each polygonal base edge has length \(2r\sin\theta\); every slanted edge has length \(r\sqrt{2q+t^2}\). Equality of all edges is therefore equivalent to \(t^2=4\sin^2\theta-2q=2q(1+2c)\). The polyhedron has volume
\[
 V_n(r,h)=\frac{nr^2h}{3}\bigl(\sin(2\theta)+\sin\theta\bigr).
\]
One derivation is to sum the facet-area times positive origin-to-plane distance divided by three: both bases contribute a total \(nr^2h\sin(2\theta)/2\), and the \(2n\) lateral triangles contribute \(nr^2h\sin\theta(1+c)\). For circumsphere radius \(\mathcal R\), one has \(r^2+h^2/4=\mathcal R^2\), hence volume is a positive constant times \(h(\mathcal R^2-h^2/4)\) on \(0<h<2\mathcal R\). Its unique maximum is at \(h=2\mathcal R/\sqrt3\), equivalently \(t=\sqrt2\).

5. The squared ratios satisfy \(t_{\mathrm E}^2/t_{\mathrm U}^2=q/(2c^2)\) and \(t_{\mathrm U}^2/t_{\mathrm V}^2=q(1+2c)\). Both are strictly less than one exactly when \(c>1/2\), i.e. \(n\ge4\); at \(n=3\) both equal one. Above the equidihedral optimum, \(\beta\) is the active, strictly decreasing exterior angle; therefore \(\Phi_n\) strictly increases along the ordered heights. Substituting the two squared heights into the cosine for \(\beta\) simplifies to \((4c-1)/3\) and \((2c-q^2)/(2+q^2)\), respectively. Since interior angle is \(\pi-\beta\), this proves the exact comparison formulas.

6. Use \(c=1-\theta^2/2+O(\theta^4)\) and \(q=\theta^2/2+O(\theta^4)\) in the three heights and cosine expressions. Elementary inverse-cosine expansion gives the stated angle and height asymptotics, including the exact limiting gap \(\pi/3\).

## Verification
The standalone standard-library script `verify_antiprism.py` constructs every vertex and triangular supporting facet directly for orders \(3\) through \(30\), checks outward support and all facet incidences, and compares directly computed adjacent-normal dihedrals with the analytic expressions. It computes volume independently from oriented origin-pyramids over the base and lateral facets, and verifies the optimizer algebra and inequalities at numerous heights. It passed **261044** finite assertions in the execution recorded here. These floating-point tests corroborate the algebra; they do not prove the claims for all integers or arbitrary real parameters. The proof above is analytical.

## Relationship to prior work
Li, Wang, and Yu (2026) establish a general small-dihedral-angle construction with maximum interior dihedral approaching \(\pi/2\); their six-page manuscript does not study regular antiprisms or their constrained exact minimax. Classical accounts give the geometry and volume of edge-uniform antiprisms. Rajpoot (2023) treats dihedral formulas for the edge-uniform realization, not optimization across all positive heights. The theorem here characterizes the unique **equidihedral** minimax shape and proves it is, for every order above three, different from both the edge-uniform and spherical-volume-optimal shapes. The limit \(2\pi/3\) is specific to this one-parameter family; it is not a general dihedral threshold for all convex polyhedra.

## Limitations
Originality is evaluated against the indexed mathematics records and accessible primary sources listed below, not against an exhaustive historical bibliography. The exact height optimization is elementary once both lateral normal orbits are identified; its mathematical point is the complete extremal classification and asymptotically nonvanishing difference between the three natural shape selectors, not a new general convexity method. The numerical verifier requires no third-party packages and supplies no formal proof of the continuum-wide optimization. Non-half-step twists and asymmetric antiprisms are outside scope.

## References
- Z. Li, J. Wang and J. Yu, *Infinitely many convex polytopes with dihedral angles bounded above by \(\pi/2+\delta\)*, arXiv:2611.09021v1, first public 2026-11-06, https://arxiv.org/abs/2611.09021 .
- H. C. Rajpoot, *Mathematical analysis of regular n-gonal right antiprism*, dated 2023-05-23, publicly accessible excerpt https://www.studocu.com/in/document/indian-institute-of-technology-bombay/discrete-structures/regular-polygonal-right-antiprism/59995040 .
- G. P. Michon, *Polyhedra & Polytopes*, section “Regular Antiprism”, https://www.numericana.com/answer/polyhedra.htm (accessed 2026-11-09).
- R. Díaz and J. L. Estévez, *Hyperbolic homology 3-spheres from drum polyhedra*, Algebraic & Geometric Topology 24 (2024), 3543–3570, https://doi.org/10.2140/agt.2024.24.3543 (hyperbolic setting, not the Euclidean optimization studied here).
