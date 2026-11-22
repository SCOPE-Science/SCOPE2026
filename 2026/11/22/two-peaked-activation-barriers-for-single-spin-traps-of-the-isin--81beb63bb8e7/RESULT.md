# Two peaked activation barriers for single-spin traps of the Ising cuboctahedron

## Finding
Let \(G\) be the twelve-vertex cuboctahedral graph, or equivalently the line graph of the three-dimensional cube \(Q_3\). Put spins \(s_v\in\{-1,+1\}\) on its vertices, with energy
\[
H_x(s)=J\left(\sum_{\{u,v\}\in E(G)}s_us_v-x\sum_{v\in V(G)}s_v\right),\qquad J>0,\quad x=h/J\geq0.
\]
A **strict one-spin minimum** is a configuration for which flipping any one spin strictly raises energy; an **excited strict trap** is such a minimum that is not a global ground state. For a trap \(s\), define its *ground-reaching activation barrier* as
\[
B_x(s)=\min_{s=s^{(0)}\sim s^{(1)}\sim\cdots\sim s^{(k)}\in\mathcal G_x}
\left(\max_{0\le i\le k}H_x(s^{(i)})-H_x(s)\right),
\]
where each \(\sim\) flips exactly one spin, \(k\) is arbitrary, and \(\mathcal G_x\) is the complete global-ground-state set.

The complete positive-field strict-trap classification and every trap's exact barrier are:

| Field \(x\) | Ground states | Excited strict traps | All excited-trap barriers \(B_x/J\) |
|---|---:|---:|---|
| \(0<x<2\) | 9 | 36 | \(2\min\{x,2-x\}\) |
| \(x=2\) | 9 | 0 | No excited strict traps |
| \(2<x<4\) | 9 | 8 | \(2\min\{x-2,4-x\}\) |
| \(x\geq4\) | 1 for \(x>4\), 108 at \(x=4\) | 0 | No excited strict traps |

At \(x=4\) the ground state is degenerate but **none** of its configurations is a strict one-spin minimum. The count of all strict minima at \(x=0,2,4\) is respectively \(0,9,0\), and that of weak one-spin minima (no strictly energy-decreasing single flip) is respectively \(458,185,108\). At \(0<x<2\) the 36 traps have zero-field exchange energy \(-8J\) and magnetization \(2\); at \(2<x<4\) the eight traps have exchange energy \(0\) and magnetization \(6\). The nine common ground states have exchange energy \(-8J\) and magnetization \(4\).

Each excited trap has an optimal **three-spin-flip** path to a ground state. The barriers peak at exactly \(x=1\) and \(x=3\), each at height \(2J\), even though the equilibrium ground-state family is unchanged throughout \(0<x<4\). The 36 lower-field traps split into cuboctahedral symmetry orbits of sizes 12 and 24; the eight upper-field traps form one orbit.

## Assumptions and scope
The theorem concerns the finite, unweighted, simple cuboctahedral graph with twelve labelled vertices and twenty-four edges, the specified classical spin normalization \(s_v=\pm1\), uniform antiferromagnetic exchange \(J>0\), and nonnegative physical field \(h\). Only single-spin-flip paths enter the barrier definition. Multiplication of all energies by \(J\) multiplies all barriers by \(J\). For negative field the corresponding statements follow by global spin reversal. A weak minimum permits zero-energy flips and need not be dynamically absorbing if those moves are allowed. The equilibrium and strict-minimum counts are distinct notions.

## Proof
**1. Graph and local stability.** Label the cube vertices by integers \(0,\ldots,7\), regard bitwise neighbors as cube edges, and let the twelve cube edges label the vertices of \(G=L(Q_3)\). Two such vertices are adjacent exactly when their cube edges share an endpoint. Independently, their midpoint coordinates are the twelve points obtained by permuting \((0,\pm1,\pm1)\), with adjacency when squared Euclidean distance is two. These realizations give the same four-regular graph. For any spin \(i\), direct subtraction gives
\[
H_x(s^{(i)})-H_x(s)=2J s_i\left(x-\sum_{j\sim i}s_j\right).
\]
Because every vertex has four neighbors, the signed local-field thresholds at nonnegative \(x\) are only \(0,2,4\); the truth value of strict or weak stability is constant on each open interval between these values.

**2. Complete stationary-minimum census.** There are exactly \(2^{12}=4096\) spin assignments. The attached standalone integer-only verifier constructs both graph realizations, independently verifies their edge sets, computes for every assignment its zero-field edge energy and magnetization, and evaluates all twelve exact flip inequalities. It finds 45 strict minima in \(0<x<2\), consisting precisely of nine \((-8,4)\) and 36 \((-8,2)\) assignments, and 17 in \(2<x<4\), consisting precisely of nine \((-8,4)\) and eight \((0,6)\) assignments. Each pair here is \((H_0/J,\sum s_i)\). For \(x>4\), only the all-plus assignment is strictly stable. At the three threshold fields it verifies the stated strict and weak counts.

The same enumeration checks \(H_0/J\geq-8\) and \(H_4/J\geq-24\) for all 4096 assignments; nine assignments attain both endpoint lower bounds and have \((H_0/J,M)=(-8,4)\). Since the difference of any competing energy and \(-8J-4h\) is affine in \(x\), it is nonnegative throughout \([0,4]\). Above \(x=4\), the all-plus ground state wins strictly because it has the maximum possible magnetization and is already a ground state at \(x=4\). Thus the stated strict minima are correctly partitioned into ground states and excited traps for every real field, not merely sampled fields. In \(2<x<4\), the down-spin set of a strict minimum is an independent dominating set of \(G\), equivalently a maximal matching of \(Q_3\); its size is three for the eight traps and four for the nine ground states.

**3. Sharp escape barriers for a continuum of fields.** Consider the four closed intervals \([0,1]\), \([1,2]\), \([2,3]\), and \([3,4]\). On each interval the displayed barrier function is affine. For every excited trap and for every one-spin neighbor, the difference between the neighbor's energy and the trap's energy is likewise affine. The verifier checks at both integer endpoints that **every** first flip costs at least the stated barrier, and that some first flip attains it at **both** endpoints. Affinity proves the sharp lower bound throughout the interval.

For the upper bound the verifier constructs, separately for every one of the 36 or eight traps and for each of the corresponding two intervals, a sequence of exactly three flips ending in one of the nine ground configurations. Every intermediate configuration satisfies at *both endpoints* the inequality that its excess energy above the starting trap does not exceed the proposed barrier. Each inequality again extends to the entire interval by affinity. The four interval checks require respectively 36, 36, 8 and 8 successful ground-reaching paths. A one-flip path is impossible from a strict minimum, and endpoints of different magnetization parity require an odd number of flips; thus the three-flip paths are shortest as well as barrier-optimal. This proves the claimed barriers and two maxima for all real \(x\) in the open regimes.

**4. Symmetry.** All 48 signed coordinate permutations act by automorphisms on the twelve midpoint vertices. Applying these permutations to every trap gives two lower-field orbits of 12 and 24 and one upper-field orbit of eight, verified exhaustively by the same exact integer certificate.

## Verification
Run `python3 cuboctahedron_barriers_verify.py` using Python 3 standard-library modules only. It must terminate with the line `CUBOCTAHEDRON_EXACT_CONTINUUM_BARRIER_CERTIFICATE_PASSED states 4096 endpoint_reachability_checks 88`. The verifier itself constructs the complete configuration space and the four sets of interval-wide path certificates; it does **not** extrapolate a sample of numerical field values. The two separate constructions of the graph, the symmetry orbit sizes, field-threshold counts, energy lower envelopes, and boundary-inclusive inequalities are all explicitly checked. Full text of the verifier is included beside this result.

## Relationship to prior work
Karlová and Strečka, arXiv:1611.04301v1 (14 November 2016), study the quantum XXZ/Ising cuboctahedron and explicitly identify the equilibrium Ising one-third-magnetization plateau. That equilibrium plateau is established prior work, not a claim of novelty here. Godrèche and Luck, arXiv:cond-mat/0412077v1 (3 December 2004), explain the physical role of blocked states and energy barriers in zero-temperature single-spin-flip dynamics, mainly for ferromagnets on chains and two-dimensional lattices. The present statement instead resolves the *complete finite frustrated cuboctahedron's strict-trap inventory and ground-reaching minimax barriers*. Previously indexed analyses of crown-graph and wheel-graph spin trapping, an icosahedral one-spin classification, and spin-one ground states on cubic line graphs do not imply these cuboctahedral path barriers; their models, observables or state spaces differ. An unindexed specialization could still precede this result.

## Limitations
No kinetic prefactor, Arrhenius lifetime constant, escape probability, or stochastic transition law is proved. The barrier is a combinatorial minimax energy quantity, not an independently verified physical lifetime. The claim does not extend to multisite simultaneous flips, quantum XXZ exchange, nonuniform bonds or other polyhedral graphs. The proof is a finite exhaustive integer certificate with analytically valid field-interval reduction, not a closed-form non-enumerative classification for arbitrary graphs. Historical priority is assessed only against the inspected accessible sources and indexed records; independent scientific validation is not asserted.

## References
- K. Karlová and J. Strečka, *Magnetization process and magnetocaloric effect of the spin-1/2 XXZ Heisenberg cuboctahedron*, arXiv:1611.04301v1, posted 2016-11-14, https://arxiv.org/abs/1611.04301.
- C. Godrèche and J. M. Luck, *Metastability in zero-temperature dynamics: Statistics of attractors*, arXiv:cond-mat/0412077v1, posted 2004-12-03, https://arxiv.org/abs/cond-mat/0412077.
