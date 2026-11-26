---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Re-audited /workspace/repairs/3/RESULT.md. The original branch paragraph asserted uniqueness within a half-wave; a full sign-matched lobe between two sine zeros can yield two crossing intervals. The corrected proof selects one zero-to-peak quarter-wave and uses the first 2δ crossing and last δ crossing before it. At order one, log|xy| is bounded on each compact invariant set in the specified interior; neither sine vanishes there, and the nonpositive increment of log|xy| has zero integral for every invariant probability. Its zero set on the compact coordinate projections is finite: the phases are bounded, and for each of the finitely many admissible sine-extremum phase values the equation in t is quadratic. Invariant probabilities on this finite support are mixtures of cycle measures; each periodic Jacobian is a signed permutation matrix, so both exponents vanish. The variational principle yields zero entropy and a diagonal sine-maximum fixed point makes the defining supremum nonempty. Off order one, near zero Tν either has a nonzero constant term or, at order three, has slope −3, so |Tν|>2δ on [δ,2δ]. The phase length is asymptotic to a/(2δ), furnishing any specified number of disjoint selected crossings. On those intervals |sin Φ|≤ρ<1, |Φ′|≥a/(8δ²), and |Tν′| is bounded. Thus |Tν cos Φ Φ′| dominates |Tν′ sin Φ|, with the first term of order at least δ^(−2) or δ^(−1) at order three. The scalar derivative is of constant sign with modulus >Λ on each selected interval, giving separated inverse contractions and a bijective full-shift coding by nested intervals. In the fixed diagonal and antidiagonal frame the same bound controls both planar eigenvalues; compactness and the ergodic theorem applied to their log moduli give the asserted strict almost-sure bounds for every invariant measure. This proves exactly the compact-restriction result, not entropy at a compactification or typical-orbit chaos. The quarter-wave construction is an analytic replay; the supplied diagnostic was inspected, not executed.

## originality

PASS

The correction leaves the model-specific theorem intact: one exactly neutral order, with both ambient directions expanding on arbitrarily large full shifts for every other order. Finite-time chaos indicators, related singular sine maps and general full-branch coding do not supply that classification. The judgment is limited to inspected evidence.

## value

PASS

The conclusion identifies a singular parameter boundary in a named map: all compactly supported invariant probabilities become finite periodic mixtures at one order, while arbitrarily close nonneutral orders admit arbitrarily large finite-symbol dynamics with verified transverse as well as tangential expansion. This distinction matters when finite-time indicators are used to interpret singular maps. It does not imply anything about physical attractors, positive-area basins, or applications outside the compact-invariant scope. The proof correction preserves this value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
