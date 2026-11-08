# Scientific review: adjacency-distinct subsequence universality

## Correctness — PASS

The result fixes the ambient alphabet and counts labeled words, explicitly including the empty word in the rational series. The greedy-arch characterization is proved in both directions by a constructive missing-subsequence witness; in the adjacency-distinct language the transition counts are exactly \(q-1\), \(s-1\), and \(q-s\), including the closure state. The resulting scalar-state recurrence is solved algebraically without analytic assumptions. The number of minimum-length universal words follows from independent permutation-block counting. Every claimed attainable index–length pair is constructed. For the probabilistic conclusion, each post-boundary collection phase has the same conditional length law, so strong Markov/letter symmetry gives i.i.d. arch lengths; the explicit geometric sum justifies both renewal limits. Tests independently compare the rational identity, exact state recurrence, brute-force words, and direct subsequences. Risk: finite checks alone would not prove the result, but all infinite steps are covered by the analytic and combinatorial arguments.

## Originality — PASS, with stated bibliographic limits

The most relevant primary source, Barker et al., *Scattered Factor-Universality of Words* (arXiv:2003.04629), supplies the arch framework but not a bivariate enumerator for the class with all identical adjacent pairs forbidden. Adamson, *Ranking and Unranking k-subsequence universal words* (arXiv:2304.04583), supplies algorithms for unconstrained alphabets. Adamson et al., *k-Universality of Regular Languages* (arXiv:2311.10658), supplies counting algorithms for arbitrary DFA-recognizable languages, which *could calculate instances* of this problem but does not state the all-alphabet closed rational law, exact shortest count, complete support classification or renewal limit. Searches for the equivalent terminology *Smirnov/Carlitz words*, adjacency-distinct or no-immediate-repeat words, and coupon collection did not identify the combined theorem. Publicly indexed earlier mathematical findings on binary unconstrained universality, insertion radii, Dyck constraints, and binary run-limited languages have distinct assumptions and do not logically entail the displayed all-\(q\) formula. An unindexed equivalent special-case enumerator or independently derived renewal result remains a residual risk; a failed search is not a proof of novelty.

## Mathematical value — PASS

The constraint of forbidding immediate letter repetition is the natural complete-graph path language and the simplest fully symmetric nontrivial regular sublanguage of the unconstrained universal-word problem. The full rational length–index distribution for every alphabet size is an exact natural invariant, not a finite cutoff or arbitrary parameter slice. It implies the sharp minimal-length count, a genuine alphabet-two versus alphabet-at-least-three support dichotomy, and exact universality density and Gaussian fluctuation constants under the uniform proper-word source. The stand-alone expectation of a first cover time is classical in spirit and is not asserted to be a separate discovery. The value lies in the combined exact enumerative and renewal characterization.

## Literature and limitations

- Barker, Fleischmann, Harwardt, Manea and Nowotka, 2020, arXiv:2003.04629: arch characterization, basic universality; not this specific constrained all-alphabet enumerator in the inspected material.
- Adamson, 2023, arXiv:2304.04583: unrestricted word counting/ranking; not an evaluated adjacency-distinct closed form in the inspected material.
- Adamson, Fleischmann, Huch, Koß, Manea and Nowotka, 2023, arXiv:2311.10658: algorithms for general regular languages; algorithmic coverage is acknowledged, but an explicit uniform symbolic answer is not furnished in the inspected counting section.

The claim assumes the fixed full ambient alphabet and uniform forbidden self-transitions. It does not cover arbitrary directed forbidden-pair graphs, nonuniform transition weights, or alphabets growing with length. Source coverage is bounded by the named primary inspections and public searches, not a global bibliographic guarantee.

Self-review: passed. Independent audit: not yet performed.
