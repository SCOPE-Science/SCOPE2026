# Scientific review

## Correctness — PASS

The exact Faulhaber identity \(F=H\circ T\), two triangular parity isometries, and two normalized unit classes for each nonzero valuation shell give an infinite proof. Difference factorizations have precisely one factor of two on each relevant class, so finite-level injectivity and compactness imply exact surjectivity. The zero fiber is isolated, and summing disjoint output balls gives Haar measure \(1/6\). The finite-fiber census and sharp least period follow from an independent argument at each precision. `check.py` passed 32,805 exact assertions through precision \(2^{13}\). Its finite coverage is not used as an infinite-proof step.

## Originality — PASS (historical priority qualified)

Faulhaber's 1631 identity is credited and is not being claimed as new. Lengyel's *On Divisibility of Some Power Sums* (2007), inspected in the published full text, proves special-endpoint two-adic valuations such as \(\nu_2(F(2^m-1))=2(m-1)\); this is not the complete target-value image, image density, exact preimage census, or least-period theorem. The accessible 2013 computational power-sum algorithm addresses evaluation rather than the target-classification statement. Searches of archived mathematical findings and relevant published literature did not reveal an equivalent fifth-power partial-sum image theorem. The accessible comparison does not establish historical uniqueness, and potentially implicit older treatments remain a priority risk.

## Mathematical value — PASS

The fifth-power partial-sum sequence is the first odd Faulhaber case beyond the pure triangular square identity \(\sum_{j\le n}j^3=T(n)^2\). Its extra odd unit factor generates a genuinely distinct, alternating local-solubility law: odd targets occupy \(1+8\mathbb Z_2\), while positive even valuations require odd part congruent to five modulo eight. The exact four-preimage law, singular zero fiber, sharp index periods, finite target counts, and measure \(1/6\) provide a natural complete local classification at every precision, not a hand-selected numerical slice.

## Closest literature, scope, and risks

1. Tamás Lengyel, *On Divisibility of Some Power Sums*, *Integers* 7 (2007), A41, https://math.colgate.edu/~integers/h41/h41.pdf — direct special-index valuation predecessor; full relevant theorem/proof inspected.
2. *Faulhaber's Formula*, https://mathworld.wolfram.com/FaulhabersFormula.html — preexisting polynomial identity and triangular coordinate, not the image theorem.
3. *A Fast Algorithm for Computing Binomial Coefficients Modulo Powers of Two*, 2013, https://onlinelibrary.wiley.com/doi/10.1155/2013/751358 — published Section 4 algorithm excerpt; full publisher text inaccessible in the present comparison.
4. Distinct published classifications of dyadic polynomial images and fifth-power graphs concern different input maps; inspected search-result summaries are not substituted for whole-text negations.

An unindexed historical equivalent and inaccessible plausible sources are residual originality risks. The result is local at two. An independent mathematical audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
