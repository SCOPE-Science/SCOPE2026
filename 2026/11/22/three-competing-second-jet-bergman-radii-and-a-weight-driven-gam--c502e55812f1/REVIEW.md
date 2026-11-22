# Self-review: Three competing second-jet Bergman radii and a weight-driven Gamma peak reversal

## Correctness — PASS
The automorphism unitary identifies the same-site second-jet representer space with the first three Taylor modes. Its exact expansion gives the three-term captured-norm expression, and an exact derivative factorization produces a shifted-Jacobi quadratic and cubic. The Christoffel endpoint transformation strictly interlaces their roots for all \(n\ge3\), \(\beta>1\), yielding exactly three maxima and two minima. Fixed-weight Jacobi-to-Laguerre convergence proves the sharp Gamma boundary law at all three possible optimizers. The \(\beta=2\) ranking is certified by rational root/exponential intervals; the large-\(\beta\) Hermite limit proves the opposite central-peak preference. This forces at least one crossover without alleging uniqueness. The independent three-by-three Gram calculation and the exact derivative identity were tested by the included standard-library checker (98 assertions). These finite tests are diagnostics, not infinite proofs.

## Originality — PASS, best knowledge
The 2019 Qu–Dang adaptive Bergman approximation paper supplies a motivating precursor; only its publisher abstract and metadata were accessible, so a worked-example priority risk remains. The full arXiv Qu–Qian–Deng 2020 text establishes generic multiple-kernel approximation existence rather than this explicit second-jet radial landscape, and the full 2021 Escudero–Haimi–Romero paper treats weighted Fock sampling density. A previously known Bergman value-plus-first-derivative theorem has only two local maxima. A published Gaussian Fock all-jet theorem gives a bulk Hermite scaling, whereas the present disk-Bergman theorem gives a boundary Gamma profile and a weight-dependent winning-peak reversal. DLMF/Gaussian-quadrature tables account for polynomial identities but were not found to give the claimed peak preference or transition. Classical Christoffel-function coverage remains a residual historical risk; negative queries are not proof of global novelty.

## Value — PASS
The measurement consists of a natural and minimal same-site three-jet: value, first derivative, second derivative. Resolving all possible exact best radii for arbitrary degree and positive disk weight is mathematically substantive. The counterintuitive switch of the best high-degree sampling shell as weight varies is a new qualitative geometric boundary, not a small numerical optimization gain. It may guide constrained derivative-sampling placement. Scope is limited to monomial targets and a single sampling site.

## Closest literature and limitations
- Qu–Dang (2019), DOI:10.1002/mma.5648: abstract available, full article inaccessible.
- Qu–Qian–Deng (2020), arXiv:2006.03290: full mathematical HTML checked; existence rather than sharp radial optimality.
- Escudero–Haimi–Romero (2021), DOI:10.1007/s11785-020-01065-4: open-access full text; Fock sampling densities.
- Classical Jacobi and Laguerre results: standard orthogonality/interlacing and fixed-degree scaling, without a sourced equivalence for this global weighted Gamma switch.

The theorem does not claim a unique crossing weight or a globally optimal unconstrained multi-site approximation. The comparison with inaccessible historical full texts is best-knowledge only. Verification is internal to the stated proof and accompanying checker.

Self-review: passed. Independent audit: not yet performed.
