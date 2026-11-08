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

Run `python3 verify.py` from the directory containing `witnesses.json`. The program uses only the Python standard library, checks every deletion shadow, rebuilds the exact compatibility graph for all 129 guarded length-sixteen words, verifies both explicit codebooks, and performs an exhaustive colored maximum-clique search. The expected successful output is `EXACT_PROOF_OK n16_max=14 n17_code=16`, including a search node count of 33491.

An independent SciPy/HiGHS integer-programming model, with one linear inequality for each distinct length-fifteen deletion output, returned 14 as both optimum and dual bound at length sixteen; its floating-point status is not used as an exact mathematical certificate. The exact bitmask search is the authoritative finite upper bound. No claims about length-seventeen optimality or other source constraints are certified.
