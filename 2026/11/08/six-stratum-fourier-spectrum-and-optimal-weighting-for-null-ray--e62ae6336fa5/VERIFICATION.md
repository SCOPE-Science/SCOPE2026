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

Execute `python3 checker.py` in the same directory. The checker uses only Python's standard library, exact modular integer arithmetic, and finite set enumerations. It checks every Fourier frequency and multiplicity for prime orders 2 and 3, and checks explicit Smith-stratum representatives at 5, 7, and 11. The odd-prime mathematical assertion is derived in the proof; computational sampling does not establish its validity for untested primes. Expected success marker: `RING_NULL_RAY_EXACT_SPECTRUM_CHECKS_PASS`.

Counting norms: each distinct affine coset is included exactly once per free null direction. Direction and frequency indexing are not normalized. The review covers mathematical reasoning and the reported standalone checks; independent audit has not been performed.
