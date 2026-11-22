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

The `artifacts/check.py` program directly enumerates Katětov assignments for every partition profile through seven named vertices and independently multiplies the full three-variable cluster polynomials. It also tests exact scalar uniqueness across all integer partitions of sizes one through thirty (28,628 profiles) and checks the complete small-value collision rule up to one million. Its recorded output is in `artifacts/check_output.txt`.

The infinite relation classification is established by the primitive-divisor theorem in the written proof. No finite enumeration claims to prove that theorem. No independent mathematical audit has been performed.
