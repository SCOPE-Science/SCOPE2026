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

A start with equal first and last bit is immediately bordered; the remaining cuts are at bit transitions. The proof's prose says a 1 before a zero run, where it should say a 1 after a zero run; the actual strict tests examine the correct transition cuts. For the 1-start 1 0^a 1 0^b 1 0^c 1 0^d the final 1 0^d is a border iff a>=d; otherwise only the two-one suffix can match, iff a=c and b>=d. Reversal gives the companion zero-start test. In summing cyclically, the strict baseline counts unequal neighbors; one repeated opposite gap strictly below both others removes two cuts, with two more removals when the larger gaps are also equal. This gives exactly the stated weak-order law, including periodic words. A separate exact replay summed all 75 ordered weak orders (class counts 3,16,24,32), reproduced each numerator and compared the series with direct tests of all rotations of all 20,349 indexed words of lengths 4–20. Marking a 1 accounts for the n/4 factor without a freeness assumption. The double pole or lower order away from z=1 cannot affect the n^3 terms; at 1, D~24(1-z)^4 and P'_2(1)=-12, P'_3(1)=-48. The four witnesses and the exact periodic-word count are consistent with these identities.

## originality

PASS

Credit the general absence of a singleton primitive unbordered-conjugate class, the known characterization of the two-conjugate fiber and the prior cut-level ordinary/Abelian gap analysis. The distinct contribution supported here is the joint cyclic count law and exact four-class distribution at weight four, particularly the opposite-gap correction in the rotation count and the simultaneous rational series for the classes; neither the verified general characterization nor the available closest catalogue statement evaluates that profile.

## value

PASS

Four markers are the natural next sparse case where two opposite gaps can interact, whereas the three-marker rule uses only neighbors. The exact law detects this first nonlocal obstruction and separates the exceptional populations at every length; it gives concrete comparison data for extending rotation counts to higher weights, rather than just a bounded enumeration or maximum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
