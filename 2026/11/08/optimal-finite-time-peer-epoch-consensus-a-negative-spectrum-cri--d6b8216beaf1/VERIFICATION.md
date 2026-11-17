---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For irreducible reversible stochastic W the D^1/2 W D^-1/2 similarity is symmetric with stationary projection 1*pi^T. Derive finite peer epoch multiplier (1-alpha+alpha^(K+1)*mu^K*(1-mu))/(1-alpha*mu): denominator >0, for mu>=0 always positive; even K strictly positive for all mu; odd K exactly one possible negative root. Each epoch kills at most one distinct negative nonconstant eigenvalue, so generic initial vectors require at least their number of epochs, regardless of adaptive choices. K=1 and alpha=1/(1-mu) constructs the exact projection when all nonconstant eigenvalues are negative. Reversible nonedge implies principal 2x2 matrix diagonal and mu_2>=min W_uu,W_vv>=0 via interlacing; for simple regular graphs only complete graph qualifies. Independent three-state exact Fraction calculation annihilates two distinct negative eigenvalues and produces J/3. Strong statement is restricted to fixed W, shared scalar alpha in (0,1), finite K and anchor resetting; generic-input lower bound is not a uniform bound over every degenerate initial vector.

## originality

PASS

Wu/Abebe/Mendler-Dünner 2026 already derive finite FJ peer filter and their Theorem 4 treats equilibrium/asymptotic opinions. Kibangou 2012 Theorem 1 already constructs a Laplacian-eigenvalue factor product, hence the K=1 product by itself is not original. The additional necessity across all positive-susceptibility finite peer filters, even/odd horizon optimality, generic adaptive lower bound, reversible nonedge obstruction and topology classification survive these comparisons as a complete model-specific controllability theorem. Qualified by possible existing finite-factor consensus literature.

## value

PASS

Exact finite-time control is materially different from asymptotic convergence; showing a sharp obstacle for noncomplete support under a physically constrained common-susceptibility FJ protocol, and proving longer horizons never help, settles a natural protocol design question. It is not a general topological impossibility for arbitrary time-varying consensus matrices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
