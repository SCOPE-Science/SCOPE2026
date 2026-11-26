# Three consecutive multineighbor transitions for Hamiltonian-cycle-deleted bicliques

## Finding
Let \(n\ge7\). Construct the bipartite graph \(G_n\) on shores \(A=\{a_i:i\in\mathbb Z/n\mathbb Z\}\) and \(B=\{b_i:i\in\mathbb Z/n\mathbb Z\}\), with \(a_i b_j\) an edge precisely when \(j\notin\{i,i+1\}\). Thus the missing edges form an alternating Hamiltonian cycle in \(K_{n,n}\). For a positive integer \(m\), let \(\mathcal N_m(G_n)\) consist of nonempty vertex sets with at least \(m\) *common open neighbors* (together with the empty face).

Put \(p_n=\binom n2-2n+1\) and \(q_n=n(n-5)/2-1\). The three consecutive levels have exact **integral homotopy types**
\[
\begin{aligned}
\mathcal N_{n-3}(G_n)&\simeq C_n\amalg C_n,\\
\mathcal N_{n-4}(G_n)&\simeq\left(\bigvee^{p_n}S^1\right)\amalg\left(\bigvee^{p_n}S^1\right),\\
\mathcal N_{n-5}(G_n)&\simeq\left(\bigvee^{q_n}S^2\right)\amalg\left(\bigvee^{q_n}S^2\right).
\end{aligned}
\]
For each shore separately, the natural inclusion from threshold \(n-3\) to \(n-4\) is injective on integral first homology, with primitive rank-one image; its complement has rank \(n(n-5)/2\). The subsequent inclusion from threshold \(n-4\) to \(n-5\) kills *every* first-homology class. Across these three levels the two connected components never merge, so \(\widetilde H_0\cong\mathbb Z\) remains unchanged.

Equivalently, as the reversed threshold \(t=n-m\) increases through \(3,4,5\), every shore first carries one circle, then \(p_n\) circles, then \(q_n\) two-spheres. The result is a three-stage statement, not a classification of all later thresholds.

## Assumptions and scope
The graphs are simple, undirected and unweighted. Indices in subscripts are cyclic modulo \(n\). Homotopy equivalence refers to ordinary realizations of abstract simplicial complexes and integer coefficients. Every asserted threshold is positive when \(n\ge7\). A circle \(C_n\) in the theorem means its one-dimensional cycle complex. The original multineighbor definition is that of Matysiak and Spaliński, with *open* (not closed) neighborhoods.

## Proof
**1. Exact shore decomposition.** In a bipartite graph, no set containing vertices from both shores has even one common neighbor. Hence for every positive \(m\), \(\mathcal N_m(G_n)\) is a disjoint union of its two shore subcomplexes. They are isomorphic by the cyclic interchange \(a_i\leftrightarrow b_{-i}\). It suffices to calculate one shore.

Represent a nonempty subset of shore \(A\) by its cyclic index set \(S\subseteq\mathbb Z/n\mathbb Z\), and let \(S+1=\{i+1:i\in S\}\). The common neighbors of the vertices \(a_i\) for \(i\in S\) are exactly the \(b_j\) whose indices avoid \(S\cup(S+1)\). Therefore the shore complex \(Y_t\), corresponding to \(m=n-t\), has the exact combinatorial description
\[
Y_t=\{\varnothing\ne S\subseteq\mathbb Z/n\mathbb Z:|S\cup(S+1)|\le t\}\cup\{\varnothing\}.
\]
For every proper nonempty \(S\), if \(c(S)\) denotes the number of runs of consecutive selected vertices on the cyclic index set, then \(|S\cup(S+1)|=|S|+c(S)\). This follows by adding the one successor outside each maximal run. All faces in \(Y_3,Y_4,Y_5\) are proper because \(n\ge7\).

**2. First stage, \(t=3\).** Singletons have coverage two. A pair has coverage three exactly when the pair is consecutive; every three-element set covers at least four indices. Hence \(Y_3=C_n\), a circle.

**3. Second stage, \(t=4\).** Every pair has coverage at most four, so the one-skeleton is the complete graph \(K_n\). The only triangular faces are the \(n\) consecutive triples \(\{i,i+1,i+2\}\); there are no higher faces. Each such triangle has a free edge \(\{i,i+2\}\) used in no other triangle, because \(n\ge7\). Collapse these \(n\) edge–triangle pairs simultaneously or sequentially. The remainder is a connected graph with \(n\) vertices and \(\binom n2-n\) edges, so it is a wedge of \(\binom n2-2n+1=p_n\) circles. These collapses preserve every edge of the original cyclic \(C_n\). Consequently the inclusion \(Y_3\hookrightarrow Y_4\) induces an injective map on \(H_1(-;\mathbb Z)\), and the original cycle is primitive: it is an embedded simple cycle in a graph, and a spanning-tree basis can be chosen to include it as one of the free generators. The complementary rank is \(p_n-1=n(n-5)/2\).

**4. Third-stage face census, \(t=5\).** The one-skeleton remains \(K_n\). A triple is a face precisely when at least two of its vertices are consecutive. Indeed the union of the three deleted-neighborhood pairs covers at most five indices exactly when their index set has one or two cyclic runs. The missing triangles are exactly the independent three-subsets of the cycle \(C_n\). Their number is \(n(n-4)(n-5)/6\), obtained by a standard circular-gap count, giving \(f_2=\binom n3-n(n-4)(n-5)/6=n(n-3)\). A four-element face must be a run of four consecutive indices; these produce exactly \(n\) tetrahedra. There are no five-element faces, since any proper nonempty selected set of size five has at least one run, hence coverage at least six. Thus the nonempty face counts are
\[
(f_0,f_1,f_2,f_3)=\left(n,\binom n2,n(n-3),n\right).
\]

**5. Eliminate three-cells.** The tetrahedron \(\{i,i+1,i+2,i+3\}\) has the triangular face \(\{i,i+1,i+3\}\), which belongs to no other tetrahedron when \(n\ge7\). These \(n\) distinct free-face pairs give elementary collapses onto a two-dimensional complex \(Z_n\). Hence \(Y_5\simeq Z_n\), and its integral homology vanishes above degree two.

**6. Simple connectivity.** Every edge of \(K_n\) can be homotoped, using triangles \(\{i,i+1,j\}\) with a consecutive pair, onto a path around the original cycle. Thus \(\pi_1(Y_5)\) is generated by the loop \(C_n\). That loop bounds the fan of triangles \(\{0,i,i+1\}\), for \(1\le i\le n-2\), all of which are faces of \(Y_5\). Therefore \(Y_5\) is simply connected. This argument takes place before the elementary collapses, so it is unaffected by which free tetrahedral triangles are removed.

**7. Identify the integral wedge.** Because \(Z_n\) is a connected, simply connected two-dimensional CW complex, its reduced integral homology is zero except possibly in degree two, where it is free abelian. Its reduced Euler characteristic is
\[
\widetilde\chi(Y_5)=n-\binom n2+n(n-3)-n-1=\frac{n(n-5)}2-1=q_n.
\]
Thus \(\widetilde H_2(Y_5;\mathbb Z)\cong\mathbb Z^{q_n}\). Choose maps from \(q_n\) two-spheres representing a basis under the Hurewicz isomorphism. Their wedge induces an isomorphism on integral homology; the simply-connected homological Whitehead theorem makes the map a homotopy equivalence. Hence \(Y_5\simeq\bigvee^{q_n}S^2\). In particular, the inclusion \(Y_4\hookrightarrow Y_5\) is zero on first homology, as the target first homology vanishes. This proves all three homotopy types and the asserted inclusion-map properties.

## Verification
The standalone standard-library Python program `checks/verify.py` independently constructs the bipartite adjacency sets, intersects actual open neighborhoods for every nonempty shore subset, and enumerates the full faces for all three thresholds and each \(7\le n\le11\). It checks the exact face-count formulas, all nonzero reduced Betti ranks over \(\mathbb F_2\) using boundary-matrix elimination, the diagonal unique-coface condition, and the mod-two status of the original cyclic first-homology class at the second and third stages. Its recorded result is `checks/verification_output.txt`, ending with `CYCLIC_MULTINEIGHBOR_THREE_STAGE_OK`. Invoke `python3 checks/verify.py` at the root of this package. The integer and all-parameter conclusions rely on Steps 1–7, not on extrapolation from the finite calculations.

## Relationship to prior work
Matysiak and Spaliński (2023) define the multineighbor filtration and analyze its asymptotic topology for random graphs, with a complete-graph example. That construction is used here without claiming it as new. The present exact deterministic three-stage homotopy and integral inclusion-map classification for a Hamiltonian-cycle-deleted biclique is not among those results. A published classification for the **closed-neighborhood complex** of the same graph has different faces: it includes each center vertex in its neighborhood and has no witness-threshold parameter. An independent classification for the **independence complex** of a cyclic-band biclique also concerns a different complex and does not determine the multineighbor filtration. None of these statements implies the three displayed stages or their inclusion maps. The comparisons are about the precise definitions and results, rather than absence of matching titles.

## Limitations
The homotopy and persistence classification treats only \(m=n-3,n-4,n-5\) for \(n\ge7\). No statement about later-stage persistence endpoints, equivariant homotopy, or arbitrary deleted two-factors is proved. No positive threshold admits a mixed-shore face, but this does not imply two connected components at every threshold: at \(m=n-2\), all \(2n\) vertices are isolated, since every vertex has degree \(n-2\) and every same-shore pair has at most \(n-3\) common neighbors. For \(m>n-2\) there are no vertices in the complex. Finite-field computations do not certify the integral claims; these follow from the explicit collapses and the simply-connected two-dimensional argument. Unindexed equivalent results cannot be ruled out.

## References
- Wojciech Matysiak and Jan Spaliński, *The asymptotic topology of the multineighbor complex of a random graph*, arXiv:2302.09017v1, first public 2023-02-17, Sections 1–5. https://arxiv.org/html/2302.09017v1
- *Periodic sphere wedges in closed-neighborhood complexes of cycle-deleted complete bipartite graphs*. https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-periodic-sphere-wedges-in-closed-neighborhood-complexes-of-cycle--7e09d423324e
- *Cyclic-band bipartite independence complexes collapse to a two-sphere*. https://github.com/Resultary/2026/tree/main/2026/11/1/SCOPE-cyclic-band-bipartite-independence-complexes-collapse-to-a-two-s--6e43077a0a25
