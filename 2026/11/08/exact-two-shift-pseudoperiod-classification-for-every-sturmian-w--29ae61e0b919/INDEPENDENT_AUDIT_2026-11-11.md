# Independent mathematical audit

## correctness

PASS

Encode mechanical letters by a half-open circle arc of length alpha, swap labels so the shorter arc I has m=min(alpha,1-alpha)<=1/2. For each nonzero shift a, the set E_a of points whose membership changes is a union of intervals. A shift inside [m,1-m] mismatches on an open subarc of I and must overlap every other nonzero mismatch; two offsets both in (0,m), or both in (1-m,1), likewise overlap. For opposite offsets a=u in (0,m), b=1-v with v in (0,m), a direct half-open interval analysis gives simultaneous mismatch empty precisely when u+v<=m, i.e. b-a>=1-m; all other pairs have nonempty open mismatch, hit by every irrational rotation orbit. Endpoint orientations yield disjoint half-open pieces at equality. This proves the universal over n and arbitrary intercept equivalence, not only density one. Independently stress-tested 975 distinct shift pairs across three irrational slopes with 2000 orbit positions each; when a fractional difference equals the boundary, accounted for floating-point rounding in the test tolerance. Tests are supplementary to the circle proof.

## originality

PASS

Meleshko–Ochem–Shallit–Shan (2023; first arXiv 2022) Proposition 9 proves that each Sturmian word has at least one two-shift pseudoperiod; Example 8 constructs a 28-state automaton for all pseudoperiod pairs of the Fibonacci word. The inspected full primary source gives no uniform necessary-and-sufficient fractional-part inequality for arbitrary irrational slope and arbitrary pair. Its known special Fibonacci classification and mere existence are acknowledged, while the all-slope complete numerical criterion remains new on current evidence, with residual risk of an alternative Sturmian rotation theorem.

## value

PASS

Classifying every allowed pair of return shifts is a natural complete invariant for the central family of aperiodic balanced binary words, expressly raised as a question in the motivating pseudoperiodicity paper. The criterion turns a slope-specific automaton into a universal explicit Diophantine inequality and proves complete intercept invariance. This is mathematically stronger than a single existential witness and useful for checking any shifts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
