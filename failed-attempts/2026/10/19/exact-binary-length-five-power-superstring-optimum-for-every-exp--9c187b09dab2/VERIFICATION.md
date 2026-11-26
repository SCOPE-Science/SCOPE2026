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

One occurrence per required equal-length word, sorted by start position, gives a lower bound by overlap costs; appending with those maximal overlaps attains that length for a given order. Within a rotation class the least positive shift d gives overlap 5p−d, irrespective of p≥2. Between different classes every overlap has length at most four, determined by the root boundaries. An order using B cross-class edges has length at least 5p+31+5(p−1)B, with B≥7; if B≥8 the lower bound 45p−9 exceeds 40p+2 throughout p≥3. An independent reproduction at p=3 built literal suffix/prefix costs and used a root-level remaining-set recurrence: from a current root, if any unvisited root in its class remains, the next root must be one of these; otherwise any remaining root is allowed. This recurrence enumerates exactly the grouped permutations and yielded minimum 122 over 61696 memoized states. The literal 122-bit witness contains all 32 cubes. A grouped route has length increment 40 per exponent because its seven cross-class edges and initial length each increase by five; thus both the all-exponent optimum and the restriction on all optimal orders follow.

## originality

FAIL

The distinct indexed exact square result implies the entire exponent-at-least-three optimum by an affine overlap-cost lift, even though it only states p=2. Independently, Au's existing overlap bound and attainable upper bound imply the necklace rigidity. This is demonstrable coverage against the available corpus, not an inference of historical priority from index dates.

## value

FAIL

This is a natural exact optimization problem, but its numerical constant and all-optima block restriction are already determined by the square comparison and elementary cost lift. Reproducing the same invariant by a cubic DP or giving a cubic witness does not leave a distinct exact fact or structural claim at the stated scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
