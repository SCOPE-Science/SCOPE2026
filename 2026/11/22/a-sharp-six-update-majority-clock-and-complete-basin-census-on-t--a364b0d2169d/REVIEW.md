# Independent mathematical audit

## correctness

PASS

The specified Hamiltonian cycle plus six chords is a 12-vertex simple cubic graph; degree three removes all ties. An independent replay (`node /workspace/branches/replay-majority-census.js`) constructs the entire successor map and runs reverse breadth-first search from precisely the states satisfying F²(x)=x. All 4096 states are reached; the least reverse distance is exactly first periodic-entry time. It yields 20 fixed points, 103 primitive two-orbits and entry counts (226,1226,1364,608,408,216,48). Grouping by orbit yields the fixed and two-cycle basin spectra in the frozen report and the unanimous basin sizes 392 each. The fixed-weight census also agrees. Enumerating images of the ordered Hamiltonian cycle and testing the six chords is exhaustive for vertex automorphisms and gives eight; their actions on temporal orbits give respectively 7 and 29 spatial classes with the reported size multiplicities. The witnessed orbit is 59,118,43,86,41,82,33,66,33, so F⁷≠F⁵; global depth six and periods dividing two give F⁸=F⁶. A separately executed Python replay agrees: `/workspace/branches/e06b8c43-1097-465d-adf2-a547dea5720b/bidiakis_replay.py`. The supplied verification scripts were inspected, not executed. The certificate is exact for this finite graph and rule, not a theorem for arbitrary cubic graphs.

## originality

PASS

The supported distinct finding is the complete Bidiakis-specific finite census and six-step sharpness, not eventual period two or the majority enumeration method. The strongest different nearby results are for different graphs or give only uniform upper bounds. No checked exact table or dominating theorem implies this census; the searches do not prove priority.

## value

PASS

This is a complete benchmark on a named small cubic polyhedral graph that is not vertex-transitive, not a lone run on a sampled graph. The exact sharp clock and distribution distinguish worst-case and typical starts; the per-orbit basins and spatial classes provide information that a graph identifier, an attractor count or the universal period-two theorem cannot supply. A researcher testing finite majority dynamics or symmetry reductions can use these quantities as exact reference values. The value is finite and graph-specific, not a general convergence claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
