# Self-review

**Correctness — PASS.** The result covers all six permutations of the triple `01?` and arbitrary infinite directives, including the single persistent-hole exception. An explicit infinite-recurrence lemma ensures that every extremal tail factor can be realized after a phase shift; the three exact hole-count and fixed-sign phase multisets then give max/min recurrences. A complete induction uses the balanced-ternary carry inequality to identify their solutions as opposite digit weights. Sliding one-position windows proves there are no gaps in Parikh counts. The standalone finite checker was run on the package candidate and passed 1794 phase cases, 100000 digit cases and 8960 word-window cases. Finite tests are not the proof.

**Originality — PASS, qualified.** The fully inspected guiding preprint arXiv:2112.12125 gives ordinary complexity exactly \(2n\), but does not state the Parikh/digit-weight formula or prove its unboundedness. arXiv:2011.00453 assumes bounded abelian complexity and cannot imply this result; Khodier's 2026 relevant thesis sections concern ordinary factor complexity and critical exponents. Searches included Stewart, choral, Sierpiński gasket, Parikh, Toeplitz, Abelian complexity, and balanced-ternary aliases, as well as related mathematical results and claims. No exact or stronger covering theorem was found. The risk of unindexed prior equivalents is not eliminated.

**Mathematical value — PASS.** The claim is a full exact all-length Parikh classification for an uncountable, foundational Toeplitz family studied for ordinary complexity in 2021. Its weight formula identifies sharp infinitely many length-wise minima and logarithmic maxima, proving that these linear-factor-complexity words are uniformly unbalanced. It is not a finite table or a parameter substitution.

The main scientific limitation is the six-template setting; vector occurrence frequencies and other Toeplitz alphabets are outside the theorem. The computed tests were run with a finite prefix and do not constitute independent external validation.

Self-review: passed. Independent audit: not yet performed.
