---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

Conditioning on shared triangle/star vertices, intersection size <=1 is independent; size two contributes p^{r+2}q^{r choose 2}(2-(r+1)p) per star set and size three contributes -(r+1)p^{r+3}q^{r choose 2}. Counting shared W gives exactly the displayed binomial covariance. Dividing the bracket by C(n-3,r-1) yields a strictly decreasing affine function of p and the unique root p*=6(n-r-1)/((r+1)(3n-2r-4)), with the n=r+1 boundary strictly negative. Algebraic differentiation establishes n and r monotonicity, with r/n->rho asymptotic. Independent verification substituted H=K1,r into the stronger earlier universal clique/induced-motif covariance formula and matched all terms in rational cases. Finite tests are corroboration, not the general proof.

## originality

FAIL

FAIL. The 2026-10-26 published universal clique-count vs arbitrary induced-motif theorem already yields this precise covariance after H=K1,r and clique order 3, including unique sign switch and finite n>=r+2; the n=r+1 boundary is a one-overlap degeneration. The threshold, monotonicities and r/n scaling are direct algebraic corollaries. Different motif wording is not an escape from mathematical coverage.

## value

FAIL

FAIL: The induced-star threshold and asymptotics are routine specialization and algebraic recasting of an already published all-induced-motif clique covariance theorem. Correctness and clean computation do not add independent new mathematical value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
