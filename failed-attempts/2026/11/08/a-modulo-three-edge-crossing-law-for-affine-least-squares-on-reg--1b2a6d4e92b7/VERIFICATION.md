---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

PASS: Rotational symmetry yields covariance (2+cos h)I/6 and kernel 1+6 x·y/(2+cos h). Its absolute integral is convex in the evaluation position and strictly maximized at vertices. The first negative endpoint index ceil(n/3), wholly negative edge sum and two crossing-edge triangle areas give the exact norm. Three residue-class Taylor expansions give the claimed coefficients. Independently integrated piecewise-linear absolute kernel at n=3,4,5,6,10,30,100,301,1000 and compared direct values with the formula and cubic asymptotic; finite checks corroborate, not establish unbounded n.

## originality

FAIL

FAIL: A full October 26 earlier published RESULT.md treats the same normalized continuous arclength boundary, same affine projection, exact sharp vertex norm, the same circle limit and identical modulo-three n^-3 correction. Its displayed formula is algebraically equivalent by moving the negative endpoint contribution into the crossing-area term; the prior paper additionally proves the L1 norm. The original is covered in entirety.

## value

FAIL

FAIL as a new claim because the exact invariant and both correction orders are already known; correct rederivation of the same natural projector norm does not add a new motivated mathematical fact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
