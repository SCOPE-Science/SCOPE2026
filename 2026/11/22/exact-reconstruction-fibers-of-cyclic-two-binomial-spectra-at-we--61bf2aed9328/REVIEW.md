# Independent mathematical audit

## correctness

PASS

For the three gaps g_j, direct one-start counts are t_j=2g_j+g_(j+1). Moving a leading one adds n-3 and moving a leading zero subtracts 3. Multiplication of each zero-gap geometric progression by X^3-1 telescopes to X^(t_j+n)-X^(t_(j+1)+3), including when the gap is empty; adding the three one-start terms yields the exact polynomial identity. Cancellation reduces complete spectra to unordered t triples, working also for periodic sources. The matrix taking gaps to t is invertible with determinant 9 and commutes with 3-cycles, so the two permutation cosets give at most two necklaces. Swapping t_2 and t_3 gives the reversed coordinates subtracted from 2(n-3)/3; integrality requires 3|n, and nonnegativity is exactly the stated bound. At n=3(h+1), there are 3h^2+3h+1 admissible ordered triples by subtracting three disjoint forbidden-coordinate ranges. Burnside gives h^2+h+1 cyclic orbits. Equality under the reflected-complement involution up to a 3-cycle forces one coordinate h and the other two complementary; with h in the middle this gives exactly 2h+1 fixed orbits, including (h,h,h). The remaining orbits pair, giving binom(h,2); subtracting from the unconstrained Burnside count gives (h+1)^2. Independently checked n=3 through 30 (1,360 necklaces) by encoding the one positions p and computing each rotation's count as sum((p-i) mod n)-3, without the gap compression. It reproduced the stated first doubleton spectrum and all sampled fiber counts. This finite check supplements the all-n proof.

## originality

PASS

The basic inversion increment and ordinary two-binomial word invariant are prior ingredients. The supported distinct result is the exact inverse-fiber classification for the full rotation multiset, including its only possible mate, divisibility obstruction and complete doubleton census. Inspected neighboring results do not imply it.

## value

PASS

The exact inversion ambiguity of a natural deliberately unlabeled rotation observation is more informative than a support-size bound. A uniform reconstruction law, a sharp divisibility condition, and the exact number and identity of ambiguous sources at the first weight where this obstruction is substantive are useful together. The theorem classifies all lengths, not just the first collision.

The dated certificate retains the supplied scientific assessment, sources and limitations.
