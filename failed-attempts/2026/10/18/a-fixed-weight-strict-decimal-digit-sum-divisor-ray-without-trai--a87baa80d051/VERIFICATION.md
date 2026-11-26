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

The decimal block certificate is exact. With a=448999=449000-1, the square is 201600102001 and its double is 403200204002. Their digit sums are 13 and 17, and s_10(a)=43. For B=10^k and k>=12, all of a, a^2 and 2a^2 are smaller than B. Thus aB+a has two noninterfering blocks and a^2 B^2+2a^2 B+a^2 has three, giving 86 and 43. The last digit is 9, and strict increase in k gives infinitely many distinct integers. This verifies the entire ray by exact arithmetic, not by extrapolating the finite frozen checker.

## originality

PASS

Pass only for the explicit seed and ray with weights (86,43), for which no exact or dominating prior statement was located. Do not credit as distinct the existence of some fixed unequal non-trailing-zero pair with quotient two: it is a direct specialization of the earlier Hare–Laishram–Stoll polynomial construction and the published noninterference identities, as shown in the implication check.

## value

FAIL

Holding both weights fixed without padding and keeping quotient two would be a motivated refinement of the OEIS question, but the earlier construction and its block identity already give that refinement directly. What is distinct here is a smaller, convenient seed and the explicit numerical pair (86,43). The original does not connect either of those numbers to a threshold, extremal weight, prescribed fiber, or other mathematical reason a researcher would need that exact pair. No new structural restriction or proof technique survives, so the exact witness alone does not justify acceptance or an ostensible repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
