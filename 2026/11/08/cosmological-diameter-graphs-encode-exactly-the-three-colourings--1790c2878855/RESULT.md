# Cosmological diameter graphs encode exactly the three-colourings of their source graphs

## Finding
Let \(G=(V,E)\) be any finite connected simple graph with \(n=|V|\ge2\) and \(m=|E|\ge1\). Equip \(\mathbb R^{V\sqcup E}\) with the Euclidean metric in which the standard coordinate vectors are orthonormal. For each edge \(f=\{u,v\}\), define
\[
 t_f=e_u+e_v-e_f,\qquad
 a_{f,u}=-e_u+e_v+e_f,\qquad
 a_{f,v}=e_u-e_v+e_f,
\]
and the cosmological polytope
\[
 C_G=\operatorname{conv}\{t_f,a_{f,u},a_{f,v}:f=\{u,v\}\in E\}.
\]
Its **diameter graph** \(\mathcal D_G\) has the \(3m\) source vertices as vertices and an edge between two distinct points exactly when their Euclidean distance is the diameter of \(C_G\). This is *not* the one-skeleton of the polytope.

**Theorem.** The Euclidean diameter of \(C_G\) is \(2\sqrt2\). The graph \(\mathcal D_G\) has exactly
\[
3m+4\sum_{v\in V}\binom{\deg_G(v)}2
\]
edges, has clique number exactly three, and admits a canonical bijection between its proper labelled three-colourings and the proper labelled three-colourings of \(G\). Equivalently, if \(P_H(k)\) denotes the chromatic polynomial of a graph \(H\), then
\[
\boxed{P_{\mathcal D_G}(3)=P_G(3).}
\]
In particular, \(\mathcal D_G\) is three-colourable if and only if \(G\) is. Recognizing three-colourability among graphs presented as the diameter graphs of standard cosmological polytopes of connected simple graphs is NP-complete. Every such diameter graph is \(K_4\)-free, despite this hardness.

## Assumptions and scope
The graph is finite, connected, simple and nontrivial; the coordinate basis \(\{e_v:v\in V\}\cup\{e_f:f\in E\}\) is orthonormal. The theorem applies to the stated affine lattice realization, not to an arbitrary affine or projective image. It uses labelled colours \(\{1,2,3\}\), not colourings modulo permutation. An isolated vertex of \(G\) produces no source point; connectedness excludes that ambiguity. In the standard model all \(3m\) points listed above are distinct extreme points: for an edge \(f\), the vertex \(t_f\) uniquely minimizes the \(e_f\)-coordinate, while the two vertices with \(e_f\)-coordinate \(+1\) can each be exposed with a small perturbation in the \(e_u-e_v\) direction.

## Proof
**1. Exact distances and the diameter.** Every displayed point \(p\) has \(\|p\|^2=3\) and coordinate sum \(\sum_{i\in V\sqcup E}p_i=1\). Two different points belonging to the same edge-triple have inner product \(-1\), hence squared distance \(3+3-2(-1)=8\). For points belonging to distinct source edges \(f\ne g\), simplicity implies that either \(f\cap g\) is empty (inner product zero, squared distance six), or they share exactly one endpoint \(v\). In the latter case the inner product is the product of the two coordinate signs at \(v\), namely \(+1\) or \(-1\), giving squared distance four or eight, respectively. No greater squared distance occurs, and every edge-triple realizes eight. As the distance between two points in a convex hull is bounded above by the maximum distance between its vertices (successive convexity of the norm), \(\operatorname{diam}(C_G)=\sqrt8\).

This calculation also identifies every diameter edge: within each three-point source-edge triple every pair is diametral; between two distinct source edges incident at \(v\), precisely the pairs with opposite coordinate signs at \(v\) are diametral. No disjoint source-edge pair is diametral. Each edge-triple contributes three pairs. At a fixed common endpoint, in each triple two points have sign \(+1\) and one has sign \(-1\), producing \(2\cdot1+1\cdot2=4\) diametral pairs for each unordered pair of distinct incident source edges. The incidence intersection is unique for a simple graph, so there is no double counting. This proves the edge-count formula.

**2. No four-cliques.** Suppose four distinct source vectors \(p_1,\ldots,p_4\) form a clique in \(\mathcal D_G\). Then \(\langle p_i,p_j\rangle=-1\) for \(i\ne j\) and \(\|p_i\|^2=3\), so
\[
\left\|\sum_{i=1}^4p_i\right\|^2=4\cdot3+2\binom42(-1)=0.
\]
Their vector sum would be zero, contradicting the fact that its total coordinate sum is four. Hence \(\omega(\mathcal D_G)\le3\). Any source-edge triple is a three-clique, giving equality.

**3. From a diameter-graph colouring to a source-graph colouring.** Fix a proper map \(\phi:V(\mathcal D_G)\to\{1,2,3\}\). Every edge-triple is a triangle and therefore uses all three colours. For a source vertex \(v\) and an incident edge \(f\), write \(a_{f,v}\) for the unique member of the \(f\)-triple with negative \(v\)-coordinate. If \(f\ne g\) are both incident at \(v\), the point \(a_{f,v}\) is diametral to *both* members of the \(g\)-triple with positive \(v\)-coordinate. Those two positive members have distinct colours because they are in a triangle. Consequently \(\phi(a_{f,v})\) must equal the third colour \(\phi(a_{g,v})\). Thus \(c_\phi(v)=\phi(a_{f,v})\) is independent of the choice of incident \(f\). For each source edge \(f=\{u,v\}\), the two points \(a_{f,u}\) and \(a_{f,v}\) belong to the same diameter triangle, so \(c_\phi(u)\ne c_\phi(v)\). Hence \(c_\phi\) is a proper three-colouring of \(G\).

**4. Conversely, with exact inverse.** For any proper labelled three-colouring \(c:V\to\{1,2,3\}\), colour the source-edge triple for \(f=\{u,v\}\) by
\[
\phi_c(a_{f,u})=c(u),\qquad
\phi_c(a_{f,v})=c(v),\qquad
\phi_c(t_f)=\{1,2,3\}\setminus\{c(u),c(v)\},
\]
where the last expression means its unique element. The three colours on each source-edge triple are distinct. For two distinct source edges meeting at \(v\), all diameter edges connect a point with negative \(v\)-coordinate (which has colour \(c(v)\)) to one with positive \(v\)-coordinate (whose colour is different from \(c(v)\)); thus \(\phi_c\) is proper on the entire diameter graph. The constructions in parts 3 and 4 are mutually inverse because each source-edge triple uses all three colours. This proves the canonical bijection and the chromatic-polynomial equality at three.

**5. Complexity.** The explicit \(3m\)-point integer coordinate list and the diameter adjacency list can both be constructed from \(G\) in polynomial time. Three-colourability belongs to NP for the displayed diameter graph. Ordinary graph three-colourability is NP-complete even restricted to connected simple graphs: from an arbitrary input, connect its components by bridge edges (each component's three colour labels may be permuted independently to satisfy the bridges). The equivalence just proved is therefore a polynomial many-one reduction. The \(K_4\)-free property from part 2 holds in the output class.

## Verification
The included standalone `verify.py` uses only Python's standard library and integer arithmetic. It checks every connected labelled simple graph on two through five vertices (771 graphs): all pairs of polytope source vertices have squared distance in \(\{4,6,8\}\); their squared-distance-eight adjacency is exactly the stated incidence/sign relation; the edge-count formula holds; and no four-vertex clique exists. For all connected labelled graphs through four vertices, the program independently enumerates proper three-colourings of the source graph and the diameter graph and compares their counts. The full run completed 2,627,773 assertions. The proof above, not this bounded enumeration, establishes the result for all finite connected simple graphs.

To reproduce: `python3 verify.py` from the same directory as this document. The program should print `PASS: 2627773 assertions for 771 connected labeled graphs, 2 <= n <= 5.`

## Relationship to prior work
Arkani-Hamed, Benincasa and Postnikov introduced the graph-to-polytope construction; Kühne and Monin established detailed face and ordinary one-skeleton descriptions. Donzelmann, Juhnke, Rednoß and Thäle (2026) study asymptotic random ordinary *polytope-edge counts* and triangulation edges, not longest-distance pairs or colourings of the Euclidean diameter graph. Birkemeyer, Donzelmann, Fink and Juhnke (2026) analyze canonical forms and duals. A relevant prior published geometric calculation, *Every connected cosmological polytope has graph-independent Euclidean circumradius* (2026), shows all the standard source vertices belong to one minimum enclosing sphere and explicitly leaves the pairwise distance spectrum uncomputed. Its circumradius statement does not imply the present diameter adjacency classification or the three-colouring equivalence: equidistance to a sphere centre leaves pairwise vertex distances unconstrained.

The present result specifically concerns *maximum Euclidean-distance edges*, not the polytope's ordinary graph edges or the graph's shortest-path diameter. The local colour-propagation mechanism is not obtained merely from the fact that the norm of every source vector equals \(\sqrt3\).

## Limitations
The statements require the unaltered standard orthonormal coordinate metric. A generic linear transform can change the diameter graph. There is no claimed formula for arbitrary chromatic polynomial evaluations \(P_{\mathcal D_G}(k)\) with \(k\ne3\), nor for the polytope's edge graph or face lattice. The finite verifier is a check of examples, not a proof of the arbitrary-size theorem. Priority is provisional: an equivalent formulation in geometric graph colouring or in physics-related cosmological-polytope notes might exist without using the term "diameter graph". Independent mathematical assessment has not been performed.

## References
1. N. Arkani-Hamed, P. Benincasa, A. Postnikov, *Cosmological Polytopes and the Wavefunction of the Universe*, arXiv:1709.02813 (2017).
2. L. Kühne, L. Monin, *Faces of Cosmological Polytopes*, arXiv:2209.08069 (2022; full revised text 2024), https://arxiv.org/html/2209.08069v2.
3. A. Birkemeyer, T. Donzelmann, M. Fink, M. Juhnke, *On cosmological polytopes, their canonical forms and their duals*, arXiv:2603.03894v1 (2026-03-04), https://arxiv.org/html/2603.03894v1.
4. T. Donzelmann, M. Juhnke, B. Rednoß, C. Thäle, *Central limit theorems for high dimensional lattice polytopes: cosmological polytopes*, arXiv:2605.23371v1 (2026-05-22), https://arxiv.org/html/2605.23371v1.
5. *Every connected cosmological polytope has graph-independent Euclidean circumradius*, published-finding corpus mathematical record `2026/10/11/SCOPE-every-connected-cosmological-polytope-has-graph-independent-eucl--099bd090b126` (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-every-connected-cosmological-polytope-has-graph-independent-eucl--099bd090b126.
6. M. R. Garey, D. S. Johnson, L. Stockmeyer, *Some simplified NP-complete graph problems*, Theoretical Computer Science 1 (1976), 237–267 (standard hardness of three-colourability).
