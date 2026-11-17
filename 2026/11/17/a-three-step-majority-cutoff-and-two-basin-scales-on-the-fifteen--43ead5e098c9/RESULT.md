# A three-step majority cutoff and two basin scales on the fifteen-vertex Kneser graph

## Finding

Let \(G=KG(6,2)\) be the graph whose vertices are the fifteen two-element subsets of \(\{0,1,2,3,4,5\}\), with two vertices adjacent precisely when their pairs are disjoint. In synchronous binary strict-neighbor-majority dynamics, a vertex switches to the strict majority of its six neighbors, retaining its previous value on a three-to-three tie. Write \(F:\{0,1\}^{15}\to\{0,1\}^{15}\) for the update.

**Theorem (complete labelled dynamical census).** The sharp global identity is
\[
F^5=F^3,\qquad F^4\ne F^2.
\]
Every configuration therefore enters a fixed state or a primitive temporal two-cycle in at most three steps, and three steps are necessary for some configurations. There are exactly **502 fixed configurations** and **2,670 primitive two-cycle orbits** (5,340 periodically oscillating configurations).

For each recurrent orbit let its *basin size* be the number of labelled initial configurations eventually entering that orbit, including its recurrent phases. The complete orbit-level basin distribution is:

| Primitive period | Basin size | Number of recurrent orbits |
|---:|---:|---:|
| 1 | 1 | 360 |
| 1 | 10 | 140 |
| 1 | 10,944 | 2 |
| 2 | 2 | 2,460 |
| 2 | 20 | 210 |

The two unanimous fixed configurations each have basin 10,944, all other fixed configurations have basins 1 or 10, and every primitive two-cycle has basin 2 or 20. The total numbers of initial states eventually reaching fixed points and primitive two-cycles are respectively **23,648** and **9,120**.

Under the full graph automorphism group \(S_6\), the fixed states form exactly **eight** geometric orbits, and the primitive temporal two-cycles form **eighteen** geometric orbits. The size and representative of each orbit, its basin size, the weights of both phases and the number of flipping vertices are recorded in `classes.tsv`. The eight fixed-state geometric orbit sizes are \(1,1,10,10,60,60,180,180\); the eighteen two-cycle orbit sizes are \(45,45,60,60,60,60,90,90,90,90,90,90,180,180,360,360,360,360\).

The exact first-periodic-entry table (entries count *initial states*, not orbits) is:

| First entry time | Fixed-point destination | Primitive two-cycle destination |
|---:|---:|---:|
| 0 | 502 | 5,340 |
| 1 | 4,426 | 3,780 |
| 2 | 13,680 | 0 |
| 3 | 5,040 | 0 |

In particular, every oscillatory basin is exhausted by its recurrent states and their one-step predecessors. The precise invariants above describe the labelled \(15\)-vertex graph, not a claim for all Kneser graphs.

## Assumptions and scope

Use the lexicographic vertex order \((0,1),(0,2),\dots,(4,5)\), indexing bits from zero to fourteen. Write a configuration as the integer
\[
s(x)=\sum_{i=0}^{14}2^i x_i,\qquad 0\le s(x)<32768.
\]
For an edge \(e=\{a,b\}\), define its open-neighbor occupancy
\[
c_e(x)=\sum_{f\cap e=\varnothing} x_f.
\]
Since exactly six two-subsets of the remaining four labels are disjoint from \(e\), the update is
\[
(Fx)_e=\begin{cases}1,&c_e(x)\ge4,\\0,&c_e(x)\le2,\\x_e,&c_e(x)=3.\end{cases}
\]
All updates occur simultaneously; no self-loop or randomness is present. An orbit's temporal period is its least positive return time; a two-cycle is counted once, not once per phase. A configuration's first entry time is the least nonnegative \(t\) for which \(F^t(x)\) lies on a recurrent orbit. Spatial automorphism orbits are counted only in the separate symmetry census, not used to identify labelled temporal orbits.

## Proof

**Finite exact certificate.** There are precisely \(2^{15}=32768\) bit integers in the stated range. For each integer \(s\), the standalone C++ program `verify_majority.cpp` constructs all fifteen six-element disjoint-neighbor masks by the explicit disjointness test and evaluates the displayed update on every one of the 32,768 integers. Its first exhaustive loop checks both \(F^5(s)=F^3(s)\) and the least entry time \(t\in\{0,1,2,3\}\) at which \(F^{t+2}(s)=F^t(s)\). At that point the period is one if \(F^{t+1}(s)=F^t(s)\), and two otherwise. Sorting the two phases yields a unique integer key for each temporal orbit, and counting the initial states assigned to each key produces the exact five basin classes above. Thus the program is a finite exhaustive proof of the sharp universal upper bound and all numerical counts, not an extrapolation from sampled configurations.

The upper bound is sharp independently of any historical data: in the stated bit order the initial integer \(s=63\) has update trajectory
\[
63\longmapsto28704\longmapsto32\longmapsto0\longmapsto0.
\]
Consequently \(F^4(63)=0\ne32=F^2(63)\), so the global identity cannot begin two steps earlier. All nontrivial periods are at most two by the explicit exhaustive identity, without invoking a general theorem.

**Full spatial symmetry.** A family of two-subsets of a six-set is independent in \(KG(6,2)\) exactly when those two-subsets pairwise intersect. A pairwise-intersecting edge family of size at least four in the complete graph on six labels must be a star: if two edges \(ab\) and \(ac\) belong to a family, then any edge not through \(a\) that intersects both must be \(bc\); including \(bc\) limits the family to the three edges of the triangle. Thus the maximum independent sets in \(KG(6,2)\) are precisely the six five-edge stars. Every automorphism permutes these six stars, and their pairwise intersections identify all fifteen vertices uniquely. Conversely every permutation of the six labels preserves disjointness. Hence \(\operatorname{Aut}(G)\cong S_6\).

The five adjacent transpositions generate \(S_6\). The C++ certificate applies those transpositions to each recurrent orbit's canonical temporal key, traverses the full closure and records one representative per spatial class. Direct summation of the orbit sizes in `classes.tsv` yields 502 fixed configurations and 2,670 primitive two-cycle orbits, agreeing with the dynamical loop. Since these generators are the whole automorphism group, the eight- and eighteen-class counts are exact rather than subgroup orbits.

**Independent reconstruction.** The standalone Python checker `verify_majority.py` constructs occupied *sets of named edges*, evaluates their six disjoint neighbors without using the C++ bit-neighbor masks, determines first periodic entry by direct iterate comparison, and recomputes basins and spatial classes. It tests all 32,768 states and checks the exact tables. The two programs' different implementations and their recorded outputs, `verify_cpp.txt` and `verify_python.txt`, agree on all reported totals.

## Verification

Compile and run `verify_majority.cpp` with `g++ -O2 -std=c++17 -Wall -Wextra -pedantic verify_majority.cpp -o verify_majority && ./verify_majority`. Run `python3 verify_majority.py` with Python 3.10 or later. Both use only language standard libraries and regenerate their respective text outputs. The two certificates assert the complete 32,768-state loop, the basin table, both sharp iterate bounds, and the 26 spatial classes. The two captured output logs and `classes.tsv` supplied with this result were generated from the stated algorithms and replayed against their packaged bytes.

Exact consistency checks are
\[
502+2(2670)=5842,\qquad
360+140+2=502,\qquad
2460+210=2670,
\]
\[
360+140(10)+2(10944)=23648,\qquad
2460(2)+210(20)=9120,
\]
\[
23648+9120=32768.
\]
These identities are checks of the computed census, not independent substitutes for the exhaustive loops.

## Relationship to prior work

Goles and Olivos established the eventual period-at-most-two property for finite symmetric binary threshold dynamics [1]. Benjamini and collaborators treat general and random-graph majority convergence, citing that finite-graph theorem explicitly [2]. Neither general statement provides the exact first-entry distribution, basin sizes, or all \(S_6\) symmetry classes for the present Kneser graph.

The publicly available study *Exact excitation clocks and \(S_6\)-symmetry on the first triangular Kneser graph* [3] uses the identical disjointness graph but has **three-state Greenberg–Hastings excitation**, not binary majority; its four possible primitive periods and its counts cannot imply the present theorem. The published treatment *Complete NOR attractors and basin concentration on two-set Kneser graphs* [4] covers the whole graph family but updates each vertex by **NOR** rather than majority with tie retention; despite an overlapping graph parameter, its explicit rule and attractor classifications are different.

## Limitations

This is a complete finite classification on \(KG(6,2)\) only. It gives neither an exact formula uniform in \(KG(n,2)\) nor a detailed geometric naming of every support in the twenty-six classes beyond reproducible labelled representatives. The census depends on the **tie-retaining** majority rule; changing that rule changes the system. Computational exhaustiveness is justified by two simple, completely included finite checkers, but independent mathematical validation and a comprehensive search of unpublished historical calculations have not occurred. An older journal paper [1] was located with month-only bibliographic dating; 2014-05-11 is the first **day-verified public posting date among the primary historical sources used as a date anchor**, not an invented day for that earlier paper.

## References

[1] E. Goles and J. Olivos, *Comportement périodique des fonctions à seuil binaires et applications*, Discrete Applied Mathematics **3** (1981), 93–105. DOI: https://doi.org/10.1016/0166-218X(81)90034-2. The accessible bibliographic record and abstract state the finite fixed/two-cycle theorem; complete original text was not available for inspection.

[2] I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz and L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, arXiv:1405.2486v1 (first posted 2014-05-11), https://arxiv.org/abs/1405.2486. The public HTML text of the primary paper was inspected, including its finite-graph background, theorem statements and proofs.

[3] *Exact excitation clocks and \(S_6\)-symmetry on the first triangular Kneser graph*, published research result, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-excitation-clocks-and-s-6-symmetry-on-the-first-triangular--df4858aabb3d. Its `RESULT.md` was read for the model and conclusion.

[4] *Complete NOR attractors and basin concentration on two-set Kneser graphs*, published research result, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-complete-nor-attractors-and-basin-concentration-on-two-set-knese--e75c8d277ab3. Its `RESULT.md` was read for the model and conclusion.
