# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260920-828a911cf7d9`

## Correctness — PASS

The exact-CG derivation is valid. Residual orthogonality and search-direction conjugacy give the displayed identity for the squared successive-residual ratio. Kantorovich applied to the current search direction yields the factor \(K^2/d_k-1\); the Euclidean orthogonality recurrence gives \(d_k=1+\beta_{k-1}d_{k-1}\). Dropping \(d_k\ge1\) gives the global sharp factor \((\kappa-1)/(2\sqrt\kappa)\), and the endpoint-eigenvector initial residual attains it at the first step. Solving when this factor is at most one gives the threshold \(3+2\sqrt2\). The inspected verifier correctly corroborates the endpoint examples and sampled all-step inequalities but is not used as proof.

### Correctness sources

- assigned RESULT.md
- artifacts/verify_cg_residual_threshold.py
- current published CG residual-spike frontier

### Correctness risks

- Exact arithmetic and fixed finite-dimensional SPD matrices are essential.

## Originality — FAIL

Current published coverage is decisive for the unchanged final claim. A later published finding gives the same sharp all-step factor \((\kappa-1)/(2\sqrt\kappa)\), the same universal monotonicity threshold \(3+2\sqrt2\), the same two-dimensional sharpness mechanism, and the same fixed-preconditioner consequence in the natural residual norm. The audited \(d_k\) history certificate is not repeated there, but it is a short standard recurrence inserted into the same Kantorovich estimate and does not preserve originality of the unchanged theorem package. Because the covering record is dated 2026-09-21, this is a current-coverage judgment, not a historical-priority finding.

### equivalent_formulations

Searches:
- Resultary query: conjugate gradient residual norm monotone condition number threshold 3+2 sqrt 2 sharp all-step
- Resultary query: conjugate gradient history factor d_k search direction norm residual norm beta recurrence

Evidence:
- The later CG residual-spike theorem matches the central factor, threshold, sharpness, and PCG statement exactly.
- No separate source was found for the \(d_k\) refinement.

Reasoning:
Equivalent formulations through residual ratios, CG \(\beta_k\), Lanczos Schur complements, and Kantorovich bounds were compared.

### broader_coverage

Searches:
- https://github.com/Resultary/2026/tree/main/2026/9/21/SCOPE-cg-residual-spike-condition-number-frontier--df8cc0336f35
- Bouyouli–Meurant–Smoch–Sadok 2009
- Meurant 2020

Evidence:
- The later theorem fully dominates the central scientific claim and additionally gives a conditioning certificate.
- Historical sources already cover weaker all-step bounds and first-step feasibility frontiers.

Reasoning:
A later stronger/current theorem is sufficient to fail current originality even if historical priority is unresolved.

### exact_database_or_table

Searches:
- current Resultary CG findings

Evidence:
- No finite database issue is relevant because direct theorem-level coverage exists.

Reasoning:
The statement is analytic, not a tabulated invariant.

### claim_vs_prior_implication

Searches:
- statement-by-statement comparison with the 2026-09-21 CG residual-spike theorem

Evidence:
- The factor, threshold, endpoint equality family, and PCG transformation coincide.
- The history refinement follows by retaining the standard \(d_k\) factor before the final \(d_k\ge1\) relaxation.

Reasoning:
The small residual refinement does not rescue the unchanged final claim from coverage.

### source_inspections

- **Sharp condition-number frontier for CG residual spikes** — https://github.com/Resultary/2026/tree/main/2026/9/21/SCOPE-cg-residual-spike-condition-number-frontier--df8cc0336f35. Trigger: Exact current semantic match. Material read: Complete published RESULT.md. Method: Full theorem-and-proof implication comparison. Assessment: DECISIVE CURRENT COVERAGE of the central claim. Evidence: It proves the same sharp all-step ratio, the same iff monotonicity threshold, the same first-step sharpness, and the same fixed-preconditioner residual-norm consequence.
- **Assigned CG verifier** — artifacts/verify_cg_residual_threshold.py. Trigger: Required computation check. Material read: Complete source and saved output. Method: Line-by-line inspection. Assessment: Correct corroboration only. Evidence: It checks endpoint sharpness and both global/history bounds on deterministic random SPD cases.

### checked_sources

- https://github.com/Resultary/2026/tree/main/2026/9/21/SCOPE-cg-residual-spike-condition-number-frontier--df8cc0336f35
- https://doi.org/10.1002/nla.618
- https://doi.org/10.1007/s11075-019-00851-2
- assigned RESULT.md and verifier

### residual_risks

- The covering result postdates the audited record, so historical first-discovery priority is not adjudicated.

## Scientific value — FAIL

The sharp CG frontier is mathematically valuable, but as an unchanged research finding it is now duplicated by a current theorem. The only uncovered \(d_k\) clause is a routine history bookkeeping refinement of the same standard estimate rather than a distinct motivated structural result sufficient to sustain the whole package.

### Value sources

- current published CG residual-spike theorem
- assigned history recurrence

### Value risks

- Scientific rejection is not a correctness defect and does not deny historical interest.

## Limitations

- Correctness passes.
- Originality and value fail for the unchanged final package under current published coverage.
- The later covering result postdates this record, so no historical-priority conclusion is made.
- The theorem is exact-arithmetic only.

## Disposition

**FAILED**
