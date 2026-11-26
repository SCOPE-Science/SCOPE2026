---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

A connected allocation exists and the budget binds by homogeneity. The simple graph makes the grounded-Laplacian map injective; the logdet second derivative is minus a squared Frobenius norm, so uniqueness forces the two edge-orbit weights without imposing symmetry. The nonzero even Fourier modes contribute m^2 a^(m-1), the odd modes 2 a^m[T_m(1+t)+1], and dividing by 2m gives the tree formula. The log objective is strictly concave in b along the budget line; the increasing t reparameterization preserves derivative signs. At the cycle boundary the derivative in t is [m^2-(2m-1)q]/2, including unique deletion at equality. As t goes to infinity the design disconnects. For fixed q the stationarity equation bounds t above, and t cannot tend to zero: tanh(m u/2)/sinh(u) then grows at least at order min(m,1/u), where u=arcosh(1+t), against a bounded right-hand side. The positive-root limiting quadratic agrees with the formula. At t=s^2/(2m^2) the scaled derivative tends to tanh(s/2)/s-alpha, supplying the stated brackets including the zero scaled limit at alpha=1/2, where exact eventual deletion is not asserted. Inspected RESULT.md, VERIFICATION.md and verify.py; the reported 815 finite checks are supplementary and were not rerun.

## originality

FAIL

An earlier indexed theorem on the very same simple Möbius ladders states the same exact weighted tree polynomial, threshold, unique unrestricted optimizer, and both limiting laws on a strictly larger size range. It also gives an asymptotic tree gain not claimed here. The failure rests on exact prior coverage, not on the fact that standard KKT conditions are applicable or on an inaccessible source.

## value

FAIL

The price-screening and scaling questions are well motivated, but this record repeats the complete known solution and omits some cases and a gain asymptotic already covered. Its independent derivation and finite checks add no distinct invariant, boundary regime, or mathematical use beyond the earlier exact classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
