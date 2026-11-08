# Scientific review

## Correctness — PASS
For any base-three integer with \(k\ge5\) digits, the chain \(T(n)\le16k<3^{k-1}\le n\) is valid (base \(k=5\) and an elementary induction). Thus every trajectory enters \([1,80]\). The fourteen distinct outputs \(a+16b\) for \(1\le a+b\le4\) are all shown, every outgoing arrow is computed, and the graph is closed; it has exactly the three stated cycles. Parity is invariant because \(d^4\equiv d\pmod2\). The included code and output corroborate the finite edge table and independently recompute all small starting trajectories. No unproved infinite computation is assumed.

## Originality — PASS within inspected literature
Grundman–Teeple (2007) prove the parity invariant for all exponents in base three. Hargreaves–Siksek (2010) develop a general finite-cycle algorithm and show a quartic **decimal** example, but not the exact quartic ternary graph. Goedhart–Gurtas–Harris (arXiv v1 posted 17 October 2024) analyze general trees and preimages; their primary full text has no such explicit case. The original four-state/six-state dynamics is not claimed newly introduced: this review accepts only the **explicit** five-periodic-point global classification and its fourteen-arrow proof. Source-inspection gaps, especially the inaccessible survey body, and possible unindexed tables remain risks.

## Mathematical value — PASS
Complete fixed-point and cycle determinations for a natural base/exponent are exact invariants in the generalized happy-number literature. Here the explicit global phase portrait additionally identifies a unique attractor for every even integer and exactly two distinct odd attractors. This is a natural complete classification rather than an arbitrary bounded sample, though it is an elementary instance of a previously known finite-cycle algorithm and gives no densities or digit characterization of the odd basins.

## Limits
The conclusion covers one base/exponent only. It does not determine odd-basin densities, other exponents, or statistical heights. Independent audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
