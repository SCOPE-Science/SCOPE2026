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

`verify.py` is a standalone Python standard-library checker. It reconstructs all independent faces, flags of nonempty faces, their exact orbit-cell incidence relation, and the lexicographically indexed quotient cells. It reads `collapse_pairs.csv`, replays each of 2,768 specified elementary collapses, and requires the lower face to have a unique remaining coface and the upper cell to be maximal. It checks the dimension-two remainder, connected 1-skeleton, and Euler characteristic. Observed output is embedded in `verification_output.txt` and ends `ALL_VERIFY_OK`.

The computation establishes the finite cellular collapse for the specified graph only. The published nonequivariant homotopy theorem and Armstrong's fundamental-group theorem are mathematical proof premises, not claims of computational certification. The Whitehead step is ordinary algebraic topology. No independent mathematical audit has occurred.
