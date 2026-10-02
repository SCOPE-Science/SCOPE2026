---
{
  "schema_version": 1,
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-01.md",
      "INDEPENDENT_AUDIT_2026-10-01.json"
    ]
  },
  "lean_verification": {
    "status": "unknown",
    "evidence": null
  },
  "expert_attestation": {
    "status": "unknown",
    "evidence": null
  }
}
---

# Independent mathematical audit

## correctness

PASS

The block computation is exact: compressing [T_j*,T_j] to an invariant subspace gives [A_j*,A_j]-X_jX_j*, hence D_A=P_M D_T|_M+sum_j X_jX_j*. For a sum-normal ambient tuple this yields D_A=sum_j X_jX_j*, so a sum-normal restriction forces every X_j=0 and conversely reduction makes the restriction sum-normal. A finite-dimensional invariant subspace has positive D_A with trace zero and is therefore reducing. The bilateral-unitary/Hardy-space example is a standard explicit counterexample to blanket normal inheritance.

## originality

FAIL

The exact correction is mechanically implied by the same primary source. In the full text, equation (3.3) already gives [A*,A]=sum_j X_jX_j* for a sum-normal tuple, and Remark 3.1 explicitly states that a sum-hyponormal tuple whose invariant restriction is sum-normal must reduce the subspace. Since sum-normal implies sum-hyponormal and the converse direction under reduction is immediate, the advertised iff boundary is already a direct implication of the paper. The paper also states that every finite-dimensional sum-hyponormal tuple is normal, so together with Remark 3.1 it implies the finite-dimensional corollary. The new record usefully identifies the inconsistency with Remark 1.2(b), but under the required implication bar that is not an original mathematical theorem.

## value

PASS

Flagging a false blanket inheritance statement in a current operator-theory paper, giving a standard counterexample, and identifying the precise downstream auxiliary argument that uses the false assertion is scientifically useful. The value is diagnostic/corrective even though the replacement theorem is already implied by the paper's own later calculations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
