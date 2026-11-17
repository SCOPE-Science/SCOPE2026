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

# Reproducibility and proof boundaries

Run `python3 verify.py` using Python 3.10 or newer; no external packages are needed. `verify_output.txt` records the exact expected output. The code independently constructs the graph and simplicial complex directly from graph triangles and checks the chain ranks modulo two, reduced Euler characteristic, signed Lefschetz traces of a common-core transposition, an internal private transposition, and permissible page swaps. It has nine complete finite cases, five of which are comparison controls from the two-page boundary; its four-page case uses 3,171 nonempty simplices. The last line must be `COMMON_CORE_CLIQUE_BOOK_PASS`.

Finite mod-two homology cannot prove integral freeness, the wedge type, or an unrestricted formula. Those assertions instead follow from the explicit simplicial cover, the nullhomotopic cone attachments, the CW one-cell argument, and natural integral relative-chain calculations in `RESULT.md`. Integral symmetry is at the homology-module level; an equivariant wedge splitting is unproved.
