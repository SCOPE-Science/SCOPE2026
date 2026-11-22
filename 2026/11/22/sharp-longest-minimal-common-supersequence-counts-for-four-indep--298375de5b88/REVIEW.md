# Scientific review

## Correctness

**PASS.** Every input embedding pair covers the full word under deletion minimality; length equal to the sum of input lengths would force unique embeddings, contradicted by the relative positions of the specified marker symbols. At length one less than the sum, exactly one letter is shared, yielding two disjoint branches. The central-gap classification proves necessity and sufficiency for all positive parameters, and the independent exhaustive and constructive scripts corroborate the boundary cases. Finite checks do not replace the unrestricted proof.

## Originality

**PASS against inspected literature; residual historical-priority uncertainty.** The 2026 Sopp–Liyanage–Gong–Zhu full article enumerates arbitrary minimal supersequences algorithmically but provides no explicit four-parameter longest-layer formula. The 1996 Fraser–Irving–Middendorf article gives a dynamic program for longest minimal-supersequence lengths, rather than this particular number of maximizers. The closest two public specialized results cover only equal or paired opposite run lengths; their longest-layer identities are implied here and are excluded from novelty. Actual queries checked four-independent-run asymmetry, opposite-run minimal supersequence enumerators and equivalence to previous binomial laws. Earlier unindexed work may cover a more general equivalent.

## Value

**PASS.** This is an exact and sharp count of all extremizing outcomes of a natural sequence-integration problem for every tuple of four independent run parameters. It goes beyond the numerical maximum length or an enumeration algorithm, distinguishes the two forms of symbol sharing and resolves otherwise easy-to-miss one-symbol boundary transitions. It is a complete natural maximum-layer classification; no claim is made about other layers.

Self-review: passed. Independent audit: not yet performed.
