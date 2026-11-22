# A sharp six-update majority clock and complete basin census on the Bidiakis cube

## Finding

Consider the 12-vertex Bidiakis cube with the standard Hamiltonian LCF description `[-6,4,-4]^4`. At every simultaneous update each vertex replaces its binary opinion by the strict majority of its three neighbors. There are exactly **20 fixed configurations and 103 primitive two-cycle orbits**. The sharp first-periodic-entry cutoff is six updates, or equivalently \(F^8=F^6\) on all \(2^{12}=4096\) initial configurations, while \(F^7\ne F^5\) as maps.

The exact first-periodic-entry population, where entry time zero means the state is already periodic, is:

| First periodic entry \(t\) | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Number of labelled states | 226 | 1226 | 1364 | 608 | 408 | 216 | 48 |

The **complete individual attraction-basin spectrum** follows. For each period, the listed pair means `(basin size, number of temporal orbits with that basin size)`:

- Fixed points: `(1,8), (3,2), (6,8), (392,2)`.
- Primitive two-cycles: `(2,27), (4,8), (6,28), (7,8), (13,8), (18,2), (26,8), (138,8), (192,4), (360,2)`.

Each unanimous fixed point has a basin of size 392. Under all eight spatial graph automorphisms, the 20 fixed points form exactly seven classes (orbit-size multiplicities `(1,2), (2,1), (4,4)`), and the 103 temporal two-cycles form exactly 29 classes (orbit-size multiplicities `(1,3), (2,6), (4,18), (8,2)`). The fixed-state Hamming-weight census is `(0,1), (4,4), (5,4), (6,2), (7,4), (8,4), (12,1)`.

## Assumptions and scope

This is a *finite, fully enumerated theorem* for a specified labelled 12-vertex graph, not a statement about arbitrary cubic graphs. Vertices are \(0,1,\dots,11\) with indices modulo 12. Let \(d=(-6,4,-4,-6,4,-4,-6,4,-4,-6,4,-4)\). The edges are the undirected cyclic edges \(\{i,i+1\}\) and the undirected LCF chords \(\{i,i+d_i\}\), duplicates counted only once, giving precisely 18 edges, all vertices degree three. States are \(x\in\{0,1\}^{12}\) and
\[
F(x)_i=\mathbf 1\!\left\{\sum_{j\sim i}x_j\ge2\right\}.
\]
A temporal orbit is counted once regardless of its phase. The first periodic-entry time is the least nonnegative integer \(t\) for which \(F^t(x)\) belongs to a periodic orbit. A basin of one orbit consists of all initial configurations eventually entering that orbit. A spatial class is an orbit of temporal orbits under the automorphism group of the labelled graph.

## Proof

An exact finite exhaustive computation suffices because the state space has cardinality \(2^{12}=4096\). Two independent standalone algorithms check the complete claims rather than sampling. Their key logically exhaustive steps are:

1. `check_majority_a.py` constructs the graph from its LCF chord rule, checks 18 distinct edges and degree three everywhere, and explicitly constructs the successor of every integer-encoded binary state by bit-counting its neighbors. Each state appears exactly once in this successor array.
2. It deletes indegree-zero states repeatedly from the finite functional digraph. Every state surviving this elimination lies on a directed cycle: a finite functional digraph with no indegree-zero vertices is a disjoint union of cycles. Reversing the deletion order therefore gives exactly the cycle reached, the first-entry depth and the orbit basin for every deleted state. Cycle traversal yields 20 singleton cycles and 103 two-cycles, and no cycles of other lengths. The resulting depths and basin sizes are precisely those in the tables.
3. The same script exhausts all vertex bijections compatible with adjacency through injective partial mappings. It finds eight automorphisms; applying them to each temporal cycle gives seven fixed and 29 two-cycle spatial classes with the listed size multiplicities. This last step is a complete finite group-orbit enumeration.
4. `check_majority_b.py` instead constructs the graph from a fixed, explicit 18-edge list. It represents each state as a 12-entry tuple and evaluates majority as the Boolean disjunction of the three possible neighbor pairs. From each of all 4096 initial tuples it traces until the first repeated tuple and canonicalizes the period by temporal rotation. The independently obtained entry-time and complete basin-size spectra agree term for term.

For sharpness, the integer-encoded initial state \(x=59\) has the six-step trajectory \(59,118,43,86,41,82,33,66,33,\dots\). Its first repeated state is \(33\), entered at time six, and the terminal temporal orbit is \(33\leftrightarrow66\). Thus the upper bound six is attained; the 48 last-entry states in the census give an independent population certificate. In particular, \(F^8=F^6\) but \(F^7\ne F^5\).

## Verification

From the directory containing the two supplementary scripts, run:

```
python3 check_majority_a.py
python3 check_majority_b.py
```

Both use Python 3 standard-library modules only, no graph database or hidden inputs. Each contains assertions for the central exact populations; the first additionally asserts all spatial class counts, and the second tests the sharp six-step witness. On successful execution both print `PASS`. All 4096 input configurations are tested, not a subset. The independent method diversity is LCF/bitset/functional-graph pruning versus explicit-edge/tuple-state/direct trajectory tracing.

## Relationship to prior work

The general period-one/period-two conclusion follows from classical majority-dynamics theory discussed in Benjamini et al. (first preprint 2014) and Kaaser, Mallmann-Trenn and Natale (first preprint 2015), but a general period bound does not determine the graph-specific orbit numbers, transient depths, attraction-basin spectra, or symmetry classes here. The standard LCF representation of the Bidiakis cube is documented by Maple's graph-theory reference. The new assertion is an exact finite classification for this particular cubic polyhedral network, not the general period-two theorem itself.

## Limitations

All conclusions pertain to the specified Bidiakis cube and its strict simultaneous neighbor-majority rule. The argument is a mathematically exhaustive finite certificate supported by executable source, not a symbolic formula for general graph families. Independent external audit has not been performed. No claim of definitive historical priority is made; unindexed earlier equivalent computations remain possible.

## References

- I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz and L.-Y. Tan, *Convergence, Unanimity and Disagreement in Majority Dynamics on Unimodular Graphs and Random Graphs*, first arXiv version May 11, 2014, https://arxiv.org/abs/1405.2486 .
- M. Kaaser, G. Mallmann-Trenn and E. Natale, *On the Voting Time of the Deterministic Majority Process*, first arXiv version August 14, 2015, https://arxiv.org/abs/1508.03519 .
- Maplesoft, *GraphTheory/SpecialGraphs/LCFGraph*, standard Bidiakis cube Hamiltonian LCF representation, https://de.maplesoft.com/support/help/maple/view.aspx?path=GraphTheory/SpecialGraphs/LCFGraph .
