---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification of the affine triangle Lissajous sextic

The self-contained script `verify.py` uses exact SymPy algebra. Execute from a directory containing the script with `python verify.py`.

It checks the affine sextic relation in the free rank-four normalization algebra, the nonzero determinant of the powers of \(x\), all three nontrivial conductor-basis identities and the scalar conductor identity, polynomial and Jacobian vanishing on the six proposed lines, twelve designated pinch points, and the four-factor quartic tangent cone at the origin. The script completed with all assertions satisfied.

The infinite statements additionally require the proof in RESULT.md: smooth normality of the torus, finiteness and generic birationality, generic two-point fibers along the conductor components, and analytic local descriptions. The program alone does not certify those geometric arguments. It does not inspect any behavior at projective infinity, nor does it perform an independent audit.
