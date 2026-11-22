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
# Verification

Run `python3 check.py` using Python 3. The executable constructs each recurrence from the initial values, determines its return period from the full two-coordinate state, and independently counts all values and quotients modulo each tested prime power. It verifies the asserted least scalar period and two-per-parity value fibers for regular cases, and the two full value balls plus the entire unit quotient set at the exceptional dyadic boundary.

Observed output:

```
PASS 470 complete-period finite tests; 38068 recurrence terms; every regular prime-power fiber and dyadic unit quotient checked
```

For the unrestricted theorem, the regular-case step is the exact valuation of a first binomial term in \((I+aM)^d-I\); every higher term has at least one additional factor of \(p\). In the exceptional dyadic case, the first \(4dB\) matrix term has scalar valuation \(3+\nu_2(d)\) on the selected branches and all higher terms are divisible by \(2^{4+\nu_2(d)}\). These are the infinite mathematical arguments; a finite execution is not exhaustive for all integers and powers.

No independent mathematical audit has been performed. The verified source's earliest public version was 14 July 2022, earlier than its 2023 journal publication.
