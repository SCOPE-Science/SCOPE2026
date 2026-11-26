---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproduction and scope

Run `python verify_multiplicity.py` with SymPy installed. On 2,592 rational parameter-frequency cases it evaluates the endpoint polynomial and its first two frequency derivatives by exact reduction modulo a cyclotomic polynomial. It checks zero membership, leading derivative formulas on every applicable branch, and the quadratic Taylor term at double zeros. The counts by order are 2,166 nonzeros, 402 simple zeros, and 24 double zeros. The finite grid also encounters cases exclusive to each of the three families. This is a finite exact check, not a substitute for the analytic argument for all real parameters.

Łaba's Lemma 3.1 gives the previously known zero locations. The local law follows by differentiating the endpoint expression at a zero and substituting the phase constraints in each family. At equal-length double overlaps the second derivative of the numerator is nonzero, which determines the leading quadratic amplitude and quartic intensity. The normalized slope bound is at exact real zeros for unequal-length intervals; it is not a uniform nonzero amplitude estimate away from zeros. The Wiener cyclicity statements are consequences of the known zero locations and the classical Tauberian criteria.
