---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

PASS: Rotations of 0^a1^b are distinct for a,b>=1. The Myhill-Nerode quotient layers of the fixed-length rotation language have 2 min(j,a,b,n-j) distinct nonempty right languages at each 1<=j<n; summing yields 2ab intermediate states, with initial, accepting and dead states for 2ab+3 total. The submitted pure/mixed prefix-suffix collision analysis covers all split ranges and integer boundaries. Independent rotation-prefix residual enumeration verified all a,b=1..22 and every layer. Finite checks corroborate the all-parameter proof.

## originality

FAIL

FAIL decisive: October 25, 2026 full published Resultary theorem Exact state complexity of rotations of a two-run binary word establishes identical language C(0^a1^b), minimal complete DFA size 2ab+3 for all positive runs, exact quotient profile 2 min(a,b,d,n-d), and balanced-run extrema. Full RESULT.md read. The November 8 record restates the same theorem and proof approach; no new result remains.

## value

FAIL

FAIL: The exact counts, layer profiles, and balanced optimization were already completely proved in the earlier identical theorem. Rephrased counting cases and additional finite verification have no independent mathematical value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
