# Independent mathematical audit

## correctness

PASS

The cyclic Fano lines are translates of {0,1,3} modulo seven (every nonzero difference occurs once). Independently enumerating deletion masks and repeatedly stripping remaining vertices of degree at most one tests foresthood exactly: every forest strips to nothing, while no cycle can lose its first vertex under this rule. The feasible counts at sizes zero through six are 0,0,0,0,70,812,2254, and the fourteen five-vertex kernels give exactly the seventy four-vertex masks. Different kernels meet in at most two vertices and two minima in one kernel meet in three, so the only shared size-five neighbor of two minima is their common kernel. At cap five, each of fourteen such centers has five size-four neighbors, each with nine private size-five leaves; the remaining 168 size-five vertices are isolated. This gives 882 states and 700 edges with disconnected optima (also isolated at cap four). Flipping one mask bit gives exactly the TAR adjacency. At cap six all-source breadth-first searches give one component, 3136 states, 8008 edges, and eccentricities 10,11,12 at sizes 4,5,6 respectively. All 2415 unordered optimum pairs attain the symmetric-difference lower bound, with distance counts 140,630,980,665 at 2,4,6,8. Attaining the bound forces exactly one flip per differing coordinate and no other flips, proving monotonicity. Over all unordered distinct pairs, the excess counts at 0,2,4 are 4532374,382466,840, with no other excess. A separate DFS-based enumeration reproduces the finite census. Replay: node /workspace/heawood-replay.js. Both supplied scripts were inspected, not executed. These checks are exhaustive for the specified graph and capacities, not for arbitrary subcubic graphs.

## originality

PASS

The known Heawood geometry directly explains the nontrivial cap-five components; a cited general exchange theorem may also cover optimum connectivity at cap six via a two-step lift. The distinct supported contribution is the complete Heawood TAR census including the isolates, the all-optimum Hamming isometry at the threshold, and the unrestricted cap-six metric and excess census. Similar statements on Petersen and the four-cube are substantive analogues, not Heawood results.

## value

PASS

For the canonical Fano incidence graph, the first feasible buffer that merges the optimum components is also sufficient to make every optimum pair Hamming-isometric, even though hundreds of thousands of larger feasible pairs still require detours. The exact component, eccentricity and excess counts distinguish global connectivity from this stronger local constraint and provide useful finite benchmarks for feedback-set reconfiguration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
