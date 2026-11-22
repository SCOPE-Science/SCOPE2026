# Facet spectra and circle-wedge topology of capacity-constrained labelled-token clique complexes

## Finding
Let \(n\ge2\), \(s\ge2\), and \(1\le k<ns\) be integers. Let \(H=F^s_{k\times1}(K_n)\) be the graph of placements of \(k\) **distinguishable** tokens on \(n\) labelled sites, with no more than \(s\) tokens at a site. Two placements are adjacent when exactly one token changes site. Write \(X=\operatorname{Cl}(H)\) for the simplicial clique complex (a face is a nonempty clique).

Define \(E_j(x)=\sum_{a=0}^{j}x^a/a!\), \(L=\max\{0,k-1-n(s-1)\}\), and \(U=\min\{n-2,\lfloor(k-1)/s\rfloor\}\). Put
\[
V=k![x^k]E_s(x)^n,\qquad
M_f=k\binom nf\frac{(k-1)!}{(s!)^f}[x^{k-1-sf}]E_{s-1}(x)^{n-f}\quad (L\le f\le U).
\]
A coefficient of negative degree is zero. Then \(M_f\) is **exactly** the number of inclusion-maximal cliques of cardinality \(n-f\). Every maximal clique has one of these cardinalities, and each integer in \(\{n-U,\ldots,n-L\}\) occurs. The complete clique-counting polynomial, including the empty clique, is
\[
C_H(z)=1+Vz+\sum_{f=L}^{U}M_f\sum_{j=2}^{n-f}\binom{n-f}{j}z^j.
\]
The complex \(X\) has the integral homotopy type
\[
X\simeq\bigvee^{B}S^1,\qquad B=1-V+\sum_{f=L}^{U}(n-f-1)M_f.
\]
As usual, a wedge of zero circles means a point. In particular its reduced integral homology is free, concentrated in degree one with rank \(B\), and its fundamental group is free of rank \(B\).

**Sharp purity classification.** For \(n=2\), \(X\) is always a pure one-dimensional complex. For \(n\ge3\), it is pure **if and only if** \(1\le k\le s\) or \(k=ns-1\). For every \(s+1\le k\le ns-2\), it has facets in at least two different dimensions, with no gaps among the occurring facet dimensions.

## Assumptions and scope
All graphs are finite, simple, undirected, and labelled. The base is the complete graph \(K_n\), not an arbitrary host. Token identities matter: configurations are ordered \(k\)-tuples. The capacity is the **per-site** upper bound \(s\ge2\). For \(k\le s\), the graph is the unrestricted Cartesian power \(K_n^{\square k}\). The full-capacity endpoint \(k=ns\) is excluded because it has \((ns)!/(s!)^n\) isolated configurations; its clique complex is discrete, not connected. This result is about ordinary clique complexes, not independence complexes or clique-avoidance complexes.

## Proof
**1. Coordinate fibres.** Fix a token index \(i\) and the locations \(a=(a_j)_{j\ne i}\) of the other \(k-1\) tokens, each site holding at most \(s\) of those fixed tokens. If exactly \(f\) sites are saturated, the \(i\)-th token can occupy any of the other \(n-f\) sites. These placements form a complete coordinate fibre \(K_{n-f}\). An edge changes a unique coordinate. For any triangle, all three edges must change that same coordinate; otherwise two vertices differ in two coordinates and are not adjacent. By applying this argument to every vertex of a clique of size at least two, every such clique belongs to a *unique* coordinate fibre. Every fibre of size at least two is therefore an inclusion-maximal clique, since no different coordinate can be added. Distinct maximal fibres meet in at most one vertex.

Every configuration has an incident edge when \(k<ns\). Indeed, there is a nonsaturated site, and some token can move there from a different site unless all tokens are at that site, in which case another site is nonsaturated and receives a token. Hence singleton cliques are not facets.

**2. Feasible saturated-site counts.** For a fixed partial placement, \(f\) saturated sites contribute \(sf\) tokens; the \(n-f\) remaining sites hold from zero through \(s-1\) tokens each. Therefore \(f\) is feasible for a fibre of at least two vertices exactly when
\[
0\le k-1-sf\le(n-f)(s-1),\qquad 0\le f\le n-2,
\]
which rearranges to \(L\le f\le U\). Every such integer is attained because every intermediate total can be distributed across the \(n-f\) bounded sites.

**3. Counting.** There are \(\binom nf\) choices of saturated sites. Distributing the distinct fixed tokens among them and the remaining sites gives
\[
\binom nf\frac{(k-1)!}{(s!)^f}[x^{k-1-sf}]E_{s-1}(x)^{n-f}
\]
partial placements. Multiplying by \(k\) choices of moving token gives \(M_f\) different maximal fibres, without double counting (each fibre has a unique moving coordinate and fixed partial placement). The vertex enumerator is \(V=k![x^k]E_s(x)^n\). Every clique of size \(j\ge2\) occurs in its unique maximal fibre; such a fibre contributes \(\binom{n-f}{j}\) cliques. This proves the polynomial.

**4. Connectivity and homotopy.** Every nonsaturated configuration exists with at least one vacancy. Occupancy vectors of two configurations can be reconciled by repeatedly moving a token from a site with surplus occupancy to a site with deficient occupancy. At any fixed occupancy vector, any two tokens at distinct sites can exchange locations using the vacancy: if one endpoint site is nonsaturated, use it directly in two moves; otherwise use a nonsaturated third site as temporary storage in three moves. These exchanges generate every reassignment of distinct labels at fixed occupancy. Thus \(H\) is connected.

The maximal simplices of \(X\) are the coordinate fibres, and any two intersect in at most a vertex. Each simplex can be deformation-retracted relative to all its vertices onto the star joining its barycentre to its vertices. The retractions agree on intersections, giving a deformation retraction of \(X\) onto the bipartite incidence graph whose nodes are configurations and maximal fibres, with an edge for each incidence. That graph is connected; it has \(V+\sum_f M_f\) nodes and \(\sum_f(n-f)M_f\) edges. Its first Betti number is therefore \(1-V+\sum_f(n-f-1)M_f=B\), and every connected graph is homotopy equivalent to a wedge of \(B\) circles.

**5. Purity.** The facet sizes are consecutive integers \(n-U,\ldots,n-L\), so purity is equivalent to \(L=U\). When \(n=2\), both equal zero. Suppose \(n\ge3\). When \(k\le s\), both equal zero; when \(k=ns-1\), both equal \(n-2\). Conversely, put \(r=k-1\) and suppose \(s+1\le k\le ns-2\). If \(r\le n(s-1)\), then \(L=0\) but \(U\ge1\). If \(r>n(s-1)\), then \(1\le L=r-n(s-1)\le n-3\). Hence \(n-2\ge L+1\); moreover \(r-s(L+1)=(s-1)(n-L)-s\ge3(s-1)-s\ge0\), so \(\lfloor r/s\rfloor\ge L+1\). In both cases \(U>L\). This proves the sharp classification.

## Verification
A standalone Python checker `verify_supertoken.py` enumerates admissible ordered token placements independently of the coefficient formulas, creates the adjacency graph, enumerates all maximal cliques, and compares the observed facet-size multiplicities against both direct partial-assignment counts and exact rational coefficient extraction. It checks connectivity, the clique-complex Euler characteristic and the purity criterion in all enumerated non-full cases. Its finished run checked 45 instances with at most 420 configuration vertices each and returned `TESTED_INSTANCES 45 VERIFY_OK`.

For the small mixed-dimensional example \((n,s,k)=(3,2,4)\), there are \(V=54\) vertices, \(72\) edge facets and \(24\) triangular facets, and \(B=67\). At \((3,2,5)\), there are \(90\) vertices and \(180\) edge facets, giving \(B=91\). Computation is finite corroboration; the five proof steps above establish all parameter cases.

## Relationship to prior work
Song et al. (2026) introduced the broader distinguishable-capacity token configuration construction and determined its order and size. Cai et al. (2026) proved the common-coordinate property for cliques and a clique-number formula, as well as a connectivity theorem. These are credited and not claimed as new. Dalfó et al. (2026) investigated the single-capacity \(s=1\) subfamily, which is not the range proved here. The unrestricted Hamming graph is a familiar special case; its coordinate-line clique decomposition is not new. The contribution here is the all-capacity labelled facet-size **distribution**, consecutive facet-size interval and exact purity boundary, and the resulting **integral** circle-wedge rank for every non-full capacity-constrained complete-base graph. None of the inspected primary results states or implies those numerical distributions merely by taking a parameter special case of a previously stated counting formula.

## Limitations
The theorem assumes a complete host and capacity at least two; no assertion is made for arbitrary base graphs or the disconnected full-capacity case. It uses the ordinary clique complex only. The verification script checks finitely many cases, not a proof for all parameters. Historical priority is provisional: similar coordinate-line topology of induced Hamming subgraphs may exist under other terminology. The homotopy mechanism uses a standard simplicial gluing principle; its generality is not itself claimed as novel. No independent audit has been performed.

## References
1. X. Song, C. Dalfó, M. À. Fiol, M. Mora, S. Zhang, *On Generalized Token Graphs*, arXiv:2604.04845, first public 2026-04-06, https://arxiv.org/abs/2604.04845 (definition and counting of configurations).
2. Y. Cai, C. Dalfó, B. Fernández, M. À. Fiol, *On generalized \(k\)-token graphs with distinguishable tokens and a maximum capacity of \(s\) tokens per vertex*, arXiv:2611.06275, first public 2026-11-04, https://arxiv.org/abs/2611.06275 (Lemmas 5.1–5.2 and Section 3).
3. C. Dalfó, B. Fernández, M. À. Fiol, M. A. Reyes, *On generalized token graphs with tokens of different colors*, arXiv:2611.08186, first public 2026-11-05, https://arxiv.org/abs/2611.08186 (capacity-one comparison, Section 8).
