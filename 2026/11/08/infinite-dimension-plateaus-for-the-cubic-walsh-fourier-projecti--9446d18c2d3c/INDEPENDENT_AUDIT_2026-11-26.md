# Independent mathematical audit

## correctness

PASS

The norm of normalized convolution is the absolute kernel mean by taking the sign of the real kernel at the identity, and self-adjointness gives the L1 endpoint by duality. The same sign witness works over either scalar field. Adding an independent sign Y changes the cubic kernel from E3 to E3+Y E2, and the average of |E3+E2| and |E3-E2| is max(|E3|,|E2|). This gives the stated increment and the pointwise equality condition. Newton identities on signs give the displayed E2 and E3. For even n, s=0 witnesses strict increase; for odd n, the points |s|=1 contribute zero increment. At positive odd s>=3 the squared comparison factors with sign given by (s(s-2)-3n)(s(s+2)-3n). The corresponding open intervals exactly partition the interior of [3,n(n+2)] except their shared endpoints. This proves equality exactly at 3n=r(r+2) for odd r>=3: in the converse n=r(r+2)/3>=r+2 and n is odd, so both adjacent lattice points are available. Integrality is r congruent to 1 or 3 mod 6, giving the two families and count sqrt(X/3)+O(1). Read the frozen proof, verification notes and code without executing uploaded code. Direct sign enumeration for dimensions 3–8 and exact comparisons through n=300 were separately reproduced (including plateaus 225 and 261 above the frozen check range). Replay: /workspace/branches/3899ca18-66a6-441f-9dec-532d71e4c5c2/cubic_walsh_independent_check.py. The bounded check is only corroboration.

## originality

PASS

The known norm identity, fixed-degree asymptotics and cubic Krawtchouk algebra are not new. The supported distinct claim is the exact one-step equality classification for the cubic endpoint norms and its positive-part formula. The strongest same-invariant comparisons give the exact per-dimension norm or its asymptotics, not the pointwise one-step comparison and infinite zero-increment set. An integer root in the next even dimension is another formulation of the new plateau criterion; the arithmetic of those roots is not a separately new claim.

## value

PASS

This classifies exactly when extending the ambient cube adds no endpoint norm, despite the strictly enlarged cubic span. It reveals a sparse but infinite parity-sensitive obstruction and gives a quantitative increment formula. One can use this exact comparison to distinguish finite-dimensional norm behavior that per-dimension leading asymptotics do not resolve.

The dated certificate retains the supplied scientific assessment, sources and limitations.
