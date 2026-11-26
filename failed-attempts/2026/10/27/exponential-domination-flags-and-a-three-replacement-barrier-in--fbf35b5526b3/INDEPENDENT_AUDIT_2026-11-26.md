# Independent mathematical audit

## correctness

PASS

I independently enumerated all subsets through size four on the duad–syntheme incidence graph using exact integer weights in units of 2⁻²⁸; replay: python3 /workspace/audit_work/record2.py. The counts of porous dominating sets at sizes 0–4 are (0,0,0,0,45), with precisely the sets obtained from flags. Blocked distances cannot be shorter than porous distances, so it suffices to recheck these 45 sets with all other sources deleted separately for each distance term. Every one has the same outside weight multiset: sixteen 9/8, eight 21/16 and two 3. This proves both minima and both classifications without relying on the supplied scripts. All 990 unordered comparisons gave 540 intersections of size zero and 450 of size one. For each state the 20 neighbors and their neighbors reach all 45 states, giving the distance profile (1,20,24), and hence radius and diameter two. For the analytic e=1 case at RESULT.md line 28, once the unique disjoint pair is 01,34 the two remaining duads must come from 03,04,13,14 and meet each other, so they are all equivalent to 13,14 by relabeling preserving the unordered pair of blocks. The listed second representative includes an extra disjoint pair and is extraneous; the first covers all actual e=1 cases. This does not affect the theorem.

## originality

FAIL

A distinct indexed Resultary finding, 9fe747acb02d, demonstrably covers the same graph, both conventions, the identical 45 flag-selected sets and weight profile, and the complete exchange statement. Its at-most-three convention equals the frozen exact-three convention since there are no smaller exchanges. Its path is later-dated; the decision is that the mathematical finding is already equivalently covered in the index, not that the other record had historical priority or that the frozen work was copied. No substantive distinct remainder was identified.

## value

PASS

As a mathematical result, the natural cage has a complete structural classification linking two domination notions to its flag geometry; the exchange obstruction and connected three-replacement graph are substantive, not just a one-number census. That value describes the theorem and does not confer distinctness on a second equivalent finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
