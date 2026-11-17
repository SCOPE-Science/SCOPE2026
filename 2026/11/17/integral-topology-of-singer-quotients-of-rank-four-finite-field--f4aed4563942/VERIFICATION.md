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

# Reproducible finite checks

Run `python verify.py` with Python 3 and SymPy installed. The script reconstructs vector subspaces and Singer multiplication on four-dimensional vector spaces over the prime fields \(\mathbb F_2\) and \(\mathbb F_3\); it does not use precomputed chain matrices. It constructs quotient chains of all strict flags, checks \(\partial_1\partial_2=0\), contracts a graph spanning tree integrally, and obtains the Smith normal form of the resulting degree-two boundary. It also enumerates all nonidentity powers of the projective Singer generator and their fixed subspaces. The complete recorded output is in `verification_output.txt`.

For \(q=2\), the quotient has \((5,21,21)\) cells in degrees zero through two, a reduced integral boundary with sixteen unit factors and one factor five, and four free degree-two homology generators. For \(q=3\), it has \((6,39,52)\) cells, thirty-three unit factors and one factor ten, and eighteen free degree-two homology generators. The exact output has been replayed from the embedded code.

The infinite-family statements do **not** follow from these finite tests. Their proof uses the finite-field intermediate-subfield classification, the rank-four Solomon–Tits theorem, Armstrong's theorem, Euler counting and the universal coefficient theorem. The full higher homotopy type and cup-product ring are not checked or claimed. No external independent audit is represented by this verification.
