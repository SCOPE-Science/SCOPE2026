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

# Computational verification

Run `python3 verify_clique_join.py` with a standard Python 3 installation; no third-party libraries are required. The code constructs every labelled triangle-free graph on \(1\) through \(5\) vertices, forms both \(K_2\) and \(K_3\) graph joins, enumerates all clique-free faces from actual forbidden triangles, and separately enumerates the independence-complex faces. Exact augmented boundary ranks are calculated over \(\mathbf F_2\) and \(\mathbf F_3\) and every reduced Betti number is compared with the wedge prediction. Additional instances use \(C_6\) and \(C_7\).

Recorded result: `TRIANGLE_FREE_CLIQUE_JOIN_HOMOLOGY_PASS`; \(1764\) coefficient-field checks, \(119588\) face instances and \(33316\) forbidden-triangle instances across repeated parameter tests. The checker does not certify the homotopy splitting, which is established by the contractible-CW-subcomplex proof in `RESULT.md`. It does not test every finite graph or infinite sizes and gives no independent audit.
