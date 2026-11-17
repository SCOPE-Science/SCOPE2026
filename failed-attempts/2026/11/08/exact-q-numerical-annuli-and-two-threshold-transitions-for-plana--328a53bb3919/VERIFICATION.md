---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-08.md",
      "INDEPENDENT_AUDIT_2026-11-08.json"
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

Takagi/unitary-congruence decomposition writes each planar scaled antiunitary as (aI+bJ)C, with a²+b²=c² and overlap |<Ax,x>| ranging over [0,a]. For constrained pairs, y=bar(q)x+sqrt(1-|q|²)u gives sharp modulus envelopes; elementary one-variable optimization and connected U(2) fill the complete *closed* annulus with hole at r<b/c and norm plateau through r<=a/c. Degenerate symmetric/skew cases and all boundaries are included. This matches full earlier published proofs and formulas, hence C PASS despite O/V failures.

## originality

FAIL

The October 18 published full result explicitly classifies *every scaled antiunitary on C²* with precisely the same inner radius (b sqrt(1-r²)-ar)_+, outer full-norm plateau and transition, including both thresholds and all boundaries. The November 1 published full result reproduces the normalized case and an A²-trace invariant. The assigned principal theorem has identical objects, parameters, implications and proof reduction; C passes, O fails. Its truth does not make the duplicate result original.

## value

FAIL

Identical exact annuli and their two transitions were published October 18 for the same entire scaled 2D antiunitary class, and again Nov 1 in normalized form. Re-derivation and further finite checks are not separate valuable mathematical findings.

The dated certificate retains the supplied scientific assessment, sources and limitations.
