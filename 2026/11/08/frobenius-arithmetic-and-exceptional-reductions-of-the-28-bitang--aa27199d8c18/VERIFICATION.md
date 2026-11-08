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

# Reproduction of the finite incidence and arithmetic certificate

Run the two bundled stand-alone Python 3 programs:

```console
python3 verify_incidence.py
python3 verify_direct.py
```

The first uses exact integer quadruples for \(\mathbb Z[t]/(t^4+1)\), builds the full set of \(28\) line equations, enumerates \(378\) pair cross products and \(3276\) triple determinants, computes field norms by \(4\)-by-\(4\) integer determinants, and checks that the only odd prime divisors are \(3,5,17\). It separately enumerates the complete exceptional incidence and Frobenius classes over the split finite fields \(\mathbb F_{3^2}\), \(\mathbb F_{5^2}\), and \(\mathbb F_{17^2}\). Its assertions validate all singular-multiplicity profiles, rational component counts, and rational singular-branch tables. The second script independently tests every rational point of \(\mathbb P^2(\mathbb F_p)\) for thirteen primes and every point over \(\mathbb F_9,\mathbb F_{25},\mathbb F_{49}\) against all geometric bitangents over a splitting field.

Expected terminal assertions are `VERIFY_DYCK_INCIDENCE_OK 28_LINES 3276_TRIPLES 3_5_17_EXCEPTIONAL` and `VERIFY_DYCK_DIRECT_OK 13_PRIME_FIELDS` and `VERIFY_DYCK_DIRECT_EXTENSION_OK F9_F25_F49`. Any assertion failure is an unsuccessful check, not evidence of impossibility. All-extension claims are deduced from the exact norm and Frobenius arguments, not from the finite-prime sample.

No separate independent mathematical audit has been performed.
