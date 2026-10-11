---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

The intrinsic subspaces are indeed \(P_q^2=Fu\) and \([P_q,P_q]=Fu\oplus Fv\). In an adapted basis \(u_0=au\), \(v_0=bu+cv\), \(x_0=dx+ru+sv\), the product condition gives \(dc=a\) and the bracket normalization gives \(d=1\), hence \(c=a\) and \([x_0,v_0]=v_0+qu_0\). Thus the adapted-basis coefficient is exactly \(q\). The associative component is independent of \(q\); all nonzero Lie parameters are isomorphic by the stated scaling map; and the zero parameter is separated by scalar versus non-scalar adjoint action on the characteristic derived ideal. The dimension-two minimality follows from the primary classification theorem that both products cannot simultaneously be nonzero in dimension two.

## originality

FAIL

The final claim is already mechanically contained in Petrov–Pypka's primary classification. Their Theorem 5.5 gives exactly the family \(P_{3,22}(q)\), states \(P_{3,22}(q)\cong P_{3,22}(q')\) iff \(q=q'\), and proves this using the same intrinsic subspaces and coefficient comparison \(a=dc\), \(d=1\), then \(q=q'\). Their dimension-two theorem supplies the claimed minimality. The remaining observation that all nonzero underlying Lie matrices are isomorphic is a one-line change of basis from the displayed family. Repackaging the source's parameter-separation proof as an 'adapted-basis compatibility scalar' does not create an original theorem under the implication-based originality standard.

## value

FAIL

Once the primary classification and its exact q-separation proof are available, the assigned 'compatibility scalar' is a relabeling of that proof and the common-component observation is a routine basis change. The conceptual phrasing is useful exposition, but it does not isolate a remaining motivated mathematical gap sufficient for an independent validated finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
