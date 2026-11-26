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

Reconstructed the Gaussian gain using C(s)=(1-q)s-(s-t)_+^2/(2h)+(s-t-h)_+^2/(2h), q=t+h/2. Split integration recovers V=(3-2h)/12-z and I=(5-5h^2+2h^3)/240+(h^2-2)z/12+z^2/3 for z=(q-1/2)^2. The derivative numerator for I/(M-z) increases strictly since H'=2(M-z)/3>0. Thus interior displacements cannot tie either maximizing endpoint; the two distinct reflected boundary starts correspond to the same far endpoint in z. Clearing the positive endpoint denominators gives the stated bracket h(35h-14h^2-20)-60η(1+2h-2h^2). This establishes all strict regimes including h=h_c with positive noise, as well as the three-way tie. Exact substitution gives 779/87600 and both printed rational gains. Read the frozen result and all supporting files, including verify.py (symbolic checks and direct-kernel quadratures, not executed). The replay for the mathematical result is the piecewise covariance, polynomial integration, and sign test above, not the finite sample of quadratures. No claim for h=0, h=1, other window profiles or adaptive sensors.

## originality

PASS

The inspected statements furnish the Gaussian criterion or solve point-sampling and scalar-moment problems; they do not give the placement phase diagram for this window sensor and trace loss. This is an evidence-qualified assessment, not a priority certificate.

## value

PASS

One fixed exposure and integrated recovery error are natural restrictions. The theorem excludes continuously departing asymmetric optimizers and distinguishes a genuine jump and exact three-way tie from an intuition based on reflection symmetry. The guarantee is structural across the full width/noise domain; small absolute gain in some regimes does not establish practical superiority.

The dated certificate retains the supplied scientific assessment, sources and limitations.
