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

Execute `python verify_row_cyclic.py` using Python 3 and SymPy. The program constructs each nonattacking-rook face from labeled rows and columns, computes the threefold row-permutation orbit representatives and signed quotient boundaries, and verifies \(\partial_1\partial_2=0\). It then expresses the two-boundary map in the independently defined integral fundamental-cycle basis and applies exact integer Smith normal form.

Recorded output is embedded in `verification_output.txt`; the exact cases \(n=3,4,5,6,7,8\) respectively give free ranks of \(H_1\) equal to \(2,2,0,0,0,0\), torsion lists empty, empty, \([3],[3],[3],[3]\), and ranks of \(H_2\) equal to \(0,1,4,15,34,63\). No floating-point rank tests occur. All remaining integers \(n\ge9\) are proved by the general signed boundary presentation, connectivity theorem, freeness and Euler calculation, *not* by extrapolation from six cases.

The small-surface identifications use an elementary collapse for \(n=3\) and the classical triangulated-torus result for the cover at \(n=4\). A completely independent audit has not been performed.
