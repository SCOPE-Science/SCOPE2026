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

# Verification record

Running `python3 verify.py` on the delivered standalone source executes two distinct checks. The first enumerates the entire height-one Motzkin language for lengths zero through sixteen, computes the nine ordered two-letter multiplicities and three one-letter multiplicities directly from each word, then compares the complete inverse-fiber dictionary with the explicit binomial enumeration; it also checks the known total number of source words. The second expands the rational singleton generating function using only integer power-series arithmetic and compares its coefficients with independently computed binomial fiber tests for every length through sixty-five. All assertions passed.

The proof in `RESULT.md` establishes infinitely many lengths combinatorially. The tests are finite, so they do not alone establish the theorem. The exact readout convention is oriented, overlapping, multiplicity-preserving and noncyclic. No independent audit has been performed.
