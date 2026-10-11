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

The channel output determinant separates into the pure-state value plus a nonnegative input-mixedness term, so equality at the entropy roof forces purity. The exact scalar roof \(g_p(q)\) is strictly convex for \(0<p<1\), hence equality in Jensen forces every signal excitation to equal \(q_*\). Proposition 5.6 fixes the ensemble average to the diagonal state \(\tau_*\), which is equivalent to weighted phasor balance. Conversely those conditions give the required average and each signal has entropy \(g_p(q_*)\), so the Holevo value is capacity. A finite set of positive weights closes to a zero phasor polygon iff the largest weight is at most half the total.

## originality

FAIL

Tang--Zhu--Bai--Wang already prove the fixed-input roof \(\widehat S_{\mathcal A_p}(\tau)=g_p(q)\), exhibit a fixed-excitation pure decomposition attaining it, prove the binary capacity formula, and prove the unique optimal average input \(\tau_*\) for \(p<1\), while explicitly noting that different optimal ensembles are allowed. The audited classification follows by equality analysis of these results: strict convexity of the displayed scalar roof forces every pure signal in an optimal decomposition to have excitation \(q_*\); purity/equality fixes the latitude; averaging to diagonal \(\tau_*\) is exactly the weighted phasor-balance equation. The probability criterion is the standard polygon-closing condition. Under the required implication standard this is a direct corollary of prior results, not an original theorem.

## value

PASS

As a mathematical statement, the complete equality-case classification is useful: it describes all finite optimal alphabets and gives an exact feasibility criterion for prescribed probabilities. Its value survives even though it is not original under the required implication standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
