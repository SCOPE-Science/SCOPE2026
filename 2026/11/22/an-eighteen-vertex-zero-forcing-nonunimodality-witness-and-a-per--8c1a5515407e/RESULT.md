# An eighteen-vertex zero-forcing nonunimodality witness and a persistent twin-expansion family

## Finding

There is a connected simple graph of order **18** with a nonunimodal ordinary zero forcing polynomial. More strongly, a one-block clique-twin extension produces a connected counterexample at every order \(n\ge18\). The explicit family satisfies
\[
z(G_t;n-5)=690+68t,\qquad z(G_t;n-4)=678+64t,\qquad z(G_t;n-3)=680+112t,
\]
where \(t\) is any integer with \(t\ge0\), \(n=18+t\), and \(z(G;k)\) is the number of ordinary zero forcing sets of size \(k\). Thus the middle coefficient is strictly below *both* neighbors: the left gap is \(12+4t\) and the right gap is \(2+48t\).

At \(t=0\) the entire polynomial is
\[
\mathcal Z(G_0;x)=58x^{11}+345x^{12}+690x^{13}+678x^{14}+680x^{15}+146x^{16}+18x^{17}+x^{18}.
\]
The base graph has 18 vertices and 105 edges.

## Assumptions and scope

All graphs are finite, undirected, simple and labelled. An ordinary zero forcing process initially colours a vertex subset blue, then repeatedly colours a white vertex blue whenever it is the unique white neighbor of some blue vertex. A zero forcing set is an initial blue set from which all vertices can eventually be coloured blue. The polynomial counts such initial sets according to size. Unimodality refers to the coefficient sequence in increasing degree, including initial zeroes.

The graph is fully specified by 12 indexed vertex blocks \(B_0,\ldots,B_{11}\). Their sizes are
\[
(|B_0|,\ldots,|B_{11}|)=(1,1,1,2+t,1,1,1,1,2,3,2,2).
\]
The quotient has the following **decimal** adjacency bit masks in index order:

`3721, 3628, 3646, 511, 3708, 3550, 3768, 3817, 3624, 2007, 3063, 3575`.

For \(i\ne j\), every vertex of \(B_i\) is adjacent to every vertex of \(B_j\) exactly when bit \(j\) of mask \(i\) is set. Within a block, all distinct vertices are adjacent iff its own mask's diagonal bit is set. A diagonal bit never creates loops. The quotient masks are symmetric off diagonal; the definition gives a valid simple graph for every \(t\ge0\). The case \(t=0\) is called \(G_0\).

## Proof

**Twin reduction.** All vertices within any one block are twins (they have identical neighbors outside each pair). Any two such vertices form a fort. Indeed, if both begin white then no blue vertex can see exactly one of them, and neither can ever be the first of that pair to be forced. Consequently, the complement of any zero forcing set has at most one white vertex per block. A missing-vertex choice is therefore given by a subset \(W\subseteq\{0,\dots,11}\), and a selection of one concrete vertex in each indicated block. The number of selections is \(\prod_{i\in W} |B_i|\).

**Quotient forcing equivalence.** In a configuration with at most one white vertex per block, a blue vertex in block \(j\) exists precisely when \(|B_j|-\mathbf1_{j\in W}>0\). If it exists, it sees exactly one white neighbor precisely when the bit mask of its block has exactly one common bit with the current mask of \(W\). The unique common bit identifies the vertex to force, so removing this bit gives exactly the full-graph force. Conversely, every full-graph force removes a bit in this way. One can greedily apply any available force; when none remains, the remaining white set is a fort and no forcing sequence can succeed. Therefore testing this quotient algorithm for each of the \(2^{12}\) block masks is an *exact exhaustive* characterization, not an experimental approximation.

**Uniform dependence on the expanded block.** The size of block \(B_3\) is at least two for all \(t\ge0\). Therefore the existence of a blue representative in that block, for every permitted white mask, is independent of \(t\). All other block sizes are fixed, and the quotient forcing algorithm has the same outcome for every \(t\). For any successful mask not containing index 3, its multiplicity is constant; for a successful mask containing index 3, the multiplicity is its multiplicity at \(t=0\) multiplied by \((2+t)/2\). Hence, for each fixed number of missing vertices, the exact count is affine in \(t\), and its slope is the sum of the multiplicities of successful masks containing block 3 after removing its factor 2.

Exhausting all block masks with precisely \(3,4,5\) missing blocks produces:

| Missing-block count | Successful masks | Multiplicity at \(t=0\) | Coefficient of \(t\) |
|---|---:|---:|---:|
| 3 | 214 | 680 | 112 |
| 4 | 247 | 678 | 64 |
| 5 | 214 | 690 | 68 |

The included `quotient_check.py` is the standalone exact integer enumeration and prints these four columns. The three coefficient formulas follow by substituting the number of blue vertices \(n-|W|\). The inequalities
\[
(690+68t)-(678+64t)=12+4t>0,
\]
\[
(680+112t)-(678+64t)=2+48t>0
\]
hold for every \(t\ge0\). Thus no coefficient mode can make the polynomial unimodal. Connectedness of \(G_0\) follows from its given adjacency masks (independently checked by graph traversal); adding true twins preserves connectedness.

## Verification

`verify.cpp` expands the quotient to the **actual 18-vertex graph** and independently tests all \(2^{18}=262144\) white subsets using the ordinary blue-to-white forcing rule, without the quotient reduction. Its exact output gives the full polynomial and the coefficient valley. `quotient_check.py` independently checks all \(2^{12}=4096\) quotient white-block masks, their weighted counts and their affine slopes. Both computations were executed against the embedded source files. The explicit quotient proof above extends the three certified counts to all \(t\ge0\), rather than extrapolating from finite tests.

## Relationship to prior work

Newton and Brimkov (arXiv:2611.11352v1, first posted 2026-11-08 UTC) disproved general zero-forcing-polynomial unimodality and gave an infinite family with a displayed example of order 81/82; they explicitly asked for the smallest order. A subsequent independently published public computation dated 2026-11-11 reported a formal 20-vertex example and mentioned an unformalized 19-vertex example. Neither source provides or implies an order-18 witness or this family; their existence theorems at larger orders do not rule in the smaller object. The graph-size upper bound is therefore reduced to at most 18, subject to historical priority verification. No claim of the *exact smallest* order is made. The present family is also not claimed to be the first infinite family of nonunimodal examples.

## Limitations

There is no global classification of all nonunimodal graphs and no proof that 17 or fewer vertices are impossible. The 18-vertex example is dense (105 edges), and the construction does not establish special hereditary graph properties. Historical priority is provisional: databases and online literature may omit prior examples or certificates. The finite computation proves the base enumerator, while the all-order extension depends essentially on the proved twin reduction and stable quotient dynamics. Independent mathematical verification has not been performed.

## References

1. T. Newton and B. Brimkov, *Zero forcing is not unimodal*, arXiv:2611.11352v1, submitted 2026-11-08 UTC. https://arxiv.org/abs/2611.11352
2. *Existence of a Simple Graph of Order 20 with a Non-Unimodal Zero Forcing Polynomial*, AFTD public research note, 2026-11-11. https://rainwangphy.github.io/aftd-platform/blog/2026-11-11-op-1400/
3. K. Boyer et al., *The zero forcing polynomial of a graph*, Discrete Applied Mathematics 258 (2019), 35–48. https://doi.org/10.1016/j.dam.2018.11.033
