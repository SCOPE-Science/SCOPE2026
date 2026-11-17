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

# Verification of the even \(C_4\square C_n\) open-neighborhood theorem

Execute `python3 verify_even_tori.py` under Python 3; no third-party packages or external files are needed. Compare its stdout byte-for-byte with `EXPECTED.txt`.

For every even \(n\in\{6,8,10,12,14,16,18,20\}\), the checker constructs all faces from the original four-vertex graph neighborhoods, constructs the two-stage discrete-Morse matching, validates every matched cover and every unique face usage, checks the residual critical-cell counts \((2,2,2n)\), and topologically sorts the directed Hasse diagram to certify acyclicity. It independently checks that the signed integer column-winding function is a cocycle on every triangle and evaluates to \(n\) on each of the two preserved row-zero cycles. For \(n\in\{6,8,10,12\}\) it additionally calculates complete reduced mod-two homology by chain rank, obtaining dimensions \((1,2,2n,0)\) in degrees zero through three.

These are complete finite checks for each enumerated parameter, not proof for all even parameters. The infinite theorem relies on the explicit fiberwise Morse matching, its general acyclicity argument, and the integer winding obstruction written in RESULT.md. Neither a finite test nor a single field's Betti numbers would establish an integral sphere-wedge homotopy equivalence by itself. No independent mathematical audit has been carried out.
