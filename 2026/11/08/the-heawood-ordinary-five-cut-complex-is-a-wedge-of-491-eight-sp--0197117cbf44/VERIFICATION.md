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

# Reproducible checks

Run `python3 verify.py` with Python 3 standard library. The source and a real execution transcript are embedded as `verify.py` and `verification_output.txt`. No other files or remote access are necessary. The verifier constructs the Fano graph explicitly; enumerates all 2,002 five-sets; validates their connectivity by both graph search and edge counting; enumerates all 14,633 faces both by facet-closure and an independent complement predicate over all 16,384 subsets; checks the 28-cycle/missing-face correspondence; produces the deterministic 7,070-pair acyclic matching; exhaustively checks its full directed Hasse graph; and checks the Euler characteristic.

The exact observed output includes `FIVE_SETS connected=252`, `SIX_CYCLES 28`, `MORSE matched_pairs=7070 critical_0=1 critical_8=491 other=0`, `HASSE incidences= 96880 acyclic_nodes= 14632`, and the terminal `VERIFY_OK HEAWOOD_FIVE_CUT_TOP_SPHERE_WEDGE`. The complete canonical matching-pair SHA-256 is `72e2fe9bfdd9509f5054b3b4ee42ec66068b47683a83f64266110dc3b4710314`.

The finite computation is exhaustive for this precisely specified 14-vertex graph; it makes no infinite-family or mathematical novelty certification claims. Its Morse-theoretic deduction uses the standard discrete Morse homotopy theorem. An external independent audit has not been performed.
