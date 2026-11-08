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

# Verification

The theorem is proved for arbitrary primes and finite abelian primary groups. In particular, the matrix-avoidance lemma is established by an exact fixed-vector incidence count, not inferred from computation. The quotient-to-matrix-ring argument proves the universal fiber size.

Standalone checks used only the Python standard library:

- Every ordered pair of the 48 matrices in GL2(F3): 2,304 instances; each admits at least 14 witnesses.
- Every single input in GL2(F2): 6 instances; each admits at least two witnesses.
- 125 reproducibly sampled four-input lists in GL2(F5): each admits at least 148 witnesses. This sample is not exhaustive.
- Exact enumeration of all scalar input lists for p=2,3,5,7, and one or two multiplicity-one blocks; probabilities and witness-count distributions match occupancy.
- All 11,664 automorphism pairs of C3 ⊕ C9: 2,916 have exactly 27 witnesses and 8,748 have none.

The included `checks.py` can be run using `python checks.py`; output is included as `CHECKS.txt`. The standalone tests do not establish historical novelty or general correctness independently of the proof.
