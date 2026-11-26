# Independent mathematical audit

## correctness

PASS

The largest Apéry member is 4m+r, so x_r=4. For i+j=m+r the Kunz inequalities give x_i+x_j≥3, or x_i≥2 at a fixed point; these are disjoint orbits on r+1 through m−1. The only noncarry constraint with target r is i=j=1 on the second line, giving x_1≥2. Summing the disjoint lower bounds gives ceil((3m+r+1)/2), and equality forces precisely the indicated independent binary choices and fixed coordinates. Conversely every other target coordinate is ≤2, so positivity suffices there, while the constraints targeting 4 are satisfied by construction. The required largest Apéry member follows from the other coordinates being ≤2. The empty pair sets at the smallest admissible m work as well. The usual F-reflection bound with equality exactly in the symmetric/pseudosymmetric cases identifies these with all irreducibles. An independent exhaustive Kunz-vector search through m=11 found the full minimizer sets, not just the counts, in all 19 cases; it is bounded corroboration of the symbolic argument. Replay: /workspace/branches/0743ace4-b9c8-48d9-9e65-2fa9f83a0b80/independent_kunz_check.py; output: independent_check_full.txt in the same directory. The frozen verification program was inspected, not run.

## originality

PASS

The supported distinct claim is the all-m product classification and count of the irreducible layer on the two specified lines, not the genus lower bound, Kunz machinery, or any finite-case enumeration. The relevant counting theorem and recurrences miss both lines; the general fixed-pair algorithm enumerates the candidate set but does not give independence of choices or the uniform count. Known coordinate and tabulation overlaps are credited below.

## value

PASS

The first admissible lines beyond the established m≥(F+1)/3 regime give a motivated boundary problem; the intervening multiple of m is impossible. The equality-layer factorization provides all irreducibles and a power-of-two count for unbounded multiplicity without searching the Kunz polytope. It does not replace the census of higher genera.

The dated certificate retains the supplied scientific assessment, sources and limitations.
