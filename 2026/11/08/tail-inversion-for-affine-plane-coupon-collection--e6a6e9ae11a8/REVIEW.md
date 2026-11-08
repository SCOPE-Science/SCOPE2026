# Review of the affine-plane tail-inversion theorem

## Correctness

**PASS.** The all-order assertion follows from finite-plane incidence identities, exact tail inclusion–exclusion and comparison of exponential bases. Pair contributions cancel identically because both sampling laws are \(2\)-balanced; noncollinear triples have the unique largest surviving avoidance probability \((q-2)/(q+1)\), with multiplicity \(q^3(q-1)^2(q+1)/6\). Each four-point-or-larger set has a strictly smaller avoidance probability because at least one line through its fourth point misses any chosen noncollinear triple. An independent early-cover calculation compares parallel classes to disjoint random blocks. For order three the finite signed-subset table is exhaustively checked and an explicit monotonicity identity proves the unique sign switch. Reproducible checker `verify.py` passed 3,060 assertions. Finite checks do not establish the infinite theorem, which is instead analytically proved in RESULT.md.

## Originality

**PASS (subject to historical-priority risk).** The primary June 2026 affine-plane source gives expectation comparisons, in particular the reversal between orders three and four, but neither an all-order theorem of stochastic incomparability nor a sharp positive late-tail difference and exact order-three crossover in the inspected sections. The general 2025 recovery-set source supplies mean formulas and fair-sampling bounds, not this distribution-level implication. The related group-drawing paper studies expectation optimization. The statement is not a corollary of their displayed mean inequalities: an expectation relation neither entails nor excludes stochastic order. The proof needs a separate two-point cancellation, classification of triple avoidance, and minimum-time parallel-class comparison. No directly covering public-record match was retrieved. Potential hidden coverage by a broader block-design tail theorem remains possible; database nonmatching is not a mathematical uniqueness certificate.

## Mathematical value

**PASS.** The source's contrasting affine-plane mean comparisons naturally raise whether any distributional comparison survives. The theorem rules out stochastic dominance for every existing affine-plane order at least three, even though the mean can favor either mechanism. It isolates the geometry of noncollinear triples as the sharp eventual tail obstruction and gives the exact crossover time for the smallest nontrivial affine example. This is a structural boundary on what mean-based comparisons of fair collection mechanisms can imply, not merely another tabulated mean.

## Closest literature and limitations

The primary predecessor is D. Barak-Pelleg and D. Berend, *Fano Geometry and Slow Coupon Collecting*, arXiv:2606.28216v1, Proposition 2.2, Table 2, and Sections 2–5. General methods appear in Y. Grunbaum and E. Yaakobi, *General Coverage Models: Structure, Monotonicity, and Shotgun Sequencing*, arXiv:2510.25305v1, and expectation comparisons in D. Berend and T. Sher, arXiv:2509.17201v1. Existence of an affine plane of order \(q\) is assumed. The asymptotic fixes \(q\); no joint \(q,t\) limit or exact general-order crossover is asserted. Historical-priority assessment could change if an unlocated general-design theorem proves a stronger result.

Self-review: passed. Independent audit: not yet performed.
