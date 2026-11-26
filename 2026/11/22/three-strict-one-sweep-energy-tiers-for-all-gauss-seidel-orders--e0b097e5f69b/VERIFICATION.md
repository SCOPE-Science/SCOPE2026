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

A is SPD exactly in the stated positive-coupling range up to t=1/2. The dihedral action preserves A and produces three disjoint free orbits, exhausting 24 orders. Independently using triangular splitting in sweep coordinates, G=−(I+L)^{-1}L^T, I reproduced the generalized polynomials, ordinary characteristic polynomials (including the cyclic one), Sylvester minors and the radical identity; replay: python /workspace/branches/independent_frozen_checks.py 1. Evaluating 4u A−G_c^T A G_c with u=t² gives all positive leading minors on 0<u<1/4, so the cyclic largest generalized root is below 4u. The signed cyclic polynomial at the largest interlaced root is positive: P>0, Q<0 and P²−u(u+2)Q²=(1−4u)². Its negative leading term then guarantees a larger cyclic root. The ordinary polynomials give spectral radius 4u for both tied orbits and a real cyclic eigenvalue above 4u. The penalty ratio and small-t limit follow from the exact factors. The claim is worst-case squared energy of one scalar sweep, not error-by-error dominance, optimal parallel runtime, or a multi-sweep comparison.

## originality

PASS

The supported distinction is the exact strict all-order hierarchy of one-sweep squared A-energy factors, including the splitting of orders tied by spectral radius. The asymptotic comparison by itself is covered by Varga's consistent-order result and is not credited as independently original.

## value

PASS

The screened cycle gives a concrete separation between asymptotic and one-sweep order selection. In particular the familiar red–black sweep is tied for asymptotically best yet is worst for the one-sweep energy criterion, and its penalty relative to the optimal interlaced order tends to a factor of two. The strict all-parameter classification resolves the finite-sweep choice for this natural model without extrapolating to larger grids.

The dated certificate retains the supplied scientific assessment, sources and limitations.
