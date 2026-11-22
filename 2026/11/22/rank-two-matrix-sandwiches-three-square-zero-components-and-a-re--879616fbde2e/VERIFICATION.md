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

The block computation establishes \(XJX=0\) if and only if \(P^2=PQ=RP=RQ=0\). The argument uses an incidence vector bundle over \(\mathbf P^1\), proper projection to prove closedness, and the exhaustive rank-two dichotomy to identify all irreducible components. These general proofs do not rest on enumeration.

To reproduce the finite checks, run `python check_rank2.py` using Python 3 without third-party dependencies. Its output can be compared with `check-rank2-output.txt`. It directly multiplies the rectangular matrices over prime fields and an explicit polynomial-basis field of size four. It checks eight finite parameter triples and exact rank profiles and ends with `ALL RANK-TWO CHECKS PASSED`. A separate symbolic arithmetic comparison of the two equivalent closed forms was made for five field sizes and all excess dimensions through six; this is a consistency check, not an infinite proof.

There has been no independent mathematical audit. The reduced-geometric statements are not assertions about nilpotent thickenings of the defining scheme. The historical comparison is bounded by the inspected sources; in particular the full original 1981 varieties-of-complexes article was not materially available for inspection.
