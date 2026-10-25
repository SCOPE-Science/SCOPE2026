# Direct graph spines for nonbipartite square-free neighborhood complexes
## Finding
Let \(G\) be a finite connected simple nonbipartite square-free graph with \(n=|V(G)|\) and \(e=|E(G)|\). For every choice of a root \(r_v\in N_G(v)\) for each \(v\in V(G)\), the Lovász neighborhood complex \(\mathcal N(G)\) simplicially collapses onto the graph \(T_r\) on \(V(G)\) with \[E(T_r)=\bigl\{\{r_v,x\}:v\in V(G),\ x\in N_G(v)\setminus\{r_v\}\bigr\}.\] The graph \(T_r\) is connected, has \(n\) vertices and \(2e-n\) edges, and therefore \[\mathcal N(G)\simeq T_r\simeq\bigvee^{\,2e-2n+1}S^1.\]

The collapse is explicit and works for every root choice. It replaces a neighborhood complex that can contain high-dimensional simplices by a graph on the original vertex set, without expansions or auxiliary vertices.

## Assumptions and scope
A graph is square-free when it contains no subgraph isomorphic to \(C_4\). Equivalently, any two distinct vertices have at most one common neighbor. The neighborhood complex \(\mathcal N(G)\) consists of the nonempty sets \(\sigma\subseteq V(G)\) having a common neighbor. The hypotheses are finite, connected, simple, nonbipartite, and square-free. No regularity, degree bound, planarity, or girth condition beyond exclusion of \(C_4\) is assumed; triangles are allowed.

For each \(v\in V(G)\), choose an arbitrary root \(r_v\in N_G(v)\). Define \(T_r\) by retaining, for each center \(v\), the rooted-star edges \(\{r_v,x\}\) with \(x\in N_G(v)\setminus\{r_v\}\).

## Proof
Square-freeness gives the key uniqueness property. If a face \(\sigma\in\mathcal N(G)\) has at least two vertices and both \(v\) and \(w\) are common neighbors of \(\sigma\), choose distinct \(a,b\in\sigma\). If \(v\ne w\), then \(a,v,b,w\) form a \(4\)-cycle, impossible. Hence every face of cardinality at least two has a unique common-neighbor center.

Fix \(v\). For each \(\sigma\subseteq N_G(v)\setminus\{r_v\}\) with \(|\sigma|\ge2\), pair \(\sigma\) with \(\sigma\cup\{r_v\}\). Execute these elementary collapses in decreasing order of \(|\sigma|\), with any fixed order among equal sizes. At the moment the pair indexed by \(\sigma\) is processed, every remaining coface \(\tau\supseteq\sigma\) has common-neighbor center \(v\) by uniqueness, so \(\tau\subseteq N_G(v)\). If \(\tau\) contains any vertex outside \(\sigma\cup\{r_v\}\), then the corresponding larger lower face has already been processed; if \(\tau\) omits \(r_v\) and strictly contains \(\sigma\), it also was removed earlier. Thus the only remaining cofaces of \(\sigma\) are \(\sigma\) and \(\sigma\cup\{r_v\}\), so \(\sigma\) is free and the pair is an elementary simplicial collapse.

After all such pairs are removed, every vertex remains and the only remaining edges are \(\{r_v,x\}\) with \(x\in N_G(v)\setminus\{r_v\}\). No edge can be contributed by two different centers: two distinct common-neighbor centers for its endpoints would create a \(4\)-cycle. Therefore
\[
|E(T_r)|=\sum_{v\in V(G)}(\deg(v)-1)=2e-n.
\]

Two vertices lie in the same component of the \(1\)-skeleton of \(\mathcal N(G)\) exactly when they can be joined by an even-length walk in \(G\). Because \(G\) is connected and contains an odd cycle, walk parity can be switched, so every pair of vertices is joined by an even-length walk. Hence \(\mathcal N(G)\), and therefore \(T_r\), is connected. A connected graph with \(n\) vertices and \(2e-n\) edges is homotopy equivalent to a wedge of \((2e-n)-n+1=2e-2n+1\) circles.

## Verification
The standalone verifier `verify.py` independently constructs the neighborhood complex and replays the stated free-face collapses. It exhausts all \(3{,}610\) connected labeled nonbipartite square-free graphs on at most six vertices. It checks every root choice for graphs on at most five vertices and one deterministic root choice on six vertices, for \(7{,}916\) root assignments and \(19{,}974\) elementary collapses in total. For every case it checks the free-face condition at the instant of removal, equality of the residue with \(T_r\), the edge count \(2e-n\), connectedness, and the cycle-rank formula. The saved output ends with `VERIFY_OK` and reports no exception.

The finite verification is a stress test, not the proof for arbitrary finite graphs; the proof above supplies the universal quantifiers.

## Relationship to prior work
Donovan and Scoville use star-cluster collapses and the Cluster Lemma to obtain explicit homotopy reductions for several graph-associated complexes; their paper is the middle-window methodological source for asking for a direct collapse rather than only an abstract homotopy calculation. Their scope is matching, Morse, and generalized Morse complexes, not Lovász neighborhood complexes.

For neighborhood complexes, Shukla proves that each component of \(\mathcal N(G)\) is contractible or a wedge of circles when \(G\) has maximum degree at most three, using local collapses. The present statement has no degree bound and gives a single root-parametrized target graph and exact cycle rank under square-freeness and nonbipartiteness.

Kamibeppu determines the equivariant homotopy type of the box/Hom complex for graphs without \(4\)-cycles, and Fujii--Kimura--Nozaki explicitly record that for connected square-free \(H\), \(\operatorname{Hom}(K_2,H)\) is homotopy equivalent to \(H\times K_2\); they also recall the standard homotopy equivalence with \(\mathcal N(H)\). Csorba proves that the standard graph complexes, including the neighborhood and box complexes, have the same simple equivariant homotopy type. These results determine or constrain homotopy type, but they do not state the direct elementary collapse here onto the root-selected graph \(T_r\) on the original vertex set. For nonbipartite \(G\), the known connected double cover has \(2n\) vertices and \(2e\) edges, whereas \(T_r\) has \(n\) vertices and \(2e-n\) edges with the same cycle rank.

## Limitations
The claim is only for the nonbipartite square-free domain. It does not assert a canonical root choice or graph isomorphism type for \(T_r\); different roots can produce different spine graphs with the same connected homotopy type and edge count. The result does not cover graphs containing a \(4\)-cycle, where a face can have more than one common-neighbor center and the free-face argument can fail.

The closest older work on box complexes and the general simple-homotopy equivalence among graph complexes leaves a residual literature risk: an equivalent direct neighborhood-complex collapse may exist under different terminology. The searches and inspected sources located the homotopy and simple-homotopy statements above, but not the root-selected direct collapse claim.

## References
1. C. Donovan and N. A. Scoville, “Star clusters in the Matching, Morse, and Generalized Morse complex,” arXiv:2207.13780v1, first public 2022-07-27. 2020 Mathematics Subject Classification: primary 57Q70.
2. S. Shukla, “Homotopy type of the neighborhood complexes of graphs of maximal degree at most \(3\) and \(4\)-regular circulant graphs,” arXiv:1802.04526v1, 2018; Electronic Journal of Combinatorics 26(2), 2019, P2.4.
3. A. Kamibeppu, “Homotopy Type of the Box Complexes of Graphs without \(4\)-cycles,” Tsukuba Journal of Mathematics 32(2), 2008, 307–314.
4. P. Csorba, “On the Simple \(\mathbb Z_2\)-homotopy Types of Graph Complexes and Their Simple \(\mathbb Z_2\)-universality,” Canadian Mathematical Bulletin 51(4), 2008, 535–544, doi:10.4153/CMB-2008-053-9.
5. S. Fujii, K. Kimura, and Y. Nozaki, “Homotopy types of Hom complexes of graph homomorphisms whose codomains are square-free,” arXiv:2412.19039v1, first public 2024-12-26.
