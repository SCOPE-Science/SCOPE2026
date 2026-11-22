# Scientific review: two-parameter ternary multiplier collapse

## Correctness (C): PASS

The exact quantified domain is \(2\le r\le k-2\), with integer multipliers \(L_r=(3^r-1)/2\) and \(M_{r,k}=3^{k-1}+L_{k-r}\). The proof establishes a first-collision lemma: a repunit constraint imposes gap \(r\), and the sparse top digit plus the lower consecutive block creates a digit-\(2\) collision at most \(r-1\) positions after any first forbidden short gap. The preceding digit coefficients are at most one; a later input digit cannot intervene before the collision. This eliminates a possible carry-cancellation objection. The opposite inclusion follows from disjoint multiplier blocks when gaps are at least \(k\). Exact Python enumeration verified 75,600 finite input words in 48 parameter/depth combinations, while the infinite conclusion follows only from the proof.

## Originality (O): PASS, with priority risk

The 2013 Abram–Lagarias paper establishes general intersection automata and the already known repunit gap/dimension family; its Theorem 4.8 includes related constraints from successive two-digit multipliers \(3^j+1\). The boundary \(r=k-1\), which would recover such a multiplier, is excluded from the novelty scope. The 2015 follow-up treats \(2\cdot3^j+1\) and \(3^{2j}-3^j+1\) rather than the interior multiplier \(3^{k-1}+L_{k-r}\). The present claim is a uniform *equality of languages* for a genuine two-parameter family, not a numerical evaluation of a finite automaton or a restatement of the previously known dimension formula. Published-record searches and accessible prior-claim checks yielded no stronger statement that entails this exact interior family. General automaton methods make an indirect earlier derivation possible; an independent priority determination remains open.

## Mathematical value (V): PASS

The motivating problem is the explicit structure of simultaneous multiplicative translates of a \(3\)-adic Cantor set, whose automata can grow rapidly and whose dimensions do not usually identify the actual sets. The theorem collapses two genuinely different digit constraints to one exact forbidden-gap shift for every interior parameter pair. This yields all finite-prefix counts, a simple recurrence and Hausdorff dimension without parameter-specific automata. It is a structural simplification of an infinite arithmetic family; these consequences are given only as consequences, not separate originality claims.

## Closest literature and limits

- W. Abram and J. C. Lagarias, arXiv:1308.3133v1 (2013), Theorems 4.2, 4.7, 4.8, and general Algorithm A/B. Covers the repunit and boundary mechanisms but no stated interior mixed-multiplier identity.
- W. C. Abram, A. Bolshakov and J. C. Lagarias, arXiv:1508.05967v1 (2015), sections on the families \(2\cdot3^j+1\) and \(3^{2j}-3^j+1\), and Appendices A–B. Related multiplier families and entropy comparisons, no stated equality for the present parameters.

An earlier implicit equivalent derived from general automata remains a residual originality risk. The checker covers finite inputs; correctness of the infinite statement is established by the written proof. Independent mathematical audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
