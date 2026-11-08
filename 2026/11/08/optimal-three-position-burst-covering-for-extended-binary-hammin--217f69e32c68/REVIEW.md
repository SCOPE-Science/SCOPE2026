# Scientific review — optimal burst covering of extended binary Hamming codes

## Correctness: PASS

For every \(m\ge2\), the parity-check columns \((1,v)\) list all affine labels \(v\in\mathbb F_{2^m}\) exactly once. A two-position syndrome is zero, one labeled column, or a sum of neighboring columns, so the two-position count is governed exactly by distinct neighboring field sums. The noncyclic obstruction is a telescoping-XOR contradiction; the cyclic obstruction is a repeated-element-XOR contradiction. Both use the explicit hypothesis \(m\ge2\), for which the sum of all nonzero field elements is zero. The primitive-element ordering has all neighboring field sums except \(u=1+\alpha^{-1}\), and the missing one appears as a two-apart sum inside a three-position window. The exclusions for the exponent prove this for all admissible degrees, including \(m=2\). Hence the sharp two-position spectrum and radius-three optimum follow without any computational assumption.

The embedded `checker.py` directly enumerates cyclic and noncyclic syndromes for degrees two through eleven, confirms the unique missing syndrome, and exhausts the coordinate orderings at degree three. This tests the symbolic argument but is not an infinite proof. The mathematics assumes the standard existence of a primitive element in each finite field.

## Originality: PASS against inspected evidence, with residual risk

The decisive nearby source is Sac Himelfarb–Schwartz, arXiv:2601.00435, first publicly submitted January 1, 2026. Its Definition 14 and Remark 15 define the coordinate-sensitive burst-covering measure; Example 16 gives a length-eight extended Hamming example of burst-covering radius three. Theorems 17 and 18 provide general parameter inequalities, not a complete-length constructive ordering. The new claim has universal quantifiers over every \(m\ge2\), solves both cyclic and noncyclic coordinate optimization, and sharply counts the accessible syndromes at radius two. The source's length-eight example is already covered and is not treated as novel.

Searches for finite-field ordering/adjacent-difference aliases and relevant indexed research records did not locate a dominating family theorem. The general finite-group terrace literature could contain a combinatorially equivalent ordering fact, so unindexed equivalence and full priority remain risks. This is a reasoned best-knowledge comparison, not a claim of absolute uniqueness.

## Value: PASS

The 2026 source explicitly makes coordinate order part of the burst-covering problem and gives an eight-coordinate demonstration of its importance. A sharp uniform construction and universal impossibility result for the complete extended Hamming family settle the natural order-optimization question, not a short numerical parameter increment. The further exact \(2^{m+1}-1\) syndrome coverage characterizes the optimal partial performance when access is limited to two neighboring coordinates. These statements give a structural access-locality benchmark applicable across all binary extension degrees.

## Limitations and comparison scope

The result is only for extended binary Hamming codes and one burst of bit flips. It does not extend to arbitrary codes, multiple bursts, or deletion noise. Computer checks cover finite degrees; the all-degree claim rests on the algebraic proof. Other primitive elements and field bases generate equivalent valid constructions, but all optimal orderings are not classified. Historical priority has not been independently certified.

Self-review: passed. Independent audit: not yet performed.
