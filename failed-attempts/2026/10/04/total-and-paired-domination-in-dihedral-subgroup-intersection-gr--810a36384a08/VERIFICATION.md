---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

Reflection subgroups force at least \(p\) selected subgroups. The \(p\) subgroups \(P_r\) partition the reflections and share \(\langle a^p\rangle\). They cover every prime-order rotation exactly when \(p^2\mid n\); otherwise adding \(\langle a\rangle\) is necessary and sufficient. These witnesses are cliques, and the two odd-size cases admit the stated one-vertex clique extension, proving the paired formula. Prime \(n\) has an edgeless graph.

## originality

FAIL

Kayacan's Lemma 4.3 already proves the exact ordinary domination formula using the very same \(p\) maximal dihedral subgroups \(P_r=\langle a^p,a^rb\rangle\), and its proof records when those subgroups cover the prime-order rotation subgroups. For composite \(n\), those \(P_r\) visibly share \(\langle a^p\rangle\), hence form a clique; adding the rotation subgroup in the other branch preserves that clique. Total domination therefore equals Kayacan's ordinary value immediately, and paired domination is just the even-cardinality adjustment of the same clique construction.

## value

FAIL

The strengthened parameters are natural, but the entire lower bound and sharp witness already appear in Kayacan's proof. Observing that the witness is a clique and imposing even cardinality is a routine strengthening under the common value standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
