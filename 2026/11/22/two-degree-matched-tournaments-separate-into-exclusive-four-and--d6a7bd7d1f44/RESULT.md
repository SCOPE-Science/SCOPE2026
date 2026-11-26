# Exact majority basins and a sharp four-update entry bound in the 23-vertex carousel tournament

## Finding

On the labelled 23-vertex carousel tournament, synchronous strict binary majority over the eleven out-neighbors sends **3,906,412** of the **8,388,608** initial configurations to travelling waves and **4,482,196** to unanimity. The sharp maximum time to enter a periodic orbit is **four updates**. Exactly **60,858** configurations take all four updates, and all of them enter unanimity. The latest entry to a travelling wave is at update three, attained by **47,012** configurations. The exact profile is:

| First periodic-entry time | Eventually unanimous | Eventually a travelling wave |
|---:|---:|---:|
| 0 | 2 | 276 |
| 1 | 1,375,952 | 2,302,576 |
| 2 | 2,427,880 | 1,556,548 |
| 3 | 617,504 | 47,012 |
| 4 | 60,858 | 0 |

In particular, the carousel map satisfies \(F^{27}=F^4\) and \(F^{26}\ne F^3\). The two unanimous states and twelve travelling-wave orbits of period 23 follow from the centered-majority classification of Nakar and Ron [1], as explained below. The contribution here is the labelled **attraction and first-entry census**, not the classification of the recurrent states.

## Assumptions and scope

The vertices are \(i\in\mathbb Z/23\mathbb Z\), and the out-neighbors of \(i\) are \(i+1,\ldots,i+11\). For a configuration \(x\in\{0,1\}^{23}\), the synchronous rule is
\[
 F(x)_i=\mathbf 1\left\{\sum_{j=1}^{11}x_{i+j}\ge 6\right\}.
\]
The first periodic-entry time of \(x\) is the smallest \(t\ge0\) for which \(F^{t+p}x=F^t x\) for some \(p>0\). The basin counts refer to all labelled inputs, with no quotient by spatial rotation or complementation. The encoding of a configuration is \(\sum_{i=0}^{22}2^ix_i\).

The reproducibility files also report a comparator: the Paley tournament on the same vertex set, with arc offsets \(\{1,2,3,4,6,8,9,12,13,16,18\}\) and the same threshold. Its census is stated in [2] and is not a new result here.

## Recurrent states from centered majority

Write \((Sx)_i=x_{i+1}\), and let \(M_5\) be strict majority in the centered window \(i-5,\ldots,i+5\). Then \(F=S^6M_5\), and \(M_5\) commutes with \(S\). The vertices on periodic orbits of \(F\) are exactly the configurations on periodic orbits of \(M_5\): a period \(p\) for either map yields a return for the other after \(23p\) steps, since \(S^{23}=I\).

Nakar and Ron's Theorem 1 and Definitions 8–9 [1] imply that a nonconstant recurrent configuration either has all monochromatic runs of length at least six, or has a spatial period strictly smaller than 23. The latter is impossible on a prime-order ring: invariance by a nonzero shift implies invariance by a generator and hence constancy. In the former case there can be just two runs, since the number of runs of a nonconstant binary cyclic word is even and four runs of length at least six would use at least 24 sites. The words with two runs of lengths at least six are all fixed under \(M_5\), as are the unanimous states. Thus \(F\) acts on the nonconstant recurrent words by shift \(S^6\). For each one-block length from 6 to 17 the 23 labelled rotations form a single orbit. This gives precisely twelve orbits of least period 23 and the 276 nonconstant inputs at entry time zero.

## Exhaustive basin and entry calculation

The supplied programs enumerate all integers from zero to \(2^{23}-1\). Their carousel branches compute the rule above using eleven consecutive offsets but use different classification algorithms:

- `code/exhaustive_peel.cpp` computes the successor by popcount on each out-neighborhood mask, builds indegrees, and successively removes vertices of indegree zero. A vertex on a cycle always retains its predecessor. Conversely, the unremoved finite subgraph has one successor per vertex and positive indegree everywhere, so every unremoved vertex lies on a cycle. A cycle has entry time zero; in reverse removal order each other vertex inherits its successor's least eventual period and adds one to the successor's entry time.
- `code/exhaustive_paths.cpp` uses direct bit tests of the eleven neighbors. Following an unclassified path either finds a repetition on that path, which gives the entire new cycle, or hits a previously classified state. In either case processing the remaining path backwards gives the period and first-entry time.

The carousel output rows in `data/peel_output.txt` and `data/paths_output.txt` agree and give the table above. The table's period-23 and unanimous columns sum to the two basin totals. The input mask `171551` first reaches a periodic state after four updates. All periods divide 23; consequently the universal depth-four bound yields \(F^{27}=F^4\). At time three the depth-four witness cannot already return after 23 more steps, proving \(F^{26}\ne F^3\).

## Reproduction

With C++17 and a compiler supporting the stated flag, run from the package directory:

```sh
g++ -std=c++17 -O3 -mpopcnt code/exhaustive_peel.cpp -o exhaustive_peel
./exhaustive_peel
g++ -std=c++17 -O3 code/exhaustive_paths.cpp -o exhaustive_paths
./exhaustive_paths
```

Compare the carousel rows with the corresponding files under `data/`. The programs also print Paley rows, which reproduce the comparator. The recurrence classification above is independent of this finite basin computation.

## Relationship to prior work and limitations

The centered classification [1] supplies the carousel's recurrent states through a shift, but not the exact numbers of inputs reaching either type at each entry time. The same-size Paley census [2] gives 3,542 primitive four-cycles, an oscillator basin of 69,828 inputs, and a sharp entry time of ten. Thus on the same 23 labelled vertices with the same out-degree and threshold, the carousel waves attract far more inputs while the Paley relaxation tail is longer. The disjoint nontrivial periods follow from [1] and [2]; they are not a separate novelty claim. Both the present record and [2] have the same catalogue date, which does not establish priority. The closely related carousel calculation [3] treats order 19, including its exact basins and sharp depth; that different order does not give the 23-site histogram.

The census is for one graph size, threshold and orientation, under synchronous updates. The proportions refer to uniform choice from the labelled binary inputs. No general transient bound, per-wave basin size, or historical priority is asserted.

## References

1. Y. Nakar and D. Ron, *The Structure of Configurations in One-Dimensional Majority Cellular Automata: From Cell Stability to Configuration Periodicity*, [arXiv:2205.08972](https://arxiv.org/abs/2205.08972), especially Definitions 8–9 and Theorem 1.
2. [*Paley-23 majority: fourteen affine oscillator families and a sharp ten-step consensus tail*](https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-paley-23-majority-fourteen-affine-oscillator-families-and-a-shar--200a56a85158), Finding and assumptions.
3. [*A ten-wave nineteen-clock and exact majority basins on the cyclic tournament of order nineteen*](https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-a-ten-wave-nineteen-clock-and-exact-majority-basins-on-the-cycli--caf7069a6706), Finding and assumptions.
