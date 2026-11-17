# Independent mathematical audit

## correctness

PASS

The graph has 19 vertices, 38 edges, degree 4, girth 5. For each spin-up subset S with k vertices, exact energy/J=38-2cut(S)-(h/J)(2k-19). Exhaustive independent vectorized enumeration of every 2^19=524,288 subset, using the original inspected adjacency list but a separately implemented edge-count method, reproduced all twenty maximal cut sizes B_k=(0,4,8,12,16,20,24,28,30,30,30,30,28,24,20,16,12,8,4,0) and multiplicities N_k=(1,19,133,437,703,516,137,4,2,6,6,2,4,137,516,703,437,133,19,1). Comparing all twenty affine energy lines at endpoints 0,2,4 and their slopes proves the all-real-field lower envelope; exact boundary sector ties give h=0:16, 2J:6, 4J:1950. Spin reversal covers negative h. The finite exhaustiveness is a complete proof for this fixed 19-site system, not a thermodynamic-limit assertion.

## originality

PASS

The 1950 independent-set count and hence critical saturation-field degeneracy were published by Cambie–Jooken; this part is expressly covered. Their independence-polynomial and hard-core occupancy work does not give the exact frustrated AF Ising maximum-cut spectrum B_k for non-saturated states, the h/J=2 crossover, or all internal plateau multiplicities. These constitute the surviving distinct full-field classification.

## value

PASS

Robertson’s 19-site unique quartic girth-5 cage is a canonical frustrated finite antiferromagnet. The exact magnetic lower envelope and competing maximum-cut sectors are natural invariants necessary to analyze its field response, not an arbitrary graph slice; all-field completion and exact plateau multiplicities offer a self-contained useful fact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
