# Complete orbit spectrum and geometric symmetry types of Langton's ant on the \(4\times4\) torus

## Finding

**Theorem (complete labelled orbit and geometric-quotient census).** Standard synchronous turn–flip–move Langton-ant dynamics on the labelled \(4\times4\) periodic square lattice has exactly **46,976 primitive temporal cycles** on its **4,194,304 states**. Their least periods comprise exactly the 25 integers in the table below; every least period is divisible by 16, the sharp minimum is 16, and the sharp maximum is 512. Under the 128-element group of periodic translations and square dihedral isometries, with global binary-color complementation appended to orientation-reversing isometries, these temporal cycles fall into exactly **376 symmetry classes**. The 256 maximal-period cycles form two symmetry classes of 128 cycles each; the 16,384 minimal-period cycles form 128 symmetry classes.

| Least temporal period | Primitive temporal cycles | Labelled states | Geometric symmetry classes |
| ---: | ---: | ---: | ---: |
| 16 | 16,384 | 262,144 | 128 |
| 32 | 4,096 | 131,072 | 36 |
| 48 | 3,328 | 159,744 | 26 |
| 64 | 3,840 | 245,760 | 31 |
| 80 | 3,840 | 307,200 | 30 |
| 96 | 1,600 | 153,600 | 14 |
| 112 | 1,664 | 186,368 | 13 |
| 128 | 1,728 | 221,184 | 14 |
| 144 | 1,152 | 165,888 | 9 |
| 160 | 384 | 61,440 | 3 |
| 176 | 1,664 | 292,864 | 13 |
| 192 | 1,344 | 258,048 | 11 |
| 208 | 1,664 | 346,112 | 13 |
| 224 | 384 | 86,016 | 4 |
| 240 | 896 | 215,040 | 7 |
| 256 | 384 | 98,304 | 3 |
| 272 | 128 | 34,816 | 1 |
| 288 | 320 | 92,160 | 3 |
| 304 | 384 | 116,736 | 3 |
| 320 | 256 | 81,920 | 2 |
| 352 | 384 | 135,168 | 3 |
| 432 | 128 | 55,296 | 1 |
| 448 | 512 | 229,376 | 4 |
| 496 | 256 | 126,976 | 2 |
| 512 | 256 | 131,072 | 2 |
| **Total** | **46,976** | **4,194,304** | **376** |

## Assumptions and scope

Let the site set be \(V=(\mathbb Z/4\mathbb Z)^2\), with 16 *labelled* cells and four distinct cardinal neighbors at each cell. Let \(S\) be the space of all state triples \((\eta,p,d)\), where \(\eta:V\to\{0,1\}\) is the full binary board (0 white, 1 black), \(p\in V\) is the current ant location, and \(d\in\{0,1,2,3\}\) records north, east, south, west in that order. Thus \(|S|=2^{16}\cdot16\cdot4=4,194,304\). One update reads the **old color at the present cell**; on white it turns clockwise, on black counterclockwise; it then flips that cell and moves one step in the new direction with both coordinates taken modulo 4. A temporal cycle is an orbit of the full labelled state, not merely a return to a blank board or to the ant's position. Symmetry equivalence identifies two temporal cycles precisely when one is the image of the other under a member of the specified group, possibly with a temporal rotation.

The spatial symmetry group is \(\Gamma=V\rtimes D_4\) of order \(16\cdot8=128\): its elements are translations followed by the eight signed-permutation isometries of the square. Orientation-preserving elements transform positions, directions and board sites normally. Orientation-reversing elements also complement **every** board color, ensuring commutation with the chirality-sensitive ant rule. This is a geometric action, not the full automorphism group of the underlying 16-vertex adjacency graph.

## Proof

**Reversibility.** If \((\eta',p',d')\) is a successor state, the preceding position is uniquely \(p=p'-e_{d'}\). The old color was \(s=1-\eta'(p)\). The preceding direction was \(d=d'-1\pmod{4}\) when \(s=0\), and \(d=d'+1\pmod{4}\) when \(s=1\). Flipping the color at \(p\) recovers \(\eta\). This gives a two-sided inverse for the update. Therefore every state on the finite torus is periodic **from time zero**.

**Exhaustive finite certificate.** Encode a board as an integer from 0 through 65,535, a site as its row-major index from 0 through 15, and a direction from 0 through 3. The state ID is \(64m+4p+d\), ranging from 0 through 4,194,303. The standalone program `CODE/temporal_orbits.cpp` reconstructs the successor from these definitions, traverses the permutation from each previously unseen state until returning to its starting state, and assigns all states to their unique primitive temporal cycles. A visit to a previously assigned state before return would cause an error. The program tabulates the least periods and maps each representative by all 128 geometric actions; images form entire symmetry classes because the group acts bijectively and commutes with the update. It also checks commutation for the four geometric generators on **every** state and tests all 128 group elements on a deterministic subfamily. All tabulated counts are its direct integer output.

**Independent structural count.** The separately written program `CODE/burnside_cycles.cpp` constructs all 4,194,304 successors, tests the explicit inverse on **every** state, checks all target indegrees are one, and constructs all temporal cycles by a second path-tracing implementation. For each of the 128 signed-permutation affine isometries, it counts temporal cycles left invariant by that isometry acting on a single cycle representative. Burnside's lemma then gives each displayed number of geometric classes as the number of fixed cycle–symmetry pairs divided by 128. The two programs agree in **all 25 rows**, including the 46,976 total primitive cycles, 376 geometric classes and sharp periods 16 and 512. The complete integer output tables are `DATA/temporal_orbits.txt` and `DATA/burnside_cycles.txt`.

The programs cover every state ID without omission, provide all encoded transitions, and use only bounded integer arithmetic. Hence they are finite exhaustive proof certificates for the stated finite state space; this is not an inference from sampled trajectories.

## Verification

Compile each standalone C++17 file with `g++ -std=c++17 -O3` and run the resulting executable. No external libraries, datasets, runtime downloads, or hidden supporting files are required. `CODE/temporal_orbits.cpp` checks group generators and maps all temporal cycles; `CODE/burnside_cycles.cpp` checks the inverse for all states and independently computes the Burnside fixed-sums. Exact stdout must match the respective bundled `DATA` file. In particular, the second output reports `all_indegree_one=1 inverse_all=1 group=128`, `total 46976 4194304 376`, and the known uniform-board return period 96. The first output also reports total `46976 4194304 376`. The row sums of labelled states are 4,194,304, so the table is exhaustive.

## Relationship to prior work

The standard ant rule, time reversibility and finite-torus recurrence are known concepts, not claimed as discoveries. The 2015 MathOverflow discussion concerns cover times from a **uniform** board. The 2019 square-torus discussion and OEIS A309251 record one selected full return period at each torus size, including 96 for the \(4\times4\) board, and explain a general factor-of-eight restriction for even-by-even dimensions. This result instead classifies **every** labelled starting board/position/heading, provides the full least-period spectrum and quotients every primitive temporal orbit by its natural geometric symmetry; it also establishes that **on this particular torus** every period is divisible by 16, a stronger finite-specific conclusion not implied by the general factor-of-eight observation. The 2011 generalized-ant complexity paper treats unbounded lattices with altered rules, and the 2020 twisted-torus complexity paper concerns large-system hardness; neither implies the present exact finite census. Earlier complete censuses on the \(3\times3\) and \(3\times4\) tori concern distinct state spaces and do not imply these counts. No universal period-divisibility theorem for other torus sizes is asserted.

## Limitations

The classification is confined to the 16-site *untwisted* periodic square lattice, the specified initial-state convention, and the stated 128-element geometric action. All 4,194,304 states are enumerated exactly; the result does not establish a closed-form formula across arbitrary torus sizes, nor claim that all even-by-even torus periods are divisible by 16. The complete finite enumeration and symmetry quotient rest on the two specified executable certificates rather than a short hand-computed table. The literature searches did not identify a covering all-states classification, but unindexed historical calculations could affect priority. No independent external mathematical audit has been performed.

## References

1. T. Tsukiji and T. Hagiwara, *Recognizing the Repeatable Configurations of Time-Reversible Generalized Langton’s Ant Is PSPACE-Hard*, Algorithms **4** (2011), 1–15, first published 2011-01-28, https://doi.org/10.3390/a4010001. General ant conventions and complexity on different state spaces.
2. S. Palcoux, *Time for Langton’s ant to cover a “square” torus*, MathOverflow question 199543, posted 2015-03-10, https://mathoverflow.net/questions/199543/time-for-langtons-ant-to-cover-a-square-torus. Uniform-initial-state coverage time, not complete orbit decomposition.
3. *What is the period of Langton’s ant on a torus?*, Mathematics StackExchange question 3296855, first posted 2019-07-18, https://math.stackexchange.com/questions/3296855/what-is-the-period-of-langtons-ant-on-a-torus. Includes the all-white \(4\times4\) return of 96 and an eight-divisibility argument for even-by-even tori.
4. OEIS A309251, *Period of Langton’s ant on an n X n torus*, https://oeis.org/A309251, entered 2019-07-18. Uniform initial state only, with the \(4\times4\) period 96.
5. T. Hagiwara and T. Tsukiji, *Hardness of Approximation for Langton’s Ant on a Twisted Torus*, Algorithms **13** (2020), 344, https://doi.org/10.3390/a13120344. Large twisted torus complexity rather than this finite untwisted orbit census.
