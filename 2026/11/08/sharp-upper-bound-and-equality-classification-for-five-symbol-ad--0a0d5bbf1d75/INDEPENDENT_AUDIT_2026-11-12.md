# Independent mathematical audit

## correctness

PASS

For w=abcde, B(w)={cde,ade,abe,abc}. Weight palindromic output 1, other 1/3. If none palindromic, a,c,e pairwise distinct and at least three distinct nonpalindromic outputs, hence local weight>=1 universally. Disjoint shadows bound codewords by q²+(q³-q²)/3. Equality forces full output partition and local weight exactly one: singleton balls are period-two ababa; other families are xbybz with distinct x,y,z, whose nonpalindromic outputs each correspond to one of three directed transitive pairs. Thus every maximizer is q independent labeled directed triple systems and D(q)^q such codes. Cited existence theorem yields equality for q>=3 and q=0,1 mod3; claims no exact A_q for q=2 mod3. Independently enumerated every word for q=2..5 and verified local shadow inequality.

## originality

PASS

Chee–Li–Zhang (ISIT 2015) already produced this family by lifting perfect 3-symbol single-deletion codes; original family and its size not new. The surviving bound is over all possible length-five correcting codes, and the rigidity/count of all attaining it. Older Resultary minimum ternary perfect code (8) addresses minimum rather than maximum (15); ordinary two-deletion bounds use nonadjacent deletions, a different channel.

## value

PASS

Completes a natural exact short-block coding problem in an infinite alphabet congruence family and identifies all optimal code structures, providing a universally sharp dual shadow inequality; more than a known construction or isolated tiny instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
