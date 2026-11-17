# Exact chord-quadrilateral enclosure and elevenfold rigidity of the regular hendecagon

## Finding
Let \(P_{11}\) be the regular hendecagon whose vertices are \((\cos(2\pi j/11),\sin(2\pi j/11))\), for integers \(0\le j<11\). An admissible enclosure is a convex polygon containing \(P_{11}\), having at most four sides, each parallel to a chord joining two distinct vertices of \(P_{11}\). Its minimum possible area is
\[
q_{\mathrm{ch}}(P_{11})=\cos^2(\pi/11)\left(\tan(2\pi/11)+3\tan(3\pi/11)\right)
=3.7790306749908567\ldots.
\]
The ratio to \(\operatorname{area}(P_{11})=\frac{11}{2}\sin(2\pi/11)\) is \(1.2708927335446785\ldots\). Exactly eleven enclosures attain equality: their four outward supporting normals have index sets obtained by adding an even integer modulo \(22\) to \(\{1,5,11,17\}\). Every side of each winning quadrilateral contains an entire side of \(P_{11}\). The four circular normal gaps are \((4,6,6,6)\) units of \(\pi/11\), up to cyclic ordering.

Every other nonredundant *fully supporting* quadrilateral from the finite chord-normal family has area at least \(q_{\mathrm{ch}}(P_{11})+0.008\), a rational certified separation. This does not claim a positive area gap for general arbitrarily translated, nonsupporting enclosures approaching a minimizer.

## Assumptions and scope
A chord includes an edge. A containing quadrilateral is not assumed to be a parallelogram. Its sides may initially lie away from the input polygon, but translating each side inward to the first support line cannot increase area, so at a minimum all nonredundant sides are supporting. The problem also permits enclosing triangles; these are compared explicitly. The result concerns the restricted chord-direction problem, not the unrestricted minimum enclosing quadrilateral.

## Proof
Set \(\theta=\pi/11\), \(c=\cos\theta\), and \(n_k=(\cos(k\theta),\sin(k\theta))\), with indices \(k\) modulo \(22\). A chord joining vertices \(v_i,v_j\) is normal to \(v_i+v_j\), and its unoriented normal direction has angle \((i+j)\theta\) modulo \(\pi\). As distinct indices vary, every such angle occurs. The complete set of outward oriented chord normals is therefore \(n_0,\ldots,n_{21}\). Their support numbers are
\[
h_k=\max_{x\in P_{11}} n_k\cdot x=\begin{cases}1&k\text{ even},\\c&k\text{ odd}.\end{cases}
\]
For any cyclically ordered set of three or four distinct normals \(k_0<\dots<k_{m-1}\), boundedness of the intersection of their support half-planes is equivalent to every cyclic index gap \(g_i=(k_{i+1}-k_i)\bmod22\) being strictly less than \(11\). Here \(k_m=k_0+22\). The bounded intersection is a polygon of area
\[
A(k_0,\dots,k_{m-1})=\sum_{i=0}^{m-1}
\frac{h_{k_i}h_{k_{i+1}}-\tfrac12(h_{k_i}^2+h_{k_{i+1}}^2)\cos(g_i\theta)}{\sin(g_i\theta)}.
\]
This follows by intersecting consecutive supporting lines, computing tangent-coordinate displacements along each supporting side, and summing one-half its support distance times its signed side length. The formula holds for zero-length sides. An input side-support inequality can be redundant only if it touches \(P_{11}\) at a vertex simultaneously lying on two other selected supporting lines. This occurs precisely when an even index \(k\) is accompanied by both adjacent odd indices \(k-1,k+1\) modulo \(22\). Removing such a redundant inequality leaves a bounded three-support enclosure, which is treated in the triangle comparison.

The remaining optimization is finite and exhaustive. The included standard-Python checker constructs rigorous rational outward intervals for \(\pi\) using Machin's arctangent formula and alternating series, then for each \(\sin(j\theta)\), \(\cos(j\theta)\) using Taylor polynomials with explicit remainders. Its fixed-point scale is \(10^{28}\), and no floating-point comparison enters the certificate. It checks all \(3674\) bounded nonredundant four-normal sets and all \(330\) bounded three-normal sets; the other \(11\) bounded four-normal sets have one redundant vertex support. Exactly the eleven sets
\[
\left\{\operatorname{sort}\bigl((1,5,11,17)+2r\pmod{22}\bigr):0\le r<11\right\}
\]
meet the winning area interval. Every other nonredundant quadrilateral has a rigorously certified excess greater than \(0.008\); every triangle has strictly larger area as well. These exact inequalities establish the global minimum over all permitted enclosures.

For the winning four odd indices each support height equals \(c\). A summand in the area formula then reduces to \(c^2\tan(g_i\theta/2)\). Substituting gaps \((4,6,6,6)\) proves the stated exact minimum. Translation and positive-determinant or negative-determinant affine maps preserve the minimum-area ratio and the eleven-fold classification for affine-regular hendecagons, under the corresponding affine notion of chords.

## Verification
With standard Python 3, run `python chord11_checker.py`. The script reconstructs rational enclosures for trigonometric constants; enumerates all admissible triple and quadruple normal-index subsets; verifies boundedness and removes the eleven known redundant supports; checks all nonwinning candidates strictly above the exact winner interval; and asserts that all eleven winners form precisely the predicted rotational orbit. The checked strict interval separation exceeds \(0.008\) in unit-circumradius area. This finite computation proves the required finite inequalities; the reduction from arbitrary enclosures to the finite supporting-line family is the geometric component of the proof.

## Relationship to prior work
Vígh's work introduces chord-quadrilateral enclosure and gives a universal upper bound and several polygonal benchmarks, but not the exact regular-hendecagon result. Existing exact seven-gon and nine-gon calculations yield different instances of the same natural enclosure invariant. In particular, the seven-gon winner is edge-supported and the nine-gon winner needs one genuine diagonal direction; neither statement determines the eleven-gon optimum or its eleven equalities. The known all-order minimum-area enclosing *parallelogram* formula concerns a strict subclass of four-sided enclosures, and its odd-order value cannot imply our smaller, nonparallelogram optimum.

## Limitations
The certificate is exhaustive for chord-direction enclosures of the single regular eleven-gon, not a general all-order solution and not a proof of Kuperberg's broader conjecture. The discrete positive gap is between *fully supporting* normal configurations only, and is not a gap among all nearby admissible quadrilaterals. Older unindexed geometric-computation sources could contain an equivalent specialization; independent historical-priority review has not been performed.

## References
1. V. Vígh, *A note on Kuperberg's quadrilateral conjecture*, arXiv:2610.08168v1, first publicly posted October 6, 2026, https://arxiv.org/abs/2610.08168.
2. *Exact chord-quadrilateral enclosure of the regular heptagon*, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-exact-chord-quadrilateral-enclosure-of-the-regular-heptagon--8caa008cc219.
3. *Exact chord-quadrilateral enclosure of the regular nonagon and essential diagonal directions*, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-exact-chord-quadrilateral-enclosure-of-the-regular-nonagon-and-t--54cf1fb013d5.
4. *Exact minimum-area enclosing parallelograms for regular polygons*, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-minimum-area-enclosing-parallelograms-for-regular-polygons--827c68cd7bad.
