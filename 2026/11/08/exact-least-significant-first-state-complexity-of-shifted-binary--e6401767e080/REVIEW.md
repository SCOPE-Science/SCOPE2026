# Scientific assessment: shifted binary digit-sum state complexity

## Correctness — PASS

The assertion is about one precise function, \(n\mapsto s_2(n+c)\bmod m\), for all \(m\ge2\) and \(c\ge0\), under binary LSD-first reading and arbitrary trailing-zero padding. The proof establishes the residual quotient-and-remainder identity for every digit length, computes the exact attainable popcount intervals without extrapolating from samples, and proves all different parameter pairs inequivalent using \(n=2^h-a'\) with unbounded \(h\). Reachability is exhaustive because depths below the binary length of the shift and depths at or above it are separately analyzed. The transition/output formula is closed and padding-compatible. A separate program checked 903 finite shift/modulus pairs by independent BFS and Moore minimization, 2,047 interval extrema, 96 power-shift specializations and 30,600 residue identities. The finite checks corroborate the analytic proof; they are not substituted for it.

## Originality — PASS, subject to residual priority uncertainty

The closest primary source, Moradi–Rampersad–Shallit (2025, arXiv:2512.10017v1), studies state complexity of linear subsequences and shifts of Thue–Morse. Its shifted-Thue–Morse theorem provides a most-significant-digit-first upper bound rather than this exact LSD-first all-shift/all-modulus count. Zantema–Bosma (2022) gives general shift bounds and the isolated binary shift-one special case; those do not imply the complete reachable-pair formula. Moradi–Popoli–Shallit–Vukusic (2026, arXiv:2603.18858v1) deals with shifted Fibonacci sequences under Zeckendorf representations; the objects and digit system differ. Charlier–Cisternino–Massuir (2021) concerns regular languages of affine *images* of the even-digit-sum integer set, and its stated theorem does not give state complexity for the *inverse-input shifts* here. The accessible specialized statements and their implication ranges were compared; an unindexed equivalent specialization remains a residual risk, and this assessment is not a claim of exhaustive historical priority.

## Value — PASS

The exact least number of states for every shift and alphabet modulus is a natural descriptional-complexity invariant of a basic automatic-word family, not an arbitrary single-parameter computation. The construction provides the full minimal kernel and effective automaton, while the power-of-two formula distinguishes quadratic growth in shift-bit depth when the output modulus is large from linear growth once the modulus is fixed. This resolves the precise-state-count question within a family for which published work supplies generic constructions and bounds. No general theorem about unrelated automatic sequences is claimed.

## Sources, limitations and remaining risk

Primary evidence: Moradi–Rampersad–Shallit, arXiv:2512.10017v1 (sections on linear subsequences, shifted Thue–Morse and LSD-first constructions); Zantema–Bosma, *Information and Computation* 288 (2022), article 104710; Moradi–Popoli–Shallit–Vukusic, arXiv:2603.18858v1 (introduction and LSD-first Zeckendorf analysis); Charlier–Cisternino–Massuir, *Electronic Journal of Combinatorics* 28(3) (2021), P3.12 (statement and interpretation of Theorem 3). The claimed result is limited to the standard base-two LSD-first convention; most-significant-digit-first automata and other bases are outside scope. The assessment remains subject to historical-priority uncertainty and lacks independent mathematical audit.

Self-review: passed. Independent audit: not yet performed.
