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

For any \(v\), each neighbor \(w\) has two distinct triangle-completing vertices in \(N[v]\), so every vertex of the induced \(G[N[v]]\) has degree at least three and none is removable. If \(\deg(v)\le n-1\), then \(|N[v]|\le n\), contradicting \(\psi_n\); hence \(\delta(G)\ge n\). Thus \(V\ge n+1\), \(E\ge nV/2\), and \(E\le3V-6+6g\) gives \(g\ge1+\lceil(n-6)(n+1)/12\rceil\).

## originality

FAIL

Lockhart's planar-obstruction proof already forms the same closed neighborhood, proves it has no removable vertex, and invokes \(\psi_6\) after a planar low-degree bound. Removing the planar degree-\(5\) input immediately gives the arbitrary-\(n\) minimum-degree lemma; handshaking plus the standard Euler edge inequality then gives the genus formula. The final claim is therefore a mechanical generalization/corollary of the published proof.

## value

FAIL

The quantitative genus expression is correct but, after Lockhart's published neighborhood proof, follows from routine handshaking and Euler inequalities rather than a distinct mathematical gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
