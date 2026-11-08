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

# Reproduction

Extract the bundled `verify.py` next to this file and run `python3 verify.py` using Python 3. No external libraries, external files, probable-prime oracle, or network are needed. The exact program enumerates both Vieta rays up to the 160-bit boundary and checks all node equalities, 81 parity obstructions, 77 base-two Fermat witnesses, and the six surviving pairs by full integer trial division.

Expected terminal summary:

```text
VERIFY_OK cutoff=2^160 orbit_nodes=169 eligible_nodes=164
CERTIFICATES even_coordinate=81 odd_fermat_base2=77
FULL_TRIAL_DIVISION_PRIMES=YES conic_discriminant_crosscheck_100000=YES
PRIME_PAIRS=137,37;4817,1291;4817,17977;934441,3487381;998988257,3728274931;35166746297,131244083917
```

The independent discriminant check covers the bounded square through 100000; the unlimited claim that the two rays exhaust the Diophantine solutions is proved in the accompanying result, not inferred from the finite check. The cutoff census is exhaustive only because that proof and the exact finite certificates are combined. No independent audit has been performed.
