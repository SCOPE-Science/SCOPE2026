# Independent mathematical audit

## correctness

PASS

For D_n=μ^n(0), n≥3, the block form XYXXXYXY with X=D_(n−3) and Y its last-bit flip supplies partners at offsets +4h,+h,−h,−4h,−6h on the five intervals. The first four matches end at a differing final block bit; in the fifth the remaining suffix repeats in full. Opposite-parity positions have LCP at most two since every even-start triple ends in zero while an odd-start triple beginning in zero must be 001 (the source word has no 11). Same-parity LCPs have upper bounds 2r_n(a)+1 and 2r_n(a) after morphing, with the actual suffix lengths giving the sharper fifth piece. The base profile at n=3 matches directly; the resulting upper bounds coincide with the explicit lower bounds for every order. A net occurrence must have length r_n(i)>0 and, away from the left boundary, r_n(i−1)<r_n(i)+1. Applying this criterion gives exactly the five claimed pairs, including the equality at 6h. Independently, direct all-pairs suffix comparisons and direct enumeration of repeated factors with unique extensions matched every case at orders 3 through 7. To replay the finite check, substitute 0→01 and 1→00, compare each suffix with all other suffixes, and tabulate every nonempty substring by its starting positions before checking its left and right extensions. The frozen check_period_net.py was inspected, not run; the frozen log reports orders 3 through 14. Neither finite check is used as the all-order proof.

## originality

FAIL

A distinct indexed theorem gives the complete list of minimal unique substrings of exactly these finite period-doubling iterates for n≥3. This list determines the first unique prefix length of every suffix, not just the shortest unique factor length in the word. Its four stated starts and lengths mechanically give all five pieces and hence all five net pairs. This is demonstrable coverage, not a conclusion about chronological priority; the indexed dates alone do not determine priority.

## value

FAIL

The profile is a useful way to express repeated-factor information, but as a distinct exact invariant here it supplies no additional classification beyond the complete minimal-unique-substring list for these same words. Taking first endpoints gives the whole profile and adjacent comparison gives every net occurrence. There is no independently established surviving mathematical contribution beyond that exact conversion in the stated finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
