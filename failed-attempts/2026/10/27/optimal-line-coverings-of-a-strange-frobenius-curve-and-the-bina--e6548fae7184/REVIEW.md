# Independent mathematical audit

## correctness

PASS

The curve has q graph points and only P_infinity at Z=0. For two distinct parameters s,s+u, the affine secant has slope u^(p^2-1); its fiber is a coset of the kernel u F_p because gcd(p^2-1,p^m-1)=p-1 for odd m. This is exactly the affine line through the two parameters, and hence all blocks and their pair multiplicities follow. All projective lines meet at most p points of the curve; a parallel affine spread and one line through infinity attain ceil((q+1)/p)=q/p+1. For odd p, counting affine incidences excludes two or more lines through infinity or any nonmaximal ordinary line. The q secant incidences can have just one hole only if there is also exactly one double point. Every affine line has parameter sum zero, as does all of F_q, so the double point minus the hole would be zero, impossible. Thus the cover uniquely determines its spread and a freely chosen line through infinity. Partitioning into affine two-plane cosets and independently choosing any of p+1 parallel line partitions proves the stated lower bound (not a count of all covers). In the binary example the four different secants on eight parameters cover seven with one repeat, pairing the remaining parameters covers all but the same hole, and the vertical line covers that hole and infinity; the size meets the same lower bound. Independent replay (python3 -B /workspace/branches/independent_replay.py 4) enumerated slope fibers rather than generating secants from input blocks in fields of sizes 3, 8, 27 and 125, yielding respectively 1, 28, 117 and 775 maximal secants and verifying pair uniqueness, the odd-characteristic moments and the binary witness. The proof, not the bounded check, treats all the claimed fields.

## originality

FAIL

Earlier exact Resultary coverage establishes the odd-characteristic complete spread classification, the secant identification and a stronger binary classification/count. The different odd-characteristic numerical lower bound is obtained by allowing all parallel directions in each independent two-plane choice of the prior proof, rather than restricting to two choices. It is a genuine numerical improvement but a mechanically available consequence of that same construction, not an independent surviving contribution under review.

## value

FAIL

The full extremizer geometry and the binary boundary are substantive questions, but their answers are already covered. The only differing deliverable increases the numerical lower bound by counting every available direction in the same independent-plane construction that previously used two. It neither distinguishes a new configuration type nor adds an independently motivated extremal result. No separate viable repair is supported by the frozen contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
