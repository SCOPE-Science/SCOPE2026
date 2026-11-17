---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-14.md",
      "INDEPENDENT_AUDIT_2026-11-14.json"
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

The cyclic de Bruijn closed-walk test recognizes exactly same-period outputs, including rings n=1,2. Boolean product relations form 735 reachable deterministic states (631 accepting), so a_n=uT^n e. Independently re-derived the 735-state closure, polynomial denominator degree 34, 39 initial coefficients, and all 735 recurrence tests at n=40..774 with exact integers. Cayley-Hamilton applied to the 735x735 T proves the annihilating scalar recurrence for ALL n>=40, hence the rational identity for every n; direct input/output enumeration n=1..12 independently agrees. The -2z^2/-5z^5 boundary corrections were checked. Saved source verifier’s claims were not substituted for the fresh proof/certificate reconstruction.

## originality

PASS

No located prior statement determines the exact one-step Rule-73 indexed-ring image series at all lengths. The de Bruijn relation technique, elementary CA symmetry, and finite Gardens-of-Eden data are prior art. No priority claim is made for those ingredients. Resultary prior Rule 30/54/110/18/232 enumeration applies to different local Boolean rules, not Rule 73 or its Rule 109 color conjugate.

## value

PASS

The exact full-length image-size sequence is a natural information-loss invariant for a dynamically studied ECA; the rational series and finite-order recurrence replace isolated census tables by a repeatable all-n count and permit exact growth analysis. This is a nontrivial 735-state finite automaton certificate and not merely relabeling a known series; no downstream universality claim is needed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
