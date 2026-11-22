# Review

## Correctness — PASS

Every conflict-free set omits marked self-loop vertices; mutual attacks make all independent subsets of the unmarked induced forest admissible. Maximal independent sets dominate the unmarked vertices, so the only remaining obstruction to stability is domination of each marked vertex. The forest property implies a neighbourhood-transversal lemma: if none of the marked vertex's unmarked neighbours is isolated in the unmarked induced forest, choose one unmarked neighbour of each such neighbour; acyclicity makes these chosen vertices pairwise distinct and nonadjacent, and any independent extension avoids the entire marked neighbourhood. This proves necessity, including boundary and isolated-vertex cases. The converse follows because every maximal independent set contains all isolated unmarked vertices. The path enumeration uses an explicit four-bit transfer automaton, finite boundary checks, exact characteristic polynomial, a unique primitive recurrent component and the exact integer identity \((T^5-T^4-T^3+T-I)B=0\). These supply a proof for all lengths, unlike finite experimentation alone. The bundled standalone checker independently re-evaluates Dung semantics on 9,987 marked forests and all path markings through 14 vertices.

## Originality — PASS within inspected evidence

Zhang–Liu's path-based 2026 results give broad sufficient criteria mostly for self-attack-free frameworks, with self-loop handling restricted to conditions for stable existence or preferred extensions containing a chosen set. Andrews–San Mauro's symmetric-framework Lemma 20 already identifies preferred with maximal conflict-free sets, which is explicitly credited; this does not by itself give the iff isolated-neighbour criterion or the path-marking enumerator. A related OEIS sequence for minimal dominating sets differs from the new one already at the second nontrivial coefficient. Both actual published-finding corpus and web queries used semantic aliases, local criteria, path enumeration, and the full initial sequence. No equivalent or dominating published assertion was located in inspected material; historical priority is not independently certified. The OUP journal article was available only through indexed substantial excerpts because direct full-text opening redirected unsuccessfully, leaving residual priority risk.

## Value — PASS

General preferred/stable agreement is computationally difficult, and existing theorems emphasize sufficient conditions without self-attacks. The theorem gives a linear-time, necessary-and-sufficient local certificate for every loop marking of any symmetric finite forest; it identifies precisely which self-attacks are harmless to *all* maximal admissible viewpoints. The exact length-generating function then quantifies how rarely agreement survives arbitrary self-attacks along an increasing path. Its denominator has degree five and yields a non-obvious exponential rate strictly below two; the complete census is a natural invariant of this semantic boundary, rather than a rewording of a known path count.

## Sources and limitations

Relevant comparisons: Zhang–Liu (2026), arXiv:2610.30176, relevant full-text HTML sections 1–6; Andrews–San Mauro (2026), DOI 10.1093/logcom/exag036, introduction, Lemma 20 and discussion seen in indexed HTML excerpts; the 2018 survey chapter on symmetric frameworks; and OEIS A253412. Limits: no claim for nonforests, no automated certificate of global literature completeness, some journal full text not accessible, and no independent audit. Checking finitely many examples is only corroboration; the all-order claim rests on the forest proof and exact transfer identity.

Self-review: passed. Independent audit: not yet performed.
