# Independent mathematical audit

## correctness

PASS

At each cubic vertex the edge omitted by a Hamiltonian cycle gives one perfect matching edge, and two distinct matchings give an alternating two-regular difference on their active vertices. Thus a move requires testing connectivity of the entire difference, not just its size. A fresh exact enumeration branches on all 1024 subsets of spokes: after deleting the endpoints of selected spokes, a rim has either an even cycle (two matchings), a disjoint union of even paths (one forced matching), or an odd path (no matching). This exhausts the possibilities without relying on the frozen matchers. It gives 36 complementary (10,10) factors and 24 Hamiltonian factors. All 276 unordered pairs give 84 connected differences of size 10, 60 connected of size 18 and 132 disconnected, size counts 10:84, 12:60, 16:60, 18:60, 20:12. All states have seven neighbours and their two-step balls are the whole state set. The local degrees are five twos and two zeros; the degree-two vertices form one simple pentagon, giving 24*5/3=40 triangles. Pairwise intersections independently give two common neighbours for all 192 nonadjacent pairs, and 60/24 adjacent pairs with two/zero; the local structure alone is not used to infer the nonadjacent count. An explicit isomorphism to the subset incidence graph transports the states, and enumerating the coordinate action and exact edge images checks state transitivity and edge orbits of sizes 60 and 24. These are exhaustive finite checks, not a general claim about other graphs. Replay: python3 -B /workspace/reproductions/3.py.

## originality

PASS

The static 24-cycle count and matching-complement model are background. The distinct claim is the first legal exchange length and the complete independent local, metric and orbit counts for the induced Hamiltonian state space. The closest same-move and same-graph records each differ on a hypothesis decisive for the transition graph; the result is not implied by either. Bounded best-of-knowledge judgment, not historical certification.

## value

PASS

The Desargues graph is a natural small symmetric cubic graph and single-cycle trades are the canonical components of perfect-matching differences. Imposing Hamiltonicity can forbid short trades; pinning down the first allowed length, two-step reachability and the two local kinds of moves tells a researcher how the Hamiltonian constraint changes that dynamics. Neither the static count nor an arbitrary enumeration cutoff is the contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
