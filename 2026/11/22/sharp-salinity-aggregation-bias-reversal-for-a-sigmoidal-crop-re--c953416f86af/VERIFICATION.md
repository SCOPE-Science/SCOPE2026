---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

For nonconstant X in [a,b], a>0, fix common C50 and p and put t=(lambda/C50)^p, Z=X^p, v=(EX)^p. The bias has the sign of K(t)=E[(v-Z)(1+tv)/(1+tZ)]; K'(t)=E[(v-Z)^2/(1+tZ)^2]>0. This independently verifies strict single crossing. Its endpoint values are v-EZ and v(vE[1/Z]-1); strict power Jensen gives the three p-regimes at zero and the strict positive limit. Strict concavity/convexity up to/from the inflection endpoint bounds the positive root even when the endpoint is an atom. For two equal weights and p=3, I independently cleared the three positive denominators and obtained delta^2 t[t(6mu^4-3mu^2 delta^2+delta^4)-3mu]. In q=delta/mu the denominator 6-3q^2+q^4 decreases strictly from 6 to 4; both sharp limiting bounds are unattained. Replay: python3 /workspace/branches/independent_checks.py 5; it checks the symbolic identities and the numerical example, not the universal sign claims. The frozen checker is numerical, not a proof or an independent audit.

## originality

PASS

Best-knowledge pass for the model-specific synthesis and the exact cubic contrast-dependent switch. The Hill response itself and the general variation-diminishing mechanism are not distinct contributions. The latter, together with the two endpoint Jensen signs, already yields the qualitative crossover under the stated assumptions. Neither the closest available catalogue statements nor the accessible evidence for the primary literature supplies the symmetric cubic salinity threshold with its sharp contrast dependence. Priority is bounded by the access limitations below.

## value

PASS

For a common calibrated response, the comparison decides whether a mean-input prediction overestimates or underestimates spatial mean yield. The precise cubic threshold gives a usable contrast-dependent rule, not just the qualitative possibility of reversal, and the strict limiting bounds quantify how far spread can move the switch. This does not establish field effects for nonproportional scaling, variable crop response, unequal potential yield, or coupled salinity transport.

The dated certificate retains the supplied scientific assessment, sources and limitations.
