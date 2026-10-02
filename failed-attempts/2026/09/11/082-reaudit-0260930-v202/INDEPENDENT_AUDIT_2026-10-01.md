# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260911-082`

## Correctness — PASS

The committed ledger and complete enumerator/verifier reproduce all six diagram rows. Summing them gives W_F0=(8,6,4,2), W_F2=(6,6,4,2), W_corr=(1,1,1,1), and therefore the explicitly defined naive expression W_F2+2W_corr=(8,8,6,4) with defect (0,-2,-2,-2). The claim is correctly limited to this arithmetic comparison and does not assert failure of the established real Abramovich-Bertram formula.

## Originality — PASS

No earlier source was found tabulating this exact six-row ledger or this explicitly named naive defect vector. Prior work does cover the genuine real and q-refined Abramovich-Bertram mechanisms, so originality is only for the finite ledger/arithmetic comparison, not for the surrounding enumerative theory.

### equivalent_formulations

Searches: Resultary: F0 F2 real Abramovich Bertram fixed class (2,2) defect -2 r-real floor diagrams; exact W_F0=(8,6,4,2) W_F2=(6,6,4,2) W_corr=(1,1,1,1)

Evidence: The exact Resultary hit was the audited record; no earlier exact ledger was found.

Reasoning: Equivalent formulations as three Welschinger/floor-diagram rows and as the defect vector were searched.

### broader_coverage

Searches: Brugallé-Puignau, Behavior of Welschinger invariants under Morse simplifications, arXiv:1203.2773; Bousseau, Refined floor diagrams from higher genera and lambda classes, arXiv:1904.10311

Evidence: Brugallé-Puignau gives a real Abramovich-Bertram relation; Bousseau proves a q-refined F0/F2 Abramovich-Bertram relation.

Reasoning: These are stronger genuine-theory results, but the record explicitly defines a different naive fixed-coefficient arithmetic comparison.

### exact_database_or_table

Searches: published fixed-class Welschinger/floor-diagram tables for the stated three classes

Evidence: No exact table matching all three archived rows was located.

Reasoning: The finite ledger is not shown to be copied from an external database.

### claim_vs_prior_implication

Searches: real/q-refined Abramovich-Bertram theorems versus RHS_naive

Evidence: The established formulas are not the same as blindly reusing the complex +2 coefficient at each r, which the record explicitly acknowledges.

Reasoning: Prior theorems do not make the naive defect a contradiction; they instead show why the naive comparison is not the correct real formula.

### source_inspections

- **Refined floor diagrams from higher genera and lambda classes** — https://doi.org/10.1007/s00029-021-00667-w. Trigger: Same F0/F2 q-refined Abramovich-Bertram setting. Material read: Open-access article theorem material, including the q-refined Abramovich-Bertram section and Theorem 1.3. Method: Primary-source full-text web inspection. Assessment: Confirms that the genuine q-refined F0/F2 relation is prior work; does not supply the audited naive defect ledger. Evidence: Theorem 1.3 states a q-refinement of the Abramovich-Bertram relation for floor-diagram counts.
- **Behavior of Welschinger Invariants under Morse Simplifications** — https://arxiv.org/abs/1203.2773. Trigger: Prior real Abramovich-Bertram formula. Material read: Primary-source abstract and stated scope. Method: Primary-source comparison. Assessment: Confirms the genuine real surgery relation is prior; the audited record does not contradict it. Evidence: The abstract explicitly says the relation is a consequence of a real version of the Abramovich-Bertram formula.
- **Assigned fixed-class census** — 2026/09/11/082/artifacts/enumerate.py and verify.py. Trigger: Critical six-row finite ledger. Material read: Complete source files and ledger.json. Method: Line-by-line package inspection. Assessment: Supports the exact rows and defect arithmetic. Evidence: The verifier recomputes the six rows and asserts defect [0,-2,-2,-2].

### checked_sources

- Resultary exact-object search
- Bousseau 2021
- Brugallé-Puignau arXiv:1203.2773
- assigned enumerate.py, verify.py, ledger.json

### residual_risks

- Exact numerical ledger originality remains best-of-knowledge.
- The record's artifact_inventory uses output/artifacts although the actual audited files are under artifacts/.

## Scientific value — FAIL

The retained claim is only that a deliberately naive transplant of the complex coefficient gives a small defect in one fixed class, while the record itself stresses that this is not the real surgery formula and does not challenge or refine the known theory. Once the three rows are known, the defect is immediate arithmetic; no structural boundary, motivated invariant, or future mathematical use for this precise naive comparison is established.

## Limitations

- The audit does not dispute the genuine real or q-refined Abramovich-Bertram formulas.
- The exact ledger originality is best-of-knowledge.
- The package metadata references output/artifacts paths although the actual files are under artifacts/.

## Disposition

**FAILED — not a validated finding.**
