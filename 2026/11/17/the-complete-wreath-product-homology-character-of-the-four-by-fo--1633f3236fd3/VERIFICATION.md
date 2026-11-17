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

# Reproduction and limits

Run `python3 verify_rook2.py` in an environment with Python 3 and its standard library; no network or nonstandard packages are required. `verification_output.txt` records the complete expected output. Success requires the final line `ROOK2_FULL_EQUIVARIANT_CHARACTER_PASS`.

The executable enumerates all \(2^{16}\) cell subsets, constructs exact integral simplicial boundary *supports* for mod-two reduction, checks boundary ranks \((15,105,279,144)\), and uses dimension and \(\partial^2=0\) to justify their equality with the rational ranks. It generates all \(1152\) graph automorphisms, checks they preserve each face, computes the signed Lefschetz number two independent ways, and checks the expected twenty conjugacy-class aggregates. The irreducible multiplicities are recovered from exact character inner products and extension traces; subgroup invariant ranks are independently averaged. `character_table.csv` is an inspectable compressed table of all twenty class values.

A complete finite check is not an independent mathematical audit, a proof of novelty, or a theorem for other board sizes. This package does not claim any determination of integral quotient torsion or homotopy equivalences of orbit spaces.
