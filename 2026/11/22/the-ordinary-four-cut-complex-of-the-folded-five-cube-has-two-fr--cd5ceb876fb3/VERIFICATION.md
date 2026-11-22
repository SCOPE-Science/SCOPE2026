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

## Reproduction

Run `python3 verify_clebsch_cut4.py` using Python 3.10 or newer. The only necessary file is the enclosed script; `verification_cut4_output.txt` contains an actual run for comparison. Both are included together with the proof.

The script reconstructs the five-regular folded five-cube from sixteen even-parity bit strings; checks degree, common-neighbor counts and graph symmetry; exhaustively tests all 1820 four-subsets by two distinct connectivity implementations; enumerates all five- and six-subsets of the Alexander-dual complex; checks the complete two-skeleton; certifies a 455-by-455 triangular oriented boundary submatrix with diagonal entries ±1; verifies 480 shared tetrahedra and 200 unshared tetrahedra; and checks connectivity and coherent orientation of the 192-vertex incidence graph.

The determinant and primitiveness arguments are exact over the integers. The original cut-complex homology follows by integral Alexander duality, not from mod-prime ranks. The script does not attempt an independent proof of standard Hurewicz, Whitehead, or Alexander-duality theorems. It provides a finite combinatorial certificate for the nonstandard graph-specific steps and retains no reliance on unexamined external computation.

## Scope

The graph is the five-regular, not ten-regular, Clebsch graph. The claim is restricted to the ordinary four-cut complex and its combinatorial Alexander dual. No external or independent validation has been performed.
