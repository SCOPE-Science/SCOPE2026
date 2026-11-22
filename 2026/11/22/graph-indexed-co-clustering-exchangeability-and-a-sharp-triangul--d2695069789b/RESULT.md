# Graph-indexed co-clustering exchangeability and a sharp triangular horizon for Ewens–Pitman partitions

## Finding
Let \(n\ge3\) be an integer and let \(G\) be any finite simple graph on \([n]\) with at least one edge. Generate an exchangeable Ewens–Pitman random set partition \(\Pi\) of \([n]\) with parameters \(0\le\alpha<1\) and \(\theta>-\alpha\). For every edge \(e=\{u,v\}\), let \(X_e\) be one when the endpoints belong to the same partition block, and zero otherwise.

**Complete classification:** the edge-coordinate vector \((X_e:e\in E(G))\) is exchangeable if and only if the non-isolated part of \(G\) is a **matching, a star, or a triangle**. Isolated vertices are irrelevant. The matching and star vectors admit infinite exchangeable Bernoulli extensions. For a triangle, the sharp maximal extension length is
\[
N_{\max}(\alpha,\theta)=\left\lfloor\frac{\theta+3-\alpha}{1-\alpha}\right\rfloor.
\]
For every integer \(N\) with \(3\le N\le N_{\max}\), an exchangeable length-\(N\) extension exists and is unique in distribution; for larger \(N\), no such extension exists. In particular, the triangle vector is never infinitely extendible.

## Assumptions and scope
The graph is simple (no loops or parallel edges); the partition has the **two-parameter** sampling-consistent law with \(\alpha\in[0,1)\) and \(\theta>-\alpha\), not a uniformly selected set partition. Vertex labels and incident-edge ordering do not affect the asserted distributional symmetry. All parameters are finite reals, and all claimed extension lengths are integers. A length-\(N\) extension means an exchangeable \(\{0,1\}\)-valued vector whose first \(|E(G)|\) coordinates have the original joint law. The only nonempty graphs with at least one edge covered by the classification are matchings, stars, and triangles; a single edge is both a matching and star.

For reference, the Ewens–Pitman exchangeable partition probability function for a *particular* partition into \(k\) blocks with sizes \(n_1,\ldots,n_k\), where \(\sum_i n_i=n\), is
\[
p_{\alpha,\theta}(n_1,\ldots,n_k)
=\frac{\prod_{j=1}^{k-1}(\theta+j\alpha)}{\prod_{j=1}^{n-1}(\theta+j)}
\prod_{i=1}^{k}\prod_{r=1}^{n_i-1}(r-\alpha).
\]
Empty products equal one. Pitman's exchangeable construction and consistency justify restricting to two, three, or four named vertices.

## Proof
**Step 1 (pair-type distinction).** Let \(p_{\mathrm{adj}}\) be the probability that two given distinct graph edges sharing a vertex both have indicator one. Their endpoints are three labels forced into one partition block, so
\[
p_{\mathrm{adj}}=\frac{(1-\alpha)(2-\alpha)}{(\theta+1)(\theta+2)}.
\]
If the two edges are disjoint, their four endpoints either occupy one block or two specified two-element blocks. Hence
\[
p_{\mathrm{dis}}=
\frac{(1-\alpha)\bigl((2-\alpha)(3-\alpha)+(\theta+\alpha)(1-\alpha)\bigr)}{(\theta+1)(\theta+2)(\theta+3)}.
\]
A direct subtraction gives
\[
p_{\mathrm{adj}}-p_{\mathrm{dis}}
=\frac{(1-\alpha)(\theta+\alpha)}{(\theta+1)(\theta+2)(\theta+3)}>0.
\]
All denominators are positive on the stated parameter domain. Thus coordinate-exchangeability forbids a graph from containing *both* an incident pair of edges and a disjoint pair of edges: a coordinate permutation would have to preserve their two different joint probabilities.

**Step 2 (graph classification and sufficiency).** If every pair of distinct edges is disjoint, \(G\) has only matching components. If all pairs of edges intersect, choose two edges with common endpoint \(v\). Any third edge not containing \(v\) must join their two other endpoints. Such an edge completes a triangle and precludes a fourth distinct edge meeting all three; otherwise every edge includes \(v\) and the graph is a star. This argument includes one- and two-edge cases. Conversely, for each matching, star, or triangle, *every* permutation of its edges is induced by a relabeling of vertices of the non-isolated graph. Exchangeability of the vertex partition therefore gives exchangeability of the edge indicators.

**Step 3 (infinite extensions for matchings and stars).** Pitman's construction supplies an exchangeable, consistent partition of the positive integers with these finite-dimensional laws. For a star, fix one vertex and select countably many other vertices as leaves. For a matching, select countably many disjoint vertex pairs. The resulting infinite indicator sequences are exchangeable by invariance under finite permutations of vertex labels, and their first \(|E(G)|\) indicators have the specified finite laws. The empty isolated portion contributes no indicators.

**Step 4 (triangle joint law).** Name the three edge indicators \(X_1,X_2,X_3\) in arbitrary order, and abbreviate
\[
D=(\theta+1)(\theta+2),\quad
A=\frac{(1-\alpha)(2-\alpha)}{D},\quad
B=\frac{(1-\alpha)(\theta+\alpha)}{D},\quad
C=\frac{(\theta+\alpha)(\theta+2\alpha)}{D}.
\]
The partition of three vertices is either one block, exactly one doubleton, or three singletons. Therefore the binary vector has probability \(A\) at \((1,1,1)\), probability \(B\) at each of \((1,0,0),(0,1,0),(0,0,1)\), probability \(C\) at \((0,0,0)\), and probability zero at each vector having exactly two ones. The masses satisfy \(A+3B+C=1\), with \(A>0\) and \(B>0\).

**Step 5 (sharp extension bound and construction).** Let \(Y_1,\ldots,Y_N\) be any exchangeable Bernoulli extension for an integer \(N\ge3\), and put \(K=\sum_{i=1}^N Y_i\). Conditioned on \(K=k\), the one-set of the \(Y_i\)'s must be a uniformly random \(k\)-subset by exchangeability. If \(2\le k\le N-1\), a uniformly drawn triple has exactly two ones with positive probability. The triangle law assigns that outcome probability zero. Thus necessarily
\[
\Pr(K\in\{0,1,N\})=1.
\]
Writing \(w_j=\Pr(K=j)\), its three-label law uniquely forces
\[
w_N=A,\qquad w_1=NB,\qquad
w_0=1-A-NB
=\frac{(\theta+\alpha)\bigl(\theta+3-\alpha-N(1-\alpha)\bigr)}{D}.
\]
Since \(\theta+\alpha>0\), nonnegativity of \(w_0\) is equivalent to \(N\le(\theta+3-\alpha)/(1-\alpha)\). For every such \(N\), all three weights are nonnegative and sum to one. Draw \(K\in\{0,1,N\}\) with those weights, then choose a uniformly random \(K\)-subset of \([N]\) as the one-positions. The resulting law is exchangeable. Its triple probabilities are respectively \(w_N=A\), \(w_1/N=B\) for each singleton one, and \(w_0+(N-3)w_1/N=C\) for all zero. No other pattern occurs, so it extends the prescribed triangle law. Conditional uniformity and the forced weights prove uniqueness for every permissible \(N\), including the integer boundary. For \(N\) above the stated ceiling, \(w_0<0\), proving impossibility. Because the ceiling is finite for every finite admissible parameter pair, no infinite triangle extension exists.

## Verification
The standalone standard-library Python 3 program `check.py`, embedded with this result, enumerates all set partitions through six labels and verifies their Ewens–Pitman probabilities for eleven exact-rational parameter pairs (including admissible negative \(\theta\)). It separately checks all eight triangle patterns, adjacent and disjoint edge-pair moments, every extension weight through two lengths beyond the predicted threshold, and the claimed graph shapes for every simple graph through five vertices. It reports **2,063 exact finite checks passed**. These computations are consistency checks, not the proof for infinitely many graphs, real parameters, or extension lengths; those conclusions follow from Steps 1–5.

## Relationship to prior work
Pitman (1995, Proposition 9) supplies the two-parameter exchangeable partition law and its consistency; the calculation of three- and four-label probabilities here uses that established law. Gnedin and Pitman (2006) construct an Ewens fragmentation with the one-parameter partition law as a special case. Konstantopoulos and Yuan (2015) establish general finite-exchangeability extension criteria. The elementary star-or-triangle structure of pairwise-intersecting edges is also familiar in line-graph theory. The result asserted here is the combined exact classification of which **fixed graph edge co-clustering indicators** are coordinate-exchangeable under the two-parameter partition law, the infinite-versus-finite dichotomy, and the explicit sharp parameter-dependent triangular extension ceiling. It is not a theorem about exchangeability of graph arrivals, random edges sampled in order, or the uniform measure over Bell set partitions.

## Limitations
This is restricted to unweighted simple graphs, binary same-block indicators, and \(0\le\alpha<1\), \(\theta>-\alpha\). It does not classify dependent multi-edge observables, directed/multigraph edges, or other random-partition families. Published work on general finite exchangeability could imply parts by specialization; the claim of historical priority remains qualified, especially for older literature not exhaustively searchable. The first-public-date field identifies a day-verified preprint in the cited lineage (Gnedin–Pitman, 12 August 2006); Pitman's older foundational paper and a 1992 report predate it, but no day-verified earliest public release of the latter report was established. Independent verification has not occurred.

## References
1. Jim Pitman, “Exchangeable and partially exchangeable random partitions,” *Probability Theory and Related Fields* **102** (1995), 145–158, Proposition 9, https://doi.org/10.1007/BF01213386 ; accessible text: https://www.stat.berkeley.edu/~aldous/206-Exch/Papers/pitman95a.pdf .
2. Alexander Gnedin and Jim Pitman, “Poisson representation of a Ewens fragmentation process,” arXiv:math/0608307v1 (public 2006-08-12), https://arxiv.org/abs/math/0608307 .
3. Takis Konstantopoulos and Linglong Yuan, “On the extendibility of finitely exchangeable probability measures,” arXiv:1501.06188v1 (public 2015-01-25), https://arxiv.org/abs/1501.06188 .
