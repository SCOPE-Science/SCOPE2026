# Independent mathematical audit

## correctness

PASS

Ragnarsson–Tenner's wedge theorem and affine cycle count give integral freeness, degree n−1 and rank L_n−2. Each cell is a directed induced graph from an injective word, with its simplex orientation fixed by the increasing label order. Thus the augmented Hopf trace has prefactor (−1)^n, and a selected support orbit contributes −1 regardless of its size. For a rotation with d orbits, proper supports lift paths (so invariant directions are independent); on full support exactly the two consistently directed cycles are excluded, including d=1,2. For d≥3 use the chromatic evaluation at −1. The cyclic coloring/vacancy transfer acts on the constant-vacancy and constant-ordinary-color sector by [[1,q],[1,q−1]], with the remaining eigenvalue −1 of multiplicity q−1. Power traces are polynomials in q; at −1 the two roots have power sum (−1)^d L_d, and the remaining contribution is −2(−1)^d. Direct sums give Z_1=Z_2=1. For reflections the endpoint-swapped edges forbid their whole orbits; the remaining path lengths k, k+1, k−2 give the three cases. The weight Q_l satisfies Q_l=Q_(l−2)−Q_(l−1) (sum the last bit, giving factor 0 after a vacant penultimate vertex and −1 after an occupied one), with Q_0=1,Q_1=0. This gives (−1)^l F_(l−1) and covers n=3 and the empty quotient path at n=4. Independent replay: python3 /workspace/review-evidence/reproduce.py 3, log /workspace/review-evidence/3.txt, all 66 character values for 3≤n≤8 using enumerated word classes; this finite check does not prove the general formula. The supplied exact cellular script computes and prints the characters and checks kernel stability but does not automatically assert equality with the theorem; its terminal PASS alone is not a character-comparison certificate. Supplied scripts were inspected, not executed.

## originality

FAIL

A distinct indexed manuscript, f3988be26e9c, demonstrably gives the same all-n character for the same Boolean complex and action. This is a coverage verdict for the frozen contribution, not a claim that the indexed manuscript preceded it or that either was derived from the other. The comparison uses the exact theorem, not title similarity or inaccessible evidence.

## value

FAIL

The full symmetry invariant would be a motivated contribution if not already covered. The frozen statement, however, differs from the independently indexed all-element formula only in expressing the reflection recurrence in Fibonacci notation. It adds no distinct invariant, scope, or mathematical consequence to that coverage. This is not a criticism of the correctness or usefulness of the common theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
