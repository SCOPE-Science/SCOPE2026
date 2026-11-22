# Sharp three-polytope graph diameters under arbitrarily small dihedral excess

## Finding
For every integer \(f\ge4\) and real \(\delta>0\), there exists a simple convex three-dimensional polytope \(P\) with exactly \(f\) facets, every interior dihedral angle strictly smaller than \(\pi/2+\delta\), and one-skeleton graph diameter
\[
\operatorname{diam}G(P)=\left\lfloor\frac{2f}{3}\right\rfloor-1.
\]
This is the largest graph diameter of **any** convex three-polytope with \(f\) facets. Moreover, within the particular near-right-angle construction of Li–Wang–Yu there is a specified pair of vertices attaining that diameter and an explicit rational-height Lipschitz certificate.

## Assumptions and scope
Graph diameter counts edges of shortest vertex-edge paths, not Euclidean distance. A simple three-polytope is one with exactly three facets incident to each vertex. Dihedral angles are interior angles. The conclusion holds separately for every finite \(f\) and every positive \(\delta\); no single bounded polytope is claimed to work for infinitely many values of \(f\).

Fix \(k=f-2\ge2\). The geometric realization is the sequence of three-dimensional apex truncations introduced by Li, Wang and Yu [1], with base facet \(B\) and side facets \(F_0,\dots,F_k\). The first object, at \(k=2\), is a tetrahedron. Subsequently the vertex incident to the last three side facets is cut off; this creates a triangle \(F_k\) and three new vertices, without deleting the other old vertices.

## Proof
**1. The near-right-angle realization.** For arbitrary \(k\), choose an integer \(M>k\) and a sufficiently large transcendental real \(R>2\). Set \(\theta=\arccos(-1/R)\) and outward side normals proportional to
\[
 v_j=(\cos(j\theta),\sin(j\theta),R^{j-M}),\quad 0\le j\le k,
\]
with base normal \((0,0,-1)\). The geometric construction and its verification in [1, Section 2] give a bounded, simple realization of the stated successive truncations and show that every interior angle is strictly less than \(\pi/2+\arcsin(4/R)\). Briefly, the key recurrence is
\[
 v_{j+3}=R v_j+v_{j+1}+(R-2/R)v_{j+2}.
\]
Its coefficients are positive for \(R>\sqrt2\); therefore the next normal uniquely exposes the triple intersection at the current apex, which can be cut sufficiently shallowly. Only faces whose indices differ by at most three become newly adjacent. For such pairs, the normalized outward-normal dot product is less than \(4/R\), and base-side dihedral angles are acute. Taking \(R\) sufficiently large, in particular with \(\arcsin(4/R)<\delta\), gives the required strict angle condition. This construction and its angle estimate are those of [1], not new claims here.

**2. Exact vertex labels and edges.** A vertex is labeled by its three incident facets, identifying facet \(B\) with symbol \(b\). The vertex set is
\[
 L_{01}=\{b,0,1\},\quad L_{02}=\{b,0,2\},\quad L_{12}=\{b,1,2\},
\]
\[
 U_j=\{j,j-1,j-3\},\quad W_j=\{j,j-2,j-3\}\quad(3\le j\le k),
\]
\[
 T_k=\{k,k-1,k-2\}.
\]
These labels are an induction on the truncations: at the step from \(k-1\) to \(k\), the old apex \(T_{k-1}\) is removed and the three vertices \(U_k,W_k,T_k\) replace it. In the base tetrahedron, the first three vertices and \(T_2\) are precisely its four vertices. There are \(2k\) vertices altogether. Two labeled vertices share an edge if and only if their facet-label sets share exactly two members: this follows from simplicity and the fact that an intersection of two distinct facets is either empty or an edge. This incidence rule supplies the graph without assumptions about Euclidean lengths.

**3. A sharp graph-distance certificate.** Define the integer potential \(H=3h\) on these vertices by
\[
 H(L_{01})=2,\quad H(L_{02})=3,\quad H(L_{12})=4,
\]
\[
 H(U_j)=2j,\qquad H(W_j)=2j-1,\qquad H(T_k)=2k+1.
\]
Every graph edge \(vw\) satisfies \(|H(v)-H(w)|\le3\). To check this for all \(k\) without an appeal to finite experiments, inspect the induction. It holds for the tetrahedron. In a truncation, only the three edges formerly incident to the removed top vertex change. Its three former neighbors are the vertices supported on the three pairwise intersections of its incident side facets; the three replacement vertices connect, respectively, to those neighbors. Direct substitution in the displayed formula gives potential difference exactly \(3\) along those three links, while the new triangle has potential differences \(1,1,2\). For the first two truncations, the same check uses the explicit base labels (the neighbors of \(T_2\) are \(L_{01},L_{02},L_{12}\); the remaining exceptional old neighbor at \(k=4\) is \(L_{12}\)). Every old edge surviving truncation retains its endpoint potentials: the only old vertex removed was the apex, while the labels of the other vertices, including the special base vertices, are unchanged. Hence the edge bound holds for every integer \(k\ge2\).

Any path from \(L_{01}\) to \(T_k\) therefore has at least
\[
 \left\lceil\frac{H(T_k)-H(L_{01})}{3}\right\rceil
 =\left\lceil\frac{2k-1}{3}\right\rceil
 =\left\lfloor\frac{2k+1}{3}\right\rfloor
\]
steps. Thus \(\operatorname{diam}G(P)\ge\lfloor(2k+1)/3\rfloor\).

**4. Universal upper bound.** In any convex three-polytope with \(f\) facets and \(V\) vertices, Euler's formula and vertex degrees at least three give \(V\le2f-4\). Its one-skeleton is three-vertex-connected (the classical polytope graph connectivity theorem, equivalently the three-dimensional case of Steinitz/Balinski). Choose vertices at graph distance \(D\). Every intermediate breadth-first-search level from the first vertex has at least three vertices: otherwise that level, of size one or two, separates the root from the last vertex. The two endpoint levels contain at least one vertex each, so \(V\ge3(D-1)+2=3D-1\). Consequently
\[
 D\le\left\lfloor\frac{V+1}{3}\right\rfloor
 \le\left\lfloor\frac{2f-3}{3}\right\rfloor
 =\left\lfloor\frac{2f}{3}\right\rfloor-1.
\]
Substituting \(f=k+2\), this equals the lower bound from the potential. Therefore all asserted graph diameters are sharp. The upper bound is classical [2,3]; the simultaneous near-right-angle sharpness and explicit potential are the claimed additions.

## Verification
The standalone `CHECKER.py` reconstructs the complete facet-triple graph, checks all edges against the integer potential and tests graph diameters for the 99 values \(2\le k\le100\) with standard-library integer arithmetic. It also verifies the cubic degree, face/edge/vertex counts, and the stated diametral pair. Reproduction: run `python3 CHECKER.py` in a directory containing that file. These finite checks are corroboration of, not replacements for, the induction and the three-connectivity argument above. The geometric angle bound is taken from the proved construction in [1].

## Relationship to prior work
Li–Wang–Yu [1] supply the exact near-right-angle realization, all face counts, and its apex-truncation incidence rule, but do not state or evaluate the one-skeleton diameter. Klee's diameter theory [2], also summarized in [3], gives the extremal \(\lfloor2f/3\rfloor-1\) bound without a near-right-angle constraint. The present combination proves that arbitrarily small **positive** right-angle excess preserves the maximum combinatorial diameter **at every facet number**, with an explicit extremal vertex pair and Lipschitz certificate. Its proof of the graph statement is independent of the geometric construction's estimates once the facet-triple data are known.

## Limitations
This is a three-dimensional existence theorem; it does not classify every near-right-angle polytope, prove uniform shape regularity, or extend graph-diameter sharpness to higher dimensions. The new graph result is based on an earlier specific construction and an established classical upper bound. Novelty is provisional pending specialist historical assessment; in particular, a previously published implicit identification of the same truncated chain as a diameter-extremizer could reduce priority. No independent mathematical audit has been performed.

## References
[1] Z. Li, J. Wang and J. Yu, *Infinitely many convex polytopes with dihedral angles bounded above by \(\pi/2+\delta\)*, arXiv:2611.09021v1, first public November 6, 2026. https://arxiv.org/abs/2611.09021

[2] V. Klee, *Paths on polyhedra. II*, Pacific Journal of Mathematics **17** (1966), 249–262. https://msp.org/pjm/1966/17-2/pjm-v17-n2-p08-p.pdf

[3] F. Santos, *Diameter of polytopes and the Hirsch Conjecture*, MDS summer school problem sheet, Exercise 1 (2012). https://www3.math.tu-berlin.de/combi/MDS/summerschool12-material/santos_problems.pdf
