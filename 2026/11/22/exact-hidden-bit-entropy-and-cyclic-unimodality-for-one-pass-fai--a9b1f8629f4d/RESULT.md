# Exact hidden-bit entropy and cyclic-unimodality for one-pass fair switching on cycles

## Finding
Fix an integer \(k\geq3\), label the vertices of the simple cycle \(C_k\) by \(0,1,\ldots,k-1\), and let the edge \(e_j\) join \(j\) to \(j+1\pmod k\). Fix any ordering \(\omega=(e_{a_1},\ldots,e_{a_k})\) of its edges. Independently choose fair bits \(B_1,\ldots,B_k\), and define the random permutation
\[
P_\omega=\tau_{e_{a_k}}^{B_k}\cdots\tau_{e_{a_1}}^{B_1},
\]
where \(\tau_e\) exchanges the endpoints of \(e\). In the circular sequence of chronological edge ranks \(r_j\), call \(\omega\) *cyclically unimodal* if it has precisely one strict circular local minimum and one strict circular local maximum.

**Theorem.** For every \(k\geq3\) and every edge ordering \(\omega\):

1. If \(\omega\) is not cyclically unimodal, the map from the \(2^k\) private bit strings to output permutations is injective. Its output law is uniform on \(2^k\) permutations and its Shannon entropy is exactly \(k\) bits.
2. If \(\omega\) is cyclically unimodal, exactly two output permutations have two preimages each, and exactly \(2^k-4\) output permutations have one preimage each; there are no larger fibres. The output entropy is exactly \(k-2^{2-k}\) bits, its support has \(2^k-2\) elements, its min-entropy is \(k-1\) bits, and its Rényi entropy of order two is \(k-\log_2(1+2^{2-k})\) bits.
3. Precisely \(k2^{k-2}\) of the \(k!\) chronological orders are cyclically unimodal. Therefore, if the edge order is independently uniform, the probability of any bit-to-permutation ambiguity is \(2^{k-2}/(k-1)!\), and the **expected conditional Shannon entropy loss**, relative to the \(k\) fair hidden bits, is exactly
\[
\mathbb E_{\omega}[k-H(P_\omega\mid\omega)]=\frac1{(k-1)!}\quad\text{bits}.
\]
Here all entropies condition on the public order, and the averaging in the last display is only over that order.

This completely classifies output ambiguity in a natural one-pass fair switching network whose possible switches form a single simple cycle. For comparison, a one-pass network on any forest has an injective private-bit map for every edge order; thus the cycle gives the first nonforest case. The theorem does **not** assert the same criterion for cyclic components with interspersed pendant switches, or for schedules containing repeated edges.

## Assumptions and scope
All edge transpositions are distinct and occur exactly once. There is no null switch, no repeated edge, no additional adjacent pendant edge, and no dependence between the fair switch bits. The underlying cycle has \(k\ge3\) vertices. The public order can be arbitrary, and its randomness is invoked only in conclusion 3. Entropies are in base two. The support counts refer to distinct permutations of the \(k\) labelled vertices, not to conjugacy classes or cycle types.

## Proof
**1. Forest subset products.** For any proper subset \(F\subsetneq E(C_k)\), the chosen edge graph is a forest. Reading its chosen edge transpositions in the inherited chronological order, each added edge joins two distinct connected components of the previously selected forest, and hence merges two cycles of the currently induced permutation. Inductively, the final permutation has exactly one permutation cycle on the vertices of each component of \((V,F)\), including singleton fixed points. Consequently, its cycle-support partition equals its graph-component partition. For a forest whose available edge graph is fixed, these partitions uniquely identify the chosen edge subset: an edge is included exactly when its endpoints belong to the same component, since the unique path between endpoints is that edge.

For the ambient cycle \(C_k\), a proper edge subset is instead determined uniquely by its component partition **except** when that partition has one block containing all \(k\) vertices. The exceptional proper subsets are the \(k\) spanning paths obtained by omitting exactly one edge. Indeed, when at least two edges are absent, each connected component is a proper consecutive arc of the cycle, with its selected internal edges uniquely determined.

The full edge set produces exactly two permutation cycles: after \(k-1\) edges have been applied the selected edges form a spanning tree and the permutation is a single \(k\)-cycle; the final edge has both endpoints in this cycle and splits it into two cycles. Hence the full-edge output could agree with a proper-subset output only when that proper subset omits exactly two edges and has exactly two components.

**2. Algebraic collision criterion.** Write the chronological transpositions as \(t_1,\ldots,t_k\). Suppose positions \(i<j\) are omitted and all other bits are one. Write \(U=t_{j-1}\cdots t_{i+1}\), the ordered product between these positions. Comparing the permutation using every edge except \(t_i\) with the permutation using every edge except \(t_j\), and cancelling the common outer prefix and suffix, gives the exact criterion
\[
t_j U=U t_i. \tag{1}
\]
Comparing the permutation using **all** edges with the permutation using all edges **except** \(t_i,t_j\) gives the same criterion (1). These are the only potential collisions by step 1.

Equality (1) says that the action of \(U\) maps the unordered pair of endpoints of \(t_i\) onto the unordered pair of endpoints of \(t_j\). Delete the two corresponding cycle edges from \(C_k\). The remaining edges form two disjoint paths, allowing a one-vertex path if the deleted edges meet. To transport the two endpoint vertices along the two paths, every edge of both nontrivial paths must occur in \(U\): removing any one of these edges separates an endpoint from its required target, and no transposition in \(U\) crosses that cut. Thus every edge other than \(t_i,t_j\) lies temporally strictly between them; necessarily \(i=1\) and \(j=k\).

Conversely, suppose \(t_1\) is the first and \(t_k\) the last edge. Their deletion leaves two paths. A product of distinct adjacent transpositions along a path carries its designated starting endpoint to its opposite endpoint exactly when those transpositions are applied in chronological order starting from that designated endpoint (the unique-path transport criterion). Therefore, (1) holds exactly when the chronological ranks increase along both of the circular arcs from \(t_1\) toward \(t_k\). Equivalently, the circular chronological-rank sequence has one strict local minimum, at \(t_1\), and one strict local maximum, at \(t_k\): cyclic unimodality.

When this condition holds, precisely two pairs of different bit strings collide: (a) the word containing every edge except the earliest versus the word containing every edge except the latest, and (b) the all-edges word versus the word containing every edge except those two extremes. The first pair outputs a single \(k\)-cycle, whereas the second pair outputs two cycles, so these are distinct output permutations. No other pair collides by the component-partition argument. When cyclic unimodality fails, no pair collides.

**3. Exact order count.** Choose the earliest edge in \(k\) ways. For a possible latest edge, the remaining \(k-2\) cycle edges form two paths of lengths \(r\) and \(k-2-r\), for one \(r\in\{0,\ldots,k-2\}\). Cyclic unimodality forces the relative order along each path, leaving \(\binom{k-2}{r}\) interleavings. Summing over the latest edge gives
\[
k\sum_{r=0}^{k-2}\binom{k-2}{r}=k2^{k-2}
\]
good chronological orders. Division by \(k!\) gives their exact probability.

**4. Information calculation.** In the unimodal case, two outputs have probability \(2/2^k\) each and \(2^k-4\) outputs have probability \(1/2^k\) each. Direct substitution into Shannon's definition gives \(H=k-4/2^k=k-2^{2-k}\). The largest probability is \(2^{1-k}\), proving the min-entropy; the collision sum is \((2^k+4)/2^{2k}\), proving the Rényi-2 formula. In the nonunimodal case all probabilities are \(2^{-k}\). Finally,
\[
\frac{k2^{k-2}}{k!}\cdot\frac4{2^k}=\frac1{(k-1)!}
\]
is the exact expected entropy deficit. This proves the theorem.

## Verification
The standalone script `checker.py` exhaustively enumerates every chronological order and every bit string on simple cycles of lengths \(3\) through \(8\), checks cyclic unimodality and the entire fibre multiplicity spectrum, checks the order counts and expected-entropy identities exactly as rational numbers, tests selected larger cycles, and independently verifies forest injectivity on three families. Run with `python checker.py` using Python 3 and no external libraries. Its deterministic execution yielded 277,769 successful assertion-group checks; sample counts of bad orders for \(k=3,4,5,6,7,8\) are \(6,16,40,96,224,512\), respectively. The finite enumeration is not the proof for arbitrary \(k\); the preceding arguments prove all lengths.

## Relationship to prior work
Mironov (first public November 2, 2026) studies conditional mixing of the random-pair Monte shuffle with **many** publicly selected, possibly repeated transpositions and independent hidden fair bits. The present result restricts the public edge support to an exactly once-used cycle and derives the previously unaddressed *bit-to-output injectivity*, exact fibre counts and conditional information loss. Its finite one-pass entropy statement is not obtained from an asymptotic mixing-time estimate.

Dénes's tree-transposition lemma, discussed by Cameron and Stott and by Tsujie and Uchiumi, supplies the forest permutation-cycle fact credited and used in the proof. Cameron and Stott study **variation of the order of all edges of a fixed tree** and multiplicities of resulting full cycles; this is not the private subset-of-edges law on a fixed cycle. Tsujie and Uchiumi examine full-support products, cycles and graph embeddings, not the full \(2^k\)-word fibre or Shannon entropy spectrum. A search of the cited full-text primary sources and other available literature did not establish that the information-loss formula was previously published; search absence is not a proof of priority.

## Limitations
The theorem is a structural finite probabilistic result; it does not improve the mixing time of the random-pair Monte shuffle or establish cryptographic security. It only treats one pass on a single simple cycle, with arbitrary temporal order and independent fair bits. Attaching extra switches to that cycle can change the collision structure, so the criterion must not be extrapolated to a generic unicyclic graph. Prior results about transposition factorizations may contain equivalent special identities under a different formulation; historical originality is provisional and independent expert assessment is absent.

## References
- I. Mironov, *Mixing Time of the Random-Pair Monte Shuffle*, arXiv:2611.03959, first posted 2026-11-02, https://arxiv.org/abs/2611.03959.
- P. J. Cameron and L. Stott, *Trees and cycles*, arXiv:2010.14902, 2020, https://arxiv.org/abs/2010.14902.
- S. Tsujie and R. Uchiumi, *Upper Embeddability of Graphs and Products of Transpositions Associated with Edges*, arXiv:2211.05422, 2022, https://arxiv.org/abs/2211.05422.
- J. Dénes, *The representation of a permutation as the product of a minimal number of transpositions and its connection with the theory of graphs*, 1959, cited for the classical tree-transposition principle.
