# Four- and six-cycles distinguish two arc-transitive quartic excitable networks

## Finding
Let \(C\) be the cuboctahedral graph \(L(Q_3)\), the line graph of the three-dimensional cube. Let \(B\) be the twelve-vertex circulant on \(\mathbb Z/12\mathbb Z\) joining vertices whose difference is \(\pm1\) or \(\pm5\). Both are connected, simple, four-regular, arc-transitive graphs with twelve vertices and 24 edges. Consider the synchronous **three-state Greenberg--Hastings rule with threshold two**: states \(1\) and \(2\) become \(2\) and \(0\), respectively; state \(0\) becomes \(1\) precisely when at least two of its four neighbors are in state \(1\). Otherwise it remains \(0\).

Every one of the \(3^{12}=531441\) labelled configurations on either graph becomes periodic within at most six updates; six is sharp on both. The only eventual periods on \(C\) are \(1,3\), whereas those on \(B\) are \(1,3,4,6\). Their full individual-attractor basin spectra are:

| Graph | Least period | Number of primitive temporal orbits | Basin size **per orbit** |
|---|---:|---:|---:|
| \(C=L(Q_3)\) | 1 | 1 | 531417 |
| \(C=L(Q_3)\) | 3 | 8 | 3 |
| \(B=C_{12}(1,5)\) | 1 | 1 | 500055 |
| \(B=C_{12}(1,5)\) | 3 | 2 | 3 |
| \(B=C_{12}(1,5)\) | 4 | 32 | 180 |
| \(B=C_{12}(1,5)\) | 6 | 2 | 12810 |

All other least periods and basin sizes are absent. In particular, the cuboctahedral graph has no transient state attracted to a nontrivial period, while the circulant has precisely \(31386\) initial states eventually oscillating. Under independent uniform random initial states, the respective eventual oscillation probabilities are \(8/177147\) and \(10462/177147\). This distinguishes their nonlinear dynamics despite identical order, size, degree and arc-transitivity.

## Assumptions and scope
The graphs have **no loops, no weights and no random updating**. On \(B\), vertices are labelled \(0,1,\ldots,11\), and \(i\sim j\) iff \(j-i\pmod{12}\in\{1,5,7,11\}\). On \(C\), index the eight cube vertices by three-bit integers \(0,\ldots,7\). The 12 vertices of \(C\) are the ordered-by-first-then-second list of pairs \((u,v)\) with \(u<v\) and the binary Hamming distance from \(u\) to \(v\) equal to one. Two such pairs are adjacent iff they share a cube endpoint. Both specifications give 12 vertices, four neighbors per vertex, and 24 undirected edges.

For any initial configuration \(x\), let \(\tau(x)\) be the least nonnegative time such that the state at time \(\tau(x)\) belongs to a periodic temporal orbit; let \(p(x)\) be the least positive period of that orbit. The basin of an orbit is the set of all initial states eventually entering it, including every periodic phase. Spatially relabelled configurations and distinct temporal phases are counted separately; only rotations within one temporal cycle are quotiented when counting primitive orbits. Every displayed number is exact for these two **fixed finite graphs**, not a statement about arbitrary four-regular graphs or larger graphs.

Arc-transitivity follows directly from the explicit graphs. Cube bit flips and permutations of its three bit coordinates act transitively on ordered incident pairs of cube edges, hence on arcs of \(L(Q_3)\). Translations of \(\mathbb Z/12\mathbb Z\), together with multipliers \(-1\) and \(5\), act transitively on the four neighbor directions in \(B\). The two graphs are nonisomorphic: \(C\) contains triangles, while \(B\) is bipartite. Moreover, \(B\) has six twin classes \(\{i,i+6\}\) for \(i=0,\dots,5\), whose quotient is a six-cycle with each quotient edge replaced by a complete bipartite \(K_{2,2}\).

## Proof
**Finite-state encoding and complete successor map.** Every initial state has one and only one code
\[
s=\sum_{i=0}^{11}x_i3^i,\qquad 0\le s<531441.
\]
For each graph, `census_walk.cpp` constructs all 531441 successor codes by reading the four specified neighbors of each vertex, then traverses the **entire** outdegree-one state graph. When it reaches an already classified state, it propagates depth and eventual period backwards; when it first closes a previously unvisited directed circuit, it records that circuit's exact least period and propagates the classification backwards. An accumulator for each circuit counts its entire basin. The code never uses random trials, a time cutoff, a conjectured period list or a bound inferred from incomplete enumeration.

**Independent whole-space certificate.** `census_kahn_check.cpp` constructs the same graphs by a separate adjacency-matrix procedure and computes updates from excited/refractory bit masks. It obtains each state indegree, removes all indegree-zero states in a queue and follows every surviving directed cycle. In a finite functional graph, the unremoved vertices are exactly its disjoint directed cycles; reversing the removal order assigns \(\tau(x)=1+\tau(Fx)\) and \(p(x)=p(Fx)\) to each removed vertex. The second program thereby computes every orbit and every individual basin independently of first-visit trajectory detection. Both programs count all 531441 states per graph and agree on every aggregate below and the basin-size multiplicities. Since the graph, transition and complete state domain are explicit and the loops cover them without exceptions, this provides a finite exhaustive proof; no finite sample is being extrapolated to an infinite family.

**Period/time census.** The exact numbers \(\#\{x:\tau(x)=t,\ p(x)=p\}\) are as follows (omitted entries equal zero):

| \(t\) | \(C,p=1\) | \(C,p=3\) | \(B,p=1\) | \(B,p=3\) | \(B,p=4\) | \(B,p=6\) |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 1 | 24 | 1 | 6 | 128 | 12 |
| 1 | 4095 | 0 | 4095 | 0 | 896 | 756 |
| 2 | 106767 | 0 | 120103 | 0 | 4736 | 8448 |
| 3 | 315390 | 0 | 229514 | 0 | 0 | 16356 |
| 4 | 102176 | 0 | 120152 | 0 | 0 | 48 |
| 5 | 2916 | 0 | 17598 | 0 | 0 | 0 |
| 6 | 72 | 0 | 8592 | 0 | 0 | 0 |

The sum in each graph is \(531441\). The unique fixed point is all zero, since states 1 and 2 cannot themselves remain fixed. Summing all basins on \(C\) gives \(531417+8\cdot3=531441\); on \(B\), it gives \(500055+2\cdot3+32\cdot180+2\cdot12810=531441\). Rows with \(t=6\) are nonempty for both graphs, establishing sharpness. The possible temporal lengths and exact orbit counts follow from the surviving directed circuits, not from observing a truncated trajectory.

**Structural cross-check using the twin quotient of \(B\).** Because \(i\) and \(i+6\) have identical open neighborhoods, their pair-colour histogram is one of the six triples \((2,0,0),(0,2,0),(0,0,2),(1,1,0),(1,0,1),(0,1,1)\). Its update depends only on the two neighboring pair histograms along the quotient six-cycle. If \(r\) excited vertices occur in those neighboring pairs, the histogram \((a,b,c)\) maps to \((c,a,b)\) for \(r\ge2\) and \((a+c,0,b)\) otherwise. A signature with histogram \((a,b,c)\) has \(2!/(a!b!c!)\) distinct labelled realizations. Hence all \(6^6=46656\) signatures together have weight \(3^{12}\). The independent `verify_twin_quotient.py` enumerates those signatures, follows the quotient dynamics, and checks the actual return of a canonical labelled lift. This latter check is necessary: all quotient two-cycles lift to labelled **four-cycles**, not to two-cycles. The weighted labelled joint census exactly matches the table from both full-state algorithms. The quotient is a further proof check on the circulant counts, not a claim that quotient periods always equal labelled periods.

## Verification
Within the directory containing these files, run:

```sh
c++ -std=c++17 -O3 census_walk.cpp -o walk
./walk > walk_census.txt
c++ -std=c++17 -O3 census_kahn_check.cpp -o check
./check > kahn_census.txt
python3 verify_twin_quotient.py > twin_quotient.txt
```

The two C++ outputs provide the same first-entry/period table and basin-size histogram, with differing but equivalent presentation and a common state total. `twin_quotient.txt` ends in `PASS` and reproduces every circulant joint count. No external data files, packages, web access or unspecified code dependencies are used by these verifiers beyond C++17 and Python 3. The certificates are the source programs and their explicitly justified exhaustive algorithms; the output text alone is not a proof.

## Relationship to prior work
The three-state Greenberg--Hastings rule and contact thresholds are classical; Durrett and Griffeath's 1993 paper studies threshold/range-dependent oscillations primarily on lattices, rather than these two finite quartic state graphs. Existing published results identify proper three-edge-colourings of connected cubic graphs with initially primitive-three excitation of their line graphs, which **already determines** the 24 immediate three-periodic states on \(C=L(Q_3)\). Another published half-degree rigidity result characterizes the initially primitive-three configurations of arbitrary connected even-degree regular graphs through balanced proper colourings. Neither result states or determines the entire transient/orbit/basin spectrum or the additional four- and six-periodic circulant orbits. The 2016 arbitrary-graph activity paper studies the one-contact rule; its stated criteria do not imply the present two-contact results. Published threshold-two biclique and tripartite classifications do not directly cover the circulant, which is neither a complete biclique nor a complete tripartite graph, or the cuboctahedral line graph. The two particular quartic symmetric graphs and their automorphisms are classical, not new objects; an existing graph census identifies this pair as the two arc-transitive quartic graphs at twelve vertices.

## Limitations
This is a **finite, computer-exhaustive theorem**, with a full explicit domain of \(2\cdot3^{12}\) input configurations. It does not give closed formulas for larger graph families, claim general results for quartic graphs, or prove an undecidability/complexity statement. Some of the period-three component is already implied by the preceding colouring theorems, so novelty rests on the complete temporal/basin spectra and their contrast, particularly four- and six-cycles on the circulant and their basin sizes. The search does not prove absolute historical priority; specialized unindexed tables and additional source material might overlap. The results have not undergone independent external mathematical audit.

## References
1. R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, first public preprint 1993-03-22, arXiv:patt-sol/9303002, https://arxiv.org/abs/patt-sol/9303002; historical full text https://services.math.duke.edu/~rtd/reprints/paper79.pdf.
2. J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, first preprint 2016-10-24, arXiv:1610.07320, https://arxiv.org/abs/1610.07320 (one-contact model).
3. W. Joyner, *Quartic graphs with 12 vertices*, 2020-10-13, https://yetanothermathblog.com/2020/10/13/quartic-graphs-with-12-vertices/ (graph classification and symmetry).
4. *Tait colourings as primitive-three excitation on cubic line graphs, with a constant-six seam law*, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-tait-colourings-as-primitive-three-excitation-on-cubic-line-grap--c4fb511b080a/RESULT.md (existing period-three classification).
5. *Half-degree rigidity and a sharp contact-threshold collapse on squared cycles*, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-half-degree-rigidity-and-a-sharp-contact-threshold-collapse-on-s--7c3fe196f42d/RESULT.md (existing balanced-colouring criterion).
6. J. Bello and D. Sivakoff, *Cyclic Cellular Automata and Greenberg-Hastings Models on Regular Trees*, arXiv:2108.06404, https://arxiv.org/abs/2108.06404 (higher thresholds on infinite trees).
