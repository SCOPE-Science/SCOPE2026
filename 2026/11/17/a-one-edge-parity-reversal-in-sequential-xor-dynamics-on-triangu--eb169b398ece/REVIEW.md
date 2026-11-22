# Independent mathematical audit

## correctness

PASS

The final claim quantifies over every k>=1 and every labelled one-visit scan, for current-neighbor self-inclusive XOR on B_k and Q_k. Each local update is an involution; cyclic rotation conjugates products and leaves commute, reducing scans to the t-gap order. The two hub/parity equations yield four parity cases; the nonzero rank-one second-power differences for odd k, k-dimensional fixed space and T^2/T^3/T^4 identities uniquely determine the stated GF(2) rational/Jordan forms and primitive periods. The schedule argument counts each t in (k+2)k! ways; at k=1,2 boundary groups are treated vacuously, not divided by zero. Independently rebuilt adjacency-mask updates exhaustively for both graphs every labelled scan and all 2^(k+2) initial states, k=1..4, checking predicted least periods, conjugacy-relevant orbit counts and schedule frequencies. Also read verification/verify_exhaustive.py and verification/verify_linear.py and inspected frozen tree; finite tests corroborate but do not establish all k. No general scan-with-repetitions claim is made.

## originality

PASS

The exact single-edge editing theorem on the triangular book has a new non-bipartite half: for odd k adding ab preserves similarity for all cyclic scan gaps; for even k it interchanges the pure order-two and irreducible order-three sectors at every gap. The earlier full complete-bipartite schedule theorem covers the Q_k comparison baseline, not the B_k update with a spine. Macauley et al analyze asynchronous cycle rules and general rotation/commutation principles, not this pair or its every-order Jordan response. Search did not show an implication deriving the added-edge spectrum from a broader earlier theorem; historical priority is best-of-knowledge, not proven.

## value

PASS

A one-edge perturbation that reverses scan-cycle regimes in an entire natural graph family is structurally motivated: unlike raw finite census, it exactly answers how a single hub-edge edit changes linear conjugacy classes and frequency distribution for unbounded k. The odd/even threshold is non-obvious, not a renaming of the Q_k theorem, and may be useful for robustness of sequential graph dynamics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
