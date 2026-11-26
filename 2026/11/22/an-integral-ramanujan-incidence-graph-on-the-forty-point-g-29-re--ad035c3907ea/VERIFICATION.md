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

I confirmed the published geometric inputs and independently reconstructed exact block memberships by representing nonzero complex coordinates as exponents modulo 4 and zeros by absence from the support. There are 40 distinct points, 30 distinct four-point blocks, three blocks per point and 180 distinct unordered pairs from the blocks. This independently gives a simple 9-regular point graph and BBᵀ=3I+A. An exact Faddeev–LeVerrier calculation of the entire characteristic polynomial, followed by exact linear-factor division, gave roots and multiplicities (-3,15),(-1,4),(1,15),(5,5),(9,1), with no polynomial factor left. This independently checks the supplied annihilator-and-traces certificate by a different calculation. Multiplicity one of the degree eigenvalue gives connectedness; 5<2√8 gives the Ramanujan bound. A real Gram matrix and its rectangular factor have equal rank, and extending Q to R preserves rank, giving rank 25 and nullities 15 and 5. Replay: `python3 /workspace/g29_exact_reproduction.py`; the supplied script was read, not executed.

## originality

PASS

Credit the points, line system, incidence degrees and hence ordinary regularity and edge count to the existing geometry. The distinct supported claim is the complete integral point-collinearity spectrum, with its rank and Ramanujan consequences. The strongest checked sources supply geometry or spectra of different incidence systems, not this spectrum or an equivalent invariant for this graph.

## value

PASS

This is a natural point set from a specified reflection subgroup with all of the parent Klein lines retained, not an arbitrary forty-point slice. The full spectrum quantifies the expansion of its nine-regular graph and determines a substantial and exact incidence-nullity defect, neither of which is evident from the geometry’s degree counts. The precise invariant is useful for comparisons of these reflection configurations without requiring an application to Waldschmidt constants. The contribution is a bounded exact invariant, not a new general construction of expanders.

The dated certificate retains the supplied scientific assessment, sources and limitations.
