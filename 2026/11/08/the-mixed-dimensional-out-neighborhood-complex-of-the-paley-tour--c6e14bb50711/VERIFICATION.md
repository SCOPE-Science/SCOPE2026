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

Run `python3 verify.py` with Python 3.10 or later. Only the standard library is used. This code computes all 19 residue blocks and validates every pairwise four-point intersection; it enumerates the 8246 faces twice using different membership algorithms. A complete topological sort of all 40014 oriented Hasse cover incidences proves that the 4080-pair Morse matching is acyclic.

The code evaluates every integer entry of the four-by-eighty-one critical Morse boundary by signed gradient recursion, proves a left row dependence with coefficients \((1,-2,-1,1)\), and proves a rank-three unit determinant using rows \((0,1,2)\) and columns \((0,1,4)\). It then independently computes the entire mod-two simplicial boundary-rank sequence. These exact computations are the finite ingredients needed for the homotopy proof in `RESULT.md`; they are not claimed as an independent audit.

Recorded standard output appears in `verification_output.txt`. The assertion `ALL_CHECKS_PASS` means precisely that the listed algorithmic checks succeeded. It does not establish publication priority or imply an equivariant theorem. The human-readable proof explains the topological implications of the certificate; machine output alone is not a substitute for them.
