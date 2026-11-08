# Scientific review

## Correctness — PASS

For each length \(n=tL+r\), the proof determines **all** possible zero counts of periodic factors as a contiguous integer interval. With equal period and unequal zero densities, one interval is coordinatewise to the right of the other, so the intersection is exactly an interval with explicit endpoints. The proved level-set lemma converts a nonempty intersection into the finite disjoint length intervals. Endpoints, the missing full-period length, and the final island follow by integer algebra. The identical-profile case is separate. The checked program independently enumerates actual cyclic factors for 2,870 parameter pairs and 123,682 length/count comparisons, including boundary and post-cutoff cases. The theorem is proved for all positive parameters; the finite experiments are not treated as proof.

## Originality — PASS, with qualification

The closest full primary text inspected is Sugimoto–Noda–Inenaga–Bannai–Takeda, *Computing Abelian regularities on RLE strings* (arXiv:1701.02836; Section 5, especially Theorem 3 and supporting window lemmas). Its finite-input algorithm computes longest common Abelian factors, but neither its theorem nor the inspected derivation states the all-length, infinite equal-period two-run coincidence spectrum, its consecutive forbidden gaps, or the symbolic last length. Fici–Puzynina, *Abelian Combinatorics on Words: a Survey* (arXiv:2207.09937; sections 1 and 3.1–3.2), explains Abelian complexity and periodicity but explicitly excludes algorithmic Abelian stringology from detailed treatment. Grabowski (arXiv:1503.01093) and Alatabbi et al. (2016) give earlier finite-string algorithms according to their accessible abstracts; their full texts were not inspected here. Semantic record searches and claim comparison found no theorem dominating these exact formulas. This is a best-knowledge originality determination, not a proof of global uniqueness in the literature; an unindexed or implicit specialization remains possible.

## Mathematical value — PASS

The longest common Abelian factor is a basic string-matching invariant for which general algorithms are known. A complete symbolic answer for **every pair** of two-run binary cycles with the same period includes all possible factor lengths and the number of shared Parikh classes at each length, not just a one-instance optimum. The counterintuitive fact that a longer common Abelian factor can exist when a shorter length fails (e.g. lengths \(1,2,4\) but not \(3\)) explains the role of disconnected matching islands. Increasing exact gap lengths and the closed maximal-length expression supply structural behavior that is not a routine parameter rename or arbitrary finite slice.

## Limitations and closest sources

No different-period or larger-alphabet classification is asserted. A generic finite-input algorithm and the known single-word Parikh interval are background, not claimed innovations. A direct, previously indexed symbolic specialization was not found. The 2015 and 2016 algorithm papers had only abstracts accessible during this review, leaving some bibliographic uncertainty. Source dates use initial public versions, not later revisions.

Self-review: passed. Independent audit: not yet performed.
