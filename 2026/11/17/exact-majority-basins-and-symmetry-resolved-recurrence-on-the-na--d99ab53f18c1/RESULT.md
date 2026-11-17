# Exact majority basins and symmetry-resolved recurrence on the Nauru graph

## Finding

For the synchronous binary strict open-neighbor majority map \(F\) on the 24-vertex Nauru graph, the complete finite dynamics has
\[
F^7=F^5,\qquad F^6\ne F^4.
\]
Exactly 494 configurations are fixed; precisely 243,542 other configurations are periodic with least period two, forming 121,771 two-cycle orbits. All remaining configurations reach this recurrent set after at most five updates. The exact entrance-time census is

| First recurrent entry \(t\) | Fixed-point basin entry | Two-cycle basin entry | Total |
|---:|---:|---:|---:|
| 0 | 494 | 243,542 | 244,036 |
| 1 | 17,886 | 3,722,094 | 3,739,980 |
| 2 | 104,280 | 4,863,768 | 4,968,048 |
| 3 | 506,400 | 5,042,400 | 5,548,800 |
| 4 | 254,880 | 1,436,832 | 1,691,712 |
| 5 | 95,328 | 489,312 | 584,640 |
| **Total** | **979,268** | **15,797,948** | **16,777,216** |

The recurrent states form 17 fixed-configuration symmetry classes and 1,147 primitive two-cycle symmetry classes under the 144 automorphisms of the graph, identifying phases of each temporal two-cycle. Each unanimous fixed configuration has attraction basin 462,400, while the two-cycle exchanging the unanimous colors between the two bipartition shores has basin 924,800. In contrast, every other fixed point has a basin of size at most 1,936, and every other two-cycle has a basin of size at most 59,840.

## Assumptions and scope

The labelled vertices of \(GP(12,5)\) are \(u_i,v_i\) for \(i\in\mathbb Z/12\mathbb Z\); edges are \(u_iu_{i+1}\), \(u_iv_i\), and \(v_iv_{i+5}\), with undirected indexing. This is the simple 3-regular 24-vertex Nauru graph. Each vertex simultaneously takes state 1 at the next step iff at least two of its three neighbors currently hold state 1; otherwise it takes state 0. There are no self-inputs, stochastic updates, or ties. All 24 vertices are labelled; counts are not divided by spatial symmetries unless explicitly specified.

Equivalently, label vertices by injective triples of symbols from \(\{0,1,2,3\}\); two triples are adjacent iff they differ in one coordinate. This is the four-symbol star graph, another realization of the same Nauru graph. The full geometric symmetry group has order 144 and acts as independent permutations of the four symbols and the three coordinate positions; this is also the graph automorphism group described in the cited graph reference.

The entry time of an initial state \(x\) is \(\tau(x)=\min\{t\ge0:F^{t+2}(x)=F^t(x)\}\). Periodic configurations have entry time zero. A temporal two-cycle is counted once as an orbit, not once per phase.

## Proof

**Bipartite factorization.** The graph is bipartite with twelve vertices in each shore. Write a binary configuration as \((a,b)\), with \(a,b\in\{0,1\}^{12}\). Let \(H_0\) map shore-one opinions to the updated shore-zero opinions, and \(H_1\) map shore-zero opinions to updated shore-one opinions. Because every vertex has three neighbors, each bit of \(H_i\) is exactly the Boolean majority of the three explicitly listed neighbors. Thus
\[
F(a,b)=(H_0(b),H_1(a)),\qquad F^2(a,b)=(G_0(a),G_1(b)),
\]
where \(G_0=H_0\circ H_1\) and \(G_1=H_1\circ H_0\).

**Exact twelve-bit calculation.** Construct the 24 injective triples and all 36 edges, identify the two twelve-vertex shores by a breadth-first graph coloring, and evaluate both \(H_i\) on every one of the \(2^{12}=4096\) possible inputs. The standalone verifier `nauru_cayley.py` has no external dependencies and performs these bounded operations. For either \(G_i\), exactly 494 of the 4096 inputs are fixed. The complete distribution of the least \(d\ge0\) such that \(G_i^{d+1}(a)=G_i^d(a)\) is
\[
(d,\#a)=(0,494),(1,2498),(2,1032),(3,72).
\]
The program checks every input against the constructed transition table and confirms that no other cycles occur. Hence \(G_i^4=G_i^3\) on all twelve-bit inputs; this statement is an exhaustive *finite* conclusion, not an inference from a sample.

**Temporal recurrence.** Once both shore coordinates are fixed by \(G_0,G_1\), the pair is fixed by \(F^2\). Conversely, a configuration fixed by \(F^2\) has both shore coordinates fixed by their respective \(G_i\), so there are exactly \(494^2=244036\) period-dividing-two phases. The mapping \(H_1\) restricts to a bijection from \(\operatorname{Fix}(G_0)\) to \(\operatorname{Fix}(G_1)\), with inverse \(H_0\). Therefore exactly 494 of these phases satisfy \(F(a,b)=(a,b)\); the remaining \(244036-494\) phases form \((244036-494)/2=121771\) genuine two-cycle orbits.

**Sharp first-entry distribution.** For any nonnegative integer \(s\), define \(P_i(s)\) as the number of shore inputs \(z\) satisfying \(G_i^{s+1}(z)=G_i^s(z)\). Define \(Q_0(s)\) by the equation \(H_1(G_0^{s+1}(z))=H_1(G_0^s(z))\), and \(Q_1(s)\) analogously with \(H_0,G_1\). The two disjoint shores give the exact identities
\[
\#\{x:F^{2s+2}(x)=F^{2s}(x)\}=P_0(s)P_1(s),
\]
\[
\#\{x:F^{2s+3}(x)=F^{2s+1}(x)\}=Q_0(s)Q_1(s).
\]
Evaluating these formulas over 4,096 inputs per shore gives cumulative first-entry counts, for \(t=0,1,2,3,4,5\), of 244,036; 3,984,016; 8,952,064; 14,500,864; 16,192,576; and 16,777,216. Consecutive differences give the entry-time table. All inputs have entered by time five and 584,640 enter *at* time five, proving both the claimed iterate identity and its sharpness.

**Exact basin counts.** For each shore-fixed state \(z\), count the inputs whose \(G_i\)-orbit first reaches \(z\); this gives 494 rooted basin sizes on each shore. Their distribution is: size 1 occurs 66 times; 2 occurs 24 times; 3 occurs 234 times; 4 occurs 72 times; 8 occurs 72 times; 44 occurs 24 times; 680 occurs twice. A fixed configuration \((a,H_1(a))\) has attraction basin equal to the product of these two shore basin sizes, and the basin of a genuine two-cycle is the sum of the products for its two phases. Enumerating all 494-by-494 fixed-shore pairs yields fixed-state basin total 979,268 and genuine-two-cycle basin total 15,797,948. It also yields two fixed-point basins of 462,400 each (the two unanimous states), one two-cycle basin of 924,800 (the alternating shore-unanimous pair), and the maxima stated above for other orbits. The complete basin histograms are recorded in `nauru_cayley_output.json`.

**Symmetry quotient.** The 24 symbol-permutation maps and six position-permutation maps acting on injective triples give 144 automorphisms. The Python verifier builds these permutations from five transposition generators, checks that each preserves all graph edges and that their group closure has size 144. The cited complete graph symmetry description supplies the fact that this is the full automorphism group. Recurrent phases are partitioned into orbits under these generators and, for two-cycles, under the temporal transition \(F\). A breadth-first enumeration of these finite orbits yields 17 fixed-state classes and 1,147 temporal two-cycle classes. Orbit-size histograms and their exact summed populations are given by the program's JSON output.

## Verification

The package contains two structurally independent reproducible implementations. `nauru_direct.cpp` builds the generalized Petersen realization and exhaustively iterates *all* \(2^{24}\) labelled binary states, giving the first-entry counts refined by eventual least period. `nauru_cayley.py` builds the graph instead from 24 injective triples, uses two independently constructed 4,096-entry shore maps to derive the same first-entry totals, and independently computes shore basins and symmetry orbits. Each source can be replayed without internet access (standard C++17 and Python 3 standard library). Commands in the extracted package directory:

```sh
g++ -std=c++17 -O3 nauru_direct.cpp -o nauru_direct
./nauru_direct > nauru_direct_output.txt
python3 nauru_cayley.py > nauru_cayley_output.json
```

The embedded output files are exact expected outputs. The C++ direct census totals 16,777,216 states. The shore checker independently reports 494 fixed states and 121,771 two-cycle orbits, confirms all time totals and the symmetry/basin decompositions, and verifies group size 144. No finite enumeration has been extrapolated to larger graphs.

## Relationship to prior work

Goles and Olivos' symmetric-threshold theorem proves that every finite undirected binary majority network eventually reaches period one or two, but does not yield the present graph-specific exact counts or sharp cutoff. Kaaser, Mallmann-Trenn, and Natale's voting-time analysis gives general potential-function bounds and graph-module arguments, not the Nauru graph's full orbit and basin distribution. Eppstein documents the Nauru graph's generalized Petersen, permutation-Cayley and full-symmetry models. Other published majority censuses on the dodecahedral, Heawood, and related canonical graphs concern distinct adjacency structures; their numerical statements do not imply this graph's exact classification.

## Limitations

This is a **finite** exact dynamical classification for the named 24-vertex graph only; it is not a theorem about all generalized Petersen or Cayley graphs. Basins are deterministic cardinalities for all labelled initial states, not Monte Carlo estimates. The all-graph period-two guarantee is credited to preceding theory. A source-index and statement-level comparison found no equivalent classification, but historical priority is not independently established, and inaccessible full records can contain an equivalent unpublished or unindexed calculation. No independent external mathematical audit has yet occurred.

## References

1. D. Eppstein, *The many faces of the Nauru graph* (2007-12-12). https://11011110.github.io/blog/2007/12/12/many-faces-of.html
2. D. Kaaser, F. Mallmann-Trenn, E. Natale, *On the Voting Time of the Deterministic Majority Process*, arXiv:1508.03519 (2015-08-14). https://arxiv.org/abs/1508.03519
3. E. Goles, J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics 30 (1980), 187–189. https://doi.org/10.1016/0012-365X(80)90121-1
4. E. W. Weisstein, *Nauru Graph*, MathWorld. https://mathworld.wolfram.com/NauruGraph.html
