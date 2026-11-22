---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

At the frozen tree 96a9fe26, reconstructed the orientation-bit convention and the unique source strongly connected component recurrence: each source component U contributes its signed internal strong-tournament sum and the forced outward cross-arc sign. An independent 2^15-orientation reachability enumeration followed by exact 15-bit integer Walsh transform reproduced 22,320 strong tournaments, the complete 12-level absolute coefficient distribution, 24,352 zero coefficients and 8,416 nonzeros. Independently enumerated all S_6 edge-support permutation orbits and orientation-reversal parity; obtained 156 orbits, two exceptional eight-edge zero orbits represented by 958 and 1883, 360 members each, and exactly 720 symmetry-unforced zeros. The inverse transform of nonzero-frequency support has absolute numerator sum 1,399,040 and hence projection norm 1,399,040/32768=5465/128. Translation averaging of arbitrary projections onto the invariant Fourier range proves unrestricted optimality. Actual code and certificates checked at the assigned Git tree: verify_tournament_enumeration.cpp, verify_tournament_scc.cpp, walsh_coefficients.txt (32,768 coefficients), tournament_support_orbits.tsv (156 rows). The statement classifies only the two specifically defined symmetry-forcing mechanisms, not all conceivable identities.

## originality

PASS

The edge-wise signed Fourier census and precise two unexpected zero orbits are not supplied by the classic enumeration of strong tournaments, by the source-component descent polynomial, or by distinct tournament subclasses in the indexed SCOPE comparisons. Best-of-knowledge priority with nonexhaustive historical records.

## value

PASS

Strong connectivity is a basic tournament invariant, and the first moderate complete orientation cube where nontrivial symmetry-unforced cancellation can be classified is mathematically natural. Separating exactly 720 zeros in two eight-edge support orbits from 23,632 symmetry-forced zeros produces a structural, precisely reproducible boundary, while rank and sharp endpoint projection norm quantify Fourier recovery. The calculation is finite but not an arbitrary slice or merely reprinting the 22,320 tournament count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
