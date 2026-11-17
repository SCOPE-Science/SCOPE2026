# Primitive vertex-deletion stability for Vietoris–Rips complexes of finite projective-plane incidence graphs

## Finding
Let \(\Pi\) be any finite projective plane of order \(q\ge 2\). Let \(G_\Pi\) be its bipartite point–line incidence graph with unit-edge shortest-path metric. Delete an arbitrary *point* vertex \(v\), recompute distances on the connected graph \(H=G_\Pi-v\), and use inclusive radius \(2\). Then
\[
\operatorname{VR}_{\le2}(H)\simeq\bigvee^{q^3-q}S^2.
\]
Writing \(K_H=\operatorname{VR}_{\le2}(H)\) and \(K_G=\operatorname{VR}_{\le2}(G_\Pi)\), the vertex-inclusion map induces an integral primitive injection
\[
0\longrightarrow H_2(K_H;\mathbb Z)\longrightarrow H_2(K_G;\mathbb Z)
\longrightarrow\mathbb Z^q\longrightarrow 0.
\]
Both complexes have no other positive-degree reduced integral homology. The same conclusions hold upon deleting an arbitrary *line* vertex, by point–line duality. Thus deletion of one point or line erases exactly \(q\) independent, primitive degree-two classes without introducing torsion.

## Assumptions and scope
For a finite projective plane of order \(q\), the number of points and of lines is \(N=q^2+q+1\), every point or line has incidence degree \(q+1\), every two points have a unique joining line, and every two lines a unique intersection point. The statement covers all finite projective planes, including non-Desarguesian planes when they exist; it makes no existence assertion for any unconstructed order. Graph distance on \(H\) is computed *after* deletion and is not the metric inherited from \(G_\Pi\). Radius \(2\) includes distances equal to \(2\). Homology is integral and unreduced unless explicitly marked.

## Proof
The incidence graph has no four-cycles, because two distinct points cannot both lie on two distinct lines. Its vertex deletion \(H\) also has no four-cycles and is connected: every pair of surviving points remains joined through its unique line; every line contains at least \(q\ge2\) surviving points. More concretely, every surviving point meets every line by a path of length at most three or, when the unique point of intersection was removed, by a longer path. This suffices for connectivity.

Let \(P'\) be the surviving points, and \(L\) all lines. All pairs in \(P'\) are at distance two in \(H\), so the point-side radius-two clique complex is a simplex. Let \(T\) be the set of \(q+1\) lines through the deleted point \(v\). Two lines in \(T\) have no surviving common point, so are not distance two. Every other pair of lines intersects at a surviving point. Thus the line-side radius-two clique graph is a complete graph except for the missing edges among \(T\). Its clique complex is a cone: choose any line \(\ell_0\notin T\), which is adjacent to every other line in that graph. Such lines exist because \(N>q+1\).

An edge between different sides at radius two is precisely an incidence edge: bipartite paths between opposite sides have odd length, so distance at most two means distance one. A radius-two clique cannot contain two points and two lines, since that would require a four-cycle in \(H\). Partition \(K_H=U\cup V\) into faces with at most one line, respectively faces with at most one point. Then \(U\cap V=H\), exactly as a one-dimensional simplicial complex. In \(U\), each line vertex \(\ell\) belongs to only one maximal mixed simplex \(\{\ell\}\cup P'(\ell)\), where \(P'(\ell)\) is its surviving nonempty incident-point set. Hence \(U\) collapses by dominated-vertex deletions to the simplex on \(P'\). Likewise in \(V\) each point vertex \(p\) belongs to a unique maximal mixed simplex \(\{p\}\cup L(p)\), and \(V\) collapses onto the conical line-side clique complex. Both pieces are contractible; their intersection \(H\) is connected. Because the inclusions are simplicial cofibrations, the union is a homotopy pushout, so
\[
K_H\simeq \Sigma H.
\]
A connected graph with first Betti number \(b\) has homotopy type \(\bigvee^b S^1\); suspension yields \(\bigvee^bS^2\). The full incidence graph has \(2N\) vertices and \((q+1)N\) edges, giving \(b(G_\Pi)=(q+1)N-2N+1=q^3\). Deleting one degree-\(q+1\) point removes one vertex and \(q+1\) edges, so \(b(H)=q^3-q\). This proves the homotopy claim.

For the inclusion, carry out the same cover decomposition on \(K_G\), whose two pure-side subcomplexes are simplices; therefore \(K_G\simeq \Sigma G_\Pi\). The Mayer–Vietoris connecting homomorphisms for the two covers identify \(H_2(K_H;\mathbb Z)\) naturally with \(H_1(H;\mathbb Z)\) and \(H_2(K_G;\mathbb Z)\) with \(H_1(G_\Pi;\mathbb Z)\). Naturality identifies the induced map with graph cycle inclusion. With the oriented edges of \(G_\Pi\) as a basis, \(H_1(H;\mathbb Z)\) is exactly the kernel of the coordinate projection from \(H_1(G_\Pi;\mathbb Z)\) onto the \(q+1\) deleted incident edges. The quotient embeds into \(\mathbb Z^{q+1}\); it is thus torsion-free, and its rank is \(b(G_\Pi)-b(H)=q\). The claimed primitive short exact sequence follows. Point–line duality repeats the argument for deletion of a line.

## Verification
The bundled standard-library `verify.py` constructs \(\mathrm{PG}(2,2)\) and \(\mathrm{PG}(2,3)\) from homogeneous coordinates, deletes one point, recomputes shortest-path distances, enumerates all radius-two maximal cliques and their faces, and independently checks every face against the structural cover decomposition. Exact binary chain-boundary elimination independently verifies degree-one vanishing and second Betti ranks \(6\) and \(24\). For \(q=2\), the enumerated face vector is \((13,51,75,38,9,1)\), with boundary ranks \((12,39,30)\) in degrees one through three. For \(q=3\), the face vector is \((25,186,586,1045,1443,1512,1164,648,257,70,12,1)\), with ranks \((24,162,400)\). These finite checks do not replace the all-order proof or establish the integral homotopy claim on their own.

## Relationship to prior work
A published 2026 calculation gives \(\operatorname{VR}_{\le2}(G_\Pi)\simeq\bigvee^{q^3}S^2\) for unpunctured finite projective-plane incidence graphs, via a union of contractible parts. That theorem does not calculate the recomputed metric after deletion, the resulting missing edges among lines through the removed point, or the induced integral map; the preceding proof establishes these separately. In particular, the present homotopy equivalence for \(H\) is not a formal consequence of the bare homotopy type of \(K_G\), and the primitive comparison requires naturality in integral graph cycle lattices.

General work on clique complexes of graph powers and on Rips complexes of metric gluings supplies broader methodological context, without treating this specific vertex-deletion map. The present result does not purport to introduce the general homotopy-pushout technique or the known complete-plane calculation.

## Limitations
The one-vertex deletion is essential to the present formulation; removing multiple points or a point and a line may destroy the conical pure-side condition. The theorem does not determine the later-radius Rips filtration of \(H\), whose recomputed diameter can exceed that of \(G_\Pi\). The finite computational checks cover only the Desarguesian orders two and three. Bibliographic priority cannot exclude unindexed treatments of a similar puncture, and independent mathematical validation has not been performed.

## References
1. *Scale-two Vietoris–Rips complexes of finite projective-plane incidence graphs* (first published 2026-10-04), published result and full proof at https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-scale-two-vietoris-rips-complexes-of-finite-projective-plane-inc--c3740b96b3c3/RESULT.md .
2. M. Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433 (2011).
3. M. Adamaszek, H. Adams, E. Gasparovic, M. Gommel, E. Purvine, R. Sazdanovic, B. Wang, Y. Wang, L. Ziegelmeier, *Vietoris–Rips and Čech Complexes of Metric Gluings*, SoCG 2018, DOI: 10.4230/LIPIcs.SoCG.2018.3.
