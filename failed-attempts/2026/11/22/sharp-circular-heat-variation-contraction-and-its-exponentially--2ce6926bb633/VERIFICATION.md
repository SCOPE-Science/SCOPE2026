---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

A real circular BV derivative is a finite zero-mass signed measure; any antipodal atom difference has a semicircle step as its primitive. The Jordan product representation with the factor V/2 makes the BV quotient bounded by the maximum probability TV distance of two kernel translates, and two atoms attain it. The Jacobi product gives k_t'(u)<0 for 0<u<π, so for separation h the positive region of the density difference is the semicircle (h/2−π,h/2), with TV derivative k_t(h/2)−k_t(π−h/2)>0 for 0<h<π. At h=π this gives the semicircle mass formula and integrating the Fourier heat density gives the alternating odd series. Equality requires that almost every pair sampled independently from the two normalized Jordan parts is antipodal; hence both parts must be opposite singleton atoms. Strict time decrease follows by differentiating the semicircle integral to get 4k_t'(π/2); strict submultiplicativity follows because an attaining semicircle step becomes nonconstant and smooth after any positive time and so cannot attain the second quotient. Positivity and K<1 follow from strict radial decrease and strict kernel positivity. For a=π/2 the wrapped Gaussian differs from the unwrapped two-sided outside tail only on |u|≥3a, so 1−K(t)=4Φ(−a/√(2t))+O(exp(−9a²/(4t))). The first two Mills terms give the stated constants; the first two odd Fourier modes and the exponentially smaller tail give the large-time expansion. Replay: RESULT.md lines 33–71. VERIFICATION.md and verification/check_heat_bv.py were inspected, not run; their finite samples are not a universal certificate.

## originality

FAIL

The principal claimed coefficient is an established exact result under an equivalent formulation: Aldous–Fill §13.1 explicitly identifies the worst pair of circle Brownian transition laws as antipodal and gives their exact total-variation profile in (13.6). Differentiation identifies circular BV modulo constants isometrically with the real zero-mass measures, under which heat acts by precisely that transition kernel. The known Dobrushin formula then identifies the two norms, not just a bound. The earlier fractional-circle Lipschitz entry explicitly gives the same semicircle integral and odd series at α=1 and credits Aldous–Fill. The semicircle normer classification and strict submultiplicativity are direct consequences of the uniquely maximizing separation and smoothing, and an overlapping general radial-density derivation is explicit in the von Mises entry. The further terms retained in the two expansions are routine evaluations of the known profile. This is shown coverage and implication, not failure due to access or uncertainty about same-day priority.

## value

FAIL

The sharp heat TV profile is a useful quantity, but the frozen contribution is essentially its repackaging on the isometric BV quotient. The residual equality follows from unique antipodal separation, strict composition from smoothing, and the extra asymptotic terms are the next terms of standard expansions of the already known exact function. These are useful explanatory details, but no substantive new mathematical result remains in the frozen scope. No distinct valuable corrected claim is established here.

The dated certificate retains the supplied scientific assessment, sources and limitations.
