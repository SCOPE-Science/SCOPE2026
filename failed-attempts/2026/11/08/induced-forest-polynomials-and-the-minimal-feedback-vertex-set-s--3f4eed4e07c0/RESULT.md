# Induced-forest polynomials and the minimal feedback-vertex-set spectrum of crown graphs

## Finding
For each integer \(n\ge4\), write \(H_n=K_{n,n}-M_n\) for the labelled **crown graph** with shores \(A=\{a_1,\ldots,a_n\}\) and \(B=\{b_1,\ldots,b_n\}\), with \(a_i\) adjacent to \(b_j\) if and only if \(i\ne j\). For a vertex subset \(S\), the induced subgraph \(H_n[S]\) is a forest if it has no cycle.

Let \(P_n(z)=\sum_{S:\,H_n[S]\,\text{is a forest}}z^{|S|}\), and let \(F_n(z)\) count only the **inclusion-maximal** such \(S\). Then
\[
P_n(z)=2(1+z)^n-1+2nz\big((1+z)^n-1\big)-n^2z^2+\binom{n}{2}(2n-3)z^4+n(n-1)(n-2)z^5
\]
and
\[
\boxed{F_n(z)=2nz^{n+1}+n(n-1)(n-2)z^5.}
\]
The two terms of the second formula count two disjoint structural classes, except that their exponents coincide when \(n=4\).

The complements of these maximal forest subsets are exactly the inclusion-minimal **feedback vertex sets** (vertex sets whose deletion destroys all cycles). Their size polynomial is
\[
\boxed{T_n(z)=2nz^{n-1}+n(n-1)(n-2)z^{2n-5}.}
\]
Thus the minimum feedback vertex set size is \(n-1\); the largest size of an inclusion-minimal feedback vertex set is \(2n-5\). For \(n\ge5\) both sizes occur, with gap \(n-4\); for \(n=4\) both formulas give size three.

## Assumptions and scope
All graphs are finite simple undirected graphs; all vertices and matched indices are distinguished. The statement covers every integer \(n\ge4\), with neither quotient by graph automorphisms nor implicit restrictions to connected forests. 'Maximal' means maximal under vertex-set inclusion, not necessarily of maximum cardinality. All polynomials use the number of **selected vertices** as exponent. The small graph \(H_3\) is deliberately excluded from the maximal-forest formula because its full-shore stars are extendable.

## Proof
**1. Exact possible shore sizes.** Write a selected vertex set as \(S=A_I\cup B_J\) for index subsets \(I,J\subseteq[n]\). Whenever \(|I|\ge3\) and \(|J|\ge3\), choose three indices from each. The six corresponding vertices span at least \(9-3=6\) edges, since at most three of the nine potential cross-edges belong to the deleted matching. A forest on six vertices has at most five edges; hence \(H_n[S]\) contains a cycle. Likewise, if \(|I|=2\) and \(|J|\ge4\), at least two indices in \(J\) lie outside \(I\). Those two vertices of \(B_J\) together with the two vertices of \(A_I\) form a four-cycle. This also holds with the shores interchanged.

When \(|I|\le1\) or \(|J|\le1\), the induced subgraph is always a forest: it is a star together with isolated vertices. The only remaining cases with both shores of size at least two are \((|I|,|J|)=(2,2),(2,3),(3,2)\). For two selected vertices on each shore, the sole possible cycle is a four-cycle, which occurs precisely when the two index sets are disjoint. Thus \((2,2)\) is permitted if and only if \(I\cap J\ne\varnothing\). For \(|I|=2,|J|=3\), the graph contains a four-cycle precisely when at least two indices of \(J\) lie outside \(I\). Hence it is a forest if and only if \(I\subset J\), in which case the induced subgraph is a five-vertex path. The \((3,2)\) case is symmetric. These conditions exhaust all possible forests.

**2. Every forest counted.** The subsets with one entire shore empty contribute \(2(1+z)^n-1\) (the empty subset is counted only once). Subsets whose smaller nonempty shore has exactly one selected vertex contribute \(2nz((1+z)^n-1)\), with the \(n^2\) two-vertex cross-shore subsets counted twice; subtract \(n^2z^2\). In the \((2,2)\) case, first choose \(I\) in \(\binom n2\) ways; then \(J\) must intersect \(I\), leaving \(\binom n2-\binom{n-2}2=2n-3\) choices. Finally, choose a two-index shore in \(\binom n2\) ways, one extra index outside it in \(n-2\) ways, and either orientation, giving \(2\binom n2(n-2)=n(n-1)(n-2)\) five-vertex paths. Adding disjoint cases proves \(P_n(z)\).

**3. Inclusion maximality.** A set missing a shore can be enlarged by adding a vertex on that shore without creating a cycle. A forest with exactly one vertex on one shore can be enlarged by adding all missing vertices of the other shore, so maximality forces a whole shore plus one vertex. Conversely, in such a full-shore configuration, adding any further vertex on the singleton shore creates a four-cycle: the two selected shore vertices have at least \(n-2\ge2\) common neighbors on the full shore. Thus exactly \(2n\) maximal forests are full-shore stars (possibly with one isolated selected vertex).

Every forest with two vertices on each shore can be enlarged to a \((2,3)\) or \((3,2)\) forest: if both index sets coincide, append an index outside them; if they share exactly one index, append the missing index from the two-element shore to the other shore. For a forest with two vertices on one shore and at most one vertex on the other, first complete the latter to the same two indices plus one extra index. Hence no remaining smaller forest is maximal. Conversely, a permitted \((2,3)\) forest is an induced five-vertex path. Adding a vertex to its three-vertex shore yields a \((2,4)\) configuration with a four-cycle; adding to its two-vertex shore yields a \((3,3)\) configuration with a cycle. Thus every such path is maximal. Its count was found in step 2. These are all maximal forests, proving \(F_n(z)\).

**4. Minimal feedback vertex sets.** A set \(X\subseteq V(H_n)\) is a feedback vertex set precisely when \(V(H_n)\setminus X\) induces a forest. It is inclusion-minimal precisely when its complement is an inclusion-maximal forest. Replacing each exponent \(k\) of \(F_n(z)\) by \(2n-k\) yields \(T_n(z)\). The claimed extremal sizes and gap follow immediately, completing the proof.

## Verification
The accompanying `verify.py` independently constructs each labelled graph from its cross-shore adjacency rule. It tests acyclicity of every induced vertex subset using union-find cycle detection, then checks whether any single omitted vertex can be added while preserving acyclicity. Orders \(n=4,5,6,7,8\) exhaustively cover \(256+1024+4096+16384+65536=87296\) labelled subsets. All coefficients of \(P_n\) and \(F_n\), and both maximal structural types, agree with direct enumeration. Further integer arithmetic checks run for \(4\le n<150\). Finite checks supplement but do not replace the unrestricted proof.

## Relationship to prior work
Gaikwad, Kumar, Maity, Saurabh, and Tripathi study maximum-size **minimal** feedback vertex sets and the parameterized complexity of this problem [1]. Johnston, Kayll, and Palmer study perfect matchings in \(K_{n,n}-M_n\), the same underlying graph family, under the derangement interpretation [2]. A later paper by Ghalavand and Li proves that any balanced bipartite graph on \(2n\) vertices with minimum degree at least \(n/2+1\) has largest induced forest of cardinality \(n+1\) [3]; in particular, it already implies the **scalar minimum feedback vertex set size** \(n-1\) for the crown graph when \(n\ge4\). Its odd-order structural theorem also constrains largest forests. Neither this scalar equality nor the basic maximal/minimal complement duality is claimed as new. The additional assertions here are the complete all-forest polynomial, the classification and cardinality polynomial of *all inclusion-maximal* forests (including the nonmaximum five-vertex paths), and the full minimal-feedback-set size spectrum and multiplicities.

## Limitations
The theorem covers the fixed full-matching deletion family only, not arbitrary matchings deleted from rectangular bipartite graphs. The result gives labelled enumerations, not orbit counts. Publication priority is provisional: no equivalently strong result was identified in the inspected sources or database searches, but material may exist under other descriptions of maximal acyclic vertex sets or minimal cycle transversals. No independent mathematical audit has been performed.

## References
[1] A. Gaikwad, H. Kumar, S. Maity, S. Saurabh, S. K. Tripathi, *Maximum Minimal Feedback Vertex Set: A Parameterized Perspective*, arXiv:2208.01953, first public version 2022-08-03. https://arxiv.org/abs/2208.01953

[2] D. Johnston, P. M. Kayll, C. Palmer, *Deranged matchings: proofs and conjectures*, arXiv:2209.11319, first public version 2022-09-22. https://arxiv.org/abs/2209.11319

[3] A. Ghalavand, X. Li, *On Maximum Induced Forests of the Balanced Bipartite Graphs*, arXiv:2501.05145, first public version 2025-01-09 (later supporting literature). https://arxiv.org/abs/2501.05145
