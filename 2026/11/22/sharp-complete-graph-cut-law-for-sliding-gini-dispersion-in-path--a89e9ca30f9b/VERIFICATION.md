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

Work modulo constants and telescope along steps in x-y, whose jump magnitudes sum to V(x-y). For a step of height t at a cut, a crossing pair (a,b) counted outward from the cut contributes a single response of magnitude at most |t|, present for left occupancy a through m-b inclusive. Under variation sign duality each response is multiplied by the difference of signs at transitions a-1 and m-b. These pairs of transition indices run through exactly the edges of K_m. Thus the total is at most |t| times twice the maximum cut, divided by binom(m,2). An endpoint can only truncate the packet of window increments and cannot increase its variation; n=m gives zero output variation. At a cut after m sites, take x_i=i and add a unit step to get y. Both are strictly increasing, V(x-y)=1, and the full packet is ell(m-ell)/binom(m,2), rising from zero and returning to zero when n≥2m. This attains the bound; the parity simplifications follow directly. The argument proves an envelope for difference kernels, not sharpness for every kernel or for all shorter lengths. Frozen verification and checker inspected; computations are corroborative only and the uploaded script was not executed.

## originality

PASS

The all-width two-input coefficient and kernel envelope are distinct on the evidence checked. There is real m=3 overlap and a close variance proof analogue, but neither gives the general statement. This is not a finding of historical priority.

## value

PASS

The exact sensitivity in a standard seminorm for a natural nonlinear sliding statistic resolves a meaningful operator question. The transition-to-cut reduction explains the parity constant and supplies a nondifferentiable kernel envelope and finite attainment, beyond the known three-point coefficient and the variance analogue.

The dated certificate retains the supplied scientific assessment, sources and limitations.
