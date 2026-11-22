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

# Verification of the finite-field line-pencil synthesis formula

The exact proof uses: (1) strict convexity of the fourth-power Fourier moment on the normalized affine support space, giving a unique minimizer; (2) scalar multiplicative invariance and an exact character-orthogonality reduction; (3) symmetry of the resulting moment under all permutations of selected direction coefficients; (4) a strictly convex real quartic and its explicit cubic-root minimizer; (5) separate boundary checks when there is one line or the entire plane.

The package includes `check_line_pencils.py`, a Python 3 standard-library checker. The executed checker passed 3,015 supplementary optimizer and random-complex-signal assertions on prime and extension fields of orders \(2,3,4,5,7,8,9,11\). It enumerates small-field projective choices and samples larger families, evaluating Fourier transforms directly. These finite checks validate arithmetic and normalizations but are not an exhaustive proof of an unbounded theorem.

The associated primary scientific texts were inspected in HTML, including Iosevich–Li–Yu's affine-transitive exact constant and Bhowmik–Deodhar–Iosevich's indicator estimate. Unindexed equivalent formulations are a remaining originality risk. No independent mathematical audit or validation has been carried out.
