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

# Reproducibility and boundaries

Run `python3 f4_cartier_check.py` with Python 3.9 or later; only the standard library is used. The script enumerates \(1,152\) type-\(F_4\) Coxeter matrices, validates \(24\) positive root/coroot pairs, checks inversion lengths and two independent constructions of each of \(6,168\) Bruhat covers, then computes all integer determinantal divisors. It prints \(233\) \(\mathbb Q\)-factorial elements, split as \(171\) with no torsion, \(49\) with \(\mathbb Z/2\mathbb Z\), and \(13\) with \((\mathbb Z/2\mathbb Z)^2\). The remaining \(919\) are non-\(\mathbb Q\)-factorial.

The bridge from these integer matrices to \(\mathrm{Cl}(X_w)/\mathrm{Pic}(X_w)\) is the cited Picard/Weil divisor basis theorem, not part of the finite checker. The code does not compute local class groups, partial flags, or torsion for nonsquare matrices. Computation with complete enumeration is an exact finite proof when combined with the described Coxeter and divisor-basis lemmas; it is not an external certification or an independent mathematical audit.
