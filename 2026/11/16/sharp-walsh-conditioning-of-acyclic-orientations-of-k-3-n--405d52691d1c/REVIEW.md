# Independent mathematical audit

## correctness

PASS

A directed 4-cycle in K_{3,n} occurs exactly for two incomparable three-bit column supports; any longer directed cycle in a complete bipartite graph admits a chord producing a shorter directed cycle, so acyclic orientation matrices are exactly n-tuples of mutually nested columns. Every column chain is covered by one of six Boolean-lattice maximal chains C_π. Exact inclusion–exclusion of their product sets gives six positive 4-column-character products minus six 3-column {0,v,7} products plus the common 2-column {0,7} product. At u=0 this gives N_n=6·4^n−6·3^n+2^n≡2 (mod 4) for n≥2. Global edge reversal x↦x+1 pairs orientations: odd-weight characters vanish; for even-weight frequencies each reversal-pair contribution is ±2 and there are N_n/2 odd such pairs, so W≡2 (mod 4) and no further zeros. The exact product formula at explicit frequency columns [1]*(n−1)+[7] gives 1+(−1)^n (even n witness 2); [2,3]+[1]*(n−2) gives (−1)^n−1 (odd n≥3 witness −2). Thus min nonzero=2, rank=2^{3n−1}, κ+=(6·4^n−6·3^n+2^n)/2, and the frequency projector is average over global reversal. Independent local exact Walsh butterflies over chain-compatible orientations for n=2,3,4 yielded totals 46,230,1066; zeros 32,256,2048 and sharp gap 2, agreeing with analytic proof. The source checker additionally gives separate topological-sorting acyclicity and all-frequency n=2..5 assertions; those saved logs were not used as proofs.

## originality

PASS

Cameron–Glass–Rekvényi–Schumacher Theorem 3.5 already proves that absence of directed 4-cycles is equivalent to acyclicity of complete bipartite orientations, and their Theorem 3.1 counts these lonesum matrices via Stirling/poly-Bernoulli formulas. These known structural and unsigned results do not state the signed coordinatewise 13-product Fourier function, full parity-determined zero set and sharp 2-valued nonzero gap with explicit all-n witnesses. Other indexed Resultary K_{3,n} calculations concern matchings, four/six-cycle supports or sink restrictions—different subsets of the edge cube. The mod-four argument itself is elementary once the unsigned count is known, so value/originality rests on the complete signed formula and constructive sharp all-size conditioning theorem, not an artificial rediscovery of reversal symmetry. Older specialist lonesum matrix Fourier literature remains possible.

## value

PASS

Acyclic orientations on the smallest nontrivial fixed-left-width complete bipartite family naturally encode 3-by-n lonesum matrices. Exact convolution recovery on the reversal-invariant Fourier range asks for the entire signed transform and smallest surviving multiplier, not just counts. The 13-term product formula and parity-dependent exact 2-witness give an all-order sharp condition law and explicit range projector, a useful precise finite-family harmonic invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
