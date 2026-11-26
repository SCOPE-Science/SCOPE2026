# Independent mathematical audit

## correctness

PASS

The frozen interval argument recovers the two positions directly if their separation is at least k. Otherwise two-one reads give the separation d and force a unique position except on the stated plateau; within that plateau the sum of offsets of single-one reads changes by r−d per unit shift, and at d=r the offset multisets themselves are constant. An independent replay uses the sum over reads of the unit vectors for their (k−1)-prefixes minus those for their (k−1)-suffixes. It telescopes to the prefix-minus-suffix of the whole word. If nonzero, it gives both ordered ends, which cover the word because k>r implies 2(k−1)≥n. If zero, the word has period r. Here n≥2r, so a period-r word of weight two has one nonzero residue containing exactly two positions; those phases are precisely n−2r≤a≤r−1, and changing the phase permutes the r read starts. Thus the potential fiber has size max(0,3r−n), with a collision only when size is at least two. The injectivity cutoff is k≥ceil((2n+2)/3), within the long regime for n≥5. For all shorter k≥3, valid two-copy phases are max(0,n−2r)≤a≤min(r−1,n−r−1). There are at least two phases: if n<2r the upper endpoint is at least one, and otherwise the count is 3r−n≥2. At k=1 all words collide, and at k=2 the stated pairs (0,2),(0,3) have equal bigram counts. No monotonicity of single-length reconstruction is assumed. Replay: RESULT.md lines 31–73; inspected scripts and captured outputs corroborate only their finite test domains. The conclusion is in-class, linear, ordered within reads, and multiplicity-sensitive.

## originality

PASS

The distinct supported contribution is the exact weight-two long-read fiber and spectrum count, plus the first length that is identifying with a witness at every shorter length. Periodic phase collisions, degree balance, and the column-marginal rigidity method are not new. A closely related same-day result gives a general residue-chain observation and its application to weight three; it is strong method-level overlap but does not supply a full fiber classification or an all-shorter-length result for weight two. No containing exact theorem was established in the sources inspected.

## value

PASS

The exact fiber tells not only when length alone permits reconstruction, but precisely which two-marker placements fail and how many indistinguishable source words each ambiguous observation represents. Separately certifying every earlier length is important for one-length observations, where longer read spectra need not directly encode the shorter multiset including its end effects. The two-thirds cutoff and recurrence of the same phase mechanism in all short ranges are structurally useful beyond a small enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
