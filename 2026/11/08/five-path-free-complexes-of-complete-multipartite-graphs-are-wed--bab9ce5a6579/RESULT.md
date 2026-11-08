# Five-path-free complexes of complete multipartite graphs are wedges of three-spheres

## Finding
Let \(m\ge3\), let \(n_1,\ldots,n_m\ge1\), and put \(N=\sum_{i=1}^m n_i\ge5\). For the complete multipartite graph \(G=K_{n_1,\ldots,n_m}\), let \(\operatorname{PF}_5(G)\) be the simplicial complex of vertex sets that contain **no simple path on five distinct vertices** in the induced graph. Such a path need **not** be induced. With out-of-range binomial coefficients understood as zero, set
\[
B(n_1,\ldots,n_m)=\binom{N-1}{4}-\sum_{i=1}^{m}\left(\binom{n_i-1}{4}+(N-n_i)\binom{n_i-1}{3}\right).
\]
Then \(B(n_1,\ldots,n_m)\) is a nonnegative integer and
\[
\boxed{\operatorname{PF}_5(G)\simeq\bigvee^{B(n_1,\ldots,n_m)} S^3.}
\]
The wedge with zero summands means a contractible space. In particular, reduced integral homology is free of rank \(B\) in degree three and vanishes in all other degrees, and the fundamental group vanishes.

For instance, the ranks for \(K_{2,2,2}\), \(K_{3,3,3}\), and \(K_{4,4,4}\) are respectively \(5\), \(70\), and \(306\). The last example fails sequential Cohen–Macaulayness by the obstruction in the motivating paper, yet its homotopy type is a wedge of spheres.

## Assumptions and scope
All graphs are finite simple undirected graphs; all vertices have distinct identities, even within one part. The parts \(V_i\) of \(G\) are disjoint, nonempty, and their union is its full vertex set \(V\). A five-vertex path is a sequence of five **distinct** vertices with consecutive vertices adjacent; additional chords are permitted. Realizations of simplicial complexes are used when writing homotopy equivalences. The theorem covers all part sizes with at least three parts and at least five total vertices, with no equal-size or connectivity restriction beyond those assumptions.

For a finite vertex set \(W\), let \(\Delta_W\) be its full simplex. We write \(\Delta_W^{(3)}\) for its three-dimensional skeleton. Binomial coefficients satisfy \(\binom ab=0\) when \(a<b\) or \(b<0\). A zero-dimensional skeleton includes the empty face.

## Proof
**1. Path characterization.** For any vertex subset \(S\subseteq V\) with \(|S|\ge5\), write \(a_i=|S\cap V_i|\). There is a simple five-vertex path in \(G[S]\) if and only if \(|S|-\max_i a_i\ge2\). The forward implication follows because five consecutive vertices cannot lie in the same part, so no part contributes four of the five vertices. For the converse, if at least two vertices lie outside the largest part, select five vertices with each part contributing at most three; arrange the selected part labels so adjacent labels differ. Such an arrangement exists: choosing at most three from the largest part and at least two outsiders gives the pattern \(i,j,i,k,i\) when three from one part are chosen; any more balanced choice admits alternating labels (the criterion that no color occurs more than three times among five). Consecutive vertices from different parts are adjacent. Hence the subsets in the complex are precisely all sets of size at most four and the larger sets that have at most one vertex outside some part.

**2. Contractible cover.** Let \(A=\Delta_V^{(3)}\). For each part put
\[
F_i=\Delta_{V_i}*\bigl(\Delta_{V\setminus V_i}^{(0)}\bigr),
\]
where a face of \(F_i\) contains any number of vertices of \(V_i\) and at most one vertex outside \(V_i\). Each \(F_i\) is contractible because it is a join with the nonempty simplex \(\Delta_{V_i}\). Step 1 gives the exact identity
\[
K:=\operatorname{PF}_5(G)=A\cup\bigcup_{i=1}^{m}F_i.
\]
For distinct \(i,j\), every face shared by \(F_i\) and \(F_j\) has at most two vertices, since each such face has at most one vertex outside each of two disjoint parts. Thus \(F_i\cap F_j\subset A\). All of \(A\)'s faces of dimension at most three already belong to \(A\); adding the \(F_i\) attaches only cells of dimension at least four.

**3. The attaching links.** Let \(L_i=F_i\cap A=F_i^{(3)}\). Because \(F_i\) is contractible and has no cells beyond \(L_i\) of dimension less than four, its inclusion of its three-skeleton induces isomorphisms on \(\pi_j\) for \(j\le2\). In particular \(L_i\) is two-connected. It is three-dimensional, hence has no reduced homology below degree three and has \(\widetilde H_3(L_i;\mathbb Z)\) free. Its face counts for \(1\le q\le4\) are
\[
f_{q-1}(L_i)=\binom{n_i}{q}+(N-n_i)\binom{n_i}{q-1}.
\]
Euler characteristic and the alternating binomial identities now yield
\[
\operatorname{rank}\widetilde H_3(L_i;\mathbb Z)=c_i
=\binom{n_i-1}{4}+(N-n_i)\binom{n_i-1}{3}.
\]
This holds when \(L_i\) is a point or contractible (the right side then vanishes). The complete three-skeleton \(A\) is also two-connected, and its well-known skeleton calculation, obtainable by cellular induction on the number of vertices, gives
\[
\widetilde H_3(A;\mathbb Z)\cong\mathbb Z^{\binom{N-1}{4}},\qquad\widetilde H_j(A;\mathbb Z)=0\quad(j\ne3).
\]

**4. Integral primitivity.** Every oriented three-simplex of \(L_i\) has at least three vertices in \(V_i\). Hence the sets of three-simplices of \(L_i\) and \(L_j\) are disjoint whenever \(i\ne j\). As \(L_i\) has no four-simplices, \(H_3(L_i;\mathbb Z)\) is exactly the kernel of the cellular boundary \(\partial_3:C_3(L_i;\mathbb Z)\to C_2(L_i;\mathbb Z)\). This kernel is a **saturated sublattice** of its free integral three-chain group: if an integer multiple of a chain has zero boundary, the chain itself has zero boundary. Distinct \(i\) have disjoint chain-coordinate supports, so the direct sum of these kernels is saturated in \(C_3(A;\mathbb Z)\). It lies inside \(H_3(A;\mathbb Z)\subset C_3(A;\mathbb Z)\), and is therefore also saturated there. In particular the inclusion-induced map
\[
\bigoplus_i\widetilde H_3(L_i;\mathbb Z)\longrightarrow\widetilde H_3(A;\mathbb Z)
\]
is injective with torsion-free cokernel of rank \(\binom{N-1}{4}-\sum_i c_i=B\). This also proves \(B\ge0\).

**5. Relative homology and homotopy type.** Since all \(F_i\cap F_j\subset A\), the relative cellular chain groups of \((K,A)\) split as the direct sum of those of \((F_i,L_i)\). Contractibility of \(F_i\) and the homology of \(L_i\) show that the only possibly nonzero relative group is \(H_4(K,A;\mathbb Z)\cong\bigoplus_i H_3(L_i;\mathbb Z)\). The connecting homomorphism in the pair's exact sequence is precisely the inclusion map of Step 4. Therefore \(H_4(K;\mathbb Z)=0\),
\[
\widetilde H_3(K;\mathbb Z)\cong\mathbb Z^{B},
\]
and every other reduced integral homology group vanishes. Since \(K\) is obtained from two-connected \(A\) by attaching simplices of dimension at least four, \(K\) is itself two-connected. The Hurewicz theorem identifies \(\pi_3(K)\) with \(H_3(K;\mathbb Z)\). Choose based sphere maps representing a basis; their wedge \(\bigvee^B S^3\to K\) is an integral homology equivalence between simply connected CW complexes. The homological Whitehead theorem makes it a homotopy equivalence. For \(B=0\), the same theorem identifies \(K\) as contractible. This proves the stated formula over \(\mathbb Z\), including its homotopy conclusion.

## Verification
The standalone script `verify_pf5.py` constructs the actual five-vertex-path-free simplicial complex by inspecting every five-element subset and all permutations of its vertices, independently of the structural cover used in the proof. It computes simplicial boundary ranks in characteristics two and three, compares all reduced Betti numbers with the asserted dimension and rank, and tests every ordered multipartite composition with \(2\le m\le5\) and \(5\le N\le8\): \(199\) cases in each characteristic. It also prints representative ranks for larger parameter tuples (those larger tuples are formula evaluations, not homology enumerations). The recorded output is in `verify_output.txt`.

These finite field calculations are corroboration, not proof of integral torsion-freeness, primitivity, or the infinite statement. The integral chain proof in Steps 3–5 supplies those facts.

## Relationship to prior work
Deshpande, Goyal, and Sawant (2026), *On a complete characterization of path-free complexes associated with complete multipartite graphs*, identify the cover structure in their Lemma 3.5, treat bipartite path-free complexes in Theorem 4.3 and the three-path-free case for general multipartite graphs in Theorem 4.5, and pose the general wedge-of-spheres conjecture (Conjecture 4.7) and exact sphere-count question (Question 4.8). The cover itself is **not** claimed as new. The present theorem proves the next odd-path case \(t=5\) for every complete multipartite graph with at least three parts and gives an exact rank and integral homotopy classification; this is not implied by the cited bipartite and three-path results.

Deshpande and Singh (2020), *Higher independence complexes of graphs and their homotopy types*, study the different condition that every connected component of an induced subgraph has bounded size. In a complete multipartite graph, forbidding a five-vertex path is not equivalent to bounding all connected-component sizes by four: a five-vertex induced star is path-free but has a five-vertex connected component. The path-free and higher-independence theories therefore cannot be interchanged in this proof.

Related computations for four-path-free multipartite complexes and complete split graphs do not imply this uniform five-path-free theorem: the former forbids a smaller path, and the latter restricts the multipartite graph to a different parameter subfamily. Search comparisons did not locate a mathematically dominating result, but absence of an indexed match cannot establish absolute priority.

## Limitations
This is an **ordinary** (nonequivariant) integral homotopy classification. It does not determine the automorphism representation on its three-dimensional homology, an equivariant wedge decomposition, or the path-free homotopy type for thresholds \(t\ge6\). It concerns paths as not-necessarily-induced subgraphs, not induced-path avoidance. The proof relies on a specific elementary-cover pattern that can change for other forbidden path lengths. Independent external mathematical validation has not been performed.

## References
1. P. Deshpande, S. Goyal, R. Sawant, *On a complete characterization of path-free complexes associated with complete multipartite graphs*, arXiv:2607.05358v1, first posted July 6, 2026. https://arxiv.org/abs/2607.05358.
2. P. Deshpande, A. Singh, *Higher independence complexes of graphs and their homotopy types*, arXiv:2001.05448v2. https://arxiv.org/abs/2001.05448.
