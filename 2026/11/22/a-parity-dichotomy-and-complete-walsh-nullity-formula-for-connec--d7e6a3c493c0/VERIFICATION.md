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

# Mathematical verification

The closed-form proof in `RESULT.md` derives every multiplier directly from a disjoint decomposition of connected and disconnected vertex subsets. The proof treats the empty frequency separately and checks admissible frequency sizes in both parity cases. A polynomial-coefficient argument counts every zero frequency once, and a binomial estimate establishes the asymptotic.

Run `python3 verify.py` from this directory. The program uses exact integers to enumerate all nonempty connected vertex subsets, computes full Walsh–Hadamard transforms, and checks agreement with an independently evaluated formula. It also constructs the omitted-part coefficient counts. The reproduced check passed 751 assertions covering all 136 nondecreasing part-size vectors with two to six parts, each size at most six and total number of vertices at most eleven. The tests are finite and do not establish the all-parameter theorem.

No independent audit has been performed.
