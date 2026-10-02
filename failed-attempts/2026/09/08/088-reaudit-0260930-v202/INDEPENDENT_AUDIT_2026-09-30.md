# Independent audit — SCOPE-20260908-088

Audit date (UTC): 2026-09-30 (UTC)

## Final claim

All 15 nonempty symmetric normal Cayley graphs of A5 are connected Ramanujan graphs; their exact spectra are those obtained from the standard A5 character table, the minimum degree is 12, and the elementary absolute character-sum estimate certifies 12 of the 15 cases.

## Correctness

**PASS** — The standard A5 conjugacy classes were rebuilt directly from all 60 even permutations; class sizes 1,12,12,15,20 and inverse-closure were verified. Exact character orthogonality and all 15 normal-Cayley eigenvalue formulas were recomputed, and every Ramanujan inequality holds. Connectedness follows because a nonempty union of nontrivial conjugacy classes generates a nontrivial normal subgroup of the simple group A5.

## Originality

**FAIL** — The complete claim is mechanically implied by two standard prior ingredients: the classical A5 character table and the standard normal-Cayley character formula. There are only 15 nonempty unions of the four nonidentity conjugacy classes. Evaluating the formula and comparing with 2 sqrt(d-1) is a finite table calculation, not a new implication beyond those known data. The Frobenius-group literature is not itself broader coverage of A5, but explicit prior A5 wording is unnecessary because the claim follows directly from standard published representation data.

### Originality checks

#### Equivalent formulations

Searches: published-results semantic semantic search for A5 normal Cayley Ramanujan spectra; Search for A5 normal Cayley character-spectrum classifications.

Evidence: The published-results index returned the present record as the exact phrasing match.; The spectra are identical to the central-character scalars from the classical A5 table..

Reasoning: Changing from Cayley-graph language to central character sums yields the same finite calculation.

#### Broader coverage

Searches: Hirano-Katata-Yamasaki arXiv:1503.04075 full text; standard normal-Cayley spectral formula and A5 character data.

Evidence: The Hirano-Katata-Yamasaki theorem inspected in full text concerns Frobenius groups and does not include A5.; Nevertheless, the general normal-Cayley character formula plus the known A5 character table determines every claimed spectrum without new mathematics..

Reasoning: The decisive broader coverage is the standard representation-theoretic formula together with a complete known table, not the Frobenius-group theorem.

#### Exact database or table

Searches: published-results semantic exact A5 15-graph table search.

Evidence: No separate exact 15-row table was located in The published-results index..

Reasoning: Absence of a preassembled table does not create originality when every row is mechanically generated from standard published data.

#### Claim versus prior implication

Searches: Normal Cayley eigenvalue formula; A5 character table.

Evidence: For a normal connection set S, each irreducible character gives the scalar eigenvalue |chi(1)|^{-1} sum_{s in S} chi(s); all inputs for A5 are classical.; There are only 15 nonempty unions to test..

Reasoning: Prior facts directly imply the audited claim by routine substitution and arithmetic.

## Value

**FAIL** — This is a known-table recomputation over 15 cases. It gives a tidy reference table but does not isolate a motivated unknown invariant, structural lemma, counterexample, or nontrivial boundary that survives the value bar; the result is essentially a textbook application of the normal-Cayley spectral formula to the smallest nonabelian simple group.

## Source inspections

- **Package exact A5 verifier** — RESULT.md; artifacts/verify.py; artifacts/census.json. Trigger: Correctness. Material read: Complete result, verifier, and table. Method: Independent reconstruction in exact quadratic arithmetic plus permutation-model class enumeration. Assessment: Correct finite calculation. Evidence: All 15 Ramanujan inequalities and the 12/15 elementary-bound split reproduce.
- **Ramanujan Cayley graphs of Frobenius groups** — https://arxiv.org/abs/1503.04075. Trigger: Claimed program context and broader-coverage check. Material read: Full-text theorem scope and setup. Method: Primary-source comparison. Assessment: Does not cover A5 because its theorem is for Frobenius groups. Evidence: The inspected theorem hypotheses are group-family specific.
- **Expander Graphs in Pure and Applied Mathematics** — https://arxiv.org/abs/1105.2389. Trigger: Ramanujan background. Material read: Background definitions as cited. Method: Context comparison. Assessment: General background, not an A5 classification. Evidence: No specific 15-case A5 result is needed for the originality failure.

## Residual risks

- The correctness calculation is exact except for the optional numerical adjacency-matrix cross-check, which is not needed.
- A published paper may already list these exact 15 spectra explicitly; that would only strengthen the originality failure.

## Disposition

FAILED
