# Review: exact directional fragmentation of quantum dimers on the four-cube

## Correctness — PASS
The theorem concerns exactly 272 perfect matchings of one sixteen-site binary cube and all 64 subsets of six directional square-plaquette moves. Two independently organized exact enumerators agree on every state; mask-adjacency BFS and edge-set DSU agree on all 64 component spectra. All eleven row sums are 272 and the class multiplicities sum to 64. The RK ground-space statement follows from the positive semidefinite graph-Laplacian form: zero energy requires and is implied by component-constant amplitudes. The finite proof is exhaustive and makes no infinite-size extrapolation. `verify_directional_plaquettes.py` replays the certificate using only Python 3.

## Originality — PASS on examined evidence
Syljuåsen (2005) establishes the underlying planar quantum-dimer plaquette Hamiltonian. Klivans–Saldanha (2020), Example 2.2, already explicitly record the isotropic four-cube 272 states, the 264-state component and eight frozen configurations. Hartarsky–Lichev–Toninelli (2023) give higher-dimensional connectivity when longer cycles are permitted. Published exact flip-distance records also analyze the full six-orientation graph. The present claim is only the **64 anisotropic move-repertoire classification, eleven symmetry-class component spectra, and sharp five-versus-six-type disconnection**. The inspected stronger or equivalent formulations do not determine the components of the edge-deleted subgraphs. Unindexed prior equivalent computations remain a residual historical-priority risk.

## Mathematical value — PASS
Anisotropic suppression of selected plaquette resonances is a natural physical control on accessible dimer Hilbert-space sectors. This gives a complete exact small-cube benchmark, identifies the sharp six-type necessity for full mobile-sector connectivity, and translates each of the eleven component spectra into the positive-weight RK zero-mode multiplicity. The result is finite but concerns a natural full classification, not a cosmetic reformulation of the isotropic census.

## Scientific limitations
The conclusion is restricted to the sixteen-site four-cube, uniform inclusion or exclusion of all four faces of a chosen coordinate plane type, square-flip moves alone, and positive enabled coefficients for the RK ground-space statement. No results about spectral gaps, non-equilibrium mixing or larger cubes are claimed. Independent scientific audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
