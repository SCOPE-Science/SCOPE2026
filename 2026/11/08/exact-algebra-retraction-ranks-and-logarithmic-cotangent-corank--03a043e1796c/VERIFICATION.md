---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-14.md",
      "INDEPENDENT_AUDIT_2026-11-14.json"
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

The corrected theorem explicitly starts with the earlier published exact Gaussian-binomial rank multiplicities. Write N_{n,n-s}=q^{Phi(s)} B_{n,s}, with Phi=(n-s)2^n+(2s-n)2^{n-s}-s and 1<=B<=C_q. Exact adjacent difference Phi(s+1)-Phi(s)=2^(n-s)(n/2+1-s-2^s)-1 is >=2^(n-1) below T-2 and <-2^(n-1) from T+2 onward for T=floor(log2 n), n>=64. Comparison of each tail weight to a window endpoint proves P(|S-T|<=2)>=1-(n+1)C_q q^(-2^(n-1)). Window exponent and bounded Gaussian factor prove total-count log asymptotic. This is an infinite proof using the prior finite rank theorem, not finite extrapolation.

## originality

PASS

The original exact all-rank enumerator and conjugacy classification are fully covered by the 2026-10-12 same-algebra published theorem; neither is a new contribution. The corrected final claim is specifically the quantitative asymptotic typical corank/logarithmic image-dimension law and uniform tail bound. The earlier primary full result gives the rank enumerator but no asymptotic concentration or total count. Best-of-knowledge O passes for the genuinely new probabilistic asymptotics; a general coefficient/saddle-point analysis elsewhere may cover them.

## value

PASS

A uniform random algebra retraction is natural in a finite algebra with exponentially many nilpotent monomials. The exact finite counts (previously known) do not themselves quantify typical image size: a five-index cotangent-corank window at log2 n and a superexponential tail give a genuine structural probability law and total-count entropy. Because image dimension is exponential in retained generators, this is a precise invariant another researcher could need. This value does not rest on rebranding a prior rank polynomial.

The dated certificate retains the supplied scientific assessment, sources and limitations.
