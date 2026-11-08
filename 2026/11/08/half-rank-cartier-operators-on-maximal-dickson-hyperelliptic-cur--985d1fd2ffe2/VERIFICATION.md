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

# Reproducible checks and limits

Run `python3 cheb_verify.py` with Python 3 (standard library only). The program computes the Dickson recurrence directly, exponentiates the defining polynomial modulo each prime, constructs the hyperelliptic Cartier–Manin matrix via the coefficients indexed by \(pi-j\), and performs exact prime-field row reduction and multiplication. For \((p,n)=(5,13),(7,25),(13,17),(31,13),(47,13),(73,13)\), it checks first Cartier rank \((n-1)/4\) and square zero, ending in `VERIFY_OK`.

The checks cover six finite inputs. They do not prove a theorem for unbounded \(n\) or primes. The uniform proof is the fixed-point-free modular involution argument and the tame quotient differential calculation in `RESULT.md`.
