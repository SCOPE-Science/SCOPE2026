---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

The printed predator and prey equilibrium equations entail x* increasing with tau and y*>0 iff x*<K. Independent substitution gives tau*=132.9233416526083 and y*(tau=250)=-409.07785. This is a correct parameter-specific positivity assertion, not a general global stability theorem.

## originality

FAIL

The very same Liu and Zhang 2024 article Proposition 3.1 publishes the exact general condition tau<1/s*log(alpha*Y*(1-exp(-beta*K))/s), whose printed numeric specialization is precisely the final theorem; moreover Section 4.1 already reports tau_3=132.9233. Both count as prior coverage by implication, notwithstanding that the source also prints an inconsistent tau<250 sentence. Failed Resultary retrieval does not undo decisive actual primary-source coverage.

## value

PASS

Clarifying contradictory interval statements is motivated: use of a negative predator population beyond the collision has substantive ecological interpretive consequences. This is valuable as a source correction despite the exact endpoint already being supplied by the source; this value does not rescue O failure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
