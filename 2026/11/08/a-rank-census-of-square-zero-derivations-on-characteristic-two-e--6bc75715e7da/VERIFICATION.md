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

# Verification notes

The mathematical result follows from the written proof and explicit finite-group orders. The included standalone `checker.py` tests the original derivation equations and checks exact rank distributions from the independent formula. It requires Python 3 and no dependencies. Its corresponding UTF-8 console output is in `checker_output.txt`.

Exhaustive original-equation checks cover all linear endomorphisms in dimensions 3 and 4 over the two-element field; accepted maps must satisfy both the Leibniz rule on all basis pairs and the equation \(D^2=0\). Separate symmetric-matrix and functional enumeration covers \((r,q)=(2,2),(3,2),(4,2),(2,4),(3,4)\). Each rank count agrees with the formula. Finite-field arithmetic over the four-element field uses a polynomial basis modulo \(u^2+u+1\).

**Unproved by computation:** all unbounded-dimension cases, all powers of two not listed, and historical priority. These depend on the symbolic proof and literature comparison. No independent mathematical audit has been conducted.
