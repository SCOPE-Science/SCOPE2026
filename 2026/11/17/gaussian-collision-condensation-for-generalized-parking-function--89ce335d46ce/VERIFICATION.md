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

The actual Bayer et al. vertex theorem gives orbits of permutations of k ones followed by increasing S_{k+1},...,S_n (S_i=cumulative b_i), with k=0/1 identified exactly when b1=1. For any generic Gaussian cost vector, signs determine k and the positive cost ranks order the nonunit values; a rank-j vertex has mass 2^-n/j! and multiplicity (n)_j if b1>1. For b1=1, n! formerly separate rank-n/-n-1 vertices collapse into n! rank-(n-1) vertices, mass (n+1)/(2^n n!). Raising those masses to rth powers proves 2^{nr}C=Σ(n)_j/(j!)^r plus the exceptional correction [(n+1)^r-n^r-1]/(n!)^{r-1}, for every fixed r>=2, n>=2, positive b. This finite spectrum/moments are explicitly admitted prior. Let x=n^{1/r}; weights n^j/(j!)^r concentrate at j=x+O(sqrt x); Stirling local expansion gives e^{rx}/[sqrt r(2πx)^((r-1)/2)] and a normal rank (J-x)/sqrt x=>N(0,1/r). Falling factorial ratio (n)_j/n^j yields e^-1/2 precisely at r=2 and 1 for fixed r>=3, while its change on the central Gaussian window is o(1); exceptional b1=1 correction is negligible by factorial comparison, uniformly over b(n). Independently reconstructed exact small-n finite moment identities for n=3,4,5, r=2,3,4. The checked source verify.py enumerates finite sign/rank chambers; infinite fixed-r asymptotic assessed analytically.

## originality

PASS

Best-of-knowledge, excluding the completely covered finite cone census and exact collision moments: the new final claim survives only on the sharp all-fixed-r saddle constants (especially r=2 e^-1/2) and the conditional Gaussian collision-rank collapse at n^(1/r). Primary Bayer/Behrend and published exact partial-permutohedron normal-cone theorem provide inputs but not these asymptotic conclusions. Related complete-bipartite/star zonotope Rényi results concern different fans and parameter scalings.

## value

PASS

Simultaneous independent Gaussian support objectives selecting a common vertex is a natural collision/Rényi statistic; the precise conditional rank n^(1/r) and r-dependent correction reveal an uncommon rare-event condensation relative to the ordinary Binomial(n,1/2) exposed rank. These exact asymptotic constants and Gaussian fluctuations can be needed in angular probability and high-dimensional polytope comparisons. Their value is not the known normal-cone table or a renamed Laguerre identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
