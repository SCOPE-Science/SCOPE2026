---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Condition on the earliest of (q+1)n vertices. If it is one of q leaves, it blocks its spine vertex and ensures q leaves selected in that cell, separating subpaths of lengths i-1,n-i. If the spine vertex is first, it contributes 1 and forces q leaves of each existing adjacent cell, leaving lengths max(i-2,0),max(n-i-1,0). Summing yields the claimed Riccati coefficients and base n=1,2. Identity X=qn-(q-1)K for accepted spine count K gives support 0<=K<=ceil(n/2), with strictly positive cell-priority constructions for each K, and P(K=0)=(q/(q+1))^n. The one-sided acceptance integral yields exponential partial sums and exactly the displayed mean; extending the entire exponential series gives its factorial remainder. Independently recomputed exact arbitrary-graph recursive priority laws for (n,q)=(1,2),(2,2),(3,2),(2,3), all matching the first-cell formula.

## originality

PASS

The primary Krivelevich–Mészáros–Michaeli–Shikhelman full open-access article gives general local limits, ordinary path expectation and tree inequalities but not an evaluated all-n,q probability-generating law for this vertex-greedy leaf-decorated path. Penrose–Sudbury gives broad RSA forward equations. A same-day published decorated-PATH MATCHING law instead orders edges and is explicitly a different random variable/process. The exact distribution and support are distinct from universal first-step recurrences and local-mean results.

## value

PASS

PASS: Greedy MIS on regularly leaf-decorated paths is a natural random sequential adsorption family. Its exact all-finite distribution, constrained support and explicit boundary mean identify useful information not determined by just the asymptotic occupation density. The full support is structurally nontrivial for q>=2, and the family covers every spine length.

The dated certificate retains the supplied scientific assessment, sources and limitations.
