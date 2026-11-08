# Review of the uniform cubic-scroll Hamming spectrum

## Correctness — PASS
The rank-five evaluation map is injective for each \(q\ge4\) because vanishing in two distinct \(y\)-coordinates forces both coefficient polynomials to vanish on at least three distinct \(x\)-values. The proof independently classifies the linear polynomial \(B\) into zero, root-free on the torus (\(2t\) choices), and one-root (\(t^2\) choices), and derives complete quadratic-root counts for each case. The particularly delicate case \(A(r)=0\), \(B=\beta(x-r)\), counts \(3t\) rather than \(2t\) choices of a root-free quotient linear polynomial on the *punctured* torus: the three classes are nonzero constants, scalar \(x\), and scalar \(x-r\). This accounts for the coefficient \(3t^3\) at the next-to-minimum weight. The total multiplicity is \(q^5\). Independent brute-force coefficient enumerations in five finite fields agree coefficientwise; all-field validity rests on the symbolic count, not on the finite checks.

## Originality — PASS, provisional historical priority
The exact uniform full weight enumerator, plus classifications and multiplicities of the two lightest weights, goes beyond the minimum-distance bounds in Hansen (2000), Joyner (arXiv:math/0208155), and Little–Schenck (arXiv:math/0507598), and beyond the five-point polygon identification in Luo–Yau–Zhang–Zuo (arXiv:1402.0060). The latter's Appendix enumerators explicitly apply to dimension-six codes; its Figure 1.3 places this trapezoid in the dimension-five list. Targeted mathematical record searches using both monomial support and scroll aliases returned no equivalent complete formula, and accessible previous findings contained no implication-equivalent claim. The 2009 Yau–Zuo full text could not be accessed; it is especially relevant because it treats dimension-five codes and remains a historical-priority risk. Neither a failed query nor partition membership proves novelty.

## Mathematical value — PASS
The cubic-scroll polygon is a distinguished smooth, degree-three toric surface, not an arbitrary isolated exponent set. The exact eight-term Hamming spectrum for every field size determines all word frequencies, including the second weight (an invariant that differentiates codes sharing minimum distance), and explains extremal supports as unions of toric ruling fibers and one additional section. These exact uniform invariants extend the earlier minimum-distance-focused geometric code literature and are directly reusable in code comparison and weight-based enumerator tests.

## Limitations
The code is defined on the dense rational torus, not on all points of the compact scroll. The proof assumes \(q\ge4\). No independent check is claimed. Full text of Yau–Zuo (2009) was not obtained; historical priority could change after specialist comparison. Finite arithmetic runs are confirmatory only.

Self-review: passed. Independent audit: not yet performed.
