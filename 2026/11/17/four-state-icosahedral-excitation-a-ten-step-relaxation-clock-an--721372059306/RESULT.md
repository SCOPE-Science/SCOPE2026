# Four-state icosahedral excitation: a ten-step relaxation clock and two extremal symmetry classes

## Finding
Consider synchronous four-state threshold-one Greenberg–Hastings excitation on the ordinary labelled icosahedral graph \(I\) with twelve vertices. Its update map \(F\) obeys the all-state identity
\[
F^{14}=F^{10}.
\]
There is exactly one fixed state, exactly \(835400\) primitive-period-four states in \(208850\) distinct temporal orbits, and **no other primitive periods**. Exactly \(3620436\) of the \(4^{12}=16777216\) labelled starting states eventually become completely resting; the remaining \(13156780\) enter a primitive four-cycle.

The maximum first periodic-entry time is **ten updates**, attained by exactly \(240\) states. Under the full icosahedral automorphism group of order \(120\), the \(240\) maximally delayed states form precisely two geometric orbits of size \(120\), represented by base-four codes \(75769\) and \(441799\) in the vertex order defined below.

The full joint census of first-entry time \(\tau\) and eventual primitive period \(p\) is:

| \(\tau\) | \(p=1\) | \(p=4\) |
|---:|---:|---:|
| 0 | 1 | 835400 |
| 1 | 4095 | 652540 |
| 2 | 527345 | 1729120 |
| 3 | 1053937 | 2875740 |
| 4 | 918588 | 3279180 |
| 5 | 737818 | 2228520 |
| 6 | 359782 | 1225680 |
| 7 | 18810 | 315660 |
| 8 | 60 | 13020 |
| 9 | 0 | 1680 |
| 10 | 0 | 240 |

## Assumptions and scope
Vertices are \(0,1,\ldots,11\). Vertex \(0\) is adjacent to each of \(1,\ldots,5\), and vertex \(11\) to each of \(6,\ldots,10\). Put \(U_i=1+i\), \(L_i=6+i\) for \(i\in\mathbb Z/5\mathbb Z\). The other edges are \(U_iU_{i+1}\), \(L_iL_{i+1}\), \(U_iL_i\), and \(U_iL_{i-1}\). Thus the graph is simple, connected, has thirty edges, and every vertex has degree five.

A state is \(x\in\{0,1,2,3\}^{12}\), with state \(0\) resting, state \(1\) excited, and states \(2,3\) successively refractory. All vertices update **simultaneously**:
\[
(Fx)_v=\begin{cases}
1,&x_v=0\text{ and some adjacent }u\text{ has }x_u=1,\\
0,&x_v=0\text{ and no adjacent }u\text{ has }x_u=1,\\
x_v+1\pmod4,&x_v\in\{1,2,3\}.
\end{cases}
\]
The first-entry time \(\tau(x)\) is the least nonnegative integer \(t\) for which \(F^t(x)\) is periodic. A temporal orbit counts its four phase positions only once. Geometric equivalence of states means equality after a graph automorphism (not a time shift or arbitrary permutation of the local states). Codes use \(\operatorname{code}(x)=\sum_{v=0}^{11}x_v4^v\).

## Proof
**1. Recurrent-state structure.** A state on a nonconstant cycle of length dividing four must contain an excited vertex at some phase: otherwise all initially refractory vertices become resting in at most three steps and no excitation can recur. A vertex that is ever excited necessarily follows the four successive local states \(1,2,3,0\); periodicity with period dividing four then forces this vertex to rotate through all four states on every update. An adjacent vertex cannot remain permanently resting, since it would be excited whenever the rotating vertex equals one. On a periodic cycle a vertex with a nonzero state at any time must itself rotate. Connectivity therefore forces *every* vertex to rotate. Consequently any nonconstant recurrent cycle of period dividing four has primitive period exactly four and satisfies \(F(x)=x+1\pmod4\).

A configuration has this synchronous four-phase rotation if and only if every vertex \(v\) has at least one neighbor of color \(x_v+1\pmod4\). Necessity follows by observing the update at the phase when \(v\) is resting; sufficiency follows by applying the update simultaneously to all vertices. This local successor-neighbor condition provides a static count independent of orbit traversal.

**2. Complete transient certificate.** The `icosahedron_census.cpp` program constructs the thirty edges from the specified geometric rule, checks all degrees, and enumerates exactly the integer codes \(0\le k<4^{12}\), producing one transition \(F(k)\) per code. It then computes indegrees, peels all nonrecurrent states, traverses the remaining cycles and propagates their periods and first-entry depths backwards along the peeled sequence. The resulting values are exactly those in the table, with largest depth ten. This is exhaustive because each twelve-digit base-four word corresponds bijectively to one integer in that range; peeling a finite functional digraph leaves exactly its directed cycles.

Independently, `icosahedron_direct.cpp` specifies the graph through twelve literal five-neighbor lists and directly forms the fifteen iterates \(F^0(x),\ldots,F^{14}(x)\) for **every** base-four code. It verifies \(F^{10}(x)=F^{14}(x)\) for every code and finds the least \(0\le t\le10\) with \(F^t(x)=F^{t+4}(x)\). At this time the primitive period is one exactly if \(F^t(x)=F^{t+1}(x)\), otherwise four. These direct counts match every table entry and show that the asserted map identity holds globally, not merely on a sample. The first-entry time cannot exceed ten; its sharpness follows from the nonzero final row and the displayed representative codes. Both algorithms are included in full, together with their actual outputs.

**3. Independent recurrent census.** The `icosahedron_phase.cpp` program independently enumerates the entire base-four state space, constructs four color-class bit masks, and tests the local successor-neighbor condition from step 1. Exactly \(835400\) states satisfy it; each primitive cycle has four distinct states, giving \(835400/4=208850\) temporal cycles. The all-resting configuration is the only fixed state, since a fixed state cannot contain a nonzero local value. Summing the period-one and period-four columns of the table yields the respective basin populations \(3620436\) and \(13156780\).

**4. Exhaustive symmetry quotient of the extremal layer.** For each vertex the induced graph on its five neighbors is a cycle of length five. Any graph automorphism is determined by the image of the distinguished vertex \(0\) (twelve choices) and the image of the oriented neighbor cycle (at most ten choices), because each lower-ring vertex is the unique common neighbor other than the apex of the corresponding two consecutive upper-ring vertices, and the remaining vertex is the opposite apex. Hence the automorphism group has size at most \(120\). The pure-Python verifier `symmetry_extremal.py` constructs exactly \(12\cdot10=120\) distinct adjacency-preserving permutations in this way, so these are the entire automorphism group. It applies every permutation to every maximal-delay state obtained by the direct census, checks that all images remain in that layer, and partitions all \(240\) states into the two full-size classes represented above. This proves the stated symmetry classification.

## Verification
Replay from the standalone files in a single directory:

```sh
g++ -O3 -std=c++17 icosahedron_census.cpp -o census
./census > census_output.txt
g++ -O3 -std=c++17 icosahedron_direct.cpp -o direct
./direct > direct_output.txt
g++ -O3 -std=c++17 icosahedron_phase.cpp -o phase
./phase > phase_output.txt
python3 symmetry_extremal.py > symmetry_output.txt
```

The package includes the corresponding recorded outputs named `icosahedron_census_output.txt`, `icosahedron_direct_output.txt`, `icosahedron_phase_output.txt` and `symmetry_extremal_output.txt`, as well as the full `extremal_codes.txt` list produced by the direct checker. All three C++ programs and the dependency-free Python verifier were run on the standalone source files. The indegree, direct-iterate, and static phase-condition approaches return identical recurrent counts; the indegree and direct-iterate approaches agree on all time/period cells. The symmetry verification returns exactly two 120-element extremal classes. The computations use only integers and exhaust all \(16777216\) states; no floating-point or random estimate is used.

## Relationship to prior work
The Greenberg–Hastings model and cyclic cellular automata were established in the classical excitable-media literature; Durrett and Griffeath (1993) formulate multi-state systems, including thresholds and stable periodic objects, principally in lattice settings. Gravner, Lyu and Sivakoff (2016) give a three-color graph theory of excitation and synchronization, while Doba (2018) proves graph-level results for the **three-valued** model. Those sources supply definitions and qualitative context, not the four-state icosahedral all-state identity and counts reported here.

The closest published graph-specific study, *Icosahedral excitation: exact three-cycle, geometric-orbit, and six-step entrance census* (2026), treats **three states** on the same graph: it has a six-step cutoff and a single geometric class of sixty maximally delayed configurations. Here the addition of a second refractory state leads instead to a ten-step cutoff and two maximal-delay spatial classes, each of size 120. The comparison is of exact dynamical statements, not merely different paper titles. Published four-state excitation work on complete multipartite graphs concerns different adjacency and cannot imply the present icosahedral census directly.

## Limitations
This is a finite exact graph classification, not a formula for an infinite family of polyhedral graphs. The sharp time cutoff, class populations and symmetry counts rely on reproducible complete enumeration of a finite state space, rather than a shorter conceptual proof of the ten-step bound. The local four-phase condition gives an independent conceptual characterization of recurrent configurations, but does not alone bound transient length. The result does not cover stochastic excitation, different thresholds, asynchronous updates, or a different graph. An unindexed earlier exact four-state icosahedral table cannot be ruled out, and no independent external mathematical audit is claimed.

## References
1. R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, arXiv:patt-sol/9303002, first publicly posted 1993-03-22. https://arxiv.org/abs/patt-sol/9303002
2. J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320, first publicly posted 2016-10-24, especially Theorem 3. https://arxiv.org/abs/1610.07320
3. N. Doba, *The Time Evolution of a Greenberg–Hastings Cellular Automaton on a Finite Graph*, Complex Systems 27 (2018), 101–126. https://wpmedia.wolfram.com/sites/13/2018/09/27-2-1.pdf
4. *Icosahedral excitation: exact three-cycle, geometric-orbit, and six-step entrance census*, published 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-icosahedral-excitation-exact-three-cycle-geometric-orbit-and-six--6295ce972482
