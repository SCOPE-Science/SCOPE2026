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

`verify.py` uses only the Python standard library and directly reconstructs the two-dimensional cubical deleted-product chains for four bipartite graphs, before comparing the full signed cellular Lefschetz characters against the tensor-lattice formulas. For each of the four graphs it constructs integral fundamental-cycle vectors in the two crown graphs, takes their tensor products and tests every cellular boundary coefficient. It also checks the full degree-two boundary rank over the finite field with 101 elements. The independent character enumerator handles graph relabelings, particle transposition, and the class exchange when the part sizes agree; 4,176 actions are compared.

Run `python3 verify.py`; the stdout must match `verify_output.txt`. Tested graph sizes are \((3,3),(3,4),(4,4),(3,5)\). The general integral tensor-lattice theorem is established in the written proof using direct-summand arguments over \(\mathbb Z\), not inferred from these finite checks. No computational claim about arbitrarily large instances, homotopy equivalence, publication priority, or an independent audit is made.
