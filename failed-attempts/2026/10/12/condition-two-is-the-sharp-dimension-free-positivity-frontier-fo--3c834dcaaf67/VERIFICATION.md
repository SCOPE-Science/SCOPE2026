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

With the usual convention of stopping or holding the solution when r=0, inactive coordinates stay zero and each active normalized residual starts at 1. The reciprocal Rayleigh quotient confines αλ_i to [0,2] for κ≤2, so those residuals remain in [−1,1]. In two dimensions the orthogonal residual directions alternate, with the printed two-step scalar γ obtained by substitution; the denominator minus numerator equals ac(u²+v²)². Even iterates are on [0,x*], and odd iterates on [x_1,x*]. Degenerate equal-eigenvalue and single-active-mode cases terminate in one step. For fixed κ>2, the limiting first residual of the equal lower-mode construction is nonzero, so both reciprocal steps are continuous at ε=0, with sum tending to 1+κ/2<κ. Therefore (x_2)_3<0 for small enough positive ε. Independent rational residual updates reproduced α_0=201/304, α_1=22713/39817 and (x_2)_3=−3353283/121043680 for the printed witness and also gave an exact negative coordinate for κ=2000001/1000000, ε=10^−12. Reviewed the frozen proof and verifier; the universal statement is analytic, not inferred from those replays.

## originality

FAIL

The frozen sharpness, second-iterate 3D minimal witness family and all-iterate two-dimensional safety are already covered by the October 4 steepest-descent result, which supplies the very same family and a stronger two-dimensional hypothesis. Its first/second-iterate guarantee also covers the initial part of the diagonal claim. It explicitly leaves later iterations in dimensions at least three unclassified; that later-iterate clause is the only candidate increment, not evidence that the full bundled result is distinct. Its variable-step diagonal contraction is a direct consequence of the standard scalar iteration, and there is no valuable narrowed remainder.

## value

FAIL

The independently motivated boundary and low-dimensional witness would be valuable if uncovered, but those are known for the same iteration. After removing them, the later-iteration addition for diagonal A is the elementary observation that a product of scalars in [−1,1] has modulus at most one. It holds for every sequence of steps from [0,2/L], without using exact minimization beyond its standard Rayleigh-quotient step bound. There is no additional structural ingredient or quantitative phenomenon to support a repaired finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
