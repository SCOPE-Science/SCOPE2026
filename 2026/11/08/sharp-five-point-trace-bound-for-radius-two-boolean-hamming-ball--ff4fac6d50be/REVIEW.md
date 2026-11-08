# Review of the radius-two Boolean-ball trace theorem

## Correctness

**PASS.** If five points are shattered, one radius-two ball contains all of them. Binary translation makes its center zero; the five distinct points are then weight-at-most-two rows. The finite-column reduction is exhaustive: every nonzero column is one of 31 membership masks with multiplicity zero, one or two, and each row has total column incidence at most two. The supplied `verify.py` enumerates exactly 14,778 feasible templates and 7,260 with distinct rows, computes every possible saturated trace using four auxiliary all-zero coordinates, and finds a sharp maximum of 27. Centers of weight at least five cannot meet any of the five rows, so no trace is lost in the finite reduction. An explicit six-dimensional witness attains 27; explicit four-point witnesses and elementary dimension-four complement arguments settle the sharp VC threshold. The finite computation constitutes a fully exhaustive certificate *after* the dimension-independent reduction, not a finite-dimensional extrapolation.

## Originality

**PASS within inspected sources, with historical-priority qualification.** Adler, Benediktsson and Macpherson, arXiv:2007.16042, Sections 1 and 4, prove VC properties of open Hamming-graph adjacency (radius exactly one and excluding the center). Their statement does not imply the present radius-two closed-ball 27-trace bound. Chalopin, Chepoi, Mc Inerney, Ratel and Vaxès, arXiv:2206.13254, Sections 1, 5 and concluding remarks, address sample compression for graph balls and do not supply this exact hypercube classifier. Bousquet and Thomassé's distance-VC graph-ball framework does not imply the exact uniform value or the dimension threshold. Related published mathematical records for Boolean Hamming radius-two balls study positive-definite Turán mass, not VC traces. Searches for fixed-radius binary Hamming-ball VC dimension and shatter functions found no equivalent exact statement. This is evidence of noncoverage in checked materials, not a claim of exhaustive worldwide priority.

## Mathematical value

**PASS.** The theorem gives an exact, dimension-independent capacity limit for a natural nontrivial metric-ball range family, sharply improves the generic finite-domain counting bound, and pinpoints the first dimension allowing four-point shattering. The stronger local five-point bound of 27 traces (rather than merely fewer than 32) is attained by a concrete support and refines the usual VC-dimension statement. It distinguishes radius-two balls from the previously analyzed radius-one neighborhood case and is pertinent to metric range-query complexity. The computational certificate is short, exhaustive and independently reproducible.

## Limits

The alphabet and radius are fixed, and the 27-trace bound assumes that the entire support fits in one radius-two ball. No formula for the complete shattering polynomial is asserted. The proof uses an executable exhaustive finite certificate; a shorter human-only structural inequality is not supplied. Uninspected literature under alternative terminology remains a priority risk. Source inspections and computations are not independent scientific validation.

Self-review: passed. Independent audit: not yet performed.
