# Unique antipodes in the nine-symbol derangement switch graph

## Finding
Let \(\mathcal D_9\) be the graph on permutations \(\pi\) of \(\{1,\ldots,9\}\) having no fixed points, where one move exchanges two entries while maintaining the absence of fixed points. Then \(\mathcal D_9\) has exactly \(133496\) vertices and \(1835568\) edges; it is connected, with radius \(8\) and diameter \(10\).

The pairs at distance \(10\) are **exactly**
\[
\{\pi,\pi^{-1}\},\qquad\text{where the cycle type of }\pi\text{ is }(3,3,3).
\]
There are exactly \(1120\) such unordered pairs. Every other pair is at distance at most \(9\). The full eccentricity classification by cycle type is below; each listed cycle type forms one conjugacy orbit.

| Cycle type | Number of vertices | Vertex degree | Eccentricity |
|:--|--:|--:|--:|
| \((2,2,2,3)\) | 2520 | 30 | 9 |
| \((2,2,5)\) | 9072 | 29 | 8 |
| \((2,3,4)\) | 15120 | 28 | 9 |
| \((2,7)\) | 25920 | 28 | 8 |
| \((3,3,3)\) | 2240 | 27 | 10 |
| \((3,6)\) | 20160 | 27 | 9 |
| \((4,5)\) | 18144 | 27 | 8 |
| \((9)\) | 40320 | 27 | 8 |

Consequently, exactly \(93456\), \(37800\), and \(2240\) configurations have eccentricity \(8\), \(9\), and \(10\), respectively.

## Assumptions and scope
The underlying labels are individually named: \([9]=\{1,\ldots,9\}\). A state is a bijection \(\pi:[9]\to[9]\) satisfying \(\pi(i)\ne i\) for every \(i\). For distinct positions \(a,b\), the switched state \(\sigma\) has \(\sigma(a)=\pi(b)\), \(\sigma(b)=\pi(a)\), and \(\sigma(i)=\pi(i)\) elsewhere. The move is legal if and only if \(\pi(b)\ne a\) and \(\pi(a)\ne b\). The graph is simple and undirected; neither an illegal intermediate state nor a different move rule is allowed.

Equivalently, states are perfect matchings of the crown graph \(K_{9,9}-M\), where \(M\) is the removed diagonal matching. One move replaces the occupied opposite edges of a \(4\)-cycle by the other two edges. This is the bipartite perfect-matching switch operation.

## Proof
**Exhaustive vertex and edge construction.** Every labelled permutation is visited exactly once by the lexicographic permutation generator. The fixed-point test retains exactly the \(133496\) derangements, agreeing with the subfactorial inclusion-exclusion formula \(9!\sum_{j=0}^{9}(-1)^j/j!\). For each retained permutation, all \(\binom 92=36\) unordered position pairs are examined. The condition stated above is both necessary and sufficient to keep the switched permutation a derangement; hence every legal edge, and no illegal edge, is constructed. The recorded total degree is \(3671136\), giving \(1835568\) undirected edges. Symmetry of every edge is checked explicitly.

**Orbit reduction.** Simultaneously relabelling positions and values transforms \(\pi\) to \(\tau\pi\tau^{-1}\). It preserves fixed points and maps a legal position swap to a legal position swap. Thus it is a graph automorphism. Conjugacy classes of permutations are classified by their cycle lengths. For derangements of nine symbols the eight classes listed above are exhaustive. In particular, all vertices in any one row have the same eccentricity and the same number of vertices at each possible distance.

**Complete shortest-path certificate.** For one lexicographically selected representative of each of the eight classes, breadth-first search traverses *all* \(133496\) vertices and assigns their exact distances. Each graph edge is examined by standard queue expansion, which inductively proves that the first assigned distance is the minimal number of legal switches. The resulting eccentricities are the eight table entries above, proving the asserted radius and diameter without extrapolation to larger orders.

For the representative of type \((3,3,3)\), the breadth-first-search shell counts at distances \(0,1,\ldots,10\) are
\[
(1,27,324,2259,9777,26442,43059,37899,13590,117,1).
\]
Its unique distance-\(10\) vertex is explicitly checked to be its inverse. The equivariance above carries the uniqueness and inverse identification to **every** type-\((3,3,3)\) vertex. No other type has eccentricity \(10\). There are \(2240\) type-\((3,3,3)\) vertices and none equals its own inverse, so the number of distinct unordered diameter pairs is \(2240/2=1120\).

For an explicit upper-bound witness, the following eleven one-line permutations form a legal ten-switch path from \((1\ 2\ 3)(4\ 5\ 6)(7\ 8\ 9)\) to its inverse, reading each line as the sequence of nine images:

```text
231564897
531264897
351264897
851264397
751264398
951264378
351264978
315264978
314265978
316245978
312645978
```

Each consecutive pair differs by one exchange of positions and every line is fixed-point-free. The exhaustive search proves that this path cannot be shortened.

As a supplementary count check, if \(c_2(\pi)\) is the number of two-cycles of \(\pi\), the valency is \(\deg(\pi)=\binom92-9+c_2(\pi)=27+c_2(\pi)\): the \(9\) directed assignments \(i\mapsto\pi(i)\) forbid position swaps, with a two-cycle duplicating one forbidden unordered pair. This degree relation is a previously studied kind of local invariant, and is not asserted as the principal novelty.

## Verification
Two standalone programs are included. `verify_crown_switch.cpp` compiles with `c++ -O3 -std=c++17 verify_crown_switch.cpp -o verify_crown_switch` and runs as `./verify_crown_switch`. It explicitly indexes every derangement, verifies bidirectional adjacencies and the exact graph size, then computes all eight breadth-first-search distance distributions.

`verify_crown_switch_independent.py` runs as `python3 verify_crown_switch_independent.py`. Independently of permutation-array iteration and edge indexing, it recursively builds all perfect matchings while forbidding diagonal edges; it then generates neighbours directly as tuples and explores the state space independently from one representative of each conjugacy class. Its visited sets equal the entire generated state set. The two programs agree on every eccentricity and distance-shell profile, including the unique inverse antipode and the absence of any other diameter pairs. Both were executed successfully from the embedded source contents.

## Relationship to prior work
Dyer, Jerrum and Müller introduced and analyzed the general bipartite perfect-matching switch chain (public preprint dated January 30, 2015); their chordal-bipartite upper bound does **not** apply to the nine-crown graph, which contains induced six-cycles. Jain's *Transpositions in Derangements* (public September 2021 preprint) studies exactly this derangement transposition graph and establishes its connectivity, extremal degrees, shortest spanning-walk length and vertex-connectivity bounds. **None of those facts is claimed here as new.** The present exact distance and antipode classification is not supplied by those theorems.

The 133496 state count is classical and appears in OEIS A000166. The standard *derangement graph* used in the Erdős–Ko–Rado literature has all permutations as vertices and an edge when relative displacement is fixed-point-free; it is **not** the graph studied here. Searches of mathematical literature and public research records did not locate an equivalent finite nine-symbol metric classification. Such search results cannot prove priority. One potentially relevant 2026 journal title, *Some Results on the Graph of Derangements*, was accessible only at bibliographic level and remains a residual comparison risk.

## Limitations
The theorem concerns exactly nine named symbols and legal exchanges of two arbitrary positions. It proves nothing about the diameter for all \(n\), adjacent-position-only exchanges, or the mixing time of a random walk. The shortest-path certificate is finite and is established by complete traversal, not by a claimed closed-form geodesic formula. Historical priority is qualified because an equivalent unindexed computation could exist and the 2026 bibliographic-only source could not be compared at full-text level. No independent scholarly audit has been performed.

## References
1. M. Dyer, M. Jerrum and H. Müller, *On the switch Markov chain for perfect matchings*, arXiv:1501.07725, first posted January 30, 2015. https://arxiv.org/abs/1501.07725
2. P. Jain, *Transpositions in Derangements*, September 2021 public preprint, DOI:10.13140/RG.2.2.35817.42088. https://www.researchgate.net/publication/354533290_Transpositions_in_Derangements
3. OEIS Foundation, A000166, *Subfactorial or rencontres numbers, or derangements*. https://oeis.org/A000166
4. Y.-P. Deng and X.-D. Zhang, *Automorphism Group of the Derangement Graph*, Electronic Journal of Combinatorics 18 (2011), P198. https://doi.org/10.37236/685
