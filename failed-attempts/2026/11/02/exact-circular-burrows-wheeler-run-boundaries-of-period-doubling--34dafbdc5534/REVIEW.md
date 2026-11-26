# Independent mathematical audit

## correctness

PASS

With no endmarker and no merging of first and last runs, the statement is correct. The odd number of ones rules out every nontrivial power of a word of length 2^k. The length-three parity test forces a bispecial factor of length at least three to start and end at even positions and hence to have form μ(v)0. Occurrences and both extensions correspond to those of v, with extension letters complemented. For a right-special factor the only adjacent pair with that LCP straddles the 0/1 extension cut; the substitution reverses the order across that cut and complements the predecessor letters, preserving whether they disagree. At rank two only the cut at 00 is active; thereafter the elementary cuts at 00 and 0 are active while the empty cut is inactive. Transport gives the stated distinct A and B families, excluding B_(k−1), and hence 2k−2 runs. A separate valuation-of-position construction and rotation sort at ranks 2–11 reproduced all boundary LCP sets and counts (python -I /workspace/branches/independent_checks.py 5); this is finite corroboration only. Frozen VERIFICATION.md and checker.py were inspected, not executed.

## originality

FAIL

The distinct 18 October Resultary record already states 2k−2 for the identical circular sentinel-free transform and gives the full transform. Its ordered four-class rotation lemma also mechanically yields the extra LCP family, not merely by invertibility or finite enumeration. In that lemma classes A and B have constant predecessor symbols 1 and 0, and prefixes 0001 and 0010, so their sole boundary is labeled 00. B and C meet at LCP 0 and their predecessors differ exactly from rank three onward: C begins with the complement of the last symbol of the old zero-start segment, which ends in 0 from rank two. C ends with 0 and D begins with 0, so their interface is inactive. Within C the even-start rotations are the reverse-ordered block images of the old zero-start rotations, with complemented predecessors. An old pair with LCP v has image LCP μ(v)0 because the first blocks that differ still share their leading 0. Every old boundary is in the zero-start segment, since its last symbol and the whole one-start segment are 0. Thus the prior proof gives exactly the base {00} and recursion {00,0} union {μ(v)0 : v is an old boundary LCP}; iterating is exactly the frozen list. The same-day distinct record confirms the four-block coverage but its relative timing is not used.

## value

FAIL

Run counts and lexicographic labels are motivated invariants, and the proof is a useful exposition. As a new finding, however, the count is already known and the extra labels follow directly from the existing sorted-rotation proof. The frozen claim supplies no independently useful unknown remainder; reorganizing the proof around bispecial factors is not a substantive repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
