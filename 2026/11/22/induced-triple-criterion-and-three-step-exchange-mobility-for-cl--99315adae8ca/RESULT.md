# The complete failure boundary for power domination on the Clebsch graph

## Finding

Let \(C\) be the sixteen-vertex, five-regular Clebsch graph. A sensor set \(S\) is **successful** if observation of its closed neighborhood \(N[S]\), followed by the unique-unobserved-neighbor forcing rule, observes every vertex.

The inclusion-maximal unsuccessful placements are exactly the sixty four-vertex sets inducing two disjoint edges \(2K_2\). Each unsuccessful three-set belongs to **exactly one** of them. In particular, a sensor set of arbitrary size succeeds exactly when it contains an independent triple or an induced three-vertex path. The complete successful-placement polynomial is
\[
\sum_{S\text{ successful}} z^{|S|}
=(1+z)^{16}-1-16z-120z^2-240z^3-60z^4.
\]
Every successful placement finishes at initial neighborhood observation or in one subsequent simultaneous forcing wave.

## Assumptions and scope

Label the graph by \(0,1,\ldots,15\), with adjacency when two labels have bitwise XOR in \(D=\{1,2,4,8,15\}\). Equivalently, take the five-dimensional cube and identify opposite vertices. An antipodal class has a unique representative which is a subset of the five coordinate directions of size at most two, and two distinct representatives are adjacent when their symmetric difference has size one or four. Placements are unordered subsets of the labelled vertex set. Initial observation is not counted as a forcing wave.

## Proof

The forcing process is monotone, wave by wave, in its initially observed set: if \(O\subseteq O'\) and \(x\notin O'\) is forced from \(O\), its observed forcer lies in \(O'\) and still has \(x\) as its unique unobserved neighbor. Thus taking a superset of a successful placement cannot increase its number of forcing waves, and taking a subset of an unsuccessful placement leaves it unsuccessful.

**The three-set input.** The graph is triangle-free. Translations and permutations of the five directions act transitively on triples of each of the three induced types. In the five-coordinate model translate the midpoint of a path to the empty set; the remaining two vertices are distinct singletons. For an independent triple translate one vertex to the empty set; the other two are intersecting two-subsets. For a single-edge triple translate an endpoint to the empty set; the other vertices are a singleton and a two-subset not containing it. This gives representatives \(\{0,1,2\}\), \(\{0,3,5\}\), and \(\{0,1,6\}\), respectively. The following checks use the XOR adjacency rule:

| Placement | Initially unobserved | Forces or obstruction |
|---|---|---|
| \(\{0,1,2\}\) | \(\{7,11,12\}\) | \(5\to7,\ 9\to11,\ 13\to12\) |
| \(\{0,3,5\}\) | \(\{6,9,14\}\) | \(2\to6,\ 8\to9,\ 10\to14\) |
| \(\{0,1,6\}\) | \(\{10,11,12,13\}\) | Each observed vertex has zero or two unobserved neighbors. |

In particular the unsuccessful triples are the triples with exactly one edge. The three-set criterion and these initial blind spots also appear in [1].

**Unique extension and stalling.** By symmetry a given edge can be taken to have representatives \(\varnothing,\{i\}\). The six vertices adjacent to neither endpoint, excluding the endpoints, are the two-subsets of the other four directions. Two such vertices are adjacent precisely when they are disjoint two-subsets, so their induced graph is a matching of three complementary pairs. For a single-edge triple its isolated vertex lies in this matching; it must be paired with its unique matching partner in any induced \(2K_2\) containing the triple. For the representative \(\{0,1,6\}\) the extension is \(\{0,1,6,7\}\). Adding \(7\) does not change the initially observed set: \(N[7]=\{3,5,6,7,8,15\}\) is disjoint from \(\{10,11,12,13\}\). Hence the extension is stalled. By the triple symmetry and uniqueness, every induced \(2K_2\) is stalled. There are \(40\) choices of an edge and three matching partners for it at the level of disjoint edges; each induced \(2K_2\) is counted twice, so there are \(40\cdot3/2=60\) such sets.

**Exhaustion and polynomial.** Every pair extends to a failed triple: for an adjacent pair add one of its six common nonneighbors; for a nonadjacent pair, translate to \(\varnothing,\{i,j\}\) and add a singleton from outside \(\{i,j\}\). Thus all placements of size at most two are subsets of stalled \(2K_2\)'s. If a four-set contains no successful triple, every triple has exactly one edge. Counting edges in its four triples gives two edges in the four-set itself. They cannot meet, since then their three vertices would induce a path. If a five-set contained no successful triple, counting the edge incidences in its ten triples would give \(3e=10\), impossible. Every larger set therefore contains a successful triple as well. This proves the classification and, by wave monotonicity, the one-wave bound. The unsuccessful counts at sizes \(0,1,2\) are \(1,16,120\). At size three there are \(40\cdot6=240\) single-edge triples, and at size four there are sixty failures. Subtracting these coefficients from the all-placement polynomial gives the formula.

## Verification and limitations

The argument is self-contained. The accompanying `verify_python.py` and `verify_cpp.cpp` also give exhaustive finite checks of all \(2^{16}\) placements. For this result the relevant checks are the failed counts by size, the sixty induced \(2K_2\)'s, unique extensions of the 240 failed triples, and the one-wave success bound. The conclusion is specific to the five-regular Clebsch graph; it is not a classification for other folded cubes or for the complementary ten-regular graph.

## Related work

[1] *Blind-spot antipodes and the sharp relocation gap of the five-regular Clebsch graph*, Resultary, 2026-11-22. [Result](https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-blind-spot-antipodes-and-the-sharp-relocation-gap-of-the-five-re--142d52a30ab7/RESULT.md). Its minimum-placement classification and one-wave check for triples overlap with the three-set input above. The theorem here concerns maximal failures and the full placement polynomial, not the reconfiguration of minimum placements.

[2] T. W. Haynes, S. M. Hedetniemi, S. T. Hedetniemi and M. A. Henning, *Domination in Graphs Applied to Electric Power Networks*, SIAM J. Discrete Math. **15** (2002), 519–529. [DOI](https://doi.org/10.1137/S0895480100375831).

[3] N. Dean, A. Ilic, I. Ramirez, J. Shen and K. Tian, *On the Power Dominating Sets of Hypercubes*, IEEE CSE (2011), 488–491. [DOI](https://doi.org/10.1109/CSE.2011.211). This concerns ordinary hypercubes, rather than the antipodal quotient used here.
