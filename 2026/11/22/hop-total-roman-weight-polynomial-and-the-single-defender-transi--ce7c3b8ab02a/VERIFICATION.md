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

# Reproducibility and scope

Use Python 3 and a C++17 compiler. In a directory containing the accompanying verification files, execute:

```sh
python3 verify_agreement.py
```

The driver compiles the direct graph-based C++ program, independently evaluates the symbolic polynomial, and compares every integer coefficient across ten parameter tuples. A successful run prints `DIRECT_AND_FORMULA_AGREE`, followed by the exact test summary. The exact direct enumeration output is stored in `direct_counts.txt`.

The C++ implementation constructs graph edges, computes graph distances, enumerates all \(3^{1+\sum_i s_i}\) assignments, and tests both original feasibility rules. The symbolic implementation manipulates integer polynomials and uses no graph-distance oracle. Both are reproducible without third-party Python packages. No finite check establishes the theorem in all dimensions; the all-parameter proof is the case classification in `RESULT.md`.

The source date used for the comparison literature is the documented 2023-03-30 online publication. Publication priority has not been independently certified. The verification programs do not constitute an external mathematical audit.
