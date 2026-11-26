# Independent mathematical audit

## correctness

PASS

At n=1 the empty sum is 0, different from S(2)=2; two primes have distinct sums. In the prime/semiprime orientations, equality and adjacency give (a−1)(b−1)=2 or 0 respectively. Only the first is possible, with factors 2 and 3, giving (5,6), which checks. For semiprime/semiprime, the frozen integer factorization t(b−a−t)=1 follows from a+b=c+d and cd−ab=1. Sorting a≤b excludes the negative factorization; the positive one gives b=a+2 and c=d=a+1, impossible for three consecutive primes. An independent parity check gives the same exclusion: the sum of the two prime factors of an odd semiprime is even, so the even semiprime would have to be 4 (any other has factors 2 and an odd prime), whose neighbours are both prime. Finally S(8)=S(9)=6 and the two multiplicities are 3 and 2. Independent prime-power accumulation on n≤2,000,000 confirms 215 total equal-sum pairs, only (5,6) in the low layer, and the indicated sharp witness. Replay: python /workspace/checks/adjacent_audit.py. This sweep is only corroborative.

## originality

FAIL

A distinct indexed record proves the exact unrestricted multiplicity-based classification including prime squares and the no-two-semiprimes assertion. The sharpness witness (8,9) is already in the standard sequence, and its Ω-values follow from its displayed small factorizations. This establishes substantive coverage, not same-day priority or dependence.

## value

FAIL

The low-multiplicity layer is natural, but its complete classification is already independently contained in the distinct indexed statement. The frozen addition is only the depth of an already tabulated pair whose factors are 2³ and 3². Neither that elementary evaluation nor a larger regression range supplies a separate valuable finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
