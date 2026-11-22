# The Fano-incidence NOR oscillator: a 37-symbol duality and exact 703-attractor basin census

## Finding

Consider the 14-vertex Heawood graph, the point-line incidence graph of the Fano plane, under simultaneous **open-neighborhood NOR** updates: a vertex is occupied at the next time if and only if none of its three neighbors is currently occupied. Among all \(2^{14}=16,384\) labelled configurations, there are exactly **37 fixed configurations and 666 primitive temporal two-cycle orbits**, and every trajectory is periodic after at most **one** update.

The **complete individual-attractor basin-size distributions** are as follows (size \(s\), number of attractors whose basin contains exactly \(s\) initial configurations):

| Period | Basin size \(s\) | Number of distinct attractors |
|---|---:|---:|
| 1 | 1 | 21 |
| 1 | 5 | 14 |
| 1 | 64 | 2 |
| 2 | 2 | 210 |
| 2 | 6 | 294 |
| 2 | 10 | 42 |
| 2 | 26 | 49 |
| 2 | 65 | 42 |
| 2 | 69 | 14 |
| 2 | 321 | 14 |
| 2 | 4097 | 1 |

The unique 4097-state basin belongs to the orbit alternating between the empty configuration and the fully occupied configuration. Exactly 219 initial configurations enter fixed points, and 16,165 enter two-cycles. The first-periodic-entry census, indexed by \((\text{entry time},\text{least period})\), is \((0,1):37\), \((0,2):1332\), \((1,1):182\), \((1,2):14833\). Of the 37 fixed configurations, 21 have **no transient predecessors**.

## Assumptions and scope

Number Fano points and lines by \(\mathbb Z/7\mathbb Z\). Let line \(j\) contain precisely points \(j,j+1,j+3\) (indices modulo seven). A configuration is a pair \((X,Y)\) of subsets of the seven points and seven lines. The map \(F\) uses **open** neighbors, with neither self-feedback nor stochastic tie-breaking. All vertices update synchronously. In particular the graph has no self-loops. A basin comprises every labelled configuration whose forward orbit eventually enters a specified temporal orbit, counting both phases of a primitive two-cycle as belonging to the same basin. Entry time means the earliest number of updates needed to reach a periodic configuration.

Define the two antitone maps
\[
\alpha(X)=\{j:\text{line }j\text{ is disjoint from }X\},\qquad
\beta(Y)=\{i:\text{point }i\text{ lies on no line of }Y\}.
\]
Then \(F(X,Y)=(\beta(Y),\alpha(X))\). A **closed point set** is one satisfying \(\beta\alpha(X)=X\), and similarly for lines. Write \(w(P)=\#\{X:\beta\alpha(X)=P\}\) and \(v(L)=\#\{Y:\alpha\beta(Y)=L\}\).

## Proof

**1. Universal bipartite closure reduction.** By definition of avoiding incidence, \(X\subseteq\beta\alpha(X)\) and \(Y\subseteq\alpha\beta(Y)\). Moreover \(\alpha\beta\alpha=\alpha\), \(\beta\alpha\beta=\beta\) by the elementary inclusion-reversing Galois identities: for any point set \(X\) and line set \(Y\), \(Y\subseteq\alpha(X)\) if and only if \(X\subseteq\beta(Y)\). Consequently the maps \(\beta\alpha\) and \(\alpha\beta\) are idempotent, and \(F^3=F\). The complete periodic-state set is therefore the Cartesian product of the 37 closed point sets and the 37 closed line sets, with \(F\) swapping their dual labels.

**2. The Fano closed-set and fiber classification.** Every point pair lies on exactly one Fano line; every pair of Fano lines meets in exactly one point. If \(|X|=0,1,2\), its closure is \(X\). If \(X\) is a noncollinear three-set, exactly one line is disjoint from it, so its closure is the four-set complementary to that line. If \(X\) is a collinear three-set, no line avoids it, so it closes to all seven points. A four-set complementary to a line is closed; its fiber consists of itself and its four three-subsets. All other subsets of size at least four, and the collinear triples, close to all points. Thus the full closed-point inventory is

| Type of closed point set | Number | Fiber size \(w\) | Fiber size of the dual closed line set \(v(\alpha(P))\) |
|---|---:|---:|---:|
| Empty | 1 | 1 | 64 |
| Singleton | 7 | 1 | 5 |
| Two points | 21 | 1 | 1 |
| Complement of one line | 7 | 5 | 1 |
| All seven points | 1 | 64 | 1 |

There are exactly \(1+7+21+7+1=37\) closed sets. The fiber weights sum to \(1+7+21+35+64=128\), the number of arbitrary point subsets. Point-line duality gives the same inventory on the line shore. The dual-fiber column follows because the anti-incidence operator interchanges empty/full, singleton/complement-of-line and pair/pair types.

**3. Orbits.** Every periodic state is uniquely of the form \((P,\alpha(Q))\) with \(P,Q\) closed point sets. The update exchanges these two labels, \(F(P,\alpha(Q))=(Q,\alpha(P))\). Equal labels give 37 fixed points; unordered unequal labels give \(\binom{37}{2}=666\) primitive two-cycle orbits. The 37 fixed points correspond to maximal independent sets, a pre-existing general relation; the new claim is the complete Heawood orbit/basin census.

**4. Basin sizes.** If \(P\) and \(Q\) are closed, then the configurations with \(F^2(X,Y)=(P,\alpha(Q))\) have cardinality \(w(P)v(\alpha(Q))\). If \(P=Q\), this is the fixed-attractor basin size. If \(P\ne Q\), the two disjoint halves of the orbit basin have combined size
\[
B(P,Q)=w(P)v(\alpha(Q))+w(Q)v(\alpha(P)).
\]
Substituting the five rows above and multiplying by the corresponding unordered type-pair counts yields the eleven rows in the Finding table, and every possible unordered pair is included exactly once. In particular, the empty/full pair has basin size \(1+64^2=4097\), unique because no other unordered type pair yields that value. The total fixed basin mass is \(21+14\cdot5+2\cdot64=219\); the remaining \(16384-219=16165\) belong to two-cycles. Of these, exactly \(2\cdot666=1332\) are periodic themselves. These counts also establish the entry-time census. Sharpness of one update follows because the 15,015 nonperiodic initial configurations are nonempty in number.

## Verification

The source files `heawood_nor.cpp` and `verify_duality.py` are standalone and require respectively a C++17 compiler and Python 3 standard library. Run `c++ -O2 -std=c++17 heawood_nor.cpp -o heawood_nor && ./heawood_nor` and `python3 verify_duality.py`. The C++ code enumerates all 16,384 state transitions, checks \(F^3=F\) for every input and tabulates both entry times and individual orbit basins. The Python code separately enumerates all 128 subsets of each shore, checks closure fibers, and recomputes the basins from the analytic Galois formula, including a basin-size weighted sum of 16,384. Their outputs are supplied in `census.txt`.

## Relationship to prior work

The correspondence between fixed points of fully negative conjunctive Boolean networks and maximal independent sets is known (Aracena, Richard and Salinas, arXiv:1507.06141, Section 1). This fact is used rather than claimed as new. General max/minterm Boolean-network studies give periodic-point bounds or counts for different local conventions, but do not provide the closed-fiber geometry or complete 14-vertex Heawood attraction-basin distribution. Closely related published case studies concern NOR on leaf coronas and majority (not NOR) on Heawood; neither specializes to the stated Fano incidence computation. The present contribution is the **complete geometry-resolved exact attractor and basin census**, not the elementary general statement that a bipartite NOR network has two-step recurrent dynamics.

## Limitations

This is an exact finite-graph theorem for the specified labelled Fano incidence network. It does not assert a corresponding basin census for larger projective planes, altered local rules, asynchronous updates or perturbed graphs. The historically earliest appearance of any equivalent unindexed finite computation has not been established. Independent external mathematical validation has not been performed; all proofs and computational cross-checks described here belong to the same scientific submission.

## References

- Julio Aracena, Adrien Richard, Lilian Salinas, *Fixed points in conjunctive networks and maximal independent sets in graph contractions*, original arXiv submission 22 July 2015, https://arxiv.org/abs/1507.06141.
- J. Aracena, A. Richard, L. Salinas, *Maximum number of fixed points in AND–OR–NOT networks*, *Journal of Computer and System Sciences* 80 (2014), 1175–1190, https://doi.org/10.1016/j.jcss.2014.04.025.
- J. A. Aledo et al., *Counting Periodic Points in Parallel Graph Dynamical Systems*, *Complexity* (2020), Article 9708347, https://doi.org/10.1155/2020/9708347.
- *Heawood Graph*, Wolfram MathWorld, https://mathworld.wolfram.com/HeawoodGraph.html (graph geometry and the Fano point-line interpretation).
