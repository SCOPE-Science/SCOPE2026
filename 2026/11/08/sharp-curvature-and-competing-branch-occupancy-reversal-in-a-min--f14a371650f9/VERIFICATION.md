---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

Reset renewal gives leaf occupancy p/h,(1-p)/h with h=[(1+(r/k)(1-p))^nu-v]/(1-v). Differentiation gives d2y/dx2=-h'' h^3/(h-ph')^3, hence sign opposite nu-1. F_nu(z)=v+(1+z)^(nu-1)((nu-1)z-1) is strictly increasing for nu>1 and has one root; for shape two the maximum condition is r(r+a)>k^2 at lambda=sqrt(r(r+a))-k. Independent four-integer-shape phase-expansion CTMC solve for 12 parameter cases reproduces reset-Laplace occupancy to 1e-12. Reconstructed noninteger-gamma Laplace renewal algebra and derivative sign monotonicity; finite CTMC cases do not establish real nu.

## originality

PASS

Earlier Markov mutual-linearity and semi-Markov resetting work supply the general renewal transform; inspected relevant semi-Markov treatment does not classify this coupled gamma branch-rate perturbation by exact curvature sign or the one-peak threshold in a minimal three-state witness. Best-of-knowledge original specialized classification; specialized unindexed full coverage remains possible.

## value

PASS

Minimal three-visible-state memory effects produce a sharp curvature and paradoxical competing-branch occupation boundary, a motivated structural exception to Markov linearity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
