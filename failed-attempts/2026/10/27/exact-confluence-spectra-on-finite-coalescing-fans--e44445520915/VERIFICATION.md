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

The normal form, counts and asymptotics are correct for labelled relations on the stipulated poset. The only distinct comparable source points are a leaf and t. Downward confluence requires all leaf successors of t in every leaf row and requires each row nonempty if t is a successor of itself. Forward confluence caps each leaf row by the top row if the latter omits t and is automatic otherwise. For k>0 leaf successors of t with t in its row, each leaf row has 2^(m+1-k) choices. In the reflexive count, k rows have that number and the other m-k rows have 2^(m-k); summing the resulting 2^(m^2-(m-1)k) over all leaf sets gives H_m, including the k=0 stratum. Dividing C_m by U^m gives 1+m/U+O(m^2/U^2), while the singleton-row numerator divided by U^m is 1-m/U+O(m^2/U^2); the other ratio uses H_m/U^m=2^(-m)(1+4/U)^m. This gives both stated asymptotics. Recorded exhaustive evidence covers only m=1,2,3; the supporting checker was inspected, not executed.

## originality

FAIL

An earlier Resultary record classifies the very same relations on the dual rooted star, with the same three cases, unrestricted labelled count and exact singleton distinguished-row count. The reflexive count and probability estimates are direct consequences; the small two-world case does not produce a distinct finding.

## value

FAIL

The star is a natural finite modal order, but its exact classification and total are already available on the dual order. The remaining statistics are a diagonal filter in independently chosen rows and a first-order expansion of previously known exact counts, not a distinct independently useful contribution under the scientific standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
