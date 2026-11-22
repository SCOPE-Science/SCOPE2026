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

# Verification procedure

Run `python3 check_inverse_lyndon.py` from the directory containing the two packaged auxiliary files. The code builds the compressed suffix-rank solution with integer prefix doubling, counting sorting, Kasai LCP and segment-tree range minima. On small words it independently computes each longest inverse Lyndon prefix by trying lengths and checking every proper suffix, then compares the full arrays. It also checks large compressed cases without expanding the text and verifies segment coverage and value bounds.

`check_output.txt` records 27,304 exhaustive nonempty gap tuples, 1,500 pseudorandom small cases with a fixed seed, and large tests through 2,048 marked ones and more than ten billion character positions. All passed. The symbolic proof in RESULT.md, including the published NGS/LCE lemma and the terminal-aware gap-code comparison, is needed for universal correctness. These tests do not establish priority, asymptotic runtime empirically, or independent certification.

Output coordinates are zero-based; the code's input consists of the number of initial zeros and the list of the zero lengths immediately after each one, with zero-length gaps allowed. Returned triples `(start, stop, first_value)` represent an arithmetic progression `lambda[position] = first_value - (position-start)` on the half-open interval. No expansion is performed for the large tests.
