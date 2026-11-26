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

Exact line search makes consecutive residuals orthogonal. In dimension two their normalized directions give an orthonormal basis; writing A in this basis as [s t; t q], the reciprocals of the first two steps are s and q. Cayley–Hamilton gives r2 = rho b, with rho = t²/(sq) in [0,1). Scale invariance then gives even iterates (1−rho^m)A⁻¹b and odd iterates equal to these plus alpha0 rho^m b, all nonnegative. A zero residual terminates (including b=0); dimension one terminates in at most one step. For the witness the leading minors are 2, 2 and 12 and the off-diagonal graph is connected. The first line search gives 2/5. With r1=(3,14,−9)/5, Ar1=(−22,45,−77)/5, hence alpha1=286/1257 and x2,3=−4/419. Multiplication by A confirms the displayed strictly positive solution. The first step cannot lose sign in any dimension. Reviewed RESULT.md, VERIFICATION.md, verify.py and its recorded CHECK_OUTPUT.txt; the judgments above follow from the proof and exact arithmetic, not the recorded success line or a new run.

## originality

FAIL

An earlier, distinct Resultary result expressly states the full all-iterate theorem in dimensions at most two, proves the same two-step residual cycle under broader hypotheses, and gives the same dimension-three/step-two sharp boundary. The irreducible existence refinement follows by continuity from its strict diagonal counterexample; only the particular rational witness differs.

## value

FAIL

The positivity boundary is intrinsically useful but already established. Replacing the strict diagonal counterexample with one explicit irreducible example adds no new mechanism or frontier, since irreducible counterexamples follow from the open sign inequalities by a routine perturbation. No separately motivated exact invariant of the displayed matrix is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
