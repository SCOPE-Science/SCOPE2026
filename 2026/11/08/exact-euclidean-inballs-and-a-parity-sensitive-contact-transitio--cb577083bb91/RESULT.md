# Exact Euclidean inballs and a parity-sensitive contact transition for complete multipartite symmetric-edge polytopes

## Finding

Let \(k\ge3\) and let \(n_1,\ldots,n_k\) be positive integers, with \(N=\sum_i n_i\), \(L=\max_i n_i\), and \(c=|\{i:n_i=L\}|\). In the zero-sum Euclidean hyperplane \(H=\{x\in\mathbb R^N:\sum_i x_i=0\}\), consider the symmetric-edge polytope
\[
P=\operatorname{conv}\{\pm(e_u-e_v):u,v\text{ in different parts of }K_{n_1,\ldots,n_k}\}.
\]
Put
\[
B=\frac{\lfloor N^2/4\rfloor}{N},\qquad
T=\begin{cases}0,&L=1,\\L-\frac{L\bmod2}{N},&L\ge2,\end{cases}\qquad Q=\max\{B,T\}.
\]
Then the intrinsic Euclidean inradius is exactly
\[
\boxed{r(P)=Q^{-1/2}}.
\]
The centered ball of this radius is maximum, and the exact number of facets tangent to **that centered ball** is
\[
\boxed{F=\mathbf1_{B=Q}\,b_N+\mathbf1_{T=Q}\,c\,t_L},
\]
where \(b_N=\binom N{N/2}\) for even \(N\), \(b_N=2\binom N{(N-1)/2}\) for odd \(N\), and \(t_L=\binom L{L/2}\) for even \(L\ge2\), \(t_L=2\binom L{(L-1)/2}\) for odd \(L\ge3\) (with \(t_1=0\)). The two summands classify disjoint kinds of tangent facets: globally balanced two-level potential functions, and balanced three-level functions supported on a largest graph part.

If \(L\ge2\), equality \(B=T\) occurs **if and only if** \(N\) is divisible by \(8\) and \(L=N/4\). Thus the two contact mechanisms coexist only on a parity-restricted threshold. For example, \(K_{2,2,2,2}\) has \(r=1/\sqrt2\) and exactly \(78\) facets tangent to its centered maximal ball, while \(K_{3,3,3,3}\) has \(r=1/\sqrt3\) and exactly \(924\) such facets, all of the two-level kind.

## Assumptions and scope

The vertex classes are nonempty, and their number is at least three; the underlying graph is simple and complete between distinct classes. Distances and facet-support normal lengths are computed in the inherited metric on \(H\), not an arbitrary affine realization. A facet is counted once for each distinct supporting hyperplane; opposite facets are distinct. The claim concerns the origin-centered maximal Euclidean ball, and does not claim that every maximum-radius center is unique.

## Proof

**Facet potentials.** Let \(f:V\to\mathbb Z\) be a facet potential with the supporting inequality \(\langle f,x\rangle\le1\). The facet criterion says that \(|f(u)-f(v)|\le1\) on every graph edge, and edges on which equality holds form a connected spanning graph. These facts also follow directly: a facet contains enough oriented edge-root vertices to span \(H\), hence its tight edges contain a spanning tree; differences along this tree are \(\pm1\), so all potential values are integral up to a constant. Conversely, a connected tight-edge graph has edge roots spanning \(H\), hence defines a facet.

If the range of \(f\) is one, normalize its values to \(0,1\). If the range is at least two, an absolute minimum vertex and an absolute maximum vertex must belong to the same original graph part, since any two vertices in different parts are adjacent. Every vertex outside that part is within one unit of both extrema, forcing the range to be exactly two and all outside values to equal the midpoint. An inside vertex at the midpoint has no tight edge, so connectivity excludes it. After adding a constant, the only possible three-level functions have values \(0,2\) (both present) on one part and value \(1\) on every other part. Their tight-edge graph is a spanning complete bipartite graph, so every such potential is a facet. These are the only two types.

**Euclidean normal lengths.** The intrinsic facet normal is \(f^\circ=f-\overline f\mathbf1\), and the supporting hyperplane is at distance \(1/\|f^\circ\|\) from zero. For a binary potential with \(a\) zeros and \(N-a\) ones,
\[
\|f^\circ\|^2=\frac{a(N-a)}N\le B.
\]
For a three-level potential whose special part has size \(s\), let its numbers of zeros and twos be \(u,v\ge1\), \(u+v=s\). After subtracting the constant one, its values are \(-1\) on \(u\) vertices, \(+1\) on \(v\) vertices, and zero elsewhere. Hence
\[
\|f^\circ\|^2=s-\frac{(u-v)^2}{N}\le s-\frac{s\bmod2}{N}\le T.
\]
The final upper bound is sharp by balancing the two signs in a largest part; the quantity \(s-(s\bmod2)/N\) increases strictly with \(s\ge2\). The binary upper bound \(B\) is also sharp: if all parts are singletons, any nonconstant balanced binary function has connected tight edges. Otherwise choose two vertices in one part, one vertex from each of two other parts, and assign the four selected vertices labels \(0,1,0,1\) in that order. Their tight-edge graph is connected and every remaining vertex, whichever label it receives, has a tight edge to this four-vertex core. Assign the remaining labels to achieve \(\lfloor N/2\rfloor\) and \(\lceil N/2\rceil\) of each color. Thus the maximum squared facet-normal length is exactly \(Q\).

**Optimality of the centered ball.** The polytope is centrally symmetric and full-dimensional in \(H\). If it contains a ball of radius \(r\) with center \(z\), it also contains the same ball centered at \(-z\), so by convexity it contains the radius-\(r\) ball centered at the origin. Consequently its inradius is the minimum origin-to-facet distance, equal to \(Q^{-1/2}\).

**Counting tangent facets.** A three-level facet is tangent precisely if its special part has size \(L\), its signs are as evenly split as parity permits, and \(T=Q\). This yields \(c\,t_L\) distinct facets. If \(B=Q\), every balanced binary labeling is a facet: for \(N\ge4\), the inequality \(B\ge T\) forces \(L<\lfloor N/2\rfloor\) (otherwise \(T\ge\lfloor N/2\rfloor-1/N>B\)). Each color then has more vertices than any single original part. The graph of edges between opposite colors has no isolated vertices. If it had two connected components, choose a tight edge in each; their opposite-color cross-pairs must both be nonedges, forcing those two edges to run between the same two original parts with opposite endpoints. A vertex of a third part would be adjacent by a tight edge to one endpoint in each component, a contradiction. Thus the tight-edge graph is connected. The case \(N=3\) is \(K_3\) and is immediate. All \(b_N\) balanced binary labelings therefore define distinct contacting facets. No other facets attain squared norm \(Q\).

**Parity of coexistence.** For \(L\ge2\), the equality \(B=T\) is \(\lfloor N^2/4\rfloor=NL-(L\bmod2)\). For odd \(N\), this rearranges to \(N(4L-N)=4(L\bmod2)-1\), impossible for odd \(N\ge5\), while \(N=3\) has \(L=1\). For even \(N\ge4\), it rearranges to \(N(4L-N)=4(L\bmod2)\). The odd-\(L\) case has no integer solution; the even-\(L\) case forces \(N=4L\), and therefore \(N\equiv0\pmod8\). Conversely these parameters give equality.

## Verification

The standalone checker `check_multipartite_inball.py` enumerates all integer facet potentials with values in \(\{0,1,2\}\), checks the connected-tight-edge criterion, calculates centered squared norms using exact rational arithmetic, and verifies both the largest norm and the number attaining it. It exhaustively checked \(67\) complete multipartite parameter lists with at least three parts and at most nine total vertices. It also checks the stated higher-order parity examples by exact formulas. It returns `MULTIPARTITE_SYMMETRIC_EDGE_INBALL_CHECKS_PASSED 67 cases`. All-dimensional correctness rests on the proof, not on finite enumeration.

## Relationship to prior work

Higashitani, Jochemko, and Michałek provide the facet-normal criterion for symmetric-edge polytopes and discuss complete multipartite cases. Chen, Davis, and Korchevskaia classify facet subgraphs via maximal bipartite subgraphs. Kölbl revisits the multipartite facet descriptions in studying Ehrhart-root questions. The present result uses their common polyhedral setting but maximizes the *intrinsic Euclidean length* of facet normals and counts only facets meeting a largest centered inball. The cited prior results give neither this maximum and its quarter-size/parity transition nor these contact counts. Other published metric results for individual graph families do not cover all multipartite graphs with three or more parts.

## Limitations

The realization is the standard signed edge-root embedding with unit edges; a general affine transform changes Euclidean radii. No assertion is made about the full set of maximum-ball centers, John ellipsoids, volumes, or graphs that are not complete multipartite. Historical priority under alternative Lipschitz-free or Kantorovich–Rubinstein terminology remains subject to further independent checking. The current verification is an analytical derivation plus finite reproducibility checks, not an independent audit.

## References

1. A. Higashitani, K. Jochemko, M. Michałek, *Arithmetic aspects of symmetric edge polytopes*, arXiv:1807.07678v1 (first posted 2018-07-20), Theorem 3.1 and Section 3.1. https://arxiv.org/abs/1807.07678
2. T. Chen, R. Davis, E. Korchevskaia, *Facets and facet subgraphs of symmetric edge polytopes*, arXiv:2107.12315 (first posted 2021-07-26), Theorem 3 and Sections 4.2–4.5. https://arxiv.org/abs/2107.12315
3. M. Kölbl, *On a Conjecture Concerning the Roots of Ehrhart Polynomials of Symmetric Edge Polytopes from Complete Multipartite Graphs*, arXiv:2404.02136v1 (first posted 2024-04-02), Proposition 1.2 and the Ehrhart analysis. https://arxiv.org/abs/2404.02136
