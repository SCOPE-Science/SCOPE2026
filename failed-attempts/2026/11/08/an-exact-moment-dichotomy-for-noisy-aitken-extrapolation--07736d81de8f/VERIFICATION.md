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

C PASS. From assigned RESULT.md, V=Y2-2Y1+Y0 has mean b(q-1)^2≠0. If Var(V)=0, T is quadratic Gaussian; otherwise decompose U=κV+H and Y0=cV+J with (H,J) independent of V. T=J-2κH+(c-κ²)V-H²/V. A Gaussian pole at V=0 has two equal one-sided constants f_V(0)EH²; positivity iff S=EH²>0. S=0 iff U=κV identically and the pole cancels. Layer-cake proves p<1 exactly. Covariance contractions for equicorrelated noise give κ=-1/2 and τ²=σ²(1-ρ)/2. The argument handles singular covariances, q∈(-1,1), b≠0, including q=0; no finite check is used as a general proof.

## originality

FAIL

O FAIL. A public 2026-11-02 prior theorem proves exactly the same equal-marginal Gaussian Aitken tail coefficient and perfect-sharing endpoint, and its Step 3 proves the stronger GENERAL jointly Gaussian pole-tail lemma with arbitrary singular covariances. Regression of U on V and elementary Var(V)=0/S=0 degeneracy algebra immediately give the submitted purported extension to arbitrary PSD covariance. The earlier same-problem proof and formula were read in full. The submitted covariance classification is thus a direct application, not a separate nonstandard result.

## value

FAIL

V FAIL for this submitted finding (not the underlying problem): detecting when unregularized noisy extrapolation has no finite mean is mathematically motivated, but a published identical coefficient plus general pole lemma already resolves it; the remaining variance-degeneracy cases are routine polynomial/Gaussian regression. Rephrasing an existing singularity theorem under a wider covariance heading supplies no independent structural invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
