---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

RESULT.md blob f89ed72: row-space character orthogonality yields rank-shell Fourier multipliers. Rank-two eigenvalue Phi dominates ranks 1 and 3 for all a>0, is monotone with Phi(0)=-1 and Phi(1)>0, so a unique root in (0,1) determines negative type. Rank-two multiplicity h(t-1)(t-q) determines endpoint centered Gram rank; implicit-function/mean-value expansion gives alpha~q^-m/[q log(3/2)-log2]. Independently computed alpha_(2,3)=0.34862420028772034. Proof is symbolic for all prime powers, finite checks corroborate only selected q,m.

## originality

FAIL

Full published November 8 Resultary paper already treats every q prime power, m>=3 and M_(m,3)(F_q), exactly the same scalar root, rank-two-only endpoint eigenspace, minimum Euclidean dimensions and row asymptotic. Candidate writes c=qt-(q-1)h-1; since (q-1)(q^2+q+1)+1=q^3, this equals q(t-q^2) in the older polynomial. Earlier theorem additionally includes fixed-m large-q asymptotic.

## value

FAIL

Exact negative-type thresholds of bilinear-forms graphs are useful geometric invariants, but the submitted three-column classification and Hilbert dimension drop duplicate the complete published one; no distinct structural lemma beyond a standard alternative rank-character inversion survives.

The dated certificate retains the supplied scientific assessment, sources and limitations.
