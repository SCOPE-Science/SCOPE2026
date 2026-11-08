# Matching-attachment rigidity of longest total dominating sequences in triangular graphs

## Finding

Let \(n\ge3\), and let \(T_n=L(K_n)\) be the triangular graph: its vertices are the two-element subsets of the labelled ground set \([n]\), with adjacency when two such subsets intersect. A *total dominating sequence* is an ordered sequence \((e_1,\ldots,e_\ell)\) of distinct vertices of \(T_n\) such that, for every \(j\), the open neighborhood of \(e_j\) contains a vertex absent from the union of the earlier open neighborhoods, and the union of all open neighborhoods is \(V(T_n)\).

**Theorem.** The longest possible length is
\[
\gamma_{\mathrm{gr}}^t(T_n)=\begin{cases}n-1,&n\text{ odd},\\ n-2,&n\text{ even}.\end{cases}
\]
For odd \(n=2m+1\), every longest sequence, and no other sequence, has the following *matching-attachment form*:

1. Its first \(m\) edges of \(K_n\) form a matching on all but one vertex \(r\), in an arbitrary order.
2. Its next edge joins \(r\) to an endpoint of one of those matched edges.
3. Its remaining \(m-1\) edges successively attach each still-isolated matched pair by one edge from the previously connected component to one endpoint of that pair; every pair is attached exactly once.

Consequently, the number of **ordered**, fully labelled longest sequences is exactly
\[
\boxed{\mathcal N_{2m+1}=\frac{(2m+1)!(2m)!}{2^m}.}
\]
There is also an unordered characterization: a set of \(2m\) vertices of \(T_{2m+1}\), regarded as the edges of \(K_{2m+1}\), supports a longest total dominating ordering **if and only if** those edges form a spanning tree that admits a matching of size \(m\). The tree statement concerns the *set* of selected graph edges, while the factorial formula counts *ordered* sequences and does not count distinct trees.

## Assumptions and scope

All graphs are finite, undirected, and simple. The ground-set labels, the order of the selected vertices, and the ordinary **open** neighborhoods matter. We count no quotient by graph automorphisms. The line graph has \(\binom n2\) vertices. A sequence is *legal* when each selected vertex contributes a previously undominated neighbor; it is *total* when all vertices are dominated at termination. We make no claim about the number of longest sequences for even \(n\), or about the number of distinct underlying spanning trees for arbitrary odd \(n\).

## Proof

**1. Exact description of still-undominated edges.** Regard each selected vertex of \(T_n\) as an edge of \(K_n\). After any prefix, let \(F\) be the graph on \([n]\) consisting of the selected edges, let \(U\) be its isolated *vertices*, and write \(u=|U|\). Let \(I\) be the selected edges that are isolated components \(K_2\) in \(F\), and put \(i=|I|\). An unselected edge of \(K_n\) touching a nonisolated vertex of \(F\) is adjacent in \(T_n\) to a selected edge. A selected edge is already dominated if and only if it touches another selected edge. Therefore the vertices of \(T_n\) not yet dominated are **exactly**
\[
\binom U2\ \sqcup\ I. \tag{1}
\]
In particular, the prefix is total precisely when \(u\le1\) and \(i=0\).

**2. Legal moves and the length identity.** A newly selected edge of \(K_n\) has either two, one, or zero endpoints in \(U\). The possibilities are:

* Type \(A\): two endpoints in \(U\). Such a step is legal precisely when \(u\ge3\); it decreases \(u\) by two and increases \(i\) by one.
* Type \(B_0\): one endpoint in \(U\), the other in a component of \(F\) having at least two edges. It is legal precisely when \(u\ge2\); it decreases \(u\) by one without changing \(i\).
* Type \(B_1\): one endpoint in \(U\), the other in an isolated selected edge. This is legal for \(u\ge1\); it decreases both \(u\) and \(i\) by one.
* Type \(C_1\): both endpoints already in \(F\), one in an isolated selected edge and the other in a component with at least two selected edges. It decreases \(i\) by one and is legal.
* Type \(C_2\): both endpoints already in \(F\), in **different** isolated selected edges. It decreases \(i\) by two and is legal.

No other step is legal. Indeed, a type with an endpoint in \(U\) obtains a fresh neighbor either among \(\binom U2\) or by touching an edge in \(I\); a type with neither endpoint in \(U\) must touch an edge in \(I\). Importantly, a component with at least two selected edges can first appear only via \(B_1\) or \(C_2\). Before this first event, only \(A\)-moves are possible.

Let lower-case \(a,b_0,b_1,c_1,c_2\) denote the five move counts in a completed sequence. Since \(i\) begins and ends at zero, and because the initial number of unused vertices is \(n\),
\[
a=b_1+c_1+2c_2,\qquad n=2a+b_0+b_1+u.\]
The total length \(L\) thus satisfies the exact identity
\[
L=a+b_0+b_1+c_1+c_2=n-u-b_1-c_2. \tag{2}
\]
The terminal unused-vertex count is \(u\in\{0,1\}\). If \(u=0\), some step must reduce the unused count from one to zero, and the only legal type doing so is \(B_1\). Hence \(u=0\) implies \(b_1\ge1\). If \(u=1\) and \(b_1=c_2=0\), no nontrivial connected component ever appears; only \(A\) occurs and the remaining \(i=a\ge1\) contradicts total domination. Therefore (2) yields \(L\le n-1\) for all \(n\ge3\).

**3. Equality and its parity obstruction.** Suppose \(L=n-1\). Equation (2) and the preceding paragraph force \(u=0,b_1=1,c_2=0\). The *sole* \(B_1\)-move must remove the final unused vertex, because no other move can remove that final vertex. No \(B_0\)-move can occur before that \(B_1\)-move (there is then no nontrivial selected-edge component), and none can occur after it (there are no unused vertices left). Thus \(b_0=0\), and \(n=2a+1\) is odd. Before the sole \(B_1\)-move there are only \(A\)-moves; afterwards there are only \(C_1\)-moves. Consequently \(a=m\), followed by a \(B_1\) step and \(m-1\) steps of type \(C_1\), exactly the matching-attachment form above. Each of those moves is legal by (1), so these sequences exist and have length \(2m=n-1\).

When \(n=2m\) is even, equality \(n-1\) is impossible. To attain \(n-2\), select \(m-1\) pairwise disjoint edges, leaving two unused vertices; attach one unused vertex to one of those isolated matched edges (\(B_1\)); then join every other still-isolated selected edge to the already connected component (\(C_1\)). One unused vertex remains, but (1) shows that all vertices of \(T_n\) are dominated. The length is \((m-1)+1+(m-2)=2m-2=n-2\). This handles \(n=4\), while the odd construction includes \(n=3\).

**4. Exact enumeration for odd order.** For \(n=2m+1\), the ordered initial matching is chosen by selecting the unmatched vertex, pairing the other \(2m\) vertices, and ordering the pairs. Its number is
\[
n\,\frac{(2m)!}{2^m m!}\,m!=\frac{n!}{2^m}.\]
At the \(j\)-th attachment, where \(1\le j\le m\), choose one of the \(m-j+1\) not-yet-attached matched pairs, one of its two endpoints, and one of the \(2j-1\) vertices already in the connected component (which initially consists of the single unmatched vertex). These independent choices give
\[
\prod_{j=1}^{m}2(m-j+1)(2j-1)
=2^m m!(2m-1)!!=(2m)! .
\]
Every choice produces a different ordered edge sequence, and the equality classification in Step 3 proves that none is omitted. Multiplication gives \(n!(2m)!/2^m\), the stated formula.

**5. Unordered spanning-tree equivalence.** The \(m\) initial matching edges together with \(m\) successive attachments form a connected graph on \(2m+1\) vertices with exactly \(2m\) edges; it is a spanning tree. Its original matching has size \(m\). Conversely, let \(H\) be a spanning tree on \(2m+1\) vertices containing a matching \(M\) of size \(m\), leaving one vertex \(r\) unmatched. Contract the edges of \(M\). The resulting graph is a tree on \(m+1\) vertices. Root it at \(r\), first select the edges of \(M\) in any order, and then select the other \(m\) edges in a parent-before-child order of this contracted tree. In the uncontracted tree, each later step attaches precisely one isolated matched pair to the previously connected component. By Step 3 this is a longest legal total dominating sequence with selected-edge set \(E(H)\). This proves the set characterization.

## Verification

`verify_open_neighborhood_dp.py` constructs \(T_n\) explicitly from all two-element subsets, computes open-neighborhood bit masks without using the matching argument, and uses memoized dynamic programming to calculate maximum legal-sequence length and the number of attaining ordered sequences. It checked every \(3\le n\le11\). Its observed odd-order counts were \(6,720,453600,914457600,4526565120000\) for \(n=3,5,7,9,11\), agreeing with the formula. Its lengths were \(2,2,4,4,6,6,8,8,10\) over \(n=3,\ldots,11\). The recurrence counts only paths ending with all open neighborhoods covered, so it does not confuse a merely maximal partial sequence with a total one.

`verify_matching_attachment.py` separately generates ordered matchings and all legal attachments without invoking the neighborhood dynamic program; for \(n=3,5,7\), it explicitly checks that each generated sequence is distinct, legal, total, and of the predicted length. The counts were respectively \(6,720,453600\). Actual outputs are included in the two text artifacts. These finite checks corroborate the proof; the theorem for all \(n\) follows from Steps 1–5, not from interpolation.

To reproduce: run `python3 verify_open_neighborhood_dp.py` and `python3 verify_matching_attachment.py` with standard Python 3 (no third-party dependencies). Both scripts finish with a `PASS` line if every assertion succeeds.

## Relationship to prior work

The foundational 2016 paper by Brešar, Henning and Rall introduces Grundy total domination and its open-neighborhood formulation, establishes general bounds, and relates it to hypergraph edge-covering sequences. The 2016 paper by Brešar, Kos, Nasini and Torres gives algorithms for trees, split graphs, and modular decompositions; its tree input is the *original graph* whose neighborhoods are used, not the complete-graph spanning tree extracted here from a triangular-graph sequence. Neither inspected paper states the matching-attachment classification or the factorial enumeration of longest sequences for \(T_n\). The Kneser graph \(KG(n,2)\) is the **complement** of \(T_n\), and total-neighborhood sequence results for it do not automatically transfer to \(T_n\): adjacency is disjointness there and intersection here. General results for *closed*-neighborhood Grundy domination also concern a different parameter. OEIS A290716 gives the number of *minimal ordinary dominating sets* of triangular graphs, not the count of longest *ordered total* dominating sequences considered here.

## Limitations

This is an exact theorem for the open-neighborhood version. It does not enumerate longest sequences for even \(n\), nor does the odd-order ordered-sequence formula count distinct spanning trees. No assertion of priority can exclude every unindexed or inaccessible work. Independent scholarly assessment has not been performed.

## References

1. B. Brešar, M. A. Henning, and D. F. Rall, *Total Dominating Sequences in Graphs*, arXiv:1601.07525v1, publicly posted January 27, 2016; subsequently Discrete Mathematics 339 (2016), 1665–1676. https://arxiv.org/abs/1601.07525
2. B. Brešar, T. Kos, G. Nasini, and P. Torres, *Total dominating sequences in trees, split graphs, and under modular decomposition*, arXiv:1608.06804v1, August 24, 2016. https://arxiv.org/abs/1608.06804
3. B. Brešar, T. Kos, and P. D. Torres, *Grundy domination and zero forcing in Kneser graphs*, Ars Mathematica Contemporanea 17 (2019), 419–430, DOI:10.26493/1855-3974.1881.384. Contrasting complement-graph setting.

4. OEIS Foundation, *A290716: Number of minimal dominating sets in the n-triangular (Johnson) graph*, https://oeis.org/A290716, public entry dated 2017. Distinct ordinary minimal-set enumeration.
