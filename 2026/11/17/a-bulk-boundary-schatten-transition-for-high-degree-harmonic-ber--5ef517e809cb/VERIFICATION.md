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

Direct projection of normalized signed harmonic monomials gives a single frequency shift for T_(z^r). Comparing T_z T_(z^m) with T_(z^m) T_z leaves precisely the m input modes -m through -1, with coefficients beta*mu_m*(m+1-2q)/[(q+beta)(m-q+1+beta)*sqrt(mu_q*mu_(m-q+1))]. Distinct orthogonal inputs/outputs yield the full singular-value list, including a zero for odd m. Gamma-ratio bounds supply the bulk density beta*(1-2t)[t(1-t)]^(beta/2-1), the two summable endpoint sequences, and the harmonic logarithm exactly when p=2/(1-alpha). Fixed beta and p are essential. Independent direct coefficient calculations for beta=.5,1,3 and m<=11 corroborated this reduction; the proof's summation estimates, not the finite computations, establish all-degree limits.

## originality

PASS

The subject is a two-analytic-monomial finite-rank commutator with one growing degree, not an analytic/coanalytic mixed or self-commutator. Cui–Huang–Lu–Zu's 2026 structural classification gives square-zero finite rank but not beta-weight-dependent p-mass limits; Dong–Zhou's unweighted canonical decomposition gives part of the finite formula but does not state the three weighted m-asymptotics. The nearest published result on TWO simultaneously growing monomial degrees assumes a fixed nonzero degree ratio, which does not include the present ratio 1/m->0. Strong related literature reduces priority confidence, but no inspected prior statement entails this entire transition.

## value

PASS

The natural higher-degree magnitude of a finite-rank monomial Toeplitz commutator is not determined by rank. A sharp bulk-to-boundary threshold p_c=2/(1-alpha), explicit beta-integral bulk profile, logarithmic critical coefficient and edge summable limit answer an analytically motivated spectral concentration question across all radial beta weights. This is a sharp asymptotic classification rather than a trivial membership test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
