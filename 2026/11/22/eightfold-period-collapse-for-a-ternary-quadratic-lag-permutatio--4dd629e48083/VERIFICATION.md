---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Because k>=2, the last old coordinate remains available when inverting T_k. A state fixed at 8k is a cyclic recurrence solution. Writing k columns of eight rows gives D y_j=B_{j-1} and D y_0=rho B_{k-1}, with rho the one-row shift and B the nonzero mask. Cyclic summation forces weights 0,3,6; a zero forces all columns zero because an ensuing nonzero constant would have weight eight. The independent exhaustive enumeration of 3^8 words at /workspace/branches/744fb5ef-27ca-4681-ad52-d3cc8969e69/mask_graph_check.py reproduced 84 vertices, 96 arrows, the stated four-mask adjacency, no core exits, and no three-step exterior walk. Equivariance lets the path to rho^{-1}B_0 close after eight rotated copies; every vertex of a closed walk is on a cycle, hence in the core. Four consecutive predecessor mask bits then sum to three, forcing y_{j,t+4}=y_{j,t}, including across the wrap. The reverse inclusion is immediate. For the count, a unique predecessor zero at row z in a four-row column allows exactly two admissible lifts with zeros at z+1 or z+2, each unique for its support. The wrap contributes one extra row shift; if j transitions move by two, k+j+1 is divisible by four. Four starting rows and the resulting binomial sum count nonzero states, plus the zero state. This argument is universal; bounded direct state counts in the supplied verifier were not rerun.

## originality

PASS

The same map, fourfold fixed-point count, and equality at k=2 are already known. A related short least-period catalogue concerns the recurrence with the linear and quadratic lags interchanged. The distinct claim is the uniform equality of the two fixed sets; it was not established by the inspected results.

## value

PASS

For a studied family with a known fourfold sector, determining whether the next doubled sector adds any points is a natural gap, not a count of a chosen instance. The uniform exclusion follows from a finite exact recurrent-mask obstruction and a rotation argument that handles every lag, and determines an otherwise unknown iterate-fixed set from an established one.

The dated certificate retains the supplied scientific assessment, sources and limitations.
