# Self-review

## Correctness — PASS

The proof checks the complete presentation, an induction eliminating repeated hub letters, and distinct normal forms via leaf-wise morphisms to a concrete five-element transformation monoid. The exact centralizer formulas follow from the verified five-element commuting table, not statistical sampling. The summation and asymptotic step use binomial identities and exact finite monoid size. The embedded checker directly verifies all centralizers for \(m=1,\ldots,5\). Risk: the computation is finite and does not certify arbitrarily many leaves; the written normal-form argument provides that proof.

## Originality — PASS (best-knowledge; residual risk)

Searches covered directed-star Hecke–Kiselman commuting pairs, centralizers, normal forms, exact numerators \(7^m+3\cdot4^m\), and the associated endomorphism census. The 2010 foundational paper provides the presentation and structural idempotent theorem; the 2013 paper treats graph dynamics, focusing on complete acyclic orientations. The 2019 general normal-form paper covers the normalization step, but not this centralizer enumerator. The indexed oriented-star endomorphism paper is the closest same-object result; its accessible summary concerns endomorphism counts and concentration, not centralizer-size multiplicities or commuting probabilities. That paper's complete text was inaccessible; this remains a material historical-priority risk. The prior general normal form makes elementary reductions available, so the new contribution is specifically the exact full spectrum and exponential commutativity law, not an assertion that the normal form itself is new.

## Value — PASS

Centralizer statistics and commuting probabilities are natural invariants of finite noncommutative semigroups. The result determines **every** element's centralizer size, not just a single small numerical count, and gives a sharp exponential noncommutativity law for an unbounded family of finite aperiodic \(\mathcal J\)-trivial monoids. The proof explains why the fixed five-element base gives two independent coordinate regimes and the nontrivial base \(7/9\). It is a motivated exact classification even if the proof techniques are elementary; significance beyond this family is not claimed.

## Scope and verification risk

Only inward-oriented stars, \(m\ge1\); no claim about arbitrary quivers. Tests used actual embedded code, with no reliance on previous executions. The indexed endomorphism comparison was limited to its published search summary; the three arXiv sources' pertinent sections were accessed as full HTML.

Self-review: passed. Independent audit: not yet performed.
