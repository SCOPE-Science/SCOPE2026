# Exact maximum independent configurations of two-token double stars

## Finding
For integers \(a,b\ge1\), let \(S_{a,b}\) be the double-star tree formed by joining the centers \(x,y\) of two stars with leaf sets \(U,V\), where \(|U|=a\) and \(|V|=b\). The two-token graph \(F_2(S_{a,b})\) has one vertex for each unordered pair of distinct vertices of \(S_{a,b}\), with adjacency when exactly one token moves across a tree edge to an unoccupied vertex.

Its matching number, minimum vertex-cover number, and independence number are exactly
\[
\nu(F_2(S_{a,b}))=\tau(F_2(S_{a,b}))=2(a+b)-\mathbf1_{\{a\le2\}}-\mathbf1_{\{b\le2\}},
\]
\[
\alpha(F_2(S_{a,b}))=\binom{a+b}{2}+1+\mathbf1_{\{a\le2\}}+\mathbf1_{\{b\le2\}}.
\]
Moreover **every** maximum independent set is obtained by taking all \(ab\) mixed-leaf configurations \(\{u,v\}\) with \(u\in U,v\in V\), the double-center configuration \(\{x,y\}\), and exactly one of the following choices for each leaf branch, independently:

- For a branch of size \(1\) or \(2\), take every center–leaf pair on that branch and no same-branch leaf pair.
- For a branch of size \(3\), choose **either** all three center–leaf pairs **or** all three unordered same-branch leaf pairs.
- For a branch of size at least \(4\), take every unordered same-branch leaf pair and no center–leaf pair.

Consequently the number of maximum independent sets is precisely
\[
2^{\mathbf1_{\{a=3\}}+\mathbf1_{\{b=3\}}}.
\]
In particular, there is a unique maximum independent set whenever neither branch has three leaves; a branch of exactly three leaves contributes an independent binary choice.

## Assumptions and scope
Graphs are finite, simple and undirected. The two leaf sets are distinct and disjoint. The leaf counts are positive integers; the result includes \(S_{1,1}\cong P_4\). Token pairs are *unlabelled configurations* but are formed from individually distinct vertices. The result concerns pairwise independent vertices of the two-token graph, **not** two tokens being nonadjacent in the host tree, and not the domination number of the token graph.

## Proof
Use abbreviations \(UU=\binom U2\), \(VV=\binom V2\), \(UV=\{\{u,v\}:u\in U,v\in V\}\), \(XU=\{\{x,u\}:u\in U\}\), \(YV=\{\{y,v\}:v\in V\}\), \(XV=\{\{x,v\}:v\in V\}\), \(UY=\{\{u,y\}:u\in U\}\), and \(XY=\{\{x,y\}\}\). These eight types partition \(V(F_2(S_{a,b}))\).

**Edge decomposition.** Direct inspection of legal token moves shows that all edges, and no others, are of the types: \(UU-XU\) by incidence of the leaf; \(VV-YV\) by incidence; \(UV-XV\) and \(UV-UY\) by incidence of the retained leaf; \(XY-XV\) and \(XY-UY\) for every indicated partner; and the same-leaf edges \(XU-UY\) and \(YV-XV\).

Partition the vertices into three disjoint blocks \(B_U=UU\cup XU\), \(B_V=VV\cup YV\), and \(B_0=UV\cup XY\cup XV\cup UY\). Their induced graphs, ignoring the two families of interblock edges, are respectively the vertex–edge incidence graph of \(K_a\), the vertex–edge incidence graph of \(K_b\), and a bipartite graph whose left shore is \(L=XV\cup UY\) of cardinality \(a+b\), whose right shore is \(R=UV\cup XY\), and where \(XY\) is adjacent to every vertex of \(L\).

**The two incidence blocks.** For \(t\ge1\), the minimum vertex-cover size of the incidence graph of \(K_t\) is \(m(t)=\min\{t,\binom t2\}\). The corresponding matching has size \(m(t)\): for \(t=1\) it is empty; for \(t=2\) it matches the sole edge-vertex to one endpoint-vertex; for \(t\ge3\), match every endpoint-vertex with the different incident edge-vertex connecting it to its cyclic successor. To classify minimum covers, if \(p\) of the \(t\) endpoint-vertices are omitted, all \(\binom t2-\binom{t-p}2\) incident edge-vertices must be included. For \(t=2\) the unique minimum is the single edge-vertex; for \(t=3\) the two minima are the whole endpoint shore and the whole edge shore; for \(t\ge4\), \(\binom t2-\binom{t-p}2>p\) for every \(1\le p\le t\), so the unique minimum is the whole endpoint shore. For \(t=1\) the empty cover is the unique minimum.

**The mixed block.** Its left shore \(L\) is a cover of size \(a+b\). It also has a matching saturating \(L\). If \(a=1\), match each \(XV\) to its distinct \(UV\) vertex and match the remaining \(UY\) to \(XY\); the case \(b=1\) is symmetric. If \(a,b\ge2\), the subgraph between \(L\) and \(UV\) is the vertex–edge incidence graph of \(K_{a,b}\). A subset containing \(p\) vertices of \(UY\) and \(q\) of \(XV\) has exactly \(bp+aq-pq\) neighbors in \(UV\). If \(q<b\), this number minus \(p+q\) is \((b-q-1)p+(a-1)q\ge0\); if \(q=b\), it is \(ab-b-p\ge ab-a-b=(a-1)(b-1)-1\ge0\). Hall's theorem supplies the required matching. Thus the mixed block's matching and vertex-cover numbers both equal \(a+b\).

**Exact matching and cover.** Matchings in the three vertex-disjoint blocks unite into a matching of size \(m(a)+m(b)+a+b\). Independently, combine the two minimum incidence-block covers with all of \(L=XV\cup UY\). This covers all edges within the three blocks **and** the only interblock edges \(XU-UY\) and \(YV-XV\). The cover has the same cardinality as the matching, so both are optimal. Since \(m(t)=t-\mathbf1_{\{t\le2\}}\), the claimed matching and vertex-cover formulas follow. The elementary complement identity \(\alpha(G)=|V(G)|-\tau(G)\), together with \(|V(F_2(S_{a,b}))|=\binom{a+b+2}{2}\), gives the independence formula.

**Exhaustive optimizer classification.** Any minimum cover has the sum of the separate minimum-cover cardinalities, hence its restriction to each of the three disjoint blocks is itself a minimum cover. If \(a,b\ge2\), the mixed block has a matching from \(L\) into \(UV\) alone. Therefore any nonempty set of omitted \(L\)-vertices forces at least as many distinct \(UV\)-vertices **plus** \(XY\) into a cover, strictly increasing its size. Thus its only minimum cover is \(L\). If \(a=1\), the first incidence block has empty unique minimum cover, so \(XU\) is absent from every global minimum cover; the edge \(XU-UY\) forces its unique \(UY\)-vertex into the cover. Omitting any \(q\ge1\) vertices of \(XV\) would then force their \(q\) distinct \(UV\) neighbors and \(XY\), increasing the mixed-block cover size by one. Hence again the mixed-block cover is exactly \(L\). The symmetric argument applies if \(b=1\). Finally the incidence-block minimum covers can be chosen independently, since their only interblock edges already meet \(L\). Taking complements gives precisely the configurations listed in the Finding and the multiplicity \(2^{\mathbf1_{\{a=3\}}+\mathbf1_{\{b=3\}}}\). This completes the proof for every stated parameter, including both singleton-branch boundaries.

## Verification
The accompanying `verify.py` builds the token graph **directly from the host-tree edges**, independently of the proof's eight-type decomposition. It runs a generic bipartite augmenting-path matching algorithm for every \(1\le a,b\le8\) (64 instances), tests the explicitly described independent sets for all 64 instances, and uses an exact memoized maximum-independent-set recurrence to determine both the optimum size and number of optimizers for all nine cases \(1\le a,b\le3\). The included execution log contains the actual results. These checks are finite corroboration, not a proof of the universal quantifiers; the proof above is combinatorial and independent of computations.

## Relationship to prior work
Benítez-Bobadilla, Contreras-Mendoza, Gómez-Galicia and Trujillo-Negrete, *Domination in token graphs of graphs with domination number two* (arXiv:2611.15124, first submitted 2026-11-11), prove \(\gamma(F_2(S_{a,b}))=2\min(a,b)+\max(a,b)-1\). Their full Section 2.2 treats domination, rather than matching numbers, independence numbers, or the classification of maximum independent sets proved here.

De Alba, Carballosa, Leaños and Rivera, *Independence and matching numbers of some token graphs* (arXiv:1606.06370; Australas. J. Combin. 76 (2020), 387–403), give general matching lower bounds when a host has a perfect or near-perfect matching, and exact independence numbers for stars, paths, cycles and complete bipartite hosts. A double star with \(a+b\ge4\) has maximum host matching size two, strictly less than \(\lfloor(a+b+2)/2\rfloor\), so their main general bound does not directly apply there. Some smallest boundary cases are already covered by that theorem and are included here only to make the classification exact.

The matching and optimizer results on two-token complete bipartite host graphs appearing in public research records concern a different host graph; neither implies the double-star formulas through a graph isomorphism or simple specialization. No priority or independent verification is claimed from the absence of search hits.

## Limitations
The result treats exactly two indistinguishable tokens on double stars with two nonempty leaf groups. It does not address three or more tokens, arbitrary trees, weighted independent sets, or full independent-set polynomials. Historical novelty is provisional because equivalent results might be unindexed or expressed using other token-graph nomenclature.

## References
1. G. Benítez-Bobadilla, F. E. Contreras-Mendoza, S. G. Gómez-Galicia and A. Trujillo-Negrete, *Domination in token graphs of graphs with domination number two*, arXiv:2611.15124 (submitted 2026-11-11). https://arxiv.org/abs/2611.15124
2. H. de Alba, W. Carballosa, J. Leaños and L. M. Rivera, *Independence and matching numbers of some token graphs*, Australasian Journal of Combinatorics **76** (2020), 387–403; arXiv:1606.06370 (2016). https://ajc.maths.uq.edu.au/pdf/76/ajc_v76_p387.pdf
3. L. M. Rivera and G. Vázquez Briones, *Independence numbers of the 2-token graphs of some join graphs*, arXiv:2505.17419 (2025). https://arxiv.org/abs/2505.17419
