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

# Reproduction and scope

Execute `python3 verify.py` from a directory with `spectral_witnesses.json`; no third-party packages are required. The check dynamically reconstructs the relevant graph transitions and all reachable states instead of relying on a saved graph or an old output log. It then exhausts the product DFAs for both directions at one step and two steps, verifying equality and the two short non-inclusion witnesses. It independently enumerates all input blocks through length 11 and checks the complete sets of first forbidden words.

For each leading SCC it performs every strict integer Collatz–Wielandt comparison with the bundled positive vector. The Perron inequalities are exact; decimal entropy values shown in the written result are approximations only. The infinite-language and entropy conclusions additionally require the stated finite-state language and Perron–Frobenius arguments, respectively. Independent audit and independent mathematical validation have not occurred.
