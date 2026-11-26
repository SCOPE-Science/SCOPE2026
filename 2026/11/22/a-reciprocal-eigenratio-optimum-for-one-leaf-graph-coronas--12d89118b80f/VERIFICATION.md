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

Averaging uses the minimum Rayleigh quotient on the mean-zero complement and the largest Rayleigh quotient to improve the ratio in the asserted directions, preserving the priced equality. The leaf/core block gives determinant a^2 z and trace a(z+2), hence f_-(sx) and f_+(ell x) give the two relevant eigenvalues after division by a. The strictly increasing elasticity of F=f_+ and F(4/z)=2F(z)/z give one stationary point x=2/sqrt(s ell) and a strict global minimum; the budget fixes scale and substitution gives the stated minimum. For a cyclic optimizer equality in both averaging bounds holds, since neither inequality can strictly improve the ratio at an optimum. The complex first Fourier mode, with corresponding leaf amplitudes, has constant squared edge differences on each orbit and thus the original Fiedler Rayleigh energy even under any other optimizer. Equality in the Rayleigh minimum makes it an eigenvector; the leaf equation fixes each leaf weight and the imaginary part of the core equation forces equality of consecutive rim weights, since sin(2 pi/n) is nonzero for n>=3. Independently, maximizing f_-(sx)/(1+x) for the unit-price gap gives y=f_-(sx) with s=y^2/(1-y)^2 using sx=y+y/(1-y); this gives the cited gap ratio. With Lambda=sqrt(ell/s), x=c x_* and c bounded away from zero and infinity, expansion gives R(x)=2 Lambda^2+Lambda(c+c^-1)+O(1). Thus c=1 gives the stated optimal expansion and c=2+O(1/n) gives the n/(2 pi) gap-allocation regret. Inspected RESULT.md, VERIFICATION.md and verify.py; the supplied finite tests were not run and are not needed for these conclusions.

## originality

PASS

The exact same-host priced spectral-gap solutions and the general eigenratio setup are prior. Same-day wheel eigenratio optimization is a different graph family. No inspected theorem covers the one-leaf-corona reciprocal optimizer and cyclic rigidity for the unconstrained positive Laplacian eigenratio.

## value

PASS

The exact unrestricted conditioning optimum compresses a many-edge allocation into the two spectral edges of the core, while proving cycle rigidity rather than presuming symmetry of all optima. Exact placement and the order-n gap-design penalty distinguish two plausible network objectives on a natural infinite family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
