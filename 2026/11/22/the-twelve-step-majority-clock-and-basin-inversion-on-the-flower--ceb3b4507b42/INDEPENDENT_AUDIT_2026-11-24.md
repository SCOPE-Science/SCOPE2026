# Independent mathematical audit

## correctness

PASS

The stated spokes, five-cycle and twisted ten-cycle define a simple 20-vertex cubic J5. The majority rule uses only the pre-update state; no tie or symmetry quotient is involved. In the functional graph zero-indegree peeling never removes a cycle vertex. After the queue empties every remaining vertex has positive indegree within the remainder, so the total indegree equals the number of remaining vertices and each component is a cycle. Reverse removal order gives exact first-entry depth and canonical orbit, with one basin per temporal orbit. A separately written exhaustive integer implementation, with NumPy Boolean transitions and its own graph construction, reproduces all entry-period and basin-spectrum tuples: 154 fixed points, 7,397 primitive two-cycles, no longer periods, 874,268 oscillatory initial states, and unanimous basins of 85,522 each. The maximum depth is 12 and exactly 240 states attain it, all entering two-cycles. At x=7581 the 11th and 13th iterates are 10500 and 8452, while the 12th and 14th are both 4232. Thus F^14=F^12 holds globally and F^13≠F^11 as maps. A separate graph input for the dodecahedron GP(10,2) gives 118 fixed points, 9,679 two-cycles, 860,448 oscillatory initial states and maximum depth 7; all three comparisons are reproduced.

## originality

PASS

The supported distinct claim is the exact J5 majority census and sharp clock, with a basin-mass comparison to an already documented different cubic graph. The matching indexed J5 record is the frozen claim itself, not independent earlier coverage. The graph definition, the general eventual period bound, and the dodecahedral comparator are credited background.

## value

PASS

A standard small snark is a natural test of how synchronous majority depends on graph structure at a fixed size and degree. The sharp relaxation time and complete basin distribution are useful exact benchmarks. In particular, the comparison demonstrates that ranking these two cubic graphs by the number of oscillatory attractors gives the reverse ranking from the fraction of uniformly initialized configurations that ultimately oscillate. That contrast uses information neither the general period bound nor an orbit count alone supplies.

The dated certificate retains the supplied scientific assessment, sources and limitations.
