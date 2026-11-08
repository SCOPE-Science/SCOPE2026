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

# Reproduction and checks

The standalone `check.py` requires only Python 3 and its standard library; run `python check.py` in the same directory as the extracted package files. It reconstructs the original nonunital algebra on word bases of lengths one and two; for every tested candidate, it verifies composition-square-zero on the full operator matrix and checks images of products of generator pairs. It also performs independent finite-field row reduction of the \(S\)-constraint for all square-zero quotient maps of sizes two and three. Exact expected stdout is provided in `verification_output.txt`.

For \(m=2\), all square-zero algebra endomorphisms over \(\mathbb F_2\) and \(\mathbb F_3\) are enumerated directly (304 and 7209 total respectively). For \(m=3\), rank of the linear constraint on quadratic corrections is checked for all 22 square-zero quotient matrices over \(\mathbb F_2\) and all 105 over \(\mathbb F_3\). The latter checks do not enumerate all quadratic corrections, but verify the per-matrix kernel-dimension lemma exactly. No untested prime-power computations or infinite exhaustive enumeration are claimed. The arbitrary-field statement is proved in `RESULT.md` using module decompositions.

External independent audit and independent historical-priority validation have not been performed.
