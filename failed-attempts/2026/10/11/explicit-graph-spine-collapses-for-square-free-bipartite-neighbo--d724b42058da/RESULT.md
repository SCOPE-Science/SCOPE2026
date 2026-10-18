# Explicit graph-spine collapses for square-free bipartite neighborhood complexes
## Finding
Let \(G\) be a finite connected simple bipartite square-free graph with bipartition \(A\sqcup B\), \(v=|V(G)|\), \(e=|E(G)|\), and \(\beta=e-v+1\). Choose one root \(r_b\in N_G(b)\) for every \(b\in B\) and one root \(s_a\in N_G(a)\) for every \(a\in A\). The Lovász neighborhood complex \(\mathcal N(G)\) simplicially collapses onto the disjoint union \(T_A\sqcup T_B\), where \(T_A\) has vertex set \(A\) and edges \(\{r_b,x\}\) for \(b\in B\) and \(x\in N_G(b)\setminus\{r_b\}\), and \(T_B\) is defined symmetrically using the \(s_a\). Both \(T_A\) and \(T_B\) are connected graphs of cycle rank \(\beta\). Consequently \(\mathcal N(G)\simeq (\bigvee^{\beta}S^1)\sqcup(\bigvee^{\beta}S^1)\), with \(\bigvee^0S^1\) interpreted as a point.

## Assumptions and scope
The graph \(G\) is finite, connected, simple, bipartite, and square-free, meaning that it contains no subgraph isomorphic to \(C_4\). Write the fixed bipartition as \(A\sqcup B\). The neighborhood complex \(\mathcal N(G)\) has the nonempty vertex subsets having a common neighbor as its simplices. Since \(G\) is bipartite, every simplex lies entirely in \(A\) or entirely in \(B\), so \(\mathcal N(G)=K_A\sqcup K_B\).

For every \(b\in B\), choose \(r_b\in N_G(b)\), and for every \(a\in A\), choose \(s_a\in N_G(a)\). Define \(T_A\) on \(A\) by
\[
E(T_A)=\bigl\{\{r_b,x\}:b\in B,\ x\in N_G(b)\setminus\{r_b\}\bigr\},
\]
and define \(T_B\) on \(B\) symmetrically. The choices are arbitrary; the conclusion holds for every such root system.

## Proof
For \(b\in B\), let \(\Delta_b\) be the simplex on \(N_G(b)\subseteq A\). Then \(K_A=\bigcup_{b\in B}\Delta_b\). Square-freeness implies
\[
|N_G(b)\cap N_G(c)|\le 1\qquad(b\ne c),
\]
because two distinct common neighbors of \(b\) and \(c\) would form a \(4\)-cycle.

Fix \(b\in B\). For every \(\sigma\subseteq N_G(b)\setminus\{r_b\}\) with \(|\sigma|\ge2\), pair \(\sigma\) with \(\sigma\cup\{r_b\}\). Perform these pairs in decreasing order of \(|\sigma|\), with arbitrary tie-breaking among different centers. When the pair for \(\sigma\) is reached, every strictly larger coface of \(\sigma\) inside \(\Delta_b\) has already been removed. No simplex \(\Delta_c\) with \(c\ne b\) can contain \(\sigma\), because \(|\sigma|\ge2\) and two vertices of \(\sigma\) would then be common neighbors of \(b\) and \(c\). Thus \(\sigma\) is a free codimension-one face of the unique remaining maximal coface \(\sigma\cup\{r_b\}\). Each pair is therefore an elementary simplicial collapse.

After all such pairs are removed, the contribution of \(\Delta_b\) consists only of its vertices and the edges \(\{r_b,x\}\) with \(x\in N_G(b)\setminus\{r_b\}\). Doing this for all \(b\in B\) gives \(K_A\searrow T_A\). The same construction gives \(K_B\searrow T_B\), hence
\[
\mathcal N(G)\searrow T_A\sqcup T_B.
\]

Different centers cannot create the same edge of \(T_A\): if \(b\ne c\) created \(\{x,y\}\), then \(x\) and \(y\) would be two common neighbors of \(b\) and \(c\). Therefore
\[
|E(T_A)|=\sum_{b\in B}(\deg_G(b)-1)=e-|B|.
\]
The graph \(T_A\) is connected. Indeed, an alternating path \(a_0,b_1,a_1,\ldots,b_k,a_k\) in \(G\) produces a walk in \(T_A\) from \(a_{i-1}\) to \(a_i\) through \(r_{b_i}\) for each \(i\). Connectedness of \(G\) supplies such a path between any two vertices of \(A\). Hence
\[
\operatorname{rank}H_1(T_A;\mathbb Z)=|E(T_A)|-|A|+1=e-v+1=\beta.
\]
The symmetric argument gives the same rank for \(T_B\). Every connected graph of cycle rank \(\beta\) is homotopy equivalent to \(\bigvee^{\beta}S^1\), proving the claim.

## Verification
The standalone verifier reconstructs the neighborhood complex and the stated collapse order for every connected labeled bipartite square-free graph on \(2\) through \(6\) vertices. It checks \(1{,}501\) graphs, \(17{,}850\) neighborhood-complex faces, and \(1{,}530\) elementary collapses. For every collapse it verifies directly that the lower simplex is present and has the stated unique remaining coface, then checks that the residue is exactly \(T_A\sqcup T_B\), that both target graphs are connected, and that their cycle ranks equal \(e-v+1\).

To stress-test degrees beyond the exhaustive small-graph range, the verifier also checks incidence graphs of the projective planes of prime orders \(2\), \(3\), and \(5\). Their cycle ranks are \(8\), \(27\), and \(125\), respectively, and all prescribed collapses pass. These finite calculations test the construction and implementation; they are not substitutes for the general proof above.

## Relationship to prior work
Shukla proved that for connected graphs of maximum degree at most \(3\), apart from two exceptional graphs, each neighborhood-complex component is contractible or a wedge of circles, and the proof collapses the degree-three case to a one-dimensional subcomplex. The present statement instead uses square-freeness to give a uniform root-prescribed collapse for connected bipartite graphs of arbitrary degree and identifies the exact surviving graph and cycle rank.

Matsushita proved a broad homotopy classification for \(\operatorname{Hom}(F,H)\) when the codomain \(H\) is square-free. Applied to \(F=K_2\), that framework covers the abstract homotopy type expected for a bipartite square-free neighborhood complex. The statement here is stronger in a different direction: it exhibits a monotone sequence of elementary simplicial collapses of the neighborhood complex itself onto an explicit root-dependent graph spine. The inspected theorem and proof statements do not provide this direct collapse or these root-parametrized spines.

The collapse method is also consistent with star-cluster and elementary-collapse techniques used in discrete topological combinatorics; Donovan and Scoville provide a methodological collapse reference with primary MSC \(57Q70\).

## Limitations
The square-free hypothesis is essential to the proof: a pair of centers with two common neighbors destroys both the uniqueness of the simplex center used in the free-face argument and the edge-count formula. The theorem does not assert that the chosen spine is canonical; different root choices can produce different embedded graph spines, although all have the same cycle rank. The literature comparison cannot exclude an unindexed equivalent direct-collapse formulation, and the 2024 square-free Hom-complex classification is close at the level of homotopy type even though it does not state the direct collapse proved here.

## References
1. S. Shukla, “Homotopy type of the neighborhood complexes of graphs of maximal degree at most 3 and 4-regular circulant graphs,” arXiv:1802.04526, first posted 2018-02-13; Electronic Journal of Combinatorics 26(2), 2019, #P2.4.
2. T. Matsushita, “Hom complexes of graphs whose codomains are square-free,” arXiv:2412.19144, first posted 2024-12-26; Journal of Combinatorial Theory, Series B 178 (2026), 267–293, DOI 10.1016/j.jctb.2026.01.005.
3. C. Donovan and N. A. Scoville, “Star clusters in the Matching, Morse, and Generalized Morse complex,” arXiv:2207.13780, first posted 2022-07-27; New York Journal of Mathematics 29 (2023), 1393–1412. Primary MSC 2020: \(57Q70\).
