---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For OU drift gamma and noise D with Poisson jumps X->qX at rate r, fixed q∈[0,1), the stationary conditional variance sigma²V has deficit U=1-V distributed as A(1-q²V'), A~Beta(alpha,1), alpha=r/(2gamma). Thus P(U<=u)=u^alpha B for 0<u<1-q², B=E[(1-q²V)^-alpha]. The variance-process generator gives m_k=prod_{j<=k} j/[j+alpha(1-q^(2j))], and binomial expansion yields its convergent coefficient series. Gaussian scale mixture with an endpoint Laplace argument establishes p_q(x)~Gamma(alpha+1)(2sigma²)^alpha B |x|^-2alpha exp(-x²/(2sigma²))/sqrt(2pi sigma²). Coupling Poisson histories yields strict B increase in q and divergence q→1; q=0 gives B=1. Independently recomputed first 12 exact rational moments and positive series partial sums at q=0,1/2,3/4; the analytic proof, not those finite sums, establishes exact edge and all-parameter asymptotic.

## originality

FAIL

DECISIVE STRONGER SAME-MODEL COVERAGE. The 2026-11-02 published full RESULT.md Exact endpoint law and sharp Gaussian tails for partially reset Ornstein–Uhlenbeck diffusion already establishes the identical invariant position OU+Poisson contraction model for every c∈(0,1): exact endpoint law P(vstar-V<=w)=C w^alpha, identical convergent coefficient, identical sharp Gaussian density tail and additional right survival/critical Gaussian-square exponential moment threshold. With sigma²=vstar and C=(sigma²)^(-alpha) B, the earlier p(x) prefactor is algebraically identical. Extra submitted q=0 limit, monotonic prefactor and q→1 divergence are elementary consequences of that earlier endpoint coefficient and coupling, not a distinct new model or theorem.

## value

FAIL

The sharp OU Gaussian-tail and variance-deficit identity are intrinsically meaningful rare-event results, but their exact formula and main physical interpretation are already established in published prior work, which further proves stronger tail and moment boundaries. Repeating them plus easy amplitude-boundary consequences does not constitute a new motivated invariant; value as an original finding fails despite mathematical correctness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
