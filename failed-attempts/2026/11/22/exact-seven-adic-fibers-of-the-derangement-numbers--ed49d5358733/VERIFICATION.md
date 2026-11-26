---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The signed interpolation F is the sum of integral falling-factorial polynomials; the j-th term and its derivative have uniform valuation bounds floor(j/7) and floor(j/7)-1. Passing the polynomial Taylor congruence to uniform limits gives F(x+h)-F(x)-hF'(x) in h^2 Z_7. Direct omitted-factor differentiation gives slopes (1,5,4,1,5,1,3); the signed base values are (1,0,1,5,2,5,6). Each disk is therefore bijective onto its output disk by successive unique digit lifts. Each input modulo 7^k has one even and one odd representative, giving the stated counts and the five-ball closure. The sign excludes a period dividing 7^k, and the isometry on the zero input disk excludes 2*7^(k-1) for k>=2 by comparison at n=0; modulo 7 the proper divisors 1, 2, 7 are excluded by comparing indices (0,1), (1,3), (0,7). Independent replay: python3 /workspace/branches/audit_arithmetic.py 2 verified the slope table and every target and cyclic least period through k=6, including period 235298 and image size 84035 at k=6. The lifting argument, not this finite check, proves the general statement.

## originality

FAIL

A distinct indexed Resultary finding explicitly contains the entire all-depth theorem for the same recurrence and index block, including each target multiplicity, least period, five-ball closure and measure. It also gives additional density/least-prime statements. The same-day date does not determine order or provenance; the failure is demonstrated equivalent coverage, not a claim of priority or copying. Separately, Miska explicitly supplies the least period and zero fiber, so these are not new components either.

## value

FAIL

A complete fiber law for classical derangements would be useful as a precise distribution invariant, but this frozen finding adds no new count, image, or period to the distinct indexed all-depth theorem, and its proof uses the same falling-factorial isometry mechanism with the same reduced tables. As a stand-alone additional finding it is recomputation of already covered facts; no valuable distinct remainder is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
