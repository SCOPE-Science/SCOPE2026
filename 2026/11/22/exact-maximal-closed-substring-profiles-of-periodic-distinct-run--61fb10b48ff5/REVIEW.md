# Independent mathematical audit

## correctness

PASS

The explicit domain is n >= p, with pairwise distinct run letters, positive lengths and q >= 3; the introductory wording does not extend it to n < p. A witnessing border is necessarily the longest border: a longer border would supply an intervening occurrence of any shorter border. Each mixed factor determines its start phase by the first directed transition it contains. Therefore a mixed witnessing border must return after exactly p symbols, and any available one-character extension still has a mixed complete-return border. A nonconstant unary return must connect successive copies of its run type and have equal endpoint fragments of length h: any longer fragment or intervening run gives a third occurrence. For h < r_i a one-letter extension destroys the unary witness; a mixed witness would have length |X|+1-p = 2h-r_i+1 <= h and hence cannot reach a boundary at the extended prefix. At h = r_i any available extension has a mixed border one period apart. Whole runs are maximal. In the whole prefix p <= n < p+r_0, any mixed border would have length at most n-p < r_0, impossible; every unary border has a third occurrence in the first run. At equality the full first-run return witnesses closure, and above it the length n-p mixed border does. Counting runs, partial returns, and the whole prefix gives the stated formula, including the increments at the wrap to the next cycle and the density limit. An independent longest-border/first-return checker passed exact endpoints and cardinalities on 1,172 periodic prefixes; the proof, not this sample, establishes the quantifiers.

## originality

PASS

Supported distinct contribution: the explicit interval families and phase-sensitive count for all prefixes of length at least one period in the stated q >= 3 family. General consecutive-border-pair/RLE methods, the initial-period distinct-run count, and binary complete-power analogues are not new. The available comparisons do not supply the periodic all-prefix profile without additional classification and counting.

## value

PASS

Periodic run encodings are a natural benchmark for maximal-closed-substring output size. The phase-specific intervals and exact changes in total count locate where output turns over inside a period, not just its asymptotic density or its size at complete powers. This gives a usable exact benchmark for positional enumeration at moving cutoffs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
