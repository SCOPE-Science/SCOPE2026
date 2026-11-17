# Scientific review

## Correctness

PASS. With integer discrepancy \(H=aN_0-bN_1\), the original transition rule is exactly equivalent to the sign test after a one. The induction on completed one-runs is valid for \(a>b\): after each closed run \(-b\le H\le-1\), and an intervening zero ensures the next run begins positive. The witness \(0^b1^{a+1}0^m1^q0\) is admissible; the complete alternative-position analysis leaves only a possible preceding zero-run of length \(b+1\). That imitation leaves residual discrepancy strictly greater than \(-b\), and the congruence for \(m\) forces its next one-run to have length \(q+1\), not \(q\). The language closure then forbids every return word. The proof handles \(b=1\), strict inequality endpoints, and all coprime denominators. Finite automaton checks corroborate but do not replace the proof.

## Originality

PASS, with historical-priority qualification. Reyes (arXiv:2611.10995v1) derives the governing recurrence and treats integer ratios, explicitly leaving the general classification open. Previously accessible related work already covers rational parameters with numerator at least twice the complementary denominator through a single-run marker, and another result covers smaller-than-half rational frequencies by transitivity; neither proves the new interval \(1/2<c<2/3\). This result adds a second-run modular witness that closes the entire previously untreated rational interval. The founding Becker–Baraviera 2023 article was available only in an introductory preview and metadata, so there is residual risk of an overlooked statement in inaccessible pages. Bounded-density shifts are not equivalent to this history-dependent successor shift.

## Mathematical value

PASS. Transitivity versus nontransitivity is a primary structural question posed explicitly for this family. The theorem resolves an infinite, dense rational set in a whole open parameter interval, not an arbitrary finite sample, and isolates a reusable arithmetic memory mechanism: one run can be imitated after a shift but a second congruence-selected run cannot. It does not answer the irrational case, the uniqueness-of-maximal-entropy question, or shortest-witness optimization.

Self-review: passed. Independent audit: not yet performed.
