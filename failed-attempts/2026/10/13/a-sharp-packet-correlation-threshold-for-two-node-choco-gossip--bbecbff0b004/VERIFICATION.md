---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

FAIL

The submitted proof is internally algebraically consistent for its explicitly written update, and independent SymPy checks confirmed the 4x4 second-moment matrix, rational generating function, Lyapunov identity and critical pole. But source Algorithm 1 in Koloskova–Stich–Jaggi updates x using the OLD cache, then computes q=Q(x^{t+1}-hatx^t), then updates the cache. The submission instead updates the cache first using x^t, and x then uses the NEW cache. For initial caches zero and d0!=0, the published algorithm necessarily has d1=d0 with E[d1²]=d0² at every q. The submitted recurrence predicts E[d1²]=(1/4+q/2)d0², e.g. 3d0²/8 at independent masks q=1/4, a direct counterexample to faithful application. Reconstructed original source transfer matrix is different. This material model mismatch makes the source-specific final claim incorrect as submitted; no complete corrected RESULT/PROOF package was supplied, so do not mark repaired. The q threshold may happen to coincide for a separate actual-model computation, but this does not validate the submitted proof.

## originality

PASS

The exact spectral moment phase for the explicitly defined cache-first variant is not matched by the Resultary search or by the original small-gain theorem; other dependent-gossip papers treat different memoryless updates. However it cannot be presented as a proved new phase for the published CHOCO method because the source recurrence is different, independent of whether the numerical boundary happens to agree. Originality remains conditional on defining a genuinely distinct model and its scientific motivation; no novelty claim on the source algorithm survives the original form. The original algorithm first updates nodes from old caches while audited model first changes caches; the source cannot imply the submitted moment formula. A similar threshold in the true algorithm cannot retroactively verify that formula.

## value

PASS

The mathematics of correlated Bernoulli packet masks with identical marginals governing mean-square consensus is naturally motivated and a sharp q=1/3 threshold is informative for the specified cache-first variant. That potential value does not cure the incorrect identification of the algorithm or authorize accepting its submitted source-specific result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
