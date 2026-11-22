# Exact directed-distance profiles of the first fifteen accelerated Kolakoski Schreier graphs

## Finding
For the finite accelerated Schreier graphs \(\Gamma'_n\) associated with the full Kolakoski shift in Mitchell--Walton--Whittaker (2026), the **entire directed ordered-pair distance distribution**, outward eccentricity distribution, radius, and diameter have been determined exactly for **every** integer \(1\le n\le15\). The graphs range from two through 32,768 vertices. In particular, for each integer \(9\le n\le15\), their unweighted **directed diameter** is **exactly** \(n+4\). At level 15 the radius is 18, diameter is 19, and there are exactly 17,136 ordered pairs at directed distance 19.

The summary table below reports all levels. The companion `census.tsv` records the exact count for every ordered-pair distance at every level, not merely the farthest pairs.

| Level | Vertices | Radius | Diameter | Outward eccentricity multiplicities | Ordered diametral pairs |
|---:|---:|---:|---:|:---|---:|
| 1 | 2 | 1 | 1 | 1:2 | 2 |
| 2 | 4 | 2 | 2 | 2:4 | 4 |
| 3 | 8 | 3 | 3 | 3:8 | 16 |
| 4 | 16 | 4 | 5 | 4:8,5:8 | 8 |
| 5 | 32 | 6 | 7 | 6:16,7:16 | 16 |
| 6 | 64 | 7 | 8 | 7:8,8:56 | 96 |
| 7 | 128 | 9 | 10 | 9:96,10:32 | 32 |
| 8 | 256 | 10 | 11 | 10:200,11:56 | 64 |
| 9 | 512 | 11 | 13 | 11:192,12:304,13:16 | 16 |
| 10 | 1024 | 12 | 14 | 12:56,13:936,14:32 | 32 |
| 11 | 2048 | 14 | 15 | 14:1856,15:192 | 224 |
| 12 | 4096 | 15 | 16 | 15:3640,16:456 | 480 |
| 13 | 8192 | 16 | 17 | 16:6464,17:1728 | 1992 |
| 14 | 16384 | 17 | 18 | 17:12088,18:4296 | 5088 |
| 15 | 32768 | 18 | 19 | 18:19720,19:13048 | 17136 |

## Assumptions and scope
A vertex of \(\Gamma'_n\) is a binary word of length \(n\), equivalently a directive word over the two Kolakoski symbols, in the right-to-left ordering of the cited paper. Each vertex has one outgoing edge of type 1 and one outgoing edge of type 2; distinct edge types may share an endpoint. The edges are **accelerated edges**, each assigned weight one regardless of the length of the original substitution word carried by its label. All distances here count **directed accelerated edges**. They are not minimum elapsed shift times for the original Kolakoski system, and are not distances in the unaccelerated labeled graph.

Index vertices by integers \(0,\ldots,2^n-1\), with the added outer binary digit determining the two consecutive blocks at level \(n+1\). Let \(p_n(i)\) and \(q_n(i)\) be the heads of the type-1 and type-2 edges leaving vertex \(i\). At level one both maps interchange the two vertices. For \(m=2^n\) and \(0\le i<m\), Corollary 4.8 of the cited paper gives the following exact recursion after forgetting edge labels:

\[
\begin{aligned}
p_{n+1}(i)&=m+q_n(i), &p_{n+1}(m+i)&=p_n(i),\\
q_{n+1}(i)&=m+q_n(q_n(i)), &q_{n+1}(m+i)&=p_n(p_n(i)).
\end{aligned}
\]

The graph distance \(d_n(s,t)\) is the least number of successive directed type-1/type-2 edges taking \(s\) to \(t\). The outward eccentricity of \(s\) is \(\max_t d_n(s,t)\), the radius is the minimum of these eccentricities, and the diameter is their maximum. We count all **ordered** source-target pairs, including equal pairs at distance zero.

## Proof
**Finite graph identification.** The base permutations and the two block recursions are precisely the adjacency-matrix case of the cited Corollary 4.8: the matrices are permutation matrices with a unique outgoing edge of each type. Thus the algorithm in `forward_census.cpp` constructs exactly the level-\(n\) graph, not a sampled approximation, for every stated level. The recursion uses only integer array assignments and permutations, so there are no floating-point uncertainties or numerical thresholds.

**Shortest-path completeness.** For each level and **every** starting vertex, the checker performs a breadth-first search using both outgoing edges at each vertex. Breadth-first search in a finite directed unit-edge graph discovers each reachable target at the exact shortest directed distance. The code asserts that all \(2^n\) vertices have been visited for each source. It then increments the unique distance bucket for every source-target pair, records each source's outward eccentricity, and calculates the minimum and maximum eccentricities. Thus the total number of counted ordered pairs is exactly \(2^{2n}\), not a Monte-Carlo estimate. The exhaustive program evaluates all \(2^{2n}\) pairs at each of the fifteen levels and provides the table and accompanying complete distance histograms.

**Near-Moore comparison.** A directed graph of outdegree at most two contains at most \(1+2+\cdots+2^{d}=2^{d+1}-1\) vertices within directed distance \(d\) of a chosen source. Consequently, every strongly connected such graph on \(2^n\) vertices has diameter at least \(n\). The exhaustive upper and lower evaluations in the table therefore certify a modest additive diameter excess, with the exact value \(4\) at each of levels 9 through 15. This conclusion is **finite**, not an unproved all-level extrapolation.

## Verification
Compile `forward_census.cpp` with a standard C++17 compiler using `g++ -O3 -std=c++17 forward_census.cpp -o forward`, then execute `./forward 15`; its output must exactly match the 15 rows in the companion `census.tsv`. Compile `reverse_census.cpp` similarly and run `./reverse 15`. This program builds the two permutations using a separate implementation, reverses their arrows and performs complete BFS toward every target; it independently checks all fifteen diameters and all fifteen diametral-pair counts, as reported in `reverse_checks.txt`. Run `python3 verify_small.py` to construct tuple-labeled vertices independently and recover radius, diameter and diametral-pair count for every level 1 through 9.

Every output histogram is also tested for the identities that its distance buckets total \(2^{2n}\), that its eccentricity multiplicities total \(2^n\), and that its zero-distance bucket equals \(2^n\). The exhaustive algorithms terminate at the fixed upper bound 15; there is no claim of an infinite general formula or computational certification outside this range.

## Relationship to prior work
Mitchell, Walton and Whittaker (arXiv:2611.06878v1, first public 4 November 2026) introduced these accelerated Schreier graphs, proved the precise block recurrence (Corollary 4.8), and established strong connectivity at all levels (Theorem 5.3). Those structural facts are credited, **not claimed as new**. Their article does not evaluate the level-by-level directed diameters, complete pair-distance histograms, eccentricity multiplicities, or the seven-level equality stated here. MacAulay (arXiv:2605.14234v1) studies related Kolakoski permutation automata and their transformation groups; its exact tables concern group orders through twelve levels and cycle properties of group elements, not shortest directed paths between every pair of states. Earlier finite-depth shift periodic-orbit counts measure least shift periods, not these accelerated-graph distances.

## Limitations
The new content is a finite, exact quantitative classification for levels 1 through 15, plus the elementary comparison with the two-outdegree Moore bound. It does **not** prove eventual stabilization of the diameter excess at four, nor any universal diameter bound for higher levels. The edges are measured in accelerated steps, not original symbolic shift time. A specialized historical shortest-path calculation not indexed by the searched sources may exist; no global historical priority guarantee is asserted.

## References
1. A. C. Mitchell, J. J. Walton, M. F. Whittaker, *The full Kolakoski shift is topologically transitive*, arXiv:2611.06878v1, first public 4 November 2026, especially Corollary 4.8 and Theorem 5.3. https://arxiv.org/abs/2611.06878
2. N. MacAulay, *Group Theory of the Kolakoski Sequence*, arXiv:2605.14234v1, first public 14 May 2026. https://arxiv.org/abs/2605.14234
