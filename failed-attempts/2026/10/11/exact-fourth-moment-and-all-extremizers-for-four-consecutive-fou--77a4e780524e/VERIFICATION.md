---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

From the seven pairwise distinct frequencies -3..3 modulo N for N>=7, Parseval gives <|F|^4>=S^2+2(sum_h |R_h|^2). Cauchy for the cross mirror pairs and AM-GM imply |R1|<=2AB+B^2, |R2|<=2AB, |R3|<=A^2 with equality for magnitudes (A,B,B,A). Thus the global upper bound equals M(t)=(3t^4+4t^3+12t^2+3)/(2(1+t^2)^2) at t=B/A, and M'= -2t(t^3+3t^2-3t-3)/(1+t^2)^3. Descartes sign variation plus g(0)<0<g(infinity) gives exactly one positive root; both endpoint cases give 3/2 and are strictly suboptimal. Every sharp intermediate bound must attain equality: x0=x3, x1=x2, and all three adjacent phase differences agree, giving precisely the stated family. Independent symbolic identities and independent finite checks corroborated but do not replace the proof. The target RESULT.md and check.py were retrieved from the assigned frozen Git blobs. Source record tree reconstructed from seven fetched blob SHA-1 identities matches the assignment.

## originality

FAIL

Current scientific originality fails as a distinct published claim: complete theorem and every optimizer are already present in a separately published same-day stronger Resultary source. Important chronology caveat: a separately published same-day Resultary source now mathematically covers every target conclusion and even extends to general compact abelian groups and sharp small-order threshold. It has a source commit 112 seconds LATER than the target and the same reported public sync time, so it is not established to precede the target. Historical pre-2026 sources materially inspected do not show the fully weighted sharp four-mode maximum with all extremizers. Thus this FAIL is for complete current mathematical coverage and lack of a distinct surviving contribution, not a claim that the other source preceded the target or was independently first. Source ordering remains a significant priority risk for owner reconciliation.

## value

PASS

Intrinsically valuable exact norm for the first consecutive Fourier packet with distinct optimal inner/outer magnitude scales. It yields a sharp algebraic L2-to-L4 constant for all alias-free cyclic grids and the circle, plus full complex phase rigidity, and is not a routine Parseval substitution: the all-coefficient global optimization and equality analysis require a nontrivial one-variable reduction. Its mathematical significance survives the large originality/prioritization concern; no larger theorem required. However a contemporaneous stronger published version means no distinct new theorem remains for separate publication.

The dated certificate retains the supplied scientific assessment, sources and limitations.
