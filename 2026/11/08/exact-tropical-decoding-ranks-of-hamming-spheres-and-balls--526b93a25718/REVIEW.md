# Independent mathematical audit

## correctness

PASS

A substitution changes total weight by at most one, and deleting or inserting nonzero symbols attains the required distance. All weights are represented, so word indexing just duplicates rows and columns of the weight array. Put a=max(0,r-t), b=min(ell,r), k=b-a+1. The source's row templates work because rows outside [a,b] differ from the nearest boundary template by an additive constant. Independently, with F(s)=|s| or max(0,s), the k allocation terms F(i-h)+F(j-r+h), a<=h<=b, are bounded below by F(i+j-r); equality holds at an integer h between i and r-j, since that interval always intersects [a,b]. The witness offsets left and right weights against each other, giving entries F(i-j). Its diagonal is zero and every nonidentity permutation has some i>j, hence has positive cost in either case. In any smaller outer-product representation two assigned cells must share an attaining term, and swapping their columns makes a competing assignment no more costly. Thus both ranks are exactly k=1+min(ell,t,r,m-r), including zero cut lengths and the two endpoint radii. The balanced cut realizes the stated range. Independent bounded replay: python3 /workspace/independent_checks.py 2 checked 330 exhaustive compressed tropical ranks, 8,774 direct codeword distances over alphabets of size 2, 3 and 5 through length four, and the allocation factor at these parameters. Those checks do not replace the proof.

## originality

PASS

The closest verified result gives the same two ranks for binary linear codes via a trellis dimension, not the weight-dependent ranks of radial decoding arrays. Neither the verified general rank comparison nor the identified Monge theory provides the combined closed formula. The result is distinct on the inspected evidence, not a certification of historical priority.

## value

PASS

For canonical radial targets, the exact width of a separated min-plus decoding representation is a natural invariant. The result identifies the entire cut profile and explains why two different distance functions pay the same rank cost, and why the binary nonlinear case can have rank three rather than a power of two. This is a concrete extension of the representational comparison beyond linear codes, not a claim about arbitrary nonlinear trellises, approximate rank, or computational runtime.

The dated certificate retains the supplied scientific assessment, sources and limitations.
