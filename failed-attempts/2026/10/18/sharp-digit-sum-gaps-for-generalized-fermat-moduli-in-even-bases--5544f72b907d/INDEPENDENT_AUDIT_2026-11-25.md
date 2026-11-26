# Independent mathematical audit

## correctness

PASS

The full spectrum is true. In frozen RESULT.md lines 21–55, reducing the powers of b modulo b^r+1 gives signed residue-class digit counts c_i. When the total digit weight is at most b, the integer signed evaluation has absolute value at most b*b^(r-1)=b^r, strictly less than the modulus. It must be zero; a coefficient of magnitude b would use all the weight with no other coefficient to cancel it. All remaining coefficients have magnitude less than b, so successive reductions modulo b give c_i=0 for every i, forcing even weight. The b+1 witness uses distinct positions because r>=2 and evaluates to 1+b*b^(r-1) modulo the modulus; the modulus itself has digit sum 2. Disjoint digit blocks add sums without carries. These two generators and the short-weight obstruction give the spectrum, count, largest gap and density, also for b=2. Inspected the frozen verification notes/code without execution; an independent bounded modular replay checked the b+1 witness for 60 pairs (even b=2 through 20, r=2 through 7). The frozen reachability checker, if run, covers all numeral lengths only for its tested parameters and digit caps, not the infinite theorem.

## originality

FAIL

The whole spectrum is a direct block-base corollary of established digit-sum facts. Set B=b^r and suppose N is a positive multiple of B+1 with s_b(N)<=b. For t=0,...,r-1, regroup the base-b digits of b^t N in blocks of r: s_B(b^t N)<=b^(r-1)s_b(N)<=B. Each b^t N is still a multiple of B+1. In even base B, no multiple of B+1 has odd digit sum at most B: by Clokie et al. Theorem 3, such a sum would be a signed sum of that many ±1 terms divisible by B+1, impossible. Since b is even, the parity of s_B(b^t N) is the sum of the digits of N in positions j with j+t congruent to 0 mod r. Each residue-class sum is therefore even and so is s_b(N). This handles even and odd r, not just the divisor-inclusion case. For sufficiency, the known digit-sum increment Theorem 4 applied to the sum 2 of the modulus gives b+1, and no-carry block concatenation gives precisely the proposed semigroup. This is positive coverage by reduction to prior results, not a failure for lack of access or an inference from same-day priority.

## value

FAIL

A genuinely unresolved exact gap spectrum would be worthwhile, but this one is determined by routine digit block regrouping and parity, plus the established increment rule. The auxiliary cancellation lemma uses the same short-weight bound and positional uniqueness; the package provides no separate unresolved application or nonroutine classification that would survive as a valuable repaired claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
