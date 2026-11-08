# Universal outer-EF1 spectra and exact counting on complete bipartite resource graphs

## Finding

**Theorem (universal binary spectrum and enumeration).** Let \(G=K_{a,b}\) with \(1\le a\le b\), and let \(n=a+b\). Its vertices are distinct indivisible goods, and each of \(k\) labeled agents (\(1\le k\le n\)) has the **same** additive valuation taking only values zero and one on individual vertices. A complete allocation partitions the vertices into \(k\) nonempty sets, each inducing a connected subgraph. Say it is **outer-EF1** if for every pair of agents \(i,j\) with \(u(B_i)<u(B_j)\), there is a vertex \(g\in B_j\) such that deleting \(g\) leaves a connected bundle (the empty set is allowed) and \(u(B_j\setminus\{g\})\le u(B_i)\).

Every common binary valuation admits such an allocation **if and only if**
\[
 \boxed{k\le a\quad\text{or}\quad k\ge b.}
\]
In both feasible ranges the allocation can be constructed in polynomial time. Thus, when \(b\ge a+2\), the exact universal nonexistence gap is \(a<k<b\), of unbounded length.

Furthermore, the number of labeled complete, connected, outer-EF1 allocations for any prescribed common binary valuation is an explicit multivariate coefficient computable in polynomial time. Write \(a_+,a_0,b_+,b_0\) for the numbers of one-valued and zero-valued vertices in the two parts, and let \(P=a_++b_+\). For \(\mathbf h=(i,j,\ell,m)\), set \(s_A=i+j\), \(s_B=\ell+m\), and \(|\mathbf h|_+=i+\ell\). Define a feasible local composition as one for which either \(s_A+s_B=1\) or both \(s_A,s_B\ge1\). Let \(C(\mathbf h)\) denote this condition, and let \(R(\mathbf h)\) denote the existence of a one-valued vertex removable without disconnecting the remaining induced bundle. Precisely,
\[
R(\mathbf h)\iff
 [s_A+s_B=1\ \land\ i+\ell=1]
 \ \lor\ [i\ge1\ \land\ (s_A\ge2\ \lor\ s_B=1)]
 \ \lor\ [\ell\ge1\ \land\ (s_B\ge2\ \lor\ s_A=1)].
\]
With \(\mathbf x^{\mathbf h}=x_+^i x_0^j y_+^\ell y_0^m\), define
\[
P_t(\mathbf x)=\sum_{\substack{\mathbf 0\le\mathbf h\le(a_+,a_0,b_+,b_0)\\ C(\mathbf h),\ |\mathbf h|_+=t}}\frac{\mathbf x^{\mathbf h}}{i!j!\ell!m!},\qquad
Q_t(\mathbf x)=\sum_{\substack{\mathbf 0\le\mathbf h\le(a_+,a_0,b_+,b_0)\\ C(\mathbf h),\ R(\mathbf h),\ |\mathbf h|_+=t}}\frac{\mathbf x^{\mathbf h}}{i!j!\ell!m!}.
\]
Put \(Q_{P+1}=0\). Then the **exact** allocation count is
\[
\boxed{\mathcal N(\mathbf c,k)
=a_+!a_0!b_+!b_0!\,[x_+^{a_+}x_0^{a_0}y_+^{b_+}y_0^{b_0}]
\sum_{t=0}^{P}\bigl((P_t+Q_{t+1})^k-Q_{t+1}^k\bigr).}
\]
The coefficient is understood in the polynomial ring truncated to the four prescribed counts.

For the all-one valuation, put \(n=kq+r\), \(0\le r<k\), and define \(H_1(x)=1+x\), \(H_s(x)=(1+x)^s-1-x^s\) for \(s\ge2\). The count simplifies to
\[
\boxed{\mathcal N_1(a,b,k)=\binom{k}{r}\frac{a!b!}{(q!)^{k-r}((q+1)!)^r}
[x^a]\,H_q(x)^{k-r}H_{q+1}(x)^r.}
\]
For example, at \((a,b)=(2,4)\), the six counts indexed by \(k=1,\ldots,6\) are \((1,12,0,288,960,720)\).

## Assumptions and scope

The graph is a simple complete bipartite graph with two nonempty parts. Goods are vertices rather than edges. All \(n\) goods must be allocated, all \(k\) agents must receive a **nonempty connected** bundle, and agent utilities are the same binary additive function. The fairness notion deletes only from the envied bundle and requires the remaining bundle to be connected; the empty set is permitted after deletion. Labeled vertices and labeled agents are distinguished in the enumerator. The theorem is **not** an arbitrary-valuation EF1 guarantee, a weighted-valuation theorem, or a result for arbitrary connected graphs.

## Proof

**Lemma 1 (removable positive vertices).** A connected nonempty vertex set in \(K_{a,b}\) is either a singleton or meets both parts. Let its part sizes be \(s_A,s_B\). For a positive vertex on side \(A\), deletion preserves connectivity exactly when \(s_A\ge2\) or \(s_B=1\); the corresponding condition on side \(B\) is \(s_B\ge2\) or \(s_A=1\). For a singleton, deletion yields the permitted empty set. These observations prove the predicate \(R\). In particular, any connected bundle containing at least two one-valued vertices has some removable one-valued vertex: if at least two are on the same side delete one of those, while if both sides contain a positive vertex and each side has one vertex either is removable. When a side is a singleton and the other side has several vertices, the positive vertex in the larger side can be removed instead. More systematically, if no positive vertex on \(A\) is removable, then \(s_A=1,s_B\ge2\); all positives in \(B\) are removable, so a bundle with at least two positives cannot fail. The symmetric case is identical.

**Lemma 2 (fairness by one-unit spread).** For any connected allocation, outer-EF1 holds if and only if either all agent utilities are equal, or their values lie in \(\{t,t+1\}\) for some integer \(t\), both values occur, and every bundle with utility \(t+1\) has a removable one-valued vertex. Necessity follows because removal reduces a binary additive utility by at most one; sufficiency follows by deleting the indicated positive vertex in any envied bundle.

**Necessary bound.** Apply the all-one valuation. Every connected bundle of size at least two has a removable vertex (delete a leaf of a spanning tree of its induced graph). By Lemma 2, an outer-EF1 allocation must have bundle sizes differing by at most one. Let \(n=kq+r\) with \(0\le r<k\). If \(q\ge2\), each of the \(k\) bundles must meet both parts and so \(k\le a\). If \(q=1\), there are exactly \(r=n-k\) size-two bundles, each requiring one vertex from each part, whence \(n-k\le a\), equivalently \(k\ge b\). These are the only cases because \(k\le n\).

**Construction when \(k\le a\).** Then both part sizes are at least \(k\). Let \(p_A=a_+\), \(p_B=b_+\), and \(P=p_A+p_B\). If \(P<k\), start with \(k\) disjoint edges, one per agent, and place each of the \(P\) positive vertices into a distinct edge. To partner the \(p_A\) positives in \(A\) use \(p_A\) zero vertices of \(B\), and analogously use \(p_B\) zero vertices of \(A\). Because \(a,b\ge k>P\), sufficiently many zeros exist. Fill out the remaining edges with zeros, then place all leftover zero vertices in one of the \(k-P\) zero-only bundles. Each bundle is connected, has utility zero or one, and each positive bundle has a removable positive endpoint.

If \(P\ge k\), distribute the \(p_A\) positive vertices as evenly as possible across the \(k\) bundles, giving the first \(p_A\bmod k\) bundles an extra positive in \(A\). Distribute the \(p_B\) positive vertices similarly, but give the extra positives to the *last* \(p_B\bmod k\) bundles. The resulting total utility of each bundle is \(\lfloor P/k\rfloor\) or \(\lceil P/k\rceil\) (if the two remainders overlap, all bins receive at least one extra, and the overlap bins receive two). Use as many zero vertices as needed to give every bundle at least one vertex of each part. This is possible because there are at least \(k\) total vertices in each part, and every positive vertex already placed there reduces the number of necessary zero vertices by one. Dump all remaining zero vertices into any bundles. All bundles remain connected. If \(P=k\), all utilities are one; otherwise any higher-valued bundle has utility at least two, hence has a removable positive vertex by Lemma 1. Lemma 2 proves outer-EF1.

**Construction when \(k\ge b\).** Let \(r=n-k\le a\). We construct \(r\) disjoint size-two edges and leave all remaining vertices as singleton bundles, producing exactly \(k\) bundles. If \(P\le k\), the number of zero-valued vertices is \(z=n-P\ge r\). Form the bipartite graph with every edge of \(K_{a,b}\) **except** edges between two positive vertices. Its maximum matching size is \(\min(a,b,z)\). To see this, its vertex-cover number is the minimum of \(a,b,z\): the three displayed full sets are covers, and any cover of smaller size than \(\min(a,b)\) must leave some vertex uncovered on each side, forcing all remaining uncovered vertices to be positive and hence forcing the cover to contain every zero vertex. Equivalently, apply the two complete rectangles \(A_0\times B\) and \(A_+\times B_0\) with König's theorem. Thus there is a matching of \(r\) edges, each containing at most one positive vertex. All resulting bundle utilities are zero or one. Every positive edge has a removable positive endpoint, so the allocation is outer-EF1.

If \(P>k\), write \(z_A=a-p_A\), \(z_B=b-p_B\). Since \(k\ge b\ge a\), we have \(p_A>z_B\) and \(p_B>z_A\). First match every zero vertex in \(A\) to a distinct positive vertex in \(B\), and every zero vertex in \(B\) to a distinct positive in \(A\). Let \(t=P-k>0\). The remaining positive vertices in each side number at least \(t\), since \(p_A-z_B=P-b\ge P-k=t\) and \(p_B-z_A=P-a\ge P-k=t\). Form \(t\) more disjoint edges between remaining positive vertices. Altogether the number of edges formed is \(z_A+z_B+t=n-k=r\), and every unpaired vertex is positive. The resulting \(k\) bundles have utility one or two; every utility-two edge admits deletion of a positive endpoint. Thus outer-EF1 holds. All constructions use simple counts and matchings and are polynomial-time.

**Exact enumerator.** In a complete bipartite graph, connectivity and the availability of a removable positive vertex depend only on the four within-bundle category counts. Lemma 2 says precisely that either all \(k\) utilities coincide, or they take the values \(t,t+1\) with at least one low-utility bundle, all high-utility bundles satisfying \(R\). The exponential generating polynomial \((P_t+Q_{t+1})^k\) counts the latter together with the (inappropriate, multiply-counted) all-high cases; subtracting \(Q_{t+1}^k\) ensures that at least one low-utility block is present. When all utilities are \(t\), that allocation appears only at index \(t\), in \(P_t^k\), not at \(t-1\) after subtraction. Multiplication by \(a_+!a_0!b_+!b_0!\) and extraction of the four full-degree coefficients assigns the distinct labeled vertices exactly once. This gives the stated formula. A dynamic program truncating all four degrees and multiplying \(k\) layers (or directly adding labeled blocks by binomial choices) uses a polynomial number of states and operations in \(n\) and \(k\), with counts of polynomial bit length since they are bounded by \(k^n\).

In the all-one case, Lemma 2 forces bundle sizes \(q\) or \(q+1\). A connected bundle of size \(s=1\) can lie in either part, counted by \(H_1\); for \(s\ge2\), both parts must occur, counted by \(H_s\). Select the \(r\) larger labeled-agent bundles in \(\binom{k}{r}\) ways, then choose the labeled vertices using the multinomial factors. Coefficient extraction yields the last formula.

## Verification

The standalone file `checker.py` requires only Python 3 and its standard library. Run `python3 checker.py`. It compares the exact four-type dynamic-program count with independent explicit enumeration of all allocations on small labeled graphs and all binary profiles; checks the all-one coefficient formula and its exact threshold; and verifies the constructive universal-existence cases over a larger bounded parameter grid. The expected summary is 304 exhaustive comparisons, 252 all-one comparisons, and 1,611 binary existence checks. These finite checks support reproducibility but **do not prove** the infinite-parameter statements; those follow from the preceding lemmas and constructions.

## Relationship to prior work

Bousquet, Connor, Totschnig, and Zeitoun (2026) develop graph fair-division guarantees beyond traceability, including a distinct study of existence spectra and common binary valuations on other graph families. Bei, Igarashi, Lu, and Suksompong (2019/2022) establish ordinary connected EF1 existence on complete bipartite graphs in several regimes, including both part sizes at least the number of agents. Igarashi and Zwicker (2023) formulate the stronger outer-EF1 deletion requirement. Equitable-connected-partition results cover the all-one special case but not the binary-valued full allocation count. The present theorem concerns the **exact universal common-binary outer-EF1 spectrum** and the **exact count for each binary profile**, including the high-agent regime \(k\ge b\) and the excluded interval.

## Limitations

The theorem is restricted to complete bipartite resource graphs and identical binary valuations, and allows deletion to the empty bundle when considering an envied singleton. It does not imply outer-EF1 for arbitrary monotone, nonidentical, or weighted valuations. Its exact counting algorithm is polynomial in the number of vertices, but does not establish a comparable formula for arbitrary graphs. Search comparisons do not establish absolute publication novelty; a 2026 relevant primary manuscript's accessible introduction and stated contributions were inspected, but full-text access to its remaining material was incomplete. An independent scientific audit has not been performed.

## References

1. Bousquet, Connor, Totschnig, and Zeitoun, *Fair Division of Graphs: Beyond Traceability* (2026), arXiv:2608.29902v1, https://arxiv.org/abs/2608.29902.
2. Bei, Igarashi, Lu, and Suksompong, *The Price of Connectivity in Fair Division*, arXiv:1908.05433, https://arxiv.org/html/1908.05433v3.
3. Igarashi and Zwicker, *Fair Division of Graphs and of Tangled Cakes*, Mathematical Programming (2023), https://doi.org/10.1007/s10107-023-01945-5.
4. Blažej and collaborators, *Equitable Connected Partition and Structural Parameters Revisited* (2024), arXiv:2404.18968, https://arxiv.org/abs/2404.18968.
