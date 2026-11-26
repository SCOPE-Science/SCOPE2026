# Independent mathematical audit

## correctness

PASS

For each p|n, restrict σ^(n/p) to a p-point orbit with its induced total order. Times in this restricted orbit correspond to multiples of n/p in the original signatures. If one chooses its second-least point, just one nonzero time t₀ modulo p sends it below itself, to the least point. The same-sign condition forces ut₀=t₀ modulo p, which gives u=1 modulo p since t₀ is nonzero there. This includes p=2 without exception. All these congruences yield the radical condition, whose n/rad(n) residues are units. In the attaining CRT lexicographic order, components with t=0 modulo their prime powers do not change under either increment. In a changed p^a-component p^r is the exact p-part of t; the first r lowest digits stay fixed and the next digit changes by t/p^r modulo p, the same for t and ut when u=1 modulo p. Its changed digit value, and therefore the first differing digit comparison in the product order, agree. Multiples of n give equality, and reducing all other times modulo n loses no data. Squarefree rigidity is only for powers of one cycle. The independent integer check compared all non-return signs for the proposed orders for 2≤n≤80 and exhaustively tested 5913 phase-anchored oriented cycles at 2≤n≤8; it confirmed the claimed stabilizer sizes. To replay, fix the least element as phase zero, permute the remaining phase entries and test all unit residues against the signs of positions j+t and j+ut relative to j, modulo n. The supplied VERIFY.py is a separate replay path and was inspected, not executed. These finite checks corroborate the symbolic proof.

## originality

FAIL

The upper obstruction and squarefree consequence are direct restrictions of the verified prime-cycle rigidity theorem. The frozen record explicitly excludes its sharp prime-power bound and digit-order construction from novelty. The stated mixed-factor advance is a mechanical coprime product of exactly that acknowledged baseline, by coordinate restrictions and lexicographic ordered products; no additional independent obstruction or attaining construction is established. This is an implication assessment, not a claim to have located a publication for the full mixed theorem or independently dated the acknowledged prime-power work.

## value

FAIL

Stabilizers of order signatures form a natural invariant, but the proposed extra result supplies neither a new mixed-prime interaction nor a useful new classification beyond the prime-power baseline and the verified prime obstruction. The exact cardinality factorizes by the elementary restriction/product argument, and the squarefree composite case follows from prime reconstruction and the CRT. No separate worthwhile gain for the claimed extension was established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
