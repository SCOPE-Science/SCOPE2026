# Review of balanced two-circle quadratic phase retrieval

## Correctness — PASS
The real Hermitian lifting operator is computed directly by its three angular Fourier bands. The independent radius equations eliminate both first-harmonic coefficients, nonquarter-turn angular staggering eliminates the second-harmonic coefficient, and the two radial DC equations leave exactly the nonsingular diagonal kernel. The difference of two rank-one positive matrices cannot belong to that nonzero kernel. Explicit counterexamples certify each parameter boundary. A direct kernel-dimension plus determinant argument proves eight-measurement minimality for complex dimension three. The finite checker reproduces the linear ranks and representative boundaries and Gaussian identity; the universal result is analytical.

## Originality — PASS (qualified)
Pohl–Li–Boche (SampTA 2017) already constructed an eight-point **5+3** design for two circles and proved the general minimal cardinality; these facts are credited, not claimed new. Bodmann–Hammen (2013) gives another eight-measurement circle design on intersecting circles. Chalendar–Partington (2024) studies complete circles; Liu et al. (2026) studies two Gaussian-type channels with infinite sampling. The specific **4+4 staggered-concentric if-and-only-if theorem**, including its exact one-dimensional lifting kernel, is not covered by the inspected statements. The closest earlier related result has **5+5** samples and analyzes positive-semidefinite fibers, so its conclusion does not imply the present sparse-grid result. A prior equivalent construction in unindexed literature remains possible.

## Mathematical value — PASS
Balanced four-per-channel sampling is a natural acquisition budget distinct from the previously known 5+3 distribution. The theorem is a complete classification, not a selected success example: it explains precisely why aligned grids lose phase and why rotating one grid restores global recovery, with exact Gaussian-filter three-tone interpretation. The scope is deliberately limited to degree-two, known geometry, and noiseless data; higher degree and quantitative noise stability remain open.

## Closest sources and limitations
Primary sources compared are Liu–Ning–Wu–Zhang (arXiv:2610.39145), Pohl–Li–Boche (SampTA 2017, full author presentation), Bodmann–Hammen (arXiv:1302.5487), and Chalendar–Partington (arXiv:2403.16255). The first paper's relevant full PDF sections and the full statements of the second through fourth were examined. Publication-priority verification is not independent. General finite-dimensional 8-sample minimality and 5+3 two-radius constructions predate this result.

Self-review: passed. Independent audit: not yet performed.
