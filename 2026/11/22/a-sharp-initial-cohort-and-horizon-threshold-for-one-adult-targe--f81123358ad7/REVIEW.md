# Self-review

## Correctness
**PASS.** The pulse changes only adult survival, so exact integration reduces the objective to maximizing \(A(s)H(T-s)\). The derivative identity and monotonic comparison of \(D(s)\) prove existence, uniqueness and a complete if-and-only-if boundary including equality. The formal zero-depletion comparison establishes the strict half-horizon bound for the positive-depletion model. The standard-library numerical checker corroborated the exact example and tested 300 seeded parameter sets (25,556 assertions). Tests are not substitutes for the proof.

## Originality
**PASS on inspected evidence; historical priority provisional.** The 2024 Kummer study analyzes adulticide time-of-day and epidemic simulations, not this one-pulse cumulative linear-cohort theorem. The 2018 Barclay study treats repeated spraying and terminal knockdown, not the exact initial-cohort threshold. The 2022 Agusto work develops necessary conditions in a higher-dimensional epidemic impulsive-control system rather than the all-parameter closed timing law. Related mathematical population-control results concern different intervention maps and objectives. Analytic simplification is elementary once the model is posed, and may be implicitly obtainable through general linear impulse-control theory; independent historical verification remains necessary.

## Value
**PASS.** The exact dose-independent transition distinguishes wasting a transient adult-only treatment on the initial adult stock from waiting for protected immatures to emerge. It gives a complete benchmark, a sharp horizon threshold, and a strict pre-midpoint bound for the timing problem that simulation papers typically treat by scenarios. A two-stage idealization cannot replace operational mosquito-control studies or epidemiological optimization.

Self-review: passed. Independent audit: not yet performed.
