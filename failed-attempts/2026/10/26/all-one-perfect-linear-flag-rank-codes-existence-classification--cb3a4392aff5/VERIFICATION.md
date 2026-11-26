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

An entry at (i,j) appears in every corner from i to j; weight below three is therefore confined to the diagonal and first superdiagonal. The allowable nonzero supports are at most two diagonal positions, or a nonzero first-superdiagonal entry and its two adjacent diagonal positions, where both nonzero corners have rank one. Avoiding these supports is exactly the pair and adjacent-triple independence condition on parity-check columns. The one-error syndromes exhaust the syndrome space once the diagonal directions exhaust projective space. At α=2 the adjacent pair already spans the syndrome space; α=1 would give n=1 and no nonzero weight-three codeword. For α≥3, one may choose each adjacent image outside the corresponding two-space, independently. A projective direction of the sum of two independent representatives supplies an explicit three-diagonal dependence, so the distance is exactly three over every finite field, not just primes. Higher coordinates cannot affect the low-weight test. The syndrome maps are surjective and changing the quotient basis acts freely, giving the stated count. Inspected VERIFICATION.md and the nested verification/verify.py and verification/verify_output.txt: the finite checks cover four prime-field parameters and not general prime powers or all kernels. Independently, the binary case gives 21+6·4=45 weight-two words and the code count 30·2^57. No uploaded code was run.

## originality

FAIL

The conditional length criterion and α≥3 are exactly prior. The submitted classification, unrestricted existence, and count are not quoted as verbatim prior theorems: they are mechanically obtained by applying the prior complete support test in arbitrary syndrome dimension and the prior perfectness criterion. The earlier 3-row formulation does not impose a rank restriction on its underlying column-dependence test. The derivation below checks this distinction rather than confusing a prior rank-three construction with an all-rank existence claim.

## value

FAIL

The labeled count and all-codimension formulation are natural, but the exact count here is a direct product of already-determined local column choices with a standard change-of-basis divisor. No further metric-specific enumeration, isometry classification, or obstruction independent of the prior support and volume results remains.

The dated certificate retains the supplied scientific assessment, sources and limitations.
