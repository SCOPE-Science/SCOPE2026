# Independent Audit — 2026/09/11/045

**Audit date:** 2026-09-28 (UTC)  
**Audited tree:** `8f1c88eaa60907909422154aca521b50472c5508`  
**Disposition:** **FAILED**

## Correctness

The numerical eigenvalue ledger may be internally reproducible, but the research conclusion uses the wrong spectral test. For NtD data a larger conductivity gives a smaller NtD operator. With the record's sign convention DΛ_0(χ_C) is negative, the standard positive-inclusion linearized monotonicity condition is Λ(σ)-Λ_0-βDΛ_0(χ_C) <= 0 in Loewner order. Certifying that requires the largest eigenvalue to be nonpositive. The record instead defines detection by min spec >= 0 and infers an empty reconstruction merely because the smallest eigenvalue is negative. A negative minimum neither establishes non-detection nor even determines the sign of the operator. This already fails on σ_A, which is a definite positive inclusion, so the claimed 16-cell 'ghost' verdict is not certified by the reported minima.

## Originality

I found no prior source for this exact nested-square pair, α=1.5, 16-cell Galerkin ledger, or the reported numerical values. The finite computation itself appears specific to this package. This narrow originality does not rescue the invalid interpretation of the ledger.

## Scientific value

Because the reported statistic is not the monotonicity decision statistic, the package does not establish the advertised blind spot. The raw FEM table can be retained as exploratory data, but without recomputing the appropriate extremal eigenvalue/Loewner condition it does not support a scientifically usable obstruction to the linearized method.

## Limitations

- The audit does not dispute the reported FEM minima or NtD gap as raw Galerkin numbers; it rejects the inference drawn from them.
- A repaired record would need to state the correct linearized monotonicity inequality and recompute the appropriate extremal eigenvalue (or full semidefinite test) for every cell.
- The 16-mode/mesh-discrepancy certificate is also not a continuum proof, as the source already acknowledges.

## Evidence

- [Harrach–Ullrich, Monotonicity based shape reconstruction in electrical impedance tomography](https://arxiv.org/abs/1812.05300): States the NtD monotonicity direction: pointwise larger conductivity gives smaller current-voltage measurements; this fixes the operator-order orientation underlying linearized tests.
- [Garde–Staboulis, The regularized monotonicity method: detecting irregular indefinite inclusions](https://arxiv.org/abs/1705.07372): Provides the indefinite-inclusion monotonicity framework cited by the record; it does not justify replacing a Loewner-order test by the sign of the smallest eigenvalue as done here.

Repository evidence was read from `SCOPE-Science/SCOPE2026` at tree `8f1c88eaa60907909422154aca521b50472c5508`; comparison against current `main` found no changes under this record path since the assignment snapshot. No repository writes were made by this audit.
