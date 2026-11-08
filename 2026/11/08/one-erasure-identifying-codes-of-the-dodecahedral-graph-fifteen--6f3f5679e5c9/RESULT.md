# One-erasure identifying codes of the dodecahedral graph: fifteen isolated optima with a Kneser intersection geometry

## Finding
For the dodecahedral graph \(D=GP(10,2)\), a radius-one identifying code that remains an identifying code after deletion of *any one selected vertex* must have at least \(12\) vertices. There are **exactly fifteen** such minimum one-erasure-resilient codes. They have the following precise intersection spectrum: among the \(\binom{15}{2}=105\) pairs, exactly \(60\) pairs have intersection size \(6\), and exactly \(45\) pairs have intersection size \(8\). The graph whose vertices are these fifteen codes, with two adjacent when their intersection has size \(8\), is isomorphic to the Kneser graph \(KG(6,2)\) on two-subsets of a six-element set. Since two distinct minimum codes differ in at least four vertices, the one-token-jump and token-slide reconfiguration graphs on minimum resilient codes are each \(15K_1\). These are exact finite statements, established by exhaustive and independently checked finite enumeration, not an extrapolation to other graph orders.

## Assumptions and scope
Let \(u_i,v_i\), \(0\le i<10\), be the vertices of \(D\), with indices taken modulo ten. The edge set consists of \(u_iu_{i+1}\), \(u_iv_i\), and \(v_iv_{i+2}\). For \(w\in V(D)\), let \(N[w]\) be the closed neighborhood. A subset \(C\) is a radius-one identifying code if all signatures \(N[w]\cap C\) are nonempty and pairwise distinct. A one-erasure-resilient identifying code satisfies the same condition even after an adversary deletes any single vertex of \(C\). The deletion refers to the detector/codeword, not to a graph vertex or edge. We use the numbering \(u_i=i\) and \(v_i=10+i\) for the machine-checkable certificates. Both reconfiguration operations replace one selected detector at a time and require retaining the optimal size and resilient property; sliding additionally requires adjacency in \(D\).

## Proof
**Reduction to 210 twofold covering inequalities.** For any two distinct vertices \(a,b\), put \(\Delta_{a,b}=N[a]\mathbin\triangle N[b]\). Write \(\mathbf1_C\) for the characteristic mask of a selected code. Then \(C\) is one-erasure resilient if and only if
\[
|C\cap N[w]|\ge2\qquad(\forall w\in V(D)),
\quad
|C\cap\Delta_{a,b}|\ge2\qquad(\forall a\ne b).
\]
Necessity follows because a singleton identifying signature can disappear when its sole selected detector fails, and a pair of signatures that differ in just one detector become identical after removal of that detector. Sufficiency is immediate: deleting any one selected detector preserves nonemptiness and at least one separator in every symmetric difference. There are precisely \(20+\binom{20}{2}=210\) such constraints. The dodecahedron is cubic, so every chosen vertex lies in four closed neighborhoods; summing the first twenty constraints gives \(4|C|\ge40\), or \(|C|\ge10\).

**Complete finite enumeration and optimality.** The packaged program `verify_exhaustive.cpp` constructs the \(20\) closed-neighborhood bitmasks of \(D\) by the three explicit edge families and forms the \(190\) symmetric-difference masks. It visits each of the \(2^{20}=1,048,576\) subset masks exactly once and applies `popcount(mask & requirement) >= 2` to each of the 210 requirements. Its running upper bound only skips masks larger than an already verified valid mask, never a possible improvement or tie. The complete search returns minimum cardinality \(12\) and exactly fifteen solutions; it rejects all smaller masks. An independent Python program `verify_combinations.py` uses sets instead of the C++ bit matrices and enumerates each \(\binom{20}{k}\) subset for \(k=10,11,12\). The mathematical ten-detector lower bound proves it need not consider smaller cardinalities; the Python search independently returns no solutions at sizes ten and eleven and the same fifteen solutions at size twelve. This exhausts every set that could contradict the minimum and exact count.

The fifteen solution masks in increasing numerical order, using the stated vertex numbering, are
\[
\begin{gathered}
102135,\ 203247,\ 372636,\ 406494,\ 439923,\ 507177,\ 575355,\ 710094,\\
744249,\ 777876,\ 811965,\ 878823,\ 912714,\ 980133,\ 1014354.
\end{gathered}
\]
These decimal integers represent the exact sets \(C=\{i:\text{bit }i\text{ of mask is }1\}\), and are a complete reproducible finite certificate of the optimum. No imported graph catalog is needed.

**Intersection and Kneser structure.** The independently rechecked 105 pair intersections have sizes only six (60 times) and eight (45 times). For a constructive graph-isomorphism certificate, label the fifteen codes in the ascending-mask order displayed above with the following fifteen two-subsets of \(\{0,1,2,3,4,5\}\), in the same order:
\[
\begin{gathered}
01,\ 23,\ 35,\ 04,\ 25,\ 14,\ 34,\ 15,\\
05,\ 24,\ 12,\ 45,\ 02,\ 03,\ 13.
\end{gathered}
\]
Here \(ij\) denotes \(\{i,j\}\). Both programs verify for every pair of different indices that the two code supports intersect in exactly eight vertices **if and only if** the associated two-subsets are disjoint. This verifies the asserted isomorphism with \(KG(6,2)\), not merely matching graph parameters. Two size-twelve sets that differ by a single token jump would intersect in eleven vertices, but no pair of optima intersects in more than eight. Therefore all fifteen minimum codes are isolated in both reconfiguration graphs.

## Verification
Compile the included standalone C++17 program with `g++ -O2 -std=c++17 verify_exhaustive.cpp -o verify_exhaustive`, then run `./verify_exhaustive`; run the independent standard-library Python 3 implementation with `python3 verify_combinations.py`. The recorded actual output files are `exhaustive_output.txt` and `combinations_output.txt`. Both verifiers assert all stated numerical results and the explicit Kneser mapping, and they reject any mismatch. The C++ loop is exhaustive over all 1,048,576 graph vertex subsets, so the finite minimum and count are proved by finite decision procedure together with program inspection and execution. Neither program assumes the claimed count as a search cutoff. The Python verifier independently checks every size ten, eleven and twelve combination, using the mathematical size-ten lower bound.

## Relationship to prior work
Identifying codes and their fault-tolerant variants are established topics in separating-system design and graph monitoring; no priority is claimed for their general definitions. Gravier, Klasing and Moncel discuss fault tolerance in the identification context. The classic papers on identifying codes in girth-five and vertex-transitive graphs address standard (non-erasure) codes and general bounds, not the present one-erasure optimum census on the dodecahedron. The dodecahedron's equitable two-colorings with an \(8/12\) partition, including the \((0,3;2,1)\) quotient, are previously known; these are not the twelve-detector deletion-resilient sets investigated here. The classical five cubes inscribed in a dodecahedron also do not classify resilient identifying codes. The exact fifteen-code optimum census, intersection realization of \(KG(6,2)\), and resulting reconfiguration rigidity are the present claim.

## Limitations
This concerns the single-erasable-detector requirement and radius-one signatures on the fixed twenty-vertex graph, not sensor-signal errors or higher fault multiplicities. All finite completeness claims are conditional on the explicitly inspectable algorithms and their exhaustive execution. The result does not imply a formula on an infinite family of graphs. Older equitable-partition literature was identified and treated as strong prior context; inaccessible or unindexed results could affect priority, so global historical novelty is not independently established. No independent scholarly validation has been performed.

## References
1. S. Gravier, R. Klasing, and J. Moncel, *Hardness results and approximation algorithms for identifying codes and locating-dominating codes in graphs*, Algorithmic Operations Research, 2008, https://journals.hil.unb.ca/index.php/AOR/article/view/2808 .
2. C. Balbuena, F. Foucaud, and A. Hansberg, *Locating-dominating sets and identifying codes in graphs of girth at least 5*, arXiv:1407.7263 (first public 2014-07-27), https://arxiv.org/abs/1407.7263 .
3. S. Gravier, A. Parreau, S. Rottey, L. Storme, and E. Vandomme, *Identifying codes in vertex-transitive graphs and strongly regular graphs*, arXiv:1411.5275 (first public 2014-11-19), https://arxiv.org/abs/1411.5275 .
4. M. H. Alaeiyan and H. Karami, *Perfect 2-colorings of the Platonic graphs*, International Journal of Nonlinear Analysis and Applications 8 (2017), 29–35, doi:10.22075/ijnaa.2016.455, https://doi.org/10.22075/ijnaa.2016.455 .
5. D. S. Krotov and V. N. Potapov, *Completely Regular Codes and Equitable Partitions*, arXiv / book chapter (2024–2025), doi:10.1201/9781003393931-1 .
