# All distance-edge-monitoring sets of complete split graphs
## Finding
Let
\[
S_{m,n}=K_m\vee\overline{K_n}
\]
be the complete split graph with clique
\[
C=\{c_1,\ldots,c_m\},
\qquad m\ge1,
\]
and independent set
\[
I=\{u_1,\ldots,u_n\},
\qquad n\ge1.
\]

If \(m=1\), then \(S_{1,n}\) is a star and every nonempty vertex set is distance-edge-monitoring.

If \(m\ge2\), then a set \(M\subseteq V(S_{m,n})\) is distance-edge-monitoring if and only if either
\[
C\subseteq M,
\]
or
\[
M=V(S_{m,n})\setminus\{c\}
\]
for some \(c\in C\).

Define the distance-edge-monitoring set enumerator
\[
\mathcal D_{m,n}(z)
=
\sum_{\substack{M\subseteq V(S_{m,n})\\M\text{ distance-edge-monitoring}}}
z^{|M|}.
\]
Then
\[
\mathcal D_{1,n}(z)=(1+z)^{n+1}-1,
\]
while for \(m\ge2\),
\[
\mathcal D_{m,n}(z)
=
z^m(1+z)^n+mz^{m+n-1}.
\]

In particular,
\[
\operatorname{dem}(S_{m,n})=
\begin{cases}
1,&m=1,\\
m,&m\ge2.
\end{cases}
\]
For \(m\ge2\) and \(n\ge2\), the clique \(C\) is the unique minimum distance-edge-monitoring set. For \(m\ge2\) and \(n=1\), the graph is complete and all \(m+1\) sets of size \(m\) are minimum. For \(m=1\), all \(n+1\) singletons are minimum.

## Assumptions and scope
All graphs are finite, simple, connected, and undirected.

A vertex \(x\) monitors an edge \(e\) if there exists a vertex \(y\) such that every shortest \(x,y\)-path contains \(e\). Equivalently, deleting \(e\) increases \(d(x,y)\) for at least one \(y\). A vertex set is distance-edge-monitoring if every edge is monitored by at least one selected vertex.

The result classifies every monitoring set of every complete split graph \(K_m\vee\overline{K_n}\), not only sets of minimum cardinality.

## Proof
First suppose \(m=1\). Then \(S_{1,n}\) is a tree. Every edge of a tree is a bridge. For any vertex \(x\) and any bridge \(e\), deleting \(e\) separates the graph into two components; choosing \(y\) in the component opposite \(x\) shows that every shortest \(x,y\)-path uses \(e\). Hence every vertex monitors every edge. Thus precisely the nonempty vertex sets are distance-edge-monitoring.

Now suppose \(m\ge2\). We show that every vertex monitors exactly its incident edges.

Every clique vertex \(c\in C\) is universal. Hence every other vertex lies at distance one from \(c\). If an edge \(e\) is not incident with \(c\), deleting \(e\) does not change any distance from \(c\): all other vertices remain adjacent to \(c\). Thus \(c\) monitors only its incident edges.

Fix \(u\in I\). Its distance layers are
\[
L_0(u)=\{u\},
\qquad
L_1(u)=C,
\qquad
L_2(u)=I\setminus\{u\}.
\]
Every vertex of \(I\setminus\{u\}\) has all \(m\ge2\) clique vertices as neighbors in \(L_1(u)\). Therefore no edge from \(L_1(u)\) to \(L_2(u)\) is the unique predecessor edge of its \(L_2(u)\)-endpoint. Edges inside \(C=L_1(u)\) also cannot be forced on a shortest path from \(u\). Hence \(u\) monitors no nonincident edge. Of course every vertex monitors each edge incident with it, by choosing the other endpoint as \(y\).

Thus, when \(m\ge2\), a set monitors every edge exactly when it contains at least one endpoint of every edge; in other words, the distance-edge-monitoring sets are precisely the vertex covers.

It remains to classify the vertex covers of \(S_{m,n}\). A set \(M\) is a vertex cover exactly when its complement is independent. Every independent set of \(S_{m,n}\) is either an arbitrary subset of \(I\), or a singleton \(\{c\}\) with \(c\in C\). Therefore every vertex cover is either
\[
C\cup J,
\qquad
J\subseteq I,
\]
or
\[
V(S_{m,n})\setminus\{c\},
\qquad
c\in C.
\]
For \(n\ge1\), these two families are disjoint.

The first family contributes
\[
z^m(1+z)^n,
\]
and the second contributes
\[
mz^{m+n-1},
\]
which proves the enumerator. The minimum-size and basis statements follow immediately.

## Verification
The included verifier constructs every complete split graph with
\[
1\le m,n\le6.
\]
For each edge \(e\) and probe vertex \(x\), it recomputes all distances after deleting \(e\), thereby determining directly whether \(x\) monitors \(e\). It then tests every vertex subset against the distance-edge-monitoring definition.

The verifier independently compares the direct results with the two-family classification, every coefficient of the enumerator, the minimum value, and the number of minimum sets.

## Relationship to prior work
Distance-edge monitoring was introduced in 2020. The foundational paper proves that every vertex cover is distance-edge-monitoring and characterizes when a graph has the stronger property that every vertex monitors only its incident edges; in that situation, the distance-edge-monitoring sets coincide with the vertex covers.

A 2025 proceedings paper specifically studies complete split graphs and proves the scalar formula
\[
\operatorname{dem}(K_k\vee\overline{K_{n-k}})=k
\]
in the nondegenerate complete-split range, with the star and complete-graph boundary cases handled separately. The present result strictly refines that scalar theorem by classifying every feasible monitoring set, giving a closed cardinality enumerator, and determining every minimum set.

A 2024 paper on perturbations of the distance-edge-monitoring number lists MSC 2020 class \(05C12\), confirming the graph-theoretic classification used here.

Targeted searches for complete split graphs together with distance-edge-monitoring sets, all-set classifications, generating functions, and monitoring-set polynomials did not locate the enumerator or the complete feasible-set classification stated above.

## Limitations
The theorem concerns complete split graphs only.

The minimum-value formula for this family is prior work. The new content is the all-set classification, exact enumerator, and complete description of minimum sets, including the star and complete-graph boundaries.

The direct computation is finite and corroborative only. The theorem for arbitrary \(m,n\) follows from the proof that, for \(m\ge2\), every vertex monitors exactly its incident edges.

The full proceedings PDF for the 2025 scalar predecessor was not retrievable through the checked public endpoint during this review; the indexed proceedings text exposed the abstract, theorem statement, proof outline, boundary cases, and conclusion used for comparison.

## References
1. F. Foucaud, S.-S. Kao, R. Klasing, M. Miller, J. Ryan, “Monitoring the edges of a graph using distances,” arXiv:2011.00029v1, 30 October 2020; Discrete Applied Mathematics 319 (2022), 424–438, DOI 10.1016/j.dam.2021.07.002.
2. C. Yang, R. Klasing, C. He, Y. Mao, “Perturbation Results for Distance-edge-monitoring Numbers,” Fundamenta Informaticae 191 (2024), 141–163, DOI 10.3233/FI-242176.
3. M. Milivojević Danas, J. Kratica, “Distance-edge-monitoring number of complete split graphs,” Proceedings of the 52nd Symposium on Operational Research, Palić, 2025, 208–211, DOI 10.5281/zenodo.17533261.
