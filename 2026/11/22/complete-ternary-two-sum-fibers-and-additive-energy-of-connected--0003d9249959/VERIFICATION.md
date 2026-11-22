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

# Reproducibility and verification

From the directory containing these embedded files, run:

```sh
python3 fiber_certificate.py
python3 independent_energy_check.py
```

Both scripts use only Python's standard library and deterministic exact integer arithmetic. The first reconstructs the whole carry-state closure, checks every state transition and output label, and verifies the exact 18-by-18 integer matrix identity \(T^2(T-3I)(T-I)^5=0\). It also checks the proposed multiplicity histograms and energy at all depths zero through seventeen. The identity, the explicit degree-four-plus-exponential formulas and the first eight checks jointly give a rigorous all-depth proof.

The independent script forms sparse digit-support sets directly, enumerates ordered pair sums modulo \(3^r\) for depths one through ten, compares support and additive energy, and separately uses four-input carry paths through depth seventeen. Its finite checks are cross-validation of the main proof, not a substitute for the symbolic matrix identity. Representative exact energies are \(E_1=6\), \(E_2=77\), \(E_3=309\), and \(E_4=822\).

Only the precise ternary two-sum theorem stated in `RESULT.md` is asserted. Historical priority cannot be proven by search, and a separate independent mathematical audit has not been performed.
