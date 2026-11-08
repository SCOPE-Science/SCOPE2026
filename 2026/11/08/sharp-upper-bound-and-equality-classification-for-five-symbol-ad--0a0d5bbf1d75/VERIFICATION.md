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

# Reproducibility

Run `python3 verify.py` in the directory containing this document, `RESULT.md`, and `verify.py`. The checker uses only standard-library Python 3. It verifies that its explicit ordered-triple systems have exactly one representation of every ordered pair of distinct letters; then it constructs all codewords and checks every possible deletion position, zero overlapping outputs and complete coverage of all received three-symbol words.

The five checked alphabet sizes are \(q=3,4,6,7,9\), and their code sizes are respectively \(15,32,96,147,297\). An additional independent enumeration covers all \(q^5\) length-five source words for each \(q=2,3,4,5,6\), checking the key rational shadow inequality by multiplying all weights by three. That phase covers \(12200\) source words. The final line of a successful run is `VERIFY_OK`.

The infinite-alphabet statement requires the exact shadow proof and the pre-existing directed-triple-system existence theorem, both described in `RESULT.md`; the finite program does not replace either. External independent auditing has not been performed. Historical priority is conditional on the inspected literature and remains subject to further expert checking.
