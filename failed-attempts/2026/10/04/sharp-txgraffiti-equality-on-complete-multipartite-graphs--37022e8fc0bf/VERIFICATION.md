---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

For \(K_{n_1,\ldots,n_r}\), let \(N\) be the order, \(m\) the smallest part, and \(M\) the largest. Then \(\Delta=N-m\) and \(\alpha=M\). The sum of the \(\Delta+1\) smallest degrees is at least \(2e-(m-1)\Delta>e\), because the edges incident with a smallest part already give \(e\ge m\Delta\); hence \(a\le\Delta\). Gupta's equality criterion then yields \((\Delta-1)M\le\Delta\), forcing complete graphs for \(\Delta\ge3\) and the stated low-degree cases. Direct invariant calculations confirm all four survivors. A fresh independent complete-multipartite enumeration reproduced exactly these four equality types through order 19.

## originality

FAIL

A stronger pre-existing source was missed by the frozen audit. Kadrawi and Levit, submitted 1 July 2026, prove a general equality characterization for the same TxGraffiti inequality. Their Corollary 9 states that for connected graphs with \(\Delta=2\), equality holds exactly when \(R=\alpha\), and for \(\Delta\ge3\) it can hold only when \(\Delta=3\) together with explicit Caro--Wei/residue/slack equalities. Specializing this theorem to complete multipartite graphs reduces the submitted classification to a tiny finite check: \(\Delta=2\) gives only \(P_3,K_3,C_4\); \(\Delta=3\) permits only five part-size patterns, of which the general equality conditions leave only \(K_4\). Thus the final classification is a direct corollary of a stronger theorem publicly available more than three months before this record.

## value

FAIL

After the July 2026 all-connected-graphs equality theorem, the complete-multipartite classification requires only identifying the \(\Delta=2\) family and checking five \(\Delta=3\) part patterns. The auxiliary bound \(a\le\Delta\) is correct but elementary and does not rescue the covered final claim as a separate substantive contribution under the common value bar.

The dated certificate retains the supplied scientific assessment, sources and limitations.
