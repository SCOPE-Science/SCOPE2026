---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The exponential Hermite generating function gives the even series (1+u)^(-1/2) exp(ux²/[2(1+u)]); this also follows from the explicit Hermite coefficients of x^(2k). The diagonal Mehler series at x/sqrt(2) has the same exponential and prefactor (1-u²)^(-1/2). Multiply it with u=gamma*t by sqrt(1-gamma*t)/(1-t) and extract t^m. This verifies the coefficient identity formally, with no restriction on gamma, including m=0. The representation has nonnegative weights on [0,1]; outside this interval the identity is a linear combination of squares, not a positivity certificate. All nonconstant coefficients of a_m as a polynomial in gamma are negative, so a_m(gamma)>=a_m(1)=[t^m](1-t)^(-1/2)=binom(2m,m)/4^m. Negative gamma fails with m=1 and large |x|. At x=0 and gamma>1, divide by (-gamma)^m c_m with c_m=binom(2m,m)/4^m. Each fixed reverse-index ratio c_(m-r)/c_m tends to 1; for r<=m/2 the ratio is uniformly bounded, and for r>m/2 the omitted sum is O(sqrt(m)*gamma^(-m/2)). The limit gamma/(1+gamma)>0 gives a genuinely negative value for all sufficiently large odd m. Equation (2.11) of the quadrature paper has this partial sum and strictly positive other factors: the classical Gaussian weights, normalization and exponential. The usual scale has finite length ell>0 and 0<gamma<1. This establishes only the Mercer-truncated approximate weights. Independently ran `python audit_checks/independent_replays.py 1`: exact coefficient comparisons of the formal Hermite/Mehler product through degree 24 in u, the central-binomial bounds, and exact negative witness m=393 at gamma=101/100. This is a finite corroboration, not the proof; submitted code was inspected, not executed.

## originality

PASS

The positive-prefactor approximate weight formula and its positivity question are prior; so are the underlying Hermite generating functions. The supported distinct claim is the explicit finite square certificate and exact all-m, all-x interval (including the failure mechanisms outside it), and their use to prove approximate weight positivity. No covering theorem for this combination was found in the retrieved evidence. This does not assert absolute priority or a theorem for exact kernel-system weights.

## value

PASS

A positivity certificate for weights in a specified practical quadrature approximation resolves a motivated sign question that node sampling cannot settle. The same identity gives a uniform-in-x lower bound and a sharp all-degree real parameter classification with explicit qualitatively different obstruction on each side. It does not promise conditioning improvements, exact-kernel weights, or error rates.

The dated certificate retains the supplied scientific assessment, sources and limitations.
