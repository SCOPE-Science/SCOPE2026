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

The reproducible code is `verify.py` and requires Python 3.8+ with no nonstandard dependencies. Run `python verify.py` in a directory containing that file. It completes with `VERIFY_OK` after exact cyclotomic-divisibility calculations and independent full-subset enumeration for every graph order \(7\le n\le18\). The finite test checks the entire vector of \((a,b)\)-regular-set multiplicities at each tested order, not only the total number.

The infinite classification rests on the exact integral-polynomial divisibility table, spectral support, the binary additive-separability lemma, and the explicit residue-class checks. The verifier does not enumerate arbitrarily large graph orders and provides no independent mathematical certification. For one relevant historical source, only an abstract and indirect quoted theorem were accessible, so a complete historical priority assessment remains open.
