# Independent audit — SCOPE-20260912-084

Audit date (UTC): 2026-10-01 (UTC)

## Final claim

Any proper continuous open discrete self-map of the Cartan group C≅R^5 with compact branch set is a homeomorphism and therefore has Brouwer degree ±1.

## Correctness

**PASS** — The Cartan group is topologically R^5. The open 5-ball is homeomorphic to R^5, and R^5 has trivial fundamental group at infinity. Kauranen-Luisto-Tengvall Proposition 4.3 therefore applies and gives homeomorphism; degree ±1 follows for a self-homeomorphism.

## Originality

**FAIL** — The full topological statement is a direct special case of the published Proposition 4.3.

### Equivalent formulations

Equivalent after the standard homeomorphism between the open 5-ball and R^5.

### Broader coverage

It strictly covers the single Cartan/R^5 application.

### Exact database or table

Specifically inapplicable.

### Claim versus prior implication

The record follows immediately from the published theorem plus the topological identification C≅R^5.

## Value

**FAIL** — The specialization requires only the standard facts C≅R^5 and trivial fundamental group at infinity. It is a routine parameter/application corollary and does not add a new motivated boundary, structural lemma, or exact invariant.

## Sources inspected

- On proper branched coverings and a question of Vuorinen — https://pmc.ncbi.nlm.nih.gov/articles/PMC9311082/ — COVERING: Proposition 4.3 states for every n>=3 that a proper branched covering from B^n with compact branch set is a homeomorphism when the image has torsion-free fundamental group at infinity.
- Published Resultary SCOPE084 — https://github.com/Resultary/2026/tree/main/2026/9/12/SCOPE084 — SELF_MATCH: The exact record was the direct match.

## Limitations

- This does not prove that an independently defined analytic quasiregular map on the Cartan group is open and discrete.
- Nonproper maps and noncompact branch sets are outside the statement.

## Disposition

FAILED
