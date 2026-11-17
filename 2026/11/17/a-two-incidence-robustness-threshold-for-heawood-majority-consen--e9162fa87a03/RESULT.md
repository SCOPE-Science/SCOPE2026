# A two-incidence robustness threshold for Heawood majority consensus

## Finding

Let \(H\) be the fourteen-vertex incidence graph of the Fano projective plane. Run synchronous binary open-neighborhood majority dynamics, retaining the current bit at any tie. For a set \(D\) of deleted incidences, let \(\mathcal B_D\) be the set of labelled initial configurations that eventually reach one of the two unanimous fixed configurations. The following **sharp two-deletion robustness threshold** holds:

\[
\mathcal B_{\varnothing}\subseteq\mathcal B_D
\quad\text{for every }|D|\le1,
\]

and, for two distinct incidences \(e,f\),

\[
\boxed{\mathcal B_{\varnothing}\subseteq\mathcal B_{\{e,f\}}
\ \Longleftrightarrow\ e\text{ and }f\text{ share a vertex in }H.}
\]

Thus **exactly two deleted incidences are needed to destroy consensus attraction for even one initial configuration**, and every disjoint pair does so. Yet every one- or two-edge deletion *increases the total number* of consensus-attracted initial configurations. A complete dynamical census, valid for all 232 choices of zero, one or two deletions, is:

| Deleted-incidence class | Choices | Fixed configurations | Primitive two-cycle orbits | Unanimity basin size | Gained against intact | Lost against intact | Sharp entry bound |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| None | 1 | 58 | 1,653 | 2,592 | 0 | 0 | 2 |
| One incidence | 21 | 66 | 777 | 3,744 | 1,152 | 0 | 6 |
| Two sharing an endpoint | 42 | 58 | 533 | 4,960 | 2,368 | 0 | 11 |
| Two disjoint with a cross incidence | 84 | 90 | 376 | 4,032 | 1,736 | 296 | 8 |
| Two disjoint without a cross incidence | 84 | 86 | 427 | 4,512 | 2,048 | 128 | 6 |

Here “gained” means \(|\mathcal B_D\setminus\mathcal B_{\varnothing}|\), and “lost” means \(|\mathcal B_{\varnothing}\setminus\mathcal B_D|\). The **first periodic entry time** of an initial configuration is the least nonnegative number of updates after which its state belongs to a temporal orbit; every orbit in the table has period one or two. The bound eleven is attained for every adjacent pair of deleted incidences.

## Assumptions and scope

Use fourteen labelled vertices numbered 0 to 13. Vertices 0 through 6 are Fano points numbered 1 through 7 with one subtracted; vertices 7 through 13 correspond, in order, to the seven Fano lines

\[
123,\quad145,\quad167,\quad246,\quad257,\quad347,\quad356.
\]

An incidence edge connects a point to a line precisely when the point appears in the listed triple. In particular, \(H\) has twenty-one undirected edges; no vertices are deleted and the same fourteen labels are retained for every defective graph.

For each graph \(H-D\), each vertex \(v\), and every binary state \(s\), let \(d_D(v)\) be the remaining degree and \(k_D(v,s)\) the number of neighbors in state one. Define the simultaneous update \(F_D\) by

\[
(F_D(s))_v=\begin{cases}
1,&2k_D(v,s)>d_D(v),\\
0,&2k_D(v,s)<d_D(v),\\
s_v,&2k_D(v,s)=d_D(v).
\end{cases}
\]

Thus ties at the degree-two vertices caused by deletion retain the incumbent state. The unanimous fixed configurations are \(\mathbf 0\) and \(\mathbf 1\). A configuration \(s\) lies in \(\mathcal B_D\) precisely when \(F_D^t(s)\) is unanimous for some integer \(t\ge0\). The census is for **labelled** binary states: complement, spatial automorphism, and temporal phase are not identified, except that primitive two-cycle *orbits* identify the two temporal phases.

A pair of removed edges is **adjacent** if the two incidences share a Fano point or line. If they are disjoint, write them as \((p,L)\) and \((q,M)\) with \(p\in L\), \(q\in M\), \(p\ne q\), \(L\ne M\). It has a **cross incidence** if \(p\in M\) or \(q\in L\). At most one cross incidence is possible because the Fano plane has no four-cycles in its incidence graph. The remaining disjoint pairs have no cross incidence.

## Proof

**1. Complete finite domain and classification of deletions.** There are exactly twenty-one incidences, hence \(1+21+\binom{21}{2}=232\) distinct labelled graphs in scope, each with exactly \(2^{14}=16{,}384\) possible labelled binary configurations. There are forty-two unordered incidence pairs sharing an endpoint, because every one of the fourteen cubic vertices yields three pairs and no pair shares both endpoints. Of the remaining 168 disjoint pairs, 84 admit a cross incidence and 84 do not. The latter two counts can be derived by fixing an incidence \((p,L)\): among the twenty other incidence edges, four share an endpoint, eight are disjoint with a cross incidence and eight are disjoint without one; count unordered pairs by dividing the resulting twenty-one-fold sums by two. The enumerators independently check the same partition for all pairs rather than relying on an unproved classification by symmetry.

**2. Exact transition enumeration.** Encode a labelled configuration as the integer \(s=\sum_{v=0}^{13}s_v2^v\). For every allowed deletion set \(D\), form its fourteen neighbor bitmasks and compute all \(16{,}384\) values of \(F_D(s)\) by integer bit counts and the update equation above. For each state iterate forward until the exact criterion \(F_D^2(s)=s\) holds. Both finite checkers verify directly that this happens in at most eleven steps for every starting state in every graph, so no external convergence theorem is required to close the exhaustive proof. In the final periodic state, count whether the state is unanimous. Simultaneously count states with \(F_D(s)=s\) and halve the number satisfying \(F_D^2(s)=s\ne F_D(s)\). For every original initial bitmask compare its unanimity indicator in the modified graph against the intact graph to obtain exact lost and gained populations.

The first independently implemented checker, `check_all_defects.cpp`, directly enumerates all 232 graphs and all \(16{,}384\) configurations of each, tests each terminal two-step identity, and checks that every graph in a given incidence-pair class yields the displayed invariant tuple and entry-time histogram. The second checker, `check_vectorized.py`, constructs the Fano lines independently from binary vector arithmetic over the two-element field, vectorizes every entire transition map, works backwards from the exact two-periodic set to compute first-entry layers, and compares all unanimity-basin bitmasks. Its full 232-graph classification agrees with the first checker. Both programs have explicit assertions of every tabulated value. The source files and captured program output are included with this result; they constitute a finite exhaustive proof over the specified 3,801,088 graph–configuration instances, not a numerical sample or extrapolation.

**3. The robustness equivalence and sharp delay.** The verified consensus-loss column is zero for the intact graph, all twenty-one one-edge deletions and all forty-two adjacent two-edge deletions. It is exactly 296 for each of the eighty-four cross-incidence disjoint pairs and exactly 128 for each of the eighty-four remaining disjoint pairs. Equality of this loss count to zero is equivalent, by definition, to \(\mathcal B_{\varnothing}\subseteq\mathcal B_D\). This proves both directions of the boxed equivalence, including its universal quantifiers. All modified unanimity basin sizes exceed 2,592; hence net gains do not force set inclusion.

As explicit loss witnesses in the required vertex labelling, delete the edges \((0,7)\) and \((1,10)\), a disjoint pair with a cross incidence. Initial integer bitmask 130 follows \(130\to0\) on the original graph but is a nonunanimous fixed point of the defective graph. For the disjoint pair \((0,7)\) and \((3,10)\), with no cross incidence, bitmask 265 follows \(265\to256\to0\) on the intact graph and is fixed nonunanimously after deletion. These witness claims can be checked directly from the seven given Fano lines and the majority equation. The full-table enumeration establishes the corresponding statement for *every* pair.

Finally, in the adjacent-pair class exactly 64 starting configurations first become periodic after eleven updates, and no configuration in any class takes longer. This proves sharpness of the reported maximal entry time without mistaking a finite search timeout for a mathematical bound.

## Verification

Compile and run `check_all_defects.cpp` using `g++ -std=c++17 -O2 -Wall -Wextra -pedantic check_all_defects.cpp -o verify && ./verify`. Its recorded output is `check_all_defects_output.txt`. The program requires only the C++17 standard library. It evaluates every zero-, one- and two-incidence deletion and every state; it asserts the full table and complete entry-time histograms.

Independently run `python3 check_vectorized.py` with Python 3 and NumPy installed. Its output is `check_vectorized_output.txt`. The second program starts from the two-dimensional binary subspaces of the Fano plane, independently generates all twenty-one edges and rechecks all 232 graph cases with a vectorized transition construction and backward entry-layer calculation. Both final outputs report PASS. The exact source files, not merely log summaries, are attached.

## Relationship to prior work

The classical Goles–Olivos symmetric-threshold theorem establishes that eventual periods of finite synchronous majority systems are at most two; it does not determine attraction-basin inclusion under missing incidences. Tamuz and Tessler study majority dynamics, preservation of information, and combinatorial convergence bounds on graphs; Kaaser, Mallmann-Trenn and Natale develop general bounds on voting time. Neither inspected treatment supplies this complete defective-Fano incidence classification or its sharp loss threshold. The standard Fano incidence geometry and the fact that the Heawood graph is the cubic girth-six cage are not new.

A public exact result titled *A two-step majority projection and exact attraction basins on the Heawood graph* establishes the intact case: the 58 fixed states, 1,653 primitive two-cycles, the 2,592-state unanimous basin, and a sharp two-step entry bound. **Those intact results are credited here rather than claimed anew.** Their 58-symbol projection acts on the full incidence graph and does not provide any of the three two-edge-deletion basin comparisons. Related single-edge majority results on complete bipartite graphs concern a different graph family; their one-edge formulas do not cover the Heawood graph, which has only three neighbors per vertex, not all seven vertices of the opposite shore. Originality claimed here is solely the complete one-/two-deletion robustness boundary and its numerical census.

## Limitations

The theorem is a finite classification for precisely the labelled Heawood graph and its zero-, one- or two-edge deletions with incumbent tie retention. It does not claim monotonicity for general graphs, higher-order defect sets, randomized tie resolution, asynchronous voting, or larger projective planes. The proof is a complete finite computation with two inspectable implementations; it is not a conceptual formula covering arbitrary graph size. Searches cannot establish absolute historical priority. An independent external mathematical audit has not yet been performed.

## References

1. O. Tamuz and R. J. Tessler, *Majority Dynamics and the Retention of Information*, arXiv:1307.4035, first publicly posted 2013-07-15, https://arxiv.org/abs/1307.4035 ; accessible full HTML https://arxiv.org/html/1307.4035v2 .
2. D. Kaaser, F. Mallmann-Trenn and E. Natale, *On the Voting Time of the Deterministic Majority Process*, arXiv:1508.03519, first publicly posted 2015-08-14, https://arxiv.org/abs/1508.03519 .
3. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics 30 (1980), 187–189, https://doi.org/10.1016/0012-365X(80)90121-1 .
4. *A two-step majority projection and exact attraction basins on the Heawood graph*, publicly indexed exact result (2026), https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-a-two-step-majority-projection-and-exact-attraction-basins-on-th--8cd2964a9d93/RESULT.md .
5. E. W. Weisstein, *Heawood Graph*, MathWorld, https://mathworld.wolfram.com/HeawoodGraph.html ; graph geometry only.
