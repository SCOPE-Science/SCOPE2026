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

The stated rare-intensity theorem holds. With z=bt, Delta=lambda b^2/a and Q=2 Delta (E exp(zJ/b)-1-z E[J/b])/z^2, algebra gives c/b=sup (1-1/M)/z, where M=(1+Q)/(1+Delta E[(J/b)^2]); for z outside the candidate moment domain the objective is already bounded by 1/z. Laplace integration of the endpoint distribution gives E exp(zJ/b)~K exp(z)z^(-beta), with log derivative tending to 1 by tilted concentration. The trial z=L+(beta+3)log L gives objective (1-o(1))/L. For each fixed epsilon, the bounds Delta exp(z)/3 and 1/z exclude respectively z<=(1-epsilon)L and z>=(1+epsilon)L. This also supplies the missing justification of interior attainment for all sufficiently small intensities: the continuous extension at zero is only O(Delta), and the objective tends to zero at infinity. Thus every maximizing z is asymptotic to L and Q diverges there. Stationarity then gives Q/z->1, recovering the tilt expansion upon taking logs; the inverse objective is z+z/(M-1)=z+1+o(1). A fresh non-integer test with a mixture of an atom at zero and Beta(1,1/2), whose endpoint amplitude is 2/3, produced tilt errors 0.72807, 0.12234, 0.01705 and inverse-scale errors 0.77709, 0.12799, 0.01763 at L=60,600,6000, respectively. Numerical stationarity is corroboration only.

## originality

FAIL

A distinct published record has full mathematical overlap, including the every-maximizer asymptotic and the additive +1 for the sharp scale. The two formulas differ only by a variance/moment normalization. There is no supported distinct remainder in this claim. This is a finding of equivalent catalog coverage, not a finding that the 2026-11-08 record was first, independently derived, or the source of the frozen work.

## value

PASS

The mathematical question is substantive: a leading Bernstein scale does not distinguish endpoint behavior, whereas this sharp true-variance asymptotic recovers both the power exponent and amplitude and locates the optimizing tilt. The value is in that theorem, not in another rendering of the same theorem; the duplicate coverage independently prevents acceptance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
