# The twelve-step majority clock and basin inversion on the flower snark

## Finding

On Isaacs' twenty-vertex flower snark \(J_5\), synchronous binary majority has exactly \(154\) fixed states and \(7{,}397\) primitive temporal two-cycle orbits. All \(2^{20}=1{,}048{,}576\) initial colorings enter a periodic orbit by the sharp twelfth update:
\[
F^{14}=F^{12},\qquad F^{13}\ne F^{11}.
\]
Exactly \(240\) states first enter their eventual two-cycle at the twelfth update. The two-cycle basins collectively contain \(874{,}268\) states; the two unanimous fixed states each attract exactly \(85{,}522\). The complete first-entry/period census is:

| First periodic entry \(t\) | Eventually fixed | Eventually two-periodic |
|---:|---:|---:|
| 0 | 154 | 14,794 |
| 1 | 2,794 | 117,934 |
| 2 | 20,640 | 185,940 |
| 3 | 37,680 | 151,440 |
| 4 | 39,180 | 147,060 |
| 5 | 25,080 | 95,700 |
| 6 | 24,660 | 75,960 |
| 7 | 19,680 | 38,520 |
| 8 | 4,260 | 26,400 |
| 9 | 180 | 12,000 |
| 10 | 0 | 7,200 |
| 11 | 0 | 1,080 |
| 12 | 0 | 240 |
| **Total** | **174,308** | **874,268** |

The entire individual-basin-size spectrum is listed as the exact `basin_spectrum` array in `evidence/peeling_output.json`; the independent checker prints the same spectrum. A particularly informative comparison is with the twenty-vertex cubic dodecahedral graph: the flower snark has fewer two-cycles (\(7{,}397<9{,}679\)) but more initial states eventually oscillating (\(874{,}268>860{,}448\)) and a longer maximum transient (\(12>7\)).

## Assumptions and scope

The graph is the standard \(J_5\), defined explicitly without a graph library. Let its vertices be \(a_i,b_i,c_i,d_i\), indexed by \(i\in\mathbb Z/5\mathbb Z\). Join \(a_i\) to \(b_i,c_i,d_i\); join the \(b_i\) in a five-cycle; join \(c_0,c_1,c_2,c_3,c_4,d_0,d_1,d_2,d_3,d_4\) in one ten-cycle. It is connected, cubic, and has twenty vertices and thirty edges. For reproducibility the bit numbers are \(a_i=i\), \(b_i=5+i\), \(c_i=10+i\), \(d_i=15+i\), for \(0\le i\le4\).

A configuration is a binary vector, encoded as an integer \(x\in\{0,\dots,2^{20}-1\}\). With all vertices updating simultaneously,
\[
F(x)_v=\mathbf1\Bigl\{\sum_{u\sim v}x_u\ge2\Bigr\}.
\]
There are no ties, since every vertex has three neighbors. A temporal orbit is counted once under cyclic time translation but not under graph automorphisms. The first periodic-entry time \(\tau(x)\) is the least nonnegative \(t\) such that \(F^t(x)\) lies on a temporal cycle. Its eventual orbit's basin includes the entire set of predecessors at all entrance times. The claim concerns this single finite graph, not all flower snarks.

## Proof

**1. Finite, complete transition computation.** In `code/check_peeling.py`, the graph is assembled using four disjoint families of explicit edges, independently of external graph packages. Each resulting adjacency mask is verified to have bit count three. For every integer configuration \(0\le x<2^{20}\), the program computes every bit of \(F(x)\) from the three-neighbor majority rule and stores the entire successor map.

**2. Exact classification by indegree elimination.** In the functional directed graph, each state has precisely one outgoing edge. Repeatedly remove zero-indegree vertices, recording removal order. The remaining vertices are exactly those on directed cycles: any cycle is protected against removal, while every noncyclic vertex has a finite forward distance to a cycle and is removed inductively. Follow each remaining cycle once to establish its least period and canonical orbit representative, then traverse removed states in reverse order to propagate the unique eventual orbit and exact entrance time. Every integer in the input interval is visited. The result is \(154\) period-one orbits, \(7{,}397\) period-two orbits, no longer cycles, and the displayed complete basin and entry table.

**3. Independent forward-dynamics verification.** In `code/check_forward.cpp`, a separate C++17 implementation constructs the twenty-vertex graph from a distinct sequence of edge additions, and uses the independent Boolean-majority formula \((a\land b)\lor(a\land c)\lor(b\land c)\). Starting separately from **every** state, it walks forward until it first satisfies \(F^2(z)=z\); it directly determines the least period, time, and canonical orbit. It does not use zero-indegree stripping or the first implementation's graph data. The complete first-entry and individual-basin spectra agree exactly. It independently verifies the headline numbers through assertions.

**4. Sharpness.** Integer initial state `7581` follows the exact sequence

```
7581, 540548, 7580, 539524, 5532, 535428, 5528,
535300, 5272, 534788, 5256, 10500, 4232, 8452, 4232
```

The states at times twelve and fourteen agree, while those at times eleven and thirteen differ. This witnesses an entrance time of twelve. Exhaustive classification of every starting state establishes the global upper bound, hence the identity \(F^{14}=F^{12}\) and its sharpness.

## Verification

All code uses exact integers. Execute in an extracted directory:

```
python3 code/check_peeling.py > peeling_replay.json
g++ -std=c++17 -O2 code/check_forward.cpp -o forward_check
./forward_check > forward_replay.txt
```

The code and captured output files `evidence/peeling_output.json` and `evidence/forward_output.txt` are included. The first implementation lists the exact twenty neighborhood masks, all \(23\) nonzero first-entry/period cells, and every attractor-basin size with multiplicity. The second prints exactly the same entry and basin distributions from independently constructed transitions. The finite exhaustive checks establish the exact result, not an inference from a partial numerical sample.

## Relationship to prior work

The general eventual-period-at-most-two property for finite symmetric majority networks is classical (Goles and Olivos, 1980), and explicitly described by Benjamini et al. (first posted 11 May 2014). This general fact does **not** count flower-snark attractors or determine relaxation and basin spectra. The graph family itself is due to Isaacs (1975). An earlier complete computation on the dodecahedral graph gives \(118\) fixed states, \(9{,}679\) two-cycle orbits, \(860{,}448\) eventual two-cycle initial states, and sharp transient length seven; it is a different cubic graph and supplies a meaningful same-size baseline but does not imply the new flower-snark census. The result here is the graph-specific complete classification and the reverse ordering of orbit populations and basin masses.

## Limitations

This is a finite, computer-assisted exhaustive theorem for \(J_5\), not an analytical classification for arbitrary \(J_n\). Its exact assertions depend on the stated explicit graph and update convention. Neither an unperformed independent external audit nor an exhaustive historical bibliography is claimed; unindexed earlier tabulations could exist. The cited old sources give the graph definition and general dynamics, not the new numerical table. The independent cross-check uses a different algorithm but is not a formal proof assistant.

## References

1. R. Isaacs, *Infinite Families of Nontrivial Trivalent Graphs Which Are Not Tait Colorable* (1975); background and explicit construction at https://mathworld.wolfram.com/FlowerSnark.html and https://en.wikipedia.org/wiki/Flower_snark .
2. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics 30 (1980), 187–189, DOI: 10.1016/0012-365X(80)90121-1.
3. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz, L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, first posted 2014-05-11, https://arxiv.org/pdf/1405.2486 .
4. *Dodecahedral majority dynamics: an exact recurrent, basin and symmetry census*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-dodecahedral-majority-dynamics-an-exact-recurrent-basin-and-symm--095dfb0decea .
