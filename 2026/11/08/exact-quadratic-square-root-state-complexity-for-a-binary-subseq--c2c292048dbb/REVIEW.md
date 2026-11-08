# Scientific review

## Correctness (C): PASS
The statement fixes an arbitrary integer \(b\ge1\), the binary alphabet, scattered-subsequence rather than factor occurrence, and the complete deterministic model. The proof derives the exact acceptance condition using the earliest two zeros in the first copy and includes the otherwise easy-to-miss contribution from the leading ones in the second copy. It explicitly lists all transitions, proves reachability, supplies distinguishing suffixes for every pair of canonical quotient types, and counts the unique identified pair \(Q_{1,1}=R_1\). A re-extracted checker builds and minimizes the proposed automata for \(1\le b\le16\), checks 49,008 direct finite words, and performs a distinct transformation-automaton minimization for \(1\le b\le8\). The Myhill–Nerode proof, not finite experiments, establishes the universal result. The original \(b+3\)-state count follows from standard matched-prefix residuals.

## Originality (O): PASS under the stated comparisons
The most relevant inspected full primary text is Guyot, arXiv:2407.10355, Section 2.1 and Appendix A, treating roots of upward-closed distinct-letter generator families with increasing alphabet; Section 2.2 treats downward-closed roots. Its reported exponential generic lower bounds and a separate quadratic downward-closed case do not entail an exact quadratic expression for the fixed binary generator \(00\,1^b\). Onishchenko, arXiv:2605.02957, addresses the worst-case nondeterministic complexity \(n^3\), a different model and quantification; only its accessible abstract was inspected, so the full-text priority risk is retained. Semantic searches of published mathematical records for binary square-root scattered-pattern ideals, deterministic left quotients and equivalent word equations returned no covering result; the nearest matches instead concern compression and reset thresholds of automata. Search absence is not novelty proof, and historical priority remains uncertain.

## Value (V): PASS
The invariant is the exact quotient complexity of a natural principal upward-closed language under a standard closure-preserving word operation. The formula gives a parametric quadratic blowup with fixed alphabet, a complete state and quotient classification, and an explicit construction, contrasting the linear complexity of the generating ideal. This addresses a specific state-complexity question motivated by prior work on root operations, rather than an arbitrary finite census or a renaming of existing general bounds.

## Limitations
No statement is made about all upward-closed languages, higher roots, nondeterministic minimality, or maximally large worst-case growth. The full text of Onishchenko's 2026 article was inaccessible, leaving a residual risk of implicit special-case coverage. Human historical-priority checking and independent mathematical validation are outstanding.

Self-review: passed. Independent audit: not yet performed.
