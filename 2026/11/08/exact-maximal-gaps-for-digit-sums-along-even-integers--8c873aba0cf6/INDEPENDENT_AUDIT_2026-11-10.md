# Independent mathematical audit

## correctness

PASS

In even bases the two affine last-digit formulas split each aligned q-block into disjoint parity classes; s_q(2k+1)=s_q(2k)+1 has no carry and each aligned q-block is exactly a permutation. Thus gaps are at most 2q-1. The displayed q-2 carry-string for 2k constructs an occurrence at the start of one block and at the end of the next, with no intervening hit; positive high-digit shifts give infinitely many. For odd q, s_q(m)=m mod 2 uniquely selects the even digit-sum class r_j mod 2q. Each q^2-block of m realizes 0,...,2q-2 plus s_q(k), so omits at most one residue; consecutive block omissions differ because s_q(k+1)-s_q(k) is odd. Two full omitted blocks cannot occur. Integer parity tightens the m-gap to 3q^2-1, and the explicit prefix 3q^2-1 with digit sum 2q yields equality. Verified endpoint and interior cases independently for every j in q=2,...,11; finite tests are corroboration, not proof.

## originality

PASS

Boreico–El-Baz–Stoll 2014 studies exactly s_q(2n) mod q, but the principal result proves global discrepancy oscillation, not sharp consecutive-return spacing. Equivalent formulation as longest constant-symbol avoidance in generalized Thue–Morse coding was queried; no dominating formula or exact earlier table was established. The explicit local covering and sharp carry construction are not consequences of discrepancy signs. Positive best-of-knowledge decision, with historical word-combinatorics and original Dekking literature risks.

## value

PASS

This is the natural sharp recurrence-gap invariant of an independently studied digit-sum sequence, quantified for all bases and all residues with infinitely recurring witnesses. The surprising even/odd growth transition (linear versus quadratic) is a real structural distinction not implied by average frequency or discrepancy estimates.

The dated certificate retains the supplied scientific assessment, sources and limitations.
