# Scientific review

## Correctness — PASS
A common three-symbol output exists exactly when coordinatewise overlap is at least three. Distinct heavy words inject into the \(q\) coordinates at which multiplicity exceeds two; two distinct light words would overlap in at least \(2n-2q\ge4\) places. A light word cannot exist at lengths exceeding \(2q\). All-pure constructions and an extra light word achieve the two phase values; two explicitly specified light witnesses show boundary sharpness at length \(q+1\). The proof covers every integer \(q\ge2\) and the stated entire length range. The standalone checker reproduces finite instances without serving as an infinite proof.

## Originality — PASS against inspected evidence
The primary three-survivor study [1, Section 3.5, Theorem 9] gives a generally nonsharp all-alphabet upper bound, not an exact value for the stated two ranges. The companion study [2, Sections 4–5] gives ball-volume bounds rather than this extremum. Previously recorded fixed-alphabet exact cases do not logically imply the universal \(q\)-parameter result, and all-alphabet exact aliases were not identified in the checked sources. Residual risk is an unindexed earlier theorem or an overlooked implicit deduction from related multiset packing literature. These checks do not establish global priority.

## Value — PASS
Three-survivor multiset deletion is a natural extremal decoding regime singled out in [1]. The two sharp phase transitions give an exact all-alphabet asymptotic stabilization, improving the prior general bound substantially and supplying explicit optimal codes for an infinite two-parameter region. The heavy/light structural argument explains why the optimum has only two phases.

## Scope and limitations
Exactly three elements survive; other deletion counts, ordered sequence codes, and classification of all extremizers are not established. At the shorter length \(n=q+1\), only an explicit \(q+2\)-word witness is asserted. No independent audit or definitive historical-priority certification is claimed.

Self-review: passed. Independent audit: not yet performed.
