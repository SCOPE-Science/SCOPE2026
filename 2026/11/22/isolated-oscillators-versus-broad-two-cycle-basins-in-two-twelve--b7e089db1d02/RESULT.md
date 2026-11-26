# Isolated oscillators versus broad two-cycle basins in two twelve-vertex Archimedean majority networks

## Finding

On the truncated-tetrahedral graph \(T\), synchronous binary majority has **239 primitive two-cycle orbits attracting 2,366 of the 4,096 labelled initial configurations**. Of those initial configurations, 1,888 are not themselves periodic. Thus a uniformly sampled initial configuration on \(T\) reaches a primitive two-cycle with probability \(2366/4096\). The sharp first periodic-entry time over all configurations is five updates; the sharp time restricted to trajectories ending in primitive two-cycles is three. In particular \(F_T^7=F_T^5\) on the entire state space, but the corresponding identity with cutoff four fails.

For comparison, the *previously documented* cuboctahedral census [1] gives 20 primitive two-cycles whose basins contain only their own 40 phase states, and sharp global first entry at update four. Its eventual oscillation probability is therefore \(40/4096\). The new computation is on \(T\); the cuboctahedron \(C\) is an established same-size benchmark, not a second discovery.

| Invariant | Truncated tetrahedron \(T\) | Cuboctahedron \(C\), benchmark [1] |
|---|---:|---:|
| Fixed configurations | 16 | 146 |
| Primitive temporal two-cycle orbits | 239 | 20 |
| Initial configurations eventually in a fixed point | 1730 | 4056 |
| Initial configurations eventually in a two-cycle | 2366 | 40 |
| Nonperiodic configurations eventually in a two-cycle | 1888 | 0 |
| Initial configurations eventually unanimous | 1360 | 2064 |
| Sharp first periodic-entry time | 5 | 4 |
| Full-automorphism classes of fixed configurations | 5 | 14 |
| Full-automorphism classes of primitive two-cycles | 26 | 3 |

## Assumptions and scope

The vertices of \(T\) are the lexicographically ordered pairs \((a,b)\) of distinct elements of \(\{0,1,2,3\}\). Vertex \((a,b)\) is adjacent to \((b,a)\) and to the two \((a,c)\) with \(c\notin\{a,b\}\). For the benchmark, \(C=L(Q_3)\) has the twelve lexicographically ordered edges of the Boolean cube as vertices; adjacency means sharing a cube endpoint, and cube vertices are indexed by their three-bit integers. The degrees are three and four, respectively.

At each synchronous step a vertex takes the strict majority among its open neighbors; in a tie it retains its own bit. The first periodic-entry time \(\tau(x)\) is the least \(t\ge0\) such that \(F^t(x)\) is periodic, including fixed points. A primitive two-cycle is the unordered pair of its two phases. A spatial class further identifies the action of the full graph automorphism group, without identifying colors by fiat.

## Proof and finite certificate

**Exhaustion.** With bit \(i\) at vertex \(i\), enumerate the integers from 0 to 4095. To build the successor array \(f\), count the one bits among each vertex's neighbors and compare twice that count to the degree, retaining the bit at equality. The supplied `archimedean_majority.py` follows successors until first repetition or until reaching a state already classified. First repetition gives the cycle; propagating backwards gives the least entry time and eventual period of every predecessor. The supplied `archimedean_independent.cpp` obtains the functional graph separately, then repeatedly peels indegree-zero states. Every removed state is transient, and the residual graph, with all remaining indegrees and outdegrees one, is a disjoint union of directed cycles. Reverse removal order gives the entry times and eventual periods of all removed states. Each method processes every initial configuration. The observed least periods are one and two, with the following complete table (the benchmark column counts are reproduced as controls):

| Graph and eventual period | \(t=0\) | \(t=1\) | \(t=2\) | \(t=3\) | \(t=4\) | \(t=5\) |
|---|---:|---:|---:|---:|---:|---:|
| \(T\), fixed | 16 | 238 | 468 | 720 | 216 | 72 |
| \(T\), two-cycle | 478 | 1264 | 528 | 96 | 0 | 0 |
| \(C\), fixed [1] | 146 | 1606 | 1200 | 1008 | 96 | 0 |
| \(C\), two-cycle [1] | 40 | 0 | 0 | 0 | 0 | 0 |

The truncated-tetrahedral two-cycle row sums to 2366, with 478 initial phases giving 239 temporal cycles. Inspecting destinations in the same calculation gives 680 initial configurations reaching each unanimous state on \(T\) (1032 per unanimous state in the benchmark). The configuration encoded by 310 on \(T\) attains time five. Since every periodic state has period dividing two, \(F^2(y)=y\) holds exactly for periodic states; applying this with \(y=F^t(x)\) proves the asserted global cutoff and its sharpness.

**Spatial symmetry.** The four intrinsic triangles of \(T\) are precisely the four groups with common first coordinate. Between any two triangles there is a unique reverse-pair edge. Permuting the triangles therefore determines each vertex image, and all 24 such permutations act by \((a,b)\mapsto(\pi(a),\pi(b))\). For \(C\), its eight intrinsic triangles are the three-edge cube stars. Their pairwise intersections recover the cube; translations of the three-bit labels and coordinate permutations give all 48 cube automorphisms. For each graph the checker applies the full group to fixed phases and to unordered temporal-cycle pairs. The orbit counts are respectively \((5,26)\) for \(T\) and \((14,3)\) for \(C\), and the checker tests the Burnside count and the orbit-size sums.

## Verification and limits

With `archimedean_majority.py`, `archimedean_independent.cpp`, `reference_census.json`, and `verify.py` in one directory, run `python3 verify.py` with Python 3.9+ and a C++17 compiler (`g++`). The supplied sources compute the census and verify the frozen reference data; the C++ source is compiled during the check, not executed from a stored binary. The markers are `INDEPENDENT_CERTIFICATE_OK` and `VERIFY_OK`. The census is a complete finite enumeration on specified graphs, not an extrapolation from a sample or a result about all Archimedean graphs.

## Relationship to prior work

The general eventual period-at-most-two theorem for finite symmetric binary threshold dynamics is classical [2,3]. The line-graph half-factor classification [4] covers cuboctahedral recurrence in principle; the cube case's actual attraction and entry census, including isolated oscillators, is already explicitly published in [1]. The truncated tetrahedron is the line graph of the graph obtained by subdividing all edges of \(K_4\), whose edges join degrees two and three. That representation does not satisfy [4]'s equal-endpoint-degree-parity hypothesis. Three-state excitation on the truncated tetrahedron [5] uses a different state space and update. None of these results supplies the truncated-tetrahedral binary-majority attraction and entry census above. Absolute historical priority, including possible unindexed graph-specific censuses, is not asserted.

The two networks provide exact, comparable finite examples: the reference network can sustain oscillation only when initialized in a recurrent phase, while the truncated tetrahedron reaches oscillation from a majority of all initial configurations. The transient destinations and times distinguish the examples beyond their numbers of recurrent states. No causal claim about degree, triangles, or the effect of a small perturbation of either graph is made.

## References

1. *Cuboctahedral majority dynamics: an exact basin and three-geometry oscillation census*, https://github.com/Resultary/2026/blob/main/2026/11/17/SCOPE-cuboctahedral-majority-dynamics-an-exact-basin-and-three-geometr--5a66d90d9da0/RESULT.md.
2. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics 30 (1980), 187–189, https://doi.org/10.1016/0012-365X(80)90121-1.
3. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz and L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, https://arxiv.org/abs/1405.2486.
4. *Incidence conservation and half-factor classification of two-cycles in line-graph majority dynamics*, https://github.com/Resultary/2026/blob/main/2026/11/1/SCOPE-incidence-conservation-and-half-factor-classification-of-two-cyc--61b3de3ad47a/RESULT.md.
5. *Exact excitation clocks and tetrahedral symmetry on the truncated tetrahedral graph*, https://github.com/Resultary/2026/blob/main/2026/11/8/SCOPE-exact-excitation-clocks-and-tetrahedral-symmetry-on-the-truncate--6c938bef9545/RESULT.md.
