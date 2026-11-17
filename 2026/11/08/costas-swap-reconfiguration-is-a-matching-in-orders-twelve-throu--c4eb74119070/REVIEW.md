# Independent mathematical audit

## correctness

PASS

The left-to-right prefix search rejects exactly repeated forward displacement differences for each h; every valid Costas permutation survives, so exhaustion is genuine and not partial raw enumeration. The original left-to-right hash-based and reverse-bitmask/direct-retest checkers were inspected. A separate independently written exhaustive C++ implementation generated all valid permutations and directly retested the full Costas predicate after each swap: n=11 4368 vertices, 140 edges, deg0/1/2=4096/264/8; n=12 7852 vertices 136 edges 7580 K1 +136 K2 gaps (8,16,4,0,20,40,8,8,20,8,4); n=13 12828 vertices 88 edges 12652 K1 +88 K2 gaps (12,16,8,4,12,4,8,0,0,8,8,8); n=14 17252 vertices 120 edges 17012 K1 +120 K2 gaps (12,0,20,0,0,8,8,0,12,12,32,12,4). Reverse enumeration is independent by different recursion; matching degree hist and gaps certify exact finite target instances, not an all-n theorem.

## originality

PASS

Drakakis–Healy–Rickard 2008 Table 2 and Section 3.2 were read in full and explicitly contain the aggregate number of Costas pairs at Hamming distance two, including 136,88,120. Those numbers do not determine maximum degree, connected components, or position-gap histogram, which are supplied by independently replayed complete enumeration. Other works concern broader Costas existence or modular index permutations, not direct two-position moves.

## value

PASS

A natural legal-swap reconfiguration graph for Costas arrays has a sharp finite immobility phenomenon: n=11 admits eight degree-two states, but n=12..14 are matchings so no two-step walk visits a third array. The new complete degree/gap refinement is mathematically motivated by connectivity and local search obstacles, not a raw re-tabulation of already known aggregate pair totals.

The dated certificate retains the supplied scientific assessment, sources and limitations.
