---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

Green's identity for the boundary-normalized solution gives \(\Lambda'(E_0)=1/(c|\psi_0(v_0)|^2)\), consistent with the standard Weyl-function derivative identity. Substituting this nonzero slope into Turek-Cheon's exact \(P_\alpha(E)=[1+\alpha^4F(E)^2]^{-1}\), with \(F=\Lambda/(2k)\), yields the local Lorentzian under the \(\alpha^{-2}\) scaling. The inverse-function expansion gives the two half-height roots; subtracting the two inverse-series branches cancels even powers and gives the \(O(\alpha^{-6})\) FWHM remainder. A change of variables gives the peak-area limit. The frozen interval verifier was read and its exact formula \(4ck_0L^{-1}\arctan(2/\alpha^2)\) has exactly the predicted expansion.

## originality

FAIL

The scientific conclusion is a direct local corollary of two established prior ingredients: Turek-Cheon publish the exact transmission probability in terms of the Dirichlet-to-Neumann function, while standard boundary-triplet/Weyl theory gives \(M(\lambda)-M(\mu)^*=(\lambda-\bar\mu)\gamma(\mu)^*\gamma(\lambda)\), whose real derivative is the squared norm of the boundary-normalized solution. In this scalar graph normalization that is exactly the reciprocal local spectral weight. Taylor expansion, inverse-function expansion and one Lorentzian integral then mechanically produce the linewidth and area formulas. Under the audit rule that direct corollaries are covered even without matching wording, the absence of a printed FWHM formula in the source does not establish originality.

## value

FAIL

The local spectral-weight interpretation is useful exposition for the filter, but once the exact source scattering law and standard Weyl derivative identity are in hand, the Lorentzian profile, FWHM coefficient, area and \(\pi/2\) ratio are routine Taylor/inverse-function/integration consequences. The precise fact is therefore mechanically implied by established formulas rather than an independently substantive structural result under the common value bar.

The dated certificate retains the supplied scientific assessment, sources and limitations.
