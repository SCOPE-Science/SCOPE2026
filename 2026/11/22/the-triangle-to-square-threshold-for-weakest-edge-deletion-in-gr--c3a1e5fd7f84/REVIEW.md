# Self-review

## Correctness — PASS

The claim concerns the precise integrated full-time Frobenius discrepancy of graph heat semigroups after one unrenormalized edge deletion. The finite-dimensional Sylvester formula in `RESULT.md` is a consequence of exact heat integration on the mean-zero space. On triangles, exact polynomial factorization proves strict sign preservation for all positive real conductances; all polynomial coefficients and identities were checked by `CHECK.py`. For the four-cycle, four exact rational values establish a strict non-weakest-edge optimum. The argument establishes an infinite family of triangular weights; finite numerical searches are not the proof.

## Originality — PASS within searched evidence

The motivating 2025 graph diffusion paper studies surrogate ODE solutions; the 2019 pseudoinverse sparsification work and 2026 polynomial-graph-filter stability source use different fidelity objectives. A 2026-11-17 preprint describes diffusion spectral error and is treated as the closest prior objective, but the inspected sections provide a general evaluation technique rather than a universal triangle edge-ordering theorem or the sharp four-cycle threshold. published-finding corpus searches for equivalent and stronger rankings returned spectral-gap, heat-gradient and positivity findings, all with different predicates. Remaining risks include historical special cases and partially inaccessible full texts. A search absence is not a proof of global originality.

## Mathematical value — PASS

Single-edge pruning under fixed conductances is an elementary but mathematically motivated graph diffusion simplification. The triangle-to-four-cycle threshold supplies the first exact obstruction to using edge conductance alone to select the least-damaging deletion for trajectories over all time. This contrasts with optimizing spectral gaps or preserving Laplacian forms, and the positive triangle law paired with the explicit counterexample is structurally more informative than a floating-point example alone.

## Limitations

The claim does not address arbitrary graph topologies, simultaneous deletion, normalized Laplacians, rescaling, or fixed-time error. All computations use exact algebra; historical priority is provisional where full primary material was unavailable.

Self-review: passed. Independent audit: not yet performed.
