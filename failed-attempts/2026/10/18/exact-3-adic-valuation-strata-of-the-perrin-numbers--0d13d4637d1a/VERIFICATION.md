---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Checked the companion transition and initial state, M^13=I+3B, the four zero classes modulo 3, and the branch slopes (12,17,29,158). For j>=2 the coefficients of the falling-factorial polynomials in the normalized interpolation have valuation j−1−v3(j!)>=1 and tending to infinity. Their divided differences therefore give the claimed 1-Lipschitz remainder after extracting 3. This proves the constant class 0 from its unit constant and the three isometries from their unit slopes. The isometries are bijections on every finite residue ring and hence on the inverse limit, so the roots are unique and the valuation formula holds at every nonnegative index, including R_1=0. The base matrix has order 13 modulo 3, and cubing I+3^{j+1}U with U=B mod 3 increases the first nonzero matrix valuation by exactly one. This establishes order 13·3^{k−1}, not merely divisibility by this number. At k>=2 each isometry selects one t mod 3^{k−1}; k=1 instead has four base zeros. The classes for each exact valuation are differences of residue cylinders, giving the three asserted density cases. Independently followed basis-vector and Perrin-state orbits and checked all zero indices in a period through k=8, and separately confirmed the branch slopes and interpolation inputs.

## originality

FAIL

Distinct indexed record 4fc0b74b0c47 covers the all-index valuation classification and exact densities, and adds root digits and uniform discrepancy. Though it does not phrase the exact matrix order as a finding, its exact thirteenth power and its own binomial congruence imply the order without a new lemma. Its root congruences then give the exact zero counts over that period. This is verified mathematical coverage by a record with a later index path, not evidence of earlier priority, reuse or dependence.

## value

FAIL

An exact valuation law for a classical recurrence and its densities would be useful, but here those facts are already covered by the distinct stronger discrepancy result. The matrix order and period-zero counts, though not separately advertised there, are mechanical consequences of that record's displayed congruence and root law, so they do not leave a stand-alone unknown exact invariant in the proposed finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
