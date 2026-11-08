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

# Reproducibility and limits

The accompanying standard-library Python program `VERIFY.py` enumerates every indexed binary word of weight three for lengths \(3\) through \(21\). It computes the sets of all nonempty contiguous-factor Parikh vectors by direct substring scanning and groups them by exact set equality, independently of the claimed threshold formulas. The program checks class sizes, the four-gap criterion, and exact enumeration versus the restricted-partition formula, then checks the nonnegative-parameter bijection for all lengths through \(100\).

Execute `python VERIFY.py` in the extracted file directory. Observed output: `VERIFY_OK words=7315 lengths=3..21 transform=3..100`.

The check requires only Python 3 and its standard library. The proof of the unbounded length and asymptotic statements is mathematical, in `RESULT.md`; no finite search is asserted to be an infinite certificate. Exhaustive ranges, absence of independent audit, and the distinction between equal Parikh sets and equal Parikh multisets are explicitly retained.
