# Star-core isometry orderings in random graphs and the almost-all distance-preservation conjecture

## Finding
Let \(G(n,p)\) be the binomial random graph on \(n\ge3\) labelled vertices, with independent edge probability \(0\le p\le1\). Call an induced subgraph **isometric** if all distances between its vertices agree with their distances in the full graph. Call a graph **sequentially distance preserving** (sdp) if there is one ordering of all its vertices such that every nonempty prefix induces an isometric subgraph.

For a specified vertex \(v\), consider any ordering that puts \(v\) first, then all its neighbors in arbitrary order, then all its nonneighbors in arbitrary order. The probability that **every such ordering** is isometric at **every prefix length** is at least \(1-B_n(p)\), where

\[
B_n(p)=(n-1)(1-p)(1-p^2)^{n-2}
+\binom{n-1}{2}(1-p)(1-p^2)(1-p^3)^{n-3}.
\]

Consequently, the probability that **every vertex** can be the first vertex of such a universally valid star-first ordering is at least \(1-nB_n(p)\). These lower bounds are understood as vacuous when negative.

For any sequence \(p=p_n\), if
\[
(n-3)p_n^3-3\log n\longrightarrow+\infty,
\]
then with probability tending to one **every vertex** gives a valid ordering of this form. The weaker condition with \(2\log n\) in place of \(3\log n\) suffices for one predetermined first vertex. In particular, for every fixed \(0<p<1\), \(G(n,p)\) is sdp with probability \(1-\exp(-\Omega_p(n))\).

In the uniform model \(p=1/2\), it follows not just that almost every *labelled* graph is sdp, but also that the proportion of *unlabelled connected* graphs that are sdp tends to one. This proves the almost-all distance-preservation conjecture in its conventional unlabelled-connected interpretation, with the stronger nested-ordering property.

## Assumptions and scope
Graphs are finite, undirected, unweighted, simple, and have no loops. Distances are standard shortest-path distances (infinite for disconnected pairs). An isometric induced graph must preserve all original distances on its surviving vertices. All logarithms are natural. The random model is independent-edge \(G(n,p_n)\); for the unlabelled counting statement only, the uniform labelled model \(p=1/2\) is transferred to unlabelled graph classes by Burnside's lemma. The density condition is sufficient, not asserted necessary or optimal. The initial vertex \(v\) is predetermined, not selected after observing the random graph.

## Proof
**1. A deterministic star-core certificate.** Fix a graph \(G\) and a vertex \(v\). Put \(W=N_G[v]\). Suppose every **nonedge** \(xy\) of \(G\) has a common neighbor in \(W\):
\[
xy\notin E(G)\quad\Longrightarrow\quad N_G(x)\cap N_G(y)\cap W\ne\varnothing.
\tag{1}
\]
Order \(v\) first, next its neighbors, then its nonneighbors, independently of the order inside either block. For a nonempty prefix \(S\) contained in \(W\), every vertex of \(S\setminus\{v\}\) is adjacent to \(v\). Hence all nonadjacent pairs of \(S\) have distance two in \(G[S]\), while adjacent pairs have distance one. Since the same two-step paths exist in \(G\), these distances are exactly those of \(G\). For every longer prefix \(S\), the entire set \(W\) lies inside \(S\). By (1), every nonedge of \(G[S]\) has a common neighbor inside \(W\subseteq S\), so again its distance in \(G[S]\) is exactly two, as it is in \(G\). Edges retain distance one. Thus every prefix is isometric, regardless of the two internal orders. Condition (1) also guarantees diameter at most two when \(n\ge2\); this is a *sufficient* certificate, not a characterization of all sdp graphs.

**2. Exact witness-failure probabilities and a union bound.** In \(G(n,p)\), fix \(v\). A specific pair \(\{v,x\}\) is a nonedge and has no common neighbor in \(N_G[v]\) with probability
\[
(1-p)(1-p^2)^{n-2}.
\tag{2}
\]
Indeed, for each of the other \(n-2\) potential common neighbors \(z\), both independent edges \(vz\) and \(xz\) must be present; these two-edge events are independent over distinct \(z\).

For a pair \(\{x,y\}\) not containing \(v\), the corresponding failure probability is exactly
\[
(1-p)(1-p^2)(1-p^3)^{n-3}.
\tag{3}
\]
The first factor makes \(xy\) a nonedge; the second prevents \(v\) itself from being their common neighbor; each of the remaining \(n-3\) vertices \(z\) would be a witness in \(N_G[v]\) precisely when all three distinct edges \(vz,xz,yz\) are present. The edge groups used for distinct \(z\) and for the first two factors are disjoint, so the product is exact. Union bounding (2) over \(n-1\) pairs and (3) over \(\binom{n-1}{2}\) pairs proves the displayed \(B_n(p)\) bound. Union bounding once more over \(n\) possible centers gives the every-center bound. No independence is claimed between different pairs or different centers.

**3. Sparse densities and exponential convergence.** Since \(1-t\le e^{-t}\), for all \(0\le p\le1\),
\[
B_n(p)\le (n-1)e^{-(n-2)p^2}+\binom{n-1}{2}e^{-(n-3)p^3}.
\tag{4}
\]
If \((n-3)p_n^3-3\log n\to+\infty\), both terms in \(nB_n(p_n)\) tend to zero; for the first, use \(p_n^2\ge p_n^3\). The same argument with the factor \(n\) omitted gives the \(2\log n\) fixed-center criterion. If \(p\) is a fixed number strictly between zero and one, both terms of (4) decay exponentially up to polynomial factors, which proves the stronger fixed-density assertion.

**4. From labelled random graphs to unlabelled connected graphs.** Let \(N=\binom n2\) and let \(F(\pi)\) be the number of labelled graphs fixed by a permutation \(\pi\in S_n\). If \(\pi\) moves exactly \(m\ge2\) vertices, at most \(\binom{n-m}{2}+m/2\) of the \(N\) possible edge positions are fixed by \(\pi\); hence at least
\[
r\ge m(n-1-m/2)\ge m(n-2)/2
\]
edge positions move. An orbit of \(\ell\ge2\) moved edge positions contributes at most \(2^{-(\ell-1)}\le2^{-\ell/2}\) to \(F(\pi)/2^N\). Therefore
\[
\sum_{\pi\ne\mathrm{id}}\frac{F(\pi)}{2^N}
\le\sum_{m=2}^n n^m2^{-m(n-2)/4}=o(1).
\tag{5}
\]
For any isomorphism-invariant bad-graph property \(\mathcal B\), Burnside's lemma and (5) bound the number of unlabelled bad classes by
\[
\frac{2^N}{n!}\bigl(\Pr(G(n,1/2)\in\mathcal B)+o(1)\bigr),
\]
whereas the number of all unlabelled graph classes is \(\frac{2^N}{n!}(1+o(1))\). Our bad event, failure to be sdp, has labelled probability \(o(1)\) by Step 3. Moreover, the probability that \(G(n,1/2)\) is disconnected satisfies
\[
\Pr(G(n,1/2)\text{ disconnected})
\le\sum_{k=1}^{\lfloor n/2\rfloor}\binom nk2^{-k(n-k)}=o(1).
\]
Applying the same Burnside estimate to the union of these two invariant bad events proves that the unlabelled *connected* sdp proportion tends to one. In particular, their weaker distance-preserving proportion tends to one. The proof needs no assumption that all random graphs are asymmetric; the needed asymmetry estimate was proved explicitly in (5).

## Verification
The source file `check_exhaustive.cpp` enumerates every labelled simple graph of order at most six (33,867 labelled graph instances in total), tests the exact nonedge-witness certificate for every possible center, and, whenever the certificate holds, checks all pairwise distances in every prefix of four independently ordered neighbor/nonneighbor variants. All 52,923 certified graph-center pairs passed. It does not attempt to prove the asymptotic theorem by finite enumeration.

The independently written `check_random.py` samples 630 reproducible finite random graphs of orders seven through twenty, builds the witness certificate by set intersection, and checks each prefix distance matrix by breadth-first search; all 6,015 certified centers passed. The proofs of (2)–(5), not these experiments, establish the infinite and unlabelled claims. Both programs depend only on standard C++17 or Python 3 libraries and may be executed as `c++ -O2 -std=c++17 check_exhaustive.cpp -o verify && ./verify` and `python3 check_random.py`.

## Relationship to prior work
The distance-preserving property and the conjecture that almost all connected graphs are distance preserving were formulated by Nussbaum and Esfahanian, with finite enumerations through eleven vertices and an earlier sufficient minimum-degree condition. The construction of star-prefix subgraphs in the *first phase* of their minimum-degree proof is acknowledged: the new ingredient is the random, all-pairs common-neighbor certificate inside the *same* star core, allowing arbitrary sparse fixed densities, and the explicit labelled-to-unlabelled transfer. Later work by Zahedi formulated the almost-all question explicitly, and Smith and Zahedi identified weakly four-simplicial elimination orderings and proved sequential preservation for four-chordal graphs. The 2025 continuation still describes almost-all distance preservation as a conjecture. None of those inspected results supplies an all-density random-graph proof, the finite failure probability above, or the universal star-first certificate.

The 2019 degree theorem of Khalifeh and Zahedi applies to minimum degree above \((1/2+\varepsilon)n\) in sufficiently large graphs and concerns distance preservation, not the stronger nested property; it therefore does not imply the statement for fixed \(p<1/2\), let alone the stated vanishing-density range. The current proof does not claim sharpness of its density threshold. Priority uncertainty remains for unindexed independent proofs of the same probabilistic question.

## Limitations
The sufficient density threshold \(np^3\) on the order of \(\log n\) is not proved sharp, and the theorem does not characterize distance preservation at the connectivity threshold. The explicit failure bound can exceed one at small orders or small densities. The unlabelled conclusion applies to the uniform graph-class model, inferred from \(p=1/2\), not to arbitrary \(p\)-weighted unlabelled graph measures. The all-center assertion is for the star-first ordering block form described here, not every possible vertex permutation. This is a mathematical proof with self-review only; independent scholarly validation is not claimed.

## References
1. R. Nussbaum and A.-H. Esfahanian, *Preliminary Results on Distance-Preserving Graphs*, Congressus Numerantium 211 (2013), pp. 141–149; author-hosted text: https://cse.msu.edu/~esfahani/Publications/2013/Preliminary_Results_on_distance-Preserving_graphs.pdf.
2. A.-H. Esfahanian, R. Nussbaum, D. Ross and B. E. Sagan, *On Constructing Regular Distance-Preserving Graphs*, arXiv:1405.1713, first posted 7 May 2014, https://arxiv.org/abs/1405.1713.
3. E. Zahedi, *Distance Preserving Graphs*, arXiv:1507.03615, first posted 13 July 2015, especially Question 5.7, https://arxiv.org/abs/1507.03615.
4. J. P. Smith and E. Zahedi, *On Distance Preserving and Sequentially Distance Preserving Graphs*, arXiv:1701.06404 (2017), especially Proposition 3.4 and Theorem 3.5, https://arxiv.org/abs/1701.06404.
5. M. H. Khalifeh and E. Zahedi, *On a conjecture about the existence of isometric subgraphs*, Journal of Graph Theory 94 (2020), 299–302, https://doi.org/10.1002/jgt.22521.
6. J. P. Smith and E. Zahedi, *On distance preserving and sequentially distance preserving graphs*, Art of Discrete and Applied Mathematics 8 (2025), P2.05, https://doi.org/10.26493/2590-9770.1813.5ce.
