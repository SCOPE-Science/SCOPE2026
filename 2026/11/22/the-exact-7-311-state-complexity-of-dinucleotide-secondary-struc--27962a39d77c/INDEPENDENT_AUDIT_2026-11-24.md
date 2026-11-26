# Independent mathematical audit

## correctness

PASS

For a prefix of length r, a newly appended factor occupies r,r+1; precisely the earlier factors ending at most at r-1 are disjoint from it. This gives the frozen recognizer invariant and induction from the empty state, including adjacency, the absent most-recent factor in a one-letter word, and absorption under every continuation after rejection. An independent set-based traversal in /workspace/branches/check_language.py exhausts that state presentation and finds 22,986 reachable states including the sink. It uses full Boolean suffix-evaluation vectors, not the submitted minimizer, to obtain exactly 2,17,2715,6807,7295,7311,7311. Suffix equivalence refines monotonically, and equality at depths five and six is a fixed point of right-congruence refinement, so the resulting classes distinguish all unequal right languages, all attained by prefixes. The strict increase from four to five also witnesses the necessity of length five for some pair. All but the single sink class accept the empty continuation; 4096<7311<=8192 proves the 13-bit state-encoding statement. The same replay checks the literal relation on 349,525 words through length nine, a semantics check rather than the all-length argument. It also tests a second, immediate-update presentation (9,458 reachable states) with the same suffix counts: two distinct overlapping factors cannot be mates because their shared letter would have to be fixed by the involution. Thus 22,986 correctly refers to the particular frozen pre-minimization recognizer, not an invariant of all presentations. The audit concerns only this abstract finite-language claim.

## originality

PASS

The language, its complement orbits, capacity questions and general DFA tools are known. The distinct supported claim is exact Myhill–Nerode complexity and stabilization depth for the entire language. Inspected primary passages give no matching minimization or result that supplies those numbers by substitution, and the exact-count catalogue hit is the assigned record itself. This is a bounded comparison.

## value

PASS

This is the first threshold beyond single-letter pairs in a known four-symbol nonoverlap constraint. The full residual-language invariant determines the exact cost of deterministic online recognition rather than the growth rate of a convenient subfamily. The useful finite cutoffs are a 13-bit state-encoding requirement and an exact five-letter bound on separating distinct states, supporting future state-level analyses of the formal language. This is not a claim about molecular structure, sequence engineering, or any physical assay.

The dated certificate retains the supplied scientific assessment, sources and limitations.
