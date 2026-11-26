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

Every pair of markers determines their relative order. For each core letter, its count before each marker gives a cumulative sum; taking differences and using the total two copies recovers every gap count, including the two end gaps. Those data determine all pair counts except the three oriented core counts, whose reverses sum with them to four. For each fixed marker order and chosen set of k occupied gaps, deletion of markers is a bijection to a core word and a split into k nonempty parts. The independent replay chooses duplicate positions and surjective monotone gap assignments, verifies the complete six-row fiber spectrum on all 2880 cases, and checks each row's source mass. Multiplication by r! times binomial(r+1,k) and summation proves all-r coverage, including r=0. After division by r! the sums and asserted closed forms are polynomials of degree at most six; equality at seven distinct arguments verifies their identities exactly. Source mass and division by (r+6)!/8 give the stated reconstruction probability and its leading 12/r^2 failure term.

## originality

PASS

The supported distinct contribution is the three-doubled-symbol all-marker multiplicity spectrum, not the marker-order reduction or the general idea of generating 2-binomial classes. The prior two-core exact formula and same-day ternary support result materially overlap but do not imply the stated populations.

## value

PASS

The first balanced doubled core with all three distinct pair coordinates interacting gives a natural test of how labeled singleton markers resolve ambiguity. The exact number of sixfold ambiguities and the sharp failure probability for increasing marker count distinguish this from an isolated finite census or a restatement of the two-core result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
