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

Baadi's real-coefficient Theorem 1.2 states for every \(q\in(1,2]\) that \(p_-(\mathcal H)<q\) iff \(\omega\in RH_{q'/2}\), and the same introduction explicitly lists the power-weight condition \(-2n/q'<\beta<n\). For \(\beta<0\), solving that inequality gives \(q>2n/(2n+\beta)\); the infimum in the source definition is therefore exactly that value. The local-finiteness clause gives the identical boundary because \(|x|^{\beta p'/2}\) is locally integrable iff \(\beta p'/2>-n\). For \(\beta\ge0\), the source explicitly places the power weight in \(RH_\infty\), and its real-coefficient theorem gives \(p_-=1\). Substitution into the source Riesz and duality ranges is algebraically correct. At \(\beta=-n^2/(n+2)\), direct algebra gives \(p_-=2_*\) while the endpoint power \(|x|^{-n}\) in the reverse-Hölder test is not locally integrable. The packaged symbolic checker correctly replays these identities.

## originality

FAIL

The exact formula is mechanically implied by the primary source itself. Theorem 1.2 gives the sharp real-coefficient equivalence \(p_-<q\iff\omega\in RH_{q'/2}\), and immediately afterward the paper already writes the power-weight membership condition \(-2n/q'<\beta<n\), the endpoint condition \(\beta>-n^2/(n+2)\), and the nonnegative-power \(RH_\infty\) regime. Taking the infimum in \(q\) is one line of algebra. The local-finiteness coincidence is the same inequality from the definition, and the displayed critical power is obtained by solving equality with \(2_*\). Under implication-based originality, absence of the final closed formula as a separate sentence does not make this an independent result.

## value

FAIL

Making the source's power-weight inequalities explicit as a single formula is convenient, but it requires only solving a displayed linear-fractional inequality and substituting into the source's theorems. The critical \(2_*\) power is the equality boundary of a condition the source already writes down. No new estimate, counterexample mechanism, or structural lemma is added, so this is below the value bar for a separate scientific record.

The dated certificate retains the supplied scientific assessment, sources and limitations.
