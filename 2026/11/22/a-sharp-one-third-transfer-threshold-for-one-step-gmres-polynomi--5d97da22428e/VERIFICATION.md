---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

For invertible T, change variables y=Tb to obtain the training step as a Rayleigh quotient of H=(T^{-1}+T^{-T})/2. The deployment quotient has the same range [m,M] and is independent of training. The exact squared-residual increment is alpha(alpha-2 beta)||Tc||²; extremizers give necessity of M≤2m since tr H=n, and this inequality also gives sufficiency, including equality. The finite Poisson-kernel bounds are strict because the support of a nonzero finite Fourier polynomial has positive measure. The constant and alternating Rayleigh quotients attain the two symbol bounds in the n→∞ limit, giving the sharp uniform cutoff 1/3 (strict reduction in each finite dimension at the uniform endpoint). Independently summing these trial quotients at n=25,t=2/5 gives H quotients 1.622222222227 and 0.722448979593, already witnessing M>2m. The n=2 endpoints are 1±t/2; for n=3 reflection splits off the antisymmetric eigenvalue 1-t²/2, and comparing it with the two symmetric eigenvalues gives the quartic test t⁴+8t²-2≤0 for 0≤t≤1. Principal-submatrix interlacing handles t>1. Checked the exact two-site ratio 45/34. Positive definiteness of the symmetric part of T for t<1 gives strict own-RHS improvement. Inspected verify_transfer.py and VERIFICATION.md without running the supplied code. The result is exact arithmetic for a single frozen scalar application, not a claim about repeated iteration or higher-degree polynomials.

## originality

PASS

The training-and-reuse procedure, general residual transfer estimates, and the Kac–Murdock–Szegő spectrum are established. The supported distinction is the exact all-training/all-deployment residual criterion and its sharp dimension-uniform threshold for this defective family. The strongest inspected overlaps do not cover it.

## value

PASS

Reusing a fitted approximate inverse across right-hand sides is an established procedure. This result separates guaranteed reuse safety from strict success on every training problem even for a basic triangular factor. The sharp uniform cutoff and larger exact finite-size cutoffs explain why low-dimensional checks can give a materially optimistic safety bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
