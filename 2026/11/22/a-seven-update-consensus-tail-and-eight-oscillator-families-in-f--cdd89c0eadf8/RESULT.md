# A seven-update consensus tail and eight oscillator families in Folkman-graph majority dynamics

## Finding

The 20-vertex Folkman graph, the smallest semisymmetric graph, has a sharp **seven-update first-periodic-entry bound** for synchronous binary majority with current-opinion tie retention. Its exact recurrent census is **4,036 fixed states** and **351 primitive temporal two-cycle orbits** (702 states). Its 4,036 equilibria form **44 spatial-automorphism classes**, while its 351 two-cycles form **eight classes after quotienting both spatial automorphisms and temporal phase**.

All \(2^{20}=1{,}048{,}576\) labelled initial states have eventual least period one or two. The eventual fixed-state basin consists of 959,624 states, and the eventual two-cycle basin consists of 88,952. Every state headed to a genuine two-cycle becomes periodic by time three, but fixed-state trajectories can require seven updates. Exactly 960 states require the full seven updates, divided equally between the two unanimous terminal states.

The complete first-entry census \(N_{t,p}\), counting initial states whose smallest periodic-entry time is \(t\) and whose eventual least period is \(p\), is:

| \(t\) | \(N_{t,1}\) | \(N_{t,2}\) |
|---:|---:|---:|
| 0 | 4,036 | 702 |
| 1 | 190,408 | 14,210 |
| 2 | 228,340 | 57,720 |
| 3 | 321,920 | 16,320 |
| 4 | 178,600 | 0 |
| 5 | 33,440 | 0 |
| 6 | 1,920 | 0 |
| 7 | 960 | 0 |

The sizes of the 44 equilibrium classes, given as `class size : multiplicity`, are `1:2, 5:2, 10:2, 20:2, 30:6, 60:12, 80:2, 120:9, 240:6, 384:1`. The sizes of the eight two-cycle classes *including both temporal phases* are `2:1, 10:2, 40:2, 120:1, 240:2`. Every number above is exact.

## Assumptions and scope

Vertices are \(u_{i,\epsilon}\) for \(0\le i<5\) and \(\epsilon\in\{0,1\}\), plus \(v_{ij}\) for \(0\le i<j<5\). Each \(v_{ij}\) is adjacent to precisely \(u_{i,0},u_{i,1},u_{j,0},u_{j,1}\). Thus there are ten doubled vertices and ten edge vertices, each degree four. This is the subdivided double of \(K_5\), hence the usual 20-vertex Folkman graph.

For any binary colouring \(x\) and vertex \(w\), the update \(F(x)_w\) is one if more than two of the four neighbours of \(w\) are one, zero if fewer than two are one, and \(x_w\) if exactly two are one. All vertices update simultaneously. The time \(\tau(x)\) is the least nonnegative integer \(t\) for which \(F^{t+2}(x)=F^t(x)\). The least period at this entry is one when \(F^{t+1}(x)=F^t(x)\), and otherwise two. Statements concern **labelled** states, not independent Bernoulli trajectories or random update schedules.

## Proof

1. **Exact finite universe.** Number the ten doubled vertices by \(2i+\epsilon\), and number the edge vertices from ten through nineteen in lexicographic order of pairs \((i,j)\). Every binary state is a unique 20-bit integer from zero through \(2^{20}-1\). The 20 four-neighbour lists in the supplied programs follow the incidence definition above. Since each pair \((i,j)\) gives exactly four edges, the graph has 40 edges.

2. **Transition evaluation.** For each integer state, `folkman_census.cpp` computes its successor with exactly the stated local majority rule, via integer bit tests. The program builds the complete successor array and traverses its functional graph. Once a visited successor repeats in the current path, the repeated segment is the unique directed cycle; the preceding states have first-entry times equal to their distances to it. If a successor belongs to a previously classified trajectory, its distance and period determine those of the new path. Every vertex is visited and assigned once. This procedure enumerates all \(2^{20}\) possibilities; no sampling or extrapolation is used. Its exact output is `CENSUS.txt`.

3. **Independent comparison.** `verify_folkman_numpy.py` constructs the graph from its pairs using a separately implemented bit-sliced transition and, for all \(2^{20}\) inputs in parallel, checks the identities \(F^{t+2}(x)=F^t(x)\) for \(0\le t\le7\). It assigns the *first* satisfying time and period by direct iterate equality, without functional-graph traversal. Its counts agree with step 2 in every cell, and the union of its classified sets is the entire configuration space. In particular the exact counts at time seven prove sharpness, while the absence of unclassified states proves the upper bound. Its first time-seven state, integer 64,340, has the following 20-bit trajectory at times zero through eight:

```
00001111101101010100
11011110000001010111
00001111111101011100
11011110010001011111
00011111111101011111
11011111111101011111
11011111111111111111
11111111111111111111
11111111111111111111
```

The final equality begins at time seven and not earlier, giving an explicit sharpness witness. The exhaustive comparison also shows that the time-six and time-seven trajectories all terminate in consensus, with exactly half in each unanimous colour.

4. **Symmetry-class census.** The five pairs \(\{u_{i,0},u_{i,1}\}\) are precisely the nontrivial classes of vertices with identical open neighbourhoods. Therefore every automorphism permutes these five pairs; once this permutation is chosen, all edge vertices \(v_{ij}\) are forced, and the two vertices in each pair may be independently swapped. Conversely every such permutation and collection of swaps preserves adjacency. The full graph-automorphism group thus has order \(5!\,2^5=3840\), generated by four adjacent base-index transpositions and five twin swaps. These generators commute with \(F\). `folkman_symmetry.cpp` traverses each group-generated orbit on the exactly recurrent states, adding the temporal successor as a generator only for two-cycles. The component sizes above sum to 4,036 and 702, respectively, and prove the stated 44 and eight symmetry classes.

5. **Basins and late phases.** Summing the first-entry table by eventual least period gives 959,624 and 88,952. The rows for times four through seven have no two-cycle basin entries, and the time-seven population is exactly 960. The two checks agree on every one of these assertions.

## Verification

The standalone C++ source files can be compiled with any C++17 compiler and executed without external libraries. For example, from the directory containing the embedded files, run `g++ -O3 -std=c++17 folkman_census.cpp -o census && ./census` and `g++ -O3 -std=c++17 folkman_symmetry.cpp -o symmetry && ./symmetry`. The first program prints the full joint first-entry census; the second prints the symmetry orbit sizes. The independent Python/NumPy checker can be run with `python verify_folkman_numpy.py`. Its exact output, including the witness trajectory, is recorded in `NUMPY_CHECK.json`.

Direct finite enumeration is a valid proof because the claim's full domain consists of exactly \(2^{20}\) states, and all operations are deterministic finite integer tests. It is not a proof of any statement about a larger graph family. Run results and full code are supplied rather than only unaudited numerical summaries.

## Relationship to prior work

Folkman's 1967 paper introduced the graph as a regular edge-transitive but nonvertex-transitive example. Kaaser, Mallmann-Trenn and Natale (public preprint 2015-08-14), building on Goles–Olivos, study general convergence to periods at most two and voting-time bounds; their complete text does not treat the Folkman graph or give the particular counts here. Related exact majority computations for the McGee and Nauru graphs, and for the Tutte–Coxeter graph, concern different graph objects and do not imply this labelled Folkman-graph census or its symmetry orbit sizes.

The familiar general period-at-most-two theorem, the graph's construction, and the existence of its semisymmetric group are not claimed as new. The contribution is the complete exact time/period and symmetry census for this specific natural graph, including the separation between late consensus and early oscillatory attraction.

## Limitations

The theorem is finite and specific to the stated 20-vertex graph and synchronous tie-retaining majority. It does not extend the sharp cutoff to arbitrary semisymmetric graphs. Historical-priority investigation cannot exclude a mathematically equivalent unpublished or unindexed enumeration. Full access to Folkman's original article was unavailable; its abstract discusses graph symmetry and construction, not majority dynamics. Independently authored external validation has not been performed.

## References

- J. Folkman, *Regular line-symmetric graphs*, Journal of Combinatorial Theory 3 (1967), 215–232, DOI: 10.1016/S0021-9800(67)80069-3.
- D. Kaaser, F. Mallmann-Trenn, E. Natale, *On the Voting Time of the Deterministic Majority Process*, first posted 2015-08-14, https://arxiv.org/abs/1508.03519.
- E. Goles and J. Olivos, *Comportement périodique des fonctions à seuil binaires et applications*, Discrete Applied Mathematics 3 (1981), 93–105, DOI: 10.1016/0166-218X(81)90034-2.
- E. W. Weisstein, *Folkman Graph*, Wolfram MathWorld, https://mathworld.wolfram.com/FolkmanGraph.html.
