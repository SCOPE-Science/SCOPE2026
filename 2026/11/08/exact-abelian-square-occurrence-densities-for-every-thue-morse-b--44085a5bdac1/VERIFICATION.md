---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

The even/odd aligned-pair counting proves the exact pointwise occurrence conditions: even n=2r has every even start and odd start iff t(q)=t(q+r)=t(q+2r); odd n has no even starts and odd start iff t(q)!=t(q+n). Signed-correlation finite recursions B_j(2r)=B_(j-1)(r), B_j(2r+1)=-(B_(j-1)(r)+B_(j-1)(r+1))/2, plus dyadic-interval boundary O(h log M), rigorously produce the ordinary natural limits. Triple-sign identity then yields both formulas. Induction identifies eta=-1/3 exactly at powers of two and eta=+1/3 exactly at 3*2^k; adjacent-extreme arguments give odd extremizers n=9,11,13,15 and global extrema. New independent direct digit-parity comparisons verified 12,800 (n,start) pairs for n<=64 and start<200, with exact first 16 rational densities; these checks alone do not prove infinite claims.

## originality

PASS

Fici–Mignosi–Shallit 2017 gives a complete decision procedure for an indexed factor and counts distinct Abelian-square factor spellings, not natural density across starting positions at each fixed block length or the sharp all-period extremizer sets. Known signed Thue–Morse two-point autocorrelations are explicit prior tools. A straightforward automaton may yield an alternative algorithm for the count, but the closed uniform density/extremizer theorem is not explicitly implied by the inspected statements.

## value

PASS

Fixed-length density of Abelian-square *occurrences* is a natural frequency invariant, different from word-factor complexity. The theorem supplies a uniform exact all-block-length law, strict parity patterns, and completely characterizes the largest and smallest frequencies. These sharp infinite families are structurally informative and not an arbitrary finite census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
