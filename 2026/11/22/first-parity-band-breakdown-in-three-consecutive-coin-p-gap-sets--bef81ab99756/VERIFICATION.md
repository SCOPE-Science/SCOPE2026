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

The proof is symbolic and holds for every even least denomination \(a\ge6\). The shipped `verify.py` script independently builds coin-change coefficients and validates the four complete threshold-gap descriptions for all 98 even bases from 6 through 200, including 5,817,672 bounded comparisons, 40,376 three-layer count comparisons, and 7,608 separately enumerated triples.

Finite checks do not establish the infinite statement; the min-layer formula, monotonicity under adding a smallest coin, and the exact case evaluations in `RESULT.md` are the infinite proof. Checks beyond the four specified levels, odd least denominations, and unrestricted literature priority are not claimed.
