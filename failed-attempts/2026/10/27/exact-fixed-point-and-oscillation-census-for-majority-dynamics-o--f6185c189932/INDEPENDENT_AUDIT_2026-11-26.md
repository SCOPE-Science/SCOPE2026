# Independent mathematical audit

## correctness

PASS

Under hub zero the local weight map on 0,1,2,3 is 0,0,1,3; under hub one it is 0,2,3,3. Mixed types that survive a switch flip bitwise, so two complementary flips restore the actual bits. The first retention at time t makes the hub permanent by monotonicity of outer total, and uniformizes the triangles by t+2. If there are three initial switches, the states at times 1 and 3 agree including the hub; otherwise t<=2, proving F^6=F^4. For r=1 every initial hub-zero state is fixed by time one or already periodic (by the four weights), with nonperiodic examples. For r=2 initial hub zero and outer weight pairs capable of switching are (1,3),(2,2),(2,3),(3,3); only (2,2) can switch back and it switches a third time. Pair (2,3) has exact depth three. For r=3 and 4 the given hub-one witnesses switch twice and then lock with mixed triangles requiring two further updates. A zero/full pair adds three to both the total and threshold, so extends both witnesses. Fixed triangles must be uniform; two-cycles must switch the hub strictly in both directions, with mixed triangles exactly the three doubletons in the hub-zero phase. Counting that phase yields the stated multinomial, with no extra factor of two. The exponential bound is the union bound on the two symmetric failure tails using the weight polynomial 1+3u^2+u^3; the derivative of the tilted expression changes sign at u^2(1+u)=1. P_1<=2^(r+1), so dividing P_1+2C_2 by 2*8^r gives the asserted density. The all-size check is analytic; the frozen code and CHECKS.txt were inspected but not treated as independent proof.

## originality

FAIL

A distinct indexed statement directly covers the central claims on the identical graph, update convention and labeled state space: sharp preperiods, fixed and primitive-cycle counts, and the leading exponential laws. This is demonstrated equivalent coverage in the available catalogue, not a finding about historical priority or derivation. The submitted smaller constant in an exponential error bound is distinct numerically but is the exponential tilt of the same one-triangle distribution; it does not establish originality of the census.

## value

FAIL

Sharp cutoff and labeled attractor counts would be useful if not already covered for this family. The distinct remainder is a tighter one-sided error bound from the textbook exponential-moment optimization of the already specified weight distribution. Without a justified need for that improvement, a matching lower bound, or any new structural census, it is not a valuable surviving result on its own.

The dated certificate retains the supplied scientific assessment, sources and limitations.
