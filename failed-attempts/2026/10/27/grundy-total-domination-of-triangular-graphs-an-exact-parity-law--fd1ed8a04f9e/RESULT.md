# Grundy total domination of triangular graphs: an exact parity law and extremal-sequence criterion

## Finding
For every integer \(n\geq 3\), let \(T_n=J(n,2)=L(K_n)\) be the graph whose vertices are unordered pairs from an \(n\)-element set, with two different pairs adjacent when they intersect. Then its Grundy total domination number is
\[
\gamma_{\mathrm{gr}}^{\mathrm t}(T_n)
=2\left\lfloor\frac{n-1}{2}\right\rfloor
=\begin{cases}n-1,&n\text{ odd},\\n-2,&n\text{ even}.\end{cases}
\]
An extremal sequence exists explicitly for every \(n\), and the exact equality criterion below characterizes *all* extremal legal total-dominating sequences by the number of two-unit reductions of a canonical potential. The theorem concerns open-neighborhood Grundy total domination, not ordinary total domination or closed-neighborhood Grundy domination.

## Assumptions and scope
All graphs are finite, undirected, loopless and simple. Write \([n]=\{0,\ldots,n-1\}\), identify \(V(T_n)\) with \(E(K_n)\), and consider a sequence of distinct edges \(\mathbf e=(e_1,\ldots,e_k)\). It is *legal* if each next selected edge has some neighbor of \(T_n\) not in the union of open neighborhoods of earlier selected edges. It is a *total-dominating sequence* if that union after the final step is all of \(V(T_n)\). Its greatest possible length is \(\gamma_{\mathrm{gr}}^{\mathrm t}(T_n)\).

For any selected-edge set \(F\subseteq E(K_n)\), let \(U(F)\) consist of original vertices incident with no edge of \(F\). Let \(I(F)\) be the set of edges that constitute one-edge connected components of the graph \(([n],F)\). In particular, its elements are pairwise vertex-disjoint. For every \(F\), define the integer potential
\[
P(F)=|U(F)|+|I(F)|.
\]
For the empty initial set, \(P(\varnothing)=n\). For a legal sequence, put \(F_i=\{e_1,\ldots,e_i\}\), \(P_i=P(F_i)\), and let \(b\) be the number of indices \(i\) with \(P_{i-1}-P_i=2\).

## Proof
**Exact uncovered-edge identity.** For any nonempty \(F\), the edges of \(K_n\) whose corresponding vertices have not yet been totally dominated in \(T_n\) are exactly
\[
\binom{U(F)}2\ \dot\cup\ I(F).
\]
Indeed, an unselected edge is adjacent to a selected edge precisely when it shares an endpoint with a selected edge, so it remains undominated exactly when both endpoints are in \(U(F)\). A selected edge is adjacent to a *different* selected edge exactly when it is not an isolated one-edge component. This proves the identity. Consequently a sequence terminates with total domination exactly when \(|U(F_k)|\leq1\) and \(I(F_k)=\varnothing\).

**Potential lemma.** Every legal addition reduces \(P\) by exactly one or two. If the new edge joins two currently unused vertices, then \(|U|\) drops by two and a new isolated selected edge is created, so \(P\) drops by one. Such a move is legal only while at least three unused vertices remain: its own vertex in \(T_n\) is not its neighbor, and no selected isolated edge meets its two unused endpoints. If exactly one endpoint is unused, then \(|U|\) drops by one, and an existing isolated selected edge is removed from \(I\) precisely when the covered endpoint belonged to such an edge. Thus the potential drops by one or two. If neither endpoint is unused, a legal addition must meet an isolated selected edge (otherwise it could not neighbor an undominated edge); it removes either one or two isolated components. Again the potential drops by one or two.

In every completed nonempty legal sequence **at least one two-unit reduction is unavoidable**. Initially the first selected edge is isolated. Before the first selected edge ceases to be isolated, all selected components are isolated single edges. The first move that destroys any such component either joins an unused vertex to a covered endpoint, eliminating one isolated edge while reducing \(|U|\) by one, or joins endpoints belonging to two distinct isolated edges. Either move drops \(P\) by two.

A completed sequence has \(P_k=|U(F_k)|\in\{0,1\}\); therefore
\[
 k=n-|U(F_k)|-b.\tag{1}
\]
Since \(b\ge1\), this gives \(k\le n-1\) for all \(n\). For even \(n\), if \(|U(F_k)|=1\) then \(k\le n-2\). If \(|U(F_k)|=0\), observe that the number of edges added with exactly one currently unused endpoint must be positive and even: the edges added with two unused endpoints remove two each, and reaching zero unused vertices by a two-unused-endpoint move is impossible because such a move is illegal when two unused vertices remain. Thus at least two one-unused-endpoint additions occur. The last one, taken with a single unused vertex left, is legal only by meeting an isolated selected edge; it drops the potential by two. There must also be an earlier two-unit reduction: otherwise, up to the first earlier one-unused-endpoint addition, all selected components are still isolated single edges, so that addition itself drops the potential by two. Hence \(b\ge2\) and \(k\le n-2\). This proves the upper bounds.

**Sharp construction.** Put \(a=\lfloor(n-1)/2\rfloor\). First select the disjoint edges \(\{0,1\},\{2,3\},\ldots,\{2a-2,2a-1\}\) in that order. Each is legal, since at least three as-yet-unused original vertices are present before its addition. Next select \(\{0,2a\}\), followed by \(\{0,2\},\{0,4\},\ldots,\{0,2a-2\}\). The first connector is legal because it neighbors the first isolated selected edge; when \(n\) is even it also dominates the sole edge between the two unused original vertices. Each remaining connector neighbors the previously undominated selected edge \(\{2j,2j+1\}\). Afterward no selected edge is isolated and at most one original vertex is unused. Hence total domination holds. The constructed sequence has \(2a\) terms, attaining the asserted formula for every \(n\ge3\).

**Characterization of equality.** Equation (1) and the preceding lower bounds on \(b\) yield the following complete test for a *legal, completed* total-dominating sequence:

- If \(n\) is odd, the sequence is longest if and only if \(|U(F_k)|=0\) and \(b=1\).
- If \(n\) is even, the sequence is longest if and only if either \(|U(F_k)|=1\) and \(b=1\), or \(|U(F_k)|=0\) and \(b=2\).

Both directions follow immediately from (1), and the construction shows that the maximum is attainable. This criterion covers all maximum sequences, without presupposing that they have the particular matching-first form used in the construction.

## Verification
The file `verify.py` implements the original neighborhood-union definition directly and independently computes the longest legal sequences by memoized exhaustive recursion on selected-edge subsets. For \(n=3,4,5,6,7,8\), it obtains maximum lengths \(2,2,4,4,6,6\), with respective numbers of ordered maximum sequences \(6,24,720,20160,453600,78865920\). These finite counts are verification data and are **not** proposed as an infinite counting formula.

A separate exhaustive test checks the uncovered-edge identity over all \(2^{\binom n2}-1\) nonempty selected-edge sets for each \(3\le n\le7\), totaling \(2,131,011\) tests (exact per-order counts are in `verification_output.json`). The explicit extremal construction is also checked directly for every \(3\le n\le50\). The infinite claim follows from the proof, not from computational extrapolation.

## Relationship to prior work
Brešar, Bujtás and collaborators introduced and compared four variants of Grundy domination, including open-neighborhood Grundy total domination. The 2017 treatment of graph products establishes bounds for products of paths and cycles, not for the Johnson graph \(J(n,2)\), which is the line graph of a complete graph rather than a Cartesian product of two factors in the studied families. Brešar, Henning and Rall give foundational general theorems for total-dominating sequences; no theorem applied in the present proof directly yields the exact triangular-graph parity law. Brešar, Kos and Torres study the complementary Kneser graphs and compute their Grundy total domination numbers; complementing edges changes open neighborhoods and does **not** imply the result here. Work on ordinary total domination and ordinary/connected zero forcing of Johnson graphs concerns different invariants.

The contribution assessed here is the exact value **together with** the incidence-potential argument and a necessary-and-sufficient equality criterion for longest sequences. The general definitions, general inequalities, and Kneser-graph results are prior work, not claimed as new. Searches cannot rule out unindexed or differently worded equivalent results.

## Limitations
The theorem is restricted to \(J(n,2)\) with \(n\ge3\); it gives no claim for higher-subset Johnson graphs. The potential equality characterization does not count all optimal sequences symbolically. It does not assert a formula for ordinary total domination or the standard zero-forcing number. The Kneser-graph paper was only accessible through its bibliographic abstract during comparison, leaving a source-access priority risk; related full texts and mathematical-search results were examined. Independent mathematical audit has not been performed.

## References
1. B. Brešar, C. Bujtás, T. Gologranc, S. Klavžar, G. Košmrlj, B. Patkós, Z. Tuza and M. Vizer, *Grundy dominating sequences and zero forcing sets*, arXiv:1702.00828v1 (first public 2017-02-02), https://arxiv.org/abs/1702.00828.
2. B. Brešar et al., *On Grundy total domination number in product graphs*, arXiv:1712.08780v1 (first public 2017-12-23), https://arxiv.org/abs/1712.08780.
3. B. Brešar, M. A. Henning and D. F. Rall, *Total Dominating Sequences in Graphs*, arXiv:1601.07525v1 (2016), https://arxiv.org/abs/1601.07525.
4. B. Brešar, T. Kos and P. Torres, *Grundy domination and zero forcing in Kneser graphs*, Ars Mathematica Contemporanea 17 (2019), DOI:10.26493/1855-3974.1881.384; repository entry https://www.dlib.si/details/URN:NBN:SI:doc-CWN748I8.
