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

# Verification evidence

Execute `python3 check_mub_phase.py` in the directory containing this file and the checker. The checker uses only the Python 3 standard library. It exhaustively counts the phases of all ordered, distinct-base, labeled triples for primes \(3,5,7,11\), then directly computes complex defining inner products on 48, 240, 672 and 2,640 selected triples, respectively. The maximum observed complex residual is below \(2\times10^{-15}\). It also verifies the published full-tensor phase-zero counts for primes 3 and 5, using an explicit convention for zero triple products. The code checks *finite* cases; the infinite-prime conclusion follows from the Gauss sum and combinatorial argument in RESULT.md.

The three-dimensional Gram cubic follows from an independent trace and determinant calculation of a Hermitian matrix. The phase-count normalization uses ordered triples, including the computational basis, and excludes any repeated basis. The results do not depend on arbitrary numerical thresholds for classifying phase equality: modular sign/exponent pairs are compared exactly before any floating-point spot test.
