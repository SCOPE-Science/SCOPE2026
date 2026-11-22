---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

In the exact Hardy H² norm, h(z)=product_(k>=1)(1-q^k z)^(-p) and its inverse are bounded analytic multipliers: h(z)=(1-qz)^(-p)h(qz). Hence T=M_h C_q M_h^(-1), with simple q^n eigenvalues and unit-normalized hz^n/sqrt(N). The extremal multiplier boundary moduli align at z=+1 and z=-1; analytic Fejér-polynomial concentration proves both sharp Riesz constants. Rank-one coefficient projection P_n has norm ||h||_2 (sum_(j<=n)|[z^j](1/h)|²)^(1/2), and Parseval yields its limit. Improper Riemann sums of -log(1-e^-x), log(1+e^-x) and a boundary arc of width epsilon² justify p*pi²/2 versus p*pi²/4 logarithmic growth rates. Critical endpoints 0<q<1 and p>1 retained; the zero spectral point is not misidentified as a nonzero eigenvalue. Finite independent Toeplitz-multiplier calculations at p=2.3,q=.42 found finite-section extreme singular values approaching the stated bounds, but are not a proof.

## originality

PASS

The exact unit-normalized eigenbasis condition and its individual rank-one spectral projection norms/asymptotic are evaluated for the specific atomic Bergman-kernel Cesàro weighted dilation; elementary similarity, multiplier norm identities and Hardy-product estimates are explicitly not asserted novel. No found primary source was shown to imply the complete quantitative statement. Best-of-knowledge priority with uninspected older weighted-composition literature.

## value

PASS

This is a motivated quantitative instability problem: compact positive-eigenvalue Hardy weighted dilations can have exponentially ill-conditioned normalized eigenvectors and spectral projectors at two distinct sharp rates. The exact products and spectral projector norms are useful to distinguish eigenvalue stability from eigenvector spectral instability, beyond a routine statement of similar diagonal operators.

The dated certificate retains the supplied scientific assessment, sources and limitations.
