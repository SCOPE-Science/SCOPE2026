# Independent mathematical audit

## correctness

PASS

Avoiding 1000 propagates any zero triple to a left-infinite tail, and avoiding 1110 propagates any one triple to a right-infinite tail. If both occur, the zero and one tails are disjoint and in that order; taking any intervening string u of length j between a chosen zero triple and the one tail creates the actual forbidden 000u1^(j^2+3). Conversely an admissible finite word with neither triple extends by alternating on both sides; one with a zero triple has only an initial long zero run, which extends left while alternating can extend the triple-free remainder right; the reverse-complement gives the other extension. These extensions prove the finite-factor criterion globally. Run-length compositions give 2F_(N+1) short-run words and F_N-1 words of each one-tail type for N>=3, and the first two lengths agree directly. A minimal word other than the two short guards must start with exactly a zero triple and end with exactly a one triple, with no other triple internally, since either one-letter deletion must be legal. A nonempty middle must start in 1 and end in 0, and these conditions also suffice. The four-state core is irreducible and has cycles of lengths two and three, so its endpoint-restricted counts have its full Perron growth. The factor language is regular (union of the core and the two one-tail regular languages); the infinite antidictionary prevents finite type. At generator level j there are 2^j words of length j^2+j+6, proving zero limsup growth; the infimum cannot be negative, even under the untruncated log convention, because every presentation here has infinitely many occupied length layers. As a bounded cross-check I generated legal words via alternating runs of lengths one and two plus their allowable initial/terminal long runs, then exhaustively checked one-letter deletion over all binary words through length 15. For example at N=8,12,15 the factor counts are 108,752,3192 and the minimal forbidden counts are 1,7,28; exact sets and formulas agreed. This test checks the consequences of the proved extension criterion, not the bi-infinite implication by itself.

## originality

PASS

Best of knowledge only for the direct binary run-guard realization with its complete literal language and antidictionary, not the general entropy separation, the sparse long-generator device, the standard Fibonacci composition count, or binary existence under unspecified recoding. The closest four-letter construction accounts for the mechanism but not the new literal model and exact classification; nearby binary antidictionaries concern different run languages and growth.

## value

PASS

The markers-on-a-binary-alphabet problem is a motivated structural constraint, and the construction gives a concrete test case for generating-forbidden versus minimal-forbidden entropy. The exact obstruction language and factor criterion permit use as a fully specified witness rather than as a generic existence statement. Its value is in making infinitely many minimal obstructions and their maximal growth explicit despite a sparse defining presentation, not in rediscovering Fibonacci numbers or the general entropy-gap phenomenon.

The dated certificate retains the supplied scientific assessment, sources and limitations.
