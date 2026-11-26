---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

After dephasing at a selected row and column, determinant vanishing equates two sums of three roots. Divisibility by the prime-power cyclotomic polynomial makes signed coefficients constant on fibers of size p; p>3 forces them all to vanish. Matching the diagonal product exponent to the three possible opposite exponents forces a repeated normalized row or column in every case. Two restricted rows are proportional exactly when their difference valuation plus the minimum column difference valuation is at least m; applying this to some versus all rows, and dually to columns, proves the ranks. Counting the first differing digits, with one distinguished close pair only for unequal valuations, gives the stated unordered triple counts. For the asymptotic, Pr(U>=a)=(N/p^a-1)(N/p^a-2)/((N-1)(N-2)); the column close-pair count is exact by inclusion–exclusion. For a fixed a>=1 the scaled contribution from U=a tends to 3(1-p^-2)p^-2a(p^a-1), dominated by a constant times p^-a. This sums to 3/p; the symmetric event contributes another 3/p. On U,S<=L the intersection costs O(p^(2L)/N^2), and outside it the scaled tail is O(p^-L), so no overlap remains at order N^-1. Rank one costs O(m/N^2) in probability. An independent bounded check enumerated all 317,750 triples at N=125, reproduced the six type counts and hence the census (5,687,500; 725,000,000; 100,234,375,000), and checked a representative of each rank by exact cyclotomic reduction. This was not an exhaustive comparison of N=125 determinants. Replay: /workspace/branches/6d052387-2e4f-4ebf-a568-821901dad651/independent_check.py; the frozen verifier was read, not executed.

## originality

FAIL

A distinct indexed result supplies the same restricted complex rank test, valuation-stratum counts, full rank census, and sharp fixed-prime limit on a larger domain. The rank-one negligible term follows directly from its rank-one rule and stratum formula. Thus the frozen claim is covered in the audited corpus, not merely similar in title or check size. This is not a finding that the frozen argument is false, nor a claim that the matching entry predates it or was independently derived. The matching catalogue entry is dated later; historical priority is not established by this comparison.

## value

PASS

The mathematical question is substantive: the exact census and sharp sparse-singularity law measure how often failure occurs for two random triples, rather than whether some minor of a chosen row pattern can be singular. The fixed-prime leading constant and separation of rank-one from rank-two defects are useful beyond individual small-order checks. This assessment of the mathematical target does not award distinct contribution credit for a covered finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
