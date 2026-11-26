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

In each feasible nonconstant output run, the first and last centers are forced one site in from the bounding sites of the run. Differences between successive centers can only be 2 or 3 (independence and no coverage holes); zero-runs decouple the choices. Thus the local count is the composition coefficient c_(L−3), with infeasible lengths 1,2,4 and unique lengths 3,5,6,7. The all-one count is Perrin: cyclic steps 2 or 3 give (2z²+3z³)/(1−z²−z³) for positive lengths; n=1 excludes one by self-adjacency and n=2 gives two predecessors by the repeated-neighbor rule. For nonconstant indexed outputs, choosing the start label of a list of k run pairs counts each actual word k times even when periodic, giving the logarithmic derivative of 1−AB. Adding the separately counted constant outputs yields both stated series. Renewal weights include lengths 4 and 5, enforcing a positive simple unique dominant root by the triangle inequality and coprimality; its simple pole in the logarithmic derivative has coefficient prefactor one. Independent exhaustive finite check of every output and allowed input for n=1–16 and both series passed; /workspace/branches/470b5e86-15db-4e21-b741-0bf9df05b45b/independent_rule254_check.py and independent_rule254_check.txt. Bisection gives ratio 0.978994288608, but complex-root dominance is analytic. The supplied script was inspected, not executed.

## originality

PASS

The scoped contribution is the nonconstant hard-core OR fiber factorization and the two aggregate indexed-ring counts; the local rule and the Perrin special case are prior. The inspected nearest works do not supply these statements or a direct implication covering them.

## value

PASS

The complete individual fiber classification explains which output patterns retain information. The two rational series distinguish reachable from uniquely invertible outputs and quantify exponential loss among indexed outputs, a stronger result than a yes/no losslessness test. The growth is combinatorial, not a noise-channel capacity guarantee.

The dated certificate retains the supplied scientific assessment, sources and limitations.
