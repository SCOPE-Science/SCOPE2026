---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-19.md",
      "INDEPENDENT_AUDIT_2026-11-19.json"
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

With a,b,c,Dx,Dy>0, ab>c^2 and r>=0, SPD drift plus nonexpansive projection gives unique stationary law. Its generator gives (2a+r)u-2cz=2Dx, 2bv-2cz=2Dy, (a+b+r)z=c(u+v); determinant 2Delta>0 for all parameters. Independently solved these equations symbolically and verified u,v,z, J_cont=c(u-v)+(a-b)z=cP/Delta, J_lag=J_cont+rz=2cQ/Delta, where P is the stated concave quadratic and Q stated affine function. Their sign partitions, roots and strict boundary cases follow directly; the explicit positive finite-lag factor follows from 2x2 symmetric semigroup B and eta>0. A new independent SymPy script checks all these symbolic identities as algebra, not just finite numerical samples. The prior October 25 source independently yields identical covariance specialization. Assumptions omit reset jumps from continuous area and do not count winding; no observed correctness defect.

## originality

FAIL

Full earlier October 25 theorem already covers the continuous-path signed area rate and its unique reversal boundary as the negative of its conservative potential torque, for the same SPD two-temperature gyrator with theta=0 one-coordinate resetting. It also publishes the full covariance, especially z. From these old formulas the target lag rate is exactly J_lag=J_cont+r*z; simplifying is one affine numerator Q, and the every-lag formula is a standard 2x2 symmetric semigroup identity. Thus the claimed paired phase classification is a direct elementary consequence of a stronger prior result plus standard linear algebra, not an original independent mathematical theorem. The November 4 paper treats whole-state reset and is not the decisive source. Independently verified algebraic identity of prior and target formulas with SymPy.

## value

FAIL

Although comparing continuous-path area and sampled antisymmetric lag is a physically intelligible distinction, the exact continuous current/reversal is already the previous torque theorem with a sign change, and the residual lag threshold and positive-lag sign are immediate algebraic corollaries of the earlier published stationary covariance plus the standard 2x2 matrix exponential. The proposed theorem contains no independently motivated unknown exact invariant or substantial new structural lemma beyond these mechanically implied deductions. It is useful explanatory commentary but not an independently valuable new mathematical finding under the common C/O/V bar.

The dated certificate retains the supplied scientific assessment, sources and limitations.
