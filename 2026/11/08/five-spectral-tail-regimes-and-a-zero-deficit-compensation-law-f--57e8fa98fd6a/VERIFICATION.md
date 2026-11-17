---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

For all beta,kappa>0 and Gaussian STFT normalization g(t)=2^(1/4)exp(-pi*t^2), rederived rho=1+(log I)''/(4pi)=4pi Var_P(X)=m'(R). The mean-transport integral gives ∫_0^R(rho-1)=m(R)-R. The beta<1 saddle implies this tends to zero; for beta=1 the exact half-line Gaussian-erfc expression yields the exponentially small coefficient and finite deficit kappa/(4pi); for 1<beta<2 the concave/convex local potential yields the R^(beta-2) correction; beta=2 is Gaussian conjugacy; beta>2 uses saddle a_R~(4pi R/(kappa beta))^(1/(beta-1)) and precision kappa beta(beta-1)a_R^(beta-2). These establish the full pointwise five-case theorem, not just numerical samples. Differentiations of an exponentially tiny erfc remainder require care, addressed via exact erfc formula. No uniform beta-boundary asymptotic asserted.

## originality

PASS

Foundational first-intensity formula is exactly Escudero–Koliander–Romero Theorem 1.1/equation (4.1), and Gaussian beta=2 constant is already their Proposition 1.3. Their inspected asymptotic theorem states general bounds rather than the five sharp stretched-exponential constants, strict overshoot and compensated improper integral. Related exact ambiguity-orbit theorem classifies inverse intensity fibers, not this forward family of limits. Thus the surviving five-case and compensation statements are not visibly covered, subject to uninspected specialist tail work.

## value

PASS

Sharp five-regime scaling including the nontrivial beta=1 exponentially small cusp and exact global overshoot compensation distinguishes long-tail spectral behavior of a natural Gaussian STFT zero process. These may matter for interpreting frequency-dependent zero-intensity biases. This is more than a known Gaussian baseline; model and limits are explicit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
