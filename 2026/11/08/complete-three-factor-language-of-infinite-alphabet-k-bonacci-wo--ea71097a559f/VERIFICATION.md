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

The mathematical argument is in `RESULT.md`; `verify_triples.py` is a standalone standard-library Python 3 consistency checker. Run it with `python3 verify_triples.py` in the same directory. It independently builds iterates by the morphism and by their block concatenation, compares all length-three factor sets to the explicit parameterized formula through six independent values of \(k\), and checks the constant-case membership decision across every triple of a bounded numeric alphabet.

The recorded execution passed 88 finite-language comparisons, 2,512 cumulative distinct-factor instances, and 4,131 brute-force membership comparisons for \(k\in\{3,4,5,6,7,8\}\). The proof, not these finite experiments, establishes the infinite and unrestricted claims. Independent mathematical audit has not been performed; any historical-priority assessment is provisional.
