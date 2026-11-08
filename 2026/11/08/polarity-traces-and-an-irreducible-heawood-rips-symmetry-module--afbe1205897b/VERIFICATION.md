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

The proof has two independent types of evidence. The integral equivariant identification is an exact Mayer–Vietoris chain argument for the canonical contractible cover. The full finite Fano character was independently recalculated by comparing (i) the signed cellular character of the incidence graph, multiplied by bipartition sign, with (ii) signed simplicial Lefschetz sums computed directly from all 331 faces for all 336 automorphisms. The full calculation found exactly nine conjugacy classes, character squared norm 336, and invariant character sum zero. The generator description of the full group was tested on every incidence edge. The order-three and order-four projective-plane examples check the same formulas using independent finite enumerations.

Run `python3 verify_plane_equiv.py` from this directory. The expected stdout is embedded as `verification_output.txt`. The code uses only Python standard library modules; no downloaded data or package dependencies are required. Numerical outputs are exact integers; no floating-point rank estimates appear.

The direct simplicial computation is finite and validates the displayed small cases only; it is not an exhaustive test of all finite projective planes. The general theorem uses the structural proof rather than extrapolation. The program does not compute integral lattice indecomposables or an equivariant homotopy equivalence. Independent mathematical auditing has not been performed.
