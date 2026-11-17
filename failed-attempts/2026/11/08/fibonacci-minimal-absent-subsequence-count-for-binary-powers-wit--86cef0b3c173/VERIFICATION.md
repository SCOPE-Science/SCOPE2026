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

For W=(0^a1^b)^k with a,b>=2 the greedy-subsequence embedding criterion and one-letter-deletion bridge condition give two distinct ways to continue at each ready run, jumping one or two runs, with last-run counts 2 and 3. Initial zero and one cases yield F_(2k)+F_(2k+1)=F_(2k+2) for all k>=1. Independently generated full minimal absent word sets in small (a,b,k) instances and checked the exact counts, including k=1; read supplied verifier source. Finite enumeration supports but is not the infinite proof.

## originality

FAIL

Decisive prior coverage. Published Resultary record 2026-11-08 "Minimal absent scattered subsequences of repeated binary run blocks" proves for all a,b,k>=1 the COMPLETE minimal-absent language via a greedy block-cost/deletion criterion and the exact piecewise formula. Its case a,b>=2 is IDENTICALLY F_(2k+2) for the same W=(0^a1^b)^k, same labeled binary alphabet and same notion of minimal absent scattered subsequence. Full prior RESULT.md inspected with complete proof, so the target is an outright special case. The older 2021 general greedy bridge theorem is acknowledged but not the decisive coverage.

## value

FAIL

FAIL because the entire proposed exact invariant and run-length invariance are already established for every parameter in a stronger, explicitly published theorem. Another derivation using a Fibonacci run graph does not produce a mathematically distinct fact, and general source claims about benchmark usefulness cannot rescue a known-table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
