# Arbitrary-degree false positives in orbit-metric Vietoris–Rips persistence under free cyclic symmetry

## Finding
For every integer \(q\ge3\) and every integer \(m\ge2\), there is an explicitly defined finite metric space on \(2qm\) points with distances in \(\{0,1,2\}\), and a free isometric action of \(C_m\), for which the following hold at every inclusive Rips scale \(1\le r<2\):

\[
|\operatorname{VR}_{\le r}(X_{q,m})|/C_m\simeq \bigvee^{\,2q(q-2)+1}S^1,
\qquad
\operatorname{VR}_{\le r}(X_{q,m}/C_m)\cong (S^0)^{*q}\cong S^{q-1}.
\]

In particular, writing \(\mathcal B_r=EC_m\times_{C_m}|\operatorname{VR}_{\le r}(X_{q,m})|\) for the categorical filtered-groupoid (Borel) space, for **every coefficient field** \(\mathbb F\),
\[
H_{q-1}(\mathcal B_r;\mathbb F)=0,
\qquad
\widetilde H_{q-1}(\operatorname{VR}_{\le r}(X_{q,m}/C_m);\mathbb F)\cong\mathbb F.
\]
Thus the orbit-pseudometric Rips algorithm can create a spurious persistent homology class in **any prescribed degree at least two**, even while the group acts freely on the entire original Rips realization at that scale. There can be no universal higher-degree analogue of the one-sided degree-one non-overcount assertion in Alsulami's filtered-groupoid formulation.

More strongly, all its field-valued persistence intervals can be specified. Let \(b_q=2q(q-2)+1\), and let \(\mathbb F\) have characteristic zero or characteristic \(p>0\):

* For **categorical groupoid persistence** \(H_j(\mathcal B_r;\mathbb F)\), degree zero has one \([0,\infty)\) bar and \(2q-1\) copies of \([0,1)\). In degree one there are \(b_q\) copies of \([1,2)\) if \(\operatorname{char}\mathbb F\nmid m\) (including characteristic zero); if \(p\mid m\), there are \(b_q-1\) copies of \([1,2)\) and one \([1,\infty)\). In every degree \(j\ge2\), there are no bars if \(\operatorname{char}\mathbb F\nmid m\), and precisely one \([2,\infty)\) bar if \(p\mid m\).
* For **orbit-pseudometric Rips persistence**, degree zero has the same bars, and the only positive-degree bar is one \([1,2)\) in degree \(q-1\).

Here the statement \(\operatorname{char}\mathbb F\nmid m\) includes characteristic zero by convention. At \(r\ge2\), categorical groupoid persistence detects \(H_*(BC_m;\mathbb F)\), not necessarily the homology of a point.

## Assumptions and scope
Let \(A=\{0,1,\ldots,q-1\}\), \(I=\{0,1\}\), and \(S=\mathbb Z/m\mathbb Z\). Define \(X_{q,m}=A\times I\times S\). Construct an undirected simple graph \(\Gamma\) as follows: for every \(a<b\), every \(i,j\in I\), and every \(s\in S\), insert the edge
\[
\bigl\{(a,i,s),(b,j,s+1)\bigr\}.
\]
Assign the distance \(d(x,x)=0\), \(d(x,y)=1\) for a graph edge, and \(d(x,y)=2\) for every other distinct pair. This is a metric: its only nonzero values are 1 and 2, and therefore all triangle inequalities hold. The group \(C_m\cong S\) acts by translation in the last coordinate. The quotient metric is \(\overline d([x],[y])=\min_{g\in C_m}d(x,gy)\). Throughout, \(\operatorname{VR}_{\le r}\) uses inclusive pairwise distances; the distinction at endpoints is stated rather than inferred from alternative strict-radius conventions.

The finding is about a **genuine geometric quotient** and the **Borel construction**, contrasted with the distinct Rips complex of the quotient metric. No isomorphism of those complexes is presupposed. It is not a claim about arbitrary pseudometrics, approximate actions, or nonfree group actions.

## Proof
**1. Metric and symmetry.** The metric condition follows from \(d\in\{0,1,2\}\), because the only potentially constraining inequalities involve three distinct points and each right-hand distance is at most 2, while the sum of two positive distances is at least 2. Translation \(s\mapsto s+t\) preserves the edge rule, so is isometric and free on vertices.

**2. The first Rips stage is one-dimensional.** For \(1\le r<2\), the original Rips complex is the clique complex of \(\Gamma\). It has no triangles. Indeed, a putative triangle must have three different first coordinates \(a<b<c\); following its two ascending edges forces the sheet coordinates at these three points to be \(s,s+1,s+2\), whereas its long ascending edge forces the final coordinate to be \(s+1\). The contradiction \(1=0\) in \(\mathbb Z/m\mathbb Z\) is impossible for \(m\ge2\). Hence the clique complex is exactly the graph \(\Gamma\).

**3. Its free geometric quotient is a graph.** A nonidentity translation fixes no vertex and cannot interchange the two endpoints of any edge, because those endpoints have distinct first coordinates. Thus the group action on the entire graph realization is free. Every orbit of vertices has representative \((a,i)\). Every pair of distinct first-coordinate classes contributes exactly one orbit of edges joining the corresponding two representatives. There are no loops or parallel orbit edges. Therefore the geometric quotient is the complete \(q\)-partite graph with two vertices per part, denoted \(B=K_{2,2,\ldots,2}\). It has \(2q\) vertices and \(4\binom q2\) edges. As \(B\) is connected, its integral first Betti number is
\[
4\binom q2-2q+1=2q(q-2)+1=b_q.
\]
Every connected graph is homotopy equivalent to a wedge of its first-Betti-number circles. Since the action is free, the canonical map \(EC_m\times_{C_m}|\Gamma|\to|\Gamma|/C_m\) is a homotopy equivalence. This establishes the degree-\(\ge2\) categorical vanishing.

**4. The orbit metric creates false flag simplices.** For distinct quotient vertices \((a,i)\), \((b,j)\), their orbit distance is 1 exactly when \(a\ne b\); for \(a=b\) and \(i\ne j\), it is 2. Thus the Rips complex at \(1\le r<2\) is the clique complex of \(B\), which is the join of \(q\) discrete two-point spaces. The identity \((S^0)^{*q}\cong S^{q-1}\) follows by induction from \(S^d*S^0\cong\Sigma S^d\). Its top reduced integral homology is \(\mathbb Z\), in degree \(q-1\ge2\), establishing arbitrary-degree false positives without using a numerical extrapolation.

**5. All three scale ranges.** Below 1 the original Rips complex is a discrete set of \(2qm\) points with a free action; its Borel construction has \(2q\) contractible components. At \(1\le r<2\), the Borel construction is homotopy equivalent to \(B\) by Step 3. At \(r\ge2\), the original Rips complex is the full simplex, hence equivariantly contractible by straight-line contraction to the invariant barycenter. Its Borel construction is therefore homotopy equivalent to \(BC_m\), while the orbit-metric Rips complex is an ordinary simplex.

**6. Persistence maps and field dependence.** The graph \(\Gamma\) is connected. One way to see this is via the connected base graph \(B\) and the lifted closed walk around any triangle of \(B\) supported on three different parts. Starting from sheet \(s\), the oriented triangle lifts to a path ending on the same base vertex at sheet \(s+1\). This monodromy generates all of \(C_m\), so the regular covering \(\Gamma\to B\) is connected and its classifying homomorphism \(\pi_1(B)\to C_m\) is surjective. The transition map \(H_1(B;\mathbb F)\to H_1(BC_m;\mathbb F)\) in categorical persistence is exactly the induced classifying-map homomorphism, hence is surjective whenever the target is nonzero. The target homology is obtained from the standard 2-periodic cyclic-group resolution with alternating differentials \(g-1\) and \(1+g+\cdots+g^{m-1}\): after tensoring with the trivial field module, the differentials alternate between zero and multiplication by \(m\). Consequently, positive-degree homology of \(BC_m\) is one-dimensional in every degree when \(\operatorname{char}\mathbb F=p\mid m\), and zero otherwise. Combining these ranks with the maps from the discrete initial stage gives exactly the barcode formulas in the Finding section; degree-zero maps are determined by the component mergers, and all remaining positive-degree maps have source or target zero.

## Verification
Run the standalone, standard-library-only checker \(\texttt{python verify_voltage_graph.py}\). It enumerates all graph edges, asserts no triangle, checks free cyclic symmetry and edge preservation, constructs the geometric edge-orbit graph, verifies connectedness, calculates its cycle rank, counts every face of the orbit-distance flag complex, and checks its Euler characteristic. Tested pairs are \((q,m)=(3,2),(3,3),(3,5),(4,2),(4,4),(5,3),(6,2)\). Each passed. The finite checker does **not** compute the homology of \(BC_m\) or replace the algebraic proof for every \(q,m\); those statements follow from Steps 3–6.

## Relationship to prior work
Alsulami's *Filtered groupoid persistence* (first public 14 September 2026; DOI below, primary MSC 55N31) proves a one-sided non-overcount relation for the practical orbit-distance algorithm in degree one under suitable free-action hypotheses, while explicitly leaving higher-degree behavior unresolved. The present example supplies a direct negative answer for all higher degrees, alongside exact persistence interval decompositions. The construction also lies outside the small-scale \(t\)-diameter hypothesis used by Adams–Heim–Peterson's quotient-Rips comparison theorem: pairwise orbit edges in a triangle do not lift simultaneously. Their general small-scale comparison and projective-space transition examples do not give the present all-degree finite voltage-cover false-positive classification. Adams–Lagoda–Moy–Sadovek–De Saha study persistent Borel-equivariant cohomology of circle actions, not the orbit-metric algorithm for finite cyclic graph covers.

## Limitations
The result uses a deliberately engineered but natural binary-distance metric on a cyclic graph cover. It establishes an obstruction to a **universal** higher-degree non-overcount theorem, not a negative result for every metric sampling geometry. The full Borel persistence may have infinitely many nonzero degrees when the coefficient characteristic divides \(m\); any truncated computation must not mistake this for finite-dimensional vanishing. No claim of a new group-homology formula or a complete literature-priority certificate is made. Independent mathematical validation has not been performed.

## References
1. S. Alsulami, *Filtered groupoid persistence: A homotopy-theoretic framework for symmetry-aware topological data analysis*, AIMS Mathematics 11 (2026), 29754–29773, DOI: https://doi.org/10.3934/math.20261180. Published 14 September 2026.
2. H. Adams, M. Heim and C. Peterson, *Metric Thickenings and Group Actions*, Journal of Topology and Analysis, DOI: https://doi.org/10.1142/S1793525320500569. Also accessible as M. Heim, *Metric Thickenings and Group Actions*, Colorado State University thesis (2020), https://api.mountainscholar.org/server/api/core/bitstreams/7d984ed2-45ec-4ff2-834d-afb9b41ba9ca/content.
3. H. Adams, E. Lagoda, M. Moy, N. Sadovek and A. De Saha, *Persistent equivariant cohomology* (2024), https://arxiv.org/abs/2408.17331.
