---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The square of a partial injection with domain D and image E is empty precisely when D and E are disjoint, hence rank is at most floor(n/2). At n=4k+2 equality would partition [n] into equally many odd points in each set by parity preservation, although [n] has 2k+1 odd points. For n=4k and n=4k+2 even shifts of [1,2k] by 2k and 2k+2 respectively attain the stated ranks. For n=2m+1 shift [1,m] by m when m is even or m+1 otherwise. These shifts preserve parity and both fence directions, and restriction gives all smaller ranks. At n=4k and rank 2k the complementary D/E words have equal ordered lists of run lengths: two successive selected positions are consecutive on one side iff their matched positions are consecutive on the other, since all fence comparabilities are between consecutive integers, and parity preserves their orientation. Complementary runs alternate, so they occur in pairs of equal length, each pair with the same starting color. The entries matched within each run pair are offset by that run length, which must be even and is sufficient under the same criterion. The half-lengths are the positive parts of a composition of k. The two starting colors and 2^(k-1) compositions give exactly 2^k maps, as the increasing matching is unique.

## originality

FAIL

The distinct catalogue record SCOPE-a-mod-four-square-zero-rank-defect-in-parity-preserving-fence-in--11bfe7935353 states the same rank function on the same monoid, and gives the same paired-even-run classification and count at n=4k. Attainment of every lower rank follows immediately by restriction there as here. The distinct record also counts additional residue classes. This is exact mathematical coverage in the inspected catalogue; its later path date does not determine priority, direction of dependence, or separate discovery. The original published membership criterion supplies the ambient monoid but is not the basis of this coverage verdict.

## value

FAIL

The modular capacity and paired-run pattern are meaningful exact invariants of the natural monoid. As a distinct contribution this record adds none of those conclusions beyond the matching catalogue theorem, and it asserts no new boundary case, refined count or different structural method. A finite histogram recheck does not change that assessment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
