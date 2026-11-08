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

The standalone `verify.py` performs exact rational checks and independent finite subset-sum enumeration. It verifies the Hamming-weight gap formula, the binomial count of dyadic cylinders, and 140 missing integers. Run `python3 verify.py` from the extracted package directory.

The proof for all positive real parameters is the binary-prefix identity and the elementary disjoint-gap argument. The almost-everywhere statement additionally invokes the strong law of large numbers for fair binary digits; finite experiments do not establish that infinite statement. No independent audit has been performed.
