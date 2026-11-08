# Self-review

## Correctness — PASS

For a nonconstant prefix, the maximal terminal run is \(a^r\) with a different symbol \(b\) immediately before it. The two terminal palindrome predicates distinguish whether a next symbol equals \(a\), equals \(b\), or avoids both. The first two classes permit exactly one candidate; the third permits at most \(q-2\). This bound is repeated after the first change, with initial choices \(q(q-1)\). It is sharp only for words avoiding equalities at distances one and two, which have only trivial palindromes. Every quantifier, including \(n=2\), \(q\ge4\) and the fully constant case, has a separate place in the proof. Center-based and interval-based full enumeration agrees within the tested ranges; it is not used to extrapolate the all-length result.

## Originality — PASS (with residual priority risk)

The 2010 introduction to maximal-palindrome fingerprints addresses counting *distinct* profiles for alphabets through three and reconstruction. The 2013 work addresses pal-equivalent pattern matching. The 2016 published article develops online multiple matching. Itzhaki (2025) proves a reconstruction–proper-coloring correspondence and minimal-alphabet results. A correspondence for individual fingerprints does not itself imply a sharp maximum across all fingerprints; no inspected statement derives that maximum. Searches for the maximal-fiber alias, radius signature, sharp formula, and proper-coloring viewpoint returned different problems rather than a dominating theorem. A full text of the 2010 chapter was not accessible, so a hidden equivalent proposition remains possible; originality remains a self-review.

## Value — PASS

The inverse-fiber maximum is a natural worst-case reconstruction ambiguity for the full palindrome-radius array, an established string-pattern representation. Its closed form and unique maximizing observation provide a complete answer for every alphabet of at least four symbols; for a four-symbol DNA alphabet the worst ambiguity is \(12\cdot2^{n-2}\). Neither code performance nor independent publication novelty is claimed.

## Scope and limitations

Only labeled linear words, full ordered palindrome-radius arrays, \(q\ge4\), and \(n\ge2\). Not the complete distribution of fiber sizes, not \(q\le3\), and no noise model. The 2010 primary chapter remained inaccessible in full; priority risk is explicitly acknowledged. The independent audit has not been conducted.

Self-review: passed. Independent audit: not yet performed.
