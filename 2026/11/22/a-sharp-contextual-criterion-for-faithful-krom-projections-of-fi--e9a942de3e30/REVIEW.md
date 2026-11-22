# Review of A sharp contextual criterion for faithful Krom projections of finite Horn programs

## Correctness — PASS

The proof is an if-and-only-if argument. A one-body replacement weakens the triggering condition, hence the source least model is included in that of every projection. Equality holds exactly when the source least model satisfies every selected unary rule. This yields independent per-rule intersections of available false-body choices across arbitrary contexts. If one intersection is empty, one context per body atom suffices to certify impossibility; a sole \(t\)-premise clause with \(t\) singleton-fact contexts is sharp for every \(t\ge2\). The empty-family, no-proper-rule, and empty-source-model boundaries are included. The body-union completion reconstructs every original rule and uses a faithful first factor. The independently implemented verifier passed 84,168 instance/family comparisons and sharp examples for body widths 2 to 6; these computations do not replace the proof.

## Originality — PASS within inspected sources

Antić 2026, Theorem 66, proves semantic equality under **minimalism**. Its Theorem 68 treats arbitrary programs but guarantees only inclusion of the source least model in the factor intersection. The new result proves exact semantic equality is selectable without minimalism, and precisely decides when one selector works over a prescribed family of fact contexts. The source's Example 69 proves that exact **syntactic** body-union can fail; it does not refute the new semantic result. Antić 2023 studies uniform equivalence between Krom programs, not constrained projection from arbitrary Horn bodies. The 2024 sequential-composition result does not supply a prescribed-context selection criterion. Database searches located related Horn-basis-width and contextual-abduction results on different objects, not an implication of this theorem. Residual priority risk: related closure-system and Horn-abstraction literature may contain equivalent language; access to some public research-record full texts was unavailable. No uniqueness inference is made from absence of search hits.

## Value — PASS

This fills a motivated exactness gap in the central decomposition question: an arbitrary finite Horn program always admits a least-model-faithful selection even where the source gives only overapproximations. Fact additions are a standard notion of robust or uniform program equivalence. The contextual criterion is an exact classification for every family of permitted inputs, with an optimal local failure certificate bounded by body width and a sharp all-context simplification. This is neither a fixed tiny enumeration nor an unmotivated parameter slice. It does not claim full program equivalence or an improved asymptotic complexity class.

## Closest literature and limitations

- Christian Antić, 2026, *Set-like Operations on Propositional Logic Programs*, Theorems 66 and 68 and Example 69, https://www.cambridge.org/core/journals/theory-and-practice-of-logic-programming/article/setlike-operations-on-propositional-logic-programs/2216B8E01234B4A5C4C14F94D401A651.
- Christian Antić, 2023, *Algebraic characterizations of least model and uniform equivalence of propositional Krom logic programs*, Section 5, https://arxiv.org/html/2302.04664.
- Christian Antić, 2024, *Sequential composition of propositional logic programs*, https://link.springer.com/article/10.1007/s10472-024-09925-x.

Only fact extensions and positive definite finite Horn semantics are covered. The necessary Krom selector may depend on the chosen context family and on least-model calculations. Equivalent older closure-theoretic formulations remain a historical-priority risk.

Self-review: passed. Independent audit: not yet performed.
