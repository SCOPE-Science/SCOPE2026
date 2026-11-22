# Exact enumeration of binary universal cycles with at most two changes per window

## Finding
For an integer \(n\ge2\), let \(\mathcal W_n\) be the set of binary words \(w=w_1\cdots w_n\) having at most two changes between consecutive positions:
\[
\operatorname{ch}(w)=|\{i:1\le i<n,\ w_i\ne w_{i+1}\}|\le2.
\]
An *oriented universal cycle* for \(\mathcal W_n\) is a binary circular word with each member of \(\mathcal W_n\) occurring exactly once as a cyclic length-\(n\) factor, and no other length-\(n\) factors. Circular words are identified under rotation alone, not reversal or complementation.

**Theorem.** Such cycles exist for every \(n\ge2\), each has circumference
\[
|\mathcal W_n|=2\sum_{r=0}^{2}\binom{n-1}{r}=n^2-n+2,
\]
and the exact number of distinct oriented universal cycles is
\[
\boxed{U_n=2^{n-2}.}
\]
Moreover, the cycles correspond bijectively to independent binary choices on \(n-2\) internal one-change vertices of the overlap digraph; this yields an explicit Boolean-cube parametrization through in-arborescences and Euler circuits.

## Assumptions and scope
Words use the alphabet \(\{0,1\}\). Changes are counted *internally* in a length-\(n\) factor; the adjacency between its last and first symbols is not included. The circular host is read periodically, with exactly one length-\(n\) factor starting at each host position. Factors may cross the chosen linear representation's boundary. Equality of circular hosts means only equality up to rotation. The theorem is for every integer \(n\ge2\); it requires no fixed Hamming weight and no maximum bound on individual run lengths. The length count is immediate from choosing the first symbol and up to two of the \(n-1\) change positions.

## Proof
Put \(m=n-1\). Form a directed labeled graph \(G_n\) with one edge for each member \(w\) of \(\mathcal W_n\), from its length-\(m\) prefix to its length-\(m\) suffix. All vertices are length-\(m\) words with at most two changes. The graph is balanced: vertices with zero or one internal change have indegree and outdegree two, and those with exactly two internal changes have both degrees one. The latter must append their final symbol (and their only predecessor must prepend their initial symbol) to avoid introducing a third change. Each such degree-one vertex therefore belongs to a forced directed path between the branching vertices. Repeated forced extension eventually shifts away the first run, so every such path ends at a vertex with at most one change. Thus contracting all maximal forced paths preserves the rooted in-arborescence count and the cyclic Euler-tour count.

Index the \(2m\) branching vertices as
\[
A_j=0^{m-j}1^j\quad(0\le j\le m),\qquad
B_j=1^{m-j}0^j\quad(1\le j<m).
\]
These vertices are distinct; set \(A_0=0^m\), \(A_m=1^m\). For clarity, the notation \(B_0=A_m\) and \(B_m=A_0\) will be used for the endpoints. Following one outgoing edge and then all forced edges gives exactly these reduced transitions:
\[
\begin{array}{lll}
A_0\longrightarrow A_0,&A_0\longrightarrow A_1, &\\
A_j\longrightarrow A_{j+1},&A_j\longrightarrow B_{m-j},&1\le j<m,\\
A_m\longrightarrow A_m,&A_m\longrightarrow B_1, &\\
B_j\longrightarrow B_{j+1},&B_j\longrightarrow A_{m-j},&1\le j<m,
\end{array}
\]
where \(B_m=A_0\). In particular the forward arrows form the directed Hamiltonian cycle
\[
A_0\to A_1\to\cdots\to A_m\to B_1\to\cdots\to B_{m-1}\to A_0;
\]
the additional arrows are loops at \(A_0,A_m\) and reciprocal cross-links \(A_j\leftrightarrows B_{m-j}\).

Count directed in-arborescences toward root \(A_0\). Such a tree chooses one outgoing edge at each nonroot vertex, so that every vertex reaches \(A_0\). The outgoing edge chosen at \(A_m\) must be the forward edge to \(B_1\), rather than the loop. We prove successively for \(j=1,\ldots,m-1\) that \(B_j\) must choose the forward edge to \(B_{j+1}\) (with \(B_m=A_0\)). Suppose earlier \(B_h\), \(h<j\), have already been forced forward and \(B_j\) instead chooses the cross-link into \(A_{m-j}\). The nonempty set
\[
T_j=\{A_i:m-j\le i\le m\}\cup\{B_h:1\le h\le j\}
\]
is then forward-closed under the selected edges: the chosen edge at \(B_j\) returns to its \(A\)-part, smaller \(B_h\)'s advance inside the \(B\)-part, and any \(A_i\) in the set either moves forward along the \(A\)-part or crosses to \(B_{m-i}\) with \(1\le m-i\le j\). The vertex \(A_m\) moves to \(B_1\). Yet \(T_j\) excludes the root, contradicting the arborescence property. Hence all \(B\)-vertices are forced forward.

At each \(A_j\) with \(1\le j<m\), the forward choice eventually reaches \(A_m\) and then follows the forced \(B\)-chain to \(A_0\); the cross-link choice immediately enters that same forced \(B\)-chain. Every choice strictly advances toward the root in this sense, so there are no selected directed cycles. The \(m-1=n-2\) choices at the internal \(A\)-vertices are independent and freely binary. Therefore the in-arborescence count is
\[
\tau_{A_0}(G_n)=2^{m-1}=2^{n-2}.
\]
This argument also covers \(m=1\) (an empty set of free vertices). Expanding contracted forced paths preserves this count because their outgoing selections are compulsory.

Since \(G_n\) is balanced and has an in-arborescence, its positive-degree portion is connected and Eulerian. The directed BEST theorem enumerates Euler circuits with the unique edge \(0^n\) fixed as the first edge:
\[
U_n=\tau_{A_0}(G_n)\prod_{v\in V(G_n)}(\deg^+(v)-1)!=\tau_{A_0}(G_n),
\]
because every outdegree is one or two. Distinct edge labels are the distinct length-\(n\) factors; every Euler circuit therefore produces exactly one desired cyclic word and conversely. Moreover, the edge \(0^n\) occurs exactly once, so it selects a unique canonical rotation and no length division is needed. Thus \(U_n=2^{n-2}\), as asserted.

## Verification
The supplied pure-Python 3 script `verify_switch_universal.py` is standalone and uses only the standard library. It independently builds the permitted labeled overlap edges, computes exact directed in-arborescence counts from integer Laplacian cofactors using fraction-free Bareiss elimination for every \(2\le n\le10\), and checks the claimed count. For \(2\le n\le7\), it additionally enumerates **all** Euler tours beginning with the uniquely labeled loop \(0^n\), constructs the corresponding cyclic host words, and checks that their cyclic length-\(n\) factors coincide exactly with \(\mathcal W_n\). The verified counts are \(1,2,4,8,16,32\) for these six exhaustive Euler-order tests; Laplacian tree counts continue with \(64,128,256\) for orders eight through ten. The program prints `VERIFY_OK` upon success. Run `python3 verify_switch_universal.py` from the extracted package. These tests corroborate the all-length proof but do not replace it.

## Relationship to prior work
Leitner and Godbole, *Universal Cycles of Restricted Classes of Words* (arXiv:0808.1309, originally public August 2008), prove universal-cycle existence for several restricted classes. Blanca and Godbole, *On Universal Cycles for New Classes of Combinatorial Structures* (arXiv:1008.2251, originally public August 2010), prove existence for restricted subset and word families. Their inspected full texts do not give an exact enumeration for binary words with at most two adjacent changes. Other published universal-cycle enumerations for Hamming-weight-one/two windows impose a bound on the **number of ones**, not the number of changes; results on binary words with runs of length at most two instead limit **run length**, and in one instance minimize a cyclic cover that may repeat windows. Neither constraint is equivalent to the present all-length source language. Standard BEST/matrix-tree theorems are prior methods; the closed all-length arborescence classification in the transition-constrained graph is the distinct result claimed here.

## Limitations
This theorem does not address three or more changes, nonbinary alphabets, reversal/complement equivalence classes, code robustness to errors, or shortest hosts permitted to repeat compulsory windows. Its scientific priority remains subject to possible earlier unindexed equivalent statements. The numerical count happens to be a familiar sequence of powers of two, but only its particular constrained-universal-cycle interpretation and structural classification are asserted as a contribution.

## References
1. A. Leitner and A. P. Godbole, *Universal Cycles of Restricted Classes of Words*, arXiv:0808.1309, first public August 8, 2008. https://arxiv.org/abs/0808.1309
2. A. Blanca and A. P. Godbole, *On Universal Cycles for new Classes of Combinatorial Structures*, arXiv:1008.2251, first public August 13, 2010. https://arxiv.org/abs/1008.2251
3. N. G. de Bruijn, *A combinatorial problem*, 1946 (classical de Bruijn cycles).
4. Classical directed BEST and directed Matrix-Tree theorems (Euler-tour and arborescence enumeration).
