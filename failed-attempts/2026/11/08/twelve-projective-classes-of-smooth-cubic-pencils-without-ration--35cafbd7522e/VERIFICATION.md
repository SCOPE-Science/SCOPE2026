---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For characteristic-two cubic F, Euler identity gives F=XF_X+YF_Y+ZF_Z. Geometric smoothness equals absence of projective zero of three quadratic partials, equivalently rank 15 of their Macaulay degree-four multiplication map (a regular sequence). There are 336 smooth masks among 1023; binary pencil is a triple {a,b,a xor b}, enumerating all [10 choose 2]_2=174251 subspaces. Complete exact filtering yields 5544 all-smooth and 2016 rational-basepoint-free pencils. PGL3(F2) order 168 acts by exact polynomial substitutions, giving 12 free orbits. Every containing all-smooth net contributes exactly four outside coset representatives, producing extension counts 504,840,672. Seven rational points and lines yield the stated 672/1344 blocking split. The finite proof domain is complete, not an extrapolation from extension-field point sampling. The same 336/5544/2016/12/504/840/672 already occur in a verified earlier full census.

## originality

FAIL

The 2026-10-18 complete all-smooth cubic-pencil census already classifies all 5544 pencils into 37 PGL3(F2) orbits and records the full joint table by rational basepoint count b and smooth-net extension e. Its b=0 row contains *exactly* 2016 pencils, e=0,1,2 counts 504,840,672 and corresponding orbit counts 3,5,4 =12. This is a strictly broader exact classification that implies the core theorem. The 672/1344 blocking split may be an additional refinement but it does not independently salvage the original principal claim without a complete substantively narrowed/republished proof and re-audit.

## value

PASS

Finite geometry of projective classes, smooth cubic pencils and extendability to nets is intrinsically motivated and complete; original classification is valuable as mathematical knowledge but the core exact table has already appeared.

The dated certificate retains the supplied scientific assessment, sources and limitations.
