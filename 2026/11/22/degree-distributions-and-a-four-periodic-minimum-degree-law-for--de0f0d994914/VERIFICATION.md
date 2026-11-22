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

# Verification

The included `verify.py` requires Python 3 standard library only. Run `python3 verify.py` from the extracted package directory. The code separately constructs all legal words of lengths zero through seventeen, flips each coordinate and counts legal neighbors, and compares those degrees to the polynomial transfer calculation. For lengths one through eighty-four it also checks the Tribonacci vertex total, the exact minimum and maximum degrees, the unique minimum vertex multiplicity at positive multiples of four, and the maximum-degree population formula.

The finite calculations are consistency checks, not an exhaustive proof for unbounded length. The run decomposition, equality conditions, witness patterns, and exact five-coordinate transfer identity in RESULT.md are the all-length proof. The matrix representation determines all distributions without a dependency on external data.

The relevant 2020 publication is not available as full readable text in the source access attempted; historical priority for a more detailed degree spectrum remains a limitation. No external independent scientific audit has been performed.
