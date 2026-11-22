---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-20.md",
      "INDEPENDENT_AUDIT_2026-11-20.json"
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

The radius-one rule after three updates is a seven-letter local predicate; its de Bruijn automaton has 729 six-letter vertices, 1,179 allowed edges. Independently regenerated graph using a separate Kosaraju SCC implementation: a unique cyclic component has 65 vertices and 118 edges. Independently reconstructed all 65 characteristic coefficients by exact trace Newton identities and got λ^61(λ^4−3λ^3+3λ²−λ−1). Closed walks are in bijection with labelled cyclic configurations even for n=3..6, so trace gives all-n recurrence. Opposite direction is spatial reflection; simultaneous satisfaction forces spatial period ≤2, and all six unequal 2-color alternating pairs fail the third iterate, leaving exactly 3 uniform states. F³=S^± implies F^(3n)=Id for each counted state. Independent brute-force dynamics n=3..9 confirmed a_n=(3,7,18,39,73,127,219), both-direction intersection three. Perron–Frobenius of primitive cyclic component yields rho=1.819... and asymptotic 2rho^n.

## originality

PASS

The source rule and qualitative synchronization are established by Lyu 2014, with infinite-line particle-model study by Lyu/Sivakoff, neither deriving this exact ring wave population. Indexed related SCOPE work classifies star graph synchronization, crown graph attractors, or a different cyclic-dominance excitation rule; their objects/updates do not imply this F³-to-one-site translation recurrence. Generic de Bruijn / Perron–Frobenius method is prior technique, not asserted original. Best-of-knowledge PASS for formula.

## value

PASS

Coherent translation after one intrinsic color-clock cycle is a canonical traveling-wave criterion in finite excitatory oscillator networks. The result supplies the full all-length and both-direction census, exact algebraic growth rate and recurrent/no-transient distinction, rather than a small-graph sample or a generic transfer-method restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
