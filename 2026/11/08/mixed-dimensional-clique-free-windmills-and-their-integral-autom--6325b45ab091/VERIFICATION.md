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

# Reproducibility and independent-channel status

`verify_windmill.py` requires Python 3.10+ and only the standard library. In the directory containing the embedded files, run `python verify_windmill.py`; compare the stdout byte-for-byte with `verify_output.txt`.

The code constructs actual graph edges and forbidden t-cliques, enumerates faces and computes augmented boundary ranks over the field with two elements. It independently calculates fixed-oriented-face traces of graph automorphisms and compares those with both claimed homology characters. It tests all automorphisms on five graphs and samples additional cases, totaling 3,886 signed trace comparisons. The recorded final line is `ALL_VERIFY_OK cases=16 simplices=4861 character_tests=3886`.

These computations are finite checks only; they do not certify the theorem for all graph sizes, and field-two calculations do not prove integral torsion-freeness. The proof in `RESULT.md` supplies the integral argument. The mathematical review reported here is a self-review; no independent audit was carried out.
