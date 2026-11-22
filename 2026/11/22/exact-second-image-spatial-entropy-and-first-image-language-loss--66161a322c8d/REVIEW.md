# Scientific review

## Correctness

**PASS.** The local-rule-to-path equivalence is exact because any finite predecessor block extends bilaterally. Full-subset determinization recognizes distinct image blocks and the minimized deterministic graph counts each once. The leading SCC has size 273 at time two (15 at time one); every other component has spectral radius at most one. Positive integer vectors \(B_t^{99}\mathbf1\) furnish strict componentwise rational spectral inequalities, proving the infinite-length entropy statements via Perron–Frobenius and Collatz–Wielandt. The verifier reproduces all automata and certificate fields, and an independently coded direct enumeration agrees for output lengths one through twelve. Risks: a subtle implementation error in both routes would affect correctness, but proof steps are mathematically explicit; independently check the finite certificate when citing this result.

## Originality

**PASS on inspected evidence, with priority risks.** Badii–Politi (1997) measured the one-step image entropy \(0.6508\), and their second-level language entropy is not the second *temporal* image. De Oliveira et al. (2015) constructed Rule 22 process graphs through time four, a prior general method, but studied graph-state complexity rather than the exact second-step exponential block-growth value. Martínez et al. (2019) discussed Rule 22 periodic states and diagrammatic behavior, not the claimed all-input entropy constant. Chan-López–Martín-Ruiz (2026) proves single-seed support identities rather than full-shift spatial-image entropy. Indexed one-step spectrum and finite two-step word-loss threshold results are stronger in their stated areas, but neither implies the asserted 273-state root or the quantitative entropy gap by direct substitution. An exact value might still be present in unpublished graph data or an inaccessible paper. No categorical claim of historical uniqueness is made.

## Value

**PASS.** Rule 22 is a canonical symmetric nonlinear cellular automaton. The exact first-to-second loss is a natural finite-time dynamical invariant: forbidding two new length-seven blocks does not alone prove that the asymptotic information rate falls. The calculation connects shortest image obstructions to strict Perron growth separation, and supplies a reproducible nontrivial 273-state spectral benchmark for time-evolving spatial languages, distinct from already-known first-image counts and long-time chaos narratives.

## Scope and residual limitations

Only bilateral synchronous full-shift images at times one and two are included. The spectral root is described by a canonical integer matrix rather than a compact polynomial. Full indexed historical coverage is not guaranteed. The exact finite-state certificates are independently reproducible in Python; their reproduction is not an external audit.

Self-review: passed. Independent audit: not yet performed.
