# Exact Vietoris–Rips homotopy and persistence of rectangular-box vertices

## Finding
Let \(a,b,c\) be arbitrary real numbers with \(0<a\le b\le c\), and let
\[
X=\{0,a\}\times\{0,b\}\times\{0,c\}\subset\mathbb R^3
\]
with the ambient Euclidean metric. Let \(R_r=\operatorname{VR}_{\le r}(X)\), with all nonempty subsets of diameter at most \(r\) as simplices, for \(r\ge0\). Put \(A=a^2\), \(B=b^2\), \(C=c^2\), and \(t=r^2\).

**Homotopy classification.** The complete list below covers every \(r\ge0\). Intervals with equal endpoints are empty, and the two explicitly conditional cases occur only under the displayed strict inequalities:

| Squared-radius range | Homotopy type |
|---|---|
| \(0\le t<A\) | Eight discrete points |
| \(A\le t<B\) | Four discrete points |
| \(B\le t<\min\{C,A+B\}\) | \(S^1\sqcup S^1\) |
| \(C\le t<A+B\) if \(C<A+B\) | \(\bigvee^5 S^1\) |
| \(A+B\le t<C\) if \(A+B<C\) | Two discrete points |
| \(\max\{C,A+B\}\le t<A+C\) | \(\bigvee^3 S^1\) |
| \(A+C\le t<B+C\) | \(S^1\) |
| \(B+C\le t<A+B+C\) | \(S^3\) |
| \(t\ge A+B+C\) | A point |

**Complete barcode.** For every coefficient field \(\mathbb F\), the ordinary persistent homology has precisely the following interval summands, with half-open intervals and repeated intervals counted with multiplicity:
\[
\begin{array}{c|c|c}
\text{degree}&\text{interval}&\text{multiplicity}\\\hline
0 &[0,\infty)&1\\
0 &[0,a)&4\\
0 &[0,b)&2\\
0 &[0,c)&1\\
1 &[b,\sqrt{A+B})&2\\
1 &[c,\sqrt{A+C})&2\\
1 &[c,\sqrt{B+C})&1\\
3 &[\sqrt{B+C},\sqrt{A+B+C})&1
\end{array}
\]
There are no positive-length bars in any other degree. All stagewise integral homology groups are free abelian. These assertions also hold for equal side lengths by simultaneous inclusion of equal-distance simplices.

The geometric transition is governed by \(c^2=a^2+b^2\). When \(c^2<a^2+b^2\), there is an intermediate cube-graph stage with five independent circles; when \(c^2>a^2+b^2\), the corresponding intermediate stage consists of two contractible components. At equality neither stage appears.

## Assumptions and scope
The data are the **eight vertices**, not the filled rectangular solid or its surface. Distances are Euclidean chord lengths, not edge-graph distances. No genericity, integrality, or distinctness of \(a,b,c\) is assumed. An interval \([u,v)\) is present at a radius \(r\) precisely when \(u\le r<v\); zero-length intervals do not count. The claimed barcodes use ordinary, not reduced, persistent homology and are asserted over every field. The topological classification uses the geometric realizations of the finite flag complexes.

Label vertices by binary triples \(v\in\mathbb F_2^3\), where a one in coordinate \(i\) selects the positive endpoint on the corresponding side. For \(u\ne v\), the squared Euclidean distance is
\[
 d(u,v)^2=A(u_1\oplus v_1)+B(u_2\oplus v_2)+C(u_3\oplus v_3).
\]
Consequently, the seven possible positive squared distances are \(A,B,C,A+B,A+C,B+C,A+B+C\). Their only potentially variable ordering, after \(A\le B\le C\), is that of \(C\) and \(A+B\).

## Proof
**1. The flag complexes at all scales.** At a squared radius \(t\), the edge graph is the Cayley graph on \(\mathbb F_2^3\) whose generating differences are precisely the nonzero binary triples having coordinate-weight sum at most \(t\); \(R_r\) is its flag complex.

Before \(t=A\) there are eight isolated vertices. Between \(A\) and \(B\), only first-coordinate edges are present, giving four separate edges. Between \(B\) and both \(C\) and \(A+B\), the permitted differences are the two first coordinate vectors; this gives two separate four-cycles. If \(C<A+B\), adding the third coordinate differences first gives the cube graph, a connected graph on eight vertices with twelve edges, hence a wedge of five circles. If \(A+B<C\), adding the first-two-coordinate diagonals first fills each of the two four-cycles to a full tetrahedron; the complex has exactly two contractible components.

After both \(C\) and \(A+B\) are attained, but before \(A+C\), the permitted differences are the three coordinate vectors and the first-two-coordinate diagonal. The flag complex consists of two disjoint tetrahedra (one in each third-coordinate layer), together with four edges joining corresponding vertices and no mixed triangles. Collapsing the two contractible tetrahedra to vertices is a homotopy equivalence for these CW complexes; the resulting graph has two vertices and four parallel edges, and is a wedge of three circles.

At \(A+C\), the only forbidden differences are the second-plus-third diagonal and the antipodal difference. These generate a two-dimensional subgroup of \(\mathbb F_2^3\), so the graph of forbidden pairs consists of two disjoint four-cycles. The Rips flag complex is the independence complex of this forbidden graph. Each four-cycle has an independence complex consisting of two disjoint edges, homotopy equivalent to \(S^0\). Independence complexes turn disjoint unions into joins, so this stage is homotopy equivalent to \(S^0*S^0\simeq S^1\).

At \(B+C\), only antipodal pairs are forbidden. They form four disjoint edges; their independence complex is \((S^0)^{*4}\cong S^3\), the boundary of the four-dimensional cross-polytope. At \(A+B+C\) all eight vertices span one simplex. These identifications also handle simultaneous thresholds because they depend only on which differences have appeared.

**2. Connected-component persistence.** Coordinate-one edges merge four pairs of initial components at radius \(a\). Coordinate-two edges merge two remaining pairs at radius \(b\); coordinate-three edges merge the final pair at radius \(c\). Extra diagonal edges never merge components not already connected by those coordinate edges. The degree-zero intervals follow.

**3. Degree-one persistence.** Consider the ordinary cube graph with its six oriented square-face boundary cycles: two in each of the coordinate planes \(12\), \(13\), and \(23\). Its integral cycle group is free of rank five. The six face boundaries generate this group with exactly one primitive relation, their signed sum; any five form an integral basis. This follows directly from the cellular chain complex of the cubical two-sphere.

At the threshold for a coordinate-pair diagonal, each of the two corresponding square faces becomes a full tetrahedron, and hence its square boundary becomes nullhomologous. All new diagonal edges are already homologous, by triangular faces, to two-edge paths along the earlier coordinate edges. Thus these diagonal additions create no new degree-one homology classes: they kill the specified square-boundary generators and leave a primitive, torsion-free quotient. The pair thresholds occur in the fixed order \(A+B\le A+C\le B+C\). At the first two such thresholds, each of the two corresponding face boundaries gives one death; at the last, the two remaining boundaries are negatives of each other modulo the previous four, so exactly one dies.

Before the third coordinate edges appear, the first two coordinate directions make two separate square cycles (or two tetrahedra after their diagonal is added). Adding the third coordinate edges introduces either three new independent cycles when the square cycles were already filled, or three independent cycles in addition to the two existing square cycles when they were not. Therefore the two first-plane square cycles are born at \(b\) and die at \(\sqrt{A+B}\); the two second-plane cycles and one further cycle are born at \(c\), with two dying at \(\sqrt{A+C}\) and one at \(\sqrt{B+C}\). The primitive cube-face relation ensures these assertions hold over every field, as well as for integral stagewise homology. When thresholds coincide, taking the corresponding simultaneous attachment simply coalesces the same intervals.

**4. Higher degrees.** All earlier stages are graphs up to homotopy; consequently their homology vanishes in degrees two and above. The only noncontractible later stage is \(S^3\), present for \(\sqrt{B+C}\le r<\sqrt{A+B+C}\). Its unique top-dimensional class is killed when the full simplex appears. This completes the field-independent persistence classification.

## Verification
The independent finite checker `verify.py` builds all 255 nonempty vertex subsets with their exact integer squared-distance grades. It performs ordinary field-two boundary-matrix persistence reduction, separately computes reduced Betti numbers at every distinct critical scale, and compares both with the stated formulas for all \(364\) ordered integer triples \(1\le A\le B\le C\le12\). Across these triples it checks \(2564\) filtration stages, including equal-length cases and cases on the Pythagorean wall. The output `verify_output.txt` records `VERIFY_OK`. This computational test corroborates but does not replace the all-positive-real proof above, which uses only the ordering of the seven squared distances and integral cubical cell topology.

## Relationship to prior work
Saleh, Titz Mite and Witzel classify Vietoris–Rips homotopy types of the vertices of Platonic solids, including the regular cube. Their cube stage is recovered by setting \(a=b=c\), but the regular-solids result does not imply the arbitrary-anisotropy filtration or the Pythagorean phase boundary. Shukla studies graph-shortest-path (Hamming) metrics on hypercube graphs, a different metric from the present arbitrary Euclidean weighted-coordinate metric. General work on homotopical decompositions of Rips complexes supplies machinery but no inspected formula for all rectangular-box vertices. The present statement is a complete three-parameter geometric classification, not a new theorem about regular cubes, graph-metric hypercubes, or higher-dimensional boxes.

## Limitations
The result is restricted to the eight vertices of three-dimensional axis-aligned rectangular boxes; a general parallelepiped has cross terms in squared distances and is not included. No statement is made for the filled box, for non-Euclidean metrics, or for higher-dimensional orthotopes. The novelty comparison is based on the inspected published works and indexed research, not an exhaustive proof that no unpublished equivalent formula exists. External independent validation has not been performed.

## References
1. N. Saleh, T. Titz Mite, S. Witzel, *Vietoris–Rips complexes of Platonic solids*, arXiv:2302.14388, first public 2023-02-28; https://arxiv.org/abs/2302.14388 .
2. S. Shukla, *On Vietoris–Rips complexes (with scale 3) of hypercube graphs*, arXiv:2202.02756, first public 2022-02-06; https://arxiv.org/abs/2202.02756 .
3. W. Chachólski, A. Jin, M. Scolamiero, F. Tombari, *Homotopical decompositions of simplicial and Vietoris Rips complexes*, Journal of Applied and Computational Topology 5 (2021), 215–248; https://doi.org/10.1007/s41468-021-00066-2 .
