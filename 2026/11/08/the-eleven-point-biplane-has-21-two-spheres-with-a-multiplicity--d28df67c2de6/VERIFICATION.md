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

# Reproducibility and verification

Execute `python3 verify.py` using Python 3.9 or later. Only the Python standard library is required. The accompanying `verification_output.txt` is the deterministic expected output.

The program reconstructs the eleven quadratic-residue blocks, confirms the symmetric \(2\)-\((11,5,2)\) design and all \(242\) faces, and separately reconstructs the identical out-neighborhood complex. It checks a \(110\)-pair matching by orienting and topologically sorting all \(715\) Hasse incidences. The critical-cell vector is one vertex and \(21\) two-cells, which proves the integral wedge through the discrete Morse theorem.

An independent mod-two boundary elimination gives rank \(45\) in degree two. All \(660\) generated automorphisms are enumerated without assuming unverified group-completion heuristics; signed simplicial Lefschetz traces are computed over *every* face and *every* group element. The full class-order trace counts agree with a sum of the published ten- and eleven-dimensional irreducible characters. The order-\(55\) affine subgroup invariants are evaluated separately.

The checker verifies finite combinatorics and identity of the group character; the interpretation invokes published mathematical theorems on discrete Morse complexes, character theory and rational finite-group transfer. It does not independently prove abstract group isomorphism with \(\mathrm{PSL}(2,11)\), which is sourced to the published biplane automorphism theorem, nor establish publication priority.
