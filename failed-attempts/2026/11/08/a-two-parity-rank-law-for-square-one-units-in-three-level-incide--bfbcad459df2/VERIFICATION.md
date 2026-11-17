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

Every diagonal element d of a square-one unit in characteristic two satisfies (d+1)^2=0 and hence d=1. Block multiplication reduces N^2=0 to AB=0; C is unrestricted q^{n²}. Rank-r A count is [n choose r]_q prod_{i<r}(q^n-q^i); compatible B has q^{n(n-r)} choices. Fixed-field D-product asymptotics around r=n/2 yield the two theta weights and total variation error O_q(q^{-n/2}); conditional B surjectivity onto ker A fails with probability bounded by E[q^{-rank A}]/(q-1). Checked complete proof and original verifier code; independent exhaustive n=2 over F2 gives spectrum [256,576,96].

## originality

FAIL

FAIL: the published November 2 zero-product matrix-pair finding explicitly fixes the identical jointly uniform AB=0 measure over all finite fields and gives the same full rank weights W_n(r), sharper joint rank/homology law, the same parity theta limit, and a sharper asymptotic homology defect coefficient. Multiplying its W_n(r) by the free C-block q^{n²} gives exactly this submission T_{n,r}. The 2026 October 12 incidence-algebra Jordan-spectrum result already identifies all square-one units with AB=0 for arbitrary three level sizes and computes their total count. Combining these two published general theorems strictly covers every mathematical conclusion of the submitted theorem. Prior full proofs inspected, not mere title matching.

## value

FAIL

FAIL as an independent new mathematical finding: the characteristic-two incidence-algebra interpretation and exact total count were already published for arbitrary layer sizes, while the parity-limit and homology statements follow directly from the November 2 stronger uniform zero-product pair theorem. The submitted problem is natural and its proof correct, but the remaining step is a routine re-expression of those results.

The dated certificate retains the supplied scientific assessment, sources and limitations.
