# Independent mathematical audit

## correctness

PASS

Closedness is checked in the factor itself. Unary factors are closed. For a two-run factor, any putative border must cross the lone transition; a proper suffix then has fewer letters before that transition than the prefix. Merely starting and ending in different letters is not sufficient to exclude borders in general, but the two-run claim is valid for this reason. A proper border of a three-run factor must be unary: a three-run border would contain both transitions but shorten the initial run in the suffix. This unary border occurs exactly twice precisely when it is the whole of two equal outer runs. In a four-run factor 0^i1^b0^c1^j a proper matching suffix must start in the third run, since starting later in the initial run shortens its initial zero block. The only candidate is 0^i1^j, and it occurs exactly twice if and only if i≤c and j≤b. This proves the disjoint families and n+1+pq. The attainable minima satisfy 2(p+q)≤n and are realized by placing all surplus in a first run of length p+n−2(p+q); balance at p+q=floor(n/2) gives the maximum and p=q=1 the minimum. The independent replay using consecutive-occurrence returns agrees on exact factor sets for 4,845 compositions and every excess spectrum at lengths 4–20. Another bounded check tested both starting letters at lengths 4–18. Neither finite experiment substitutes for the unrestricted proof.

## originality

FAIL

The earlier five-run Resultary proof directly gives the complete factor families needed for the four-run claim, not just a coincident product or related maximum. For arbitrary a,b,c,d≥1 append one zero to obtain W=0^a1^b0^c1^d0. Closedness is intrinsic to the factor, hence the closed factors of the prefix w are exactly those explicit families in W whose words occur in w. Retain the unary families (the extra run of length 1 changes no maximum), the three-run families with middle run 1^b and 0^c, and the 0-starting four-run family. Three-run factors with middle 1^d survive only if b=d and then already belong to the 1^b family. The 1-starting four-run family and all five-run factors cannot occur in w. Add the stipulated empty word. This yields the exact set claimed in the frozen record. Summation and the elementary range of two independent run minima yield the count, maximum and spectrum as direct corollaries. The earlier Finding is about five runs, but the earlier proof covers the decisive statements. This is documented prior implication, not a failure of the mathematics or of access.

## value

FAIL

The first run stratum above the binary minimum is a natural object, and the formula is a useful exposition. As a new result, however, it is a mechanically recoverable restriction of already published factor families, and the fixed-length spectrum follows by reallocating surplus run length after selecting the two minima. The frozen claim adds no independent invariant, obstruction, or nontrivial spectrum theorem beyond that prior classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
