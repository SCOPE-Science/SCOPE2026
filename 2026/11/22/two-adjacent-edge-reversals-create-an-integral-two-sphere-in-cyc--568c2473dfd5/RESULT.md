# Two adjacent edge reversals create an integral two-sphere in cyclic tournament flag complexes

## Finding
For every integer \(m\ge2\), write \(n=2m+1\) and let \(R_n\) be the cyclic tournament with vertex set \(\mathbb Z/n\mathbb Z\) and arcs \(i\to i+j\) for \(1\le j\le m\). Reverse exactly the two arcs \(0\to1\) and \(d\to d+1\), where \(2\le d\le m\), to obtain the tournament \(T_{m,d}\). Its directed flag complex \(\operatorname{dFl}(T_{m,d})\)—the complex of vertex sets inducing transitive subtournaments—has **complete integral homotopy type**
\[
\operatorname{dFl}(T_{m,d})\simeq\begin{cases} S^2,&2\le d<m,\\ *,&d=m.\end{cases}
\]
In particular, every two-reversal configuration except the extremal separation creates one primitive integral two-dimensional homology generator, whereas the extremal pair is contractible. Both arcs have cyclic length one and are vertex-disjoint. The first sphere case occurs at \(n=7\). This is a theorem for all integers in the stated range, not a finite-range extrapolation.

## Assumptions and scope
All arithmetic on vertices is modulo \(n\), and \(*\) denotes a contractible nonempty space. A tournament has exactly one oriented arc between each pair. A vertex set is a face of the directed flag complex precisely when its induced tournament is acyclic/transitive. The two reversed arcs are \(\{0,1\}\) and \(\{d,d+1\}\); our range ensures they are distinct and disjoint.

Write \(K=\operatorname{dFl}(R_n)\), and define cyclic blocks \(B_i=\{i,i+1,\ldots,i+m\}\). A transitive subtournament has a unique source vertex \(i\), and all other vertices are among its next \(m\) out-neighbors; hence every face of \(K\) lies in some \(B_i\), and conversely each \(B_i\) is transitive. Thus the maximal faces of \(K\) are exactly these cyclic blocks.

## Proof
**1. The original circle and a primitive attaching loop.** The complex \(K\) is the nerve of the closed circular arcs \(A_i=[i/n,(i+m)/n]\subset\mathbb R/\mathbb Z\), each of length \(m/n<1/2\). Every nonempty finite intersection of these arcs is contractible, and the arcs cover the circle. Thus \(K\simeq S^1\) by the nerve theorem. A particularly useful subcover consists of \(A_i,A_{i+1},A_{i+m+1}\): the three arcs cover the same circle, meet pairwise, and have no common intersection. Their nerve is the three-edge loop on the vertices \(\{i,i+1,i+m+1\}\). Naturality of the nerve theorem gives a homotopy equivalence
\[
\partial\{i,i+1,i+m+1\}\hookrightarrow K.\tag{1}
\]
This proves not merely that the boundary is nontrivial, but that it represents a primitive generator of \(\pi_1(K)\cong\mathbb Z\) and \(H_1(K;\mathbb Z)\cong\mathbb Z\).

An entirely combinatorial confirmation is available: for every \(2\le s\le m\), let \(K_s\) be the complex with facets the cyclic consecutive blocks of length \(s+1\). The edge \(\{i,i+s\}\) occurs in a unique such block, and removing the pairs
\[
(\{i,i+s\}\cup B,\;\{i,i+1,i+s\}\cup B),\qquad B\subseteq\{i+2,\ldots,i+s-1\},
\]
in decreasing \(|B|\) gives an elementary collapse \(K_s\searrow K_{s-1}\). There are \(n(2^{m-1}-1)\) elementary collapses in total, leaving the \(n\)-cycle \(K_1\). This also gives an explicit integral circle model.

**2. Effect of one reversed arc.** Fix a length-one arc \(i\to i+1\). For any old transitive set containing both endpoints, these two vertices are consecutive in its transitive order, so reversing their mutual arc preserves transitivity. Exactly one cyclic triple becomes transitive: its vertices are
\[
\tau_i=\{i,i+1,i+m+1\}.
\]
For a third vertex in \(\{i+2,\ldots,i+m\}\) both endpoints point to it; for one in \(\{i+m+2,\ldots,i+2m\}\), it points to both, leaving only \(i+m+1\) as a cyclic third vertex originally. No larger face can contain \(\tau_i\), because a fourth vertex in the first range forms an unchanged directed triangle with \(\{i,i+m+1\}\), and one in the second range forms an unchanged directed triangle with \(\{i+1,i+m+1\}\). Consequently a single reversal produces precisely \(K\cup\tau_i\). This argument also proves that every face of \(K\) survives both of our disjoint reversals: each reversed pair is adjacent in every original transitive order containing it, and the two disjoint adjacent swaps commute.

**3. Effect of two disjoint reversed arcs.** A newly transitive triple can involve at most one of the disjoint reversed edges, so the only new triples are \(\tau_0=\{0,1,m+1\}\) and \(\tau_d=\{d,d+1,d+m+1\}\). Every new face of size at least four contains one of these two triples. A new four-face containing \(\tau_0\) must contain one of the endpoints of the second reversed arc; all other new faces containing \(\tau_0\) are ruled out by the preceding unchanged-triangle obstruction. For \(2\le d<m\), neither endpoint \(d,d+1\) equals \(m+1\), and each of them already lies in \(\{2,\ldots,m\}\), where the unchanged triple \(\{0,v,m+1\}\) is cyclic. Therefore no new four-faces occur. Interchanging the roles of the two arcs gives the same conclusion for \(\tau_d\). Hence
\[
\operatorname{dFl}(T_{m,d})=K\cup\tau_0\cup\tau_d\qquad(2\le d<m).\tag{2}
\]
Each two-simplex is attached along a homotopy equivalence \(S^1\to K\) by (1). Attaching the first makes a contractible subcomplex \(K\cup\tau_0\); attaching the second along its boundary then gives a space homotopy equivalent to \(S^2\). In particular its integral \(\widetilde H_2\) is \(\mathbb Z\), with no other reduced integral homology, and its fundamental group vanishes.

When \(d=m\), the extra three-simplex
\[
\eta=\{0,1,m,m+1\}
\]
is transitive: after both reversals its order is \(1\to m+1\to0\to m\). This is the only new face of size at least four: in the preceding argument the unique additional endpoint able to coexist with \(\tau_0\) is \(m\); applying the same test to \(\tau_m\) yields the same tetrahedron. The two new triangles are \(\tau_0\) and \(\tau_m\), both facets of \(\eta\), and the other two triangular faces of \(\eta\) already lie in \(K\). Since \(\tau_0\) belongs to no other tetrahedron or higher-dimensional face, it is a free facet of \(\eta\). The elementary collapse \((\tau_0,\eta)\) leaves exactly \(K\cup\tau_m\), which is contractible by (1). This proves the second case.

## Verification
A standalone Python 3 standard-library checker, `verify.py`, independently enumerates all transitive vertex subsets for every odd order \(5\le n\le15\), all \(2\le d\le m\), and tests the exact set identity (2) or its extremal counterpart with one extra tetrahedron. It exhaustively verifies every indicated elementary free-face pair in the cyclic-block collapse and separately computes reduced mod-two Betti numbers through \(n=11\). All 21 parameter cases passed; see `verification_output.txt`. The infinite-family theorem relies on the preceding combinatorial proof, not the finite checks.

## Relationship to prior work
Govc (2020) defined and analyzed directed flag complexes of tournaments, including finite regular-tournament census data. Govc–Levi–Smith (2021) developed directionality-filtered tournament complexes. Adamaszek–Adams–Frick–Peterson–Previte-Johnson (2014/2016) studied circular-arc nerves. A previously published *single*-adjacent-edge-reversal theorem proves \(K\cup\tau_i\) contractible; its inspected proof supplies a close ingredient, but no two-reversal interaction, separating-distance dichotomy, new 2-sphere, or exceptional tetrahedron. The present proof explicitly derives and distinguishes these additional incidences. Searches for two-reversal, arc-reversal, transitive-subtournament, cyclic-tournament, and directed-flag equivalents identified no covering statement in the inspected primary sources or indexed findings. This is a comparison of actual statements, not a guarantee that no unindexed equivalent result exists.

## Limitations
The reversed arcs are consecutive edges in the standard cyclic orientation and are vertex-disjoint; the theorem does not address long arcs, overlapping reversed arcs, or three or more reversals. The explicit \(S^2\) classification is a homotopy equivalence, not an asserted simplicial collapse onto a triangulated sphere or a computation of the symmetry action. The finite verifier is supplemental and tests only the stated finite range. Originality remains subject to unindexed literature and stronger undiscovered general theorems.

## References
1. Dejan Govc, *Computing Homotopy Types of Directed Flag Complexes*, arXiv:2006.05333, first public 9 June 2020. https://arxiv.org/abs/2006.05333
2. D. Govc, R. Levi and J. P. Smith, *Complexes of tournaments, directionality filtrations and persistent homology*, published online 19 April 2021, DOI:10.1007/s41468-021-00068-0. https://link.springer.com/article/10.1007/s41468-021-00068-0
3. M. Adamaszek, H. Adams, F. Frick, C. Peterson and C. Previte-Johnson, *Nerve complexes of circular arcs*, arXiv:1410.4336. https://arxiv.org/abs/1410.4336
4. *A single adjacent reversal contracts the cyclic tournament flag complex*, published-finding corpus, 4 October 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-a-single-adjacent-reversal-contracts-the-cyclic-tournament-flag--8f4d1ced82e2
