# Review of the priced wheel spectral-gap theorem

## Correctness — PASS

The claim fixes the graph, conductance signs, weighted-cost constraint, unnormalized Laplacian, and the full family of nonnegative allocations. The proof independently derives universal inequalities from the hub-cut Rayleigh vector and both first Fourier modes. Optimizing their affine envelope gives exact aggregate weights. The explicitly diagonalized uniform wheel saturates those bounds, and the equality case in the Fourier test forces every individual rim weight to agree, followed by every spoke weight. This last step proves the claimed optimizer uniqueness and critical optimizer face rather than relying only on group averaging. The standard-library numerical verifier passed 1,279 deterministic checks on its stated finite domain. Remaining limitation: finite checks do not certify universal quantifiers, which rely on the displayed proof.

## Originality — PASS on inspected evidence, qualified

The 2006 continuous-time fastest-mixing paper provides the general cost-budget semidefinite formulation and path/cycle examples, but no two-price wheel theorem in the inspected sections. The 2007 arXiv symmetry paper does solve a wheel **discrete-time SLEM** problem; its Fourier block formula is explicitly credited. An algebraic-connectivity symmetry paper gives a general methodology for a different feasible graph family. The precise new claim is a continuous-time, two-orbit *price* cutoff with a complete set of unrestricted optimal conductances, including rigidity and a nonunique boundary interval. Exact duplicates or stronger reductions in unindexed literature are a residual priority risk; absence from search results alone does not prove novelty.

## Value — PASS

The result resolves a natural network-design decision—whether a ring of costly redundant connections should be funded—for all wheel sizes and prices, and identifies **every** optimal design rather than merely one symmetric certificate. Its sharp threshold \(4\sin^2(\pi/m)\sim4\pi^2/m^2\) implies a nontrivial unit-cost change at \(m=6\), and distinguishes spectral-gap resource allocation from total-effective-resistance design, for which rim spending can remain worthwhile even on large wheels. These are complete economically and dynamically interpretable classifications, not numerical table lookups.

## Literature and integrity limits

Primary texts examined: Sun–Boyd–Xiao–Diaconis (2006), https://web.stanford.edu/~boyd/papers/pdf/fmmp.pdf (formulation and examples); Boyd–Diaconis–Parrilo–Xiao (2007), https://arxiv.org/pdf/0709.0955 (wheel spectral block and discrete-time objective); Ghosh–Boyd (2006), https://www-leland.stanford.edu/~boyd/papers/pdf/eigbounds_laplacian.pdf (algebraic-connectivity symmetry method). Literature equivalence remains possible outside these materials; the verification script supplements, not replaces, the proof. No independent audit is claimed.

Self-review: passed. Independent audit: not yet performed.
