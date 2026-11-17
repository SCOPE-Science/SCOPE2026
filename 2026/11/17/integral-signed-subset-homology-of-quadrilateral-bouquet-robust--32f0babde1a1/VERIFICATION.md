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

The standalone standard-library Python 3 program `verify.py` is part of this package. Execute `python verify.py` and compare its stdout to `verification_output.txt`.

The program tests \(m=3,4,5\) and every \(4\le k\le m+1\). It enumerates the vertex subsets of the complete bouquet graph, checks the exact relative-ball partition and boundaries, and builds the relative fundamental cycle with signed coefficients on every top simplex. It then evaluates generators of the full natural automorphism group on these cycles, including orientation signs in integral simplicial chains, and compares the resulting representation with the proposed signed-subset action. An independent check enumerates the automorphism-fixed faces and calculates the signed simplicial Lefschetz trace, confirming the predicted group character in all six test cases.

The complete universal proof uses the combinatorial relative-ball decomposition and oriented generators. It does not infer universal validity from the finite enumeration. Source-document inspections and originality comparisons are recorded in `REVIEW.md` and `AUDIT.json`. Independent mathematical audit has not been performed.
