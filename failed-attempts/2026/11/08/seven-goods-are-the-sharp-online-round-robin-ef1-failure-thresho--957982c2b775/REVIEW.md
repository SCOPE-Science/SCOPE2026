# Independent mathematical audit

## correctness

PASS

Correct for pure equilibria, the scope explicitly stated in RESULT.md line 25. With at most six goods, a target bundle of size two has a second pick still available at every agent's first turn. A pure unilateral deviation can secure that good regardless of the continuation; monotonicity and the Nash condition give the requisite singleton bound. Bundles of size at most one are immediate. For seven goods, additivity makes already acquired utilities sunk and the number of remaining goods determines the mover. Independent exact backward induction matched the certificate in all 128 states and 448 state-action alternatives. It gives path (1,2,3,5,4,6,7), utilities (2090,1120,1042), and B's minimum value after removal from A's bundle is 1286, exceeding B's own value by 166. All 128 bundle values per agent are distinct. The unqualified phrasing in line 5 should not be read as a pathwise result for mixed equilibria. Indeed, with five goods X,Y,H,L,Z valued by B at 4,4,10,1,0 and by A and C at zero, A can first take X; after B takes L, C can mix between H (probability 1/20) and Z, and A then takes Y. After B instead takes H,Y,Z, respectively, C and A can take (Y,L),(H,L),(H,Y), leaving B payoffs 10,4,1 versus expected 10.5 from L. Completing B's prescriptions by backward induction yields a mixed SPNE in which the H branch violates EF1. This does not affect the explicitly pure claim.

## originality

FAIL

A distinct Resultary record already states the identical existential seven-good sharp boundary in the same observed sequential game and proves the pure-NE lower bound in a broader number-of-agents regime. Its strict additive witness is numerically different and has a stronger equilibrium characterization. The exact theorem is covered; neither the new table nor the different certificate is a new sharp threshold.

## value

FAIL

The sharp boundary itself is mathematically meaningful, but already established with equally strict valuations and broader lower-bound coverage. The alternative table and its replay add no identified equilibrium phenomenon, useful restriction, or stronger conclusion beyond the indexed result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
