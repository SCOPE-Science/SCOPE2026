---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

For odd y, factor y+5=2^j k with k odd, so the next odd term is ky. Any k>1 strictly increases odd states. Solving 2^j(k^2-2^{2h})=5(k-1) for a first entry to terminal 2^m-5 forces k=3,j=h=1 and initial y=1. Subsequent dyadic multiplication gives exact B(X) and logarithmic-squared asymptotic.

## originality

PASS

Existing terminal-state methods are reusable techniques, but they do not imply unique plus-five predecessor without solving equation (2).

## value

PASS

The plus-five integer map has a complete basin-vs-divergence classification with a unique genuine preterminal tail and exact growth law; not merely renaming a known coefficient.

The dated certificate retains the supplied scientific assessment, sources and limitations.
