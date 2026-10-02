# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260911-080`

## Correctness — PASS

The committed floor-diagram enumerator was read in full. For the moving weight-2 profile it has two vertices, exhausts all ordered tree/end assignments, thickening choices and compact-edge weights, imposes the stated divergence equations, and returns exactly 10 labelled diagrams with complex total 12, signed total 8 and refined coefficients 2,8,2 at exponents -1/2,0,1/2. The divergence equations force the single compact weight to be at most 2 for this profile, so the script's weight cap 8 cannot truncate the claimed census.

## Originality — PASS

Fresh exact-object searches found no earlier source tabulating this particular moving-contact profile with totals 12 and 8. The general refined/relative floor-diagram correspondence for Hirzebruch surfaces is established prior work, so originality is only best-of-knowledge for the finite numerical specialization, not for the method.

### equivalent_formulations

Searches: Resultary: F2 Hirzebruch E+4F moving contact weight 2 floor diagram signed 8 complex 12 refined 8+2[2]_q; exact profile searches around refined relative floor diagrams on F2

Evidence: The exact Resultary hit was the audited record; no earlier exact numerical table was found.

Reasoning: The same statement can be phrased as the q-refined count of the relative profile or as its q=1/q=-1 specializations; searches used both formulations.

### broader_coverage

Searches: Pierrick Bousseau, Refined floor diagrams from higher genera and lambda classes, arXiv:1904.10311 / Selecta Math. 2021; Cavalieri-Johnson-Markwig-Ranganathan, Counting curves on Hirzebruch surfaces, arXiv:1706.05401

Evidence: Bousseau proves that refined floor diagrams on Hirzebruch surfaces compute relative Gromov-Witten generating series; this supplies the general framework but not the inspected exact profile total.

Reasoning: The prior framework is broader in object class and genus, but the exact small profile still requires a finite enumeration.

### exact_database_or_table

Searches: published tables/databases for relative F2 floor-diagram counts with contact profile (2)_moving

Evidence: No exact database row for this profile was located.

Reasoning: There is no identified external table from which 12/8 can simply be read.

### claim_vs_prior_implication

Searches: Bousseau Theorem 1.1 framework versus the concrete 10-diagram profile

Evidence: The general correspondence validates the meaning of the combinatorial count but does not state the ten-diagram list or numerical total.

Reasoning: The exact numerical specialization was not found as a stated corollary, although it is mechanically obtainable from established definitions.

### source_inspections

- **Refined floor diagrams from higher genera and lambda classes** — https://doi.org/10.1007/s00029-021-00667-w. Trigger: Same Hirzebruch refined floor-diagram framework. Material read: Open-access article landing/full-text theorem material including the abstract and q-refined Abramovich-Bertram section. Method: Primary-source full-text web inspection. Assessment: General framework and correspondence are prior; no exact moving-contact 12/8 row was identified. Evidence: The article states that refined floor diagrams for Hirzebruch surfaces compute relative Gromov-Witten series and proves a q-refined F0/F2 relation.
- **Assigned finite enumerator** — 2026/09/11/080/artifacts/enumerate_f2.py. Trigger: Critical finite census. Material read: Complete source file and complete ledger.json. Method: Line-by-line package inspection and independent algebraic check of the divergence bound. Assessment: Supports the exact 10/12/8 computation. Evidence: The C_mov2 ledger is ndiag=10, complex=12, signed=8, refined {-0.5:2,0:8,0.5:2}.

### checked_sources

- Resultary exact-object search
- Bousseau 2021 / arXiv:1904.10311
- Cavalieri et al. arXiv:1706.05401
- assigned enumerate_f2.py and ledger.json

### residual_risks

- The exact finite profile may appear in unpublished computations or differently indexed tables.
- The computation uses established floor-diagram conventions rather than an independent geometric count.

## Scientific value — FAIL

The final claim is a ten-diagram numerical specialization of an established floor-diagram framework, with no structural theorem, boundary, classification, or externally motivated need for this precise contact profile. The result is correct and reproducible, but under the required narrow-invariant bar it is mechanically obtainable from known rules and the record itself disclaims a broader recursion or priority claim.

## Limitations

- The audit validates the stated combinatorial convention, not an independent geometric reconstruction of the corresponding real invariant.
- The exact numerical originality conclusion is best-of-knowledge.
- The package metadata names output/artifacts paths although the actual audited files are under artifacts/.

## Disposition

**FAILED — not a validated finding.**
