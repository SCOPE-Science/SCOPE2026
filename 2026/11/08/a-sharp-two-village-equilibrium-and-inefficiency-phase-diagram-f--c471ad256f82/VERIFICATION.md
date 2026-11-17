---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

Reconstructed strict Nash deviation comparisons. Adding inequalities for two same-village clients assigned to different sites yields C/k+C/l<=C/(k+1)+C/(l+1), impossible. The only equilibrium profiles are the two poolings (r<=1-1/(2m)) and home segregation (r>=1/[m(m+1)]); crossing fails strict comparison. Welfare OPT=min(C+md,2C), giving exact attained worst-PNE envelope 4/3 (m=1), 3/2 (m=2), (2m+1)/4 (m>=3). Independently enumerated 33 rational (m,d,C) regimes with all labeled profiles for m<=5; these checks support but do not prove arbitrary m.

## originality

PASS

PASS: Ma et al. study the same equal-share facility-assignment game and provide a potential-derived PNE and a distinct-location noncrossing lemma, but do not classify all pure equilibria for colocated populations nor their sharp worst-equilibrium price of anarchy. General PoA/PoS facility literature does not imply the two threshold faces. The special symmetric subclass is original to current best of knowledge, not a priority certificate.

## value

PASS

PASS: The sharp coexistence interval and attained worst-PNE PoA growing linearly with population size isolate a natural inefficiency boundary in a standard fixed-facility game. This all-PNE result is different from a guarantee for one computed equilibrium.

The dated certificate retains the supplied scientific assessment, sources and limitations.
