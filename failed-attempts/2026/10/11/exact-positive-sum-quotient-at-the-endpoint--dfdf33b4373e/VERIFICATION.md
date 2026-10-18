---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

The endpoint unit constraint yields f(0)=1-m_f. Substitute f′=m_f+δ_f into ||f+g||=f(0)+g(0)+max(f′+g′) to obtain exactly 2+max(δ_f+δ_g). To prove the converse, test against all nonnegative continuous derivatives u<=1 and use continuous peaked u(x)=1: inf_{u(x)=1}max(δ+u)=1+δ(x), including points with δ=-1. Thus equal pairwise profiles imply δ_f=δ_h. Writing derivative δ+M and initial value 1-M gives precisely -min δ <=M<=1; any onto self-map of each interval preserves all pairs and is globally onto. Checked singleton fiber and δ=0 affine fiber. No finite enumeration is needed.

## originality

FAIL

A published full classification of the same endpoint norm-additive maps contains an exactly equivalent quotient Hf=1+δ_f and the entire interval-fiber description, and allows all the claimed surjective fiber actions. This is decisive positive coverage, not an unsuccessful search or mere matching title.

## value

FAIL

The precise quotient and all constant-shift fibers already appear as the initial steps of a stronger complete endpoint classification; the target contribution is just that known decomposition together with a subset of the already characterized maps. No separate mathematical gap or new invariant remains in the final claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
