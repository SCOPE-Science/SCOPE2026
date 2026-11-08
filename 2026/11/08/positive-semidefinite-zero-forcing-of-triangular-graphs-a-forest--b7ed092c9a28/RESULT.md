# Positive-semidefinite zero forcing of triangular graphs: a forest criterion and complete enumerator

## Finding
For every integer \(n\ge3\), put \(T_n=L(K_n)=J(n,2)\), with a vertex of \(T_n\) for each edge of \(K_n\), and adjacency when two edges share an endpoint. For each initially blue set \(B\subseteq V(T_n)\), define its **white-edge graph** \(F_B=([n],E(K_n)\setminus B)\), retaining all isolated ground vertices. Under the positive-semidefinite (PSD) color-change rule, **\(B\) is successful if and only if \(F_B\) is a forest with at least two connected components**.

Let \(N=\binom n2\). For \(0\le k\le n-2\), let \(f_{n,k}\) be the number of labeled forests on \([n]\) with precisely \(k\) edges, including isolated vertices. The complete PSD zero-forcing polynomial is
\[
\mathcal Z_+(T_n;x)=\sum_{k=0}^{n-2}f_{n,k}x^{N-k},\qquad
 f_{n,k}=n![z^nt^k]\exp\!\left(\sum_{s\ge1}\frac{s^{s-2}}{s!}z^st^{s-1}\right),
\]
where the contribution of \(s=1\) in the sum is defined to be \(z\). Equivalently,
\[
f_{n,k}=\sum_{\substack{\pi\text{ partition of }[n]\\|\pi|=n-k}}
\prod_{A\in\pi}\tau(|A|),\qquad
\tau(1)=1,\quad \tau(s)=s^{s-2}\ (s\ge2).
\]
The minimum cardinality is \(Z_+(T_n)=N-n+2\), a value already known in earlier literature, but the number of distinct minimum PSD sets and their precise form are
\[
\boxed{f_{n,n-2}=\frac12\sum_{a=1}^{n-1}\binom na\tau(a)\tau(n-a)};
\]
these minima are exactly the complements of all spanning forests of \(K_n\) having two components. For \(n=3,4,5,6,7,8\), their numbers are respectively \(3,15,110,1080,13377,200704\).

## Assumptions and scope
All graphs are finite, simple, undirected, and labeled as indicated. The PSD rule is: if the current white induced subgraph has components \(C_1,\dots,C_r\), a blue vertex \(b\) can color white \(w\in C_i\) blue whenever \(w\) is its unique white neighbor in \(T_n[B\cup C_i]\). The graph \(F_B\) has all \(n\) ground vertices even when some have degree zero. Here \(k\) counts initially white vertices of \(T_n\), equivalently edges of \(F_B\), not blue vertices. A graph with no white vertices is successful without a force. Nothing is asserted about forcing schedules, arbitrary line graphs, or PSD propagation-time optimization.

## Proof
**1. Cycles cannot be broken.** Suppose the white-edge graph contains a cycle \(e_1,e_2,\dots,e_r\) in \(K_n\). The corresponding vertices in \(T_n\) form a connected subgraph of the current white graph. Any blue graph vertex \(uv\) adjacent to one of them has \(u\) or \(v\) on this cycle, so \(uv\) is adjacent to both cycle edges incident at that endpoint (these are different from the blue edge). Both cycle edges belong to the same white component. Thus no blue vertex has exactly one white neighbor within that component among cycle vertices. Other white vertices may be forced, but the complete cycle remains permanently white. Therefore every successful initial set has acyclic \(F_B\).

**2. One-component forests cannot start.** If \(F_B\) is a tree spanning \([n]\), every ground vertex is incident to a white edge. Every blue vertex \(uv\notin E(F_B)\) is adjacent to at least one white edge incident to \(u\), and another incident to \(v\). These two white edges are distinct and lie in the unique white component \(L(F_B)\). Hence no PSD force is available, so a spanning tree is not successful. For \(n\ge3\), a connected forest is precisely a spanning tree. Together with step 1, every successful initial set has at least two white-edge components.

**3. Every disconnected forest is successful.** Let \(F_B\) be a forest with at least two components and at least one edge. Choose a leaf \(u\) of any nontrivial tree component \(C\), let \(e=uv\) be its sole incident white edge, and take any ground vertex \(w\) outside \(C\). Because \(u,w\) lie in distinct white-edge components, the edge \(uw\) is blue. In the white component \(L(C)\) of \(T_n\), the blue vertex \(uw\) has exactly one white neighbor, namely \(uv\): no other white edge is incident to the leaf \(u\), and no edge of \(C\) is incident to \(w\). The PSD rule therefore forces \(e\). Deleting it leaves a forest with at least two components. Repeating deletes every white edge. If no white edges remain, success is immediate. This proves the if-and-only-if criterion including edgeless boundary cases.

**4. Exact enumeration.** A forest with \(k\) edges on \(n\) labeled vertices has exactly \(n-k\) connected components. A component supported on a specified block of \(s\) labels can be chosen in \(\tau(s)\) ways by Cayley's tree formula, with the singleton convention above. Summing independently over set partitions gives the stated formula for \(f_{n,k}\). The labeled exponential formula gives its coefficient-extraction representation. PSD success is equivalent to \(k\le n-2\) together with being a forest, so complementing edges gives the polynomial and its minimum degree. If \(k=n-2\), there are exactly two components. Choosing one block of size \(a\), choosing a tree on it and a tree on its complement, and dividing by two for interchangeable components proves the final sum. Every quantity is an integer; the sum counts each unordered pair of components twice.

**5. Distinction from ordinary forcing.** For ordinary zero forcing, a blue vertex \(uv\) sees \(\deg_{F_B}(u)+\deg_{F_B}(v)\) distinct white neighbors. Hence ordinary forces in a forest require at least one isolated ground label, and the same leaf-removal argument suffices when such an isolate exists. Cycles obstruct ordinary forcing as above. Thus an ordinary zero-forcing set has a white-edge forest with an isolated ground vertex, whereas PSD sets also include disconnected forests with *no* isolated ground vertex. In particular, when \(n=4\), the complement of two disjoint edges is PSD successful but ordinary unsuccessful. At minimum size, the known ordinary count is \(n(n-1)^{n-3}\); the exact additional PSD minimum-set count is \(f_{n,n-2}-n(n-1)^{n-3}\), giving respectively \(3,30,330\) additional sets at \(n=4,5,6\). These ordinary-rule statements serve only as a mathematical comparison, not as an additional novelty claim.

## Verification
`check_psd.py` constructs the triangular graph directly and simulates legal PSD moves with the actual white components, without using the forest criterion to decide success. It compares against an independently coded union-find acyclicity-and-connectivity predicate on all \(33864\) initial colorings of \(T_n\) for \(n=3,4,5,6\); all agree. `check_forest_counts.py` independently computes the labeled-forest coefficients using weighted set-partition enumeration for \(3\le n\le8\), checks these counts against exhaustive edge-subset acyclicity tests for \(3\le n\le6\), and verifies the two-component formula. The exact outputs accompany both programs. For unbounded \(n\), the proof is steps 1–4 above; finite computation alone is not used to infer the theorem.

## Relationship to prior work
Barioli and collaborators introduced the PSD color-change rule and related it to ordered subgraphs (arXiv:1003.2028v1, Section 3). Peters, *Positive semidefinite maximum nullity and zero forcing number* (2012, Proposition 3.16), already proved the **scalar** \(Z_+(L(K_n))=\binom n2-n+2\). Fallat, Meagher, Soltani, and Yang (arXiv:1508.07357v1, Section 8, Lemma 8.3) independently record that scalar for \(J(n,2)\) in their clique-cover treatment. Neither inspected result classifies **all** initial PSD forcing sets or supplies their exact cardinality enumerator. The ordinary zero forcing polynomial studied by Boyer and collaborators (arXiv:1801.08910v1) uses a strictly stronger color-change restriction; it does not imply the PSD classification. The known ordinary triangular-graph forcing-set forest criterion is similarly distinct because it requires an isolated ground vertex. The contributions here are solely the complete PSD predicate, exact polynomial, classification/count of all minimum PSD sets, and their quantified difference from ordinary forcing.

## Limitations
This is a self-reviewed, nonindependently audited mathematical argument. The literature comparisons establish no absolute priority guarantee; differently indexed discussions, theses, and unpublished enumerations could contain equivalent conclusions. The full text of the relevant 2013 thesis was not inspected for this comparison. Finite tests cover \(n\le8\) only and do not certify the infinite-domain proof. No computational complexity or propagation-time claims are made.

## References
1. F. Barioli et al., *Zero forcing parameters and minimum rank problems*, arXiv:1003.2028v1 (public 2010-03-10), https://arxiv.org/abs/1003.2028.
2. T. Peters, *Positive semidefinite maximum nullity and zero forcing number*, Electronic Journal of Linear Algebra 23 (2012), 815–830, Proposition 3.16, DOI:10.13001/1081-3810.1559, https://journals.uwyo.edu/index.php/ela/article/download/1119/1119/1119.
3. S. Fallat, K. Meagher, B. Yang, *On the Complexity of the Positive Semidefinite Zero Forcing Number*, arXiv:1407.7017v1 (2014-07-25), https://arxiv.org/abs/1407.7017.
4. S. Fallat, K. Meagher, A. Soltani, B. Yang, *Compressed Cliques Graphs, Clique Coverings and Positive Zero Forcing*, arXiv:1508.07357v1 (2015-08-28), Section 8, Lemma 8.3, https://arxiv.org/abs/1508.07357.
5. K. Boyer et al., *The zero forcing polynomial of a graph*, arXiv:1801.08910v1 (2018-01-26), https://arxiv.org/abs/1801.08910 (ordinary rule; comparison only).
