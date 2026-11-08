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

# Reproducible verification

From the directory containing both standalone verifier source files, run `python3 verify_snub.py`. This constructs the snub cube exactly in the cubic quotient ring, confirms 60 edges and 32 triangles, partitions its 24 singly-triangular edges into six squares, and enumerates exactly \(7^6=117649\) candidates. It returns `VERIFY_EXACT_OK 24_vertices 60_edges 32_triangles 6_squares critical_201 zero_18 saturation_5302`.

Run `g++ -std=c++17 -O3 verify_exhaustive.cpp -o verify_exhaustive` and then `./verify_exhaustive`. That separate Gray-code enumeration evaluates all \(2^{24}=16777216\) spin states, determines exact maximum cuts for each magnetization, and asserts the thirteen values for nonnegative field. Its final line is `VERIFY_EXHAUSTIVE_OK 16777216 configurations`.

The analytical proof uses the graph-wide triangle incidence bound and vertex degree to establish the sharp ground energy for all positive \(J\) and real \(h\). Finite checks are exhaustive over this 24-spin graph; they are not proofs of any infinite-size claim. All cases of negative field follow by spin reversal. An independent external scientific audit has not been performed.
