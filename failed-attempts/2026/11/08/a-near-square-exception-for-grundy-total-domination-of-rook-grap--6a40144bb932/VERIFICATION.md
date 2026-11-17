---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

The selected-edge graph in K_{m,n} faithfully represents open-neighborhood domination on K_m square K_n. Undominated cells are the product of untouched row/column vertices together with isolated selected-edge components. A legal edge joining only previously used endpoints must meet an isolated edge and cannot create a cycle, giving the forest invariant. At first exhaustion of one side, remaining steps destroy isolated edges, proving upper bound m+n-2 except the m by (m+1) matching case with m+n-1; the explicit row/column star sequence and saturated matching plus attachments realize both. The duality with skew zero forcing is a known identity, not a second new proof. Source proof covers all m,n>=2; finite verification is not used to infer the all-dimension claim.

## originality

FAIL

The assigned gamma_gr^t formula, incidence-forest proof mechanism, and skew zero-forcing corollary are already explicitly stated in a Resultary publication from 2026-10-25; a 2026-11-02 published theorem gives the same invariant and a strictly stronger complete description and count of exceptional longest sequences.

## value

PASS

An exact uniform formula on the two-parameter family of rook graphs with a sharp immediately-rectangular anomaly is a natural graph-invariant classification; the incidence forest mechanism and skew forcing interpretation are mathematically substantial. Intrinsic value is independent of the fact that the exact result was previously published.

The dated certificate retains the supplied scientific assessment, sources and limitations.
