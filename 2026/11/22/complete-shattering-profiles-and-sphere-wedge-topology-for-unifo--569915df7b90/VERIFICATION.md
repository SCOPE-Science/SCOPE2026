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
# Reproduction and limits

Run `python3 verify.py` from this standalone package with the standard Python 3 library. Expected final marker: `FIXED_WEIGHT_PATH_SHATTERING_PASS`. The checker independently enumerates the full concept class of exact-k stable sets and all possible supports for n up to 16; verifies the minmax trace-completion identity for all independent supports through n=13; and checks reduced homology over two finite fields through n=11. Recorded output is in `verification_output.txt`.

A finite computation cannot establish shellability for all n or rule out integral torsion. That unrestricted conclusion follows from vertex-decomposable independence complexes of chordal paths, skeleton preservation under nonpure shelling, and purity of the present rank truncation, all explicitly used in `RESULT.md`. The algebraic proof is independent of the checker.

No independent external mathematical audit has been performed.
