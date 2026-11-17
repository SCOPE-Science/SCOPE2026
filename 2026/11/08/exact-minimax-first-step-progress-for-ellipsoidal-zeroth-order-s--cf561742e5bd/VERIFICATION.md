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

The exact POEM-ES v2 Algorithm 1 uses r-scaled symmetric finite differences and Sigma^(-1/2) transformed normalized sphere directions, with first step eta0=1/||g0|| for r_epsilon=1. For f(x)=a·x on a radius-two disk, g0=2(a·Sigma^{1/2}v)Sigma^{-1/2}v and projection is inactive, hence the expected decrease is the signed angular integral in the package. The arcsinh and arcsin primitives reproduce the exact finite-delta formula including coordinate axes. Its minimizers are trapped at q between constants/sqrt(log(1/delta)) by positive-term bounds and a matching trial direction; uniform rescaling q=t/sqrt(L) gives limiting cost t/2+1/t and unique t=sqrt2, yielding m_delta~(2sqrt2/pi)sqrt(delta L). Independently evaluated the exact formula against direct 2pi-angle numerical quadrature at five pairs and checked decreasing-delta minimizers; these tests do not replace the uniform asymptotic argument.

## originality

PASS

Full primary arXiv HTML v2 Algorithm 1 and theoretical Sections 4/5 were independently inspected: the original establishes general variance and convergence bounds involving kappa, not the exact signed normalized first update on linear objectives nor its minimizing slope and sharp asymptotic coefficient. An older sign-Gaussian/minimax result could be relevant, and this residual risk is explicit.

## value

PASS

The normalized single-step progress under anisotropic zeroth-order sampling is a natural algorithmic invariant: this exact minimax quantifies a genuine loss and identifies a counterintuitive moving worst-slope direction with sharp logarithmic correction. The analysis does not claim later-iteration rate or paper-sized algorithmic improvement, but the precise worst-angle diagnostic can guide understanding of preconditioner conditioning.

The dated certificate retains the supplied scientific assessment, sources and limitations.
