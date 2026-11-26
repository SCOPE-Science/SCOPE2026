---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

On the total set of reproducing kernels, the products are exponential-affine weighted compositions with common slope v=a times conjugate(c). Independently, for T=e^(delta+beta z) C_(vz+w), TT* is the weighted composition with slope r=|v|², shift conjugate(gamma) and linear weight gamma=beta+v times conjugate(w), and constant e^(2 Re(delta)+|w|²). Conjugating the centered dilation D_r by the Weyl shift h=conjugate(gamma)/(1-r) multiplies that weighted composition's constant by e^(-|gamma|²/(1-r)). Thus the square roots of its eigenvalues give exactly the two claimed sequences on substitution, with a single nonzero singular value at v=0. Their scale difference is a Hermitian form with positive diagonals and determinant -|a-c|²; it is (1-|a|²)|b-d|² for a=c and is indefinite otherwise. Real rescaling in the two signs gives the entire positive ratio range. The frozen numerical checks are finite and were inspected, not rerun.

## originality

FAIL

A distinct Resultary record has materially equivalent coverage of the full paired singular sequences, norm ratios, and fixed-slope dichotomy. This is a coverage decision, not an assertion about which result was discovered or published first. The different displayed exponents and the explicit ratio-range wording do not leave a distinct surviving claim.

## value

FAIL

The quantitative comparison is a natural operator question, but the exact invariant and rigidity are already fully covered in the comparison corpus. The additional ratio-range wording is only homogeneity of the same displayed quadratic form; there is no remaining useful independent mathematical contribution within the frozen claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
