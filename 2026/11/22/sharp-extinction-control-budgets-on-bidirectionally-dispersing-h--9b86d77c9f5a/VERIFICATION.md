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

Irreducibility of the column-conservative migration matrix with a diagonal perturbation gives positive left and right Perron vectors. Nonnegative solutions are invariant and global (total population has a logistic upper bound); if the spectral abscissa s≤0, the positive left-vector pairing V satisfies V′≤−(min c_i)V²/(sum w_i), so the zero-eigenvalue boundary still gives extinction for every initial state. If s>0, a sufficiently small positive right-vector multiple is a stationary subsolution, and cooperative comparison rules out extinction from that initial state. The budget minimum exists by compactness of 0≤sum h_i≤nr, since uniform h_i=r works and s is continuous. Summing the right-vector equations gives nr−ns plus the paired edge terms; AM–GM forces s=0 and v_j/v_i=sqrt(m_ij/m_ji) at equality. Path integration constructs v up to scaling if and only if the ratios close around all cycles; substituting gives exactly h* and feasibility/uniqueness. Trees satisfy the cycle condition. Any optimum must have s=0, since when s<0 some nonzero control could be reduced. For two patches, minimizing bt+a/t in log t gives t=sqrt(a/b) if feasible; when a>b and r<a−sqrt(ab), the feasible left endpoint (a−r)/b is larger than this and yields exactly the stated downstream control. On the homogeneous biased triangle, the log-ratios sum to zero and strict Jensen forces the optimum at constant v, yielding H=3r. Independently checked the rational tree witness by B(1,3,6)^T=0 and the cost 16=21−5; for (a,b,r)=(9,1,1) the low-growth control (0,9/8) gives B(1,8)^T=0.

## originality

PASS

The comparison credits classical detailed balance, Perron stabilization and diagonal-similarity optimization. The inspected work that poses the same extinction objective does not solve it in the stated regimes. In the bounded comparisons no distinct source gives or implies the full closed-form budget and exactness/active-set classification under the required nonnegative constant controls. The supported claim is this constrained extinction result and its explicit contrasting regimes, not novelty of the spectral criterion or cycle balance.

## value

PASS

The Finding gives an edge-data budget and unique controls on an entire network class above a sharp threshold, detects exactly when the local edge lower bound is unattainable, and contrasts an active two-patch boundary with a circulation obstruction. These answer a natural extinction-allocation question rather than merely restating a solver or a spectral test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
