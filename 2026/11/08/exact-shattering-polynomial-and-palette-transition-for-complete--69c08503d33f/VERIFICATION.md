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

## Reproducibility

Execute `python3 verify.py` (Python 3.10+; standard library only). The program generates the tested proper colourings directly and separately checks every coefficient of the stated three-colour polynomial on eight biclique sizes through a four-by-four graph. It computes exact complete-binary-tree ranks by recursion for fifteen small cases over four palette sizes and verifies full-vertex shattering witnesses when at least four colours are allowed. The output is included as `checker_output.txt`.

The independent mathematical argument in `RESULT.md` proves the unlimited parameter statement; the enumeration only checks finite instances. Correctness and originality assessments are same-model reviews, not independent mathematical certification. Historical-priority verification is nonexhaustive.
