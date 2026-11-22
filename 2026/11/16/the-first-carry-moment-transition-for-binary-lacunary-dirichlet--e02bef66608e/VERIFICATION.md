---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

Fourier Parseval turns moments into weighted equal base-b signed-digit sums. Integer carries obey b u_{j+1}=u_j+k_j-l_j with zero endpoints. For r<b no nonzero carry can arise, so sum binomial(r,k)^2=binomial(2r,r) factors. At r=b, reachable integer carries restricted to {-1,0,1}; exact T rows [[a,K,0],[1,C,1],[0,K,a]] by Vandermonde, with central-state symmetric 2x2 characteristic (λ-C)(λ-a)-2K. Cayley-Hamilton yields the recurrence for all b,n; λ-=positive because a C>2K, λ-<C<λ+, both spectral coefficients positive, and explicit 2-step nonzero carry loops give E(n)>C^n for n≥2. Independent direct convolution b=2..6, n≤3 and source checker code verified critical figures.

## originality

PASS

Lacunary Riesz-product/Dirichlet kernel identities and carry transfer matrices are classical, but the checked Tang–Wu work treats singular Cantor-measure maximal convergence rather than Haar even moments, and Diaconis–Fulman/Holte treat probabilistic unconstrained carries with different transition probabilities. The exact universal first-carry 2-state closed form and λ+ were not identified as direct prior corollaries; classical general carry-automaton technology can generate it, so priority uncertainty is explicit.

## value

PASS

The threshold r=b is the intrinsic first nontrivial arithmetic collision for a binary digit spectral set. Closed all-base critical moment growth is a natural Riesz-product/lacunary energy invariant and quantitatively separates independent and carry-correlated moments; precise law may be used in Fourier norm estimates.

The dated certificate retains the supplied scientific assessment, sources and limitations.
