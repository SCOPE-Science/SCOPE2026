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

Integrating the held input gives the stated M(h). With K=k_p and D=k_d, its characteristic evaluations at +1 and -1 are Kh^2 and 4-2Dh; its determinant is 1-Dh+Kh^2/2. The real quadratic Schur test gives h<2/D and h<2D/K, with the lower determinant bound automatic there. For P=M(b)M(a), write s=a+b and p=ab. Direct expansion gives trace 2-Ds-Ks^2/2+(D^2-K)p+KDps/2+K^2p^2/4 and determinant 1-Ds+Ks^2/2+(D^2-K)p-KDps/2+K^2p^2/4. Thus det(I-P)=Ks(s-Dp), strictly positive since 1/a+1/b>D, and 2 det(I+P)=Phi. Also |det P|<1 as the product of the two one-step determinants. Hence Phi>0 is equivalent to Schur stability in the specified open range. At equality the second root is -det P in the open disk, so -1 is simple. At Phi<0 the monic characteristic polynomial is negative at -1 and positive sufficiently far to the left, giving a real root below -1. The rational witness reproduces both one-step Schur tests and the claimed two-step trace, determinant and signs.

## originality

FAIL

The distinct published Resultary record 18a80c1bcb0a covers the same necessary-and-sufficient boundary on the same admissible domain and proves a stronger gain-ratio dichotomy. Its two-step characteristic evaluations also give the multiplier statements by the same determinant bound; the frozen witness is one instance of the instability range it covers. This is a determination of demonstrable coverage in the published corpus, not a finding of earlier priority, improper attribution or a mathematical error. The matching record bears a later catalogue date.

## value

FAIL

The difference between fixed-interval and alternating stability is a worthwhile control question. As a contribution, however, this record supplies the already-covered special-case boundary and a routine spectral interpretation of the same Jury factors. The rational witness makes that interpretation concrete but adds no separate phenomenon beyond the stronger published gain-ratio classification. There is no surviving independently useful unknown exact claim in the frozen statement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
