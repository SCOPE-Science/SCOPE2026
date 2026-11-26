---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Rebuilt the spin-flip quotient by enumerating each of the 16 configurations per bath and checking agreement of total rates to each target orbit within each source orbit. The multiplicities are 2, 8, 4, 2 and the summed C equation is 2B-4C=0. Independently solved the normalized joint quotient using exact polynomial-domain elimination (multiply by u=e^(2 beta) to clear denominators, replace one row with normalization); both B and the mean-energy rational forms agree. Clearing D^2 gives exactly 4(gamma+2)(w^2-4)H for the defect, with all coefficients of D and H positive on the stated domain. As a replay point (u,gamma)=(2,1) gives (A,B,C,F)=(1828,3334,1667,514)/7343. The two Gibbs gap estimates differ by one quarter of log(1+Delta/B^2); the leading terms of H and D give Delta/B^2=2(w-2)/gamma+O(gamma^-2). The limiting averaged generator has up/down ratio 1/u at a +4 energy gap, hence inverse temperature beta/2. On C3, the total flux out of aligned configurations is strictly less than 3 A3 and the reverse flux is strictly greater than F3 because both cold-bath orbit masses are positive. Thus 3 A3>F3 and the positive per-state weight ratio defines the single Gibbs temperature. Applies only to simple cycles with the specified flip law and fixed beta for the expansion. The attached checker was inspected, not executed; the exact elimination above was independent.

## originality

PASS

Credit the global bath protocol, the exact four-cycle generator, and the mean-energy law to prior work. The distinct increment is the all-finite-rate strict obstruction for the full marginal, its sharp mismatch coefficient, and the triangle-versus-square boundary, not the existence of an effective fast-switching temperature or mean-energy nonmonotonicity.

## value

PASS

The first cycle with three energy levels supplies a minimal test of whether a single fitted temperature describes the whole stationary marginal. Persistent failure is not implied by nonequilibrium currents or nonmonotonic mean energy. The exact sign and 1/gamma discrepancy quantify both the failure and its approach to an equilibrium-looking limit in an appropriate benchmark. No infinite-volume non-Gibbs claim is warranted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
