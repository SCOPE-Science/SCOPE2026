# A sharp sphere-to-contractible transition for directed feedback theta networks

## Finding

Let \(D\) consist of \(m\ge2\) internally disjoint directed forward paths \(P_i:s\to t\) of arc lengths \(L_i\ge2\), together with one directed return path \(Q:t\to s\) of arc length \(r\ge1\), disjoint from all forward paths except at the distinct terminals \(s,t\). There are no additional arcs. Its ordinary multipath complex \(X(D)\) has the arcs as vertices; a face is a set of arcs whose components are directed simple paths or isolated graph vertices. Let \(h=\#\{i:L_i\ge3\}\). For \(h\ge1\), the ordinary homotopy type of the geometric realization is
\[
X(D)\simeq
\begin{cases}
S^{r+L-2},&h=1\text{ and the unique long arm has length }L,\\
\ast,&h\ge2.
\end{cases}
\]
The result is a homotopy classification, not just a computation of Betti numbers. The all-two-edge case \(h=0\) is outside the claim.

## Proof

Write \(E_i\) for the arc set of \(P_i\), \(a_i,b_i\) for its first and last arcs, \(I_i=E_i\setminus\{a_i,b_i\}\), and \(I=\coprod_i I_i\). Write \(C\) for the return arc set and \(\Delta(U)\) for the simplex on a vertex set \(U\).

A set of arcs is a multipath if and only if its selected indegrees and outdegrees are at most one and it has no directed cycle. The only degree restrictions are at most one first arc \(a_i\) and at most one last arc \(b_i\), because the return uses the other direction of incidence at each terminal and all other path vertices are private. Every directed simple cycle is exactly \(E_i\cup C\) for some \(i\). Let \(H=K_{m,m}\) on the first and last arcs as a one-dimensional simplicial complex, and let \(K=H*\Delta(I)\). Thus \(K\) is the forward-arc degree complex. Define its subcomplex \(K'\) by excluding all faces containing an entire \(E_i\). These facts give the simplicial union
\[
X(D)=(K*\partial\Delta(C))\ \cup_{K'*\partial\Delta(C)}\ (K'*\Delta(C)).
\]
Indeed, a proper subset of the return arcs cannot complete any directed cycle, while the entire return set is allowed only with a face of \(K'\). If \(r=1\), the boundary consists only of the empty face and joining with it leaves a simplicial complex unchanged.

Since \(h\ge1\), \(K\) is a cone on any vertex of \(I\). Both pieces of the union are contractible: the first is a cone on such a vertex, and the second on any return arc. The inclusions of their intersection are cofibrations, since these are simplicial subcomplexes. The union therefore has the homotopy type of the homotopy pushout of two maps from the intersection to points, namely the unreduced suspension of that intersection. When \(r=1\) the intersection is \(K'\). When \(r\ge2\), the intersection realizes the join of \(K'\) with \(S^{r-2}\), which is the \((r-1)\)-fold suspension of \(K'\). The intersection is nonempty (for instance \(K'\) contains every singleton forward arc). In all cases,
\[
X(D)\simeq\Sigma^r K'.
\]

**One long arm.** Let \(j\) be its index and \(q=|I_j|=L-2\). Let \(H_{\times}\subset H\) contain all first and last arc vertices but only the off-diagonal edges \(\{a_i,b_k\}\) with \(i\ne k\). Set \(e=\{a_j,b_j\}\), regarded as a simplex. All diagonal edges for \(i\ne j\) must be excluded: each by itself is the entire short arm \(E_i\). A face whose endpoint arcs form the long diagonal edge \(e\) may use only a proper subset of \(I_j\), whereas if its endpoint arcs form a face of \(H_{\times}\), all subsets of \(I_j\) are allowed. Hence
\[
K'=(H_{\times}*\Delta(I_j))\ \cup_{\partial e*\partial\Delta(I_j)}\ (e*\partial\Delta(I_j)).
\]
Both pieces are cones, and the intersection is \(S^{q-1}\): for \(q=1\) it is the two vertices of \(\partial e\); for \(q\ge2\) it is \(S^0*S^{q-2}\). As above the union is the homotopy pushout, so \(K'\simeq S^q\) and \(X(D)\simeq S^{r+L-2}\).

**At least two long arms.** Choose private internal arc vertices \(x\in I_i\) and \(y\in I_j\) with \(i\ne j\). For every face of \(K'\), at least one of \(x,y\) can be adjoined. Neither addition creates a degree conflict, and the only way adding one can fail is to complete its own arm, which requires both endpoints of that arm to be present in the face. The two arms cannot both have their endpoint arcs selected. Hence the two closed stars of \(x\) and \(y\) cover \(K'\). Their intersection is the closed star of \(\{x,y\}\): if the two individual additions are allowed, adding both cannot introduce any degree conflict or complete an arm not already completed by an individual addition, since the arcs belong to different arms. The edge \(\{x,y\}\) itself is a face. The two stars and their intersection are nonempty cones. Their union is contractible by the same homotopy-pushout argument, and so is \(X(D)\) by the suspension formula.

## Verification and scope

For a direct check of the one-long-arm decomposition, take \(m=2\), \((L_1,L_2)=(3,2)\). The forward degree complex has 18 faces including the empty face. For \(K'\), delete the short diagonal and its union with the private arc of the long arm, and delete the full long arm: 15 faces remain. For \(r=1\) this gives \(18+15=33\) faces of \(X(D)\), agreeing with the recorded directed-arc enumeration. The supplied `verify_mixed_feedback.py` compares the global face condition with direct degree and cycle tests and computes reduced mod-two Betti numbers for twelve finite examples; these checks do not establish the homotopy classification. The proof above is for ordinary homotopy and makes no equivariant claim. Extra chords or reverse arcs, multiple return paths and length-one forward arms are not covered.

## Relationship to prior work

Caputi, Collari, Di Trani and Smith classify the multipath complexes of oriented polygons and describe joins over dynamical modules. The alternating-orientation equivalence with matching complexes does not apply here. The all-short triangular and long-page books give the baseline \(h=0\) for one- and multi-arc returns, respectively. The result above is for \(h\ge1\); in particular the graph with one long arm is not just a coherently oriented polygon. The source–sink feedback result concerns top-dimensional Hamiltonian-path classes for one added return arc and does not give this full homotopy classification. The comparisons are bounded and do not rule out unindexed equivalent work.

1. L. Caputi, C. Collari, S. Di Trani and J. P. Smith, *On the homotopy type of multipath complexes*, [arXiv:2208.04656v1](https://arxiv.org/abs/2208.04656), §§2, 4.
2. *Equivariant collapse of consistently oriented triangular-book multipath complexes*, published mathematical record, corresponding to all \(L_i=2\) and \(r=1\).
3. *Equivariant sphere bouquets for coherently oriented long-page cycle books*, published mathematical record, corresponding to all \(L_i=2\) and \(r\ge2\).
4. *Source–sink feedback edges split off Hamiltonian-path spheres in multipath complexes*, published mathematical record.
