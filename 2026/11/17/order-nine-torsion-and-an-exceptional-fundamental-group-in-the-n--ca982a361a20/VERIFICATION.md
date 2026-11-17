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

The ordinary proof consists of the equivariant GKZ realization and the precise Mayer–Vietoris/Wang calculations given in RESULT.md. A standalone finite-check script `nonagon_verifier.py` uses only the Python standard library, enumerates all faces of the nine-gon noncrossing-diagonal complex, checks rotational orbits and character isotropy, and prints `VERIFY_OK`. Execute with `python3 nonagon_verifier.py`. The actual recorded run output is embedded as `nonagon_check.txt`.

Finite enumeration is not an integral-homology computation; it is a separate combinatorial cross-check. The H3 group order is proved by the exact-sequence argument; its cyclic-versus-split extension is not verified or claimed. No independent audit has been performed.
