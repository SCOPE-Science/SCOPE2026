---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

The greedy embedding picks the first possible occurrence of each successive retained bit, so the legality test on skipped bits gives exactly one path per distinct output; no restriction applies after the last keep. Complementation swaps the one-bit masks, and concatenation gives A_(m+1)=A_m P A_m P. An independent exact reconstruction from tm3_coefficients.json checked all 128 entries of the two base matrices by literal skip-set enumeration from each start mask, both 4-by-4 parity identities through z^3 (128 scalar polynomial identities in n, including degrees through six), and both factored output-row polynomials. Together with the recurrence this proves every depth m>=2, not just the sampled depths. RESULT.md lines 18–32 give the replay specification; verify_tm3.py was inspected as the frozen reference implementation. As a separate check, write d_m for the number of double runs and R_m=n-d_m. For m>=2 the first and last runs are singletons, the second and penultimate are doubles, and no run has length three. Group a greedy deletion set by lengths of contiguous deleted blocks. With E=n-2d_m-1 adjacent pairs of run ends and B double runs followed by singletons, the three singleton blocks give binom(R_m,3)-E(R_m-2)+(E-B) by inclusion-exclusion; a two-block and a singleton give (d_m+1)(R_m-2)-B, and a contiguous triple can occur only at the suffix. Here d_m=n/2-1-d_(m-1), and B=d_m-2d_(m-2): consecutive double runs correspond to two consecutive changes in T_(m-1), grouped in pairs about its changing inter-dyad boundaries. The sum simplifies to binom(R_m,3)+R_m-2 at even depths and binom(R_m,3) at odd depths, reproducing both formulas, including m=2,3. The ratio to binom(n,3) tends to 8/27 by the cubic leading term; it is a distinct-output-to-pattern ratio, not the probability that an arbitrary pattern has no other pattern with the same output. Scope is fixed linear dyadic words and exactly three deletions.

## originality

PASS

Pass to the best of the inspected evidence for the exact parity-sensitive count of distinct three-deletion descendants of a fixed Thue–Morse iterate. Neither the general upper bound nor the nearby counts of factor types or deletion-ball intersections determine this specialization; the limit is a consequence, not a separate priority claim.

## value

PASS

The third deletion shadow is a natural exact invariant of the dyadic Thue–Morse word in synchronization and subsequence enumeration. The result captures what remains after many deletion sets coalesce and detects a genuine endpoint- and parity-dependent correction. It supplies an all-depth calibration for a fixed structured input beyond bounds or a finite table, without claiming an average-case deletion-channel result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
