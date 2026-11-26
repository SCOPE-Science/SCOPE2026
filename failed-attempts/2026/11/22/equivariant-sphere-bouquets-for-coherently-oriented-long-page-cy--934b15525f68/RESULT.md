# Equivariant sphere bouquets for coherently oriented long-page cycle books

## Finding
For integers \(n\ge2\) and \(\ell\ge4\), define a finite directed cycle book \(D_{\ell,n}\) as follows. Take two vertices \(s,t\), distinct branch vertices \(b_1,\dots,b_n\), and distinct common-path vertices \(c_1,\dots,c_{\ell-3}\). The arcs are
\[
s\to b_i,\quad b_i\to t\quad(1\le i\le n),\qquad
t\to c_1\to\cdots\to c_{\ell-3}\to s.
\]
Thus \(n\) distinct consistently oriented cycles of length \(\ell\) share the entire return path and no other arcs. Let \(X_{\ell,n}\) be the ordinary simplicial multipath complex, with arcs as vertices and directed linear forests as faces. The permutation group \(\mathfrak S_n\) fixes the common path and interchanges the branch indices.

**Theorem.** There is a \(\mathfrak S_n\)-equivariant homotopy equivalence
\[
X_{\ell,n}\simeq_{\mathfrak S_n}\bigvee_{i=1}^{n}S^{\ell-2},
\]
where the group permutes the summands with no orientation reversal. More precisely, the class of the oriented boundary of each forbidden cycle simplex yields an integral homology basis, so
\[
\widetilde H_{\ell-2}(X_{\ell,n};\mathbb Z)\cong\mathbb Z[\{1,\ldots,n\}]
\]
as the unsigned branch-permutation lattice, with every other reduced integral homology group zero.

For every subgroup \(H\le\mathfrak S_n\), write \(f_H\) for the number of branch indices fixed separately by all of \(H\), and \(o_H\) for its number of orbits on the branch indices. Then
\[
X_{\ell,n}^{H}\simeq\bigvee^{f_H}S^{\ell-2},\qquad
X_{\ell,n}/H\simeq\bigvee^{o_H}S^{\ell-2}.
\]
The superscript denotes the **geometric fixed-point space**, and the quotient is the **actual topological quotient**, not a quotient of graph labels. A zero-fold wedge means a point.

Adding one new branch induces the standard primitive split injection of integral top homology \(\mathbb Z^n\hookrightarrow\mathbb Z^{n+1}\), adding exactly one sphere class.

## Assumptions and scope
Each chosen arc set is a **multipath** precisely when every vertex has chosen indegree and outdegree at most one and there is no directed cycle. Isolated vertices are allowed. The complex is an ordinary finite abstract simplicial complex, realized geometrically. No reverse arcs, chords, loops or multiple arcs are present. The return path has \(k=\ell-2\) arcs; thus the total arc count is \(2n+k\). All homology and homotopy statements are integral, for all finite \(n\ge2\) and \(\ell\ge4\), and all subgroups, including trivial ones. The \(n=1\) boundary case is just the boundary of an \((\ell-1)\)-simplex and is used in the proof of fixed-space formulas.

## Proof
**1. Exact face classification.** Name the branch arcs \(p_i=s\to b_i\) and \(q_i=b_i\to t\); write \(R\) for the \(k\) return-path arcs. Every multipath contains at most one \(p\)-arc (all leave \(s\)) and at most one \(q\)-arc (all enter \(t\)). Every set satisfying these two restrictions is a multipath except the \(n\) full sets
\[
\sigma_i=\{p_i,q_i\}\cup R,\qquad 1\le i\le n,
\]
because exactly those sets contain a consistently directed cycle. In particular, all proper subsets of each \(\sigma_i\) are multipaths. For \(i\ne j\), the set \(\{p_i,q_j\}\cup R\) instead forms one directed path from \(b_j\) to \(b_i\), so it is admissible.

**2. A contractible filling with exactly \(n\) missing top cells.** Let \(B\) be the one-dimensional simplicial complex having vertices \(p_i,q_j\) and all mixed edges \(\{p_i,q_j\}\), including diagonal edges. Thus \(B=K_{n,n}\) as a simplicial graph, with the empty face included. Let \(\Delta_R\) be the full simplex on the \(k\) return arcs. The join
\[
J=B*\Delta_R
\]
is contractible, since it is a join with a nonempty simplex, and has dimension \(d=k+1=\ell-1\). By the exact face classification, \(X_{\ell,n}\subset J\) is obtained by removing only the interiors of the \(n\) distinct \(d\)-dimensional facets \(\sigma_i\). Their proper boundaries remain in \(X_{\ell,n}\). Thus the integral relative cellular chain complex has only one nonzero group, \(C_d(J,X_{\ell,n};\mathbb Z)=\mathbb Z^n\), with the \(\sigma_i\) as basis. The pair's long exact sequence and contractibility of \(J\) give
\[
\widetilde H_j(X_{\ell,n};\mathbb Z)=
\begin{cases}\mathbb Z^n,&j=d-1=\ell-2,\\0,&j\ne d-1.\end{cases}
\]
The connecting homomorphism carries the oriented missing simplex to the integral cycle \(\partial[\sigma_i]\). These boundaries therefore form a **primitive integral basis**. A branch permutation sends \(\partial[\sigma_i]\) to \(\partial[\sigma_{\pi(i)}]\) with positive sign if the vertex order is \(p_i,q_i,R\); hence the representation is exactly the integral permutation module.

**3. Ordinary homotopy type.** Since \(J\) is obtained from \(X_{\ell,n}\) by attaching cells in dimension \(d\ge3\), the inclusion induces an isomorphism of fundamental groups. Therefore \(X_{\ell,n}\) is simply connected. The homology calculation and successive Hurewicz theorems make it \((d-2)\)-connected. Wedge together the \(n\) embedded cycle-boundary spheres \(\partial\sigma_i\), identifying their common fixed vertex on \(R\) as basepoint and mapping each sphere to its boundary subcomplex in \(X_{\ell,n}\). This map induces an integral isomorphism on all homology groups and is a homotopy equivalence by the homological Whitehead theorem.

**4. All subgroup fixed spaces and equivariance.** Every simplex contains at most one \(p_i\) and one \(q_j\). Since the group preserves the two arc types, a simplex that is stabilized setwise by \(H\) can only contain branch arcs whose indices are individually fixed by \(H\). Consequently the geometric fixed-point space is the subcomplex on the return arcs and the branch arcs indexed by the \(f_H\) fixed indices. For \(f_H\ge1\), the preceding proof (also valid for one branch) gives a wedge of \(f_H\) spheres. For \(f_H=0\), the fixed complex is the contractible simplex \(\Delta_R\).

Let \(W=\bigvee_i\partial\sigma_i\) be the **abstract** wedge of the cycle-boundary spheres (the embedded copies may intersect in additional faces). The map \(W\to X_{\ell,n}\) just constructed is \(\mathfrak S_n\)-equivariant. On \(H\)-fixed spaces it is exactly the inclusion of the \(f_H\) surviving boundary spheres into the fixed subcomplex, an integral homology isomorphism by step 2, and hence a homotopy equivalence by step 3. If \(f_H=0\), both fixed spaces are contractible or a point, so it is again an equivalence. The equivariant Whitehead theorem for finite \(\mathfrak S_n\)-CW complexes now gives the asserted \(\mathfrak S_n\)-homotopy equivalence. Passing this equivariant homotopy equivalence to any subgroup quotient proves the \(o_H\)-sphere formula.

**5. Primitive maps under adding branches.** The contractible joins form inclusions preserving old branch arcs and the old \(R\). On relative top cellular homology, the missing facets \(\sigma_1,\ldots,\sigma_n\) map to the same named facets among \(\sigma_1,\ldots,\sigma_{n+1}\). By naturality of the connecting isomorphisms, the induced map on top integral homology is the coordinate inclusion, with free rank-one cokernel.

As a further exact check, the number of faces **including** the empty face is \((n+1)^2 2^{\ell-2}-n\): before excluding cycles the join contains \((1+2n+n^2)2^{\ell-2}\) faces, and each of the \(n\) forbidden facets removes exactly one.

## Verification
The accompanying standalone standard-library program `verify.py` independently constructs the directed graph and verifies the arc-set path-forest rule against the exact face classification for all \(36\) cases \(3\le\ell\le8\), \(1\le n\le6\). It separately computes mod-two boundary ranks and the face formula for \(24\) bounded cases and checks \(15\) subgroup-quotient and fixed-support cases, including several nontrivial subgroups of \(\mathfrak S_4\). Run `python3 verify.py`; matching recorded output is included as `verification_output.txt`. These finite checks corroborate the definitions and arithmetic. The all-parameter integral and equivariant homotopy assertions follow from the explicit relative-cell and Whitehead arguments, not from extrapolating finite computations.

## Relationship to prior work
Caputi, Collari, Di Trani and Smith (arXiv:2208.04656, publicly available 9 August 2022) develop the multipath-complex framework and classify coherently oriented **single polygons**, but not these books with multiple longer pages. The published equivariant **triangular**-book classification gives the one-common-arrow case \(\ell=3\), including fixed-space and quotient circles; that case is expressly excluded from the new theorem. Its theorem states no classification of nontriangular pages. The present classification addresses the naturally adjacent family with arbitrarily long **common return paths**, where the resulting spheres occur in higher degrees.

A known source-sink feedback-edge result identifies the top homology contributed by Hamiltonian return-edge cycles. For \(n\ge2\), deleting the final return arc from our graph gives a source-sink digraph with no Hamiltonian path traversing all the mutually incomparable branch vertices, so that theorem does **not** imply the lower-degree \(n\)-sphere decomposition or its equivariant structure. Caputi, Collari and Ramos (arXiv:2401.01248) compare multipath complexes to bipartite matching complexes for **acyclic** digraphs; the present cyclic books are outside that hypothesis. The 2026 work on **bidirected** polygons (arXiv:2601.05670) describes suspensions under a distinct local T-operation, not a theorem classifying these consistently oriented shared-return-path books. The distinct path-free complexes of Grinberg, Katthän and Lewis (arXiv:2102.07894) do not supply this multipath classification.

## Limitations
The classification prescribes **equal branch lengths of two arcs** and a common oriented return path, with no extra arcs or orientations. It does not classify arbitrary long-page books with unequal branch paths, bidirected pages, other common intersection patterns, or other directed homology theories. The equivariant equivalence is a homotopy statement, **not** a claim of equivariant elementary simplicial collapse. The proof uses standard relative CW topology, Hurewicz and Whitehead theorems; the finite verifier alone would not establish the integral infinite-family result. No claim of globally exhaustive bibliographic novelty is made.

## References
1. L. Caputi, C. Collari, S. Di Trani and J. P. Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656v1, first posted 9 August 2022, https://arxiv.org/abs/2208.04656.
2. *Equivariant collapse of consistently oriented triangular-book multipath complexes*, publicly indexed research result, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-equivariant-collapse-of-consistently-oriented-triangular-book-mu--991b20e6f7ab.
3. *Source–sink feedback edges split off Hamiltonian-path spheres in multipath complexes*, publicly indexed research result, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-source-sink-feedback-edges-split-off-hamiltonian-path-spheres-in--41ac0ad7443c.
4. L. Caputi, C. Collari and E. Ramos, *The weak categorical quiver minor theorem and its applications: matchings, multipaths, and magnitude cohomology*, arXiv:2401.01248v1, first posted 2 January 2024, https://arxiv.org/abs/2401.01248.
5. L. Caputi, C. Collari and J. P. Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670v1, first posted 9 January 2026, https://arxiv.org/abs/2601.05670.
6. D. Grinberg, L. Katthän and J. B. Lewis, *The path-missing and path-free complexes of a directed graph*, arXiv:2102.07894v1, first posted 15 February 2021, https://arxiv.org/abs/2102.07894.
7. W. Lück, *Survey on classifying spaces for families of subgroups*, arXiv:math/0312378, Theorem 1.6 (equivariant Whitehead theorem), https://arxiv.org/abs/math/0312378.
