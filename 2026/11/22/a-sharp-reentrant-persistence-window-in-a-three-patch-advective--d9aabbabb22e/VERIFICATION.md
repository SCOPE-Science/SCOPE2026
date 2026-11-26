---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Reconstructed RESULT.md Proof 1–4. The movement matrix is conservative and irreducible for d>0, so −M=dD+qQ−aI is Hurwitz Metzler and M^−1 is strictly positive. At r=1/(M^−1)₁₁ the vector M^−1e₁ is a strictly positive null vector, explicitly identifying the zero as the Perron root, rather than just some eigenvalue; Perron monotonicity then gives the exact sign for all r. Expanding the determinant and cofactor gives R=aN/H as displayed. The derivative has the sign of a²(a+q)+2(a+q)(2a−q)d+(5a−3q)d². For q≤5a/3 it is strictly positive on d>0, including equality in the ratio. Above that ratio its roots have opposite signs, giving a single strict maximum greater than both limiting values a+q and 3a. Exactly the birth rates strictly between their larger value and the maximum give two distinct positive thresholds. For λ=s(A)≤0, the positive weighted sum satisfies U′≤λU−cU², proving extinction even at the two neutral thresholds. When λ>0, small positive Perron multiples and a large constant vector give sub-/supersolutions; strict quadratic scaling and the Metzler off-diagonal sign give uniqueness. Multiples of the equilibrium scaled by lower/upper scalar logistic solutions squeeze every eventually positive trajectory to it. The analogous two-patch derivative a(a−q)/(a+d)² has fixed sign or is identically zero. The example (a,q,r)=(1,2,25/8) reduces to the exact quadratic −d²+5d−3 for the sign of R−r. Scope is fixed q, d>0 and the stated deterministic homogeneous mortality/crowding with upstream-only births, not changing the common multiplier of both movement terms. Inspected VERIFICATION.md and the finite identity checker, not executed.

## originality

PASS

The conservative stream geometry and Perron-to-persistence method are prior. The supported distinction is the sharp reentrant window, with the exact drift-to-mortality boundary and minimal patch count, when diffusion alone varies and reproduction is confined upstream. Retrieved antecedents do not imply that classification.

## value

PASS

Demonstrates with an explicit sharp threshold that varying symmetric migration at fixed downstream transport can change deterministic persistence twice without adding sites of reproduction, changing mortality, or opening the corridor. The rank-one structure gives an exact birth-rate range, not just an example where a simulated spectral curve is nonmonotone; the two-patch obstruction isolates the minimal geometry. This is a model mechanism and not an ecological management conclusion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
