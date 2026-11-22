# Primitive Rips persistence under star-incidence faults in finite projective planes

## Finding
Let \(\Pi\) be a finite projective plane of order \(q\ge2\). Write \(G_0\) for its point–line incidence graph. Fix one point \(p\), order its \(q+1\) incident lines arbitrarily, and let \(G_t\) be obtained by deleting its first \(t\) incidence edges while retaining all vertices, for \(0\le t\le q\). Recompute the unit-edge graph distances after each deletion. For the inclusive scale-two Vietoris–Rips complexes \(X_t=\operatorname{VR}_{\le2}(G_t)\),
\[
X_t\simeq \bigvee^{q^3-t} S^2.
\]
For all \(0\le s\le t\le q\), their natural inclusions \(X_t\hookrightarrow X_s\) induce primitive injections and split integral exact sequences
\[
0\longrightarrow H_2(X_t;\mathbb Z)\longrightarrow H_2(X_s;\mathbb Z)\longrightarrow\mathbb Z^{t-s}\longrightarrow0.
\]
There are no other positive-dimensional reduced integral homology groups. Thus each additional missing incidence eliminates exactly one integral two-sphere class, irrespective of the plane or the order of deletions. At the endpoint \(t=q\), the complex strongly collapses onto the radius-two Rips complex of the graph obtained by deleting the chosen point.

## Assumptions and scope
A finite projective plane of order \(q\) has \(N=q^2+q+1\) points and equally many lines, \(q+1\) incidences per point and line, and a unique joining line for each distinct point pair and intersection point for each distinct line pair. No Desarguesian coordinate assumption is made. The incidence graph is simple and bipartite. Every retained edge has length one and every distance is recomputed in \(G_t\). The Rips convention is inclusive: every simplex consists of vertices with all pairwise graph distances at most two. The restriction \(t\le q\) ensures at least one edge survives at the chosen point and the graph stays connected. The theorem is independent of the order of the chosen deleted incidences. It does not assert existence of planes of any unconstructed order.

## Proof
Write \(P\) for the point vertices, \(L\) for the line vertices, and \(D_t\subset L(p)\) for the set of \(t\) deleted lines at the chosen point \(p\). The graph \(G_t\) is connected: the surviving line through \(p\) joins it to the remainder, and all other points and lines retain all their original incidences. A more explicit path from \(p\) to any other point \(x\) goes through a surviving line \(M\ni p\), then a point \(y\in M\setminus\{p\}\), then the unique line through \(x,y\) and finally \(x\), omitting the final two edges if \(x\in M\). Every line contains an accessible point. The incidence graph has no four-cycle, and edge deletion cannot create one.

Let \(K_P\) and \(K_L\) be the restrictions of \(X_t\) to its two vertex shores. Since a point pair has a unique joining line, among pairs of points only the pairs \(\{p,x\}\) with \(x\in M\setminus\{p\}\) and \(M\in D_t\) cease to have graph distance two. Put \(E_t=\bigcup_{M\in D_t}(M\setminus\{p\})\). The \(t\) sets in this union are disjoint, each of size \(q\). Hence
\[
K_P=\Delta(P\setminus\{p\})\cup\Delta(\{p\}\cup(P\setminus E_t)).
\]
The intersection is the simplex on \(P\setminus(E_t\cup\{p\})\), which has \(q(q+1-t)\ge q\) vertices. Thus \(K_P\) is contractible, including \(t=0\).

Among lines, only pairs of lines through \(p\) with at least one member in \(D_t\) lose their unique common incidence point at distance two. Every line not through \(p\) meets every other line at a point different from \(p\), and so is adjacent to every line in the line-shore distance-two graph. There are \(q^2\) such lines, and any one of them is a cone vertex for \(K_L\). Consequently \(K_L\) is contractible.

A point and a line are at graph distance at most two if and only if they remain incident (opposite-shore distances are odd). Moreover, a radius-two clique cannot contain two distinct points and two distinct lines: four retained incidences would make a forbidden four-cycle. Thus every mixed clique contains exactly one vertex on at least one of the shores. Let \(U_t\) consist of the pure-point subcomplex and all faces with exactly one line; analogously let \(V_t\) consist of the pure-line subcomplex and all faces with exactly one point. Then \(X_t=U_t\cup V_t\) and \(U_t\cap V_t=G_t\) as a one-dimensional simplicial complex.

For each line \(\ell\), its incident-point set in \(G_t\) spans a simplex in \(K_P\), because any two points incident with \(\ell\) have distance two via \(\ell\). In \(U_t\), the apex \(\ell\) belongs to a single maximal mixed simplex, \(\{\ell\}\cup N_{G_t}(\ell)\). Removing these unique apex vertices by elementary simplicial collapses retracts \(U_t\) onto \(K_P\). Similarly, each point apex in \(V_t\) belongs to a single maximal mixed simplex, and \(V_t\) collapses to \(K_L\). Both are therefore contractible.

Since simplicial intersections are cofibrations, the union of two contractible subcomplexes along the connected graph \(G_t\) is a model for its unreduced suspension:
\[
X_t\simeq\Sigma G_t.
\]
There are \(2N\) graph vertices and \((q+1)N-t\) retained incidence edges, hence the integral graph cycle rank is
\[
\operatorname{rank}H_1(G_t;\mathbb Z)=(q+1)N-t-2N+1=q^3-t.
\]
A connected graph has homotopy type a wedge of this many circles. Suspension proves the displayed sphere wedge, with no torsion and no other positive-degree reduced homology.

The covers \((U_t,V_t)\) are nested for \(t\ge s\), because deletion only increases distances and cannot add faces. Naturality of the Mayer–Vietoris connecting isomorphisms gives a commutative comparison
\[
H_2(X_t;\mathbb Z)\cong H_1(G_t;\mathbb Z)\longrightarrow H_1(G_s;\mathbb Z)\cong H_2(X_s;\mathbb Z).
\]
It identifies the Rips inclusion with inclusion of the integral graph cycle lattices. Orient the graph edges and project the cycle lattice of \(G_s\) onto coordinates of the \(t-s\) deleted edges. The kernel is exactly \(H_1(G_t;\mathbb Z)\). Since \(G_t\) is connected, a spanning tree of \(G_t\) provides a fundamental cycle for each removed edge with coefficient one on that edge and zero on the others, so the coordinate projection is surjective onto \(\mathbb Z^{t-s}\). The quotient is therefore free and the injection primitive and split.

Finally, for \(t=q\) the point \(p\) is a leaf, adjacent only to the one retained line \(M\). Its radius-two closed neighborhood is contained in the radius-two closed neighborhood of \(M\): the only vertices at distance at most two from \(p\) are \(p,M\) and the other points of \(M\). Thus \(p\) is dominated by \(M\) in the radius-two flag complex and its deletion is a strong simplicial collapse. Because removing a leaf does not alter distances among remaining vertices, the resulting induced complex is exactly \(\operatorname{VR}_{\le2}(G_0-p)\). This proves endpoint compatibility with the already published single-vertex deletion classification.

## Verification
The accompanying standard-library `verify.py` constructs \(\mathrm{PG}(2,2)\) and \(\mathrm{PG}(2,3)\) from homogeneous coordinates. At every stage \(0\le t\le q\) it checks the projective-plane axioms, connected shortest-path metrics, the two predicted same-shore adjacency patterns, the complete Rips face set against the independently constructed cover description, and an exhaustive elementary-collapse reduction. The residual two-dimensional complexes are analyzed using exact binary boundary elimination (a finite cross-check, not an integral proof). The resulting second Betti ranks are \((8,7,6)\) at order two and \((27,26,25,24)\) at order three, with vanishing first Betti rank in each case. The full output is included in `verify_output.txt` and can be regenerated with `python3 verify.py`. The structural proof, rather than numerical extrapolation, establishes the result for all finite projective planes and over \(\mathbb Z\).

## Relationship to prior work
Adams and Coskunuzer, *Geometric Approaches on Persistent Homology* (arXiv:2103.06408; first submitted 2021-03-11), study persistent homology of graph-power filtrations. A previously published classification, *Scale-two Vietoris–Rips complexes of finite projective-plane incidence graphs* (2026-10-04), proves the intact case \(X_0\simeq\bigvee^{q^3}S^2\) using a two-contractible-piece suspension model. A later result, *Primitive vertex-deletion stability for Vietoris–Rips complexes of finite projective-plane incidence graphs* (2026-11-17), handles deletion of an entire point or line and obtains a rank loss of \(q\) with primitive inclusion. Neither result states or implies the intermediate recomputed-metric star-incidence filtration, the exact per-edge rank loss, or all of its integral inclusion maps without a separate geometric analysis. Here that analysis proves the missing pure-shore clique complex remains contractible through every intermediate stage and that the endpoint agrees by an explicit strong collapse. The suspension/mapping technique itself is not claimed as new.

The finite-metric scale-two work of Feng and Nukala (arXiv:2302.14664, first public 2023-02-28) studies special families of subset metrics and does not address these graph incidences in its available abstract; its full text was not materially inspected. An unindexed equivalent star-fault statement remains a bibliographic risk.

## Limitations
Only deletions incident with one point (or, by duality, one line) are covered. Arbitrary disjoint edge failures, later Rips radii, and graph disconnection after deleting all \(q+1\) edges are outside the theorem. The finite computational cross-check covers only two Desarguesian orders; uniform validity rests on the axiomatic proof. This is not an independent mathematical certification, and priority cannot exclude unpublished or unindexed equivalents.

## References
- H. Adams and B. Coskunuzer, *Geometric Approaches on Persistent Homology*, arXiv:2103.06408, first posted 2021-03-11, https://arxiv.org/abs/2103.06408.
- M. Adamaszek and H. Adams, *On Vietoris–Rips complexes of hypercube graphs*, arXiv:2103.01040, first posted 2021-03-01, https://arxiv.org/abs/2103.01040.
- Z. Feng and N. C. P. Nukala, *On Vietoris–Rips complexes of finite metric spaces with scale two*, arXiv:2302.14664, first posted 2023-02-28, https://arxiv.org/abs/2302.14664.
- *Scale-two Vietoris–Rips complexes of finite projective-plane incidence graphs* (published 2026-10-04), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-scale-two-vietoris-rips-complexes-of-finite-projective-plane-inc--c3740b96b3c3.
- *Primitive vertex-deletion stability for Vietoris–Rips complexes of finite projective-plane incidence graphs* (published 2026-11-17), https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-primitive-vertex-deletion-stability-for-vietoris-rips-complexes--6fb5eec5366c.
