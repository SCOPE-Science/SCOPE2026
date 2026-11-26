# Independent mathematical audit

## correctness

PASS

With m=n−1 each support (i,j) uses the weight-one descendants at positions i and j−1, one output for adjacent ones and two otherwise. Any two consecutive adjacent starts collide after deleting a trailing zero from the first or leading zero from the second, when both inputs exist. Thus t+2e<=m and t<=ceil(m/2), giving the asserted upper bound. The construction uses odd singleton markers for the adjacent words and disjoint even marker pairs (4r+2,4r+4) for the nonadjacent words. After zero deletion the adjacent outputs still have gap one and disjoint start ranges {i−1,i}; the gap-three inputs yield only gaps two or three, with output first positions in disjoint ranges {4r+1,4r+2}. Unavailable boundary deletions only remove candidates. Its size ceil(m/2)+floor(m/4) equals the bound in all four residues; n=2 gives the unique input. Listing the support pairs takes O(n) word-position operations, without claiming O(n) time to print all expanded binary words. The supplied checker and its recorded finite output were inspected, not executed; the proof covers all n.

## originality

FAIL

Distinct indexed findings explicitly cover this all-length optimum and the same attaining construction, including an earlier-dated all-length result. The disposition rests on the mathematical overlap, not inference of provenance or order from dates.

## value

FAIL

The motivated exact weight-two optimum and its optimal packing would be useful if they filled a gap. Here the prior exact formula and support-pattern construction exhaust the claimed new content, and the counting proof does not deliver an additional distinct invariant or conclusion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
