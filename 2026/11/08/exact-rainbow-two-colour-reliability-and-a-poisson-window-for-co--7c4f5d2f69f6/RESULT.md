# Exact rainbow two-colour reliability and a Poisson window for cocktail-party graphs

## Finding

**Theorem.** For every integer \(m\ge2\), let \(G_m=K_{2m}-M\), where \(M\) is a fixed perfect matching. An edge receives one of two *named* colours, red and blue. Let \(F_m(t)\) count rainbow-connecting colourings by the number of red edges. Then

\[
F_m(t)=\sum_{k=0}^{m}(-1)^k\binom{m}{k}
(1+t^4)^{\binom{k}{2}}
(1+t^2)^{2k(m-k)}
(1+t)^{4\binom{m-k}{2}}.
\]

In particular, \(F_2(1)=10\), \(F_3(1)=3416\), and \(F_4(1)=15775808\). If every edge is independently red with probability \(p\) and blue with probability \(1-p\), the probability \(R_m(p)\) that every pair of vertices has a rainbow path is

\[
R_m(p)=\sum_{k=0}^{m}(-1)^k\binom{m}{k}
\bigl[p^4+(1-p)^4\bigr]^{\binom{k}{2}}
\bigl[p^2+(1-p)^2\bigr]^{2k(m-k)}.
\]

For any fixed real \(c\), put \(p_m=(\log m+c)/(4m)\) for sufficiently large \(m\) (natural logarithm). Then

\[
\lim_{m\to\infty} R_m(p_m)=\exp(-e^{-c}).
\]

The same limit holds at the colour-swapped bias \(1-p_m\). Thus the complete exact enumerator and a sharp critical reliability window follow from one bad-pair intersection formula.

## Assumptions and scope

All graphs are finite, simple, undirected, and labelled, and \(m\) is an integer at least two. Write the matched nonedges as \(P_i=\{(i,0),(i,1)\}\) for \(1\le i\le m\). Every pair of vertices in different \(P_i\)'s is an edge, so \(G_m\) has \(2m(m-1)\) edges. A path is rainbow if its edges have pairwise distinct colours; in a two-colour edge colouring, rainbow paths have at most two edges. The entire set of edge assignments is counted, without identifying colour swaps or graph automorphisms. The polynomial uses one factor \(t\) for each red edge, with blue edges of weight one. Independence in the probability model refers to edge colours, not vertex events.

## Proof

**1. Exact bad events.** An adjacent pair is connected by its single edge. Hence rainbow connection fails exactly when some nonadjacent pair \(P_i\) admits no two-edge red-blue path. For \(i\in\{1,\ldots,m\}\), denote this event by \(B_i\). The intermediate vertex of any two-edge path between \((i,0)\) and \((i,1)\) belongs to another matched pair. Event \(B_i\) is therefore equivalent to: for each \(w\notin P_i\), the two edges from \((i,0)\) and \((i,1)\) to \(w\) have the *same* colour.

**2. Block factorization.** Fix any \(S\subseteq\{1,\ldots,m\}\) with \(|S|=k\), and require all events \(B_i\) for \(i\in S\). Between two different matched pairs \(P_i,P_j\), the four edges form a complete bipartite graph with two vertices per side. If \(i,j\in S\), every row and column must be monochromatic, forcing all four edges to carry one common colour; their red-weight generating factor is \(1+t^4\). If exactly one index belongs to \(S\), the constraints force two independent pairs of equal-coloured edges, giving \((1+t^2)^2\). If neither index is in \(S\), the four edges are free, giving \((1+t)^4\). Distinct blocks are edge-disjoint, so these conditions factor exactly. There are \(\binom{k}{2}\), \(k(m-k)\), and \(\binom{m-k}{2}\) blocks of the three types, respectively. Therefore the red-weight generating function of the simultaneous event intersection is

\[
W_{m,k}(t)=(1+t^4)^{\binom{k}{2}}
(1+t^2)^{2k(m-k)}(1+t)^{4\binom{m-k}{2}}.
\]

Inclusion-exclusion over the \(m\) events \(B_i\), exploiting symmetry among \(k\)-element subsets, proves the polynomial identity. Because the individual blocks contain respectively four, four, or four edges, every term has the correct total maximum degree \(2m(m-1)\). In particular \(F_m(t)\) is self-reciprocal under swapping red and blue.

**3. Independent colour biases.** For a given pair of matched-pair blocks, the probability of four equal colours is \(a=p^4+(1-p)^4\). The probability of two equal-coloured edges is \(q=p^2+(1-p)^2\). Thus the event intersection probability is exactly

\[
\Pr\!\left(\bigcap_{i\in S}B_i\right)
=a^{\binom{k}{2}}q^{2k(m-k)}.
\]

Inclusion-exclusion proves \(R_m(p)\), valid also at \(p=0,1\).

**4. Critical window.** Let \(X_m=\sum_{i=1}^m\mathbf1_{B_i}\). For fixed nonnegative integer \(k\), the identity above gives the factorial-binomial moments

\[
\mathbb E\binom{X_m}{k}=\binom{m}{k}
\bigl[p_m^4+(1-p_m)^4\bigr]^{\binom{k}{2}}
\bigl[p_m^2+(1-p_m)^2\bigr]^{2k(m-k)}.
\]

Since \(p_m\to0\), \(p_m^2m\to0\), and \(4mp_m=\log m+c\), we have \(\log[p_m^2+(1-p_m)^2]=-2p_m+O(p_m^2)\). For each fixed \(k\), the logarithm of the second bracket times \(2k(m-k)\) is \(-k(\log m+c)+o(1)\), while the first bracket tends to one. It follows that

\[
\mathbb E\binom{X_m}{k}\longrightarrow \frac{e^{-ck}}{k!}.
\]

For every fixed truncation level, the two Bonferroni bounds sandwich \(\Pr(X_m=0)\) between successive odd- and even-indexed partial sums of \(\sum_{k\ge0}(-1)^k e^{-ck}/k!\). Take the limit \(m\to\infty\) first at fixed truncation, then let the truncation grow. The convergent exponential series gives \(\Pr(X_m=0)\to\exp(-e^{-c})\). But \(X_m=0\) is exactly rainbow connection. Swapping the two named colours gives the symmetrical bias statement.

## Verification

Run `python3 verify.py` with Python 3 standard library. The verifier independently constructs the original edge sets, exhaustively enumerates all two-colour assignments for \(m=2\) and \(m=3\), computes the original geodesic rainbow-connection predicate for every missing pair, and matches the entire red-edge histogram with the formula. It also checks *every* simultaneous bad-event intersection histogram in those sizes, tests the biased probabilities at rational biases, and checks nonnegative symmetric coefficients and total counts for \(m=2,3,4\). Expected final line: `VERIFY_OK`. Finite checks corroborate but do not prove the infinite result; the proof above supplies all parameter ranges.

## Relationship to prior work

Aruna and Jeyakokila (2023, Theorem 2.1) establish that every cocktail-party graph of order at least four has rainbow connection number two; their result is existential rather than a count of named colourings or their red-edge weights. Gyárfás and Sárközy (first preprint 2025; published 2026, Theorem 1) prove that every two-edge-coloured cocktail-party graph admits two monochromatic 2-reachable vertex sets covering its vertices; this property does not say whether every missing pair has a red-blue path and does not yield its counting polynomial. Barát, Boyadzhiyska and Freschi (2026) analyze rainbow-connecting two-colourings of general super-Dirac graphs and random-colouring existence; their results do not specialize to the complete red-edge enumerator or the exact critical window above. The present proof derives a blockwise event-intersection identity exploiting the exact perfect-matching complement structure. It does not assert priority over all possible equivalent, unlocated enumerations.

## Limitations

The result concerns exactly two named edge colours on a fixed labelled cocktail-party graph. The asymptotic holds for the explicit small-bias window (and its colour-swapped counterpart); it is not a general random-graph rainbow-connectivity theorem. Counts are not quotiented by graph automorphisms. Historical priority has not been independently certified, and no independent audit of the proof has been performed.

## References

- J. Barát, S. Boyadzhiyska and A. Freschi, *Rainbow connecting 2-colorings of super-Dirac graphs*, arXiv:2609.11437v1, first posted 2026-09-10. https://arxiv.org/abs/2609.11437
- T. Aruna and S. P. Jeyakokila, *Some results on rainbow connection number of graph*, Advances and Applications in Mathematical Sciences **22** (2023), 1743–1753, Theorem 2.1. https://www.mililink.com/upload/article/780357251aams_vol_228_june_2023_a6_p1743-1753_t._aruna_and_s._p._jeyakokila.pdf
- A. Gyárfás and G. N. Sárközy, *2-Reachable Subsets in Two-Colored Graphs*, Graphs and Combinatorics **42** (2026), article 43; initially arXiv:2506.11696, first posted 2025-06-13. https://arxiv.org/abs/2506.11696
