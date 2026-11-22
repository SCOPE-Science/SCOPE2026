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

# Reproduction and limits

Run `python3 artifacts/verify_fibonacci_composite.py` using the standard Python 3 library. The script constructs both Lucas-free Fibonacci recurrences directly, checks the least-period return state, compares all local parity-separated fibers for exponents one through five at each prime, and checks every residue of the composite moduli for seven exponent pairs including the large case \(7^3\cdot11^3\). It also checks that each measured support count matches the closed formula. Successful execution ends with `VERIFY_OK all local and composite parity fibers and exact support`.

Finite experiments establish only the listed finite cases; the arbitrary-exponent proof is the companion-matrix lifting, square-root formula, parity CRT, and support-counting argument in RESULT.md. The provenance of the 2022 source is arXiv first posting, not its later journal publication. Independent audit has not been performed.
