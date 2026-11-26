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

For traceless matrices polarizing X²=Q(X)I yields XY+YX=B(X,Y)I and ad_X²Y=4Q(X)Y−2B(X,Y)X. For X=0, nonzero isotropic X, and nonisotropic X the ranks are 0, 1, 2 with Y-fiber sizes q³, q², q respectively; the nonzero images are the line through X or X⊥ as asserted. For Z=0, W=0 necessarily; the total is q³+(q²−1)q²+(q³−q²)q=2q⁴−q². For nonzero nilpotent Z conjugate to E₁₂, X⊥Z means X is upper triangular, and [X,Z]=2aZ for diagonal a,−a. Nonzero isotropic X forcing Z lies on its line and gives W=0; each prescribed nonzero multiple fixes a and leaves q choices of the other coordinate. For Q(Z)≠0, ad_Z on Z⊥ squares to 4Q(Z) and therefore fixes the candidate X=−[Z,W]/(4Q(Z)) uniquely for W⊥Z. The determinant of 2ZW−B(Z,W)I gives Q([Z,W])=B(Z,W)²−4Q(Z)Q(W), proving the nonisotropy test. The equation a²+bc=s has q(q−1)+q times the number of square roots of s solutions, with the q(q−1) term added only once. For Q(Z) square, Z is diagonalizable and Z⊥ is the off-diagonal split plane; in the nonsquare case a nonzero isotropic vector in Z⊥ would make Z triangular after conjugation, which is impossible. These counts give the stated support and the conditional laws. All arguments use odd characteristic, labeled inputs, and no quotient by conjugacy for counting. The bundled verify_joint.py and verify_joint_output.txt were inspected, not rerun; the recorded support values for q=3,5,7,9 agree with the analytic count. VERIFICATION.md does not supply independent attestation or formal checking.

## originality

PASS

Pass is for the joint prescribed-pair distribution, not the already matched marginal table, the adjoint-square identity, or its fixed-X rank calculation. The strongest matching record even classifies all contributing X and their Y multiplicities for a given Z, but does not evaluate the images and multiplicities under X↦[X,Z]. That pushforward requires determining which W occur and how the admissible quadratically typed X map to them. The two nonzero Z cases use different arguments, with the nonisotropic case requiring an inverse and its quadratic behavior. The inspected results do not supply the joint refinement or a broader joint-fiber theorem implying it as a specialization.

## value

PASS

Consecutive evaluations share an input pair; their dependence is a natural question not answered by knowing individual depth marginals. The table gives exact admissibility and multiplicity for every target pair at every odd q, including an isotropic atom at W=0 and uniformity on a different quadratic support in the nonisotropic case. These data permit counting constrained simultaneous Engel equations without enumerating inputs. They are neither a single recomputed entry nor a new name for the one-depth table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
