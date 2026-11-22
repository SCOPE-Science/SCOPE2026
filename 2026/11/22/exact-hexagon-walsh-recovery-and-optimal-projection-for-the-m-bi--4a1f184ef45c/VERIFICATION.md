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

# Exact verification

Run `python3 verify.py` in the same directory. The program uses only Python's standard library and exact integers and rational fractions; no external data files or packages are required. It checks an explicit isomorphism between two graph constructions, independently enumerates all \(24\) simple six-cycles by graph paths and by all \(134{,}596\) edge subsets, verifies the nine-dimensional chord model and independently computes all \(512\) signed Fourier sums and their integer Walsh transform. It also verifies the complete endpoint projector-kernel histogram, the \(11{,}534{,}336\) rank, the \(5{,}242{,}880\) nullity, the sharp minimum nonzero multiplier \(4\), and the fraction \(123/16\).

The finite exhaustion is mathematically complete for the specified graph and the exact edge enumeration, not evidence about any infinite family. Global projection optimality is proved algebraically by translation averaging in `RESULT.md`; the code confirms its exact kernel norm but cannot itself establish the group-averaging argument. The originality judgment compares accessible relevant papers and mathematical records; unavailable full text and possible unindexed equivalents remain risks. Independent audit has not been performed.
