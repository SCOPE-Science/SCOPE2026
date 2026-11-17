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

From independent Bernoulli state matrices and conditional E[e_new|history]=0, c_k=E[x_ke_k]=E[e_k^2] for k>=1. Reconstructed the exact 2x2 covariance recursion N with entries 1-2h+h^2/p, (1+2h)/p-2, (1-p)h^2/p, (1-p)(1+2h)/p; verified determinant (1-p)(1-2h^2)/p, trace and three Jury expressions. The only binding Jury inequality is h[4p-2-(3-2p)h]/p>0. When it fails for 0<p<1, N has strictly positive entries in the excluded region and a positive nonzero residual-free first-step moment vector; Perron-Frobenius prevents x mean square from vanishing. p=1 reduces to deterministic gradient descent, 0<h<2. Memoryless baseline has multiplier 1-2h+h^2/p, stability 0<h<2p. Endpoints included as non-convergent, not inferred from finite tests.

## originality

PASS

No retrieved earlier theorem for the all-probability fixed-step unbiased 1/p-amplified Bernoulli EF frontier; an earlier exact Bernoulli EF study treats the distinct biased unscaled compressor with a renewal/residual-reset law, which cannot be transferred by renormalizing h. General unbiased-compression comparisons and Lyapunov rates do not yield this precise simultaneous half-retention obstruction. Best-of-knowledge PASS, not priority certification.

## value

PASS

The exact p=1/2 stability wall is a motivated qualitative failure of classical error feedback relative to no-memory compression with exactly the same unbiased compressor, with an explicit sharp all-p step-size diagram. The result is a structural counterexample to an intuitive advantage of feedback; it is neither a tiny numerical gain nor a formal parameter renaming.

The dated certificate retains the supplied scientific assessment, sources and limitations.
