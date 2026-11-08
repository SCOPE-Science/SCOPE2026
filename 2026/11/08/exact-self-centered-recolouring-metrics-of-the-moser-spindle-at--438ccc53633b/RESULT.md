# Exact self-centered recolouring metrics of the Moser spindle at four and five colours

## Finding

Let \(H\) be the Moser spindle and \(\mathcal C_k(H)\) its graph of **proper vertex-colourings with a palette of \(k\) individually named colours**, where an edge is one proper single-vertex recolouring. For both \(k=4\) and \(k=5\), this reconfiguration graph is connected and **self-centered**, meaning every colouring attains the graph's diameter as its eccentricity, although the reconfiguration graphs are not regular. The exact values are:

| Palette | States | Recolouring edges | Radius | Diameter | Unlabelled colour partitions |
|---|---:|---:|---:|---:|---:|
| \(k=4\) | 384 | 528 | 13 | 13 | 16 |
| \(k=5\) | 5040 | 22560 | 10 | 10 | 42 |

Here the unlabelled colour partitions identify colourings differing by a global permutation of the palette (unused named colours are permitted). The degree distributions are \(96\) vertices of degree two and \(288\) of degree three when \(k=4\); and \(1680\) of degree eight, \(1920\) of degree nine and \(1440\) of degree ten when \(k=5\). Thus adding one spare colour lowers the sharp worst-case number of recolourings between proper colourings from \(13\) to \(10\) while preserving self-centeredness.

The **complete unordered-pair shortest-path distributions** are:

| Distance | \(k=4\) pairs | \(k=5\) pairs |
|---:|---:|---:|
| 1 | 528 | 22,560 |
| 2 | 960 | 110,400 |
| 3 | 1,584 | 382,680 |
| 4 | 2,496 | 1,019,520 |
| 5 | 4,080 | 2,102,160 |
| 6 | 6,624 | 3,196,920 |
| 7 | 9,456 | 3,290,400 |
| 8 | 10,896 | 2,005,200 |
| 9 | 11,232 | 534,600 |
| 10 | 11,472 | 33,840 |
| 11 | 10,896 | — |
| 12 | 2,832 | — |
| 13 | 480 | — |
| **Total** | **73,536** | **12,698,280** |

## Assumptions and scope

Work exclusively with the simple undirected graph \(H=(V,E)\), where \(V=\{0,1,2,3,4,5,6\}\), and the eleven unordered edges are:

```text
(0,2) (0,3) (1,2) (1,3) (2,3)
(0,5) (0,6) (4,5) (4,6) (5,6) (1,4)
```

It is obtained by joining two copies of a diamond (\(K_4\) with one edge deleted) at vertex \(0\) and adding the edge \((1,4)\). This is \(H_4\) of Cereceda, van den Heuvel and Johnson, and is isomorphic to the Moser spindle. In the second certificate it is instead constructed as the complement of the graph formed by subdividing one edge of \(K_{3,3}\). The explicit isomorphism from the displayed vertex labelling to the second labelling sends the vertices \((0,1,2,3,4,5,6)\) to \((6,0,1,2,3,4,5)\).

For \(k\in\{4,5\}\), the reconfiguration graph has as vertices all functions \(c:V\to\{0,\ldots,k-1\}\) such that \(c(u)\ne c(v)\) whenever \(uv\in E\). No requirement is imposed that every colour occur. Distinct proper colourings are adjacent if and only if their functions differ at exactly one vertex. Distances count individual recolourings of one vertex, *not* Kempe-chain exchanges or simultaneous colour permutation.

## Proof

**1. Exhaustive state space.** The first accompanying checker `verify_moser_hajos.py` recursively visits all partial assignments in order \(0,1,\ldots,6\), trying every palette colour at the next vertex that differs from all already-assigned neighbours. Every proper complete assignment has exactly one sequence of valid prefixes, so this procedure generates it exactly once; conversely, every generated leaf is proper. The exhaustive result is \(384\) assignments for \(k=4\) and \(5040\) for \(k=5\). The second checker `verify_moser_complement.cpp` independently tests *every* one of the \(k^7\) possible functions against the eleven edges of an isomorphic graph; it finds exactly the same counts. These are exact finite enumerations, not samples.

**2. Exhaustive moves.** For each proper colouring and each original vertex, both checkers try all other palette colours, retaining exactly those assignments that remain proper. This construction has neither spurious moves nor missing moves, by the definition of adjacency. Every unordered edge is encountered twice, once in either orientation; degree sums therefore yield \(528\) and \(22560\) undirected edges. The direct algorithms recover the degree histograms stated above.

**3. Exact shortest paths and eccentricities.** Each checker runs ordinary breadth-first search independently from **every** valid colouring in the corresponding reconfiguration graph. Breadth-first search in an unweighted graph assigns distance \(d\) precisely at the earliest layer of a vertex, which is a shortest path of \(d\) legal moves. Every source reaches every target; hence each graph is connected, in agreement with the previously known general connectivity theorem for \(H_4\). For \(k=4\), all \(384\) BFS runs have maximum distance \(13\). For \(k=5\), all \(5040\) runs have maximum distance \(10\). Consequently the minima and maxima of eccentricity coincide, with respective values \(13\) and \(10\). Counting target entries only when the target index exceeds the source index yields the exact unordered-pair histograms in the table. Their sums are respectively \(384\cdot383/2=73536\) and \(5040\cdot5039/2=12698280\).

**4. Colour-permutation classes.** The first checker replaces the first colour encountered in a complete assignment by \(0\), the next previously unseen colour by \(1\), and so on. Two colourings produce the same canonical tuple exactly when they differ by a palette permutation. Set cardinalities are \(16\) and \(42\); no quotient distances are substituted for the full named-colour distances.

This exhausts all possible vertices, all legal local moves and all pairs, proving the finite claim. The two implementations use different underlying graph representations, enumerators, and state encodings, reducing dependence on any single implementation's enumeration logic.

## Verification

The package includes standalone source files `verify_moser_hajos.py` and `verify_moser_complement.cpp`. Reproduce on a standard Python 3 interpreter and a C++17 compiler:

```sh
python3 verify_moser_hajos.py
c++ -std=c++17 -O2 -Wall -Wextra -o verify_moser_complement verify_moser_complement.cpp
./verify_moser_complement
```

Both programs were run against the packaged sources and agreed on all state counts, move counts, radius and diameter values, degree histograms, eccentricities and pairwise distance distributions. The Python program additionally checks the colour-permutation class counts. The C++ program prints `COMPLEMENT_EXHAUSTIVE_BOTH_PALETTES_PASS`; the Python program prints `PYTHON_EXHAUSTIVE_BOTH_PALETTES_PASS`.

## Relationship to prior work

Moser and Moser introduced the classical seven-vertex four-chromatic unit-distance obstruction in 1961. Cereceda, van den Heuvel and Johnson's research report (July 2005), Section 4, defines the general Hajós graph \(H_m\) and explicitly proves that it is \(k\)-mixing for all \(k\ge m\) (Property 7). The case \(m=4\) covers the Moser spindle for both palettes here. **Connectivity is therefore not new**, nor is the definition of the recolouring graph. Our claim is restricted to the *exact finite state and shortest-path geometry*: the full distance and eccentricity distributions, the self-centeredness of both nonregular state graphs, and the sharp change in diameter between palettes of size four and five. These numerical and structural metric assertions are not implied by the known connectivity result and were not located in the inspected primary texts.

## Limitations

This is a finite classification for a **single seven-vertex graph** at two palettes only. No larger-graph or general \(m\)-Hajós diameter theorem, mixing-time estimate, or optimal recolouring algorithm for arbitrary input graphs follows. The source programs and exhaustive reasoning verify the exact finite claim; scholarly priority remains qualified because an unindexed computation or table could contain the same metrics. The original 1961 graph source and July 2005 research report are only dated to their publication month/year in accessible metadata; the separately reported day-precision provenance of the later journal record must not be mistaken for their original release day. No independent scholarly audit has been performed.

## References

1. L. Moser and W. Moser, “Solution to Problem 10,” *Canadian Mathematical Bulletin* **4** (1961), 187–189, DOI: `10.1017/S0008439500025753`.
2. L. Cereceda, J. van den Heuvel, and M. Johnson, “Connectedness of the Graph of Vertex-Colourings,” CDAM Research Report LSE-CDAM-2005-11 (July 2005), Section 4, Property 7; freely accessible: `https://matthewjohnsondurham.github.io/papers/cdam-2005-11.pdf`.
3. L. Cereceda, J. van den Heuvel, and M. Johnson, “Connectedness of the Graph of Vertex-Colourings,” *Discrete Mathematics* **308** (2008), 913–919, DOI: `10.1016/j.disc.2007.07.028` (journal counterpart of reference 2).
