# Pentagonal rectangular torus grids have a circle and one two-sphere per column at Rips scale two

## Finding

For every integer \(n\ge 7\), let \(G_n=C_5\square C_n\) be the Cartesian product of simple cycle graphs, with its unweighted shortest-path distance on vertices. Its inclusive Vietoris–Rips complex at threshold two satisfies

\[
\operatorname{VR}_{\le 2}(V(G_n))\simeq S^1\vee\bigvee^n S^2.
\]

More strongly, the complex undergoes exactly \(20n\) explicit elementary simplicial collapse pairs to a union of \(n\) consecutive two-column subcomplexes, each independently collapsible to a triangulated two-sphere. The reduced integral homology is free, with \(\widetilde H_1\cong\mathbb Z\), \(\widetilde H_2\cong\mathbb Z^n\), and all other reduced homology zero. The scale-one inclusion induces a surjection on integral first homology whose kernel is a primitive subgroup of rank \(5n\).

## Assumptions and scope

Use row labels \(a\in\mathbb Z/5\mathbb Z\) and column labels \(j\in\mathbb Z/n\mathbb Z\). The vertices are \((a,j)\), with graph metric
\[
d((a,j),(b,k))=\min(|a-b|,5-|a-b|)+\min(|j-k|,n-|j-k|),
\]
where integer representatives of the cyclic differences are taken with nonnegative absolute values. A face consists of a finite vertex subset with all pairwise distances at most \(2\). We include faces of every allowed dimension, not just the graph and not an open-threshold Rips complex. All homotopy equivalences are ordinary nonequivariant equivalences of geometric realizations. We do not assert a result for \(n<7\).

## Proof

**1. Column separation.** Since \(n\ge7\), every clique in the square of \(C_n\) lies within a unique block of three consecutive columns when it occupies three columns, and within at least one such block otherwise. If a face of the full Rips complex contains vertices from columns \(j-1\) and \(j+1\), then the row labels of its vertices in those two columns must be identical: the column distance already equals two. Furthermore, the face contains exactly one vertex in each extreme column, say \(u=(a,j-1)\) and \(w=(a,j+1)\). Its other vertices, if any, lie in column \(j\) and have row labels among \(a-1,a,a+1\). These three middle-column vertices themselves form a simplex because every pair in one pentagonal column is at distance at most two. The edge \(e_{j,a}=\{u,w\}\) therefore has full simplicial link the two-simplex on \((a-1,j),(a,j),(a+1,j)\). No face contains two different edges of the form \(e_{j,a}\): the unique outer-column pair already fixes its middle column and row label.

**2. Exact relative collapse.** Fix \(e_{j,a}\) and let \(p=(a,j)\) be the middle vertex with the same row. Write \(q_-=(a-1,j)\) and \(q_+=(a+1,j)\). For each subset \(T\subseteq\{q_-,q_+\}\), in decreasing order of \(|T|\), delete the elementary pair
\[
\big(e_{j,a}\cup T,\ e_{j,a}\cup T\cup\{p\}\big).
\]
Each lower face is free at deletion: all its other cofaces within \(e_{j,a}*\Delta^2\) have already been removed by the larger-\(T\) steps, and no face lies in two different outer-edge stars. There are four pairs per edge and \(5n\) such edges, hence exactly \(20n\) pairs. Every face not remaining after these collapses contained one such distance-two column edge. The residual complex is therefore
\[
L_n=\bigcup_{j\in\mathbb Z/n\mathbb Z} P_j,
\]
where \(P_j\) is the full induced Rips subcomplex on the ten vertices of columns \(j\) and \(j+1\). For cyclic indices, \(P_j\cap P_{j+1}\) is the full simplex on column \(j+1\); all other distinct intersections are empty unless the indices are adjacent in the column cycle. There are no triple intersections. The pairwise intersections are nonempty contractible five-vertex simplices.

**3. A two-column sphere.** Each \(P_j\) is canonically isomorphic to \(P=\operatorname{VR}_{\le2}(V(C_5\square K_2))\), where distances are the product graph metric. The full face vector of \(P\) is \((10,35,50,25,2)\). A reproducible 48-pair elementary collapse leaves six vertices, twelve edges, and eight triangles, with each edge incident to exactly two triangles and each vertex link a connected four-cycle. The residual complex is a connected closed triangulated surface with Euler characteristic \(6-12+8=2\), hence a two-sphere. This also follows by recognizing the resulting six-vertex triangulation as an octahedral boundary. The 48 exact face pairs and the complete residual face set are specified in `local_sphere_collapse.json`; `verify_rectangular.py` independently builds \(P\) from graph distances, replays the pairs and checks the full residual surface. Thus \(P_j\searrow S^2\) for every \(j\), without relying on mod-two homology or extrapolation.

**4. Cyclic graph-of-spaces gluing.** The cover of \(L_n\) by the subcomplexes \(P_j\) has intersection graph precisely \(C_n\), contractible nonempty edge intersections, and no higher intersections. All inclusions are cofibrations. Replace the diagram by its homotopy-colimit model: each vertex space has homotopy type \(S^2\) and each edge space is contractible. The maps from an edge space to its incident vertex spaces are nullhomotopic. Contracting a spanning tree of the incidence cycle yields a wedge of the \(n\) two-spheres; the remaining cyclic edge produces one additional circle. Therefore
\[
L_n\simeq \left(\bigvee^n S^2\right)\vee S^1.
\]
The elementary collapse \(\operatorname{VR}_{\le2}(V(G_n))\searrow L_n\) establishes the theorem over the integers, including absence of torsion and the homotopy type, not just Betti numbers.

**5. First persistence map.** The scale-one complex is exactly the graph \(G_n\), with \(5n\) vertices and \(10n\) edges, so \(H_1(G_n;\mathbb Z)\cong\mathbb Z^{5n+1}\). A row-fixed column cycle meets consecutive slabs in order and represents the generator of the circle factor of \(L_n\). Its image under inclusion is therefore a generator of \(H_1(\operatorname{VR}_{\le2}(G_n);\mathbb Z)\cong\mathbb Z\). This gives surjectivity, and the kernel is a primitive free lattice of rank \(5n\), as claimed.

## Verification

Run `python3 verify_rectangular.py` in the directory containing `local_sphere_collapse.json`. Both files use only the Python standard library. The verifier constructs the exact graph from the original Cartesian edges, computes two-step distances by breadth-first search, and enumerates all Rips faces directly from pairwise adjacency. It checks every prescribed elementary free-face removal and tests equality of the residual face set with the union of consecutive-column full subcomplexes. It separately checks the 48-pair sphere certificate and vertex links of the surviving surface.

For \(n=7,8,9,10,11,12\), the full complexes have respectively \(918,1049,1180,1311,1442,1573\) faces including the empty face, with \(140,160,180,200,220,240\) explicit relative collapse pairs. All six tests passed; the included checker reproduces the per-size PASS statements. The uniform all-\(n\) conclusion follows from the column-separation and link arguments in Steps 1–4, not from a finite test range. The local certificate proves the one finite computation required in Step 3.

## Relationship to prior work

Adams, Adetowubo, Barriga-Acosta, Feng, and Sterling, *Vietoris–Rips complexes of torus grids*, arXiv:2502.07134, first submitted 2025-02-10, analyze square grids \(C_m\square C_m\). Their full HTML manuscript, especially Definitions in Section 3, Theorems 5.8, 5.10, 5.12, and Section 7, contains no stated classification of the unequal-width family \(C_5\square C_n\) for all \(n\ge7\). Its square-grid theorem does not imply the present result: the first factor here remains five while the second grows without bound.

A published classification of \(\operatorname{VR}_{\le2}(C_4\square C_n)\), for \(n\ge7\), yields \(S^1\vee\bigvee^n S^3\), using local three-spheres. The new pentagonal case has local **two-spheres**, so it is neither that theorem's parameter substitution nor its corollary. A separate circular-ladder result includes the local \(C_5\square K_2\) two-sphere as a special finite case, but does not classify the cyclic gluing of \(n\) such slabs and its additional circle. Results for \(K_m\square C_n\) concern complete-graph fibers, not pentagonal fibers. The novelty comparison is based on the actual family and implication domains; absence of a search hit alone is not a uniqueness proof.

## Limitations

Only inclusive threshold two, unweighted graph distances, the pentagonal factor, and \(n\ge7\) are covered. The conclusion does not assert equivariance under graph automorphisms, a canonical splitting, higher-scale persistence maps, or a uniform formula for other fixed widths. Other literature under different terminology may contain an equivalent classification.

## References

1. H. Adams, A. Y. Adetowubo, H. Barriga-Acosta, Z. Feng, J. Sterling, *Vietoris–Rips complexes of torus grids*, arXiv:2502.07134v2, https://arxiv.org/html/2502.07134v2 (first public 2025-02-10).
2. *A thin toroidal grid has scale-two Rips type \(S^1\vee\bigvee^n S^3\)*, public published-finding corpus research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-thin-toroidal-grid-has-scale-two-rips-type-s-1-vee-bigvee-ns-3--a2c9f7beb39c.
3. *Scale-two Rips homotopy types of finite circular ladders*, public published-finding corpus research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-scale-two-rips-homotopy-types-of-finite-circular-ladders--ccd7a360a668.
4. *A sharp one-circle-to-sphere-wedge transition for clique-fiber cyclic Rips complexes*, public published-finding corpus research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-sharp-one-circle-to-sphere-wedge-transition-for-clique-fiber-c--e28e5da49d34.
