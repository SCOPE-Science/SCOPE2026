# Independent mathematical audit

## correctness

PASS

Reindex the Strehl expansion by j=n-k and cancel factorials to obtain the product of binomial(n,2j) and the two central binomial coefficients at j and n-j. Legendre gives central-binomial valuation s_2, and the digit-sum inequality bounds each summand's valuation below by s_2(n). Equality needs carry-free addition j+(n-j) and an odd binomial(n,2j). The first condition says the support of j is a submask of n; Lucas gives the corresponding condition for 2j. Thus the set of allowable bits of j is exactly the set of starts of adjacent 11s. Every submask of that set is allowed, including with overlapping pairs: doubling shifts all bits without collision, and the condition 2j<=n follows automatically. Therefore exactly 2^a_2(n) terms are odd after division and the quotient parity follows. The zero index is included, and the length-L binary avoidance count gives Fib(L+2) with zero or Fib(L+2)-1 without it. Dyadic bounds extend to ordinary density zero. The frozen finite checker was read, not executed.

## originality

FAIL

The earlier 2026/10/18 Resultary record concerns the identical cubic Franel numbers for all n>=0 and proves the identical sharpness criterion, quotient parity and exact count of minimum-valuation Strehl summands. Its census includes zero, so subtracting one yields the frozen positive-index census. This is verified prior coverage, not failure due to inaccessible literature.

## value

FAIL

The sharpness classification is a meaningful invariant in itself, but this frozen finding adds no new exact fact, case, or consequence beyond the earlier exact theorem. Naming the equality class Fibbinary and subtracting zero from the existing census do not supply incremental scientific value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
