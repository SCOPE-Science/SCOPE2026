# Independent mathematical audit

## correctness

PASS

The greedy endpoint is k plus the initial bit plus the number of equal adjacencies. The deletion drops are exactly 0 or 2 at the first and internal positions, with the zero cases given by initial 01 and internal 010/101, respectively; the last position drops 1 or 2. Hence the forbidden patterns and allowed endpoint costs give the claimed iff, including the last-pair restriction and no length-one MAS. In the run grammar, put d=1-t^2 y. Then S+t^(-1)T = t^2(1+t)^2 y^2/d + t^3 y^2(1+ty)^2/[d(d-t^3 y^2)]. Taking its odd part divided by t gives the claimed rational series on substitution x=t^2; it has no constant term in x. The recurrence and initials follow. The length-m universality follows by using one letter per block; absent words of length m+1 are exactly 1^j0^(m+1-j), by testing the number of runs in the greedy cost. The reciprocal denominator polynomial z(z-1)^2-1 has a simple root alpha>1 and a complex pair of modulus alpha^(-1/2); the positive dominant pole is not canceled. A separately written direct distinct-subword/deletion enumeration agreed with both the criterion and length polynomials through m=7.

## originality

FAIL

The distinct Resultary record 2ef499428033 states and proves the same bivariate census for the same binary hosts, including the same greedy-cost deletion characterization, the recurrence, growth and shortest count. This is affirmative full-claim coverage, not a failure based on an inaccessible paper or on resemblance of titles. Its record date is a day earlier, but the exact equivalence does not establish independent provenance or first authorship.

## value

PASS

The canonical binary alternator is a natural sharp test for the distinction between shortest and minimal absent patterns. A complete length census and a local decision criterion provide actionable information beyond a handful of totals or a general-purpose enumerator, and explain how an exponential/linear separation occurs over the binary alphabet. This is a judgment of the scientific content, not a second claim of novelty for the duplicate submission.

The dated certificate retains the supplied scientific assessment, sources and limitations.
