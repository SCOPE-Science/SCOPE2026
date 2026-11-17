---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

The displayed cubic is smooth for p>5. Its geometric lines split into 15 rational diagonal lines and six quadratic-conjugate skew pairs; in nonsplit Frobenius fields, conjugate lines meet no rational points. The 15 diagonal lines form the (15,6,1,3) incidence graph, with ten Eckardt triple points and fifteen double points. All 27 lines are rational when the character of 5 is positive; 135 meeting line pairs minus 30 pair incidences at Eckardt points leave 105 ordinary double points. The Picard intersection matrix of the diagonals has rank six and Frobenius trace five in nonsplit, trace seven in split, giving #X(Q)=Q^2+5Q+1 or Q^2+7Q+1. Subtracting line unions gives N0=Q^2-10Q+21 or Q^2-20Q+99; extension alternation generates the zeta factors. Tangent quadratic forms exclude extra Eckardt triples for p>5. Independent prime-field point counting gave Q7=0,Q11=0,Q13=60 and matches derived formulas, not an all-field proof.

## originality

PASS

The surface, all 27 lines, 10 Eckardt points, split line incidence, and split complement count were already known. The inspected general cubic-surface papers do not state the complete fourfold incidence distribution for the actual untwisted Clebsch model across all extensions in the quadratic nonsplit case, nor its open zeta factors. The Galois-skew-pair descent and Picard trace distinguish the new statement from a bare split specialization; older Hirschfeld text not fully obtainable is a residual priority risk, not a generic automatic failure.

## value

PASS

The complement of geometric exceptional lines is a canonical open algebraic surface. Its Hasse--Weil zeta function, Frobenius split/nonsplit incidence spectra and sharp base-field point-free boundary constitute natural exact arithmetic invariants for every characteristic p>5, not arbitrary finite testing or a tiny numerical improvement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
