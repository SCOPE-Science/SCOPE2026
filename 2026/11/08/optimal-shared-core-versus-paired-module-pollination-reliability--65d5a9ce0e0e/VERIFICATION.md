---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification of the exact structural reliability theorem

Execute `python3 verify.py` next to this document. The checker uses only the Python standard library and terminates with `PASS 87 exact assertions` after three exhaustive topology enumerations.

It verifies all-neighborhood incidence and exact objective-gap identities for five pairs \((d,s)\), at five rational failure rates each. It independently enumerates all pollinator survival subsets to check the corresponding probabilities for each network with at most eight pollinators. Finally it enumerates \(114\), \(5{,}670\), and \(87{,}570\) admissible labeled neighborhood triples in the cases \((2,1,4)\), \((3,1,7)\), and \((4,2,8)\), checking the full set of optimizer overlap types at each of three rational probabilities using integer numerators.

The analytic proof in `RESULT.md` provides the unbounded quantifiers over all integers \(d\ge2s\ge2\) and all real failure probabilities \(q\in(0,1)\). The finite checker is a diagnostic cross-check, not an exhaustive proof for unbounded parameters. Model validity in a specific ecological system and independent historical-priority certification have not been established.
