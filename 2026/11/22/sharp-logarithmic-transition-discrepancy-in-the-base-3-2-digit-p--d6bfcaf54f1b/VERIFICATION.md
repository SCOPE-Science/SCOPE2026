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

In the stated convention n=∑d_j(3/2)^j, the units digit is n mod 3 and the remaining value is 2⌊n/3⌋, proving the fixed-word parity rule including w0=0. For t_j=w_{2j}, adjacent signs in one auxiliary triple are (1,−ε_{2m},−ε_{2m+1}), which gives the three displayed branches for D(N) with additive terms 0,4, or −2/8. Iteration shrinks the argument by at least the factor 2/3 for N>0. The t-to-w block map contributes one transition of each orientation inside every triple; boundary orientation imbalance telescopes to t_N−t_0. Thus Q_ab(3N)−6N/5 equals −D(N)/20 plus the signed, bounded endpoint term, and the other two residues change the error by O(1). For the lower bound, the congruences for m0 are compatible and give m0≤3·4^k; multiplication of 5m+6 by 9/4 preserves the requisite divisibility, ensuring all k steps are integral and all m_j are multiples of 3. At 2m_j the sign is +1; the two inverse steps visit 3m_j+2 and 3(3m_j+2)/2, giving net drift +2. Consequently one of the two endpoint defects has magnitude at least k at a prefix ≤30·9^k, yielding the lower bound for both orientations for every sufficiently large X by choosing k=⌊log_9(X/30)⌋. This is maximal prefix discrepancy, not a lower bound at every prefix. Independently checked 6,000 direct signed prefixes, the two transfers at 2,000 complete-block prefixes, and 16 exact CRT witnesses. Replay: python3 /workspace/branches/frozen_math_reproductions.py 4. These are finite corroboration; the proof supplies the quantifiers. The upload was inspected, not executed.

## originality

PASS

The record itself limits novelty to the sharp order of maximal prefix error. Known symbol recurrences and a previous run-statistics theorem already supply the word and the limiting oriented densities, but the verified comparisons do not establish a quantitative theorem with a matching logarithmic lower bound for this word.

## value

PASS

The exact error order quantifies convergence for a named, studied rational-base sequence whose transition frequencies were explicitly conjectured. The lower bound rules out bounded or sublogarithmic maximal error despite near-linear predictability of both counts, and the congruence construction explains the persistent drift rather than inferring it from a table. The limiting frequency alone is not counted as the contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
