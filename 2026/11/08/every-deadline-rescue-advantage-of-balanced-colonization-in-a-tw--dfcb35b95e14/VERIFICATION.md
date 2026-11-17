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

Exact transient generator Q=[[-a-b,b,a],[c,-a-c,0],[d,0,-b-d]], exits r=(0,a,b). Its absorption-time Laplace transform is N(z)/D_q(z), with N=ab(a+b+C+2z) and D=z^3+[2(a+b)+C]z^2+[(a+b)^2+ab+(a+b)C+q]z+ab(a+b+C); the law depends only on q. For positive c,d, Q is self-adjoint in positive weights (1,b/c,a/d), and -Q has strictly positive Dirichlet form, so D=prod(z+lambda_j) with positive lambda_j. Differentiate survival transform at fixed C: partial_q Uhat=N/D^2=F_q(z)/D; both factors invert to positive absorption density and a strictly positive convolution of three decaying exponentials. Laplace uniqueness gives partial_q U(t)>0 for each t>0; continuity includes q=0 and q=C²/4 endpoints. Taylor expansion of e11^T exp(Qt)r produces first allocation-sensitive term t^4 ab*q/12 in survival differences. Starting from a singleton has different behavior, and is excluded. Independently verified determinant, rational transform and the derivative of fourth-order coefficient symbolically with SymPy.

## originality

PASS

The Oct18 same-model published theorem already gives the exact transform, allocation-product symmetry, a strict Laplace-transform order, and mean/variance optimality. That result explicitly warns that it does NOT assert first-order stochastic dominance: ordering Laplace transforms for all z>0 does not in general imply P(T>t) ordering for every fixed t. The new strictly-positive time-domain convolution argument supplies the stronger all-deadline usual stochastic ordering and fourth-order onset. Ecological simulation and mean-management sources are still weaker or distinct.

## value

PASS

Exact fixed-time survival is the natural risk metric when conservation deadlines matter; maximizing mean or every exponential-time transform does not settle fixed positive deadlines. A strictly positive time-domain convolution proof gives an all-t strengthening for heterogeneous mortality, and the fourth-order onset identifies why short-time and mean-only comparisons miss the effect.

The dated certificate retains the supplied scientific assessment, sources and limitations.
