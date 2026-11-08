# Scientific review

## Correctness — PASS

The theorem concerns distinct factors in the infinite binary Thue–Morse language. The length-four synchronization property and overlap-freeness are explicitly stated and cited. The proof establishes that the image of each length-\(n\) rotation class remains one inherited class, that each closing extension adds exactly one new member, and that every nonclosing odd-aligned factor has no other occurring circular shift. The last assertion uses the exact count of equal adjacent pairs in each of the two circular matchings. The closed-end factor induction doubles the unique full orbit at dyadic lengths. The published factor-complexity recurrence and the explicit base case finish the proof. The extracted finite test passes but is not used as an infinity certificate.

## Originality — PASS, qualified

The nearest primary work is Cassaigne–Fici–Sciortino–Zamboni (2014), §5.3, especially Lemma 13 and Proposition 15: same language, alignment and a lower bound on isolated cyclic classes. Krawchuk–Rampersad (2018), Proposition 1, already proves the *numerical* dyadic cyclic-complexity formula; this result does not relabel that formula as new. Bell–Shallit (2021) counts complete rotation orbits (Lie complexity) but does not classify the partially represented classes. The new information is the exact membership-size spectrum and the general per-class inflation identity. Targeted comparisons of published claims found no equivalent class-size result or dominating published theorem. An unindexed earlier size-spectrum proof remains a priority risk.

## Value — PASS

A multiset of cyclic-class sizes is a meaningful refinement of both factor complexity and cyclic complexity: it distinguishes one fully represented orbit from many partially represented orbits. The exact dyadic classification and all-length substitution rule supply structural information for subsequent studies of circular factors and motif enumeration, rather than an isolated numerical table.

## Limits and status

The general multiset formula applies from \(n=4\); the explicit spectrum applies at powers of two. The finite checker supports but does not prove the unbounded statement. Mathematical originality has not been independently audited.

Self-review: passed. Independent audit: not yet performed.
