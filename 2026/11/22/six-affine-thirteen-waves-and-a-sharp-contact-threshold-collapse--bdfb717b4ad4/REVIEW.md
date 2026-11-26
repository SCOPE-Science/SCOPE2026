# Independent mathematical audit

## correctness

PASS

An independent integer census (python3 /workspace/reviews/evidence-5.py with NumPy) constructed both transition maps by squaring residues modulo 13, applying the stated synchronous update, and iterating nested full images. At the first equality of consecutive image sizes the restrictions are a finite permutation, so the image is precisely the recurrent set and that iteration is the sharp maximum entry time. Walking the cycles of this image and following all unresolved initial states until first entry yields the primitive cycle counts (1,2288,6), recurrent populations (1,6864,78), basin totals (1498799,88114,7410), six individual 13-basins of size 1235, and sharp depth 14 attained by 624 states at threshold two. Since the least common multiple of the periods is 39 and depth-14 states are not yet periodic at time 13, F_2^53=F_2^14 but F_2^52≠F_2^13. The independent transition map sends 0000002221110 to its translate by +3, and for each affine image with multiplier a the speed is 3a; these are the six distinct quadratic residues. The 78 affine images are distinct and equal the independently enumerated period-13 set. At threshold three the stabilized image is just zero, at time four, with 101062 states first entering at that time. The frozen transcript and its two inspected classifier algorithms are consistent with these independently obtained results.

## originality

PASS

Do not credit eventual extinction itself at the half-degree threshold: Resultary fc90f3212227 has a general same-model statement for all admissible Paley orders at least 13, directly covering it. Credit the exact threshold-two recurrent and transient classification and affine traveling-wave geometry, and at threshold three only the quantitative sharp four-step cutoff and maximal-depth census. The strongest accessible broader statement does not imply those quantities, and its indexed exact census describes exceptional orders 5 and 9, not the order-13 collapse count. This assessment does not infer priority from the common date and expressly leaves a source-access risk for the Paley-13 clock in that record's full text.

## value

PASS

A canonical small six-regular residue graph is a natural adjacent-threshold test: the strict half-degree estimate does not decide the critical case, while one contact below it the long cycles have an affine wave classification, not merely an isolated numerical witness. The full basins distinguish abundant short periodic states from the few long waves, and the exact cutoffs supply a finite benchmark unavailable from qualitative extinction. Value rests on these sharp and geometric facts rather than restating the already covered eventual-rest result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
