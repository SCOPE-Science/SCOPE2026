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

Every actual majority flip strictly reduces the number of disagreeing edges, and only all-zero and all-one fixed points exist, proving a.s. absorption. With both hubs one, if j>=floor(s/2) they are stable; otherwise the competition among s-j eligible zero-leaves and the two unstable hubs has successive probabilities (s-j-i)/(s-j-i+2), giving the telescoping Φ_s(j). With opposed hubs, leaves remain tied and the first effective hub flip determines consensus by whether 2j<s,=s,>s; when equality both hub clocks are equally likely. Complementation handles zero hubs. The K_2,s threshold is ceil(s/2), so odd s changes the exact product by (s+3)/((s+1)(s+2)), even s zero. Independently solved exact rational count-state recurrences for 176 macrostates at small s, matching all kernel cases. This finite check supports but is not the all-s proof.

## originality

PASS

PASS: the same-graph Resultary record of November 8 studies synchronous independently random tie-breaking, and its oscillatory two-cycles are not the asynchronous tie-retaining process. The earlier Auletta et al. social majority paper studies existence of adversarial update sequences and graph robustness, not the exact distribution under uniformly random sequential updates. Neither implies the complete triangular-book kernel or parity-one-edge contrast. Historical unindexed special-network calculations remain a risk.

## value

PASS

Exact conditional absorption probabilities from all configurations of a natural minimally nonbipartite majority graph, including a sharp paradoxical two-hub minority winning probability and an explicit one-edge odd/even sensitivity; useful model-specific structural reliability law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
