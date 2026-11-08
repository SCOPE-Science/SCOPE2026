# Exact shattered arc supports for complete rooted arborescences

## Finding

Let \(n\ge2\), take vertices \(V=\{0,1,\ldots,n-1\}\), and distinguish root \(0\). In the complete bidirected digraph, exclude arcs entering the root and loops; the query ground set is
\[
X_n=\{(u,v):u,v\in V,\ u\ne v,\ v\ne0\}.
\]
For each spanning **out-arborescence** \(T\) rooted at \(0\), its Boolean concept is the indicator of its arc set. A support \(S\subseteq X_n\) is shattered when every subset \(P\subseteq S\) occurs as \(E(T)\cap S\) for some such \(T\).

**Theorem.** A support \(S\) is shattered if and only if (i) each vertex has at most one arc of \(S\) entering it, (ii) \(S\) contains no directed cycle, and (iii) \(|S|\le n-2\). Thus the shattered sets are exactly the directed branchings of size at most \(n-2\). The complete face polynomial is
\[
\Phi_n(z)=\sum_{S\text{ shattered}}z^{|S|}
 =1+\sum_{s=1}^{n-2}\binom{n-1}{s}(n-s)n^{s-1}z^s.
\]
Consequently \(\operatorname{VCdim}(\mathcal T_n)=n-2\). The complex is pure; for \(n\ge3\), the number of facets is \(2(n-1)n^{n-3}\). For \(n=2\) its sole face is the empty support.

## Assumptions and scope

The digraph has both orientations of every edge between distinct vertices, and the root is fixed. Out-arborescences have indegree zero at the root, indegree one elsewhere, are acyclic, and contain every vertex. Queries ask membership of individual **directed arcs**, not membership of undirected edges. All statements quantify over **every** \(n\ge2\), **every** support \(S\), and **every** binary labeling on \(S\). The polynomial counts labeled arc supports, not isomorphism classes or the number of arborescences.

A *directed branching* is a directed arc set of indegree at most one at each vertex and with no directed cycle. Because no arcs in \(X_n\) enter root \(0\), its directed components are out-trees, with one distinguished top vertex per component. Every such top vertex is the unique vertex of its component with indegree zero.

## Proof

**Necessity: the all-positive trace.** If \(S\) is shattered, its all-one trace is realized by an out-arborescence. Hence \(S\) is contained in that arborescence and must be a directed branching, in particular \(|S|\le n-1\).

**Necessity: the forbidden top rank.** Suppose \(S\) is a branching with exactly \(n-1\) arcs. All nonroot vertices have indegree one and root has indegree zero, so \(S\) itself is a spanning out-arborescence. Partition its arcs into \(P\), the arcs whose tail is nonroot, and \(Q\), the arcs leaving the root. Request exactly the arcs \(P\) positive and the arcs \(Q\) negative. Any arborescence containing \(P\) cannot enter a vertex in the head set of \(P\) with an additional root arc, because that would give indegree two. Every remaining nonroot vertex is the head of its unique arc in \(Q\), which is forbidden by the trace. Thus no root outgoing arc can be chosen, whereas every spanning out-arborescence on \(n\ge2\) requires one. Contradiction. Therefore every shattered support has \(|S|\le n-2\).

**Sufficiency: a two-level component-attachment construction.** Fix any directed branching \(S\) with \(s=|S|\le n-2\), and any target positive trace \(P\subseteq S\). Set \(Q=S\setminus P\). The directed forest \(P\) has \(t=n-|P|\ge2\) rooted components, of which one contains vertex \(0\). Each other component has a top vertex \(v_i\ne0\). Call such a component *blocked* if the arc \((0,v_i)\) lies in \(Q\), and *open* otherwise. Since \(|Q|=|S|-|P|\le (n-2)-|P|=t-2\), at most \(t-2\) of the \(t-1\) nonroot components are blocked; consequently at least one is open.

For each open nonroot component \(C_i\), add the arc \((0,v_i)\), which is outside \(Q\). Fix one open component \(C_*\). For each blocked component \(C_j\), add an arc from any vertex of \(C_*\) to \(v_j\). This arc is also outside \(Q\): the unique arc of \(S\) entering \(v_j\), if one exists, is the blocked arc \((0,v_j)\), since \(v_j\) has no incoming arc in \(P\) and \(S\) has indegree at most one. The chosen tail is nonroot, so the new arc differs from \((0,v_j)\). In each case the added arc enters a different top vertex of \(P\). All components become connected to the root, with no directed cycles and indegree one at every nonroot vertex. Their union with \(P\) is a rooted spanning out-arborescence \(T\), satisfying \(E(T)\cap S=P\). Since \(P\subseteq S\) was arbitrary, \(S\) is shattered.

**Exact enumeration.** For \(0\le s\le n-2\), a directed branching of size \(s\) has exactly \(k=n-s\) out-tree components, one rooted at \(0\). Choose its other \(k-1\) component roots among the \(n-1\) nonroot vertices in \(\binom{n-1}{k-1}=\binom{n-1}{s}\) ways. For any fixed set of \(k\) component roots, the number of labeled rooted forests directed outward is \(k n^{n-k-1}\). To verify this classical rooted-forest formula, apply the all-minors matrix-tree theorem to the complete graph: the principal minor deleting these \(k\) roots is \(nI_{n-k}-J_{n-k}\), with determinant \(k n^{n-k-1}\) for \(k<n\); for \(k=n\) the empty determinant is \(1\). Multiplying yields \(\binom{n-1}{s}(n-s)n^{s-1}\) for \(s\ge1\) and one empty face for \(s=0\).

**Dimension, purity and facets.** The degree of \(\Phi_n\) is \(n-2\) with positive leading coefficient, proving the dimension. Every branching \(S\) with \(|S|<n-2\) has at least three components; a nonroot component top \(v\) can be joined to the root by the as-yet absent arc \((0,v)\), giving a larger branching. Therefore all facets have cardinality exactly \(n-2\). Setting \(s=n-2\) gives \(\binom{n-1}{n-2}2n^{n-3}=2(n-1)n^{n-3}\) for \(n\ge3\).

## Verification

An independent exhaustive finite checker is supplied as `arbo_checks.py`. It enumerates all labeled undirected spanning trees using Prüfer codes, orients each away from the root, computes all observed binary traces on each query support, and compares the result with a separate branching test. It checks every support for \(2\le n\le5\) (65,536 supports at \(n=5\)), verifies the face counts, and additionally tests 800 reproducibly sampled supports at \(n=6\). The expected marker is `ROOTED_ARBORESCENCE_SHATTER_PASS 66866`. The unrestricted theorem rests on the preceding constructive proof, not on these finite checks.

## Relationship to prior work

Kakimura, Kamiyama and Takazawa (2018) treat directed branchings as common independent sets of graphic/sparsity and incoming-degree matroids and prove optimization and packing theorems. Király, Szigeti and Tanigawa (2019) give general arborescence-packing/matroid-intersection criteria. These are the appropriate structural foundations, but their analyzed statements concern existence, packing and optimization, not the realization of *all* positive/negative traces on one arbitrary directed-arc support, nor this face polynomial. In contrast to a general matroid base family, rooted arborescences form a common-base family of two matroids; a single-matroid base shattering theorem cannot simply be substituted. Coudert, Csikós, Ducoffe and Viennot (2024) examine exact graph VC-dimension computation for neighborhood systems; their query universe and concept family differ. The complete bidirected specialization is essential in the sufficiency proof. No claim is made about novelty of the underlying directed-branching or matrix-tree results.

## Limitations

No characterization is asserted for incomplete digraphs, for multiple roots, for unrooted directed trees, or for online (Littlestone) dimension. This is a self-reviewed result with no independent audit. Publication-priority searches under alternate language cannot establish absolute uniqueness; the risk of an unlocated classical corollary remains. The finite checker cannot replace the all-order proof.

## References

1. N. Kakimura, N. Kamiyama, K. Takazawa, *The \(b\)-branching problem in digraphs*, arXiv:1802.02381, first posted 2018-02-07, https://arxiv.org/abs/1802.02381.
2. C. Király, Z. Szigeti, S.-i. Tanigawa, *Packing of arborescences with matroid constraints via matroid intersection*, Mathematical Programming 181 (2020), 85–117, online 2019-04-02, https://doi.org/10.1007/s10107-019-01377-0. A 2018 technical report preceded the journal publication.
3. D. Coudert, M. Csikós, G. Ducoffe, L. Viennot, *Practical Computation of Graph VC-Dimension*, arXiv:2405.07588, first posted 2024-05-13, https://arxiv.org/abs/2405.07588.
4. Classical all-minors matrix-tree theorem (used only to evaluate rooted-forest counts).
