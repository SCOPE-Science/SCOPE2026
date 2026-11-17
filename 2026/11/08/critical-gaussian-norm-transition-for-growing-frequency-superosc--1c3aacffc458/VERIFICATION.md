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

From |cos theta+ia sin theta|^2=1+(a^2-1)sin^2 theta, rebuilt the exact Gaussian norm integral. For c<1 the e^{-(1-c)x^2} global majorant proves norm and TV limit. At c=1, x=n^{1/4}u yields quartic limit -u^4/2 and integrable upper bound; integral equals 2^{-3/4}Gamma(1/4)/sqrt(pi). For c>1, global comparison -y²+log(1+cy²) has precisely two maximizers ±sqrt((c-1)/c), I(c)=log c-1+1/c; independently expanded the O(1/n) exponent q(y)=-cy^4/[3(1+cy²)] giving claimed nontrivial prefactor and weak two-peak limit. All limits are for fixed c and do not imply uniform crossover.

## originality

PASS

Exact finite Gaussian-windowed superoscillation norm identities are known, but inspected Fock and STFT papers use fixed oscillation parameter and do not derive a_n^2-1=cn three-regime sharp global norms, quartic critical law, finite exponential prefactor and intensity measure bifurcation. Best-of-knowledge originality with residual older general Laplace-asymptotic risk.

## value

PASS

The natural global Gaussian Hilbert energy of an increasingly superoscillatory bandwidth-limited sequence has a sharp norm/measure transition and explicit critical constants. These resolve nontrivial changing-target asymptotics not mechanically implied by fixed-a finite-sum identities.

The dated certificate retains the supplied scientific assessment, sources and limitations.
