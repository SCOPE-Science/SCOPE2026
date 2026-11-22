# Mixed-dimensional integral homotopy of general-position complexes of double-spider trees

## Finding
Consider a finite tree with exactly two adjacent branching hubs and arbitrary positive-length arms. The simplicial complex of vertex sets containing no three points on one graph geodesic has a uniform integral sphere-wedge homotopy type. For integers \(p,q\ge2\), arm lengths \(a_i,b_j\ge1\), and
\[
N=\sum_{i=1}^{p}a_i+\sum_{j=1}^{q}b_j,\qquad
\alpha=\prod_{i=1}^{p}(a_i-1),\qquad
\beta=\prod_{j=1}^{q}(b_j-1),\qquad
E=N+1+\sum_{i=1}^{p}\binom{a_i}{2}+\sum_{j=1}^{q}\binom{b_j}{2},
\]
there is a homotopy equivalence
\[
\boxed{|\mathcal{GP}(T)|\simeq
\bigvee^{E}S^1\ \vee\ \bigvee^{\alpha}S^p\ \vee\ \bigvee^{\beta}S^q\ \vee\ \bigvee^{\alpha\beta}S^{p+q-1}.}
\]
All integral reduced homology groups are free. Zero multiplicities are omitted; when any displayed sphere dimensions coincide, their multiplicities are added. In particular, the two-hub family admits nonzero homology in four distinct positive degrees: choosing \((p,q)=(2,3)\) with all five arm lengths equal to two gives ranks \(16,1,1,1\) in degrees \(1,2,3,4\), respectively.

## Assumptions and scope
The graph \(T\) is a finite, simple, unweighted, undirected tree. Two designated adjacent vertices \(u,v\) are its only vertices of degree at least three; \(u\) has \(p\) path arms and \(v\) has \(q\) path arms, disjoint except at their own hub. Every arm length is a positive integer counting edges, and therefore each non-hub arm contains precisely \(a_i\) or \(b_j\) vertices. Distinct vertices \(x,y,z\) lie on a common geodesic if one lies on the unique shortest path between the other two. The abstract simplicial complex \(\mathcal{GP}(T)\) contains every vertex subset with no such triple, including the empty face. The geometric realization uses its usual CW topology.

For a nonempty finite set \(A\), let \(D(A)\) denote its zero-dimensional simplicial complex (all singleton faces and the empty face). For simplicial complexes on disjoint vertex sets, \(*\) denotes simplicial join; \(x*K\) denotes a cone from a new vertex \(x\). Let \(A_1,\ldots,A_p\) be the vertex sets of the paths attached to \(u\), excluding \(u\), and similarly \(B_1,\ldots,B_q\) for \(v\). Define \(J_U=*_{i=1}^p D(A_i)\) and \(J_V=*_{j=1}^q D(B_j)\), and \(J=J_U*J_V\). Both \(J_U\) and \(J_V\) are nonempty and connected because each joins at least two nonempty discrete complexes.

## Proof
**1. Exact face classification.** Every one- or two-vertex set is in general position. A face of cardinality at least three containing neither hub can contain at most one vertex from each arm: choosing two vertices on a common arm and a third vertex anywhere places the nearer selected arm vertex between the farther one and the third (or places the three in order if all are on one arm). Conversely, choosing at most one from each arm avoids every geodesic triple, so all such faces form \(J\).

Suppose a face of cardinality at least three contains \(u\). If it also contained a vertex of an arm attached to \(u\), then any third selected vertex would make a forbidden triple: on the same arm the nearer selected point separates the other two, while outside that arm \(u\) lies between the arm point and the third. If the face contained \(v\), then any third selected point would lie beyond either \(u\) or \(v\), again creating a forbidden triple. Thus its other vertices must lie in distinct arms attached to \(v\), and every such selection is valid since shortest paths between two of them pass through \(v\) but not \(u\). The resulting high-dimensional faces form \(u*J_V\). By symmetry, those containing \(v\) form \(v*J_U\).

Consequently, setting
\[
Y=J\cup(u*J_V)\cup(v*J_U),
\]
all faces of cardinality at least three belong to \(Y\). The edges not already in \(Y\) are exactly: (i) the \(\sum_i\binom{a_i}{2}+\sum_j\binom{b_j}{2}\) pairs within a single arm; (ii) the \(N\) pairs joining a hub to a vertex in one of its **own** arms; and (iii) \(\{u,v\}\). Each is a maximal edge because its inclusion in a triple was ruled out. This gives exactly \(E\) additional edges attached to \(Y\) along their endpoints.

**2. The two cone attachments.** The subcomplex \(J_V\hookrightarrow J=J_U*J_V\) has nullhomotopic geometric inclusion: choose any vertex \(x\in J_U\), and the cone \(x*J_V\subseteq J\) contracts the inclusion. Likewise \(J_U\hookrightarrow J\) is nullhomotopic through the cone over any vertex of \(J_V\). Since these are finite simplicial CW-pair cofibrations, attaching the cones on \(J_V\) and \(J_U\) consecutively gives
\[
|Y|\simeq |J|\vee\Sigma|J_V|\vee\Sigma|J_U|.
\]
The second nullhomotopy persists in the intermediate space because it was already contained in \(J\). All complexes here are connected, and the wedge is taken at a common basepoint in their CW homotopy types.

**3. Joins of discrete sets.** For any nonempty finite sets of cardinalities \(m_1,\ldots,m_k\) and \(k\ge2\), induction using the join suspension identity proves
\[
\left|*_{h=1}^{k}D([m_h])\right|\simeq\bigvee^{\prod_h(m_h-1)}S^{k-1}.
\]
Indeed, joining a nonempty complex \(Z\) to a discrete \(m\)-point space is a union of \(m\) cones on \(Z\); if \(Z\) is connected, the result is a wedge of \(m-1\) suspensions of \(Z\). The base case \(k=2\) is the complete bipartite graph with \((m_1-1)(m_2-1)\) independent circles; factors of cardinality one make the join contractible, agreeing with the zero-multiplicity convention. Applied to the two arm joins, this gives \(|J_U|\simeq\bigvee^{\alpha} S^{p-1}\) and \(|J_V|\simeq\bigvee^{\beta}S^{q-1}\). Their join \(J\) is \(\bigvee^{\alpha\beta}S^{p+q-1}\). Substitution into step 2 gives the three families of higher-dimensional spheres.

**4. The extra edges.** The complex \(Y\) is path-connected because \(J\) is a join of two nonempty complexes and all its cones attach to nonempty subcomplexes. Attaching a single interval between any two vertices in a path-connected CW complex is, up to homotopy, wedge attachment of one circle: its attaching map \(S^0\to Y\) is homotopic to a constant map because the two endpoint images are path-connected. This remains valid after each edge, so the \(E\) missing maximal edges yield \(\bigvee^{E} S^1\). Together with the preceding decomposition, this proves the displayed homotopy equivalence with integral, not merely rational, consequences.

## Verification
The independently implemented standalone `verify_double_spider.py` reconstructs each graph and computes all graph distances by breadth-first search. It enumerates every vertex set, tests every forbidden geodesic triple, and compares the complete resulting face family to the structural classification derived in the proof. A separate simplicial boundary-matrix computation over \(\mathbb F_2\) compares the entire reduced Betti table against the formula. Replay with `python3 verify_double_spider.py` from the same directory. The saved `verification_output.txt` records a successful run across \(147\) parameter instances containing a total of \(28{,}556\) nonempty simplices. For two arms of length two at each hub, the calculated ranks are \(13\) in degree one, \(2\) in degree two, and \(1\) in degree three. For a two-arm and a three-arm hub, with all lengths two, they are \(16,1,1,1\) in degrees one through four. These finite computations corroborate the general homotopy proof, not replace it; the integral conclusion depends on the argument in the preceding section.

## Relationship to prior work
The graph-geodesic general-position polynomial introduced by Iršič, Klavžar, Rus and Tuite counts the complex's faces; Rather's 2026 study extends such enumeration to complete multipartite graphs, corona operations and related families. A published antichain expansion determines the full multivariate general-position polynomial for all trees. Those face-counting identities determine face numbers, not the integral homotopy type or the attachment maps in this particular two-hub family. A published exact integral homotopy classification of the general-position complex of complete bipartite coronas uses a similar gluing viewpoint, but its graphs contain cycles and its conclusion has no counterpart to the \(\alpha\beta\) sphere family at dimension \(p+q-1\). Other results on subdivided-star higher-independence or bidirected multipath complexes refer to different simplicial constructions and cannot imply this theorem just from matching tree shapes. Database searches for the double-spider statement, its join-cone formulation and aliases did not find coverage; absence in indexed records does not prove priority.

## Limitations
The two high-degree vertices must be adjacent; arms are internally disjoint simple paths, with at least two at each hub. The claim does not extend as stated to separated hubs, weighted graphs, graphs with extra edges or arbitrary trees with more branch points. The homotopy equivalence is not claimed canonical or equivariant under graph automorphisms. The checker tests finite cases and only mod-two homology; the full integral and higher-homotopy conclusions follow from the exact theoretical pushout proof. Equivalently phrased, unindexed earlier results remain a priority risk. Independent mathematical audit has not been performed.

## References
1. B. A. Rather, *Explicit Formulas and Unimodality Phenomena for General Position Polynomials*, arXiv:2603.06930v1, first posted 2026-03-06, https://arxiv.org/abs/2603.06930 .
2. V. Iršič, S. Klavžar, G. Rus, and J. Tuite, *General Position Polynomials*, arXiv:2401.05696v1, 2024-01-11, https://arxiv.org/abs/2401.05696 .
3. *An antichain expansion for general position polynomials of all trees*, publicly accessible research result, 2026-10-13.
4. *General position polynomials of spiders and the smallest nonunimodal spider*, publicly accessible research result, 2026-10-04.
5. *Mixed-dimensional integral homotopy of bipartite-corona general-position complexes*, publicly accessible research result, 2026-11-17.
