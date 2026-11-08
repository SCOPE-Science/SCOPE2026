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

# Exact certificate reproduction

Run `python3 verify.py` with `certificate.json` and `example_code.txt` in the same directory. Only the Python standard library is required. The verifier regenerates the 640 GC-restricted words, 320 reverse-complement pairs, 260 eligible candidate pairs and 4948 conflicting pair-pairs. It validates all graph cliques and four complete branch cases using exact rational arithmetic, including every residual-vertex coverage inequality and all four upper bounds smaller than 23. It separately validates all 44 witness words and 166 distinct observed deletion outputs.

The expected success marker is `EXACT_CERTIFICATE_OK candidates=260 conflicts=4948 pairs=22 words=44 deletion_outputs=166 leaves=4`. These exact checks prove the length-five finite claim. The calculation does not prove an unbounded-length statement or independently establish historical priority.
