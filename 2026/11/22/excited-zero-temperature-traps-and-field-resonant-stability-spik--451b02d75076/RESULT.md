# Excited zero-temperature traps and field-resonant stability spikes on an Ising icosahedron

## Finding

In the uniform nearest-neighbor Ising antiferromagnet on the twelve-vertex icosahedron, the open positive-field intervals \(0<h<J\), \(J<h<3J\), and \(3J<h<5J\) contain exactly 20, 15, and 6 strict one-spin local minima above the ground energy, respectively. The first classification also holds at \(h=0\). At \(h/J=1,3\) there are 407 and 191 weak one-spin local minima, respectively, compared with 92, 45, and 26 in the three open sub-saturation intervals. At \(h=5J\) the 69 weak minima are exactly the ground states. There are no strict minima at these three threshold fields, and above saturation the unique minimum, also strict, is the all-plus state.

The excited minima have the following exact supported geometries:

* For \(0\le h<J\), the equal-sign induced subgraphs are a chordless hexagon and two disjoint induced triangles on opposite sign classes. There are ten states with the hexagon on the down-spin class and ten with it on the up-spin class. These are not partitions into two hexagons.
* For \(J<h<3J\), the four down spins induce two disjoint edges **and** every up vertex has exactly two down neighbors. The outside condition is essential: only 15 of the 75 four-subsets inducing two disjoint edges have it.
* For \(3J<h<5J\), the two down spins are an antipodal pair.

Their respective energy excesses over the ground state are \(4J\), \(4J\), and \(10J-2h\).

## Assumptions and scope

For spins \(s_i\in\{-1,+1\}\), let \(M=\sum_i s_i\), \(B=\sum_{\{i,j\}\in E}s_i s_j\), and \(\mathcal H_h=JB-hM\), with \(J>0\) and \(h\ge0\). Weak stability means no single-spin flip lowers energy; strict stability means all such flips raise energy. A strict local minimum is absorbing for zero-temperature single-spin dynamics that forbids uphill flips; weak minima at threshold fields need not be absorbing when neutral flips are allowed. No claims are made about thermal lifetimes, multi-spin stability, or basin sizes. Negative fields follow by global spin reversal.

Use the regular icosahedron with vertex positions \((0,\pm1,\pm\varphi)\) and their cyclic permutations, where \(\varphi=(1+\sqrt5)/2\), with all signs chosen independently. Edges have squared length four. Equivalently, use poles 0 and 11 and pentagons \(1,\ldots,5\) and \(6,\ldots,10\); for \(r\bmod5\) include the six edges \(\{0,1+r\},\{11,6+r\},\{1+r,1+(r+1)\},\{6+r,6+(r+1)\},\{1+r,6+r\},\{1+r,6+(r-1)\}\).

## Proof

The flip cost is \(2s_i(h-J\sum_{j\sim i}s_j)\). Degree five makes each neighbor sum one of \(-5,-3,-1,1,3,5\); thus testing \(t=h/J=0,1,2,3,4,5,6\) covers all stability cases. In particular the \(t=0\) stability set holds for the entire first interval. Equivalently, for the down set \(D\), the condition is \(t\le5-2|N(i)\cap D|\) for \(i\in D\) and \(t\ge5-2|N(i)\cap D|\) for \(i\notin D\), with strict signs for strict stability.

The accompanying finite certificate generates the 30 edges by squared distance in exact \(\mathbb{Z}[\varphi]\) arithmetic, using \(\varphi^2=\varphi+1\). It evaluates \((M,B)\) for each of the \(2^{12}\) spin masks, tabulates all energies \(B-tM\) for each representative (with no sampling or numerical tolerances), and compares each energy to the values for all twelve one-bit neighbors. This gives:

| \(h/J\) | Weakly stable \((M,B):\mathrm{count}\) | Weak | Strict | Ground |
|---|---|---:|---:|---:|
| \([0,1)\) | \((0,-10):72;\ (0,-6):20\) | 92 | 92 | 72 |
| \(1\) | \((0,-10):72;\ (0,-6):50;\ (2,-8):120;\ (2,-4):120;\ (4,-6):30;\ (4,-2):15\) | 407 | 0 | 222 |
| \((1,3)\) | \((4,-6):30;\ (4,-2):15\) | 45 | 45 | 30 |
| \(3\) | \((4,-6):30;\ (4,-2):75;\ (6,0):20;\ (6,4):60;\ (8,10):6\) | 191 | 0 | 50 |
| \((3,5)\) | \((6,0):20;\ (8,10):6\) | 26 | 26 | 20 |
| \(5\) | \((6,0):20;\ (8,10):36;\ (10,20):12;\ (12,30):1\) | 69 | 0 | 69 |
| \((5,\infty)\) | \((12,30):1\) | 1 | 1 | 1 |

It suffices to compare energies within the tabulated weakly stable sets because all global minimizers are weakly stable. Comparing their affine energy expressions, not just the values at the representatives, gives the ground counts across the whole corresponding ranges and the stated excited energies. At \(h=5J\) every listed pair gives the same energy \(-30J\).

For each of the 20 strict excited masks in the first row the certificate checks that both equal-sign subgraphs are 2-regular on six vertices and exactly one is connected. A connected simple 2-regular graph on six vertices is a cycle; if disconnected its only possible component sizes are three and three. Conversely any such partition makes every spin have two same-sign and three opposite-sign neighbors; it is strictly stable for \(0\le h<J\), with \(M=0,B=-6\). For example, in the pole/pentagon labeling the down cycle \((0,1,10,11,8,3)\) has complement given by the triangles \(\{2,6,7\}\) and \(\{4,5,9\}\).

For the 15 middle-field excited masks the certificate checks the internal degree one and external degree two conditions; conversely these degrees make both strict inequalities hold throughout the interval. There are 75 two-edge induced supports in total, with the remaining 60 having up-vertex degrees \((1,1,2,2,2,2,3,3)\) into the support, failing strict stability. For the six high-field excited masks the certificate checks antipodality. For a vertex and its antipode the neighbor sets are disjoint, contain five vertices each and cover the ten other vertices, as can be checked in the coordinate construction. Hence any antipodal pair satisfies the strict inequalities for \(3J<h<5J\), with \((M,B)=(8,10)\).

## Reproduction

Run `python3 verify_finite.py` using the Python standard library. The complete enumeration checks the table, both sign orientations of the corrected low-field geometry, the external-degree condition distinguishing the 15 middle-field traps, and antipodality. The verification concerns the exact finite single-flip landscape, not historical priority or positive-temperature dynamics.

## Relationship to prior work

Strečka, Karlová and Madaras (2015), especially Eq. (5), Fig. 2 and Table 4, give the same icosahedron's equilibrium plateaux and degeneracies, as well as a configuration/energy catalogue using induced subgraphs. Neither energy levels nor aggregate induced-subgraph degeneracies alone specify the local-flip stability of their members; the stability-resolved census distinguishes configurations even within the same energy and induced shape. The claim here is the complete one-spin stability census, including the excited subsets and exact threshold spikes, not the equilibrium data or the underlying configuration/energy catalogue. Wacław and Burda (2008) study strict single-spin minima for random Gaussian couplings rather than this deterministic uniform model. Historical priority beyond the inspected work is not asserted.

## References

- J. Strečka, K. Karlová, and T. Madaras, *Giant magnetocaloric effect, magnetization plateaux and jumps of the regular Ising polyhedra*, https://arxiv.org/abs/1502.04449 (2015).
- B. Wacław and Z. Burda, *Counting metastable states of Ising spin glasses on arbitrary graphs*, https://arxiv.org/abs/0801.1224 (2008).
