# Independent mathematical audit

## correctness

PASS

A fresh exact enumeration built the graph from the frozen LCF offsets (12 cubic vertices, 18 edges), computed all shortest distances by Floyd–Warshall, and for each of the 4096 subsets took its minimum separation count over all 66 unordered pairs. The full vertex set has minimum separation 6, so k=1 through 6 are the only feasible positive levels. Filtering by score and then by smallest cardinality yielded (2,4,5,7,9,11) with counts (2,73,7,35,39,6). Every one-out/one-in move between retained masks was tested and filtered by the Frucht edge condition for slides. Edge counts, component orders and all component radii/diameters matched the six certificate rows, with jump disconnection exactly at levels 3 and 4 and K6 at level 6. At level 6 the slide graph has components of order five and one. Replay: python3 /workspace/branches/f00aeb20-96bc-46a0-9e07-8cadfd3d5fa5/frucht_reproduction.py (fresh code; optional --smoke checks only 256 masks). The submitted Python and C++ code and certificate were inspected, not executed. This is exhaustive on the named finite graph under the stated move rules, not a claim about cubic graphs in general.

## originality

PASS

The general distinguishing-mask criterion and related graph-hierarchy and reconfiguration examples are known. The supported distinct result is the complete Frucht minimum-basis mobility profile, in particular the loss and subsequent recovery of jump connectivity. No matching prior table or general theorem determining that profile was identified in the bounded comparisons.

## value

PASS

The Frucht graph is a standard asymmetric cubic benchmark. Minimum landmark count and fault tolerance do not reveal whether a deployed optimum can move to another optimum. The six-level example establishes concretely that feasible redundancy can increase while optimum jump connectivity disappears and then returns, and that even complete jump mobility can leave a slide-isolated state. Level-specific exact counts and distances are useful benchmark data for reconfiguration, not merely six isolated dimension values.

The dated certificate retains the supplied scientific assessment, sources and limitations.
