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

For I≠S, 0 is excluded from S−I, which contains the entire conductor tail and only possible additional shifts z in [m,2m−h−1]. Intersecting S−z over those shifts excludes in the low band precisely the union of their full length-h windows [2m−h−z,2m−1−z]. Any subset of shifts together with the conductor tail gives a reflexive intersection by the antitone colon Galois relation; the tail forbids negatives and all such intersections contain the high band. The union characterization is equivalent to every omitted run having length at least h, including the empty complement. S is fixed separately. Once the high gaps have been included, the ideal contains every integer ≥m, so addition by positive S-elements cannot leave it. This is the reason ideal closure holds; the frozen sentence saying such sums are either in H or ≥2m misses sums in the middle band. The j zero-run lengths give weak compositions of r−jh, and the separating ones give binom(n−r+1,j); out-of-range counts are understood as zero. Alternating one- and zero-runs have series A=z/(1−z) and B=(uz)^h/(1−uz), and their word series is (1+A)(1+B)/(1−AB), yielding the asserted generating functions, extreme cases, and the extra contribution of S. An independently written translate-intersection and word-automaton check (python3 /workspace/reproductions/reflexive_ideals.py) reproduced the complete ideal sets in 45 parameter pairs through m=10 and all genus coefficients in 260 (n,h) pairs. These are finite checks supplementing the proof.

## originality

FAIL

The earlier Resultary record 62b4b8c42504 classifies exactly the same semigroups and all the same reflexive ideals for h≥3 by dual incidence windows. Transposing its displayed completion relation gives the frozen low-gap run rule directly. Its proof uses no h≥3 restriction in this passage, so h=1 and h=2 require no new argument; its relationship section also mentions earlier h=2 coverage without an identified source. The genus grading is not printed in the inspected earlier record, but is a routine marking of the occupied length in the mechanically equivalent run language. The frozen package has no established nonroutine originality beyond the earlier classification. This judgment does not rely on an unverified h=2 match or inaccessible literature.

## value

FAIL

The complete reflexive-ideal classification for these semigroups is a worthwhile structural object, but the previous window classification already supplies it. Rewriting the same incidence matrix in the opposite coordinate and weighting the lengths of already determined runs does not yield a separately motivated structural or genus-sensitive result beyond the routine enumeration. No nonroutine surviving component warrants a repaired acceptance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
