# The integral component group of the Reye point–line incidence degeneration

## Finding

For the classical Reye configuration of twelve projective points and sixteen lines, let \(\Gamma\) be its canonical 28-vertex, 48-edge bipartite incidence graph. Its exact critical group is \(K(\Gamma)\cong\mathbb Z/2\mathbb Z\oplus(\mathbb Z/8\mathbb Z)^2\oplus(\mathbb Z/24\mathbb Z)^4\oplus(\mathbb Z/96\mathbb Z)^2\), with exactly \(2^{29}3^6\) spanning trees, exponent \(96\), and cycle rank \(21\). For any regular split semistable smoothing with unit-thickness nodes of the stable genus-\(21\) curve obtained by gluing 28 projective lines according to these incidences, this group is the geometric Néron component group of the generic Jacobian. The stable curve is an auxiliary abstract curve, not a claimed union of lines on the original spatial Reye configuration.

## Assumptions and scope

The base geometric incidence configuration is the classical Reye point–line configuration, in characteristic zero for its standard spatial realization. The graph is simple and bipartite; its vertices represent **incidence objects**, not intersection points of a 28-line arrangement in space. The stable nodal genus-21 curve is formed **abstractly** from twenty-eight rational components; any semistable smoothing interpretation requires ordinary nodes of thickness one and a regular total space. All stated group invariants are geometric, not arithmetic Frobenius-fixed subgroups.

## Proof

The eight cube vertices are indexed by \((\epsilon_1,\epsilon_2,\epsilon_3)\in\{0,1\}^3\). Add a center point \(c\) and three coordinate-axis points at infinity \(u_1,u_2,u_3\). For each coordinate \(i\), each of the four edges parallel to that axis gives a triple \(\{v,v+e_i,u_i\}\), and each of the four antipodal pairs gives a triple \(\{v,v+(1,1,1),c\}\). They are the 16 projective lines of Reye's classical cube model. There are 48 incidences; each of the 12 point vertices has degree four, and each line vertex degree three. The graph is connected because the cube-edge incidence subgraph is connected and the other five points/lines attach to it. Hence its first Betti number is \(48-28+1=21\).

Order the points lexicographically by their three binary coordinates, followed by the center and three infinity points; order the twelve edge lines by axis and the two fixed coordinates, followed by the four antipodal diagonals. Construct the zero-one incidence matrix \(B\) and Laplacian \(L=\left(\begin{smallmatrix}4I_{12}&-B\\-B^\mathsf T&3I_{16}\end{smallmatrix}\right)\). The exact determinant identity produced by the explicit 28-by-28 integer matrix is
\[
\det(tI-L)=t(t-7)(t-4)^2(t-3)^6(t^2-7t+8)^9.
\]
The matrix-tree theorem gives
\[
\tau(\Gamma)=\frac{7\cdot4^2\cdot3^6\cdot8^9}{28}=2^{29}3^6.
\]
Delete one row and matching column. Integer Smith elimination gives 18 diagonal units and the nine nonunit invariant factors
\[
2,8,8,24,24,24,24,96,96.
\]
The given standalone exact verifier independently assembles the incidence from the cube edges and diagonals, computes the entire integral Smith form for **five** different root deletions (0,8,11,12,27), and checks each tree determinant and the characteristic polynomial, so these nine factors are a full finite integer certificate, not an inference from the spectrum alone. The construction from an explicitly ordered 28-by-28 integer Laplacian plus a standard exact Smith-normal-form algorithm is reproducible in full, with no floating-point calculations. The sandpile critical group is the cokernel of any reduced Laplacian, yielding the claimed decomposition.

For the curve application, glue 28 copies of \(\mathbb P^1\) at distinct marked rational points, one node for each edge of \(\Gamma\). Every component has degree three or four in the graph, so the resulting connected nodal curve is stable, and its arithmetic genus is \(21\). The ordinary unobstructed deformation theory of nodal stable curves permits a regular one-parameter smoothing with local equations \(uv=t\) for all 48 nodes. Raynaud's graph-component-group theorem then identifies the Néron component group of the smooth generic fiber's Jacobian with the critical group of the unit-edge dual graph. This is an existence-and-conditional-smoothing interpretation, not an assertion about the original projective configuration's embedded union.

## Verification

Run `python3 verify_reye.py` from the extracted package with SymPy available. The script independently constructs all sixteen line triples, checks 48 incidences and the 12-by-16 bidegrees, computes the integer Laplacian and its characteristic polynomial, verifies all five reduced Smith forms, and asserts that their determinant equals \(2^{29}3^6\). The observed exact execution finished with `REYE_5_ROOTS_SPECTRUM_SMITH_OK`. A second program `check_reye_matrix.py` rebuilds the same graph using a different index and asserts the block design identity; both are included, and neither uses floating-point arithmetic.

## Relationship to prior work

Servatius–Servatius (2010) give the cube realization and a classification of projective cube pictures and their lifts; their Sections 1–3 were inspected and do not supply an integral Laplacian Smith decomposition or genus-21 semistable component group. Reye's original 1882 paper establishes the underlying classical point–line configuration. The MathWorld description gives the same incidence parameters and construction, not the integral graph Jacobian. Exact published-finding corpus searches for the Reye point–line Levi graph, its sandpile critical group, Smith form and Néron component group produced no identical decomposition; results concerning the 16-by-16 Kummer biplane and earlier graphs do not imply this 28-vertex nonregular configuration's Smith invariants. The classical geometry, graph-theoretic critical-group definition and semistable identification are prior work. The claim is only the exact natural integral group and its specified geometric interpretation.

## Limitations

Historical priority is provisional: a different terminology, unindexed table or an exhaustive integral graph atlas might have computed these invariant factors earlier. The graph critical group does not identify any Picard or Néron–Severi lattice of a projective Reye variety. The smooth Jacobian statement applies only to a deliberately constructed abstract stable curve with regular thickness-one smoothing, not to the original spatial point-and-line arrangement. Self-review is not independent scientific audit.

## References

1. B. Servatius and H. Servatius, *The generalized Reye configuration*, Ars Mathematica Contemporanea 3 (2010), 21–27; first publicly posted online 2010-01-28, DOI 10.26493/1855-3974.108.423, full text https://dlib.si/stream/URN%3ANBN%3ASI%3ADOC-5K1PGKZ1/ae53e2ec-2fd3-4dc9-ac03-c624a8243516/PDF.
2. T. Reye, *Die Hexaëder- und die Octaëder-Configurationen*, Acta Mathematica 1 (1882), 97–108; classical cube-point-line model.
3. E. W. Weisstein, *Reye Configuration*, MathWorld, https://mathworld.wolfram.com/ReyeConfiguration.html; modern description of the classical 12-point/16-line cube realization.
4. Classical matrix-tree theorem, exact Smith normal form, and Raynaud’s semistable Jacobian component-group theorem.
