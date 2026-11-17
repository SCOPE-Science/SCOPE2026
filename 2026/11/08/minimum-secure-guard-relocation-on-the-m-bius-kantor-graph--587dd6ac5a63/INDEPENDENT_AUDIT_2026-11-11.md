# Independent mathematical audit

## correctness

PASS

Construct GP(8,3) by u_i-u_(i+1), u_i-v_i and v_i-v_(i+3), with 16 vertices and 24 edges. Test each subset S for domination and for each outside vertex v the existence of a selected adjacent defender u whose replacement gives ordinary domination. Exhaustive independent bitmask code over all subsets of sizes 0..7 returns none of size below seven and 336 size-seven secure dominating configurations. Exhaustively building secure-to-secure one-vertex jumps yields 1392 edges, one connected component, eccentricities 288 at seven and 48 at eight. Restricting to adjacent slides yields 528 edges, one 288-vertex component and 24 isolated K2 components, with degree and eccentricity histograms stated in the result. A second exact incidence-model verifier explicitly checks an isomorphism and agrees; no randomized inference is used.

## originality

PASS

General secure domination papers develop algorithms or host-edge deletion stability, not the exact 336-configuration relocation graph of GP(8,3). The prior Möbius–Kantor zero-forcing reconfiguration theorem uses minimum ordinary zero-forcing sets (1704 size-six sets) rather than minimum secure dominating sets (336 size-seven sets), so no implication. Search did not reveal an equivalent secure-guard relocation classification; originality remains best-of-knowledge.

## value

PASS

Exact minimum secure guard placements and their resource-preserving mobility are natural combinatorial protection invariants. The sharp separation between connected unrestricted relocation and 24 isolated slide pairs within a mostly mobile 288-state component is a motivated and complete finite phenomenon, useful in relocation model comparisons.

The dated certificate retains the supplied scientific assessment, sources and limitations.
