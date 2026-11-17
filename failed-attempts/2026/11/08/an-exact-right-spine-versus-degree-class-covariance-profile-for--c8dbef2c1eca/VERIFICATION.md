---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

The final theorem quantifies over ordinary uniform-permutation BSTs on all n>=1. Reconstructed the uniform root split: right path R_n=1+R_b, leaf count L_n=L_a+L_b for n>=2, with base L_1=R_1=1. The joint moment recursion yields q_n=((n+1)/3)H_(n+1)-1/4-1/[6n(n-1)] and Cov(R_n,L_n)=(n-2)(n+1)/[12n(n-1)]; independent exact-rational root split verified n=2..40. Deterministic full-binary-degree identities N0=N2+1 and N0+N1+N2=n then force (c_n,-2c_n,c_n), including n=1,2 and c_n->1/12. The proof is correct; enumeration is corroboration, not infinite proof.

## originality

FAIL

Decisive earlier Resultary full theorem gives exactly c_n for R_n versus leaf count; remaining entries follow solely from fixed binary-tree degree identities, so the entire new profile is a corollary. Not merely a similar BST title.

## value

FAIL

The proposed three-degree profile is a direct algebraic recasting of an already-published same-law extreme-key right-spine/leaf covariance; the accompanying joint-moment formula follows from that covariance and known E R=H_n, E L=(n+1)/3. No new motivated quantity, boundary or structural lemma survives prior coverage, so this principal claim lacks distinct scientific value, although it is correct and reproducible.

The dated certificate retains the supplied scientific assessment, sources and limitations.
