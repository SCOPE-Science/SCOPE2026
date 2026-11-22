# First degree–Tutte twins in unicyclic graph-nilmanifold cohomology

## Finding

Let \(G\) range over finite connected simple unicyclic graphs: graphs with \(|E(G)|=|V(G)|\). Write \(N(G)\) for a compact Dani–Mainkar nilmanifold associated with \(G\), and let \(P_G(t)=\sum_{k\ge0}\dim_{\mathbb Q}H^k(N(G);\mathbb Q)t^k\) be its rational Poincaré polynomial. Consider pairs of **nonisomorphic** graphs with both the same multiset of vertex degrees and the same Tutte polynomial.

**Theorem.** Among connected unicyclic graphs with \(3\le |V(G)|\le6\), such pairs first occur on six vertices; there are exactly two unordered pairs, up to independent graph isomorphisms. In each pair the two Poincaré polynomials differ. Their complete Betti vectors and total Betti ranks are as follows, with \(k\) running from \(0\) to \(12\):

| Representative | \((b_0,b_1,\ldots,b_{12})\) | \(P_G(1)\) |
|---|---|---:|
| Triangle with a length-two pendant path and a leaf at a *different* triangle vertex, \(T_{\mathrm{path}}\) | \((1,6,28,76,157,238,268,238,157,76,28,6,1)\) | 1280 |
| Triangle with a pendant vertex bearing two leaves, \(T_{\mathrm{fork}}\) | \((1,6,28,75,160,249,282,249,160,75,28,6,1)\) | 1320 |
| Four-cycle with leaves at adjacent vertices, \(Q_{\mathrm{adj}}\) | \((1,6,29,76,157,238,266,238,157,76,29,6,1)\) | 1280 |
| Four-cycle with leaves at opposite vertices, \(Q_{\mathrm{opp}}\) | \((1,6,29,77,161,246,276,246,161,77,29,6,1)\) | 1316 |

Each pair has degree multiset \((1,1,2,2,3,3)\). For the triangular pair the common Tutte polynomial is \(x^3(x+x^2+y)\); for the four-cycle pair it is \(x^2(x+x^2+x^3+y)\). Thus even the *joint* degree-multiset and Tutte-polynomial data fail to determine total rational cohomology at the earliest unicyclic size admitting such twins.

## Assumptions and scope

All graphs are undirected, finite, simple and connected, and the range \(3\le |V(G)|\le6\) is **exhaustive** for the minimality statement. In the following edge lists the labelled vertex set is \(\{0,1,2,3,4,5\}\):

- \(T_{\mathrm{path}}\): \((0,1),(1,2),(0,2),(0,3),(3,4),(1,5)\).
- \(T_{\mathrm{fork}}\): \((0,1),(1,2),(0,2),(0,3),(3,4),(3,5)\).
- \(Q_{\mathrm{adj}}\): \((0,1),(1,2),(2,3),(0,3),(0,4),(1,5)\).
- \(Q_{\mathrm{opp}}\): \((0,1),(1,2),(2,3),(0,3),(0,4),(2,5)\).

For these six-vertex/six-edge graphs, the associated Lie algebra has dimension twelve. A compact nilmanifold exists using its integral structure constants. All homology/cohomology claims use rational coefficients. No assertion is made about integral cohomology or homeomorphism of the nilmanifolds.

## Proof

**1. Tutte polynomial and census.** A connected unicyclic graph on \(n\) vertices with unique cycle of length \(c\) has \(n-c\) bridge edges. Repeated bridge contraction in the Tutte deletion–contraction recurrence gives

\[
T_G(x,y)=x^{n-c}\bigl(y+x+x^2+\cdots+x^{c-1}\bigr).
\]

Hence at fixed \(n\), equality of Tutte polynomials is equivalent to equality of unique-cycle lengths. Enumerate every \(n\)-edge subset of the complete graph on \(n\) labelled vertices, for \(n=3,4,5,6\), discard disconnected graphs, and identify isomorphisms by the lexicographically minimal edge-bit signature under all \(n!\) vertex permutations. This exhausts all connected unicyclic graph isomorphism classes: there are respectively \(1,2,5,13\). Sorting each class by (unique-cycle length, sorted degree multiset) yields no collision up to five vertices and precisely two two-member collisions at six vertices, both with degree multiset \((1,1,2,2,3,3)\), at cycle lengths three and four. Direct canonical signatures identify the four edge lists above as the distinct representatives. The exhaustive program is provided in `checks/verify_unicyclic_six.py`.

**2. Cohomology model.** Given a graph with vertex generators \(u_0,\ldots,u_{n-1}\) and one edge generator \(v_{ab}\) for every edge \(a<b\), use the Chevalley–Eilenberg exterior differential graded algebra

\[
C^*(G)=\Lambda_{\mathbb Q}(u_i,v_{ab}),\quad
\mathrm du_i=0,\qquad \mathrm dv_{ab}=u_a\wedge u_b,
\]

extended by the signed graded Leibniz rule. The standard sign convention can also use a minus sign for all \(\mathrm dv_{ab}\), which gives an isomorphic cochain complex. The graph-Lie-algebra construction and Nomizu's theorem identify \(H^*(C^*(G))\) with \(H^*(N(G);\mathbb Q)\). To make exact elimination manageable, assign each generator its support on graph vertices: \(\operatorname{supp}(u_i)=\{i\}\) and \(\operatorname{supp}(v_{ab})=\{a,b\}\). The union of supports is unchanged by \(\mathrm d\), splitting the complex into finite rational blocks, without approximation.

**3. Exact ranks.** The full exterior basis consists of all \(2^{12}=4096\) generator subsets. In each support block and each degree, the provided checker constructs the signed sparse integer boundary matrix and computes its rank **over \(\mathbb Q\)** by exact rational elimination. If \(r_j\) denotes the total rank of \(\mathrm d:C^{j-1}\to C^j\), the resulting \((r_1,\ldots,r_{12})\) vectors are

| Graph | \((r_1,\ldots,r_{12})\) |
|---|---|
| \(T_{\mathrm{path}}\) | \((0,6,32,112,226,328,328,226,112,32,6,0)\) |
| \(T_{\mathrm{fork}}\) | \((0,6,32,113,222,321,321,222,113,32,6,0)\) |
| \(Q_{\mathrm{adj}}\) | \((0,6,31,113,225,329,329,225,113,31,6,0)\) |
| \(Q_{\mathrm{opp}}\) | \((0,6,31,112,222,324,324,222,112,31,6,0)\) |

With the conventions \(r_0=r_{13}=0\), rank-nullity gives the complete vectors in the theorem by

\[
b_k=\binom{12}{k}-r_k-r_{k+1}\qquad(0\le k\le12).
\]

The calculations explicitly verify \(\mathrm d^2=0\), Poincaré duality, and zero Euler characteristic in all four cases. Together with the exhaustive census, these computations prove the stated **finite** classification. They make no inference about graphs with more than six vertices.

## Verification

The standalone standard-library program `checks/verify_unicyclic_six.py` is executable with `python3 checks/verify_unicyclic_six.py`. The included `checks/verification_output.json` records its complete numerical output. The test computes canonical graph signatures and all exact rational ranks anew; expected outputs are used as assertive cross-checks, not as inputs to the algebra. In addition, the four Betti vectors were independently recomputed by a dense-matrix exact-rational implementation using a separate graph-atlas enumeration and matrix-rank library. That independent implementation is not a dependency of the standalone checker or of the theorem.

## Relationship to prior work

Aldi, Butler, Gardiner, Grandini, Lichtenwalner and Pan (2024) give the support decomposition for graph Chevalley–Eilenberg complexes and a **general degree-three** formula for all graphs; those general tools and any low-degree special consequences are not new here. Aldi and collaborators (first public 12 November 2026) determine complete Poincaré polynomials for **path** graphs and a general lower bound, but not the six-vertex unicyclic paired classification. The contribution here is the exhaustive *minimality under two standard graph invariants* together with the explicit complete degreewise rational cohomology of both pairs, and not the underlying differential or a generic method for computing Betti numbers.

Published literature and searchable mathematical findings were compared using graph-isomorphism and invariant aliases; none inspected states these four full polynomials and this sharp unicyclic two-pair cutoff together. This is not a proof of absolute priority: an unindexed table, an independently computed graph atlas, or a stronger unpublished formula could subsume the results.

## Limitations

The minimality statement is relative to the class of connected simple unicyclic graphs, not all simple graphs or all graph nilmanifolds. This is a finite, computationally exhaustive proof through six vertices, not a formula for arbitrary graph order. The theorem concerns **rational Betti numbers** only; it does not determine cup products, integral torsion, diffeomorphism type or automorphism representations. Computed exact matrix ranks and a published algebraic cohomology identification, rather than a new abstract graph cohomology theorem, support the classification. The result has not received independent mathematical auditing or definitive publication-priority certification.

## References

1. M. Aldi, S. Bevins, E. Chatzitheodoridis, S. Da Silva, Q. Frias, T. Mejía Gómez, *Poincaré polynomials of nilmanifolds associated with path graphs*, arXiv:2611.17014, first publicly submitted 2026-11-12. https://arxiv.org/abs/2611.17014
2. M. Aldi, A. Butler, J. Gardiner, D. Grandini, M. Lichtenwalner, K. Pan, *On the cohomology of Lie algebras associated with graphs*, arXiv:2402.14188, first publicly submitted 2024-02-22. https://arxiv.org/abs/2402.14188
The rational cohomology identification follows from Nomizu's theorem, as explained in Reference 2, Section 2.
