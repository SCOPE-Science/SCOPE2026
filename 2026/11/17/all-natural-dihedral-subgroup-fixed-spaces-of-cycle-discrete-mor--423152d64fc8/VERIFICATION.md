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
# Computational verification and mathematical limitations

The standalone `verify_morse_fixed.py` uses only Python 3's standard library. It does not import research libraries, previous runs, or external data. For each checked cycle length, divisor \(t\), and reflection parameter \(b\), it constructs the original incidence arcs, uses rooted-forest acyclicity to enumerate all feasible unions of vertex orbits, and builds the predicted orbit-label model using explicit indices. It compares **every orbit subset**, not only face counts; it additionally computes reduced boundary-matrix ranks over \(\mathbb F_2\) in small cases and compares them to the asserted sphere multiplicities.

The executed output reports 151 subgroup parameter instances, 184,212 orbit subsets, and 68 boundary homology checks. Full unreflected identity-group enumerations are limited to small cycles to avoid exponential expense. The recorded `verification_output.txt` was captured from the verifier. No computation is treated as a proof for arbitrary \(n\). The unlimited parameter assertion instead follows from the incidence-cycle and orbit-barycenter proof in RESULT.md and the cited classical cycle/path homotopy results.

The package supplies no independent mathematical certificate or independent audit.
