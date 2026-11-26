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

Conditioning on a fixed vertex being isolated leaves the uniform m-edge graph on n-1 vertices. A copy cannot include the isolated vertex because H has no isolated vertices. Hence E[I X_H]=E[I] E_{n-1,m}[X_H]. Dividing the conditional and unconditional copy means gives (n-k)/n times (N)_e/(B)_e; subtracting one gives the displayed bracket, whose sign (not magnitude) is independent of m when both means are positive. Below e or above B one count is identically zero. In G(n,p) only the copy-placement ratio (n-k)/n remains because the edge presence probabilities cancel. Multiplying the fixed-edge brackets by n(B)_e gives the two stated opposite two-edge factors and the stated cubic for (k,e)=(5,3). The latter is negative at 6 and 7, increases for x>=8, and takes -30 at 10 and 64 at 11. An independently written standard-library replay, /workspace/branches/replay_5.py, checked exact moments for 837 graphs on five vertices (two motifs per graph) and 30,706 graphs on six vertices, and the three factorizations through n=200. The infinite claims use the analytic argument.

## originality

FAIL

The earlier Oct. 12 Resultary record states and proves the identical fixed-edge covariance and m-independent sign for every non-induced motif with no isolated vertices, not just trees. The three named instances are direct substitutions into that exact formula; the independently sampled-edge comparison is standard edge independence. This is verified coverage, not an inference from the earlier title or a failure to fetch a source.

## value

FAIL

An m-invariant sign for natural motif counts would be a useful structural result, but the entire invariant and its range are already recorded. The examples only substitute three small parameter pairs into that same closed form; there is no independently established new structural or motivated exact claim to retain as a repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
