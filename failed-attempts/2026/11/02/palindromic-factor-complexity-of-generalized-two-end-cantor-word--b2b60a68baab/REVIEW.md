# Independent mathematical audit

## correctness

PASS

Read the on-disk formula, RESULT.md lines 10–12: the one-marker term is one indicator. Binary carrying in the ordered one positions gives a zero gap of (b−2)b^{v2(i)} at index i. To justify the first sentence of step 3, use the preceding gap calculation: at an interior 1 the adjacent gap indices are consecutive and exactly one is odd, so the adjacent gaps differ. A palindrome centered at that 1 cannot contain a neighboring 1 on both sides; the first marker also cannot have neighbors on both sides. Thus a palindrome with at least two 1's has an even number and is centered between consecutive markers. At a gap of index i with v2(i)=j, offsets h<2^j have equal valuations on both sides, yielding the palindromic b^{j+1}-block. At offset 2^j the shorter exterior gap has valuation j+1 when the left gap exists; the left boundary otherwise cuts the extension earlier. At i=3·2^j both gaps exist and attain the shorter length a b^{j+1}. Distinct levels have distinct central zero runs. This gives both exact endpoints and the parity constraint; levels two apart cannot overlap, and a singleton cannot overlap the second level. The stated sharp bound, examples, and ternary consistency follow. A separate enumeration computed complete factor languages for each tested length using the only possible adjacent aligned block pairs 00, 01 and 10 at scale b^k≥140, not an assumed sufficient prefix. It matched 1400 cases for b=3–12 and n=1–140. Replay: python3 /workspace/evidence/4.py; output /workspace/evidence/4.out. This finite check is supplementary. The frozen verifier's digit loop covers at most 5000 symbols per base despite broader wording in VERIFICATION.md; this does not affect the theorem.

## originality

FAIL

The exact frozen count and the full centered-factor classification are both covered by a distinct indexed Resultary result a2e5375cb6f9. This is demonstrable overlap with a broader statement, not a claim about who proved it first. The covering record's catalogue path is six calendar days later than the frozen path; those labels establish neither priority nor independence. No distinct mathematical remainder is established on the compared claims.

## value

PASS

As mathematics, a complete scale-resolved description for every length in a natural family of nonprimitive Cantor words is useful beyond evaluating a few counts. The valuation argument explains the sharp bound and exhibits the words responsible for every step. This assessment of the theorem's mathematical content does not restore it as a distinct contribution in the face of exact catalogue coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
