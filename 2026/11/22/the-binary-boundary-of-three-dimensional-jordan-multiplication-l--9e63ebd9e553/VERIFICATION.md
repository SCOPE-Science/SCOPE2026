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

# Reproducible finite verification

Compile `check_jordan_f2.cpp` with a C++17 compiler and execute it with `representatives.tsv` as the output argument. It enumerates all 262,144 commutative bilinear multiplication tables, exhaustively evaluates the Jordan identity on \(\mathbb F_2^3\), checks the degree-three coefficient conditions, tests extension stability directly on all vectors of \(\mathbb F_4^3\), and enumerates the 168 possible linear basis changes. It verifies exact counts, Burnside sums, all orbit covers and the two independent strictness criteria. The success marker is `F2_3D_JORDAN_CENSUS_OK`.

The representative table is produced from the smallest numeric code in each orbit. Exact expected counts are 2,858/47 pointwise laws/classes, 1,898/32 extension-stable laws/classes and 988/16 associative laws/classes. Fixed-point sums are respectively 7,896, 5,376 and 2,688; each divided by 168 gives the corresponding class count. These are exhaustive finite checks rather than statistical experiments.

The verification does not address higher-dimensional algebras, quadratic Jordan structures, or completeness of the accessible historical literature. An independent audit has not been performed.
