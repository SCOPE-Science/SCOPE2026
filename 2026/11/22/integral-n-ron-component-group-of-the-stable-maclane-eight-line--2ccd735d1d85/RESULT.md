# Integral Néron component group of the stable MacLane eight-line boundary

## Finding

For either complex MacLane eight-line arrangement, blow up **only** its eight ordinary triple points in the ambient plane. Let \(B\) be the **reduced** union of all eight strict-transform lines and all eight exceptional curves. The resulting connected nodal curve has arithmetic genus \(13\), and the critical group of its dual graph is

\[
K(\Gamma_B)\cong \mathbb Z/2\mathbb Z\oplus\mathbb Z/6\mathbb Z\oplus(\mathbb Z/12\mathbb Z)^2\oplus(\mathbb Z/48\mathbb Z)^2.
\]

Its order is \(2^{14}3^5=3{,}981{,}312\), and its exponent is \(48\). By Raynaud's component-group theorem, this is the Néron component group of the Jacobian of any regular semistable smoothing of \(B\) over \(\mathbb C[[t]]\) with unit node thicknesses. The two conjugate realizations of the MacLane incidence have the same group.

## Assumptions and scope

Work in characteristic zero over \(\mathbb C\). The MacLane incidence is dual to the eight nonzero points \(P=\mathbb F_3^2\setminus\{(0,0)\}\). The eight affine lines in \(\mathbb F_3^2\) not through the origin each contain three points of \(P\) and correspond to the eight ordinary triple points of the plane line arrangement. The four affine lines through the origin contain two points of \(P\) each and correspond to the four ordinary double points. The two complex ordered realization-space points are defined over \(\mathbb Q(\sqrt{-3})\).

The boundary \(B\) is the reduced normal-crossings total transform after blowing up the eight triple points only. Do not blow up the four ordinary nodes: those remain direct intersections of strict-transform line components. No Jacobian group of the original, unblown-up degree-eight curve is asserted. The smoothing conclusion requires a **regular**, split semistable model over \(\mathbb C[[t]]\), with node smoothing equations \(uv=t\) up to formal units.

## Proof

Index the first eight vertices by \(P\) (the original eight line components), and the next eight vertices by the affine three-point lines in \(\mathbb F_3^2\) avoiding the origin (the exceptional components). Join an original-line vertex to a triple-point vertex exactly when the corresponding point lies on that affine line. Additionally, for each of the four one-dimensional subspaces of \(\mathbb F_3^2\), join the two corresponding nonzero-point vertices directly: this is the ordinary node left unblown-up. There are \(24\) line-to-exceptional and \(4\) direct line-to-line edges.

Each original-line component therefore meets exactly four other branches (three triple-point exceptional components and one ordinary double point); each exceptional component meets exactly three original-line components. The graph has \(16\) vertices, \(28\) edges, and is connected. All components are rational, hence its arithmetic genus is \(28-16+1=13\). Every rational component meets at least three other branches, so \(B\) is a stable curve.

Write \(L\) for the integral \(16\)-by-\(16\) graph Laplacian. Remove the last row and column to obtain \(L'\). The exact unimodular row and column operations implemented by `verify_maclane_boundary.py` construct integer matrices \(U,V\) with \(|\det U|=|\det V|=1\) and

\[
UL'V=\operatorname{diag}(1,1,1,1,1,1,1,1,1,2,6,12,12,48,48).
\]

The complete integral Smith form proves the group decomposition as a cokernel. An independent fraction-free determinant calculation of two different reduced Laplacians gives \(\det L'=2^{14}3^5\), matching the product of the nonunit Smith factors. The checker reconstructs each of the twelve underlying affine lines from its equation over \(\mathbb F_3\), ensures that every unordered pair of the eight original lines belongs to exactly one ordinary double or triple point, and verifies every matrix identity exactly.

Raynaud's regular semistable component-group theorem identifies the geometric component group of the Néron model with the degree-zero graph-divisor group modulo the image of the integral Laplacian. Because all the nodes have unit thickness, this is precisely \(K(\Gamma_B)\). No condition about the generic Jacobian having good reduction is required.

## Verification

Run `python3 verify_maclane_boundary.py` with the Python 3 standard library. The script rebuilds all graph data from finite-field equations, computes a full unimodular Smith certificate, validates the Smith identity by matrix multiplication and unimodularity determinants, and independently evaluates two rooted determinants by fraction-free elimination. Its success marker is `MACLANE_STABLE_BOUNDARY_INTEGRAL_COMPONENT_GROUP_OK`. The checked program and its exact output are included.

## Relationship to prior work

Artal Bartolo–Carmona Ruber–Cogolludo Agustín–Marco Buzunáriz (first posted 2003) describe MacLane's combinatorics as dual to \(\mathbb F_3^2\setminus\{0\}\). Nazir–Yoshinaga (2012), Example 4.3, give the two conjugate complex realizations and their disconnected ordered moduli. Raynaud's theorem supplies the general component-group/graph-Jacobian bridge. These pre-existing results provide the geometry and formal connection, but do not supply the integer Smith factors computed here.

The eight-triple-point-only Möbius–Kantor incidence graph omits the four residual ordinary-double edges and therefore does **not** have the graph used here. A generalized Jacobian or zeta calculation for the original singular eight-line union likewise does not entail this component group, because its local triple points have not been replaced by exceptional components in the same way.

## Limitations

The result is a complete exact invariant of a particular **natural stable boundary**; it does not distinguish the two complex MacLane realization-space points, since their incidence lattices agree. It is not a new classification of line arrangements, nor a formula for all possible degenerations. Changing node thickness, blowing up the four ordinary nodes as well, or retaining the original non-nodal triple points changes the relevant geometric setup. Claims of historical priority are provisional and independent expert review has not been performed.

## References

1. E. Artal Bartolo, J. Carmona Ruber, J. I. Cogolludo Agustín, M. Marco Buzunáriz, *Topology and combinatorics of real line arrangements*, first posted 2003-07-22, [arXiv:math/0307296](https://arxiv.org/abs/math/0307296); Compositio Math. 141 (2005), 1578–1588.
2. S. Nazir and M. Yoshinaga, *On the connectivity of the realization spaces of line arrangements*, Ann. Sc. Norm. Super. Pisa 11 (2012), 921–937, Example 4.3, [full text](https://archive.numdam.org/item/ASNSP_2012_5_11_4_921_0/).
3. Raynaud's component-group theorem, as formulated in O. Amini, M. Baker, E. Brugallé and J. Rabinoff, *Lifting harmonic morphisms I*, Theorem 8.2, [author-hosted full text](https://www.math.ens.psl.eu/~amini/Publications/hmmcI.pdf).
