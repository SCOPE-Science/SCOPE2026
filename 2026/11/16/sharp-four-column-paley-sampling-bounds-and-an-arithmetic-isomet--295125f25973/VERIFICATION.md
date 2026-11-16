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

Execute `python3 paley_four_check.py` using Python standard library. It constructs exact quadratic-residue sign matrices for each four-set at \(p=13,17\). For nonstar matrices it computes strictly positive leading principal minors of an explicitly scaled rational symmetric matrix. The rational floor of \(\sqrt p\) differs by less than \(10^{-9}\), giving an operator norm perturbation at most \(3/(10^9(p-1))<0.001\). It separately proves, by integer square inequalities, that the exact star smaller eigenvalue falls beneath the rational cutoff. This is an exhaustive finite certificate for the two exceptional primes.

A separate loop tests five larger primes; these tests do **not** prove the universal statement. Its proof uses Paley strongly-regular graph parameters and the Hoffman bound as explained in `RESULT.md`. Neither the full matrix nor arbitrary other graph geometries are covered. The independent mathematical audit remains unperformed.

Actual checker output:

```text
CERTIFIED_EXCEPTION 13 subsets 715 sign_matrices 56 nonstar_patterns 52 counts {'star': 26, 'matching': 39, 'independent': 0, 'other': 689} r= 0.085
CERTIFIED_EXCEPTION 17 subsets 2380 sign_matrices 62 nonstar_patterns 58 counts {'star': 136, 'matching': 102, 'independent': 0, 'other': 2244} r= 0.23
CERTIFIED_LARGE 29 edges_sampled 14
CERTIFIED_LARGE 37 edges_sampled 18
CERTIFIED_LARGE 41 edges_sampled 20
CERTIFIED_LARGE 53 edges_sampled 26
CERTIFIED_LARGE 61 edges_sampled 30
PALEY_FOUR_EXTREMA_PASS small_primes=5,13,17 large_primes=29,37,41,53,61
```
