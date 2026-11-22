# Scientific review: uniform-in-time anti-edge pairing

## Correctness — PASS
The exact theorem is proven by an invariant sign-even two-particle basis. Its hopping matrix is written using the unsigned complete-graph incidence matrix; the two squared singular values produce the exact two-frequency pairing probability. Explicit upper and lower bounds have the same leading coefficient in the *all-time* supremum. The classical comparator follows from an exactly lumpable two-state generator, rather than a heuristic mean-field argument. The supplied independent full-matrix numerical checks match 36 quantum/classical cases with maximum deviations below \(10^{-14}\); finite checks are corroboration and not the proof of the infinite-family limit.

## Originality — PASS, with historical-priority risk
The symmetric-square Hamiltonian, hard-core bosons, and general strongly regular spectral methods are not claimed as new. The nearest published result on the *same configuration graph* gives a Laplacian spectrum and spanning-tree product, not its two-frequency unitary pairing probability. Because this graph's degrees depend on the pairing sector, those Laplacian eigenvalues cannot simply be shifted to unitary adjacency evolution. Other inspected papers use a generic graph-isomorphism observable, a lossy double-occupancy model, or one-dimensional interaction-driven co-walking. Direct source/alias and research-record searches did not locate the exact all-time paired-event formula or classical inverse-size comparison. This is evidence of noncoverage, not a certificate of novelty; unindexed equivalent calculations remain possible.

## Mathematical value — PASS
The graph is a canonical cross-polytope/cocktail-party network, and two walkers initially occupy a natural nonedge pair. Even though each particle has many available hops, the total quantum probability of leaving *all* such pairs is uniformly only \(O(1/m)\), with sharp coefficient \(4\). On the same physical time scale classical exclusion has probability approaching \(1-e^{-2\pi}\) of leaving the paired sector. This motivates a precise, mechanistic coherent-confinement benchmark beyond a routine adjacency spectrum computation.

## Scientific limitations
Only two hard-core bosons, identical unit hopping, an initially occupied deleted matching edge, and a two-vertex-part paired observable are covered. The exact result does not imply noise robustness, interaction-induced dimer binding on a local lattice, many-particle versions or confinement to the particular starting pair. Independent external validation and definitive priority determination have not been performed.

Self-review: passed. Independent audit: not yet performed.
