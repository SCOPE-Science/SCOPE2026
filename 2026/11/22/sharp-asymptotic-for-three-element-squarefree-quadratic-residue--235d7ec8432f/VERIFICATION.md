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

The finite tests are reproduced by running `python3 check.py` with Python's standard library. Expected output is provided in `check_results.txt`. They compare direct enumeration of three distinct squarefree integers with the independent factor form \((uv,uw,vw)\) at heights \(30,100,200,300\). The exact counts agree: \(12,77,222,422\). The faster method gives \(2491,12775,77719\) at heights \(1000,3000,10000\). The prime product truncated at \(100000\) is displayed as numerical context only; no decimal certification is claimed.

The infinite proof requires three mathematical arguments beyond computation: Fried's criterion plus the all-prime Legendre-symbol reduction, injective and surjective pairwise-prime-factor parameterization, and CRT-lattice equidistribution plus the prime-square tail sieve on an unbounded finite-volume region. These arguments and their quantifiers are written in `RESULT.md`; finite experiments cannot replace any of them.

Scientific limitations: only the stated leading asymptotic is established. The literature comparison relies on material actually inspected, not on a priority certification. Independent audit has not been performed.
