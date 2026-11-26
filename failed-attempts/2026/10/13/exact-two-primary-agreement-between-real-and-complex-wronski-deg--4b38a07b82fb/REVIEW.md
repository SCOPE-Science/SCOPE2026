# Independent mathematical audit

## correctness

PASS

The two factorial formulas agree with Eremenko–Gabrielov for a≥b≥2 of opposite parity, using absolute real degree. Put M=ab/2, L=(a−b+1)/2 and U=(a+b−1)/2. In the quotient of degrees the leftover denominator combines the consecutive full factorial block with its odd-argument factorials canceled, leaving the factors (2t)!/t! for L≤t≤U. Each has valuation t by extracting the even terms; (2M)!/M! likewise has valuation M. There are b terms with endpoint sum a, so the difference is zero. Legendre's F(k)=k−s₂(k) gives the common binary expression after the linear terms cancel. For b=2 the source's Catalan specialization applies to every odd a≥3; modulo orientation sign the comparison is well-defined only in the stated nonzero branch. Independent finite replay `python3 /tmp/opencode/frozen-independent-checks.py wronski` verified the complex hook and real ratio calculations for opposite-parity pairs through a=45, and checked the real formula against a signed-tableau corner recurrence through a=12 (also checking vanishing on the complementary branch in that range). The valuation cancellation, not the range check, proves the theorem.

## originality

FAIL

The exact values for both degrees throughout the identical parameter range already occur together in Eremenko–Gabrielov. The audited identity is a direct arithmetic corollary of these stronger formulas: strip the even factors from (2k)!/k!, and the remaining power of 2 in the ratio is M minus the sum of b consecutive integers with mean a/2, identically zero. The digit sum is Legendre's formula on the published complex degree. This is an implication finding, not a claim that the equality is printed verbatim or that the claim is false.

## value

FAIL

The real-versus-complex comparison is natural and can be useful as a concise observation. As the submitted standalone exact finding it mechanically extracts the valuation of the two existing factorial products over their existing range, and then rewrites it by Legendre's formula. No unexplained new exact count, boundary case, or strengthened geometric conclusion survives that extraction as a distinct result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
