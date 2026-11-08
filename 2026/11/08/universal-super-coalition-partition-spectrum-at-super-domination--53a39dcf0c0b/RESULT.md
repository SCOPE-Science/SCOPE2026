# Universal super-coalition partition spectrum at super-domination defect at most two

## Finding
Let \(G\) be any finite simple graph with no isolated vertices, order \(n\ge6\), and super domination number \(\gamma_{\mathrm{sp}}(G)\ge n-2\). Define the *feasible-pair graph* \(H\) on \(V(G)\) by making distinct vertices \(u,v\) adjacent precisely when \(V(G)\setminus\{u,v\}\) is super dominating in \(G\). Write \(e=|E(H)|\), \(m_2(H)\) for the number of unordered pairs of disjoint edges of \(H\), \(m_3(H)\) for the number of perfect matchings of \(H\) when \(n=6\), and \(t(H)\) for its triangle count. Let \(c_k(G)\) count unordered, labelled-vertex super-coalition partitions into exactly \(k\) nonempty classes. Then
\[
\begin{aligned}
c_2(G)&=2^{n-1}-1-n-e,\\
c_3(G)&=\binom n2-e+(n-2)e+m_2(H)-2\mathbf1_{\{n=6\}}m_3(H),\\
c_4(G)&=t(H),\\
c_k(G)&=0\quad(k\ge5).
\end{aligned}
\]
In particular, \(c_3(G)>0\) and the super-coalition number is \(4\) exactly when \(H\) contains a triangle, and is \(3\) otherwise. Every four-class partition consists of three singleton classes corresponding to a triangle of \(H\), plus their nonempty complement; its coalition graph is the three-leaf star. Every three-class partition has coalition graph a three-vertex path, except when \(n=6\) and its three blocks are disjoint edges of \(H\), in which case it is a triangle.

For complete multipartite \(G=K_{n_1,\dots,n_r}\), where \(r\ge2\), \(n_i\ge2\) and \(N=\sum_i n_i\ge6\), the feasible-pair graph is exactly \(G\). Put \(E=\sum_{i<j}n_i n_j\) and \(Q=\binom E2-\sum_i n_i\binom{N-n_i}{2}\). The full explicit specialisation is
\[
\begin{aligned}
c_2&=2^{N-1}-1-N-E,\\
c_3&=\sum_i\binom{n_i}{2}+(N-2)E+Q-2\mathbf1_{\{N=6\}}m_3(G),\\
c_4&=\sum_{i<j<k}n_i n_j n_k.
\end{aligned}
\]
Here \(m_3(G)\) means the number of perfect matchings of the six-vertex graph, appearing only when \(N=6\). Hence \(C_s(K_{n_1,\dots,n_r})=3\) for \(r=2\) and \(4\) for \(r\ge3\). For instance, the coefficient vectors \((c_2,c_3,c_4)\) are \((16,48,0)\) for \(K_{3,3}\) and \((13,65,8)\) for \(K_{2,2,2}\).

## Assumptions and scope
Graphs are finite, simple, undirected, and without isolated vertices. A selected set \(D\subseteq V(G)\) is *super dominating* when every omitted vertex \(u\notin D\) has a selected witness \(v\in D\) such that \(N_G(v)\cap(V(G)\setminus D)=\{u\}\). The super domination number is the minimum size of such a \(D\). A *super-coalition partition* is a partition into at least two nonempty vertex subsets, none itself super dominating, and each with at least one other distinct class whose union is super dominating. Classes are unordered, original vertices are labelled, and \(C_s(G)\) is the maximum number of classes. The restriction \(n\ge6\) makes the size profiles in the counting argument disjoint; smaller orders are not claimed.

The hypothesis \(\gamma_{\mathrm{sp}}(G)\ge n-2\) is a genuine condition, not an assertion about arbitrary graphs. No assumption that \(H\) is connected is needed. Every singleton omission is feasible because the original graph has no isolated vertices; by hypothesis no omission of at least three vertices is feasible. Accordingly, the complements of the super dominating sets are precisely the empty set, individual vertices, and edges of \(H\). No classification or assertion of novelty for the previously known complete-multipartite super dominating sets is made.

## Proof
**Lemma 1 (the complement criterion).** If \(U\subseteq V(G)\), then \(V(G)\setminus U\) is super dominating if and only if \(|U|=0\), or \(|U|=1\), or \(|U|=2\) with \(U\in E(H)\). The empty case is vacuous. In the one-vertex case, a neighbour of the omitted vertex is selected and witnesses it. The two-vertex case is the definition of \(H\). For \(|U|\ge3\), feasibility would give a super dominating set of at most \(n-3\) vertices, contradicting \(\gamma_{\mathrm{sp}}(G)\ge n-2\). This proves the lemma.

Every union of two partition classes can therefore be super dominating only if all other classes together have size at most two. For \(k\ge5\), those other \(k-2\ge3\) nonempty classes contain at least three vertices, a contradiction. Thus \(c_k=0\) for \(k\ge5\).

**Two classes.** Every unordered bipartition has union \(V(G)\), hence is a coalition unless one of its blocks is itself super dominating. There are \(2^{n-1}-1\) unordered bipartitions. A block is super dominating exactly when its opposite block is a singleton (\(n\) possibilities) or an edge of \(H\) (\(e\) possibilities). Because \(n\ge6\), these forbidden bipartitions are all distinct and cannot have two super dominating blocks. Therefore \(c_2=2^{n-1}-1-n-e\).

**Three classes.** Each class must have a partner. Each successful coalition leaves the third class omitted, so by Lemma 1 that third class is either a singleton or a two-vertex edge of \(H\). The coalition graph on the three classes has no isolated vertices, hence at least two of the classes have one of those two permitted forms. Distinguish cases according to these two or more small classes:

(i) If at least two classes are singleton vertices \(u,v\), the third class has size \(n-2\). It is not itself super dominating precisely when \(\{u,v\}\notin E(H)\). Each singleton has the large class as partner because that union omits just the other singleton. The number is \(\binom n2-e\).

(ii) If exactly one class is a singleton \(u\) and another is a two-vertex edge \(\{v,w\}\in E(H)\), the remaining class has size \(n-3\ge3\) and is not super dominating. The singleton partners the large class (omitting edge \(\{v,w\}\)), and the edge block partners the large class (omitting \(u\)). Every choice of an edge and a vertex outside it yields exactly one partition, so the count is \((n-2)e\).

(iii) If no class is a singleton, at least two classes must be disjoint two-vertex edges of \(H\). Choosing two disjoint \(H\)-edges determines the remaining block, of size \(n-4\ge2\). If \(n>6\), the remaining block has size at least three and is therefore not super dominating; the two edge blocks each partner the remainder, so the count is \(m_2(H)\). For \(n=6\), the remaining block also has size two. If it is not an \(H\)-edge, the same count is unique. If it *is* an \(H\)-edge, then all three blocks are \(H\)-edges, and every such partition has been counted three times, one for each choice of two among its three blocks; exactly \(m_3(H)\) such partitions exist. Correcting the overcount by subtracting \(2m_3(H)\) proves the formula for \(c_3\). The coalitions are a path in (i), (ii), and the non-triangular instances of (iii), and a triangle in the exceptional perfect-matching case.

**Four classes.** A union of two blocks can be super dominating only when the other two blocks are *both singleton* vertices, since their total size must be at most two. Consequently every class that has a partner must belong to a pairing leaving two singleton blocks. If only two blocks were singleton, those two would be isolated in the coalition graph; hence there are at least three singleton blocks. Since \(n\ge6\), precisely three singleton blocks \(\{u\},\{v\},\{w\}\) and one other block \(B\) occur. The three singletons can only partner \(B\). The union \(B\cup\{u\}\) omits \(\{v,w\}\), which is feasible iff \(vw\in E(H)\), and similarly for the other two singleton partners. Thus the three vertices form a triangle in \(H\). Every triangle determines exactly one valid partition; all its blocks are non-super dominating because the largest has size \(n-3\). The coalition graph is a star centered on \(B\). This proves \(c_4=t(H)\).

**Existence of a three-class partition.** If \(H\) is not complete, choose a nonedge of \(H\) and use construction (i). If \(H\) is complete, choose any edge \(vw\) and any third vertex \(u\), using construction (ii). Thus \(c_3>0\) for every \(n\ge6\), proving the formula for \(C_s\).

**Multipartite specialization.** On a complete multipartite graph with all part sizes at least two, a feasible omitted pair must join different parts. Indeed, if the omitted pair lies in one part, no selected vertex can witness just one of them; if the two omitted vertices are in distinct parts, a selected vertex in each of their respective parts witnesses the other omitted vertex. The earlier complete-multipartite super-domination characterization additionally rules out omitted triples, verifying the universal hypothesis. Consequently \(H=G\). The number of unordered pairs of disjoint edges is \(Q=\binom E2-\sum_{v\in V(G)}\binom{\deg(v)}2=\binom E2-\sum_i n_i\binom{N-n_i}2\), since two distinct edges share at most one vertex. Triangles choose one vertex from three different parts, giving \(t(G)=\sum_{i<j<k}n_i n_j n_k\). Finally \(\binom N2-E=\sum_i\binom{n_i}2\). Substitution proves every displayed multipartite identity.

## Verification
Run the included standalone `verify.py` under Python 3, with no external packages. It independently constructs the graph and directly tests the defining witness condition for every candidate super dominating set; it constructs the feasible-pair graph, independently computes its edge/disjoint-edge/perfect-matching/triangle statistics, and enumerates **all** unordered vertex partitions to check every coefficient. It exhaustively checks 15 complete multipartite part-size vectors, every eligible six-vertex labelled graph (24,509 graphs), and fixed-seed tests of 197 eligible seven-vertex and 108 eight-vertex graphs. Successful output ends with `VERIFY_OK`.

As a meaningful boundary example, two connected six-vertex graphs with exactly the same all-super-dominating-set polynomial \(z^6+6z^5+6z^4\) nevertheless have different super-coalition spectra: one has \((c_2,c_3,c_4)=(19,39,0)\), while the other has \((19,42,2)\). Explicit edge lists appear in the checker. Hence the previously known size-only super-domination enumerator does **not** determine the super-coalition number. Finite checks support the proof but do not replace the unrestricted combinatorial argument above.

## Relationship to prior work
The super-coalition notion and its motivating families are introduced in Alikhani and Ghanbari's 2026 preprint. The foundational super domination witness criterion appears in Lemańska and collaborators' 2013 work. A prior 2026 public mathematical research record entitled *All super dominating sets of complete multipartite graphs* already proves the three-term complete-multipartite super-domination polynomial and characterizes its feasible omitted pairs. Those results are used as background, not claimed as original. In contrast, the theorem here counts *partitions* whose classes can form coalitions, determines the partner graph topology, and gives a universal auxiliary-graph criterion for \(C_s\). Even identical super-domination size enumerators can correspond to different super-coalition numbers, as demonstrated explicitly. The source comparison found no earlier statement equivalent to the complete partition-spectrum identities; historical priority remains provisional.

## Limitations
The universal statement requires \(n\ge6\), no isolated vertices, and \(\gamma_{\mathrm{sp}}\ge n-2\); graphs outside this defect-two class may have more than four coalition classes. The multipartite formulas require every part to have at least two vertices. The motivating 2026 preprint's abstract was accessible but its plausible full manuscript was not retrieved, so complete historical priority comparison with that particular text is not established; related work may use alternative terminology. The verifier covers finite graphs only, while the proof establishes the unrestricted quantified theorem.

## References
1. S. Alikhani and N. Ghanbari, *Super Coalition Number in Graphs*, arXiv:2607.22686, first public 2026-07-15.
2. M. Lemańska, V. Swaminathan, Y. B. Venkatakrishnan and R. Zuazua, *Super dominating sets in graphs*, arXiv:1309.1315 (2013).
3. *All super dominating sets of complete multipartite graphs*, publicly available mathematical research record (2026), full result and proof inspected.
