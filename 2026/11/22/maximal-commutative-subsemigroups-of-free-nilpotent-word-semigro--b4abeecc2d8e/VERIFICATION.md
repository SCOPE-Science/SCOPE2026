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

# Verification and reproducibility

The stand-alone Python 3 script `CHECKER.py` reconstructs every nonzero word on an \(a\)-letter alphabet through length \(N\), adjoining a distinct zero element. Its multiplication routine forms a concatenation exactly when the total length does not exceed \(N\), and returns zero otherwise. It computes every centralizer by direct multiplication. For the commutation graph on nonzero words, it enumerates *all* inclusion-maximal cliques using a Bron–Kerbosch search, reattaches the universal commuting zero, and checks exact equality to the proposed family list. It separately compares the direct ordered-pair census with the displayed gcd formula.

Run `python CHECKER.py`; the fixed test configurations are \((a,N)=(2,1),(2,2),(2,3),(2,4),(2,5),(3,1),(3,2),(3,3)\). Expected exact transcript is included in `CHECKER_OUTPUT.txt`. All eight checks passed, including an exhaustive maximal-clique search on the \(63\)-element \((2,5)\) case. No external packages, downloads, tables or binary data are required.

The proof in `RESULT.md` establishes the statements for arbitrary \(a\ge2,N\ge1\); the script verifies only the listed finite cases, not all dimensions. The historical source comparison establishes only the stated scoped literature distinction, not absolute priority. No independent scientific audit or external validation is represented by the verification files.
