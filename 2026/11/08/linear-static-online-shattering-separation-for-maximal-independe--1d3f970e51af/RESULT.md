# Linear static–online shattering separation for maximal independent sets of paths

## Finding

Let \(P_n\) be the simple path on vertices \(1,\ldots,n\), for every integer \(n\ge1\). Let \(\mathcal M_n\) consist of the incidence vectors of all **inclusion-maximal** independent vertex sets of \(P_n\) (not only the maximum-cardinality independent sets). Membership at a vertex is the binary query. Then

\[
\operatorname{VCdim}(\mathcal M_n)=\left\lfloor\frac{n+1}{3}\right\rfloor \qquad(n\ge1).
\]

For \(1\le n\le9\), the Littlestone dimension equals this VC dimension. At the first strict separation,

\[
\operatorname{VCdim}(\mathcal M_{10})=3,\qquad
\operatorname{Ldim}(\mathcal M_{10})=4.
\]

The gap persists and grows linearly even when the underlying graph must stay a **connected path**. For every integer \(k\ge1\),

\[
\operatorname{Ldim}(\mathcal M_{11k-1})\ge4k,
\qquad
\operatorname{Ldim}(\mathcal M_{11k-1})-\operatorname{VCdim}(\mathcal M_{11k-1})
\ge \left\lceil\frac{k}{3}\right\rceil.
\]

The lower bound is a constructive embedding of \(k\) independently chosen ten-vertex path hypotheses across single separating vertices. No exact general formula for the Littlestone dimension is asserted beyond the first ten path orders.

## Assumptions and scope

An independent set contains no adjacent pair. It is *maximal* if every unselected vertex has a selected neighbor. Thus a binary word belongs to \(\mathcal M_n\) precisely when it contains neither adjacent ones nor an undominated zero (a zero whose in-range neighbors are also zero). The auxiliary class \(\mathcal M_0\) consists of the empty word and has both dimensions zero.

A set \(S\subseteq\{1,\ldots,n\}\) is VC-shattered when each binary labeling of its vertices extends to a word in \(\mathcal M_n\). A complete Littlestone mistake tree of depth \(h\) has one vertex query at each internal node and, for every one of its \(2^h\) binary root-to-leaf paths, at least one word in the class realizing all the answers along that path. The largest such depth is \(\operatorname{Ldim}\). The conventions include depth zero for singleton classes. Graphs are finite, simple, and labeled in path order.

## Proof

**1. Exact static dimension.** Put \(d(n)=\operatorname{VCdim}(\mathcal M_n)\), and \(d(0)=0\). For a lower bound, take the \(t=\lfloor(n+1)/3\rfloor\) vertices \(2,5,8,\ldots,3t-1\). Associate them with their immediate left neighbors \(1,4,7,\ldots,3t-2\). The resulting disjoint edges form an induced matching: there is no edge between endpoints belonging to different pairs. Given any desired membership labeling of the selected vertices, choose the queried vertex from each pair when its label is one and choose its left neighbor when the label is zero. The chosen vertices are independent; greedily extend them to a maximal independent set of the entire path. Every labeling is obtained, so \(d(n)\ge t\). For \(n=1\), the empty support gives the same bound.

For the upper bound use induction on \(n\), with the cases \(n=0,1,2\) immediate. Suppose \(n\ge3\) and a nonempty set \(S\) is shattered; write \(a=\min S\). Necessarily \(S\) is independent, as its all-one labeling is realizable.

If \(a\ge2\), fix the answer at vertex \(a\) to be one while allowing all labelings on \(S\setminus\{a\}\). The neighbor \(a+1\), when present, must be zero. In every realizing maximal independent set, restriction to the suffix \(a+2,\ldots,n\) is itself a maximal independent set of that suffix path: its first vertex cannot rely on \(a+1\) for domination, and all subsequent vertices are internal to the suffix. Since \(S\setminus\{a\}\) lies there, this suffix shatters it. The suffix has \(m=\max\{n-a-1,0\}\le n-3\) vertices. By induction,

\[
|S|\le1+d(m)\le1+\left\lfloor\frac{m+1}{3}\right\rfloor
\le1+\left\lfloor\frac{n-2}{3}\right\rfloor
=\left\lfloor\frac{n+1}{3}\right\rfloor.
\]

If \(a=1\), instead fix the answer at vertex \(1\) to be zero. Maximality forces vertex \(2\) to be one and vertex \(3\) to be zero. Shattering implies \(3\notin S\), since every labeling of the other queried vertices must still be possible; independence implies \(2\notin S\). Therefore \(S\setminus\{1\}\subseteq\{4,\ldots,n\}\). Restrictions of the realizing words to that suffix are maximal independent sets (vertex \(4\) cannot be dominated by the fixed zero at \(3\)). The induction bound for the suffix of length \(n-3\) gives

\[
|S|\le1+d(n-3)\le1+\left\lfloor\frac{n-2}{3}\right\rfloor
=\left\lfloor\frac{n+1}{3}\right\rfloor.
\]

This proves the static classification for every \(n\).

**2. The first adaptive excess.** Let \(p_n=|\mathcal M_n|\). A maximal independent set starts either with the prefix \(10\), followed by a maximal independent set of the remaining path, or with the prefix \(010\), followed by a maximal independent set of the remaining path. Thus \(p_n=p_{n-2}+p_{n-3}\) for \(n\ge3\), with \(p_0=p_1=1\), \(p_2=2\). This gives, for \(n=1,\ldots,10\), respectively,

\[
(p_1,\ldots,p_{10})=(1,2,2,3,4,5,7,9,12,16).
\]

For every finite class \(\mathcal H\), the cardinality bound \(\operatorname{Ldim}(\mathcal H)\le\lfloor\log_2|\mathcal H|\rfloor\) follows because distinct leaves of a complete mistake tree require distinct realizing hypotheses. Also \(\operatorname{Ldim}\ge\operatorname{VCdim}\), by asking the elements of a shattered support in the same fixed order at every level. Applying these bounds to the displayed counts proves equality for \(1\le n\le9\).

For \(n=10\), the cardinality bound is four. The attached `tree_P10.json` contains a complete binary depth-four tree with fifteen internal vertex queries and sixteen terminal length-ten words. Each leaf word independently satisfies independence and domination; every bit on its query path matches the prescribed answer. The sixteen leaf words are distinct, and the independent verifier `verify.py` checks their completeness against an enumeration of all sixteen maximal independent sets of \(P_{10}\). Hence \(\operatorname{Ldim}(\mathcal M_{10})\ge4\), matching the cardinality upper bound. The VC formula gives three, so ten is the first strict separation.

**3. A connected-path amplification.** For \(k\ge1\), partition the vertices of \(P_{11k-1}\) into \(k\) consecutive blocks of ten vertices, with exactly one unqueried separator vertex between adjacent blocks. Choose arbitrary \(B_1,\ldots,B_k\in\mathcal M_{10}\). At a separator, place a one *if and only if* both adjoining block endpoints are zero; otherwise place a zero. In the first case the separator is independent of both neighbors; in the second case it is dominated by an endpoint containing a one. Every block retains internal independence and domination, and separators are not adjacent to each other. The concatenated word is therefore a maximal independent set of the entire connected path, and its restriction to block \(i\) is exactly \(B_i\).

Consequently the projection of \(\mathcal M_{11k-1}\) onto the union of the blocks contains the full product \(\mathcal M_{10}^{\,k}\). Run the certified four-level tree successively in block one, then block two, and so forth. Each root-to-leaf pattern is jointly realizable by the preceding separator rule, furnishing a complete tree of depth \(4k\). Combining this with the exact VC dimension yields

\[
4k-\left\lfloor\frac{11k}{3}\right\rfloor
=\left\lceil\frac{k}{3}\right\rceil
\]

as a lower bound on the adaptive-minus-static dimension gap. In particular the gap is unbounded and is at least \(k/3\) along the order sequence \(11k-1\), or asymptotically at least one thirty-third of the number of vertices.

## Verification

Run `python3 verify.py` in a directory containing `verify.py` and `tree_P10.json`, using only the Python standard library. The verifier enumerates maximal independent sets by *both* independence and domination conditions; computes VC dimensions for lengths one through twelve; calculates exact Littlestone dimensions by a separate exhaustive recurrence for lengths one through ten; checks every internal query and all sixteen leaf words of the supplied tree; and tests the separator embedding for every tuple of blocks when \(k=1,2,3\). The observed terminal line is `MIS_PATH_SHATTERING_CERTIFICATE_PASS`. Direct computational checking is limited to these finite instances; the induction and separator arguments supply the assertions for arbitrary lengths.

## Relationship to prior work

Liu, Shangguan, Skokan and Xu (arXiv:2403.17910, initially public 26 March 2024) define the maximal-independent-set hypergraph \(\mathcal M(G)\) and prove in their full version, Lemma 2.20 (conference version, Lemma 27), that its VC dimension is bounded by the bipartite induced matching number. This is the closest directly overlapping graph/hypergraph formulation. That general inequality does not determine the exact path value: for \(P_{10}\), a bipartite induced matching of size four exists, whereas the exact VC dimension here is three. Their text does not calculate the Littlestone dimension or a connected-path separation. Malliaris and Moran (2021) develop the model-theoretic/online-learning interpretation of Littlestone classes without these path calculations. Krivelevich, Mészáros, Michaeli and Shikhelman (2023) investigate random greedy maximal independent sets on paths, rather than the worst-case static and adaptive shattering of their full concept family. These are differences in mathematical implication, not merely terminology. Searches for minimal vertex covers, independent dominating sets, dual hypergraph formulations, and online mistake trees found no stronger covering result in the inspected sources; priority under less standard terminology remains uncertain.

## Limitations

The exact general Littlestone dimension of \(\mathcal M_n\) for \(n>10\) is not determined. The construction supplies a lower bound only along \(n=11k-1\); it does not assert optimality of that bound. The finite certificate verifies the depth-four gadget and small cases, not an arbitrary-length claim without the written proof. Historical novelty has been checked against identified literature and research records but not exhaustively certified. Independent expert validation has not been performed.

## References

1. H. Liu, C. Shangguan, J. Skokan, and Z. Xu, *Beyond chromatic threshold via the \((p,q)\)-theorem, and a sharp blow-up phenomenon*, arXiv:2403.17910, first submitted 26 March 2024; full version Lemma 2.20 and SoCG 2024 version Lemma 27. https://arxiv.org/abs/2403.17910
2. M. Malliaris and S. Moran, *Agnostic Online Learning and Excellent Sets*, arXiv:2108.05569, initially submitted 12 August 2021. https://arxiv.org/abs/2108.05569
3. M. Krivelevich, T. Mészáros, P. Michaeli, and C. Shikhelman, *Greedy maximal independent sets via local limits*, Random Structures & Algorithms 64 (2024), 986–1015, first published online 18 December 2023. https://doi.org/10.1002/rsa.21200
