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

# Exact reproduction

Run `python3 verify_fano.py` from a directory containing this file and the verifier. No nonstandard packages or network access are needed.

The verifier exhausts all \(64+729+4096+15625+46656=67170\) normalized phase assignments. For the fifth-root case it compares \(\mathbb Z[\sqrt5]\) values exactly by squared-integer tests. Every computed minimum, normalized minimizer count, and \(\operatorname{GL}(3,2)\) orbit-size partition is asserted against the displayed theorem. An independent Walsh-sample-side computation verifies the moments of all \(3472\) normalized minima (plus an additional nonoptimal test case per alphabet). Assertions passed.

The proof is a finite exhaustive computation plus the stated exact Fourier-autocorrelation identity. The verifier does not establish results for alphabets outside \(\{2,3,4,5,6\}\), for unrestricted phases, or for unrelated supports. Independent audit has not been performed.
