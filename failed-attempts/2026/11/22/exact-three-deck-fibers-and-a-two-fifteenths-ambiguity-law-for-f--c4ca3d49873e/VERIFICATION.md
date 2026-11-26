---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For the four ones the counts of preceding zeros are a, a+b, N-a-b, N-a. Reversal gives D_100=D_001=H and D_110=D_011; D_011=6a+3b+c=N+t for t=4a+b, and the count of 101 is 6b+4c=4N-2t. Each one contributes z_i(N-z_i) to 010, giving 2N(N-1)-2H. The 000 and 111 counts are fixed, including N<3. Summing binom(z_i,2) gives the stated quadratic in a at fixed N,t, so the only possible distinct partner is its reflected root, a'=a+(b-c)/5. Then b'=b-4(b-c)/5 and c'=c+6(b-c)/5. Orient by b>c, since b'-c'=-(b-c); the divisibility condition gives d>=1 and all partner gaps are then nonnegative. This proves all in-class fibers, including empty gaps. The unique parametrization gives N=2a+3c+10d and the generating series, the distinct-deck count, and the exact attainable lengths (subtract 10 and use the semigroup of 2 and 3). For fixed d the count from 2a+3c=N-10d is (N-10d)/6+O(1); summation gives N^2/120+O(N) compared to N^2/8+O(N) words, hence 2/15. Independently enumerating triples of positions in the length-14 pair gives (120,65,50,15,65,30,15,4) in both cases. The exact replay is the algebra in RESULT.md lines 31–69; verify.py and verify_output.txt were inspected as bounded corroboration. No unrestricted fiber-size claim follows.

## originality

FAIL

The statements are correct, but the full classification and the numerical census are a direct specialization of the earlier published fixed-weight three-deck moment theorem, followed by solving a one-variable quadratic and counting its admissible gap parameters. The prior result does not print these palindrome counts; coverage here is by implication, not a purported identical table. The first witness itself is already known, even for the four-deck.

## value

FAIL

Fixed-content symmetric reconstruction is a natural question and the formulas make a useful corollary. Under the exact-invariant value standard, however, the known complete moment criterion and routine one-dimensional elimination already determine the purported new classification and census. The rational series, census and limiting fraction do not survive as independently valuable unknown facts under that standard; neither does the credited first witness. No stand-alone repair is supported.

The dated certificate retains the supplied scientific assessment, sources and limitations.
