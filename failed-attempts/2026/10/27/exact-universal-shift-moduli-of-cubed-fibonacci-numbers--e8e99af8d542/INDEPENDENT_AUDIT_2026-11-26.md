# Independent mathematical audit

## correctness

PASS

Cubing Binet's formula gives the four characteristic roots α³, β³, −α, −β, yielding the monic integer recurrence and the reduction to n=0,1,2,3. Evaluation of the coefficient vector of (aX+bY)^3−X³, a=F_{k−1}, b=F_k, has determinant of absolute value 2 at the four consecutive Fibonacci pairs, so its content c divides D and D divides 2c. For odd k, Cassini gives a²≡−1 mod b; modulo an odd prime dividing b, a³≡1 would force a=−1 and contradict Cassini. If 3∤k the n=0 value is odd; if k≡3 mod 6, b≡2 and F_{k+1}≡3 mod 4, giving exactly one factor of 2 in D from the n=1 witness. For k=2m, gcd(b,a³−1)=gcd(b,a−1), which the doubling identities and consecutive-term coprimality reduce to L_m for odd m or F_m for even m. Only 3 can change the odd-prime valuation thanks to the middle coefficients' factor 3. Modulo 3, 3|b precisely when 4|k, and a≡1 rather than −1 precisely in the 8|k branch. In that branch both b and a−1 have 3-valuation e=v₃(F_m) and a³−1 has valuation e+1, so the content acquires exactly one extra factor 3. For even k divisible by 3, the even-shift factorizations and parity give v₂(b)>v₂(a−1)=v₂(c); the n=1 difference (a+b)^3−1 therefore excludes the sole possible additional factor of 2. This covers k=1 and k=2, and proves the universal gcd, not just necessary conditions. A separate bounded Python check took the gcd of 65 actual differences for each k=1..256, all matching; full modular orbit checks mod 9 gave least periods 8 and 24 for the cubes and first powers, respectively. No uploaded script was executed.

## originality

FAIL

The exact same greatest modulus for every positive shift is proved by a distinct indexed record, not merely suggested by a title or by theorems about window sums. The covering record is dated November 2 UTC, later than the frozen October 27 UTC record. This is verified existing mathematical coverage for the audit, not a finding of earlier priority.

## value

FAIL

The invariant is natural and its exceptional 3-adic branch would be useful as a new exact fact. The whole invariant, including that branch, is already established in the checked record; the modulus-9 illustration is an immediate specialization, not an independently useful unknown result. No distinct surviving claim to repair was found.

The dated certificate retains the supplied scientific assessment, sources and limitations.
