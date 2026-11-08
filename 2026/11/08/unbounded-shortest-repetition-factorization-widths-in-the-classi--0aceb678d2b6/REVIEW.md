# Scientific review

## Correctness — PASS

The valuation equality \(p(2^kq-1)=(k+\nu_2(q))\bmod2\) permits a complete case split on the odd part of any candidate period. For odd part at least \(5\), mismatches at \(q\equiv2\pmod4\) recur more frequently than the required comparison length; for odd part \(3\), adding mismatches at \(q\equiv3\pmod4\) does the same. The remaining dyadic period has mandatory mismatches with gaps at most three times the period, yielding a strict endpoint-growth bound. Every dyadic block in the witness factor is checked algebraically to be a square; iterating the endpoint bound proves the lower bound. An independently written finite dynamic program verifies the concrete shortest widths for the first ten witnesses, and exhaustive bounded index/period tests check the structural assertions. These computations are diagnostics, not an infinite proof. The upper and lower bounds, index conventions and endpoint strictness agree.

## Originality — PASS (subject to bibliographic uncertainty)

Shallit and Xu (arXiv:2311.14961, §§2–7, first public 2023-11-25) define shortest repetition factorization and prove bounded behavior for selected other automatic words; their Rudin–Shapiro theorem concerns unbounded *longest*, not shortest, factorization widths. Their paper does not investigate the classical period-doubling word or prove the present positive unbounded-shortest-width result. Goc and Shallit (arXiv:1207.5450, Theorem 3) prove unrestricted least-period existence for the same word; their statement allows factors shorter than twice the period and therefore does not imply or negate the dyadic repetition-period lemma. Currie (arXiv:2303.14539) classifies avoidable patterns and properties of period-doubling, without addressing shortest repetition-factorization width. Bognini and Ammar (arXiv:2511.20881) study kernel/gap factorizations, not minimum exponent-at-least-two factor counts. Bognini, Kaboré and Kientéga (2020, DOI:10.17654/DM025020143) study Ziv–Lempel and Crochemore decompositions based on prior occurrence, a different factorization objective. Broader mathematical-search queries on the claim and its aliases identified no exact earlier classification. An equivalent unindexed treatment or implicit consequence of further period-doubling square catalogues remains possible; searches are evidence of a gap, not proof of novelty.

## Mathematical value — PASS

The published repetition-factorization problem motivates the invariant directly. This result separates the classical period-doubling word from the bounded-width regimes already known for other highly structured automatic words, with explicit witnesses and two-sided logarithmic growth bounds. The structural theorem determines all possible periods of actual repetitions (in contrast to the much weaker least-period-of-any-factor spectrum), and forces a strict multiplicative constraint on every factorization step. Period-doubling has uniformly bounded monochromatic-run length, so the construction cannot be reduced to trivial factorizations across exponentially increasing constant runs. The exact minimum width for every witness remains open; the growth-order theorem is independently meaningful.

## Remaining scientific limits

No exact equality is claimed for the two-sided bounds. The standalone checker covers finite positions and sizes only. Complete indexing of all historical mathematical literature is not guaranteed; independent audit is not performed.

Self-review: passed. Independent audit: not yet performed.
