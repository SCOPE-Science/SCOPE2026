# Factorial geodesic multiplicity for antipodal crown-graph metric bases

## Finding
Let \(n\ge3\) be an integer. The connected *crown graph* \(H_n=K_{n,n}-M_n\) has vertices \(a_0,\ldots,a_{n-1},b_0,\ldots,b_{n-1}\), with \(a_i b_j\) an edge exactly when \(i\ne j\). Write \(X=\{a_1,\ldots,a_{n-1}\}\) and \(Y=\{b_1,\ldots,b_{n-1}\}\).

For either (i) the ordinary vertex-metric basis reconfiguration graph or (ii) the edge-metric basis reconfiguration graph, with each move sliding one chosen landmark along one edge while preserving minimum resolving-set size and validity, the number of *distinct shortest* \(X\)-to-\(Y\) slide sequences is
\[
\boxed{G_n=(n-1)!\binom{n}{3},\qquad n\ge3.}
\]
Every sequence counted has exactly \(n+3\) moves. The formula refines the previously known sharp distance by specifying all optimal relocation schedules between natural opposed placements. Each vertex and matched-pair index is labelled; no quotient by graph automorphisms is taken.

## Assumptions and scope
All graphs are finite, simple, undirected and unweighted. A vertex-metric resolving set distinguishes every pair of vertices by their vectors of graph distances to landmarks. An edge-metric resolving set instead distinguishes edges using \(d(v,xy)=\min\{d(v,x),d(v,y)\}\). A *basis* is a minimum-cardinality resolving set for the chosen metric. In either reconfiguration graph, a slide replaces a chosen landmark by an unchosen adjacent vertex and must leave a valid basis. A geodesic means a shortest path of labelled configurations in this reconfiguration graph, not a shortest path of the original crown graph. Index \(0\) denotes the common vacant matched pair and is not a free global vertex. The theorem concerns the specified pair \(X,Y\) for every \(n\ge3\), not the complete all-pairs distribution.

## Proof
**1. The common configuration family.** In \(H_n\), distinct same-shore vertices are at distance \(2\), an adjacent opposite-shore pair is at distance \(1\), and a deleted matching pair \(a_i,b_i\) is at distance \(3\). If two distinct matched indices \(i,j\) both contain no selected landmark, then \(a_i,a_j\) have the same distance to all selected landmarks, so any vertex-resolving set meets at least \(n-1\) matched pairs. Conversely, one chosen vertex at each matched index except one resolves all vertices: the coordinate at a chosen endpoint of a pair distinguishes that pair's two endpoints and distinguishes its endpoints from all other indices. Thus the vertex-metric bases are exactly these \(n2^{n-1}\) configurations.

For edge resolution the same exact family holds. Indeed, write \(e_{ij}=a_ib_j\) for \(i\ne j\). Then for a vertex at index \(k\), the edge-distance is \(0\) or \(2\) if \(k\in\{i,j\}\), depending on side, and \(1\) otherwise. If two indices \(i,j\) are omitted, the edges \(e_{it}\) and \(e_{jt}\), with \(t\) distinct from both, cannot be distinguished. Any transversal omitting one index, on the other hand, detects the endpoints of every edge by the zero/two coordinates, except that a shared omitted index is reconstructed from the other detected endpoint. This proves the same basis family for edges. The full equivalent edge-basis classification is independently established in the referenced literature.

**2. State and move rule.** Encode a basis by a vacant index \(h\) and a side bit at each other index: \(0\) for \(a_i\) and \(1\) for \(b_i\). A slide must take the landmark from some occupied index \(j\ne h\), place it at index \(h\) on the *opposite* side, and leave vacancy \(j\). Every such operation is a legal edge slide. Thus each slide changes the total number \(q\) of selected \(b\)-vertices by \(+1\) or \(-1\).

Put \(m=n-1\). Initially \(q=0\) and finally \(q=m\). If a route contains \(d\) decreasing slides and \(u\) increasing slides then \(u-d=m\), so its length is \(m+2d\).

**3. Two decreases are unavoidable, and their positions are forced on a shortest route.** The first move into the initially empty index \(0\) installs a \(b_0\)-landmark. The final move must *remove* an \(a_0\)-landmark to make index \(0\) empty while depositing a \(b\)-landmark at its destination. Therefore at some time a slide must remove \(b_0\) (a decreasing move), and a different slide must deposit \(a_0\) from a \(b\)-landmark (another decreasing move). Hence \(d\ge2\), yielding length at least \(m+4=n+3\).

If a route has exactly two decreasing moves, these two moves are precisely the removal of the initial \(b_0\) and the later deposit of \(a_0\). Before the first decrease all moves increase \(q\), so the vacancy visits a sequence of distinct initially occupied indices, then returns to index \(0\) by moving \(b_0\). Immediately thereafter, the second decrease must deposit \(a_0\) by taking a \(b\)-landmark from one of the previously visited indices. An intervening increasing slide from the empty index \(0\) would reinstall \(b_0\), requiring a third decrease to remove it; an intervening decreasing slide elsewhere would already exhaust the available decreases. Following the second decrease, every move increases \(q\); each as-yet-unchanged \(a\)-landmark must be used exactly once, and the last move takes \(a_0\) into the final vacancy. These conditions force all geodesic itineraries.

**4. Exact enumeration and realization.** Let \(t\) be the number of \(b\)-landmarks at occupied indices after the *first* decreasing move. Necessarily \(1\le t\le m-1\). The vacancy has first travelled from index \(0\) through \(t+1\) distinct occupied indices and then returned to index \(0\), making exactly \(t\) of the occupied indices hold \(b\)-landmarks. The ordered first excursion has
\[
(m)_{t+1}=\frac{m!}{(m-t-1)!}
\]
possibilities. For the second decrease choose which of the \(t\) newly created \(b\)-landmarks to move into index \(0\): exactly \(t\) choices. The resulting vacant index previously held that \(b\)-landmark. The \(m-t\) other occupied indices still holding \(a\)-landmarks (including the index reached in the first decrease) must subsequently be visited in any order: \((m-t)!\) choices, followed by the forced final move from index \(0\). Each choice gives a different legal slide sequence of length
\[
(t+1)+1+1+(m-t)+1=m+4,
\]
so it is shortest by step 3. Conversely step 3 shows that *every* shortest sequence occurs uniquely in this enumeration.

The number of shortest routes at fixed \(t\) is
\[
\frac{m!}{(m-t-1)!}\;t\;(m-t)!=m!\,t(m-t).
\]
Summing the full admissible range gives
\[
G_n=m!\sum_{t=1}^{m-1}t(m-t)
  =m!\frac{m(m-1)(m+1)}6
  =(n-1)!\binom n3.
\]
All arguments use the common basis family and move rule, and therefore apply equally to ordinary vertex and edge metric resolution. \(\square\)

## Verification
The standalone file `artifacts/verify_original.py` constructs original crown-graph edges, determines graph distances, exhaustively checks all vertex and edge resolving sets of sizes below the claimed minimum, classifies every minimum basis, and performs ordinary breadth-first geodesic counting on the *actual* slide graph for every \(3\le n\le7\). For these five orders the resulting shortest-route counts are \(2,24,240,2400,25200\), agreeing with the formula.

Separately, `artifacts/verify_quotient.py` uses orbit-state weighted transitions for the number of occupied \(b\)-landmarks, with or without index \(0\) vacant. This checker has only \(3n-2\) quotient states; it reproduces both the exact shortest length and count for every \(3\le n\le100\). The logged outputs are in `artifacts/verification_output.txt`. The all-parameter proof above, rather than any finite execution, establishes the infinite statement.

## Relationship to prior work
The published mathematical record *Sharp token-slide diameter of crown-graph metric bases* proves that these vertex-metric bases form a connected slide graph of diameter \(n+3\), and explicitly excludes a description of all shortest routes or distance multiplicities from its scope. The present exact factorial geodesic formula is not a corollary of that diameter statement; it uses the necessary and sufficient two-decrease itinerary classification.

The published record *Edge metric bases of crown graphs* proves the underlying edge-resolving basis classification, but not a route count. The record on crown-graph zero-forcing exchange distances studies another optimization predicate and unrestricted token replacement, so it does not imply this claim. Yi's study of fractional edge metric dimension establishes foundational edge-resolution terminology but does not, in its inspected abstract, assert shortest-route multiplicities. Neither the existing basis counts nor the known relocation distance determines how many optimal transformation schedules exist. Targeted semantic searches by graph aliases, vacancies, flipped binary signs, geodesics, and shortest-route counting found no matching claim; this is not by itself a proof of priority.

## Limitations
This theorem counts geodesics only between the two explicitly specified opposite-side configurations sharing a vacant pair; it does not give the complete all-pairs distance enumerator or counts for arbitrary endpoints. Published priority is provisional; a 2026 thesis on metric-basis reconfiguration and other unindexed mathematical sources remain incompletely inspected. Independent external mathematical validation has not been performed.

## References
1. E. Yi, *On the edge dimension and fractional edge dimension of graphs*, arXiv:2103.07375v1, first public 2021-03-12, https://arxiv.org/abs/2103.07375.
2. *Sharp token-slide diameter of crown-graph metric bases*, published mathematical research record (2026), identifier `f346d16bc708` (full result text examined).
3. *Edge metric bases of crown graphs*, published mathematical research record (2026), identifier `b5b3c45f23e8` (full result text examined).
4. A. Kelenc, N. Tratnik and I. G. Yero, *Uniquely identifying the edges of a graph: the edge metric dimension*, arXiv:1602.00291, 2016, https://arxiv.org/abs/1602.00291.
