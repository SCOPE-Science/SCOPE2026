# Majority oscillation basins on the rhombic-dodecahedral graph

## Finding

On the 14-vertex rhombic-dodecahedral graph (the graph of the rhombic dodecahedron, or the cube-face incidence graph), synchronous binary open-neighbor majority with incumbent tie retention has **46 fixed configurations** and **183 primitive temporal two-cycle orbits** (366 phases). Every one of its \(2^{14}=16{,}384\) labelled binary states becomes periodic within five updates, sharply:

\[
F^7=F^5,\qquad F^6\ne F^4.
\]

The complete first-periodic-entry census is:

| First periodic entry \(t\) | Eventual period one | Eventual period two |
|:--:|--:|--:|
| 0 | 46 | 366 |
| 1 | 2,122 | 4,682 |
| 2 | 3,360 | 1,536 |
| 3 | 2,136 | 480 |
| 4 | 1,368 | 96 |
| 5 | 192 | 0 |
| **Total** | **9,224** | **7,160** |

Under the graph's full group of 48 spatial automorphisms, the 46 fixed states form **six classes**, of cardinalities \(1,12,12,8,12,1\); its 183 unphased primitive two-cycle orbits form **thirteen classes**, of cardinalities \(8,12,1,24,48,12,12,6,12,24,12,4,8\). The 44 nonunanimous fixed configurations have Hamming weights four, seven, or ten; the twelve smallest have weight four. The bipartition-exchange two-cycle has an exact basin of 596 configurations, although the two unanimous fixed configurations each have a basin of 3,362.

## Assumptions and scope

Write cube corners as \(v=(v_0,v_1,v_2)\in\{0,1\}^3\), and the six coordinate-face centers as \((i,b)\) with \(i\in\{0,1,2\}\) and \(b\in\{0,1\}\). Edges connect \(v\) to \((i,v_i)\) and no other pairs. The resulting graph has eight degree-three cube vertices, six degree-four face vertices, 24 edges, and the full octahedral automorphism group of order 48. This is the skeleton of the rhombic dodecahedron and the combinatorial dual of the cuboctahedral graph.

A configuration is a function \(x:V\to\{0,1\}\). The synchronous map \(F\) replaces each degree-three cube color by the majority of its three neighbors. For a degree-four face vertex it chooses the strict neighbor majority when one exists, and otherwise retains its previous color. The first-periodic-entry time is \(\tau(x)=\min\{t\ge0:F^{t+2}(x)=F^t(x)\}\); the eventual period is one or two according as \(F^{\tau(x)+1}(x)=F^{\tau(x)}(x)\) or not. All states, faces, spatial classes, and basins are **labelled**; spatial symmetry is applied only when explicitly counting geometric classes.

## Proof

**Step 1: a six-bit symbol reduction.** Split \(x=(c,a)\), with eight cube bits \(c_v\) and six face bits \(a_{i,b}\). Define

\[
C(a)_v=\mathbf1\!\left\{\sum_{i=0}^2a_{i,v_i}\ge2\right\},
\qquad F(c,a)=(C(a),R(c,a)),
\]

where, on putting \(m_{i,b}(c)=\sum_{v:v_i=b}c_v\),

\[
R(c,a)_{i,b}=\begin{cases}
1,&m_{i,b}(c)\ge3,\\
a_{i,b},&m_{i,b}(c)=2,\\0,&m_{i,b}(c)\le1.
\end{cases}
\]

These formulas are exactly the stated local rule, including the crucial tie case. For a two-periodic state \((c,a)\), put \((c',b)=F(c,a)\). The equations \(F(c',b)=(c,a)\) imply, and are implied by,

\[
 c=C(b),\quad c'=C(a),\quad b=R(C(b),a),\quad a=R(C(a),b).
\]

Hence a complete *finite proof* of the recurrent-state count requires testing only the \(64^2=4{,}096\) ordered face-word pairs \((a,b)\); every accepted pair determines exactly one two-periodic phase \((C(b),a)\). The independent symbol-reduction checker `verify_faces.py` tests exactly these pairs. It returns 412 accepted pairs, of which 46 are fixed and 366 are primitive-two phases. Thus there are precisely \(366/2=183\) two-cycle orbits. No unexamined face or cube assignments remain.

**Step 2: all basins and the sharp five-step clock.** The direct checker `verify_direct.py` constructs the 14 adjacency lists from the cube-face incidence definition and executes the update on every integer bit state from zero through 16,383. For each state it checks successive images until \(F^2(y)=y\), increments exactly one entry in the displayed census, and verifies that the entrance time never exceeds five. It also checks \(F^7(x)=F^5(x)\) for every state and reports the witness \(x=1868\) with the trajectory of bit labels

```
1868, 2355, 1348, 273, 256, 0, 0, 0.
```

Thus \(\tau(1868)=5\) and \(F^6\ne F^4\). The independently written symbol-reduction checker also iterates all \(256\cdot64\) possible mixed-radix initial states, reproducing each entrance-time and basin entry. The two methods implement the local rule differently and do not import shared computed transition tables. The computation is exhaustive for this *fixed finite graph*, not an inference from a growing list of graphs.

Summing the rows proves that 9,224 states eventually fix and 7,160 enter primitive two-cycles. The complete orbit-basin-size histograms (size: number of orbits) are

```
fixed:     13:12, 73:24, 74:8, 3362:2
two-cycle: 2:16, 6:12, 10:6, 14:48, 27:48,
           28:12, 78:24, 139:16, 596:1
```

Their weighted sums are respectively 9,224 and 7,160. The cycle with all eight cube corners colored one and all six face centers colored zero alternates with the reverse shore coloring and has basin 596.

**Step 3: symmetry and small equilibria.** Independent coordinate permutations and independent bit reversals of the three cube coordinates induce \(3!2^3=48\) graph automorphisms. Conversely, an automorphism permutes the six degree-four faces and must preserve their three opposite pairs (the unique face pairs with disjoint neighbor sets); its effect on the eight corners is then forced by their three distinct incident faces. Thus this list is the entire spatial automorphism group. Applying each group element to every fixed state, and to each primitive two-cycle modulo temporal phase, partitions the states into the claimed six and thirteen classes. The direct checker explicitly constructs these 48 permutations, verifies all adjacency relations, and recomputes every class.

If a nonzero fixed configuration contains any occupied cube corner, that corner has at least two occupied face neighbors; conversely each occupied face must have at least two occupied cube neighbors (including the tie-retained case). A nonzero fixed support therefore has at least two vertices from each shore, hence at least four vertices total. A four-vertex fixed support must consist of two face centers on *different* coordinate axes, together with their exactly two common cube corners. There are \(\binom{3}{2}\cdot2^2=12\) choices, all of which satisfy the fixed-point conditions. Color-complementation gives twelve ten-vertex equilibria. The remaining twenty nonunanimous equilibria have size seven, as confirmed by the exact fixed-state symbol enumeration.

## Verification

Run `python3 verify_direct.py` and `python3 verify_faces.py` with Python 3 and the standard library. The expected complete deterministic output is embedded respectively as `direct_output.txt` and `face_output.txt`. Both programs have explicit assertions for the populations, basins and boundary conventions; the direct program also verifies the 48 spatial automorphisms and their classes. `verify_faces.py` obtains all recurrent states by a 4,096-pair equation check before iterating the separate 16,384-state basin test. These constitute two checkable exact finite certificates. No Monte Carlo approximation, floating-point arithmetic, or unproved infinite extrapolation is involved.

## Relationship to prior work

Goles and Olivos established that finite undirected symmetric-threshold networks eventually have period at most two; that general fact is not claimed here. Benjamini and collaborators' 2014 study concerns general finite and infinite graph majority dynamics, unimodularity, and random-graph unanimity. Kaaser and collaborators' 2015 paper studies generic and graph-family voting-time bounds and complexity. Neither inspected work determines the present graph's exact recurrent populations, basin partition, sharp five-step time, or octahedral class census. A prior finite census for the *cuboctahedral graph* addresses the **12-vertex dual**, not this 14-vertex cubic/octahedral incidence graph, and its numerical invariants do not imply those here. Likewise, the 20-vertex *ordinary dodecahedral graph* is a different graph despite its similar name.

The naturally motivated question is how synchronized majority rule behaves when polyhedral duality changes both degree parity and graph size: the six degree-four vertices here retain memory at ties while the eight degree-three vertices do not. The exact eventual oscillation probability \(7160/16384\) and the full basin profile give a concrete dynamical fingerprint for this canonical Catalan-solid graph.

## Limitations

The result is an exact finite classification of this single 14-vertex graph and the specified tie-retaining synchronous update. It does not assert analogous numbers for a family of polyhedra or for asynchronous, weighted, or tie-flipping voting. Computational verification is exhaustive but remains a human-inspectable finite certificate, not an independent formal proof assistant or external audit. No definitive historical-priority certification is claimed; a formerly unindexed graph-specific enumeration could exist. Sources with only a publication year are not used to infer an invented day-level first-publication date.

## References

1. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics 30 (1980), 187–189, DOI: 10.1016/0012-365X(80)90121-1.
2. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz, and L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, first arXiv version dated 2014-05-11, https://arxiv.org/abs/1405.2486.
3. D. Kaaser, F. Mallmann-Trenn, and E. Natale, *On the Voting Time of the Deterministic Majority Process*, first arXiv version dated 2015-08-14, https://arxiv.org/abs/1508.03519.
4. E. W. Weisstein, *Rhombic Dodecahedral Graph*, MathWorld, https://mathworld.wolfram.com/RhombicDodecahedralGraph.html (undated graph description; no claim of earliest public date).
