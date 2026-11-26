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

Positive edge weights reduce the sampled kernel to edge equations. Their signed cyclic recurrence has one free initial value exactly for an even cycle with equal products of fractions and complements; independent nodal values lift these traces. K plus the sampled penalty is positive definite because no nonzero constant is in the sampling kernel. Uniform boundedness and testing on the sampling kernel give convergence to the unique restricted stiffness solution. With resonance, a nonzero K-orthogonal complement to the zero-trace space gives a load annihilating the Dirichlet space but not that complement. For the unit-conductivity square, independently assembling in the tensor basis (1,1-2x,1-2y,f) gives diagonal stiffness (0,4,4,8/3) and load (0,0,0,1/9). Exact inversion gives the f coefficient as [eps^2 lambda^2+6 eps^2 lambda+2 lambda^2+8 lambda+8]/[6(3 eps^2 lambda^3+28 eps^2 lambda^2+60 eps^2 lambda+8 lambda^2+32 lambda+32)]. Dividing by lambda^2 gives 1/(24+9 tau) for every finite joint-limit sequence, including tau=0; the other three coefficients vanish. In the infinite-product regime the same quotient and transverse terms vanish (also det C=eps/4 and the simple defect yields sigma_min~|eps|/2 near zero). The integrated trace of f squared is 4/3 and reflection symmetry decouples f, giving the stated exact-integration coefficient. The own symbolic replay was /workspace/branches/independent-replays.py 2; frozen verify.py and recorded output claims were inspected, not executed. The numerical constant is for the assembled unit-conductivity, unit-weight square, not arbitrary stiffness or boundary weights.

## originality

PASS

The supported distinction is the exact all-load fixed-mesh result for independently sampled affine boundary traces together with the quantified one-node crossover of the square assembly, not generic penalty convergence, a cyclic linear recurrence in isolation, or the known possibility of underintegration-induced mechanisms.

## value

PASS

The all-load iff is a reusable, exact diagnostic: positive definiteness at every finite penalty does not guarantee enforcement of the intended trace at large penalty. The square profile distinguishes load responses below, on, and above a concrete scale rather than merely demonstrating a zero mode. The result neither claims a refinement estimate nor generalizes the single-element coefficient.

The dated certificate retains the supplied scientific assessment, sources and limitations.
