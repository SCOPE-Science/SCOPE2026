---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The real free two-convex norm has the same weak-2 test constraint as π₂ for the row operator. For each test vector choose a maximizing row and dualize the resulting Euclidean norm. Operator/nuclear duality gives tr√(Σw_r v_r v_rᵀ), where w_r is the sum of squared dual coordinates assigned to row r. Every probability vector is attainable, so the simplex reformulation is unrestricted. Cyclic averaging optimizes the cycle-only design at A₀=L_n/n; Fourier eigenvalues give the stated baseline. All rows lie in the mean-zero space and A₀ is positive definite there. The derivative at A₀ in a chord-mass direction minus the old distribution is the difference of the chord gradient (√n/2)a²ρ_{n,k} and the old gradient (√n/2)ρ_{n,1}. Hence any positive derivative strictly improves the objective, while if all derivatives are nonpositive the supporting inequality bounds every point in the full simplex. Fourier diagonalization and the identity for successive sin² terms give ρ_{n,k+1}−ρ_{n,k}=(2/n)cot((2k+1)π/(2n)); telescoping is valid through floor(n/2). The decreasing positive cotangents give the strict threshold inequalities, and the short-arc distance potential witnesses strict enlargement at a point, not at every potential. The fixed-span limit and diameter equivalent follow from the reciprocal-argument expansion of cotangent. A fresh direct spectral check over n=5,…,12 (32 spans) corroborated the formulas numerically, not the all-n proof. The supplied script was not executed; despite the verification description, it enforces an original-edge weight floor of 10⁻⁷ and samples selected one- and two-chord cases. The omitted simplex faces and larger families are controlled by the analytic proof, not by that numerical corroboration.

## originality

FAIL

The core criterion is mechanically implied by the inspected exact general row-design formula and derivative test, the known cycle optimizer, and an already explicit cycle Riesz kernel. The hypercube's Walsh distance formula is not being treated as a formula on cycles: it is the graph-independent optimization preceding that formula that transfers unchanged. The cycle Riesz result gives precisely the needed consecutive inverse-square-root kernel differences, not just a visually similar cotangent sum. This is demonstrated coverage by implication, not an assertion about priority between distinct same-date records.

## value

FAIL

The natural cycle design and exact threshold are motivated and would be useful if not already determined by existing results. In this submission the entire simultaneous classification follows from the available general design test and the already evaluated cycle kernel, with no new optimization or spectral invariant required. The explicit potential and elementary limits do not give a substantive independent remainder. This is mechanical application of known data, not a rejection for being a narrow exact result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
