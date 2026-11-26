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

Equal-count, hence equal-length, words yield disjoint cylinder pieces with common scale 1/(2^m 3^n) and mass M=p^m(1-p)^n; prefixing proves the offset recurrence. For a hypothesized orthonormal exponential basis translated to contain zero, Parseval for the normalized cylinder indicators gives a circle probability with the asserted difference moments zero and mass at least M at 1. Integrating the nonnegative squared Dirichlet polynomial gives (L+1)M<=1 for a complete difference interval [-L,L]. The independent exact reproduction check_certificates.py, not the frozen script, recovers for (9,9) and (11,5) the cardinalities 48620 and 4368, maxima 5028751 and 247687, and first gaps 3163277 and 92381; all rational signs at the two brackets and 2/3 were checked. The first mass polynomial exceeds one on (alpha,2/3] and the second on [2/3,beta), proving the open interval, strictly larger than the previous closed interval. Read VERIFICATION.md and verify_differences.py without executing the uploaded script. The claim is scoped to the open interval and is not an assertion of endpoint optimality: in fact 195913-11151=2*92381 in A_(11,5)-A_(11,5), so equality at beta would force sigma onto the 92381st roots of unity by equality in the Dirichlet-polynomial bound, contradicting the zero moment at twice 92381. This optional endpoint strengthening does not enter the stated theorem.

## originality

PASS

The novel evidence is the pair of large exact difference certificates and the resulting two-sided system-specific extension. The recurrence, equal-cylinder obstruction and original weight interval are prior work.

## value

PASS

Quantitatively enlarges a named same-system non-spectrality theorem at both ends, and does so by substantial exact difference certificates rather than a tolerance-level endpoint gain. The algebraic exclusions constrain attempts at the motivating all-weights conjecture and provide independently reusable certificates.

The dated certificate retains the supplied scientific assessment, sources and limitations.
