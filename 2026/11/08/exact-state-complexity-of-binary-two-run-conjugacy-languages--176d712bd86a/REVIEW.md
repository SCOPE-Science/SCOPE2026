# Self-review

## Correctness

**PASS.** The claim specifies positive run lengths, full-length rotations, a complete DFA and the precise treatment of initial, terminal and dead quotients. Unique cyclic oriented transitions imply that every mixed prefix and every mixed suffix has a unique phase. The count in proof equation (1) subtracts precisely the collisions among homogeneous suffixes, including the boundary-phase corrections. Three exhaustive algebraic regimes for \(a\le b\) yield the exact quotient profile, whose sum is \(2ab\). An independent direct residual enumeration and a bottom-up minimized trie agree through all 484 run pairs with \(a,b\le22\), and 150 larger seeded pairs agree on the quotient spectrum. Those tests are corroboration only, not proof of the unbounded result.

## Originality

**PASS, with bibliographic uncertainty.** Gabric–Holub–Shallit, arXiv:1903.05442, Section 3 (complete HTML full text inspected) give a global maximum and a structural characterization of extremal circular words. They do not state the exact formula for each two-run pair or the triangular/plateau/triangular quotient-layer profile. Jirásková–Okhotin (2008) and Jirásek–Jirásková (2013) address the general cyclic-shift operation and prefix-free subclasses, respectively; the accessible abstracts do not resolve this special case, and their complete texts were not inspected. Targeted searches for the exact formula, Myhill–Nerode aliases, and two-run cyclic languages did not identify equivalent coverage. Search failure cannot prove priority; implicit or unindexed prior treatment remains the principal risk.

## Mathematical value

**PASS.** The two-run binary necklaces are the minimal nonconstant circular run family, not an arbitrary parameter slice. Their exact deterministic memory cost is the simplest natural structured benchmark for the conjugacy-language state-complexity problem of Gabric–Holub–Shallit. The quotient-depth classification is stronger than a total alone and identifies all minimum and maximum run splits at fixed length, in contrast with worst-case-only estimates. It has a direct automata interpretation and does not rely on a tiny isolated numerical gain.

## Scope and remaining limitations

This result is not an assertion about general necklaces, arbitrary circular-language operations, or nondeterministic state complexity. The source comparison has unexamined older complete texts, so independent bibliography review may alter the originality assessment. No independent scientific audit has been performed.

Self-review: passed. Independent audit: not yet performed.
