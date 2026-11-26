---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The three partial derivatives cannot vanish together at a projective point, so the plane quartic is geometrically smooth and integral of genus 3. Independently reproduced the extension counts with `python3 /workspace/review_evidence/quartic_replay.py`, rather than executing verify_curve.py. The replay uses F9 with eta^2=−1 and builds its quadratic and cubic extensions by rootless monic polynomials. For a nonzero right-hand side a, cyclicity of the multiplicative group gives four roots precisely when a^((9^m−1)/4)=1; the zero value contributes one root. Across m=1,2,3 the affine counts are 1,105,892 and the [x:1:0] chart contributes 0,4,0; [1:0:0] is excluded. The Frobenius power sums are 9,−27,−162, hence initial coefficients −9,54,−189; reciprocity gives 486,−729,729. Multiplication yields the stated cube, with L(1)=7^3=343. The named elliptic curve has seven F3-points, trace −3, and trace 3 after the quadratic base change. The matching characteristic polynomials give the asserted finite-field isogeny, not an isomorphism of polarized Jacobians. The other root eta is a conjugate and gives the same counts.

## originality

FAIL

Two distinct indexed Resultary Findings give the exact general zeta numerator of this same family. The comparison does not depend on ordering within the date 2026-10-18: the distinct record catalogued 2026-10-13 already includes the model, with p=3, f=1, s=3, q=9 and eta outside F3. It gives the very same polynomial by substitution. L(1) and the unpolarized isogeny to the named elliptic cube follow deterministically from that polynomial. Neither a different verification route nor naming the elliptic representative establishes a distinct frozen result. This is a finding of equivalent coverage, not a claim about who first discovered it.

## value

FAIL

The one-point quartic is naturally motivated and its isogeny class is a useful invariant. For this frozen claim, however, both the polynomial and the isogeny are immediate specializations or standard deductions from exact family formulas. The independent point-count replay is useful corroboration but the submission does not establish a genuinely new arithmetic invariant or stronger decomposition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
