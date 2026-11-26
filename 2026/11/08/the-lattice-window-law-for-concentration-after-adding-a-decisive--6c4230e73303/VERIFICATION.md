---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Reconstructed the strict insertion test: adding the absent pair changes S=sum d_i^2 by 2(D+1) and m to m+1, so increase is equivalent (m>0) to D>1+2W/m+1/m+W/m^2. D is Binomial(2n-4,p_n) after conditioning; W/m tends to c. Expanding W-cm in centered edge indicators gives orthogonal linear and quadratic parts, with variance/n tending to c^3/2+c^2/2 and mean/sqrt(n) to c beta/2. For each fixed cumulant of order j>=3, only edge-overlap-connected motif tuples survive; each union has e>=v-1 and joint-cumulant bound O(p_n^e) by the partition formula, giving O(n) in total. This establishes the stated normal limit by moments. Deleting the two endpoints costs O_P(1) edges and O_P(1) wedges (the wedge expectation is bounded), and leaves a background independent of D. On the sole critical atom D=2c+1 the inequality is W-cm<-(m+W)/(2m); the scaled correction tends to zero, and the continuous Gaussian sign test gives Phi(-beta/sqrt(2(1+c))). The Poisson atom counts, beta=0 midpoint and c=1 values agree. The m=0 convention has vanishing weight. The bundled checker.py was inspected, not executed; the cumulant proof, not its finite/simulation checks, establishes the limit.

## originality

PASS

Passes on the exact sparse one-pair insertion law, in particular the atom-weighted Gaussian transition; not on the index, the graph-game encoding, or a general subgraph central limit theorem. No distinct inspected prior statement covers the insertion comparison and its critical window.

## value

PASS

The result quantifies a natural sensitivity of a voting power index to an added decisive partnership. The one local degree sum has a discrete limit while the global concentration threshold has a continuous fluctuation; resolving their interaction gives discontinuities and a precise critical window not supplied by first-order approximations or by the separate marginal limits.

The dated certificate retains the supplied scientific assessment, sources and limitations.
