# Independent mathematical audit

## correctness

PASS

The substitution emits 0 at each even position, and a 1 never has an adjacent 1. The length-three patterns at even and odd starts are disjoint, so counting occurrences of longer factors can be done separately by starting parity. The quarter-length suffix D_(j−2) starts with 010 when its size is at least four, hence each occurrence desubstitutes on even block boundaries until 01 in D₃, which occurs exactly at 0,4,6. Lifting gives 0,2q,3q for q=2^(j−2); right-aligning within those copies gives at least three occurrences of every shorter suffix. For length 2k the even encoding uses all k-factors and the odd one omits just the final k-factor occurrence; for length 2k+1 the even encoding omits that occurrence and the odd encoding uses all (k+1)-factors. Each encoding is injective, and deletion of a suffix occurrence cannot yield a singleton at lengths ≤K=2^(j−3), since that suffix occurs at least three times. In particular length 2K has no singleton; all shorter factors are nonunique because any occurrence extends within the finite word to length 2K. At length 2K+1 only the odd class can be unique and is in exact correspondence with the preceding four starts through i↦2i+1. Direct base case D₃ has starts 1,2,3,5 at length 3. This proves the claim for all n≥3. An independent exact suffix-array/LCP calculation and suffix hit-count check passed at orders 3–14 (`python3 /workspace/branches/frozen_review_checks.py`); that check is not an infinite proof or formal certification.

## originality

FAIL

A distinct indexed Resultary finding gives the complete minimal unique substring classification for the same complete iterates and all n≥3, and it demonstrably includes every frozen conclusion. This is a coverage decision, not a finding of earlier priority: the catalogue entry is later-dated, and the available records do not establish chronology of discovery, dependence, or authorship. No earlier exact theorem was established in the external literature inspected.

## value

FAIL

The observable itself is natural and the formula would make a good exact benchmark. As a standalone narrow result for acceptance it supplies no additional invariant, threshold, or witness beyond the existing complete minimal-unique list, from which every stated benchmark datum follows immediately. No separately useful new consequence beyond that list is established here.

The dated certificate retains the supplied scientific assessment, sources and limitations.
