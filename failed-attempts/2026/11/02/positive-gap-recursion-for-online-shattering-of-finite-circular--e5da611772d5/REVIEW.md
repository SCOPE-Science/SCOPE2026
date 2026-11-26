# Independent mathematical audit

## correctness

PASS

After at least one positive answer, the excluded vertices form either the empty set or one contiguous subinterval of one gap. A positive query splits the gap; a negative query pins an excluded block, whose two endpoint choices are independent threshold classes of sizes a and L-a. Balanced threshold trees and cardinality give their individual ranks; concatenation and induction on the queried factor give additivity. The two first-query branches are complementary, and no split remains for a singleton (including the n=1 boundary after the first query). This proves the exact recurrence and partition state bound. A fresh calculation evaluated it through 40, reproducing all ten thresholds. Direct explicit-concept minimax through six gave ranks 1,2,3,3,4,4 and class sizes 2,4,8,14,22,32. All 16 paths of the frozen six-vertex witness realize distinct valid concepts. The balance obstruction also checks: after query 0 with answer positive, reflection swaps the two balanced choices 2 and 4, so one can take 2. After its positive branch only 4 balances, and after its positive branch no query balances. The source's wording about reflection is imprecise but does not change the argument. Replay: branches/85039b4a-708f-4e3f-8be7-3b9f8ce330b2/independent_cyclic_arc_check.py and INDEPENDENT_CHECK.txt. The through-40 check used the proved gap recurrence; the independent explicit-concept method was used only through six. No uploaded code was executed. Alternating labels on four points and realizability on three give the VC assertion, and the two equally spaced marked points give the stated asymptotic by the threshold product.

## originality

FAIL

Demonstrated broader catalogue coverage, not just a match of titles, dates, or small ranks. The distinct finite-chain record gives an exact theorem D for nonempty interval unions on arbitrary disjoint finite blocks. The cyclic recurrence is obtained from this theorem by complementation after the first query and a singleton dummy block. The dates do not establish historical order; the assessment is of mathematical coverage by the indexed statement.

## value

FAIL

The circular rank and its first cardinality deficit are well-motivated objects. As a distinct scientific contribution, however, the advertised recurrence and finite cutoffs reduce directly to the broader disjoint-block recurrence with a redundant singleton, and the six-vertex witness is a small worked certificate of that mechanically determined case. The static bound and order-of-growth context do not supply a separate substantial remainder.

The dated certificate retains the supplied scientific assessment, sources and limitations.
