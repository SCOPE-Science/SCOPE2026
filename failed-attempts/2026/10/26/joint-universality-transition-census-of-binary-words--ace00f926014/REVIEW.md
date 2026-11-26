# Independent mathematical audit

## correctness

PASS

Each completed greedy arch supplies either bit, and greedily aiming for the successive arch-ending bits followed by a bit missing from the rest constructs an absent subsequence of length one greater. Thus the index is exactly the arch count. A direct enumeration gives a cross-check of the continuation-state proof: for k≥1 the k arch lengths contribute (z²/(1−z))^k, the internal changes t^k, the first orientation 2, the k−1 inter-arch boundaries (1+t)^(k−1), and the empty-or-unary tail 1+z(1+t)/(1−z). This is the stated coefficient of u^k. Its two terms yield exactly the two binomial contributions and r=k,…,2k−1 when n=2k, adding r=2k at n≥2k+1. The n<2k terms vanish, and k=0 has just the empty word or the two positive unary words at each length. An independent program builds all subsequence sets by length and agrees with every joint cell for n=0,…,12, including the zero cells and the support assertions.

## originality

FAIL

No duplicate joint table was located. The objection is direct prior implication, not that the prior marginal as a numerical distribution determines a joint one. The already published binary arch proof gives a finer exact orientation-and-length parametrization. At fixed lengths each arch makes one internal change, and every free starting-bit choice after the first is exactly a free binary choice of whether to change at that boundary, including at a nonempty tail. Marking the existing orientation choices gives the entire formula and support without additional constraints or enumeration.

## value

FAIL

Both statistics are natural, and the formula is usable, but in the fixed binary alphabet the entire extra statistic is the forced count of internal changes plus an unrestricted toggle at each existing orientation choice. The positive-cell range and numbers are routine consequences of the prior exact binary parametrization. The claimed refinement adds no independent boundary phenomenon surviving that comparison.

The dated certificate retains the supplied scientific assessment, sources and limitations.
