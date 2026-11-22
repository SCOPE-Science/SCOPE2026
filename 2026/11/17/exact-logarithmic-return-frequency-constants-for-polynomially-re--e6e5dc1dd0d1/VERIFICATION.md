---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

For 1≤p<∞, α>0, 0<ε<1 and n^α B^n, select k return times n_1<...<n_k. Decomposing first coordinate from tail gives |n_i^α x_{n_i}−1|^p+n_i^{αp}S_{i+1}<ε^p. Maximizing t/(u^p+t) subject to |u−1|^p+t≤ε^p yields ρ=ε/(1+ε) for p=1, or ρ=δ^{p−1}/[δ^{p−1}+(1−δ)^{p−1}] with δ=ε^{p/(p−1)}. Thus S_{i+1}≤ρ S_i and endpoint norm bounds imply k≤αp log N/log(1/ρ)+O(1). The constructive witness x_{m_j}=c m_j^{−α}, m_j=ceil(ρ^{−j/(αp)}(j+1)^2), c=1−δ (or 1 for p=1), has strict return errors due to m_{j+h}>Q^h m_j and return count (log N)/(log Q)+o(log N). Independently optimized the one-step loss for 24 (p,ε) pairs, checked the sharp algebraic witness identity, and verified p=2 simplifies to α/log(1/ε). Complex case follows ||a|−1|≤|a−1|. A fixed-ball supremum is proved, not frequent hypercyclicity or universal dense orbit of the witness.

## originality

PASS

BEST-OF-KNOWLEDGE PASS for the full finite-ε, p-dependent exact supremum coefficient. The directly earlier Resultary sharp logarithmic packing theorem proves uniform count bounds, exact c₀ coefficient, lower/upper ℓᵖ brackets and the common ε→0 limit; it explicitly leaves finite-p exact constants unsettled. The new extremal mass-loss optimization and matching sparse witness resolve this identified quantitative gap.

## value

PASS

The maximal logarithmic return coefficient is a natural quantitative refinement of non-autonomous shift recurrence. Its exact dependence on Banach exponent p and ball radius resolves a real interval left by a directly matching prior theorem and produces sharp witnesses, even though it does not claim frequent hypercyclicity or a global operator classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
