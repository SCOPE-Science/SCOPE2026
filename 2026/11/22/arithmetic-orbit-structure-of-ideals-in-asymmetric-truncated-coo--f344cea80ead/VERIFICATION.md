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

# Reproducibility and scope

The theorem concerns finite fields of all prime-power orders and all unequal branch lengths \(3\le m<n\). The symbolic proof in RESULT.md establishes that scope. These standalone numerical tests are finite cross-checks only; no computation is treated as an infinite-case certificate.

Run with Python 3 standard library from the directory containing both scripts:

```bash
python check_characteristic_ideals.py
python check_orbit.py
```

Both scripts enumerate all reduced-row-echelon radical subspaces over each tested prime field, filter those stable under multiplication by both branch generators, and then use concrete algebra automorphisms. The first verifies the number of fixed ideals and each dimension multiplicity. The second computes actual automorphism orbits via an explicit generator set, and compares the entire orbit-size-multiplicity polynomial. The exhaustive configurations are \((m,n,q)=(3,4,2),(3,4,3),(3,4,5),(3,5,2),(3,5,3),(4,5,2)\). Their detailed counts and success markers are included in `verification.log`.

The checker uses only prime finite fields and a finite generating collection, not a symbolic general prime-power algebra automorphism group. It is independent of the mathematical proof's enumerative deductions but not an external mathematical audit. Both dimensions and orbit multiplicities were replayed from the packaged code. Algebraic generality, including nonprime finite fields and all lengths, rests on the explicit proof.
