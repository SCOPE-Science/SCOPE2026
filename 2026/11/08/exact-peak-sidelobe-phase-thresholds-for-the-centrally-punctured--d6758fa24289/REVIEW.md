# Scientific review: punctured-square peak-sidelobe phase thresholds

## Correctness — PASS

The coefficient and displacement definitions coincide with aperiodic autocorrelation, and the positive-half-plane reduction covers all nonzero shifts. Three independent phase normalizations reduce an alphabet of size \(q\) to exactly \(q^5\) cases, with \(q^3\) distinct arrays in each modulation orbit. The exact squared-norm identity expands each correlation into a finite sum of doubled cosines. Every comparison uses integers or exact algebraic field representations: integer rings for \(q=2,3,4,6\), \(\mathbb Q(\sqrt5)\) for \(q=5\), \(\mathbb Q(2\cos(2\pi/7))\) with a certified rational isolating interval for \(q=7\), and \(\mathbb Q(\sqrt2)\) for \(q=8\). Exhaustively testing all 61,775 normalized arrays proves the seven sharp minima and complete equality counts. The corner shift gives a universal lower bound \(1\) and the displayed six-phase configuration attains it. The standalone verifier recomputes all entries of `OPTIMIZERS.json`, not merely the aggregate counts.

**Residual correctness limits:** This is a finite-alphabet theorem for exactly seven alphabet sizes. The proof would not establish analogous results for arbitrary alphabets or continuous coefficient phases. Finite floating checks play no role in the mathematical certificate.

## Originality — PASS, with bibliographic priority risk

The closest examined 2D source, Pai–Chen (arXiv:2102.04043v1), defines the same aperiodic correlation but proves complementary **set/pair** constructions; it does not tabulate the sharp largest single-array sidelobe for the eight-point punctured support. Katz–van der Linden (arXiv:2108.07318v1) prove asymptotic peak-sidelobe bounds for recursive **1D** sequences. Bell–Jedwab–Khatirinejad–Schmidt treat **fully occupied** 3-phase Barker arrays, including a \(3\times3\) example, which is not an array with center zero. The closest available indexed mathematical findings on full nine-point squares, triangular and cubic apertures concern different supports or the integrated fourth moment.

The prior known fourth-moment classification for the **same punctured support** is the most important implication comparison. Its q=6 minimizers coincide with the present q=6 peak-sidelobe solutions; this coincidence is not new. But equality of a summed quadratic sidelobe energy neither determines the maximum single sidelobe nor its full optimizer set. For instance, at \(q=5\), the new peak problem has 240 normalized minimizers versus only four for the fourth-moment optimum. The new claim therefore includes a distinct exact invariant, its previously undocumented classification across the given alphabets, and a sharp first attainment threshold. Search failure alone is not regarded as proof of priority.

**Residual originality risks:** A prior specialized radar, coding or sparse-array table may contain the same punctured-array PSL values. The indexed records inspected are not an exhaustive bibliography; the closest published-finding corpus entries were accessible through summaries, not full papers.

## Mathematical value — PASS

Aperiodic maximum sidelobe magnitude is a directly motivated array-design invariant distinct from integrated sidelobe energy. The punctured \(3\times3\) support is the smallest centrally vacant square aperture with four corners and nontrivial 2D overlap geometry. The exact six-phase feasibility threshold is sharp because the extreme corner shift forces a nonzero sidelobe for every unimodular choice. The loss of optimality at seven and eight phases is meaningful for alphabet-constrained phase design, and the 240 versus four q=5 optimizer distinction shows why the peak criterion cannot be replaced by a previously studied fourth moment. Complete equality catalogs allow comparison and reuse without unproved downstream claims.

**Scope and remaining work:** This does not establish an unrestricted continuous-phase optimum, the behavior for alphabets larger than eight, or an open-ended structural description replacing exhaustive enumeration.

Self-review: passed. Independent audit: not yet performed.
