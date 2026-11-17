---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

For Laplacian edge weights (1,t,t,1), t>0, use C=2R−I and reflection decomposition into even 3x3/odd 2x2 blocks. Independently checked with symbolic inversion D1=h²t+2ht+4h+4, D2=5h²t+6ht+4h+4, central return D1/D2, shoulder (h+2)[(1+ht)/D2+1/D1], and the signed shoulder−center expression. Exact substitution at h=2,t=3/4 yields zero CN diagonal entries at the three inner sites and positive outer ones. Off-diagonals are strictly positive by irreducible M-matrix inversion. Every resolvent return decreases continuously from 1 to 1/5 and crosses 1/2 once. At center crossing the difference sign factors through h−2, giving the unique switch t=3/4; implicit polynomial scaling supports H_f(t)=2/sqrt(t)−sqrt(t)+O(t). Proof also compares symmetric paths of sizes 3,4; t=0 is handled separately.

## originality

PASS

The published reversible-Markov return law already establishes C=2R-I, diagonal half threshold and monotone return probabilities; the published uniform reflecting-path theorem covers only equal conductances, with a central obstruction. Neither source evaluates the 1,t,t,1 path across t, finds the shoulder-to-center switch at 3/4 or the singular weak-coupling scaling. Published other Crank–Nicolson studies concern different operators or graph structures. Best-of-knowledge originality for the structural active-site switch.

## value

PASS

A counterintuitive switch of which physical site first loses positivity, with an exact conductance boundary and divergent weak-coupling safe-step law, is a useful nonuniform-grid structural benchmark. Its five-site minimality distinguishes genuine heterogeneity from routine explicit evaluation of a general implicit eigenvalue criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
