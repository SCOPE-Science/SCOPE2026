---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The frozen RESULT.md spectral decomposition gives eigenvalues 0 (constants), N (block means), and N-n_i (within-block zero-sum). Subtracting two rows across endpoint parts of sizes a>=b gives explicit four signed mass classes. The proposed cost-one cross-part shipments and cost-two within-part shipment achieve P+R, and potential taking +1 at u, -1 on its own remaining part, 0 elsewhere matches the cost by duality; edge W1=e^-Nt[1+2(a-1)(e^{at}-1)/a]. Maximize over edges to obtain dependence only on largest part. Differentiation gives threshold 2M<=N+2, peak time and asymptotics, including singleton endpoints. Independently solved 100 bounded graph-row transport linear programs across seven multipartite profiles and two times, matching edge formula. Thus C PASS; mathematical rejection is wholly prior coverage.

## originality

FAIL

FAIL because exact stronger published same-model result dated 2026-11-02 already gives the complete ALL-pairs W1 formula for every complete multipartite graph with r>=3, identical largest-part operator norm, exact peak, nonexpansivity threshold and unattained 2 envelope; its full RESULT.md was read. The submitted r=2 extension is already published in the exact 2026-10-26 complete-bipartite Lipschitz theorem (entire RESULT.md inspected) and has the identical two-exponential formula. Its new macroscopic alpha peak display follows by substituting the prior closed-form peak and taking N->infinity: not independent substantive novelty. No new intact final claim survives.

## value

FAIL

FAIL as a new contribution: despite an important useful invariant, the submitted exact norm, threshold and heat-row transport are established in a stronger prior result, and the remaining asymptotic alpha display is a direct limit of its published peak formula. Correctness and finite re-verification do not make a recomputation of the known profile valuable as independent research.

The dated certificate retains the supplied scientific assessment, sources and limitations.
