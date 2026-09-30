# Independent audit — 2026-09-29
- Source: `2026/09/13/072`
- Assigned/current tree SHA: `0a3d59abdbfd6556b0aa842199c4d6a4766c2615`
- Disposition: **failed**

## Three-axis assessment

### Correctness

**FAILED** — The Morita-separation argument 3-versus-infinite is sound, but the stated stronger cardinality claim |Sub(1_gra)| is countably infinite is not proved. Geometric logic allows set-indexed disjunctions; from a countable family of coherent/regular sentences one cannot conclude that the quotient lattice of geometric sentences is countable. The submitted proof establishes only a strict infinite chain Gamma_n. Thus the headline contains an unsupported cardinality assertion. The committed reproducibility paths are also wrong: the verifier is under artifacts/, not output/artifacts/.

### Originality

**FAILED** — After narrowing to the correct statement, the separation is a routine application of the standard fact that Morita equivalence preserves the classifying topos and hence Sub(1), together with elementary positive-existential normal forms for equivalence relations and the clique hierarchy for graphs. This is an illustrative example of established machinery rather than a substantive new theorem.

### Scientific value

**FAILED** — The correct 3-versus-infinite separator is pedagogically clear but too elementary and instance-specific to support the advertised research-level contribution, especially once the unsupported exact cardinality is removed.

## Independent checks

- verified the equivalence-relation positive-existential collapse to bottom/inhabited/top
- verified K_m satisfies Gamma_n iff m>=n, giving a strict infinite chain
- checked that arbitrary geometric disjunctions invalidate the submitted inference from countable syntax to countable Sub(1)
- verified the committed verifier is artifacts/verify_ledger.py and not output/artifacts/verify_ledger.py
- confirmed main has no changes under this record since the inventory commit

## Limitations

- The audit does not assert the exact cardinality of Sub(1_gra); only the submitted countably-infinite claim is rejected as unsupported.
- Open-access sources were sufficient; Oxford Download was not needed.

## Citations

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/13/072
- https://www.cambridge.org/core/journals/journal-of-symbolic-logic/article/abs/syntactic-characterization-of-morita-equivalence/2AB10C921C8084665316509AA6B3267D
- https://academic.oup.com/book/26735/chapter-abstract/195585960
- https://doi.org/10.1145/1379759.1379763
