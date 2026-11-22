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

# Verification scope

The file `verify_rung_fault.py` is executable using standard Python 3 only. Run `python verify_rung_fault.py` in a directory containing that script. A successful run prints `PASS: 44 graph-edge-deletion cases n=2..9, exact cone intersection, mod-two Betti profiles`.

The verifier independently constructs all graph perfect matchings by choosing unmatched vertices and incident edges, enumerates their simplicial faces, and checks the exact two-cone intersection for every interior rung and every ladder of length two through nine. It separately reduces binary simplicial boundaries to verify the predicted reduced Betti profiles. The proof in `RESULT.md` covers arbitrary ladder length by a graph-cut parity argument and an exact two-cone gluing theorem. The finite test does not prove the all-order theorem, and no integral boundary computation is needed for the homotopy-based integral conclusion.

External independent audit has not been performed.
