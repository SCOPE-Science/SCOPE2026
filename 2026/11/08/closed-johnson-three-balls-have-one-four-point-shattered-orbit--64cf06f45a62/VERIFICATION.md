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

Reproduce the finite type certificate by running `python3 check.py` with Python 3 standard library. It constructs all four-triple isomorphism types by canonically introducing new ground symbols and reducing by exact incidence multisets under all query permutations, then checks all traces against the 455 three-subset centers on a fifteen-symbol universe. The output `check_output.txt` is a record of the actual run, not a substitute for the executable. Independent local-ball enumerations at ambient sizes 5 through 9 check low-parameter boundary values and sample exact fourth coefficients. The universal conclusion also uses the mathematical 12-plus-3 stabilization lemma, the five-support obstruction, and the structural counting argument; arbitrary finite-size experiments without those arguments would not prove the global theorem.

Scientific limitations: this is a complete statement only for four-point supports and the overall VC dimension of the specified Johnson-rank-three closed balls. Larger ranks, all lower-degree support counts, and online dimension are not asserted. Historical priority and independent expert validation remain unverified.
