---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

For four independent endpoint-uniform circular points, the first chord midpoint has normalized planar density f(x)=[π²|x|sqrt(1-|x|²)]^-1. Exchangeability converts M1-M2 to half a four-step random walk; Borwein–Straub–Wan–Zudilin Example 4 has p4(s)~(3/(2π²))s log(1/s), giving Pr(E_eps)~(3/π²)eps²log(1/eps). A direct (radius,angle,scaled-displacement) Jacobian gives joint mark densities divided by eps² L tending to π^-4 at center and (2π⁴)^-1 at rim, with other t outside (0,1) vanishing almost everywhere. The resulting normalized limit integrates to 2/3+1/3=1, hence Scheffé proves joint total variation, not just weak convergence. Independent analytic squared-density log bands at eps=1e-12 have coefficients ≈0.03870186 and 0.01935791, confirming the 2:1 factor. The prior four-step marginal is explicitly excluded from novelty.

## originality

PASS

The unmarked four-step random-walk small-ball probability is established prior art. The new conditional joint mark law distinguishes center versus boundary singular mechanisms and proves independent logarithmic depth, polar angle and scaled difference in total variation. The inspected same-object midpoint expectation and polygon midpoint laws, as well as circle-chord crossing results, involve different statistics; none gives the joint conditional distribution as a corollary on the compared materials.

## value

PASS

Two competing natural singularities of the midpoint distribution yield a non-obvious 2:1 collision split; the exact conditional shape and independent log-uniform radial depth answer a geometric rarity question not determined by the known marginal. The joint total-variation statement supplies precise conditional sampling geometry useful beyond the scalar logarithmic small-ball coefficient.

The dated certificate retains the supplied scientific assessment, sources and limitations.
