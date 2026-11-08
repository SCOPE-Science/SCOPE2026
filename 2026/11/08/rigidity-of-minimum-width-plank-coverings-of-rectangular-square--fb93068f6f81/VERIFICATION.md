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

The complete mathematical proof is in RESULT.md. It derives the strict two-coordinate budget inequality and its equality-case consequence from Bang's sign lemma and the explicit two-variable estimate in the cited primary work. Boundary cases with coordinate normals are treated, and the passage from closed to open planks is justified by strict slack.

`verify.py` uses only exact `fractions.Fraction` arithmetic and checks the two-variable inequality, strictness for oblique normal vectors, and plank direction-budget identities. It also checks canonical interval-strip costs for a representative collection of holes. Execute `python verify.py`; a passing run prints a total number of assertions.

The verification program does not test all orientations, all intervals, or all dimensions; no finite test is an infinite proof. The numerical value of the optimum follows from earlier lower-bound machinery; the new scientific assertion is the rigidity and complete equality classification for \(h_1+h_2>1\). Independent mathematical auditing has not been performed.
