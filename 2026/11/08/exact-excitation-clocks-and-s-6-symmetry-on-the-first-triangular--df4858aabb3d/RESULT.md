# Exact excitation clocks and \(S_6\)-symmetry on the first triangular Kneser graph

## Finding

On the Kneser graph \(KG(6,2)\), synchronous three-color, threshold-one Greenberg–Hastings excitation has primitive temporal periods **exactly** \(1,3,4,7\). The numbers of distinct labelled temporal cycles are respectively \(1\), \(1{,}258{,}232\), \(90\), and \(180\). Among \(3^{15}=14{,}348{,}907\) labelled configurations, exactly \(3{,}776{,}317\) are already periodic; every configuration enters a cycle after at most \(10\) updates, and exactly \(1{,}440\) require all ten.

Under the full graph automorphism group \(\operatorname{Aut}(KG(6,2))\cong S_6\), the \(90\) period-four temporal cycles split into exactly two orbits of \(45\) each (stabilizers of order \(16\)); the \(180\) period-seven temporal cycles form exactly **one** orbit (stabilizer of order \(4\)). Counting excited vertices (color \(1\)) during successive steps, the two period-four orbits have cyclic profiles \((1,2,8,4)\) and \((1,4,8,2)\), while the unique period-seven orbit has cyclic profile \((2,3,8,3,2,6,6)\). Every vertex is excited exactly once per period-four orbit and twice per period-seven orbit.

The full joint census of first entry time \(t\) and eventual primitive period \(p\) is given below (entries are **states**, not cycles):

| \(t\) | \(p=1\) | \(p=3\) | \(p=4\) | \(p=7\) |
|---:|---:|---:|---:|---:|
| 0 | 1 | 3,774,696 | 360 | 1,260 |
| 1 | 32,767 | 1,751,640 | 24,660 | 7,020 |
| 2 | 41,977 | 3,153,000 | 33,840 | 9,180 |
| 3 | 39,096 | 3,394,560 | 29,520 | 6,480 |
| 4 | 12,090 | 1,494,960 | 13,140 | 3,600 |
| 5 | 0 | 278,820 | 0 | 0 |
| 6 | 0 | 148,320 | 0 | 0 |
| 7 | 0 | 84,240 | 0 | 0 |
| 8 | 0 | 7,920 | 0 | 0 |
| 9 | 0 | 4,320 | 0 | 0 |
| 10 | 0 | 1,440 | 0 | 0 |

## Assumptions and scope

The vertex set consists of the \(15\) unordered two-element subsets of \(\{0,1,2,3,4,5\}\), ordered lexicographically as \((0,1),(0,2),\ldots,(4,5)\). Two vertices are adjacent exactly when these subsets are disjoint. For each state \(x\in\{0,1,2\}^{15}\), the simultaneous update \(F\) is
\[
(Fx)_v=\begin{cases}1,&x_v=0\text{ and some neighbor of }v\text{ has color }1,\\0,&x_v=0\text{ and no neighbor has color }1,\\2,&x_v=1,\\0,&x_v=2.\end{cases}
\]
There are no random updates, directed edges, loops, or extra self-neighbor contacts. First entry time means the least \(t\ge0\) such that \(F^t(x)\) lies on a temporal cycle. Primitive period means the least positive return time of that cyclic state. Cycles are identified modulo temporal rotation, not spatial graph automorphisms; the latter are used only for the separate orbit classification. There is no assertion for other Kneser graphs or for more than three colors.

## Proof

**Complete finite-state enumeration.** Encode each \(x=(x_0,\ldots,x_{14})\) uniquely by \(e(x)=\sum_{i=0}^{14}x_i3^i\), so \(0\le e(x)<3^{15}\). The standalone `src/census.cpp` loops over every such integer exactly once, decodes its fifteen ternary digits, and computes the one-step successor by the displayed local rule with the six-neighbor disjointness test. It forms the successor array and the full indegree array of this finite functional graph. Repeatedly deleting indegree-zero vertices leaves exactly the union of directed cycles: a finite functional digraph has no other positive-indegree terminal core. Every remaining vertex is traversed once along its unique cycle, giving its least period. Reversing the deletion order then determines every deleted state's entry time and eventual period recursively from its already-classified successor. The resulting \(26\) nonzero \((t,p)\) counts are exactly the displayed table and `data/raw_census.txt`. Their sum is \(3^{15}\), so the classification covers the entire state space. In particular the only primitive periods are \(1,3,4,7\), and the largest observed entry time \(10\) is attained \(1{,}440\) times, proving sharpness for this explicitly finite graph.

**Independent second exhaustive algorithm.** `src/forward_verify.cpp` constructs the neighbors by a separate fixed-width six-neighbor array, recomputes the update without an indegree array, and classifies each unvisited state by following its orbit until it encounters either the current path or an already closed path. It marks every encountered state as processed and unwinds each path backward to assign its entry time and least eventual period. The second method visits all \(14{,}348{,}907\) distinct starting-state indices and obtains exactly the same \(26\) nonzero cells and four cycle counts (`data/forward_census.txt`). This is a second complete finite computation, rather than sampling.

**Full spatial symmetry and cycle orbits.** The graph contains exactly six independent sets of maximum size five: for each ground-set point \(a\), the five two-subsets containing \(a\). Indeed, an intersecting family of edges of a complete graph without a common endpoint is contained in a triangle and has at most three edges; otherwise all edges meet at one point. Hence every graph automorphism permutes these six maximal independent sets, and is uniquely determined by this permutation. All \(6!\) permutations of ground-set labels act as graph automorphisms, proving \(\operatorname{Aut}(KG(6,2))=S_6\). Each cycle representative in `data/representatives.txt` is the smallest ternary integer on that temporal cycle. `src/symmetry.cpp` takes all \(720\) ground-set permutations, acts on each of the \(270\) representative period-four and period-seven cycles, reduces by temporal rotation, and computes the resulting exact group orbits. The output is exactly two orbits of \(45\) at period four and one of \(180\) at period seven (`data/symmetry_results.txt`). Since \(720/45=16\) and \(720/180=4\), their stabilizer orders follow by orbit-stabilizer. The same program checks all \(270\) cycles close after their claimed primitive time and counts each vertex's excitations and the color-one temporal profile. The orbit representatives and their ternary digits are supplied in the data output.

This is an exact finite mathematical classification by complete enumeration with explicit algorithmic invariants. The table is not inferred from partial runs, a random sample, or an infinite-family extrapolation.

## Verification

From the embedded package root run `python3 src/verify.py` with Python 3 and a C++17 compiler on the executable path. The script compiles all three standalone C++ programs in an isolated temporary directory, executes both complete finite-state classifications, compares their full joint tables, validates the expected cycle and state counts, checks the \(270\) representative-cycle enumeration, and replays the complete \(720\)-element symmetry action. The captured replay output is in `data/checks.txt`. Cross-checked data files are `data/raw_census.txt`, `data/forward_census.txt`, `data/representatives.txt`, and `data/symmetry_results.txt`.

A direct consistency check is \(1+3(1{,}258{,}232)+4(90)+7(180)=3{,}776{,}317\), matching the first row of the joint table; the sum of its entire table is \(14{,}348{,}907\). Algorithmic exhaustiveness is justified by scanning every base-three state and by the functional-graph invariants described above. A successful run is not an independent audit.

## Relationship to prior work

The original Greenberg–Hastings setting and early rigorous work on excited media precede this calculation. Durrett–Griffeath's 1993 public preprint studies phase transitions and spatial periodic objects in excitable automata [1]. Gravner–Lyu–Sivakoff's manuscript, first publicly posted October 24, 2016 and later published in 2018, gives a general covering-space criterion for synchronization and excitation rates on arbitrary graphs [2,3]. In particular, its finite-graph Theorem 3 determines excitation activity through maximal cycle-integral ratios, **not** the exact numbers of labelled primitive temporal cycles, transient-entry counts, or spatial-symmetry classes on this graph. The canonical graph \(KG(6,2)\), its 15 vertices, spectrum and full group \(S_6\) are standard [4]; they are not presented as new.

This graph is the first two-subset Kneser graph containing triangles (in contrast with \(KG(5,2)\), the Petersen graph). The period-seven orbit forms a single symmetry type, and the period-four orbits form exactly two distinct types. That group-resolved dynamic distinction is the principal finite structural motivation, rather than an arbitrary unlabeled state count. The exact specialization was not located in the inspected literature or published-claim searches; such searches do not establish historical novelty conclusively.

## Limitations

The claim is a finite result for one specified fifteen-vertex graph and one synchronous three-color rule. It does not establish a formula for the entire Kneser family, other thresholds, stochastic variants, or graph perturbations. Its exactness relies on replayable exhaustive programs whose invariants are stated above; no independent formal certification or external audit has been performed. Prior literature under alternative nomenclature or in unindexed tables could contain an equivalent census. The accessible 2018 version of [3] was inspected in detail, but the complete text of its original 2016 arXiv version was not separately retrieved.

## References

[1] R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, public arXiv preprint `patt-sol/9303002`, posted 1993-03-22, https://arxiv.org/abs/patt-sol/9303002.

[2] J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv `1610.07320`, first posted 2016-10-24, https://arxiv.org/abs/1610.07320.

[3] J. Gravner, H. Lyu and D. Sivakoff, same title, *Annals of Applied Probability* **28** (2018), 3324–3357, DOI `10.1214/17-AAP1350`, https://www.math.ucdavis.edu/~gravner/hidden/clanki/AAP_2018.pdf.

[4] DistanceRegular.org, *Kneser graph K(6,2)*, graph data resource, https://www.math.mun.ca/distanceregular/graphs/kneser6.2.html (resource updated 2024-08-13; this update date is not used as a historical priority anchor).
