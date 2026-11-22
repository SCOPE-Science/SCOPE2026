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

Positive normalized Shepard weights sum to 1, so all data triples decompose into a constant and two unit steps; the operator BV seminorm equals the larger variation of the two step responses. The opposite-cell weight has one strict interior maximum, obtained by differentiating its denominator and solving ((a+b-x)/(x-a))^(p+1)=(a+b)/a. Evaluating the maximum and reflecting produces the stated r,c coefficient. Monotonicity in mesh ratio follows from positive derivative of s(1+c_s) and monotonic c_s^-p; limits p down to 0, p up to infinity, r down to 0 and pr→tau follow explicit power asymptotics, including tau=0. Independently evaluated several unequal meshes, p values and the nodal/extremum formula with numerical agreement; inspected checker.py; finite tests supplement the fully analytic claim.

## originality

PASS

The underlying positive inverse-distance Shepard formula is classical. Available relevant partial shape-preservation studies did not explicitly cover the exact 3-site full-interval total-variation gain or the mesh–power logistic boundary layer. Gal’s especially relevant monograph chapter was inaccessible in full; retain its substantive priority risk without treating inaccessibility as scientific falsity.

## value

PASS

A sharp exact norm for a foundational positive interpolant is useful for understanding monotonicity defects, nonuniform meshes and whether high inverse-distance powers improve edge stability. The noncommuting limits produce a nontrivial quantitative logistic boundary layer; this is not mere substitution in a standard convergence theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
