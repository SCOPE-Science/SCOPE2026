# Eighteen affine four-waves under two-contact excitation on the four-cube

## Finding

Consider synchronous three-state Greenberg–Hastings excitation on the four-dimensional Boolean cube \(Q_4\), with a resting vertex requiring **at least two excited neighbors** before becoming excited. The complete state space has \(3^{16}=43{,}046{,}721\) labelled configurations. Exactly **one fixed configuration** (the all-rest state) and **18 primitive temporal four-cycles** are recurrent; no other least periods occur. All states reach their periodic orbit within **seven updates**, and this is sharp:
\[
F^{11}=F^7,\qquad F^{10}\ne F^6.
\]
The 18 nonconstant cycles split into exactly two spatial symmetry classes under the 384 automorphisms of the cube: six *parallel* affine-plane four-waves and twelve *alternating-direction* affine-plane four-waves. Every phase contains exactly four excited vertices, forming an affine two-flat in \(\mathbb F_2^4\); the four excitation sets partition all 16 vertices. In the parallel family, all four phase planes have the same direction subspace. In the alternating family, opposite phase planes have equal directions but adjacent phase planes have distinct directions.

The attraction basin of each parallel four-wave has exactly **676** labelled initial configurations; the basin of each alternating four-wave has exactly **644**. Thus precisely \(6\cdot676+12\cdot644=11{,}784\) configurations eventually oscillate, while \(43{,}034{,}937\) reach the all-rest fixed point. Nonconstant cycles acquire no new basin members after two updates. The exact first-periodic-entry census is:

| First entry \(t\) | Eventual fixed point | Eventual four-cycle |
|---:|---:|---:|
| 0 | 1 | 72 |
| 1 | 65,535 | 1,080 |
| 2 | 5,774,795 | 10,632 |
| 3 | 20,763,318 | 0 |
| 4 | 11,855,256 | 0 |
| 5 | 3,875,184 | 0 |
| 6 | 681,648 | 0 |
| 7 | 19,200 | 0 |
| **Total** | **43,034,937** | **11,784** |

The same graph can be viewed as the \(4\times4\) nearest-neighbor toroidal lattice \(C_4\square C_4\). Counts are for the labelled four-cube, not modulo graph or temporal symmetry unless explicitly stated.

## Assumptions and scope

Vertices are the binary four-tuples \(V=\mathbb F_2^4=\{0,\ldots,15\}\); the four neighbors of \(v\) are \(v\oplus1,v\oplus2,v\oplus4,v\oplus8\), where \(\oplus\) denotes bitwise xor. A configuration \(x\in\{0,1,2\}^{V}\) labels rest by 0, excitation by 1, and refractory state by 2. The deterministic synchronous map \(F\) is
\[
(Fx)_v=\begin{cases}
2,&x_v=1,\\
0,&x_v=2,\\
1,&x_v=0\text{ and }\#\{u\sim v:x_u=1\}\ge 2,\\
0,&\text{otherwise}.
\end{cases}
\]
A *primitive temporal orbit* is a directed periodic cycle counted once, not once per phase. A cycle's *basin* includes all states eventually entering it, including cycle states. The *first periodic-entry time* \(\tau(x)\) is the least nonnegative \(t\) such that \(F^t(x)\) is periodic. The symmetry group acts by translations and permutations of the four binary coordinates, of order \(2^4\cdot4!=384\). A four-point *affine two-flat* is a coset of a two-dimensional vector subspace of \(\mathbb F_2^4\).

## Proof

**Exact local-to-global transition.** Let \(E\) and \(R\) denote the disjoint excited and refractory subsets. Define \(T(E)=\{v:\#(N(v)\cap E)\ge2\}\). The update is exactly
\[
(E,R)\longmapsto\bigl(T(E)\setminus(E\cup R),\ E\bigr).
\]
The disjoint-pair encoding is a bijection with all \(3^{16}\) configurations. Neither the threshold nor the refractory update depends on future states.

**Independent exhaustive certificates.** The standalone `census_q4.cpp` enumerates every radix-three initial index from 0 to 43,046,720 and performs functional-digraph path exploration. For each unclassified state, it follows unique successors until meeting either a state on the current path or a previously classified state. Newly repeated path segments are precisely directed cycles; preceding vertices inherit the reached cycle and their entry time is one plus the successor's time. Therefore every state is assigned exactly once, every periodic orbit is found, and the program's `HIST` and `BASIN` lines are exhaustive, rather than sampled. It uses bit-parallel neighbor permutations and an independent digit table to evaluate the update.

The separately written `forward_q4.cpp` reconstructs excited and refractory masks from radix-three coordinates, independently precomputes the local two-neighbor predicate by inspecting each of four neighbors of each vertex, and, **for each of all 43,046,721 configurations**, directly iterates its complete trajectory until the first repeated state. It calculates the repetition index and cycle length without borrowing the functional-graph labels of the first algorithm; it also groups basins by a canonical packed recurrent state. Both outputs independently yield exactly 19 components (one fixed, 18 four-cycles), the identical full 11-cell depth/period table above, the identical two nonconstant basin sizes and multiplicities, and sharp maximal entry time 7. The complete output files are `results_a.txt` and `results_b.txt`.

**Geometric certification.** The standalone `geometry_q4.py` reads all 18 periodic cycle representatives from `results_b.txt`. It independently evaluates the vertex-wise map on each of their four states, checks that each cycle contains four disjoint four-point excitation sets, and verifies the affine two-flat closure condition on each set. It classifies plane directions and exhaustively applies all 384 translation/coordinate-permutation automorphisms together with four temporal rotations. The resulting classes have sizes 6 (parallel) and 12 (alternating), and the corresponding individual basin values are supplied by the two independent census programs. The geometry script also checks that all 18 recurrent cycles persist under the extra antipodal edges of the folded cube, without claiming equality of their nonperiodic attraction basins.

**Sharpness witness.** The radix-three state index 88458 has the eight-step trace recorded in `witness.txt`. The first periodic configuration in that trace is the all-rest state at step 7, proving \(F^{10}\ne F^6\). Since all cycles have period dividing 4 and all first-entry times are at most 7, \(F^{11}=F^7\) holds for every state. A separate exact four-period trace is also included in `witness.txt`.

## Verification

Compile and execute in the same directory with a C++17 compiler:

```sh
c++ -O3 -std=c++17 census_q4.cpp -o census
./census > results_a.txt
c++ -O3 -std=c++17 forward_q4.cpp -o forward
./forward > results_b.txt
python3 geometry_q4.py > geometry_result.txt
```

The delivered `results_a.txt`, `results_b.txt`, `geometry_result.txt`, and `witness.txt` are expected complete outputs and witnesses. No proprietary libraries, dataset downloads, third-party graph files, or random seeds are necessary. All certificates use integer arithmetic. The two C++ computations independently traverse the full finite state space; the Python check exhausts all 18 computed periodic cycles and 384 vertex automorphisms. The checks establish a finite theorem on this fixed graph and do not prove a dimension-uniform assertion.

## Relationship to prior work

The Greenberg–Hastings family with multi-neighbor activation is classical: Fisch, Gravner, and Griffeath (1991) formulate the threshold parameter and study wave patterns on planar lattices, but provide neither this labelled \(4\times4\) toroidal threshold-two basin census nor its complete affine-wave symmetry partition. Gravner, Lyu, and Sivakoff (2016) prove general finite-graph criteria for the **one-neighbor** three-state rule; the crucial local premise differs from the present two-neighbor map. The previously published *Primitive excitation periods on the four-cube* computes the full four-cube census for **threshold one**, rather than two. The associated one-neighbor map has primitive periods 3, 4, and 10, whereas the current two-neighbor map has only period 4 among nontrivial periods. These are different systems, not coordinate relabellings. Another prior census on the five-regular folded cube (Clebsch graph, formed from this four-cube by adjoining all antipodal edges) reports 90 four-waves at threshold two; the present claim treats the degree-four cube without those edges. The coincidence of individual basin-size values 644 and 676 across the two graphs is a comparison with that prior report, not a claimed basin-set equivalence or revalidation of that report.

## Limitations

These conclusions concern the exact three-state synchronous two-neighbor rule on \(Q_4\), not higher-dimensional cubes, other contact thresholds, stochastic updates, or general finite graphs. Geometric orbit classification is for the cubical automorphism group, not arbitrary permutations of the vertices. The two independent exhaustive implementations are finite computational proofs conditional on their faithful execution and hardware; they are not independent peer review or external formal certification. The literature search cannot rule out unindexed prior tables or undocumented historically equivalent computations. No universal statement about a minimum dimension for two-contact waves is asserted.

## References

- R. Fisch, J. Gravner, and D. Griffeath, *Threshold-range scaling of excitable cellular automata*, *Statistics and Computing* **1** (1991), 23–39, DOI: `10.1007/BF01890834`; lawful full text: https://www.math.ucdavis.edu/~gravner/papers/fgg.pdf .
- R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, first arXiv public posting 1993-03-22, https://arxiv.org/abs/patt-sol/9303002 .
- J. Gravner, H. Lyu, and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, first publicly posted 2016-10-24, https://arxiv.org/html/1610.07320v1 .
- *Primitive excitation periods on the four-cube: an exact finite-state census*, public four-cube **threshold-one** result: https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-primitive-excitation-periods-on-the-four-cube-an-exact-finite-st--d99b448f2f7e .
