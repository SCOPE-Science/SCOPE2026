# Scientific review

## Correctness — PASS
The all-parameter result follows from the two exact equal-read conditions: equal length-\(h\) residue-column differences and zero total change in the first read. Binary mixed columns cannot be shifted; pure columns may be reassigned with their all-one count fixed. This proves every fiber size, complete enumeration, singleton count and maximum. The included direct-word checker passed 120 parameter pairs through length 15 and five further large-parameter identities. Finite verification is corroboration, not an infinite proof.

## Originality — PASS, qualified
The 2022 source by Sporring and Darkner studies precisely the same **linear ordered local-histogram** observation and gives three boundary formulas, but explicitly states that the general number of nontrivial metameric classes has no known closed form (Section 4.4). The November 2022 histogram-algebra followup offers constructive and recursive tools rather than this finite closed census. The closely related published cyclic-weight theorem uses a pure/mixed argument; its cyclic wraparound input and \(\gcd(n,h)\) class structure do not cover the nonwrapping mixed-length residue-column formula for general \(n\). The underlying pure/mixed mechanism is shared, and unindexed or indirectly equivalent old statements remain a priority risk.

## Value — PASS
This solves a concrete finite counting question identified in primary research on binary-signal reconstruction, rather than proposing an arbitrary slice. It yields an explicit zero-error codebook size, counts all nontrivial ambiguity classes, and determines the complete inverse-list distribution and sharp worst-case list size at every source length and window width. Its interest is specifically the discrete local histogram channel; no general claim about noisy or nonbinary sensors is made.

## Scope and residual risks
The result is restricted to binary words and complete ordered unit-stride nonwrapping noiseless readouts. The derivation is elementary once the residue decomposition is recognized; an equivalent statement may be derivable from previously published general histogram algebra, and a closely related cyclic result is known. Originality is therefore based on the checked statement-level distinctions, not on proof-method novelty. Independent expert priority and proof review remain unperformed.

Self-review: passed. Independent audit: not yet performed.
