# Self-review

## Correctness — PASS

For odd primes \(p\), a dominant term must have order \(2p\) and multiplicity exactly \(2p-1\). The residual length \(p-1\) is forced. Every residual term has gcd weight one or two, and a cross-number-one zero sum involving residual terms is equivalent, in both directions, to a nonempty zero-sum subsequence of the corresponding adjusted residual sequence modulo \(p\). The maximal-length zero-sum-free inverse lemma for \(C_p\) forces one common nonzero reduced residue. Exactly two exceptional reduced residues have one rather than two lifts. Counting unordered multisets gives the stated formula and support distribution. The finite DP independently checks every constructed sequence for primes \(3,5,7,11,13\); exhaustive all-sequence checks at \(3,5,7\) support the result but are not invoked as its infinite proof.

## Originality — PASS with documented residual risks

The 2025 original investigation of cross-number-one subsequences (Gao–Hui–Jiang–Li–Wang, DOI 10.4064/aa240825-15-11), the 2026 complete threshold theorem (Gao–Mu, arXiv:2611.23852), and the 2006 long ordinary zero-sum avoidance study (Savchev–Chen, arXiv:math/0604356) were compared by mathematical implication. The first two explicitly present sharp thresholds and witnesses but not the stated inverse family or cubic census. The third concerns ordinary \(n\)-term zero sums, applies in a distinct length range, and does not include the weighted cross-number test. Relevant indexed results and accessible existing claims were checked. An implicit derivation from general zero-sum or extremal sequence machinery cannot be ruled out and remains the major originality risk. No uniqueness conclusion follows merely from the absence of search matches.

## Mathematical value — PASS

This is a natural inverse refinement of a new sharp extremal threshold rather than a change of notation or an arbitrary fixed small case. It identifies all dominant-term witnesses at infinitely many cyclic orders, distinguishes support-three witnesses from the previously displayed two-symbol example, and proves a structural equivalence to maximal ordinary zero-sum-free sequences of prime order. It does not assert a complete classification of non-dominant extremizers, and supplies no unwarranted downstream conjecture.

Self-review: passed. Independent audit: not yet performed.
