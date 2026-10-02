# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260913-036`

## Correctness — PASS

The non-presheaf conclusion is correct. For a nonempty model, the intervals \(I(a)=(a,f(a))\) with \(a<f(a)\) are proper involution-closed dense-no-endpoint submodels, directed by enlargement, and their union is the whole model. Finite presentability would force the identity to factor through one proper stage, impossible. Thus there are no nonempty finitely presentable models. The fixed-point and fixed-point-free countable examples are non-isomorphic, so the classifying topos has at least two Set-points and cannot be the presheaf topos on the resulting empty/trivial finitely-presentable-model category.

Sources:
- assigned RESULT.md
- artifacts/check.py
- Caramello presheaf-type criterion

Risks:
- Standard classifying-topos/Set-model correspondence is used.

## Originality — PASS

No inspected prior source states the exact dense-order-with-reversing-involution verdict. The general criterion is classical, but the object-specific interval argument was not located as a published specialization.

Sources:
- Caramello presheaf-type framework
- assigned RESULT.md and artifacts/check.py
- Resultary search

Risks:
- The exact negative statement may be folklore.

### equivalent_formulations

Searches:
- Resultary exact semantic search
- web search for dense linear order involution presheaf type

Evidence:
- Only the audited record was an exact match.

Reasoning:
Equivalent finitely-presentable-model and point formulations were searched.

### broader_coverage

Searches:
- Caramello presheaf-type examples

Evidence:
- Decidable linear orders are treated as presheaf type and dense orders as homogeneous models.

Reasoning:
That framework does not state this audited theory's verdict.

### exact_database_or_table

Searches:
- presheaf-type model-theory catalog searches

Evidence:
- No exact database/table entry was found.

Reasoning:
Not naturally table-driven.

### claim_vs_prior_implication

Searches:
- general presheaf criterion versus this theory

Evidence:
- No inspected theorem names this exact theory and returns the verdict without the interval argument.

Reasoning:
Prior implication was not decisive.

### source_inspections

- **Topos-theoretic Fraisse examples** — https://www.oliviacaramello.com/Unification/Concrete%20examples/Fraisse.html. Material read: public examples page. Assessment: framework only. Evidence: decidable linear orders are presheaf type; dense orders appear as homogeneous models
- **Assigned finite checker** — artifacts/check.py. Material read: complete source. Assessment: correct but finite only. Evidence: the infinite proof comes from the interval directed union

## Scientific value — FAIL

The essential obstruction is caused by density and absence of endpoints, not by the involution: ordinary dense linear orders admit the same expanding-interval filtered-colimit obstruction. The record therefore does not isolate a meaningful effect of adding a reversing involution to the presheaf theory of linear orders and is a routine negative check under the required value bar.

Sources:
- Caramello's linear-order example
- assigned RESULT.md

Risks:
- The observation remains pedagogically useful but not sufficiently substantive.

## Limitations

- Correctness passes; rejection is on value.
- The RESULT replay path uses `output/artifacts`, but the actual checker is under `artifacts`.
- Originality is best-of-knowledge.

## Disposition

**FAILED**
