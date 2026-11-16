# Self-review

## Correctness — PASS
The explicit symmetric-normalized Laplacian Fourier symbol uses the spine degree three and leaf degree one; the characteristic roots give disjoint spectral bands \([0,2/3]\) and \([4/3,2]\). A single Bloch direction below the upper-band onset makes local sampling a scalar multiplier, so Plancherel yields exact sharp bounds. Endpoint Gram eigenvalues give the universal best lower bound; strict monotonicity of the Bloch eigenvector angle proves attainment and uniqueness. Varying the angle on an interval proves uniqueness of the tight quadrature sensors. Above the onset, the rank-two fiber on positive measure disproves injectivity of every one-row sampler. The included checker tests 5,495 structural and synthesized-signal assertions. A finite check is not an infinite proof.

## Originality — PASS with disclosed risk
published-finding corpus queries included normalized pendant-line Bloch sampling, one-channel complex mixing, graph Laplacian bandwidth transitions, and tight sensors. The closest returned work concerns finite cycles, finite graph dynamical sensing, and two-time diffusion on a line; those assertions do not imply the exact pendant-graph classification. An accessible full HTML paper by Giannoni proves general vertex-subset graph sampling and does not state the local complex sensor or sharp formula. Tanaka–Eldar's full HTML develops abstract generalized sampling rather than this exact case. The directly motivating Bulai–Cabrelli–Cordero–Molter–Saliani preprint was accessible only by abstract; comparison with its entire text remains unresolved and could reveal related explicit examples. No claim is made that semantic searches prove priority.

## Value — PASS
This is a natural minimal periodic decoration of the integer lattice with a genuine two-band normalized spectrum. The result distinguishes stable, optimally robust, and exactly tight *one-measurement-per-cell* recovery, and establishes the sharp impossibility threshold when two independent Bloch modes occupy the same fiber. The explicit optimal sensor is unique at every nontrivial bandwidth, while a physically interpretable quadrature sensor gives exact energy preservation. These conclusions are stronger than a routine numerical sampling example, but the result is restricted to this natural graph and sampling architecture.

## Scientific limitations
No uniqueness assertion concerns spatially varying or dynamical sensors. The underlying Fourier diagonalization and Hilbert-space min–max method are established tools. Full-text coverage of the most relevant new preprint could not be completed. No external or independent mathematical audit has been performed.

Self-review: passed. Independent audit: not yet performed.
