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

# Reproducible verification

Run `python3 verify.py` (Python 3.10 or newer; standard library only). The complete recorded output is `verify_output.txt`.

The verifier reconstructs the Chvátal graph from a literal edge list and proves its advertised graph properties by exhaustive vertex tests. It independently enumerates both facet-downward and complement-triple face criteria on every subset. It builds the exact staged matching and explicitly topologically sorts every Hasse incidence to certify acyclicity. It computes the signed integral Morse attaching degree by recursive gradient paths and by a separate integral unit-pivot top-boundary reduction. Both return 2. Finally, full mod-two boundary reduction and mod-three ranks cross-check the homology consequence.

The finite computation is an exhaustive proof for the specified graph, not evidence for an unproved infinite family. Standard discrete Morse and CW attaching-degree theorems are applied mathematically after the finite certificate. Independent external audit has not been performed.
