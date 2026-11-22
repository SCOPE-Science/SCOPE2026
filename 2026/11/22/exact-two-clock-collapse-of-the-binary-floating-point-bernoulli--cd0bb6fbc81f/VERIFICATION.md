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
# Verification and reproduction

Run `python3 check.py` with Python 3 and no third-party packages. The verifier constructs all representable normal and subnormal values directly from exponent/significand cells, maps them to integer ticks of the smallest subnormal unit, and simulates integer-exact doubling modulo one. It compares the first time to zero for every initial value and each full image set after every iteration against the theorem. The executed verification covered every parameter pair with precision 1 to 7 and normal-exponent depth 1 to 6 (42 formats), plus all 15,360 binary16 states, totalling 18,789 tested initial numerical values across 43 formats. Both histogram and support checks passed at all time indices. For binary32 and binary64, the script checks only symbolic boundary identities; exhaustive enumeration of those two very large formats is neither claimed nor needed for the proof.

The general mathematical argument is the five-step bijection/counting proof in `RESULT.md`; finite tests cannot establish the infinite-parameter theorem. Historical coverage of mathematical priority is bounded by inspected literature. Independent mathematical validation was not performed.
