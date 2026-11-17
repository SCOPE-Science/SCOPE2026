# Five periods and two extremal symmetry orbits in Petersen excitation dynamics

## Finding

For synchronous three-state Greenberg–Hastings excitation on the Petersen graph, every one of the \(3^{10}=59049\) labelled initial configurations first reaches periodic behavior in at most six updates. The possible eventual least periods are **exactly** \(1,3,4,5,8\), and the sharp maximal first-entry time is six. There are precisely \(1,80,60,30,60\) primitive periodic orbits, respectively, for those five periods.

Define \(N_{t,p}\) to be the number of initial configurations with first-periodic-entry time \(t\) and eventual least period \(p\). The **complete** joint census is:

| \(t\) | \(p=1\) | \(p=3\) | \(p=4\) | \(p=5\) | \(p=8\) |
|---:|---:|---:|---:|---:|---:|
| 0 | 1 | 240 | 240 | 150 | 480 |
| 1 | 1023 | 140 | 1680 | 4290 | 2400 |
| 2 | 2613 | 580 | 3900 | 9780 | 4320 |
| 3 | 2242 | 1360 | 2400 | 7050 | 1440 |
| 4 | 1960 | 1220 | 1620 | 6000 | 960 |
| 5 | 0 | 840 | 0 | 0 | 0 |
| 6 | 0 | 120 | 0 | 0 | 0 |

Exactly 120 configurations require six updates, and **all of them** eventually have least period three. Under the complete graph automorphism group \(S_5\), these 120 states form **exactly two orbits**, each of size 60. Hence the extremal transient states admit a two-type classification up to graph symmetry. In particular, no configuration has eventual least period six or nine, although the Petersen graph contains cycles of both lengths.

The global map also obeys \(F^{126}=F^6\), since six steps suffice to reach cycles of periods dividing 120. This is an identity on the entire labelled state space, not a claim about an infinite graph family.

## Assumptions and scope

The graph is the simple Petersen graph, realized as the Kneser graph \(KG(5,2)\): vertices are the ten two-element subsets of \(\{0,1,2,3,4\}\), and two vertices are adjacent exactly when their subsets are disjoint. Vertices are labelled in lexicographic order:

```
(0,1), (0,2), (0,3), (0,4), (1,2),
(1,3), (1,4), (2,3), (2,4), (3,4)
```

For a state \(a:V\to\{0,1,2\}\), update all vertices simultaneously by
\[
F(a)(v)=
\begin{cases}
2,&a(v)=1,\\
0,&a(v)=2,\\
1,&a(v)=0\ \text{and some neighbor of }v\text{ has state }1,\\
0,&a(v)=0\ \text{and no neighbor of }v\text{ has state }1.
\end{cases}
\]
State 0 means resting, 1 excited, and 2 refractory. The first-periodic-entry time is the least \(t\ge0\) for which \(F^t(a)\) belongs to a periodic cycle; its eventual least period is the minimum \(p\ge1\) with \(F^{t+p}(a)=F^t(a)\). Count distinct labelled initial configurations, not equivalence classes, except where the two symmetry orbits are explicitly discussed. No external random dynamics or approximation is involved.

## Proof

**Finite-state exhaustion lemma.** For any self-map of a finite set, trace the sequence \(a,F(a),F^2(a),\ldots\) and stop when a state first repeats. If the first recurrence is at index \(t+p\) of the state at index \(t\), then \(t\) is exactly the first periodic-entry time, and \(p\) is exactly the eventual least period. Indeed, the states at indices strictly before \(t+p\) are pairwise distinct; the repeated suffix is a cycle, and an earlier periodic entry would produce an earlier repetition. This argument is exact and does not depend on the trajectory length.

**Exhaustive implementation.** Encode the lexicographically ordered states as integers \(s=\sum_{i=0}^{9}a_i3^i\) from zero through \(59048\). The packaged `verify_exhaustive.py` constructs adjacency from disjointness of the two-subsets and evaluates the displayed update case-by-case for each integer. It constructs the full successor array of length \(59049\). It partitions this entire functional graph into disjoint cycles and their reverse trees, recording the first-entry time and eventual least period at every state. The algorithm maintains a dictionary of positions on each newly traversed route; when it reaches an already classified vertex, it transfers its known period and increments its entry time backwards along the route. In either case, induction backwards on route length proves each recorded value. Every route is finite, every state is visited, and the resulting table is the one displayed above (also in `census.csv`).

The row sum is exactly \(59049\). The nonzero entries in the periodic row \(t=0\) are \(1,240,240,150,480\); dividing by the respective least periods gives precisely \(1,80,60,30,60\) distinct cycles. The rows \(t=5,6\) contain only eventual period-three states, with \(840\) and \(120\) states respectively, proving the sharp six-step upper bound and the exact extremal population. All other entries are zero.

**Symmetry classification of the extremal states.** Permutations of the five ground symbols act as automorphisms of \(KG(5,2)\). Conversely, the five independent vertex sets of size four are precisely the five families of pairs containing a fixed ground symbol. To see that these are the only maximal-cardinality independent sets: four pairwise-intersecting two-subsets must have a common element (if three make a triangle instead, no fourth distinct pair intersects all three). An automorphism must therefore permute these five stars and is determined by this permutation because the stars indexed by two different symbols meet in their unique common pair. Hence the full automorphism group is \(S_5\).

Consider the following two initial states in the displayed vertex order:

\[
\begin{aligned}
a^{(1)}&=(1,2,2,2,1,1,0,0,0,0),\\
a^{(2)}&=(1,2,2,2,2,1,1,0,0,0).
\end{aligned}
\]

Directly applying the displayed rule to either representative gives first-entry time six and least period three. Enumerating the 120 permutations of the ground set, exactly 60 distinct configurations occur in each representative's symmetry orbit (`extremal_orbits.json` and the verifier). The first orbit has color multiplicities \((4,3,3)\) and the second \((3,3,4)\) in the order \((0,1,2)\), so they are disjoint. These two disjoint 60-element subsets lie within the 120 configurations already shown to have first-entry time six; they therefore exhaust that set. This proves both the two-type statement and the orbit sizes.

## Verification

All three packaged programs use only the Python standard library. `verify_exhaustive.py` computes and checks the complete successor map, the first-entry census, the period-one-through-eight orbit counts, the six-step bound, the global identity \(F^{126}=F^6\), and the two symmetry orbits. `verify_independent.py` traces every tuple-state trajectory afresh, without using the first program's successor map or memoized classifications, and checks every nonzero \(N_{t,p}\) plus the two symmetry orbits. `verify_outer_inner.py` redefines the graph independently as an outer pentagon, five spokes and an inner pentagram, and agrees on all eventual periods and each entry-time layer. The recorded results of all programs are included in the package. The exhaustive certificate is a finite mathematical computation: all \(59049\) states are covered, not sampled.

To replay in a directory containing the embedded files, run:

```
python3 verify_exhaustive.py
python3 verify_independent.py
python3 verify_outer_inner.py
```

For direct witnesses, the representatives encoded as base-three integers are 403 and 1213. Their respective integer trajectories first encounter a repeated state after nine updates, with the repeated state first occurring at update six; hence \(t=6\) and \(p=3\).

## Relationship to prior work

The Greenberg–Hastings rule was introduced by Greenberg and Hastings (1978), and excitable automata were studied by Durrett and Griffeath (1993). Gravner, Lyu and Sivakoff (2016 preprint; 2018 journal publication) prove a general characterization of synchronization by a conservative edge form and give a cycle-circulation formula for asymptotic excitation frequency on finite graphs. Those facts apply to the Petersen graph, and are **not** claimed here as new. The present exact joint basin-by-entry-time table, exact period-orbit counts, and two-orbit classification of maximally delayed colorings require a full finite dynamic census beyond those general qualitative criteria.

The Petersen graph's ordinary undirected cycle lengths \(5,6,8,9\), its identification with \(KG(5,2)\), and its automorphism group \(S_5\) are established graph-theoretic facts. No claim is made to their novelty. Instead the absence of dynamical least periods six and nine, despite the presence of graph cycles of those lengths, illustrates why the unweighted cycle-length spectrum alone does not determine excitation periods.

## Limitations

This is an exact result for **one canonical finite graph**, not a formula for all cubic graphs, general Petersen graphs, or arbitrary cycle lengths. The values come from independently replayable exhaustive enumeration together with an explicit group-action proof; they do not establish a non-computational closed-form expression for a larger family. No external independent audit has been performed. Exhaustive coverage establishes correctness of the stated finite census, not priority against every possibly unindexed paper. The historical 1978 full text and the 1993 preprint full text were not obtained; the directly relevant arbitrary-graph theorem was inspected in full accessible text, including its main results and proof discussion.

## References

- J. M. Greenberg and S. P. Hastings, *Spatial patterns for discrete models of diffusion in excitable media*, SIAM Journal on Applied Mathematics **34** (1978), 515–523, DOI: 10.1137/0134040.
- R. Durrett and D. Griffeath, *Asymptotic behavior of excitable cellular automata*, first submitted March 22, 1993, arXiv: patt-sol/9303002.
- J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, first submitted October 24, 2016, arXiv:1610.07320; Annals of Applied Probability **28** (2018), 3324–3357, DOI: 10.1214/17-AAP1350.
- A. E. Brouwer's graph reference, *The Petersen graph*, https://aeb.win.tue.nl/graphs/Petersen.html (description of graph, cycle lengths and full automorphism group).
