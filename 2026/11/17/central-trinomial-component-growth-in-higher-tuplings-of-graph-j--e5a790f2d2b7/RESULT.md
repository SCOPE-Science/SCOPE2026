# Central-trinomial component growth in higher tuplings of graph joins

## Finding
Let \(r\ge4\), and let \(G_1,\ldots,G_r\) be finite connected simple graphs, each containing an odd cycle. Regard each graph as a **one-dimensional** simplicial complex (all triangles remain unfilled), and put \(X=G_1*\cdots*G_r\). Write \(v_i=|V(G_i)|\), \(e_i=|E(G_i)|\), and \(P=\prod_{i=1}^r e_i\).

The simplicial \(r\)-tupling \(D^r(X)\) is a graph. Its connected components are indexed by orbits of balanced words \(w\in\{0,1,2\}^r\) (equivalently, \(\sum_iw_i=r\)) under \(w\mapsto2-w\). For the all-ones word, the component is the categorical graph product \(\prod_i^{\times}G_i\) and has
\[
V_0=\prod_i v_i,\qquad E_0=2^{r-1}P,\qquad \beta_0^{(1)}=E_0-V_0+1.
\]
For each remaining orbit, select a representative word \(w\) and let \(F=\{i:w_i=2\}\), \(Z=\{i:w_i=0\}\), \(B=\{i:w_i=1\}\), and \(k=|F|=|Z|\ge1\). Define \(e_F=\prod_{i\in F}e_i\), \(e_Z=\prod_{i\in Z}e_i\), and \(v_B=\prod_{i\in B}v_i\), with empty products equal to one. This component is canonically
\[
\left(\prod_{i\in B}^{\times}G_i\right)\times K_{e_F,e_Z}\quad\text{if }B\ne\varnothing,
\]
and is \(K_{e_F,e_Z}\) if \(B=\varnothing\). Its vertex count, edge count, and circle rank are precisely
\[
V_w=v_B(e_F+e_Z),\qquad E_w=2^{r-2k}P,\qquad \beta_w=E_w-V_w+1.
\]
All listed graphs are connected, so their realizations are wedges of exactly the indicated numbers of circles, with no higher homology or torsion. In particular the total number of connected components is the **central-trinomial law**
\[
\boxed{\#\pi_0(D^r(X))=\frac12\left(1+\sum_{k=0}^{\lfloor r/2\rfloor}\frac{r!}{k!^2(r-2k)!}\right).}
\]
For \(r=4\) this is ten components; for \(r=5\) it is twenty-six. The count is independent of all graph sizes and internal edges, subject to the stated connectedness/nonbipartiteness conditions.

In particular, if every factor is an unfilled odd polygon \(C_{m_i}\), \(m_i\ge5\), then \(|X|\cong S^{2r-1}\) (a PL sphere). Thus a natural simplicial tupling of an arbitrarily high-dimensional combinatorial sphere has a number of connected components growing with the central trinomial coefficient, and every component has an explicit free fundamental group.

## Assumptions and scope
The parameter \(r\) is an integer at least four. Each graph is finite, undirected, loopless, simple, connected and nonbipartite; no flag-complex filling is applied within the factors. The simplicial join has all facets consisting of one edge from each factor, hence dimension \(2r-1\). The operation \(D^r\) uses the definition of Lesh–Schreiner–Wahl: vertices are \(r\)-element faces of \(X\); distinct vertices are adjacent exactly if disjoint and their union is a face of \(X\). The absence of faces with \(3r\) vertices makes \(D^r(X)\) one-dimensional. Empty categorical products are not used: the \(B=\varnothing\) case is stated separately.

## Proof
**1. Exhaustive occupancy partition.** Every \(r\)-element face \(\sigma\subset X\) intersects each factor in zero, one, or two vertices, with two vertices required to form an edge of that factor. Let \(w_i=|\sigma\cap V(G_i)|\). Then \(\sum_i w_i=r\), so the numbers of zeroes and twos coincide. Conversely, every balanced occupancy word is realized, since each factor contains edges and vertices. Any such \(\sigma\) extends to a facet: complete its local zero- or singleton-selections to an edge in each factor. Thus no vertices are missing or isolated in the description.

**2. Precisely which patterns can be adjacent.** If \(\sigma\) and \(\tau\) form an edge of \(D^r(X)\), their union is a \(2r\)-vertex face, necessarily an edge in every factor. Consequently the local occupancies obey \(w_i(\sigma)+w_i(\tau)=2\). Thus adjacency can occur only between a word \(w\) and its involution \(\bar w=2-w\). Conversely, for a compatible assignment of local factor edges and endpoints, those two faces do form an edge of \(D^r(X)\). Hence different involution orbits have no connecting edges.

**3. Exact graph decomposition.** For the unique fixed pattern \((1,\ldots,1)\), a vertex is a choice of one vertex of each \(G_i\), and two such choices are adjacent precisely when their coordinates are adjacent in every factor. This is the categorical product \(\prod_i^{\times}G_i\).

For a nonfixed pair \(\{w,\bar w\}\), a vertex of type \(w\) is a choice of an edge in every factor of \(F\), a single vertex in every factor of \(B\), and nothing in factors of \(Z\). The opposite side reverses \(F\) and \(Z\). Every pair of complementary edge choices is compatible; in each \(B\) factor, the two singleton choices must be endpoints of an edge. This is exactly the categorical product of the graphs \(G_i\) for \(i\in B\) with \(K_{e_F,e_Z}\), or just the biclique if \(B\) is empty. These are graph isomorphisms, not merely homotopy approximations.

**4. Connectedness.** A finite connected nonbipartite graph admits, between any fixed two vertices, walks of both parities and of every sufficiently large length of either chosen parity. Indeed, connect to an odd cycle to switch parity and add two-step backtracks to lengthen. Therefore a categorical product of any positive number of the \(G_i\) is connected: for two product vertices, choose a common sufficiently long walk length in all factors. When \(B\ne\varnothing\), also fix a path of appropriate parity between any two vertices of the complete bipartite factor, and choose its sufficiently large length in every \(G_i\). Hence its categorical product is connected. When \(B\) is empty, \(K_{e_F,e_Z}\) is connected since the edge counts are positive. Thus every pattern orbit produces **exactly one** component.

**5. Counts and integral homotopy.** The all-ones product has \(\prod_i v_i\) vertices. Each combination of one undirected edge in each factor permits \(2^r\) endpoint assignments; dividing by two for reversal gives \(2^{r-1}P\) edges. For a nonfixed pattern there are \(v_Be_F\) vertices on one side and \(v_Be_Z\) on the other. Each choice of an edge in every factor and of one of two orientations in each \(B\) factor gives a distinct undirected edge, totaling \(2^{|B|}P\). A finite connected graph with \(V\) vertices and \(E\) edges collapses along a spanning tree to a wedge of \(E-V+1\) circles; this is integral and detects the entire homotopy type. Counting balanced words with \(k\) zeroes and \(k\) twos gives \(r!/(k!^2(r-2k)!)\). Complementation fixes only the all-ones word, so the involution has \((T_r+1)/2\) orbits, where \(T_r\) is the indicated central trinomial sum. This completes the proof for every allowed parameter list.

**6. Sphere specialization.** Each unfilled cycle \(C_{m_i}\) is a simplicial \(S^1\). Iterated simplicial join of \(r\) such cycles triangulates \(S^{2r-1}\); odd lengths ensure the preceding connectedness theorem applies. The stated component and circle counts follow without any additional assumptions.

## Verification
The accompanying standalone script `check.py` generates the face graph **directly from all top-dimensional faces** of each join, not from the claimed product decomposition. Every \(2r\)-element facet is partitioned into two \(r\)-subsets in all possible ways, and the resulting adjacency is checked against every legal \(r\)-face. The program enumerates actual connected components and their vertex and edge counts, and compares these with the formulas above. It verifies \(r=4\) and \(r=5\), including a mixture of odd cycles, unfilled complete graphs, and a wheel. Its exact output appears in `check_output.txt` and ends with `BALANCED_PATTERN_JOIN_TUPLING_PASS`. The finite checks are independent corroboration, not the infinite proof.

For four unfilled triangles, the components have circle ranks \(568\) once, \(271\) six times, and \(64\) three times, giving ten components. For four unfilled pentagons, the corresponding ranks are \(4376\), \(2251\), and \(576\), with multiplicities one, six, and three.

## Relationship to prior work
Lesh, Schreiner and Wahl introduced simplicial \(r\)-tupling and proved a general connectivity-transfer theorem (arXiv:2506.10436v1). Their original definition is used here. Their paper does not give this balanced-occupancy graph isomorphism, the central-trinomial component count, or componentwise free-group ranks for joins of arbitrary nonbipartite graph factors.

The classical theorem on connected categorical graph products (Weichsel, *The Kronecker product of graphs*, 1962) supplies background; for completeness, a direct common-length-walk proof is given above. Previously investigated three-factor three-tuplings and multipartite tuple graphs address restricted constructions. The present claim includes all tuple orders \(r\ge4\), arbitrary nonbipartite connected graph factors and the simultaneous numerical component/rank classification. This is a calculation for a new infinite class, not a claim that the definition of tupling or product connectivity is new.

## Limitations
The formula for a **single** component per pattern orbit need not hold if several factors are bipartite; additional parity splitting may occur. The theorem does not classify disconnected graph factors, general higher-dimensional join factors, arbitrary complexes not of this join form, equivariant circle representations, or higher tupling orders different from the number of joined factors. The proof is mathematical, while the script checks only its listed finite instances. An equivalent result under different terminology in unindexed literature remains an originality risk; independent external validation has not been performed.

## References
1. K. Lesh, B. Schreiner and N. Wahl, *The Double of a Simplicial Complex*, arXiv:2506.10436v1, first posted 2025-06-12. https://arxiv.org/abs/2506.10436
2. P. M. Weichsel, *The Kronecker product of graphs*, Proceedings of the American Mathematical Society **13** (1962), 47–52. https://doi.org/10.2307/2033769
