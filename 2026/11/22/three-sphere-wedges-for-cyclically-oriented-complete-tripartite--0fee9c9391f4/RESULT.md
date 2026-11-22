# Three-sphere wedges for cyclically oriented complete tripartite digraphs with shores \(1,2,n\)

## Finding

For each integer \(n\ge5\), let \(D_n\) be the cyclically oriented complete tripartite digraph with vertex classes \(A=\{a\}\), \(B=\{b_0,b_1\}\), and \(C=\{c_0,\ldots,c_{n-1}\}\). Its directed arcs are all \(a\to b_i\), all \(b_i\to c_j\), and all \(c_j\to a\), with no other arcs. Let \(X(D_n)\) be the simplicial complex on the arcs, whose faces are arc subsets that are vertex-disjoint unions of directed simple paths (isolated digraph vertices are allowed).

**Theorem.** For every \(n\ge5\) there is an integral homotopy equivalence

\[
X(D_n)\simeq\bigvee^{\,n^3-6n^2+8n-1} S^3.
\]

In particular its reduced integral homology is free of rank \(n^3-6n^2+8n-1\) in degree three and zero in all other degrees. This is an actual homotopy classification, not an extrapolation from finite Betti numbers. The lower boundary is meaningful: at \(n=4\), an independent exact mod-two chain calculation gives nonzero second homology of dimension two, so the asserted three-sphere-only pattern does not extend there.

## Assumptions and scope

All digraphs are finite and simple. A multipath means a collection of directed simple paths with pairwise disjoint vertex sets. Equivalently, in an arc subset each digraph vertex has indegree and outdegree at most one, and there is no directed cycle. The complex is *not* a directed flag complex, path homology complex, matching complex of the underlying undirected graph, or a complex on subsets of digraph vertices.

Use notation \(u_i=(a,b_i)\), \(v_{ij}=(b_i,c_j)\), and \(w_j=(c_j,a)\). Put \(W=\{w_0,\ldots,w_{n-1}\}\) and let \(E_n\) be the zero-dimensional simplicial complex with vertex set \(W\). Let \(\Gamma_n\) be the graph whose vertices are the \(2n\) arcs \(v_{ij}\), and whose edges join \(v_{0j}\) to \(v_{1k}\) exactly when \(j\ne k\). Thus \(\Gamma_n\) is the crown graph \(K_{n,n}\) minus its diagonal matching. This is the **one-dimensional** matching complex of the complete bipartite graph with two source vertices and \(n\) target vertices.

For \(i\in\{0,1\}\), put \(\Gamma_{ij}=\Gamma_n-v_{ij}\) (vertex deletion). Let
\[
K_0=\Gamma_n*E_n,\qquad
L_i=\Gamma_n\cup\bigcup_{j=0}^{n-1}\bigl(w_j*\Gamma_{ij}\bigr).
\]

All spaces in the proof are geometric realizations of these finite simplicial complexes. The star notation \(*\) denotes a simplicial join with a new vertex or with a discrete complex.

## Proof

**1. Exact face decomposition.** An allowed arc subset contains at most one \(u\)-arc and at most one \(w\)-arc. Its \(v\)-arcs form a bipartite matching of cardinality at most two. The only possible directed cycles are the three-arcs \(u_i,v_{ij},w_j\): any directed cycle must pass through the sole vertex \(a\), then a vertex of \(B\), then a vertex of \(C\), and return to \(a\). Hence the allowed subsets without a \(u\)-arc form exactly \(K_0\), while those containing \(u_i\) form the cone \(u_i*L_i\). Since \(u_0\) and \(u_1\) cannot occur together,
\[
X(D_n)=K_0\cup (u_0*L_0)\cup(u_1*L_1),
\]
where the two cones intersect one another inside \(K_0\) only, and the attachment of each cone to \(K_0\) is its full base \(L_i\).

**2. Four-cycles generate the cycle group of the crown graph integrally, and normally generate its fundamental group.** For \(n\ge4\), \(\Gamma_n\) is connected. Every closed walk can be reduced to simple cycles and every simple cycle with a chord splits into shorter cycles. An induced simple cycle of length \(2r\) has \(r\le3\): each of its left-side vertices is required to miss \(r-2\) right-side nonneighbors in the crown graph, but has exactly one such nonneighbor in the entire opposite shore. Thus the only induced cycles have lengths four or six. An induced six-cycle has its three left and three right vertices indexed by the same three labels \(p,q,r\). Choose a fourth label \(s\) outside this set. The six-cycle is the boundary of a disk of three four-cycles, using the new left-side vertex \(v_{0s}\) and the three old right-side vertices: the three square faces are the cycles on left pairs \(\{p,s\}\), \(\{q,s\}\), and \(\{r,s\}\) with the respective complementary pairs of right labels. The three squares share and cancel their interior edges. Consequently every integral one-cycle is a signed sum of four-cycles. The same chord-splitting and disk fillings show that the four-cycle loops normally generate \(\pi_1(\Gamma_n)\).

**3. Simple connectivity.** The join \(K_0=\Gamma_n*E_n\) is simply connected for \(n\ge4\), since \(\Gamma_n\) is connected and \(E_n\) is a nonempty discrete set with at least two points. Each \(\Gamma_{ij}\) is connected, so attaching cones to them cannot create fundamental-group generators. Every four-cycle of \(\Gamma_n\) uses only two left and two right labels. For each fixed shore \(i\), choose an unused label \(j\); that four-cycle lies in \(\Gamma_{ij}\), and is nullhomotopic in the cone \(w_j*\Gamma_{ij}\subseteq L_i\). Step 2 therefore gives \(\pi_1(L_i)=0\), and in particular \(H_1(L_i;\mathbb Z)=0\). Attaching \(u_0*L_0\) and \(u_1*L_1\) along their connected bases to the simply connected \(K_0\) yields \(\pi_1(X(D_n))=0\) by van Kampen.

**4. The integral inclusion map onto second homology is surjective for \(n\ge5\).** Give each graph edge of \(\Gamma_n\) an arbitrary fixed orientation and write \(Z_1(\Gamma_n;\mathbb Z)\) for its integral cycle lattice. There are no three-simplices in \(K_0\). By writing a two-chain as a tuple of cones over graph one-chains, the explicit simplicial boundary gives
\[
H_2(K_0;\mathbb Z)=\left\{(z_j)_{j=0}^{n-1}: z_j\in Z_1(\Gamma_n;\mathbb Z),\quad\sum_j z_j=0\right\}.
\]
Similarly the image of \(H_2(L_i;\mathbb Z)\to H_2(K_0;\mathbb Z)\) is exactly the subgroup of such tuples satisfying \(z_j\in Z_1(\Gamma_{ij};\mathbb Z)\) for each \(j\). No torsion or coefficient-field reduction is used in these identities.

The first displayed group is generated over \(\mathbb Z\) by tuples with a fixed four-cycle \(z\), coefficient \(+1\) at one index \(j\), coefficient \(-1\) at a different index \(k\), and zero elsewhere: use the integral four-cycle generation in Step 2 and the elementary presentation of the augmentation lattice of the \(n\)-element set.

Write \(P\) for the two left labels and \(Q\) for the two right labels of this four-cycle. All four cross edges are present, so \(P\cap Q=\varnothing\). If \(j,k\notin P\), the generator lies in the image from \(L_0\); if \(j,k\notin Q\), it lies in the image from \(L_1\). The only remaining case, up to exchanging \(j,k\), has \(j\in P\) and \(k\in Q\). Since \(n\ge5\), choose \(h\notin P\cup Q\). Split the desired generator as the sum of \((e_j-e_h)\otimes z\) and \((e_h-e_k)\otimes z\). The former belongs to the image from \(L_1\), while the latter belongs to the image from \(L_0\). Thus
\[
H_2(L_0;\mathbb Z)\oplus H_2(L_1;\mathbb Z)\longrightarrow H_2(K_0;\mathbb Z)
\]
is integrally surjective. The relative long exact sequence of the two cone attachments and the already proved vanishing of \(H_1(L_0)\) and \(H_1(L_1)\) imply \(\widetilde H_2(X(D_n);\mathbb Z)=0\).

**5. Rank and homotopy type.** All faces contain at most four arcs, so \(X(D_n)\) has dimension three. Direct counting from the join-and-two-cones decomposition gives the face vector
\[
(f_0,f_1,f_2,f_3)=\bigl(3n+2,\;3n^2+5n,\;n^3+5n^2-4n,\;2n(n-1)^2\bigr).
\]
For example, each cone contributes \(n(n-1)\) triangle faces through its base graph edges, \(n(2n-1)\) through its base vertices adjacent to the \(w\)-arcs, and \(n(n-1)^2\) tetrahedra. The reduced Euler characteristic is
\[
\widetilde\chi(X(D_n))= -n^3+6n^2-8n+1.
\]
Since \(X(D_n)\) is simply connected, has vanishing second integral homology, and has no cells in dimension above three, its only positive reduced homology is free third homology of rank \(n^3-6n^2+8n-1\). Simple connectivity and the integral Hurewicz theorem give \(\pi_2=0\) and \(\pi_3\cong H_3\). Represent a basis by maps of three-spheres and wedge those maps. This gives a homology equivalence from the indicated wedge to \(X(D_n)\), and hence a homotopy equivalence by the homological Whitehead theorem for simply connected CW complexes. This proves the theorem for every integer \(n\ge5\).

## Verification

The standalone `verify.py` independently constructs all directed arcs, enumerates all candidate subsets up to size four, rejects subsets violating directed in/out degree or containing a directed cycle, and compares the resulting faces to the separate crown-graph/cone construction. It computes exact ranks of mod-two simplicial boundary maps (not floating-point ranks). For \(n=3,4,\ldots,10\), both generators agree in every face, the face-polynomial predictions agree, and for each \(n\ge5\) the mod-two Betti vector is \((1,0,0,n^3-6n^2+8n-1)\). The recorded output is `verification_output.txt`.

The computations are finite cross-checks, not the justification of the infinite-family conclusion. Steps 2–5 establish the necessary integral cycle-lattice and homotopy statements without appeal to finite experimentation. At the excluded parameter \(n=4\), the independent mod-two Betti vector is \((1,0,2,1)\).

## Relationship to prior work

Caputi, Collari, Di Trani and Smith defined the multipath complex and determined homotopy types for several directed graph classes, including alternating complete bipartite graphs and transitive tournaments, in their work first publicly posted August 9, 2022. They do not classify cyclic orientations of complete tripartite graphs with shore sizes \((1,2,n)\). The earlier paper by Caputi, Collari and Di Trani develops the path-poset interpretation and realizability, including wedge-of-spheres constructions, without determining this concrete natural cyclic blow-up family. Related indexed results on *fully bidirected* complete bipartite graphs concern different arc sets and allowed cycles; a result on the cyclically oriented octahedral graph addresses shore sizes \((2,2,2)\), and a directed path-homology blow-up invariance result concerns a different homology functor. Neither implies the formula or its sharp stable range for the present multipath complex.

The core distinction is that the present theorem treats a *strongly cyclic* three-layer orientation and yields an exact integer homotopy type for all \(n\ge5\), by analyzing a crown-graph cycle lattice and two interacting cone attachments. No claim of universal uniqueness or priority beyond the inspected evidence is made.

## Limitations

The classification is for the specified shore sizes and orientations, not for general complete tripartite orientations or bidirected graphs. It says nothing about equivariant actions or the exact homotopy types for \(n=2,3,4\). The independent boundary calculation for \(n=4\) is mod-two only; no integral or homotopy classification of that excluded complex is asserted. Scholarly indexing and full-text availability can be incomplete; unindexed equivalent results remain possible. Independent mathematical audit has not been performed.

## References

1. L. Caputi, C. Collari, S. Di Trani, J. P. Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656, first version publicly posted 2022-08-09; later *Mathematika* 70 (2024), e12235. https://arxiv.org/abs/2208.04656
2. L. Caputi, C. Collari, S. Di Trani, *Combinatorial and topological aspects of path posets, and multipath cohomology*, first publicly available before 2023, *Journal of Algebraic Combinatorics* 57 (2023), 617–658. https://doi.org/10.1007/s10801-022-01180-9
