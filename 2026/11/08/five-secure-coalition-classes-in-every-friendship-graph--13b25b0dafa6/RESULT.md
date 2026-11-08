# Five secure coalition classes in every friendship graph

## Finding
For each integer \(m\ge 2\), let \(F_m=K_1\vee(mK_2)\) be the friendship graph with one universal vertex \(h\) and \(m\) disjoint peripheral pairs \(P_i=\{a_i,b_i\}\). For the secure-coalition number defined using ordinary secure domination,
\[
\boxed{\operatorname{SEC}(F_m)=5\qquad(m\ge2).}
\]
The bound is independent of the number of triangles, even though the order of \(F_m\) is \(2m+1\). A quotient-multigraph characterization below also decides whether **any** proposed partition is a secure-coalition partition, and therefore recognizes every five-class optimum, using only incidences and edge-cover tests.

## Assumptions and scope
Graphs are finite, simple and undirected. A set \(S\) dominates when every vertex outside \(S\) has a neighbor in \(S\). It *securely dominates* if, for every \(u\notin S\), some neighbor \(v\in S\) can be exchanged for \(u\) while preserving domination. Two disjoint sets form a secure coalition when neither securely dominates alone but their union does. A secure-coalition partition has nonempty classes, each of which is either a **securely dominating singleton** of degree \(n-1\), or is not securely dominating and has a secure-coalition partner among the other classes. In \(F_m\) for \(m\ge2\), no singleton is securely dominating: the peripheral vertices are not universal and \(\{h\}\) leaves at least two untouched pairs. Consequently **every** block in a valid partition is nonsecure and must have a partner.

Here \(F_m\) has exactly one universal vertex for \(m\ge2\). All statements concern this definition, rather than ordinary, total, restrained, or global coalitions. Vertices of peripheral pairs are labelled; the partition classes themselves are unordered.

## Proof
**Secure-set lemma.** Let \(e(S)\) be the number of peripheral pairs not meeting \(S\). Directly from the secure-domination definition,
\[
S\text{ securely dominates }F_m\quad\Longleftrightarrow\quad
\begin{cases}
e(S)\le1,&h\in S,\\
e(S)=0,&h\notin S.
\end{cases}
\]
Indeed, without the center, domination requires one selected vertex in each peripheral pair. A missing peripheral vertex can be defended by exchanging it with its selected pairmate, and the unselected center can be defended by exchanging it with any selected peripheral vertex. With the center selected, an unrepresented pair can only be defended by exchanging the center for one of its vertices; after that exchange every other pair must remain represented. This is possible precisely when there is at most one unrepresented pair. If there are no unrepresented pairs, peripheral exchanges with selected pairmates suffice.

**The quotient and its exact test.** Given any partition \(\pi\), call the unique class containing \(h\) by \(H\). Form a loop-allowing multigraph \(Q\) whose vertices are the classes of \(\pi\). For every peripheral pair \(P_i\), draw one edge between the classes containing \(a_i\) and \(b_i\); if both lie in one class, draw a loop. Keep multiplicities. For any set \(T\) of quotient vertices let \(r(T)\) denote the number of these \(m\) edges having no endpoint in \(T\). The secure-set lemma proves the exact equivalences
\[
B\text{ securely dominates}\Longleftrightarrow r(\{B\})=0\quad(B\ne H),
\]
\[
H\text{ securely dominates}\Longleftrightarrow r(\{H\})\le1,
\]
\[
B\cup C\text{ securely dominates}\Longleftrightarrow
\begin{cases}
r(\{B,C\})\le1,&H\in\{B,C\},\\
r(\{B,C\})=0,&H\notin\{B,C\}.
\end{cases}
\]
Thus a partition passes the complete quotient test exactly when **every** non-center class \(B\) satisfies \(r(\{B\})\ge1\), the center class satisfies \(r(\{H\})\ge2\), and **every** class has a distinct nonsecure partner satisfying the corresponding displayed pair-union condition. This includes the case \(H=\{h\}\), which is not itself securely dominating for \(m\ge2\). This is a necessary-and-sufficient finite combinatorial characterization of every admissible partition. It needs no search over vertex-exchange strategies.

**Upper bound.** Consider any admissible partition. Every class, including \(H\), is nonsecure. Therefore at least two edges of \(Q\) avoid \(H\). In particular the multigraph \(Q-H\) contains two distinct edges (possibly parallel, or loops). No class \(B\ne H\) individually meets all quotient edges, since that would make \(B\) securely dominating and forbidden as a class.

If \(Q-H\) contains two edges \(e,f\) whose endpoint supports are disjoint, every other class \(B\ne H\) must be an endpoint of one of these two edges. Otherwise \(B\) cannot partner with \(H\), because both edges survive, and cannot partner with any other class \(C\), because no single \(C\) meets both disjoint edges. These supports contain at most four classes, so the partition has at most five classes.

In the remaining case, every pair of edges of \(Q-H\) has intersecting support. Choose two distinct edges \(e,f\) and write \(U\) for the union of their supports and \(I\) for the intersection. Any class \(B\ne H\) outside \(U\) cannot partner with \(H\), and any possible non-center partner \(C\) must belong to \(I\), in order to meet both \(e\) and \(f\). A fixed \(C\in I\) cannot partner with two distinct classes \(B,B'\) outside \(U\): if both pairs cover all quotient edges, every edge not incident to \(C\) must have both \(B\) and \(B'\) as endpoints. Such an edge would be disjoint from \(e\), contrary to the hypothesis on \(Q-H\); if no such edge exists, \(C\) itself covers all quotient edges, making it an impermissible securely dominating non-center class. Hence at most one class outside \(U\) is partnered with each \(C\in I\). The number of non-center classes is at most
\[
|U|+|I|=|\operatorname{supp}(e)|+|\operatorname{supp}(f)|\le4.
\]
Loops and repeated edges are included because each support has at most two endpoints. Therefore every admissible partition has at most five classes.

**Sharp construction.** Keep the center together with both vertices of any \(m-2\) peripheral pairs in one class \(H\); place each vertex of the remaining two pairs in its own singleton class. For \(m=2\), \(H=\{h\}\); it still misses exactly two pairs and is not securely dominating. For larger \(m\) the same is true of \(H\). Each peripheral singleton misses at least one pair and is not securely dominating. Its union with \(H\) misses just one peripheral pair, so it is securely dominating by the lemma. In particular, every class including \(H\) has a valid nonsecure coalition partner. Thus this is a secure-coalition partition with exactly five classes, completing the proof.

## Verification
The standalone standard-library script `verify.py` constructs the graph from its adjacencies, independently tests domination after every legal guard exchange, and compares all secure subsets with the secure-set lemma for \(2\le m\le7\). It then enumerates every unordered set partition for \(m=2,3,4,5\), returning maxima \(5,5,5,5\) and respective numbers of labelled-vertex maximum partitions \(1,81,1174,12290\). For \(m\le4\), it additionally checks the quotient test against the independently evaluated guard-exchange definition on every partition. The run terminates with `VERIFY_OK`. These finite checks are not the proof for unbounded \(m\); the argument above is.

## Relationship to prior work
Shetty, Udupa and Rakshith introduced secure coalitions and proved general bounds, including \(\operatorname{SEC}(G)\ge\delta(G)+2\) for suitable isolate-free noncomplete graphs and \(\operatorname{SEC}(G)\le |V(G)|-\gamma_s(G)+2\). Here \(\delta(F_m)=2\) and the secure-set lemma gives \(\gamma_s(F_m)=m\), so these bounds supply only \(4\le\operatorname{SEC}(F_m)\le m+3\). Their characterizations of certain extremal values and of trees do not give the constant-five formula or the quotient proof. Ordinary coalitions, introduced by Haynes and collaborators, use a different domination condition. No covering result was identified in the inspected public references or indexed research-record searches; that is not a proof of priority.

## Limitations
The result is restricted to ordinary secure coalitions on friendship graphs with at least two triangles. It does not enumerate all optimum partitions by a closed formula for general \(m\), nor determine secure coalition numbers of larger-clique windmills. The quotient test is exact but does not replace a classification of possible quotient isomorphism types. The correctness proof and checks were performed without independent mathematical audit. Priority remains subject to additional literature review.

## References
1. S. Shetty, S. Udupa N. V., and B. R. Rakshith, *Secure coalitions in graphs*, arXiv:2511.21170, first submitted 2025-11-26, https://arxiv.org/abs/2511.21170 . The public full text of version 1 was also inspected at https://www.researchgate.net/publication/398026021_Secure_coalitions_in_graphs .
2. T. W. Haynes, J. T. Hedetniemi, S. T. Hedetniemi, A. A. McRae, and R. Mohan, *Introduction to coalitions in graphs*, AKCE International Journal of Graphs and Combinatorics 17 (2020), 653–659, https://doi.org/10.1080/09728600.2020.1832874 .
