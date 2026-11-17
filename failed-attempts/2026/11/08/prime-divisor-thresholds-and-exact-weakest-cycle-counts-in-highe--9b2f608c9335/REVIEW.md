# Independent mathematical audit

## correctness

PASS

PASS: For each primitive word with k right visits the signed monomial derivative splits into d=gcd(M,k) coordinate cycles of length M/d. Every cycle has at least k/d right-step doubling exponents, implying log2 chi>=k/(Mn) for d>1, while d=1 yields 1/M. Any d>1 forces k>=p, and a primitive p-right word with adjacent right visits realizes the sharp bound. Conversely equality for n>p enforces k=d=p and a zero left gap. Circularly nonadjacent p-subsets are n/p*C(n-p-1,p-1), and proper-power p-right words have all gaps positive: therefore division by n counts primitive cycles. Small n<=p and n=1 handled. Independent finite symbolic verification re-enumerated 56 (M,n) pairs, M=4..10, n=1..8; finite tests do not replace proof.

## originality

FAIL

FAIL: A November 2, 2026 prior theorem proves the same exact weakest absolute return eigenvalue at each n and says it is realized at least period n, and supplies the all-itinerary histogram and exact extremizer count E_M(n). Its count equals this submission’s n-times cycle count and its extremizers already have p right visits and a zero cyclic gap; these are primitive. All claimed new cases including all even dimensions and p=3 follow from the stronger prior. No genuinely independent remainder remains.

## value

FAIL

FAIL: The correct cyclic-necks enumeration, normalized nth-root restatement and primitive-orbit count are immediate translations of the prior exact same-model histogram and extremizer characterization. No independent gap or new invariant is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
