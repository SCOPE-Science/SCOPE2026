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

The model uses uniform recurrent states of each graph separately; stationary grain addition is a recurrent-group permutation, so E T=L^{-1}e_1 and total E M=1^TL^{-1}e_1. On C_n with sink 0, the Dirichlet path Green G_ab=min(a,b)(n-max(a,b))/n solves the difference equations with zero boundary; u_a=a(n-a)/2, so M(C_n)=(n-1)/2. A nonsink chord changes L to L+bb^T, b=e_i-e_j; Sherman–Morrison gives ΔM= -(L^{-1}b)_1 (b^Tu)/(1+b^TL^{-1}b). Verified (L^{-1}b)_1=d/n, b^Tu=-d(n-i-j)/2, and b^TL^{-1}b=d(n-d)/n, proving exactly ΔM=d²(n-i-j)/(2[n+d(n-d)]). All denominators positive and d≥2. The n=4 only chord {1,3} is neutral; n=5 {1,3} gives +2/11. For incident chord k=1+d, 2≤d≤n-3, 0<d²(n-d-2)/((n-1)(n+d(n-d)))<1 (both factors strictly smaller than their denominator bounds), proving 1<Mnew/Mold<2; taking k=n-floor(sqrt n) yields d/n→1 and (n-d)/sqrt n→1 so ratio→2. Independently written exact rational grounded-Laplacian solver tested every 165 valid chord through n=12, and independent burning/recurrent-state stabilizations for all 20 chords through n=7 reproduced the exact means and counts. Four n up to 10^6 show ratio convergence, not an infinite proof. Original repository checker was separately source-inspected; its claimed 120/20 cases are consistent with independent checks. This is an exact first-moment proof, not avalanche area/distribution stochastic dominance.

## originality

PASS

Best-of-knowledge PASS for the evaluated all-chord sign boundary n-i-j and the sharp incident-chord near-doubling phenomenon on a natural infinite cycle family, NOT for stationarity, Dhar Green identity, cycle Dirichlet inverse, Sherman–Morrison or generic edge-update formulas. Compared full corresponding public tree-edge-addition result, primary cycle avalanche polynomials and cactus/separable graph literature, and a normalized-spectral-gap Braess paper; hypotheses and observables do not dominate the submitted conclusion. Resultary indexes a publication of the same record 407b2e004342, which is the research subject/mirror and is not independent earlier coverage. Strong residual risk: the formula follows with elementary algebra from classic tools, so unindexed earlier chorded-cycle specialization may exist; semantic searches and literature reading do not certify priority.

## value

PASS

A structurally natural dynamical observable (stationary total toppling work after a fixed source addition) responds unexpectedly to an added edge. The exact two-endpoint criterion i+j<n,=n,>n partitions all permissible nonsink chords into increased, neutral and decreased mean and identifies the sharp threshold using actual graph positions, not an arbitrary computational slice. The smallest strict example at n=5 and an incident-chord family with finite ratio below two but asymptotic limit two reveal a motivated sharp magnitude boundary. This nontrivial infinite family classification may be used to check intuitions about avalanche activity and link augmentation despite relying on familiar linear-algebra tools. It neither claims novelty for Sherman–Morrison nor general stochastic dominance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
