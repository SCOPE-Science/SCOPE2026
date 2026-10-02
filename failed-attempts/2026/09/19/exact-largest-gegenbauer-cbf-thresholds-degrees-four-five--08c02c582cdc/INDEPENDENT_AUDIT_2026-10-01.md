# Independent audit — SCOPE-20260919-08c02c582cdc

Audit date (UTC): 2026-10-01 (UTC)

## Final claim

For the largest Gegenbauer zero, \(F_{4,d}\) is complete Bernstein exactly for \(1/2\le d\le3\) and \(F_{5,d}\) exactly for \(1/2\le d\le4\), with explicit endpoint representing densities.

## Correctness

**PASS** — The degree-four and degree-five Gegenbauer equations reduce to quadratics in \(x^2\), yielding the displayed largest-zero formulas. After translation, the squared scale factors as \(A_nB_{n,d}\). For \(d\le3\) and \(d\le4\), respectively, both factors are complete Bernstein and the weighted geometric-mean closure gives the result. Above those endpoints, the Möbius factor reverses Pick orientation on an interval left of its pole while \(A_n\) has positive boundary value, forcing the continued square root into the lower half-plane. Stieltjes inversion of the endpoint boundary values gives the displayed compactly supported densities; a fresh independent symbolic reconstruction in this run verified both polynomial factorizations and root equations, and fresh quadrature at \(s=0.2\) and \(s=2\) reproduced both endpoint representations to about \(10^{-34}\); this did not rely on the saved success log.

## Originality

**FAIL** — FAIL because the exact degree-four and degree-five threshold theorem was already published in SCOPE on 2026-09-18 with the same sharp endpoints \(3\) and \(4\), the same explicit low-degree branches, and the Pick-boundary pole obstruction. The added endpoint density formulas are a direct Stieltjes inversion of the already explicit endpoint functions and do not make the composite final theorem original.

The audit separately checked equivalent formulations, broader coverage, exact database/table overlap, and claim-versus-prior implication. Full source-inspection details and residual risks are recorded in the companion JSON.

## Scientific value

**PASS** — PASS: determining sharp complete-Bernstein ranges for the first unresolved largest-zero degrees is a natural exact boundary problem, and explicit endpoint measures are useful analytic data. The result is nevertheless covered at the theorem level by the earlier SCOPE record.

## Disposition

**FAILED.** A validated finding requires correctness, originality, and value all to pass. The original scientific files and reproducibility artifacts are retained with the failed-attempt package.
