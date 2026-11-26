---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For h_j in (0,1) the survival probabilities are positive at every finite age. The last-reset partition gives Φ_t(X)=S_t E^t(X)+Tr(X)B_t with Tr B_t=1−S_t. Setting q_t=S_{t+1}/S_t and subtracting q_t E(B_t) from B_{t+1} gives a mass ν_{t+1} at σ and coefficients ν_s S_{t−s}(h_{t+1}−h_{t+1−s}) at E^{t+1−s}(σ). Hence for nondecreasing hazards Y_t≥0 with trace h_{t+1}. The intermediate is a convex combination of E and a replacement channel and the composition identity holds without assuming E invertible. For the converse use a cyclic unitary and pure reset at site zero with dimension m+2 for a drop at m. The trace-preserving Φ_m has trivial kernel because on traceless operators it is S_m times a unitary conjugation, so the intermediate is unique. Only the age-m term contributes at site m and the test projector at m is moved to site m+1 by the unitary. The intermediate therefore has the negative site-m entry h_1S_{m−1}(h_{m+1}−h_m). I separately propagated exact age-and-site probabilities for drops at m=1,2,6: from each initial site advance mass by (1−h_{age+1}) to (age+1, next site) and by h_{age+1} to (0,0); sum over ages to form T_m,T_{m+1}, and multiply T_{m+1}T_m⁻¹. For h_j=2/5 up to m and h_{m+1}=1/5 the predicted negative entry is −(2/25)(3/5)^{m−1}; for m=1 the test column is (7/25,−2/25,4/5). The simulations corroborate the all-time operator argument. The frozen checker counts a separate m=1 example in addition to positions 1–14, so its fifteen witness checks do not mean fifteen distinct positions.

## originality

FAIL

Distinctness of the frozen scientific claim fails on direct statement-level evidence: Resultary 52ec499cc555 proves the same universal Schrödinger CP/P-divisibility equivalence under weaker assumptions and gives the same cyclic obstruction in a smaller dimension. The finite-time coefficients and negative witness agree, not just the title. This is a judgment of demonstrable coverage by a distinct record, not a claim of chronological priority, copying, or provenance. The older published literature inspections identify antecedent renewal machinery but are not the basis of the failure.

## value

PASS

As mathematics, a sharp criterion across all channels cleanly separates age-dependent resetting that always preserves divisibility from resetting admitting even a classical cyclic counterexample. It has explanatory value beyond the constant-hazard case, with a witness at an arbitrary finite drop. This is an assessment of the theorem's mathematical content, not an endorsement of a redundant record as a distinct contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
