---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

At fixed 0<ε<1 an active edge contributes ε(p_i+p_j)/(4m) to the degree-weighted mass drift, regardless of the orientation of its disagreement. Every copying rate on a discordant edge is strictly positive; a spanning-tree sequence to consensus and the finiteness of the state space give a finite mean absorption time. Stopping the bounded degree mass gives the stated occupation correction, and the fixation probability is harmonic. Testing singleton plus sets shows that a nonzero same-preference drift cannot cancel there. For arbitrary signed linear weights, the singleton plus and singleton minus equations add to the unbiased walk equation for r_i=w_i/d_i: r_i is the average of its neighbors. The connected-graph maximum principle forces a constant r_i, without a positivity assumption. Thus an arbitrary nonzero linear martingale is exactly a multiple of M and exists only under edgewise cancellation. The star degrees put half of the mass at the hub; independent rate-one clocks have total first-change hazard (r+1)(1−ε)/2. Independent replay: python3 -B /workspace/branches/independent_checks.py 1, 644 exact generator-rank tests on all connected labeled simple graphs of orders 2–4 at ε=2/5, checking the dimension and degree basis of the linear martingale space. The analytic argument, not the finite tests, establishes the general statement.

## originality

FAIL

Earlier Resultary record 4af872777a16 proves the same exact edge-cancellation and universal weighted-fixation criterion for arbitrary fixed biases on symmetric weighted graphs. It also gives the same separation as bias tends to one: fixation probabilities stay neutral while the waiting time diverges on aligned bipartite graphs. This includes the star after a constant rescaling of update-attempt rate. Its exact drift supplies the occupation correction by stopping. The only other difference, the signed-linear conservation classification, follows directly from complement symmetry, the classical connected-walk invariant, and the already proved edge criterion; it is not a distinct substantial new result.

## value

FAIL

Exact topology-dependent neutrality is a worthwhile question, but the frozen version specializes an earlier more general theorem. Signed-weight uniqueness is an immediate consequence of global opinion complementation and the connected Laplacian; the occupation and clock consequences are routine. No independently substantive remainder warrants repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
