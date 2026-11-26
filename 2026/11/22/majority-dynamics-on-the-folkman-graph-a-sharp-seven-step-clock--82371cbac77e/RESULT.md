# The individual attraction-basin spectrum of Folkman-graph majority dynamics

## Finding

For synchronous binary majority with tie retention on the twenty-vertex Folkman graph, the complete distribution of **individual labelled attraction-basin sizes** is as follows. A two-cycle and its two temporal phases define a single attractor. The basin size includes its periodic points.

| Basin size | Fixed-point basins | Two-cycle basins |
| ---: | ---: | ---: |
| 1 | 384 | 0 |
| 2 | 0 | 60 |
| 3 | 480 | 0 |
| 4 | 120 | 0 |
| 16 | 0 | 240 |
| 18 | 160 | 0 |
| 21 | 120 | 0 |
| 25 | 120 | 0 |
| 28 | 120 | 0 |
| 30 | 240 | 0 |
| 38 | 60 | 0 |
| 55 | 720 | 0 |
| 56 | 720 | 0 |
| 72 | 120 | 0 |
| 76 | 240 | 0 |
| 86 | 120 | 0 |
| 124 | 120 | 0 |
| 152 | 60 | 0 |
| 284 | 20 | 0 |
| 899 | 0 | 40 |
| 1,368 | 60 | 0 |
| 4,038 | 0 | 10 |
| 4,249 | 40 | 0 |
| 8,652 | 0 | 1 |
| 12,190 | 10 | 0 |
| 207,670 | 2 | 0 |

The two largest basins are those of the unanimous fixed points. The orbit-by-orbit assignment is in `basin_catalog.tsv`, keyed by the least numerical periodic phase. For a uniformly chosen starting mask, the probability of reaching any particular attractor is its catalogued basin size divided by \(2^{20}\). For example, 300 of the 351 oscillators attract 16 or fewer starting masks each, while a single oscillator attracts 8,652.

## Assumptions and scope

Use twin vertices \(u_{i,0},u_{i,1}\) for \(i\in\{0,\ldots,4\}\), and edge vertices \(e_{ij}\) for \(0\le i<j<5\). Each \(e_{ij}\) is adjacent to exactly \(u_{i,0},u_{i,1},u_{j,0},u_{j,1}\). Number \(u_{i,0}\) by \(i\), \(u_{i,1}\) by \(5+i\), and \(e_{ij}\) by \(10+k\) for lexicographic pair index \(k\) starting at zero. Bit \(v\) records vertex \(v\). At all vertices simultaneously, adopt the majority among the four neighbors; when they split evenly, retain the old bit. The census is labelled: graph automorphisms do not identify basins.

## Proof and replay

1. Enumerate every integer mask \(0\le x<2^{20}\). All vertices have four neighbors; counting the vertex itself as a fifth voter implements the specified tie rule. Thus threshold three on these five bits computes the exact successor \(F(x)\) in each coordinate.
2. Seed the set of classified masks with all \(x\) satisfying \(F^2(x)=x\). Assign each seed the identifier \(\min(x,F(x))\). This labels precisely the fixed states and temporal two-cycle states; both phases of each two-cycle get the same label. Repeatedly assign every unclassified state the identifier of its successor if that successor was classified before this round. By induction these are precisely the states at the next distance to the seeded set, with the correct eventual label. The full computation exhausts the state space, ruling out any other recurrent states without assuming their absence.
3. Count all labels and attach to each representative \(r\) the period 1 if \(F(r)=r\) and 2 otherwise. The supplied `check_individual_basins.py` computes all rows using only exact integer operations, validates the full spectrum above, verifies the two specified unanimous basins, and compares the complete set of labelled rows with `basin_catalog.tsv` if supplied. Run `python3 check_individual_basins.py basin_catalog.tsv` with NumPy installed.

## Relationship to existing results

The general eventual-period restriction is due to Goles and Olivos, *Periodic behaviour of generalized threshold functions* (1980), DOI `10.1016/0012-365X(80)90121-1`. The distinct record [*A seven-update consensus tail and eight oscillator families in Folkman-graph majority dynamics*](https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-a-seven-update-consensus-tail-and-eight-oscillator-families-in-f--cdd89c0eadf8) reports the exact entry-time, period, and spatial-class populations for the same graph and rule (with different twin bit numbering). Those results, including the sharp entry time and the number of periodic orbits, are not claimed here. Counts grouped only by entry time and period, and counts of recurrent states grouped by spatial class, do not assign an initial state to its individual attractor; the additional invariant here is that distribution and its full labelled catalog.

The calculation is exhaustive on this graph, not a general formula for subdivided doubles or a prediction about random update schedules.
