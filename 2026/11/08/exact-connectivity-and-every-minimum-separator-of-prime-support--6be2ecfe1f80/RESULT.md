# Exact connectivity and every minimum separator of prime-support-filtered cyclic factorization graphs

## Finding
For integers \(t\ge2\) and \(r\ge 2^t\), let \(G=C_{p_1p_2\cdots p_r}\), where the primes \(p_i\) are distinct. Form the simple factorization graph \(\Gamma(G)\): its vertices are the nonidentity proper subgroups, and distinct subgroups \(H,K\) are adjacent exactly when \(HK=G\). Write \(\mathcal F_t(G)\) for the induced graph on subgroups whose orders are divisible by at least \(t\) distinct primes.

The **connectivity-and-separator theorem** is
\[
\kappa(\mathcal F_t(G))=\lambda(\mathcal F_t(G))=\delta(\mathcal F_t(G))=2^t-1.
\]
Moreover, its **entire family of minimum vertex cuts** is
\[
\bigl\{N_{\mathcal F_t(G)}(H): H\le G,\ |H|=p_{i_1}\cdots p_{i_t}\text{ for distinct }i_1,\ldots,i_t\bigr\}.
\]
These neighborhoods are pairwise different; thus there are exactly \(\binom rt\) minimum vertex cuts. Each cut isolates the corresponding \(H\), and the other surviving vertices induce one connected component.

For \(t=2\), \(\mathcal F_2(G)\) is precisely the graph obtained by deleting every prime-order (pendant) subgroup from \(\Gamma(G)\). For all \(r\ge4\), it is **3-vertex-connected**, **3-edge-connected**, and has exactly \(\binom r2\) minimum vertex cuts. More generally, the support filtration yields successive values \(3,7,15,\ldots\) under the specified rank thresholds.

## Assumptions and scope
The group must be cyclic of squarefree order with exactly \(r\) prime factors. Subgroup products and adjacency are ordinary group products, not intersections or elementwise power adjacency. The permitted integers obey \(t\ge2\) and \(r\ge2^t\). The bound on \(r\) guarantees there is at least one surviving maximal subgroup after deleting as many vertices as the claimed connectivity and, because \(2^t\ge2t\) for \(t\ge2\), that the largest allowed deficiency subsets admit all \(2^t-1\) nonempty complementary subsets. We do not assert this rank threshold is necessary. Graphs are simple, undirected, and finite. A vertex cut \(B\) means \(\mathcal F_t(G)-B\) is disconnected; \(\kappa\), \(\lambda\), and \(\delta\) are the vertex-connectivity, edge-connectivity, and minimum degree.

## Proof
**1. Algebraic support model.** Label the prime factors by \([r]=\{1,\dots,r\}\). Every subgroup \(H\) has a unique order \(\prod_{i\in I(H)}p_i\). Put its *deficiency set* \(S(H)=[r]\setminus I(H)\). The vertex condition \(1\ne H\ne G\), together with the filtration, is equivalent to
\[
\varnothing\ne S(H)\subseteq[r],\qquad 1\le |S(H)|\le r-t.
\]
Since \(G\) is cyclic, \(|HK|=\operatorname{lcm}(|H|,|K|)\); therefore \(HK=G\) if and only if \(S(H)\cap S(K)=\varnothing\). Thus \(\mathcal F_t(G)\) is exactly the disjointness graph on nonempty subsets of \([r]\) of sizes at most \(r-t\), with one vertex for each such subset.

**2. Degrees.** The neighbors of a vertex \(S\) are exactly the nonempty subsets \(T\subseteq[r]\setminus S\) with \(|T|\le r-t\). Consequently
\[
\deg(S)=\sum_{j=1}^{\min(r-|S|,\,r-t)}\binom{r-|S|}{j}.
\]
When \(|S|=r-t\), the complement has size \(t\), which is no greater than \(r-t\), hence \(\deg(S)=2^t-1\). If \(|S|<r-t\), enlarge \(S\) to some set of size \(r-t\). Its complementary neighbor subsets are a *proper* subfamily of the nonempty eligible neighbor subsets for \(S\): one additional singleton is eligible. Thus \(\deg(S)>2^t-1\). This proves \(\delta=2^t-1\), and **exactly** the deficiency sets of cardinality \(r-t\) attain it.

**3. Exact vertex cuts.** Let \(d=2^t-1\), and remove an arbitrary vertex set \(B\) with \(|B|\le d\). The \(r\) singleton deficiency sets are pairwise disjoint and therefore form a clique. Since \(r\ge d+1\), at least one singleton survives; let \(J\subseteq[r]\) index all surviving singleton vertices. The surviving singleton clique \(K_J\) is nonempty and connected.

Consider a vertex \(S\) outside the connected component containing \(K_J\). It has no edge to any surviving singleton, so \(S\cap\{j\}\ne\varnothing\) for all \(j\in J\): necessarily \(J\subseteq S\). If \(S\) and \(T\) both lie outside that component, then both contain nonempty \(J\), so \(S\cap T\supseteq J\ne\varnothing\). Therefore no two vertices outside the anchor component are adjacent: **each is an isolated singleton component**. To isolate such an \(S\), its full open neighborhood must be contained in \(B\), giving \(|B|\ge\deg(S)\ge d\).

Hence deletion of fewer than \(d\) vertices cannot disconnect the graph. If deletion of exactly \(d\) vertices disconnects it, there is an isolated \(S\) with \(B=N(S)\) and \(\deg(S)=d\). By Step 2, \(|S|=r-t\), so the corresponding subgroup has exactly \(t\) prime factors. Conversely, for every such \(S\), deleting \(N(S)\) isolates \(S\). The remaining singleton clique corresponds to precisely the singleton elements of \(S\); any other surviving vertex that failed to touch that clique would contain all of \(S\) and have size at most \(|S|=r-t\), forcing it to equal \(S\). Thus **all other surviving vertices stay in one connected component**. In particular these are cuts of size \(d\), giving \(\kappa=d\) and the exact classification.

The cuts are distinct: for each minimum-degree vertex \(S\), the singleton vertices belonging to \(N(S)\) have labels exactly \([r]\setminus S\). This recovers \(S\) from the cut. There are \(\binom rt\) such \(S\).

**4. Edge connectivity.** The standard inequality \(\kappa(X)\le\lambda(X)\le\delta(X)\) for finite simple graphs, together with the established equality \(\kappa=\delta=d\), yields \(\lambda=d\). No assertion is made about the classification of minimum *edge* cuts.

## Verification
A standalone standard-library Python program `verify.py` constructs the finite disjointness graph without using the proof's connectivity argument, and independently checks the corresponding subgroup-product adjacency using least common multiples of actual subgroup orders. It exhaustively tests **all** vertex-deletion subsets up to the asserted connectivity for \((r,t)=(4,2),(5,2),(6,2)\): there are respectively \(176\), \(2626\), and \(29317\) deletion cases. For \((7,2)\) and \((8,3)\), it also verifies the degree layers, every predicted minimum cut, the residual component structure, and seeded random smaller deletions; these larger-case checks are not exhaustive. Total deletion cases: \(32519\). Recorded output ends `VERIFY_OK deletion_cases= 32519`. The proof of the universal statement is the preceding argument, not finite enumeration.

## Relationship to prior work
Gutiérrez, Zuleta, and García-Claro, *On the factorization graph of finite groups* (arXiv:2610.40860v1, first public on October 29, 2026), establish the squarefree-cyclic subgroup support model and prove **2-connectivity** of the pendant-free graph in their Theorem 4.17. Their result and their displayed maximal-subgroup clique are prerequisites, not new claims here. The present theorem sharpens 2-connectivity to the *exact* vertex and edge connectivity and identifies *all* minimum vertex cuts, and extends this to a filtration by subgroup prime-support size.

Rather, *Vertex connectivity of the nonzero nonunit core of the comaximal graph of \(\mathbb Z_n\)* (arXiv:2605.01565v1, May 2, 2026), proves connectivity equals minimum degree for the **weighted blow-up graph on ring elements** of all nonempty proper support sets, with weights depending on the prime factors. This is not the one-vertex-per-subgroup, support-truncated graph studied here. Rather explicitly leaves **classification of minimum vertex cuts** open as Problem 8.1 for his weighted graph; the present theorem does not claim to solve that separate weighted problem. Ekinci and Gauci's 2019 super-connectivity theorem concerns uniform-layer Kneser graphs, rather than all subset sizes up to a cutoff. The founding factorization-graph work of Farrokhi Derakhshandeh Ghouchan and Azimi (arXiv:1911.12594) concerns connectedness and forbidden subgraphs, not this complete cut classification.

## Limitations
The result covers cyclic squarefree groups and the filtration only when \(t\ge2\), \(r\ge2^t\). It is not claimed for groups with repeated prime powers, for arbitrary finite groups, or for the filtered graphs below this threshold. The argument proves all minimum **vertex** cuts, but for **edge** cuts only their minimum cardinality. The support realization depends on cyclic squarefree subgroup uniqueness. Although specific known literature was checked, an older general result on nonuniform disjointness graphs might imply the cut classification under different terminology; independent priority verification remains necessary.

## References
- I. Gutiérrez, Y. Zuleta, E. J. García-Claro, *On the factorization graph of finite groups*, arXiv:2610.40860v1 (2026), https://arxiv.org/abs/2610.40860.
- B. A. Rather, *Vertex connectivity of the nonzero nonunit core of the comaximal graph of \(\mathbb Z_n\)*, arXiv:2605.01565v1 (2026), https://arxiv.org/abs/2605.01565.
- M. Farrokhi Derakhshandeh Ghouchan and A. Azimi, *Factorization graphs of finite groups*, arXiv:1911.12594v1 (2019), https://arxiv.org/abs/1911.12594.
- G. Boruzanlı Ekinci and J. B. Gauci, *The Super-Connectivity of Kneser Graphs*, Discussiones Mathematicae Graph Theory 39 (2019), 5–11, https://geodesic.mathdoc.fr/item/DMGT_2019_39_1_a0/.
