# Independent mathematical audit

## correctness

PASS

The circular windows have length at most n and palindromes are counted as distinct nonempty strings. With sorted gaps a<=b<=c, zero- and one-marker counts are c and b+1. For each distinct internal gap, the two-marker radii are bounded by the smaller exterior gap; repeated gap values contribute one range. Three markers require two equal internal gaps and twice the exterior radius at most the remaining gap. Summing yields all three claimed cases, including zero gaps. With distinct gaps n<=3c, so the maximum requires c=ceil(n/3). The deficit of (a,b) from (c-2,c-1) is 3c-n, and listing its splits with a<b gives exactly the claimed triples. The distinct-gap maximum beats the two-equal count by floor(n/2)-ceil(n/3)-1>=1 for n>=14 (check residues modulo six); all-equal is smaller. The dihedral action realizes all permutations of three gaps. The verification note and checker were inspected, not executed; the reported run is bounded. The independent Python replay /workspace/branches/replay_frozen.py matched literal windows for 640 sorted triples through n=28 and all maximizing classes for 14<=n<=28, corroborating rather than proving the unrestricted gap formulas.

## originality

FAIL

The exact sorted-gap formula is already stated and proved for the same family and circular-window convention in a distinct indexed result. Its straightforward integer optimization yields the maximum and all equality cases; the absence of an explicit table of those triples in the indexed result does not leave a substantively distinct claim.

## value

FAIL

The exact sparse-marker invariant is natural, but the substantial wordwise computation is an existing exact result. The remaining display of maximizing patterns is a routine optimization of that same law over only the 0, 1, and 2 deficit cases. No separate nonmechanical mathematical contribution survives in the frozen claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
