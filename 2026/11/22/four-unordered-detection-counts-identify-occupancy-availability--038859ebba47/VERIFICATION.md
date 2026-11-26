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

For a subset of survey times with successive gaps g, the occupied latent moment is π times the product of π+(1−π)r^g. Independent detection and the occupancy mixture therefore multiply each subset moment by ψp^k. The gap multiplicities give the four binomial moments in the stated (t,r,z) coordinates. Independent symbolic differentiation gives ∂t log R>0 and det D(log R,log U)=−3t(1−r)²/[(1+t)BC]. At fixed r, R ranges from 4/9 to the strictly decreasing R∞(r); hence a fixed feasible R gives a single connected interval (0,r*) in r and exactly one t per r. Along that curve log U has derivative J/(∂t log R)<0, proving global, not just local, uniqueness. The endpoints for the outer monotone solve are the r→0 limit at finite t and the r→r* limit with t→∞. The positive-moment, shape and physical-parameter tests are sufficient since inverse substitution reproduces all four moments and their triangular transform determines the histogram. Transfer-matrix generating polynomials for the two stated three-survey tuples agree exactly. The constant-memory boundaries r=0 and r=1 indeed collapse different pairs of probabilities. Replay: python3 /workspace/branches/frozen_exact_checks.py 3.

## originality

PASS

The strongest count-only precedent gives an exact inverse when occupancy is fixed and known, rather than an unknown zero-inflation component. The general ordered-HMM and direct Markov-binomial passages do not supply a globally injective four-count compression for this model. On inspected evidence the additional unknown mixture, global two-shape inverse and sharp ambiguity distinguish the result.

## value

PASS

The four unknowns are distinct sources of observed zeroes and detection dependence, and the available statistic deliberately removes time order. The sharp design threshold quantifies the exact cost of that reduction in this model; the inverse and feasibility conditions diagnose which idealized count laws are compatible without needing sequence-level information.

The dated certificate retains the supplied scientific assessment, sources and limitations.
