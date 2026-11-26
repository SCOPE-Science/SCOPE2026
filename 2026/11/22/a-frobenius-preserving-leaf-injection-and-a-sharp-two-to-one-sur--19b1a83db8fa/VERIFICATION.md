---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

This PASS is for repairs/2/RESULT.md, not the frozen table as written. The frozen use of F=4h-r swaps the residue-1 and residue-3 fibers: for example the frozen r=1 row at h=1 would give N4(3)=0, against the ordinary semigroup. The repair uses F=4(h-1)+r, excludes F=1,2, and corrects the even r=2 lower bound (N-3L=(k-1)^2+2, not always >=3). It also supplies the missing boundary reasoning for the leaf classification: among maximal w2=2w1 triples, c=2a-1 leaves an effective w3, and among maximal w2=2w3 triples, a=2c+1 leaves an effective w1. The four surviving families give all leaves, since every generator other than 4 is in the Apéry set. The coordinate shifts keep the maximum and break its only decomposition, preserve all closure inequalities, and have disjoint image branches by F modulo 4 (and b parity in residue 2). Counting the resulting intervals by maximal Apéry residue gives the repaired table. For r=1 and h>=8 the displayed square plus the outside point bounds N below by floor(h/2)^2+1 and the strict surplus follows separately at h=9 and in the other cases by the quadratic inequalities. The analogous square plus point for r=3 and h>=6 gives (floor(h/2)+1)^2+1>2h+1>=3L+1. The r=2 quadratic and the small tables give exactly F=3,5,7,9,10,11. An independent enumeration from Apéry residue closure and direct minimality, including deletion of 4 when effective, checked all 5093 leaves in the bounded range through F=299 and both counts, the injection, and exact equalities there. It is the interval argument, not the enumeration, that proves all F.

## originality

PASS

The repaired theorem claims the fixed-F injection and sharp uniform surplus/equality classification, not the Apéry inequalities, the four known leaf families, the fixed-genus injection, or priority over overlapping finite data. No prior all-F fixed-multiplicity-four theorem establishing these claims was identified in the inspected sources.

## value

PASS

A fixed-F correspondence solves a natural unbounded slice of the two-invariant conjecture without changing multiplicity, and the sharp quantitative surplus and exact small exceptions add structural information beyond existence of an injection or a finite table. The repaired index convention leaves those contributions intact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
