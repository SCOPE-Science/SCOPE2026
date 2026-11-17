# Independent mathematical audit

## correctness

PASS

Factor presence with one 1 is exactly a southwest union of rectangles with corners (a,b),(b,c),(c,d); with two 1s only inner gap b or c is possible and rectangle corners are (a,c),(b,d). Minimal absence is absence with present length-(m-1) prefix/suffix. The zero-one count classification covers 0..4 ones, and every omitted higher-one candidate has an absent proper factor. Counting frontier drops yields |MAW|≤K+13 where K=min(max(a,b,c),max(b,c,d)); if the sum s of three nonmaximal gaps is ≥11, this is < n. For s≤10, the verified finite base of 4×3×C(13,3)=3432 cases plus a rigorously justified eventual affine dependence for the single large gap reduces all lengths to bounded checks. Independent direct substrings/MAW enumerator for all three-one words n=7..14 found max count n and exactly two extremizers, 110^(n-3)1 and 10^(n-3)11. Actual VERIFY.py source inspection shows the full finite certificate and separate direct classification checks.

## originality

PASS

Best-of-knowledge new exact fixed-weight-three binary MAW capacity and complete four-gap classification. Earlier general MAW algorithms and RLE bounds cover computation or order of growth but not the sharp n bound with exactly two labeled extremizers for every n≥7; no matching theorem located in searched mathematical findings. The gap-frontier classification is more than simply rerunning a general algorithm, though unindexed equivalent fixed-content work remains a risk.

## value

PASS

Minimal absent factors form a natural antifactor basis used in text algorithms and compressed representations; fixing three isolated markers gives a meaningful sparse-string subclass. The full zero-gap structural classification, exact maximum n at every n≥7 and exhaustive equality conditions constitute a natural complete classification and sharp cutoff, not an arbitrary small case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
