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

# Verification details

Compile `verify_motzkin10.cpp` with standard C++17 and run `./verify_motzkin10 --verify` in the directory containing its three complete certificates. The program enumerates all ten-step Motzkin excursions using the height boundary, constructs their exact Boolean support, and computes the 20-bit Walsh spectrum by integer butterflies. An independent per-frequency signed-height recurrence gives the same 1,048,576 values. Certificates `spectrum.csv`, `projection_kernel.csv`, and `zeros_by_weight.csv` are regenerated in memory and byte-compared against the packaged originals. The checker confirms 2,188 distinct paths, 67,312 zero coefficients, rank 981,264, 48 minimum-weight-four zeros, first minimum-weight mask 17924, and minimum nonzero multiplier magnitude 2. The two computed Parseval totals are 2,294,284,288 and 1,028,929,880,064. The support-projection kernel has absolute coefficient sum 52,163,296, yielding norm 1,630,103/32,768.

The exact boundary at lengths four through nine follows from the odd Motzkin counts 9, 21, 51, 127, 323, 835. The finite enumeration is exhaustive for the stated domain; no claim about all higher lengths follows from this computation. The unrestricted projection optimum follows separately by translation averaging. This verification is not independent external mathematical validation.
