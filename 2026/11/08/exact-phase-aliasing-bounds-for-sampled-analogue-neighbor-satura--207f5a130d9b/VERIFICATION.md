---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-14.md",
      "INDEPENDENT_AUDIT_2026-11-14.json"
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

Distinct values in different phases make K zero-distance neighbours equivalent to a residue multiplicity inequality. Exact training count is c_T(p)=max(0,1+floor((T-Y-H-p)/P)). At T-Y-H=(K-1)P+r-1 exactly r/P of full-period test starts are saturated. Stride d visits residues of one coset modulo gcd(P,d); the stated formula g/P times the intersection cardinality follows from modular orbit counting. With r=1, stride d=P selects exclusively saturated phase, yielding sample fraction 1 vs full fraction 1/P and maximal gap 1-1/P; coprime d over full orbit is unbiased. Independently verified 2376 (P,K,Y,H,stride) parameter instances. Assumptions include from-start exact periodicity, no Theiler exclusion and full stride cycles.

## originality

PASS

Earlier finite-precision Lyapunov-collapse study defines exact Kth-nearest-neighbour saturation and subsampling protocols, but the finite phase occupancy cutoff and sharp stride aliasing counterexample are not implied by the generic observation that finite orbits repeat; this identifies a sampling identifiability ambiguity rather than a new Lyapunov theorem.

## value

PASS

The specific diagnostic is motivated by finite-precision predictive-neighbour saturation. A concrete sharp false-100%-saturation example and exact sufficient anti-aliasing sampling rule provide a useful methodological boundary; not just a renamed CRT count divorced from application. No claim that existing published experiments actually had this bias.

The dated certificate retains the supplied scientific assessment, sources and limitations.
