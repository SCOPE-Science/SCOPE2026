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

Reconstructed on the real BV quotient by constants with normalized Haar L². The two Jordan parts of Df have equal mass V(f)/2; their normalized product coupling integrates ordered dipoles δ_s−δ_t, whose periodic primitives are the oriented arc indicators. The integral of their images under E=I−A_a is a bounded L² integral and its mean norm gives the arc upper bound; dividing the attained arc energy by V(1_I)²=4 gives sharpness. Independently, the overlapping lengths of an arc d≤1/2 with shift h∈[0,1] are (d−h)_+ and (d+h−1)_+. Expansion of the residual energy gives −2/a times the integral of the overlap plus 2/a² times the integral against (a−h), leaving a single −2h/a² weight. The two weighted integrals are dp³/p·(1/2)−p³/3 (i.e. dp²/2−p³/3, p=min(a,d)) and ae²/2−e³/6, e=(a+d−1)_+. For a≤1/2 the derivative of the energy at d<a is 1−d²/a² and the energy for d≥a is 2a/3; complements extend the maximizing lengths to [a,1−a]. For a>1/2 before d=1−a the same strict increase holds, and after that, a² times the derivative is a²−d²−2ae+e²=1−2d, using a+(1−a)=1. Thus only d=1/2 maximizes, yielding the stated polynomial branch. The two formulas meet at a=1/2 with value 1/12; a=1 gives mean subtraction and sharp value 1/16. For equality, the Hilbert variance identity forces almost surely one common residual vector and maximal length. Each nonzero Fourier mode of A_a has multiplier of modulus strictly below one (a positive-length average of nonconstant unit phases), so equal residuals imply equal ordered derivative dipoles. That determines both endpoints, including the semicircle case, so both Jordan laws are point masses. Differentiating the second squared norm gives (1−4a³)/(24a³) and unique maximum at 4^(−1/3), value (1−4^(−1/3))/4. All scope restrictions are necessary for this audit; centered windows change the phase of the multiplier. The auxiliary checker was inspected as finite evidence, not executed.

## originality

PASS

Best of knowledge, for the explicit forward-boxcar norm, exact all-width maximizers and equality classification. The general diameter reduction for an operator applied to zero-mass signed derivatives is not new; the nontrivial comparison is the subsequent maximization of the forward-boxcar residual with periodic wraparound. The closest classical sharp periodic averaging paper inspected measures a modulus of smoothness and uses modified centered kernels, not the real-TV residual norm.

## value

PASS

Forward moving averaging is a canonical approximation operator and the TV constraint is natural for jump signals. The exact optimal error for every width, the collapse of the family of maximizing arcs to one separation, and the strict interior worst width are structural, not a single sampled improvement. The equality classification makes the result usable as a sharp benchmark and exposes when nonmonotonic sharp error can occur.

The dated certificate retains the supplied scientific assessment, sources and limitations.
