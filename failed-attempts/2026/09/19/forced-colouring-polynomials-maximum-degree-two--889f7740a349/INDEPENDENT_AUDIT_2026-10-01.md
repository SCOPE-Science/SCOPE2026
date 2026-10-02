# Independent scientific audit — SCOPE-20260919-889f7740a349

Audited at: 2026-10-01T13:18:12.002998Z

Disposition: **failed**

## Correctness — PASS

The three-colour path and cycle formulas follow from the independent-set characterization of initially omitted degree-two vertices; the path sign encoding and cycle root-of-unity count are correct. The all-colour packaging follows from the known bipartite two-colour formula, multiplicativity, and the fact that a degree-two vertex cannot be forced when at least four colours are available. The committed exhaustive checker agrees through order eight.

## Originality — FAIL

The central final claim is already covered by earlier published SCOPE records. The 17 September record gives the exact path and cycle three-colour coefficient formulas and the maximum-degree-two multiplicative classification. The 18 September record gives the same path/cycle formulas, independence-polynomial forms, recurrences, and all-colour path/cycle classification. The current transfer-matrix presentation, isolated-vertex two-colour clarification, and minimum-domain corollaries do not create a new implication comparable to the already published classification.

### Equivalent formulations

The current core theorem is an equivalent reformulation of earlier published SCOPE results.

### Broader coverage

Together these earlier results cover the substantive mathematical content of the current record.

### Exact database or table

The relevant published-project database contains exact prior coverage, so this check is decisively negative for novelty.

### Claim versus prior implication

The final claim is mechanically implied by and mostly identical to stronger earlier published records.

## Value — FAIL

As a new scientific finding, the record is mainly an alternate derivation and repackaging of already published exact formulas. The isolated-vertex correction and minimum-domain corollaries are routine consequences and do not supply a separately motivated unknown invariant or boundary theorem.

## Sources inspected

- Exact forced 3-colouring polynomials at maximum degree two — https://github.com/Resultary/2026/tree/main/2026/9/17/SCOPE-forced-three-colouring-max-degree-two--2226d8f07ffd. COVERING: Contains the exact path formula, cycle formula, and maximum-degree-two multiplicative classification.
- Exact forced-colouring functions for paths and cycles — https://github.com/Resultary/2026/tree/main/2026/9/18/SCOPE-forced-colouring-paths-cycles-three-colours--b7cd38cd2fa2. COVERING: Contains the same formulas plus independence-polynomial forms, recurrences, and all-colour path/cycle classification.
- The forced colouring function of a graph — https://arxiv.org/abs/2609.17108. BACKGROUND: Establishes the general invariant and complexity context; decisive coverage here comes from the earlier published SCOPE records.

## Checked sources

- https://github.com/Resultary/2026/tree/main/2026/9/17/SCOPE-forced-three-colouring-max-degree-two--2226d8f07ffd
- https://github.com/Resultary/2026/tree/main/2026/9/18/SCOPE-forced-colouring-paths-cycles-three-colours--b7cd38cd2fa2
- https://arxiv.org/abs/2609.17108
- Resultary semantic search

## Residual risks

- No originality uncertainty remains material because exact earlier same-project coverage is decisive.

## Limitations

- Scientific rejection is for originality and value, not correctness.
- The complete original package must be preserved in the failed-attempt archive.
