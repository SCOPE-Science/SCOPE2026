---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

Every proper cover must include 1 or 2 marked 1s; alignment of the first and last occurrence forces its length, yielding at most one cover of each kind. For p,d,e,c as defined, 1-one case iff p,c<min(d,e), max(d,e)≤p+c+1, and 2-one iff d=e, p,c<d. Counting these gap quadruples yields A(z),B(z), and C(z) as explicit rational sums; inclusion-exclusion yields F₂=C,F₁=A+B−2C,F₀=z³/(1−z)^4−A−B+C. Root-of-unity singularity comparison yields Pr(q>0)→1/90, Pr(q=2)~1/(12n). Independently enumerated every three-one word through length 16; all cover lengths/counts matched. Infinite case rests on gap bijections and rational-function argument.

## originality

PASS

General string cover algorithms and the cited morphism/right-infinite word theories do not logically determine the exact fixed-weight-three quasiperiod-count GFs. OEIS A320434 counts unrestricted quasiperiodic binary words; not a three-one filtered multiplicity spectrum. No strongly covering result appeared in actual targeted search; unindexed enumeration possible.

## value

PASS

Three markers are the smallest fixed-content family that supports two distinct proper quasiperiods. The theorem classifies every cover and counts the entire natural Hamming slice at every length, including a nontrivial positive limiting covered density.

The dated certificate retains the supplied scientific assessment, sources and limitations.
