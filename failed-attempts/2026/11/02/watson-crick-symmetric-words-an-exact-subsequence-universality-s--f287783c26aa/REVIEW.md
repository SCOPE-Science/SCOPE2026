# Independent mathematical audit

## correctness

PASS

A word has index equal to its maximum number of disjoint full-alphabet intervals: greedily ending each interval maximizes the count, and the successive greedy end letters followed by a missing remainder letter form a missing subsequence. In the reflected word at most one interval can cross the midpoint. If it is the (2r+1)st interval in a collection, the r intervals on each side must leave the crossing interval inside the two greedy remainders. Thus the extra unit is exactly the condition that the remainder meet every involution pair. The support counts are binomial(d,j-d) times 2^(q-j); counting surjections for a fixed support and marking each half arch by u^2 gives the claimed rational series, including the binary and u=1 checks. At length qk all k arches must be permutation blocks. The midpoint either separates the blocks or bisects one whose first half is a transversal of the pairs. This proves attainability, uniqueness of the specified decomposition and both counts. The empty word is handled by r=0 and empty remainder. Read RESULT.md, VERIFICATION.md and verify_wc_universality.py; reported exhaustive tests are bounded corroboration, not newly replayed or needed for the proof.

## originality

FAIL

The strongest indexed comparison is a distinct mixed-involution record. Its theorem formally excludes f=0, and its odd-index minimum formula is not an endpoint formula. But its explicit even proof already works with no fixed letters: the same midpoint identity, pair-support count and arch summation give the entire frozen enumerator with f=0, without another lemma. Its minimum-degree argument applied to that even series gives the exact multiplicities and the same transversal/permutation blocks. Thus a separately original contribution relative to that demonstrable coverage is not established. This is not a finding that the mathematics is false or that either same-day record predates the other.

## value

PASS

A full two-marker enumerator and a classification of all shortest hosts answer natural questions for antimorphic symmetry. The odd central transversal explains why reversal-complement symmetry need not increase the unrestricted minimum. This is substantive mathematical content as a classification; passing value does not make the already-covered substance a separate contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
