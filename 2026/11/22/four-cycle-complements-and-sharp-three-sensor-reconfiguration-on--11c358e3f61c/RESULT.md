# Four-cycle complements and sharp three-sensor reconfiguration on the Desargues graph

## Finding

Let \(D=H(5,2)\) be the 20-vertex Desargues graph, whose vertices are the two-element and three-element subsets of \([5]=\{1,2,3,4,5\}\), adjacent when one is contained in the other. A redundant identifying code is a vertex set that remains a closed-neighborhood identifying code after the deletion of any one chosen detector. Its complete cardinality polynomial is

\[
R_D(z)=15z^{12}+120z^{13}+680z^{14}+1824z^{15}+2155z^{16}+940z^{17}+190z^{18}+20z^{19}+z^{20}.
\]

Consequently, the minimum size is \(12\), exactly \(15\) codes attain it, and there are exactly \(5945\) redundant identifying codes altogether. The **new classification** is that every minimum code is obtained by omitting both the two-subset vertex \(e\) and the three-subset vertex \([5]\setminus e\), for each of the four edges \(e\) of a single four-cycle in the complete graph on \([5]\). All \(\binom{5}{4}\cdot3=15\) four-cycles occur, once each. The minima form one orbit under the natural action of \(S_5\).

Under token-addition/removal (TAR) reconfiguration, with intermediate sets required to be redundant identifying codes and of cardinality at most \(b\), the 15 minimum codes lie in distinct components for every \(b\le14\); all 15 are mutually reachable when \(b=15\). Thus **exactly three spare detector positions** are needed to reconfigure among arbitrary optimum placements while retaining fault tolerance throughout.

## Assumptions and scope

The graph is the labelled simple incidence graph specified above. Codes use closed neighborhoods \(N[v]\), not open neighborhoods. For \(C\subseteq V(D)\), identification means that the sets \(C\cap N[v]\) are nonempty and pairwise distinct. One-erasure redundancy means this remains true after removing any one member of \(C\). TAR moves add or delete exactly one selected vertex; both endpoints of every move must meet the redundancy requirement. All intermediate codes have size at most the stated budget. There are no weights, multiple erasures, or restrictions on which detector is added or removed.

## Proof

**Lemma (one-erasure criterion).** A set \(C\) remains identifying after deletion of any one detector if and only if for every vertex \(v\) and every two distinct vertices \(u,v\), respectively,
\[
|C\cap N[v]|\ge2,\qquad |C\cap(N[u]\mathbin{\triangle}N[v])|\ge2.
\]
Indeed, deletion of one detector can remove at most one occupied coordinate from any identifying signature or its pairwise symmetric difference. Conversely, if either displayed quantity is at most one, deleting its unique detector (if any) produces an uncovered vertex or identical signatures. This criterion is already known in the cited foundational literature and is not claimed as a new lemma.

**Finite exhaustive deduction.** The vertices are ordered as increasing five-bit incidence masks, first all masks of weight two and then all masks of weight three. The standalone `verify_main.cpp` constructs the four-element closed-neighborhood mask \(B_v\) of every vertex and the \(190\) difference masks \(B_u\mathbin{\triangle}B_v\). For each integer mask \(c\) in the complete interval \(0\le c<2^{20}\), it tests the displayed lemma with integer bit counts. Exactly one iteration corresponds to each candidate code; no sampling or external table is used. The checked histogram is

\[
(0,\ldots,0,15,120,680,1824,2155,940,190,20,1)
\]

with the first nonzero coefficient in degree \(12\), and total \(5945\). This is an exhaustive finite proof because the code inspects every one of the \(2^{20}\) possibilities and implements precisely the necessary-and-sufficient criterion.

**Geometry of the optima.** For each four-element ground subset there are exactly three perfect matchings of its six edges. Delete one matching to obtain the four edges of a four-cycle. Omit the two-subset vertex associated with each of those four edges and the complementary three-subset vertex. This constructs \(5\cdot3=15\) pairwise distinct twelve-element candidate codes. `verify_main.cpp` constructs this family independently of the code census, verifies that its 15 masks coincide *exactly* with all minimum masks, and verifies that the action of all \(120\) ground-set permutations is transitive. The geometric description therefore covers all minima and no others.

**Reconfiguration.** The verifier builds the finite TAR adjacency relation implicitly: two valid masks are adjacent precisely when their exclusive-or is one bit and the successor obeys the budget. Exhaustive breadth-first search from one minimum reaches precisely one minimum with budget \(12\), \(13\), or \(14\), and all \(15\) with budget \(15\). Since the natural \(S_5\) action permutes minima transitively and preserves the reconfiguration rules, separation of the starting optimum from all other minima at budget \(14\) holds for every optimum. The bound is monotone in budget; hence no smaller budget permits connectivity. All reachable paths are explicitly confined to redundant codes by the adjacency membership check.

**Independent checking.** A separate Python program `verify_secondary.py` uses Python set containment to construct the incidence graph, directly tests the *definition* by deleting each selected detector and examining every remaining neighborhood signature, exhaustively checks all \(\binom{20}{8}\) and \(\binom{20}{9}\) omitted-vertex subsets, and independently reconstructs the 15 four-cycle patterns. It confirms precisely 15 valid eight-omission patterns and no nine-omission patterns. Monotonicity of redundancy under adding detectors implies that the latter also excludes all larger omitted sets. Additionally, the Python program independently enumerates all \(2^{20}\) masks using its own masks of the closed-neighborhood constraints, confirms the entire polynomial, and reproduces TAR reachability at all four budgets.

## Verification

With a C++17 compiler and Python 3, run from the directory containing the two standalone files:

```sh
g++ -std=c++17 -O2 -Wall -Wextra -pedantic verify_main.cpp -o verify_main
./verify_main
python3 verify_secondary.py
```

The verified outputs are `VERIFY_OK: 5945 codes; 15 four-cycle optima; TAR threshold 15` , `INDEPENDENT_DIRECT_ERASURE_OK 15 optima and zero size-11 codes`, and `INDEPENDENT_ALL_WEIGHT_AND_TAR_OK 5945`. The first check tests all configurations, the second gives separate direct-erasure confirmation of the sharp lower bound and complete optimum description. Both source files are embedded with this result; no downloaded data or unstated dependencies are needed.

## Relationship to prior work

Jean and Seo's *Fault-tolerant Identifying Codes in Special Classes of Graphs* (arXiv:2112.01685, first public December 3, 2021), Theorem 2, gives the one-erasure test used here; Theorem 11 proves that every cubic graph has redundant-identifying-code density at least \(4/7\). For a 20-vertex graph this already forces a lower bound of \(12\), so the lower-bound value itself is not presented as new. Their paper includes a census of cubic graphs by order and global extrema, but its inspected cubic section does not identify or classify the Desargues optimal placements or determine their TAR connectivity. The Desargues graph is canonically the bipartite Kneser graph \(H(5,2)\), also isomorphic to the generalized Petersen graph \(GP(10,3)\). Closely related research concerns one-erasure identifying codes of the *dodecahedral* graph, a different 20-vertex cubic symmetric graph; its finite configurations do not imply this Desargues incidence-pattern classification. General false-negative error-detecting identifying codes use a different fault model. The exact 15-cycle optimum description, complete polynomial, and three-spare reconfiguration threshold are the claimed additions.

## Limitations

This is a finite exact theorem for the stated 20-vertex graph, not a theorem for all bipartite Kneser graphs or all cubic distance-regular graphs. The exhaustive certificate is fully inspectable but has not undergone independent scholarly audit. Searches of relevant published work and research records did not reveal a statement implying the combined theorem, but unindexed specialized literature and full text not accessible during review remain possible originality risks. No claim is made about the minimum number of moves between each specific pair of optima.

## References

1. D. C. Jean and S. J. Seo, *Fault-tolerant Identifying Codes in Special Classes of Graphs*, arXiv:2112.01685 (first posted 2021-12-03), https://arxiv.org/abs/2112.01685.
2. S. J. Seo and P. J. Slater, *Fault Tolerant Detectors for Distinguishing Sets in Graphs*, Discussiones Mathematicae Graph Theory 35 (2015), 797–818, https://doi.org/10.7151/dmgt.1838.
3. D. C. Jean and S. J. Seo, *Optimal error-detection system for identifying codes*, Networks 85 (2025), 61–75 (first online 2024-10-01), https://doi.org/10.1002/net.22254.
4. E. W. Weisstein, *Desargues Graph*, MathWorld, https://mathworld.wolfram.com/DesarguesGraph.html.
