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

# Verification and limitations
The symbolic proof in `RESULT.md` establishes the complete classification for all finite regular Rees zero-matrices; `CHECK.py` exercises finitely many independent examples. Run with Python 3 as `python3 CHECK.py`. The recorded actual run is `CHECK_OUTPUT.txt`, terminating with `VERIFY_OK`.

The checker constructs multiplication tables of \(M^0(G;I,\Lambda;P)\), verifies their associativity, enumerates \(\varphi_{u,v}\) for every \(u,v\in S^1\), verifies the maps are injective and preserve the zero point, checks every generated nontrivial map has one source and one target regular group class, checks all pairwise compositions remain inside the proposed finite family, and compares its size with the Brandt formula. Tests cover trivial, cyclic, symmetric and dihedral structure groups; nontrivial group sandwich labels; regular supports of sizes one, three, five, and six; and group-with-zero edge cases.

This finite verification does **not** exhaust all finite groups or all sandwich matrices, and no such extrapolation is asserted. The written algebraic proof independently resolves arbitrary finite instances. Priority remains subject to comparison with potentially inaccessible historical versions of the precursor literature. There is no independent external mathematical audit.
