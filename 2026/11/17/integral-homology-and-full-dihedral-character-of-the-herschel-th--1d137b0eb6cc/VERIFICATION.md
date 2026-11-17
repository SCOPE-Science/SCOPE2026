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

# Finite mathematical verification

Run `python3 verify_herschel.py` with the attached source and Python 3 standard library. This reconstructs all 2047 subsets, the ordinary cut facets, all nonempty cut faces, the Alexander dual and its signed integer boundaries; seven mod-two boundary ranks are separately computed directly on the original complex. Exact integer unit-pivot elimination gives ranks 10,32,9 with zero residual and no nonunit Smith factors. The explicit eighteen-term integer dual two-cycle has zero boundary and a nonzero class modulo 3. All twelve automorphisms and their natural action are constructed; the six character rows agree with duality and with independent reduced Lefschetz traces on the original complex. Read `verification_output.txt` for actual observed values and `VERIFY_OK`.

The proof is exhaustive for the one finite graph. This is not a homotopy classification or an independent external audit. An unindexed prior equivalence remains possible.
