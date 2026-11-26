# Complementary fifteen-site majority networks have distinct exact attraction-basin spectra

## Finding

Consider the 15 two-element subsets of \(\{1,\ldots,6\}\), indexed lexicographically from zero. On the triangular graph \(T(6)=L(K_6)\) two distinct sites are neighbors if their subsets intersect. At each update, all sites simultaneously adopt the strict majority of their open neighbors, retaining their own opinion on a tie. Write \(F\) for this map, \(t\) for the first time the state lies on its eventual periodic orbit, and \(p\) for that orbit's least period. The basin of a **temporal** orbit includes all labelled states reaching it, including the states on the orbit itself; no quotient by spatial symmetries is taken.

**Triangular-graph transient census.** The sharp maximum entrance time is three: \(F^5=F^3\) and \(F^4\ne F^2\) as maps. The complete labelled first-entry counts are

| \((p,t)\) | \((1,0)\) | \((1,1)\) | \((1,2)\) | \((1,3)\) | \((2,0)\) | \((2,1)\) |
|---|---:|---:|---:|---:|---:|---:|
| \(T(6)\) | 164 | 8544 | 15600 | 6660 | 1080 | 720 |

All other entries are zero. The complete orbit-basin spectrum on \(T(6)\) is

| Least period | Basin size | Number of temporal orbits |
|---:|---:|---:|
| 1 | 1 | 120 |
| 1 | 22 | 30 |
| 1 | 236 | 12 |
| 1 | 13678 | 2 |
| 2 | 2 | 180 |
| 2 | 4 | 360 |

The two basins of size 13678 belong to consensus. Exactly \(1800/32768\) of the initial states, under the uniform measure, reach a primitive two-cycle.

**Comparison to the published complementary baseline.** The complement is \(KG(6,2)\), where neighbors are disjoint subsets. For this graph the result in [1] already established the entire basin and first-entry census under the same rule: sharp entrance time three, consensus basin size 10944 for each consensus state, and 9120 of 32768 initial states reaching a primitive two-cycle. Thus the complement has the **same sharp depth** as \(T(6)\) but \(76/15\) times its probability of eventual oscillation. The Kneser census is used as prior data, not claimed as new; the comparison rests on resolving the transient and basin structure for the triangular graph.

## Exact finite proof

For a state \(x\), let \(d_i\) be the degree of vertex \(i\) in the spanning subgraph of \(K_6\) whose edges are the sites with opinion one. Then the number of neighbors of site \(ij\) with opinion one is \(d_i+d_j-2x_{ij}\): only the site itself is counted twice, and it is not its own neighbor. There are eight open neighbors. Adding the incumbent as one vote converts strict majority with retention at a tie to an integer threshold, hence

\[
F(x)_{ij}=\mathbf 1\{d_i+d_j-x_{ij}\ge5\}.
\]

The enumeration domain is the entire integer interval \([0,32767]\), whose bits biject with the labelled configurations. The transition computed by this formula can equally be computed by storing the 15 neighbor masks. For each state compute \(x_0=x\) and \(x_{j+1}=F(x_j)\) through \(x_5\). Verify \(x_5=x_3\); then the first \(j\in\{0,1,2,3\}\) for which \(x_{j+2}=x_j\) is its entrance time, and the least period is one if \(x_j=x_{j+1}\) and two otherwise. The integer \(\min(x_3,x_4)\) identifies the resulting orbit uniquely: two different orbits of a function do not share a state. Count one state per entry in the resulting \((p,t)\) histogram and one count towards the orbit identified by this minimum. Group the nonempty orbit counts by their least period and basin size. Evaluating these integer loops gives the two tables; the total mass of either census is 32768. Consensus is checked by tallying the keys \(0\) and \(32767\). The lexicographically indexed seed \(695\) follows \(695\to111\to7\to0\to0\), giving the sharp lower bound three.

The standalone `verify_iterates.py` implements the neighbor-mask iteration and table checks. `verify_paths.cpp` instead computes all transitions with neighbor lists and follows the arcs of the functional digraph, assigning each cycle state depth zero and propagating depths and orbit identifiers back along predecessor paths. Their checks for \(KG(6,2)\) additionally reproduce the prior baseline; those checks do not establish priority. Replay with `python3 verify_iterates.py`, or `c++ -O2 -std=c++17 verify_paths.cpp -o verify_paths && ./verify_paths`.

## Prior coverage and scope

The general symmetric-threshold result of Goles and Olivos [2] limits the eventual periods to one and two, but gives neither of the tables above. Existing results on line-graph half-factors and on fixed states of Johnson graphs [3,4] concern recurrent configurations; the counts at \(t=0\) above are not presented as a separate new contribution. Those works do not count the transient predecessors by first-entry time or the sizes of their eventual basins. Related exact basin calculations on the Shrikhande and rook graphs [5] concern a different graph pair. This result is a complete finite enumeration for the specified triangular graph and a comparison with [1], not a formula for arbitrary \(L(K_n)\), an update rule with randomized ties, or a general statement about graph complements.

## References

1. [*A three-step majority cutoff and two basin scales on the fifteen-vertex Kneser graph*](https://github.com/Resultary/2026/tree/main/2026/11/17/SCOPE-a-three-step-majority-cutoff-and-two-basin-scales-on-the-fifteen--43ead5e098c9), 17 November 2026, Finding (same rule, full \(KG(6,2)\) census).
2. E. Goles and J. Olivos, *Comportement périodique des fonctions à seuil binaires et applications*, Discrete Applied Mathematics **3** (1981), 93–105. [DOI](https://doi.org/10.1016/0166-218X(81)90034-2).
3. [*Incidence conservation and half-factor classification of two-cycles in line-graph majority dynamics*](https://github.com/Resultary/2026/tree/main/2026/11/1/SCOPE-incidence-conservation-and-half-factor-classification-of-two-cyc--61b3de3ad47a), 1 November 2026, Finding and Limitations.
4. [*Threshold-graph rigidity and a power-of-two equilibrium type law*](https://github.com/Resultary/2026/tree/main/2026/11/17/SCOPE-threshold-graph-rigidity-and-a-power-of-two-equilibrium-type-law--ae2949f214d6), 17 November 2026, Finding and scope.
5. [*Spectral twins separate under majority dynamics: exact Shrikhande–rook attraction censuses*](https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-spectral-twins-separate-under-majority-dynamics-exact-shrikhande--a7ee2eb89698), 2 November 2026, Finding.
