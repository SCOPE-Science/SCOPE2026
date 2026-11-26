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

The radial derivative on each prescribed circle is zero and the angular speed is a+b cos θ with a>|b| and a²−b²=ω². One turn is therefore exactly one least physical period. Linearization of dr/dθ has numerator 2Kr_iF′(s_i)cos θ and no angular-denominator derivative term because F(s_i)=0. The quotient's cosine integral is −T_i w_i, giving the exact log multiplier. Choosing K above the finite maximum puts all w_i in (−1,1); the two degree-(m−1) interpolants impose their values independently. The x-component on y=0 proves degree 2m, including m=1. For the lower bound, division in y by y²+x²−s_i and evaluation on the two open semicircles gives zero remainder. The relatively prime factors together divide xP+yQ. At degree below 2m the quotient is constant, and the origin forces it to vanish. In that case radius is a first integral and regularity of a designated orbit gives an annulus of regular periodic circles, excluding hyperbolicity. Independent Cartesian ODE integration and divergence accumulation reproduced periods 2, 3.7, 1.5 and multipliers 0.66, 0.85, 1.55 on three radii, including two adjacent attracting circles. Replay: python3 branches/independent_checks.py 5 (NumPy/SciPy).

## originality

FAIL

A distinct indexed result states the same optimal-degree simultaneous numerical period and multiplier prescription for m≥2, with the same extra-orbit scope. Its explicit construction is exactly the frozen one conjugated by (x,y)↦(x,−y); its parameters agree after ω_i=2π/T_i. The proof also applies verbatim to m=1 (constant interpolants and a single divisor), with no separate new ingredient. This is equivalent coverage as reviewed; the date shown for the comparison is later and is not evidence that it preceded the frozen result or of historical priority. Unavailable older full texts do not determine the decision.

## value

FAIL

Independent control of prescribed physical times and quantitative hyperbolicity at minimal degree addresses a genuine realization problem. But the compared theorem supplies that exact control by the conjugate field and the same lower bound. The lone m=1 extension is substitution into the already available proof and has no separately motivated mathematical gap to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
