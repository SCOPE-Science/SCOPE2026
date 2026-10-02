# Independent audit — SCOPE-20260914-046

Audit date (UTC): 2026-10-01 (UTC)

## Final claim

Under the stated BPRE and stretched-exponential displacement assumptions, environment-dependent centering and scaling yield the displayed annealed Cox-cluster extremal-process limit with time-reversed-environment marks and the corresponding maximum law.

## Correctness

**FAIL** — The proof sketch imports a homogeneous stretched-exponential extremal-process theorem and replaces the deterministic growth factor by exp(L_n(Y)), but it does not prove the conditional genealogical and uniform error estimates needed for a random offspring environment. The stated BPRE assumptions (law of large numbers for L_n, L1 martingale convergence, and the displayed cluster summability) do not by themselves justify the claims that no-big-jump, multiple-big-jump, shared-ancestry, and intermediate-jump contributions retain uniform exponential margins conditional on the environment. The centering script only illustrates one fluctuation mechanism and cannot certify the point-process convergence. This is a theorem-level gap, not a failed numerical check.

## Originality

**PASS** — The checked primary literature separates the two ingredients: Dyszewski-Gantert prove the stretched-exponential extremal process for a homogeneous branching random walk, while Bhattacharya-Palmowski treat branching random environment with regularly varying displacements. No source checked proves their Weibull/random-environment combination, and Resultary found no distinct covering theorem.

### Equivalent formulations

Aliases and equivalent formulations were compared against the closest primary sources; the assessment follows implication rather than title matching.

### Broader coverage

The checked broader theorems do not imply the exact final claim under the same hypotheses.

### Exact database or table

No finite database/table comparison is decisive for this theorem claim.

### Claim versus prior implication

The checked primary literature separates the two ingredients: Dyszewski-Gantert prove the stretched-exponential extremal process for a homogeneous branching random walk, while Bhattacharya-Palmowski treat branching random environment with regularly varying displacements. No source checked proves their Weibull/random-environment combination, and Resultary found no distinct covering theorem.

## Value

**PASS** — A valid theorem combining stretched-exponential one-big-jump asymptotics with BPRE genealogical clustering would be a substantive extension linking two established extremal-process regimes and would clarify the role of random centering and reversed environments.

## Source inspections

- The extremal point process for branching random walk with stretched exponential displacements — https://arxiv.org/abs/2212.06639 — PARTIAL_COVERAGE: Covers stretched-exponential displacements in the homogeneous branching setting, not a random offspring environment.
- Extreme positions of regularly varying branching random walk in random environment — https://arxiv.org/abs/2101.05369 — PARTIAL_COVERAGE: Covers regularly varying heavy tails, not the Weibull/stretched-exponential regime.
- Published-results semantic search — https://github.com/Resultary/2026/tree/main/2026/9/14/SCOPE046 — NO_STRONGER_MATCH_FOUND: The exact record was the direct match; no distinct published SCOPE theorem covered this combination.

## Residual risks

- Literature search is best-of-knowledge and cannot exclude an obscure or unindexed source.
- The audit credits only inspected proofs, source material, and fresh computations described above.

## Disposition

FAILED
