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

# Verification of the antitone square-root factorization

Run `python3 verify.py` in the same directory as this document. Its only dependency is the Python standard library. It independently enumerates all pairs of side sequences of lengths between zero and six, tests the composition-square root condition, and compares each excess-rank coefficient to the explicit paired-rail polynomial. It also directly enumerates the order-preserving and order-reversing full transformation classes through chain length nine, builds the actual square and computes its image rank, and checks both the exact antitone fixed-target root polynomial for every idempotent and the predicted joint image-rank formula. An execution transcript of the successful checks appears in `verification_output.txt`.

There were \(2,584\) distinct idempotent targets for the largest tested chain size \(n=9\); the order-reversing square-idempotent total was \(12,087\). For the constant idempotent on a five-point chain whose value is the middle point, the directly enumerated antitone polynomial was \(1+8v+3v^2\), versus the increasing polynomial \(1+2v+v^2\).

The finite enumeration is not an infinite proof and does not establish historical priority. The full proof in `RESULT.md` derives the endpoint constraints, the rational paired-rail generating function, the per-target product and the all-size coefficient identity. No independently performed audit or external certificate is represented by these checks.
