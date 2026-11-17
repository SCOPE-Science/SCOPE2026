# Cuboctahedral majority dynamics: an exact basin and three-geometry oscillation census

## Finding

Let \(C=L(Q_3)\) be the cuboctahedral graph, the line graph of the ordinary three-dimensional cube. Give each of its twelve labelled vertices a binary state. At every synchronous step, replace a state by the strict majority of its four neighbors, retaining its previous state when the neighbors split two against two. The following is a **complete finite classification** of its \(2^{12}=4096\) configurations:

* Exactly **146 configurations are fixed**; exactly **20 primitive two-cycle temporal orbits** exist, comprising 40 configurations. There are no longer periods.
* Every configuration is periodic after at most **four** updates, and this bound is sharp. Equivalently, \(F^6=F^4\) on the entire state space. Precisely 96 configurations enter recurrence at update four.
* Every primitive two-cycle has a basin consisting of its two periodic configurations alone. Each of its 40 phase states has **exactly one** immediate predecessor (the other phase). In particular, no nonperiodic configuration ever enters an oscillation.
* Under the full 48-element graph-automorphism group, the fixed configurations form **14 geometric classes**, and the 20 primitive two-cycles form **three geometric classes** of sizes **8, 6, 6**. All cycle phases have Hamming weight six; eight two-cycles flip six vertices per step and twelve flip eight vertices per step.

The exact first-periodic-entry census is:

| Earliest periodic update \(t\) | Eventual fixed point | Eventual primitive two-cycle | Total |
| ---: | ---: | ---: | ---: |
| 0 | 146 | 40 | 186 |
| 1 | 1,606 | 0 | 1,606 |
| 2 | 1,200 | 0 | 1,200 |
| 3 | 1,008 | 0 | 1,008 |
| 4 | 96 | 0 | 96 |
| **Total** | **4,056** | **40** | **4,096** |

The exact distribution of fixed-point **basin sizes** is: eight fixed points have basin size one; twelve have size five; twenty-four size six; forty-eight size eight; twenty-four size ten; twelve size eleven; sixteen size sixty-four; and two (the unanimous states) size 1,032. Both geometric classes of six two-cycles flip eight bits; the class of eight cycles flips six bits.

## Assumptions and scope

Take the eight cube vertices to be integers \(0,\ldots,7\), adjacent when their binary representations differ in one coordinate. Order the twelve cube edges lexicographically:

```text
(0,1),(0,2),(0,4),(1,3),(1,5),(2,3),(2,6),(3,7),(4,5),(4,6),(5,7),(6,7).
```

These edges are the twelve vertices of \(C\). Two vertices of \(C\) are adjacent exactly when the corresponding cube edges share an endpoint. This fixes the labelling and makes each vertex four-regular, with 24 edges overall. The graph is the standard cuboctahedral graph, equivalently the edge-midpoint skeleton of a cube.

A binary state is an integer \(x\) with \(0\le x<4096\), with bit \(i\) representing the state at edge-label \(i\). Define \(c_i(x)\) as the number of occupied neighboring vertices at \(i\). The synchronous map is exactly

\[
(F(x))_i=1\quad\Longleftrightarrow\quad c_i(x)\ge3\quad\text{or}\quad \bigl(c_i(x)=2\text{ and }x_i=1\bigr).
\]

A **temporal orbit** identifies rotation through time but **not** spatial symmetries. A geometric class further identifies the action of a spatial automorphism, with the two phases of a two-cycle considered unordered. The first-periodic-entry time \(T(x)\) is the smallest \(t\ge0\) such that \(F^t(x)\) is periodic. A basin includes all starting states eventually entering that specific temporal orbit.

## Proof

**1. Exact complete transition rule.** The twelve-bit state space contains precisely 4096 integers. The first standalone checker constructs the cube-edge list from bitwise Hamming distance one, then constructs the four-neighbor set of each edge by incidence. For every \(x\in\{0,\ldots,4095\}\) it computes the twelve output bits from the displayed local inequality and stores \(F(x)\). The second checker uses an explicitly written array of twelve four-neighbor bit masks and an independent C++ integer popcount implementation. It checks that these masks are exactly the incidence masks obtained from the cube-edge construction. Thus neither graph labelling nor update convention is implicit.

**2. Recurrent states and the sharp clock.** Both programs inspect every state to check whether \(F^2(x)=x\). They obtain exactly 186 such states, of which precisely 146 satisfy \(F(x)=x\); the remaining 40 split into exactly 20 unordered pairs \(\{x,F(x)\}\). For each of all 4096 starting states they explicitly compute the first \(t\in\{0,1,2,3,4\}\) for which \(F^2(F^t(x))=F^t(x)\). They find the table in the Finding section, including no states outside those five entrance layers. Hence \(F^6(x)=F^4(x)\) for **every** state, ruling out all other eventual periods. State integer `348` has trajectory `348 -> 785 -> 276 -> 256 -> 0 -> 0`, so its first periodic entry is at time four, proving sharpness. This is a finite exhaustive proof, not extrapolation from sampled trajectories.

**3. Exact attraction basins.** Each state's first periodic point is mapped to a canonical orbit key, either the single fixed state or the increasing ordered pair of phases. Counting the 4096 keys gives the fixed-basin size distribution stated above. The two-cycle basin histogram is exactly twenty occurrences of size two. As a direct independent check, the second program computes the indegree of every one of the 4096 vertices in the transition digraph; every one of the 40 two-cycle phase states has indegree one. Its sole predecessor is already forced to be the other phase, so no transient state can enter in one update or in any larger number of updates.

**4. Full spatial symmetry.** Coordinate permutations and coordinate-bit translations of the cube give \(3!\,2^3=48\) distinct automorphisms of \(C\). These are all its automorphisms: the cube has no triangles, and every triangle in its line graph is precisely the set of three cube edges at one cube vertex. Therefore an automorphism of \(C\) permutes the eight such triangles and induces a unique automorphism of the cube. The latter is determined by the image of one vertex (eight choices) and the permutation of its three neighbors (six choices), giving at most 48 possibilities. The first checker constructs all 48, transforms every recurrent state, and repeatedly removes its full orbit. It obtains the 14 fixed-state and three unordered two-cycle geometric classes. The three two-cycle representative pairs (in the stated labelling) and class sizes are `(335,567):8`, `(500,1834):6`, and `(946,1388):6`. These class sizes sum to all 20 temporal two-cycles. Direct bit counts give six occupied vertices in each phase and the claimed flip counts.

This completes all parts of the finite classification.

## Verification

All calculations are exact integer or Boolean computations. From a directory containing the two supplied programs, run:

```sh
python3 verify_cuboctahedron.py
g++ -O2 -std=c++17 -Wall -Wextra -pedantic verify_cuboctahedron_independent.cpp -o check_cuboctahedron
./check_cuboctahedron
```

The supplied output files are the recorded results of running those exact sources. The Python program constructs all 48 geometric symmetries and lists representatives and orbit sizes. The C++ program separately verifies the graph masks, the transition digraph, complete first-entrance table, basin histograms, and unique incoming transitions to oscillator states. The proof concerns **all 4096 states** of this specified finite graph, not an infinite family or a probabilistic sample. The programs require only Python 3 standard library and a C++17 compiler.

## Relationship to prior work

The classical finite-graph period-at-most-two theorem of Goles and Olivos, as reproduced by Benjamini et al. (2014, Section 1), supplies the background guarantee that no longer eventual periods exist; it **does not imply any of the exact numbers**, four-step settling bound, or geometric class sizes here. Benjamini et al. treat infinite unimodular and random graphs, with no cuboctahedral census. Tošić and Agha (2004) emphasize one-dimensional threshold cellular automata and make a broader assertion about incoming transient states to cycles in their Lemma 5. Accordingly, **isolated oscillation by itself is not asserted as an original general principle** here; the new claim is the complete graph-specific numerical and geometric census, independently proved by exhaustive checks.

For nearby finite natural graph calculations, the accessible public records *Dodecahedral majority dynamics: an exact recurrent, basin and symmetry census* and *Thirty geometric recurrent classes and a sharp four-step clock for majority dynamics on the four-cube* treat different graphs and their numerical results do not imply the present line-graph census. The square/cube line-graph relation is used here to define the graph and its automorphism group, not to transfer a pre-existing orbit enumeration. Searches under the names cuboctahedron, line graph of the cube, cube-edge majority and corresponding exact numerical invariants did not locate covering work.

## Limitations

This is an exhaustive result for the single twelve-vertex cuboctahedral graph with **open-neighborhood** synchronous tie-retaining binary majority. It does not classify all line graphs, all four-regular graphs, stochastic updates, minority rules, or larger Archimedean solids. The executable complete-state enumeration is the certificate for the nontrivial integer counts; no paper-and-pencil closed-form enumeration for them is claimed. A broadly worded earlier statement about incoming transients must not be mistaken for a proof of the new full census. Historical priority remains uncertain against unindexed works; no independent external mathematical audit has been performed.

## References

1. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz, and L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, first arXiv version 11 May 2014, arXiv:1405.2486, https://arxiv.org/pdf/1405.2486.
2. P. T. Tošić and G. Agha, *Characterizing Configuration Spaces of Simple Threshold Cellular Automata*, ACRI 2004, pages 861–870, DOI: 10.1007/978-3-540-30479-1_89. Open manuscript: https://osl.cs.illinois.edu/media/papers/tosic-2004-acri-characterizing_configuration_spaces_of_simple_threshold_cellular_automata.pdf.
3. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics 30 (1980), pages 187–189, DOI: 10.1016/0012-365X(80)90121-1.
4. *Dodecahedral majority dynamics: an exact recurrent, basin and symmetry census*, public mathematical research record, 2026.
5. *Thirty geometric recurrent classes and a sharp four-step clock for majority dynamics on the four-cube*, public mathematical research record, 2026.
