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

Pinned RESULT.md blob 954197523b7255c9e655c4c9b8f5acf3bf58117f proves Hamming distance-two criterion inductively, then classifies selected columns by Q2 parity. Every legal set is either a partial same-parity transversal (two n-fold joins of S0) or one of 4n adjacent-label column edges. This yields exact F=2(1+2z)^n-1+4nz² and facets, and the two connected spheres linked by 4n edges yield S^(n-1) vee S^(n-1) vee (4n-1) S1; k-token replacement connectivity follows. Independently all 2^8 subsets for n=2 and all 2^12 for n=3 were checked directly against all-pairs shortest-path visibility and analytic face counts 25 and 65. These are finite corroboration; arbitrary n follows from the column argument. n=2 merges all summands into nine circles.

## originality

PASS

Best-of-knowledge: exact product-family face/facet polynomial, integral wedge homotopy and fixed-cardinality reconfiguration are not included in the inspected more general distance-two criterion and extremal maximum. Search does not prove universal novelty.

## value

PASS

Structural classification of every face and the integral homotopy of a natural Hamming graph family, plus a clean reconfiguration connectivity threshold, are independent mathematically meaningful invariants; they exceed routine evaluation of the already known maximum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
