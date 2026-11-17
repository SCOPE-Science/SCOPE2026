---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

For the iid scalar reflected update x[k+1]=x[k]-hU[k](2x[k]-x[k-1]), independently reconstructed the three-moment transfer K on (E x[k]^2,E x[k-1]^2,E x[k]x[k-1]); its polynomial determinant det(I-K)=h(2m-hv-3h^2mv). K is the restriction of a PSD-cone-preserving covariance map. Perturbation of the simple eigenvalue 1 at h=0 has slope -2m; its Perron spectral radius cannot cross 1 before the unique positive root, and det(I-K)<0 above that root gives a real eigenvalue >1. PSD spectral eigenvectors decompose into deterministic pair initializations, proving the quantifier, including equality/instability. For independent Bernoulli slopes 0 and 2m at h=1/(2m), symbol word 0,1,0 annihilates every augmented pair and gives P(T>3k)<=(7/8)^k; the exact second-moment recurrence S[n+1]=S[n]+S[n-1]/2 for initial (0,1) grows at root (1+sqrt3)/2 despite almost-sure finite hitting, whereas SGD risk is 2^-n. Read the full Fraction verifier; checked its exact enumerated conditions against the analytic derivation, but did not treat reported VERIFY_OK as a universal proof.

## originality

PASS

The known deterministic reflected-gradient h m<2/3 case is precisely v=m^2 and is excluded from new priority. The inspected full prior deterministic affine and finite-absorption findings do not imply the first-two-moment random-curvature frontier or finite-hit exploding-risk example for this one-oracle two-step scheme. Published stochastic reflected update sources are algorithmic background under distinct noise assumptions. Best-knowledge only: inaccessible full primary texts and general stochastic recurrence literature remain priority risks.

## value

PASS

A sharp necessary/sufficient stability frontier for the natural one-call stochastic reflected-gradient algorithm, dependent only on oracle mean/second moment and valid for every deterministic initial state, is a motivated rate-calibration fact. The explicit contrast between almost-sure exact finite hitting and exponentially divergent mean-square risk under the *same one-call oracle* reveals a nontrivial stability pitfall not explained by a routine scalar deterministic contraction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
