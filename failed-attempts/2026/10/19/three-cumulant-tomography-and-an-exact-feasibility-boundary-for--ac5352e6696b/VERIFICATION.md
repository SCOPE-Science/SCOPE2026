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

The stable backward solution splits into an independent OU Gaussian of variance w and an active part aY. Independently of the beta formula, the active state generator for (Y,S) has drift k(S−Y) and flips at rate γ. Applying stationarity to Y^{n+1} and Y^n S gives E[Y^{n+1}]=E[Y^n S]=n E[Y^{n−1}]/(n+b−1); symmetry zeros the odd moments. This yields the stated second, fourth and sixth cumulants by the ordinary moment identities and Gaussian additivity. The log derivative of the scale-free ratio is −b/[2(b+2)(b+4)], with limits 4√2 at b↓1 and zero at infinity. The quadratic in b+4 has the stated unique b>1 branch. Once b is fixed, K4 fixes the positive propulsion length a and K2 fixes w, so w>0 is exactly the remaining physical feasibility restriction. More explicitly, for a feasible fixed pair (K2,K4), the full two-cumulant fiber allows 1<b<6K2²/(−K4)−2, proving nonuniqueness. Multiplying the four original coefficients by the same positive number changes only the time unit. The description of v/k and D/k as dimensionless is a units slip: they have units of length and length squared, respectively, and this does not affect any formula.

## originality

FAIL

The distinct indexed record bf3fb81030e1 covers the same three-cumulant identifiability, exact image, reconstruction and lower-order non-identifiability and also admits zero thermal diffusivity as a boundary extension. Its Finding was inspected directly, not inferred from a title. Its displayed catalogue date is later than the frozen record's displayed date; this is a finding of equivalent catalogue coverage, not evidence that the matching record was first, nor a claim about authorship or chronology. Earlier primary papers establish the forward law and moments, not by themselves priority for the inverse theorem.

## value

FAIL

The idealized inverse problem itself is useful: the sixth cumulant separates thermal variance from active persistence and scale and gives a population model-membership check. But the frozen record supplies no independently useful new consequence beyond the matched inverse, its strict boundary and its two-cumulant obstruction. Choice of time unit and switching from a squared ratio to its positive square root add no substantive invariant; the forward moment calculation is already documented. No surviving valuable distinct repair was established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
