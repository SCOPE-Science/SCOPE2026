---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

For equal-trace 2x2 Hermitians A=aI+v·σ and B=aI+w·σ, Pauli operator norm of a difference is |scalar|+|vector|. Spectral calculus gives |A|=(|a|,sgn(a)v) for r=|v|<=|a| and (r,(a/r)v) for r>|a|. On the outer region, derivative restricted to v changes has gain sqrt(1+a²/r²) (radial and tangent directions); inner region gain one. Integration along every chord, splitting at at most two sphere crossings, yields <=sqrt2 globally when a!=0 and strict below sqrt2 for each distinct pair, since equality of outer derivative is possible only on rank-one boundary points of measure zero. A near-boundary radial-plus-transverse directional witness approaches sqrt2; at a=0, |A|=|v|I so reverse triangle proves attained constant 1. Independently calculated 3200 input-pair ratios and three approaching gains 1.4004,1.4128,1.41407. The finite examples are corroboration, not general proof.

## originality

PASS

PASS best-of-knowledge. The exact constant jumps from one on the trace-zero affine slice to sqrt2 on every nonzero trace, and the nonattainment/local spectrum profile are not furnished by the general matrix-absolute-value continuity theorem or the separate monotone scalar functional-calculus theorem.

## value

PASS

The same-trace slice is natural for trace-preserving two-level quantum/perturbation problems; a qualitative universal continuity estimate does not determine why an arbitrarily small nonzero scalar trace raises the sharp spectral sensitivity from one to sqrt2. The rank-one derivative mechanism and finite-pair nonattainment are structurally informative and not a textbook norm-equivalence exercise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
