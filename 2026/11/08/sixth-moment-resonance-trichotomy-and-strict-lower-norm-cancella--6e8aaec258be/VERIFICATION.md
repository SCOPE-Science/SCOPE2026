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

# Reproducibility and verification limits

Run `python3 artifacts/verify.py` with Python 3's standard library. The checker exactly enumerates the sixth-power Fourier zero-sum coefficient table for integer frequency ratios from \(2\) to \(50\), comparing every rational coefficient with the theorem's predicted phase monomials. It checks the four exceptional quintic derivative identities and the one twice-frequency derivative identity with rational polynomial arithmetic, evaluates rational sign-change brackets for all selected nonzero extrema, and independently checks a family of exact amplitude witnesses.

The finite frequency sweep is a consistency test, **not** proof that no further resonances exist: the proof's six-character integer-count argument handles all positive frequency pairs. The root-counting proofs rely on Descartes' rule and derivative monotonicity; the executable rational sign tests provide isolating brackets, not a black-box numerical certification of all real roots. Numerical decimal approximations are diagnostic and have not been used to justify global inequalities. Scientific originality remains qualified by possible equivalents in inaccessible literature.
