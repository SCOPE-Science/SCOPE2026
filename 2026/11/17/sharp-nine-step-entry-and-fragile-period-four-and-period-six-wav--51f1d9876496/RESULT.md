# Sharp nine-step entry and fragile period-four and period-six waves in three-shore cyclic competition

## Finding

For every complete tripartite graph \(K_{a,b,c}\) with positive shore sizes \(a,b,c\), let \(F\) be the synchronous three-colour cyclic update with contact threshold two: a vertex of colour \(j\in\{0,1,2\}\) advances to \(j+1\pmod 3\) precisely when at least two *distinct neighbours* currently have that successor colour. For all positive shore sizes,
\[
\boxed{F^{21}=F^9.}
\]
Every labelled initial configuration therefore first enters a periodic orbit by update nine. The bound nine is attained on \(K_{2,3,5}\). The possible eventual least periods, across the entire family, are precisely \(1,3,4,6,12\); in particular, no labelled two-cycle exists.

Write \(u\le v\le w\) for the three shore sizes rearranged in nondecreasing order. The **exact period-existence phase diagram** is:

| Least period | Necessary and sufficient condition |
|---|---|
| \(1\) | All \(u,v,w\ge1\) |
| \(3\) | \(u\ge2\), or \(u=1\) and either \(v\le2,w\ge6\) or \(v\ge5\) |
| \(4\) | \(u=v=2,\ w\ge4\) |
| \(6\) | \(u=v=w=2\) |
| \(12\) | \(u\le3,\ v\ge4\) |

Thus primitive six-cycles occur on the isolated size triple \((2,2,2)\), while primitive four-cycles persist only along the thin family \((2,2,w)\) for \(w\ge4\). Primitive twelve-cycles disappear once all three shores have size at least four, even though they exist whenever one shore has size one, two, or three and both others have at least four vertices. These fragile period classes distinguish the three-shore case from simpler two-shore dynamics.

## Assumptions and scope

All vertices are labelled and all three nonempty shores are pairwise joined and individually independent. The rule is simultaneous; neighbours exclude the vertex itself. Distinct vertices are counted separately when comparing the successor-colour population with the threshold two. A temporal least period is the smallest positive integer \(p\) such that \(F^p(x)=x\) for an already periodic *labelled* configuration \(x\). First periodic-entry time is the smallest nonnegative \(t\) for which \(F^t(x)\) is periodic. The claim concerns deterministic dynamics at threshold two and three colours, not arbitrary thresholds or numbers of colours.

## Proof

**1. Exact finite quotient for decisions.** For shore \(i\in\{1,2,3\}\) and colour \(j\in\{0,1,2\}\), let \(n_{ij}\) be the actual nonnegative number of vertices of that colour, and define \(s_{ij}=\min(2,n_{ij})\). Every successor-colour test depends only on the nine values \(s_{ij}\): the test for colour \(j\) in shore \(i\) is equivalent to
\[
\sum_{h\ne i}s_{h,j+1\bmod3}\ge2.
\]
For each old colour \(j\) in shore \(i\), the entire population moves together or stays. Adding incoming populations and truncating to two therefore commutes with the full update. This gives an *exact* nine-trit transition map \(H\) on \(\{0,1,2\}^9\), even when the true shore sizes are arbitrarily large. A trit vector is realizable with all shores nonempty exactly when each block of three trits has a nonzero entry; there are \(26^3=17{,}576\) such vectors.

**2. Tracking labelled colours.** The truncated quotient by itself cannot determine labelled least periods, because a sequence of populations can recur while original vertices exchange colours. For each realizable starting vector \(s\) and each initially occupied colour bucket \((i,j)\), follow the colour of a *specific* vertex of that bucket through the deterministic sequence of quotient states. Denote this colour after \(t\) updates by \(\gamma^t_s(i,j)\). Every vertex from a given bucket follows precisely the same trajectory. Hence two iterates \(F^r,F^t\) agree for every labelled configuration with truncated vector \(s\) whenever the two tracked-colour lists agree on all occupied buckets.

The standalone `verify_capped.py` enumerates all \(3^9=19{,}683\) quotient vectors, examines the \(17{,}576\) realizable ones, and independently computes \(H^9(s),H^{21}(s)\) and every occupied-bucket trajectory. It verifies for each realizable \(s\) that
\[
(H^9(s),\gamma^9_s)=(H^{21}(s),\gamma^{21}_s)
\]
(on the occupied buckets). This finite, exhaustive check proves \(F^{21}=F^9\) for **every** choice of positive shore sizes, not just the graph sizes used in small brute-force tests. The transition and comparison algorithms are included in full; every integer operation is exact.

**3. All possible labelled periods.** The directed functional graph of \(H\), restricted to realizable states, has exactly 826 distinct directed cycles. For each such quotient cycle, the map on the set of occupied colour buckets after one whole lap is a permutation, because no two occupied buckets can merge on a returning quotient cycle. Explicitly tracking this induced permutation yields the exact least period of the corresponding labelled configuration: the quotient cycle length multiplied by the least common multiple of the permutation cycle lengths on occupied buckets. The exhaustive cycle list has the following breakdown, where the entries count **quotient cycles**, not labelled orbits:
\[
\begin{array}{c|rrrrr}
\text{labelled least period}&1&3&4&6&12\\\hline
\text{quotient cycles}&174&614&9&2&27
\end{array}.
\]
The absence of a quotient cycle giving any other labelled least period proves the stated period set, including exclusion of two-cycles.

**4. Exact size conditions.** Every quotient cycle carries, for each shore \(i\), a minimum population \(m_i=\sum_j s_{ij}\) and a freedom flag: if any trit in the shore is two, every total shore size at least \(m_i\) is realizable; if no trit is two, the shore size is forced to equal \(m_i\). This is both necessary and sufficient because any extra vertices can be assigned to a bucket already holding at least two vertices. The program derives all finite population patterns for each labelled period and compares their union with the five claimed conditions. Each minimum is at most six; values of a shore size above six have indistinguishable truth values for every resulting existential test. Consequently checking all \(7^3=343\) triples with entries one through seven proves the conditions for **all** positive sizes.

**5. Sharp entry.** For shore sizes \((2,3,5)\), an initial exact colour-population profile (in colour order \(0,1,2\)) is
\[
((0,1,1),(2,0,1),(2,2,1)).
\]
The finite quotient's tracked-colour iterates at times eight and twenty differ on an initially occupied bucket, so this labelled state is not periodic at time eight: if it were, its least period, already proved to divide twelve, would imply equality at those times. It is periodic at time nine by step 2. This proves sharpness.

## Verification

Run `python3 verify_capped.py` and `python3 verify_labeled.py` from this directory. Their captured outputs are supplied as `verify_capped.out` and `verify_labeled.out`. The first certifies the exhaustive quotient graph, all occupied-bucket traces and every period-size criterion. The second independently updates every labelled vertex on seven graphs, encompassing \(171{,}315\) labelled states: \(K_{1,1,6}\), \(K_{1,4,4}\), \(K_{1,4,5}\), \(K_{2,2,2}\), \(K_{2,2,4}\), \(K_{2,3,5}\), and \(K_{3,3,3}\). In particular, it finds a labelled period-six orbit on \(K_{2,2,2}\), labelled period-four orbits on \(K_{2,2,4}\), labelled period-twelve orbits on \(K_{1,4,4}\), and a first-periodic-entry witness requiring nine steps on \(K_{2,3,5}\).

The finite quotient computation proves the infinite-family claim because the quotient is exact for decision tests and occupied-bucket colour tracking is exact for every labelled vertex. The vertex enumeration is additional corroboration, not the basis for extending finite experiments to all sizes.

## Relationship to prior work

Durrett and Griffeath [1] introduced a rigorous treatment of excitable cyclic cellular automata and threshold-range phase behavior on lattices. Matamala and Goles [2,3] studied cyclic automata on finite graphs and established general bounds on transient times and periods. The present claim specifies a complete threshold-two least-period existence diagram on complete tripartite graphs and a uniform sharp nine-step bound. Those specific formulae were not identified in the accessible records, but [2,3] are significant unresolved priority comparisons because only their abstracts and bibliographic material could be accessed.

Previously available size-family results for two-shore graphs and a singleton shore do not imply the existence or nonexistence of fragile four- and six-cycles when all three shores contain at least two vertices. An indexed complete-multipartite **binary parity** result uses a different state alphabet and update operation, so its period-four census does not cover this three-colour threshold rule.

## Limitations

The proof is a reproducible finite-exhaustion argument rather than a hand classification of all 826 quotient cycles. The code is necessary to reproduce the exhaustive step. This theorem classifies which least periods exist, not the exact number of labelled initial configurations in every attraction basin. Results do not automatically extend to four shores, other thresholds, self-loops or asynchronous updating. Historical priority against the complete texts of [2,3] is unresolved; independent mathematical review has not been performed.

## References

[1] R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, arXiv:patt-sol/9303002, publicly posted 1993-03-22. https://arxiv.org/abs/patt-sol/9303002

[2] M. Matamala and E. Goles, *Cyclic Automata Networks on Finite Graphs*, LATIN 1995, Lecture Notes in Computer Science 911, pp. 398–410. https://doi.org/10.1007/3-540-59175-3_105

[3] M. Matamala and E. Goles, *Dynamic Behavior of Cyclic Automata Networks*, Discrete Applied Mathematics 77 (1997), pp. 161–184. https://dblp.org/pid/m/MartinMatamala.html
