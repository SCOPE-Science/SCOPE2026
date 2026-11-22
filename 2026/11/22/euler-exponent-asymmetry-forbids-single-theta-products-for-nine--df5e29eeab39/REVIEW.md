# Scientific review of the no-single-theta-product theorem

## Correctness — PASS

The theorem is scoped to \(P_0,\dots,P_9\) over \(\mathbb F_{19}\), with integer powers and scalar monomial shifts. Formal Euler exponent uniqueness through degree \(18\) follows by coefficient elimination or the explicit logarithmic derivative recurrence; these steps need no unproved structural lemma. Each candidate theta monomial necessarily has paired Euler exponents at \(a\) and \(19-a\). The 18-case table supplies an incompatible pair for every nonzero component. The bundled verifier computes the components by two independent arithmetic paths and reconstructs Euler factors exactly, so the finite certificate is sufficient to exclude all formal identities in the claimed domain. Risk: transcription or implementation error in the table; independently specified generation paths and the exact source dissection mitigate it.

## Originality — PASS, qualified

The motivating 2026 work establishes two-term theta dissections and expressly presents single-product reduction as Question 2. It does not provide an impossibility theorem in the unrestricted integer-power alphabet, nor does its count of two terms imply impossibility after theta relations. Hirschhorn's 2000 work gives *positive* product identities at modulus \(11\) instead of an obstruction at \(19\). Searches of indexed partition-congruence work and available related records revealed no equivalently strong claim. An unindexed older theta or eta-quotient identity could still encode the obstruction; priority is not independently certified.

## Value — PASS

A specifically posed reduction question receives a complete negative answer for all eighteen nonvanishing classes, with a structural mod-\(19\) invariant that excludes not only quartic products but arbitrary products and quotients in the original theta alphabet. The result clarifies why the two-term dissection cannot be collapsed via identities among those factors. It is a finite exact obstruction with a natural target, not a random finite sample or an unmotivated coefficient coincidence. It does not settle representations with additional theta functions or the other open questions.

## Closest literature and limitations

Bilgici, *Nine-Colored Partition Components Modulo 19*, arXiv:2611.24516v1 (2026-11-18), Theorem 2.3, Theorem 3.2, and Section 8 Question 2, is the direct source. Hirschhorn, *Winquist and the Atkin–Swinnerton-Dyer partition congruences for modulus 11* (2000), shows the contrasting positive phenomenon. See RESULT.md for exact scope, proof and reproducible computations. An independent mathematical audit remains necessary before treating the priority assessment as definitive.

Self-review: passed. Independent audit: not yet performed.
