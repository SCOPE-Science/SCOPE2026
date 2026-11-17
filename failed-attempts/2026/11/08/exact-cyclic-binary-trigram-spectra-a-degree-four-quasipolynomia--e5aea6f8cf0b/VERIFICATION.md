---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

Every cyclic length-three histogram is a nonnegative balanced flow with connected positive-edge support on the four-vertex binary order-two de Bruijn graph, and conversely an Euler circuit realizes it, including n=1,2. Balancing gives x_100=x_001, x_110=x_011, x_010=x_001+x_101-x_011. The disjoint two-bridge, one-bridge and isolated-loop/cycle cases produce the stated rational generating function; poles at primitive third and fourth roots make 12 the least quasipolynomial period. The displayed exact formula includes all boundary cases and gives the natural zero-error count of profile classes. A fresh independent word enumerator checks its exact polynomial for n=1..12. These tests are corroborative; Euler-support partition supplies the unbounded proof.

## originality

FAIL

Decisive earlier mathematical coverage. Published November 2, 2026 Resultary exact cyclic binary three-gram profiles gives the same eight coordinates, same modulo-n cyclic convention for all n>=1, EXACT SAME quartic formula with parity/mod3/mod4 corrections, same least period 12 and zero-error code capacity. Published October 26, 2026 gives an algebraically identical all-length rational generating function and complete connected de Bruijn-flow partition. The present alternate parameters and partial fractions do not yield an independent new claim.

## value

FAIL

The counting problem is natural, but the submitted final claim is entirely already established by the October 26 and November 2 published results. Re-enumeration with a different parameterization, finite checking and restatement as code size are covered deductions, without a newly motivated invariant or structural distinction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
