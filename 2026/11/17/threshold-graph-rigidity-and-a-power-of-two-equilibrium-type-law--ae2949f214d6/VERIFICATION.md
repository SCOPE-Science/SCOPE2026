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

At line-graph vertex ij, total neighbors=2(n-2); if edge ij is one, its one-neighbors=d_i+d_j-2, so fixedness requires d_i+d_j>=n; if zero, requires d_i+d_j<=n-2. The excluded sum n-1 makes the one-edge set a self-degree threshold graph. Canonical threshold creation bits yield degrees d_i=i b_i+sum_{j>i} b_j; the pairwise inequality is necessary and sufficient. Terminal degree-twin classes give the correct orbit weight n!/prod m_r!. The sparse-case turn inequalities on height h=n-2k, bijective removal of h-2 initial zeros, two-child recursion and complement symmetry yield u_{n,k}=2^(k-1) in sparse regime, absence of odd middle class, total 2^floor(n/2). Independent direct majority enumeration over all 2^C(n,2) edge states for n=3,4,5,6 gives labelled fixed counts 2,10,12,164 and relabelling orbits 2,4,4,8; checked original verify.py and brute.cpp. These are finite diagnostics of the all-size proof.

## originality

PASS

Best-of-knowledge originality: the exact claim is not mechanically implied by inspected primary or published related theorems. The prior half-factor formula provides an algorithmic count of labelled fixed states once degree vectors h are solved, but cannot yield the concise S_n orbit type law without the explicit threshold rigidity and nontrivial sparse-word bijection. The local degree-inequality reduction is acknowledged as a special case of the general published theorem; novelty and value rest on the evaluated orbit formula and polynomial, not a repackaged characterization alone. See explicit access and indexing risks; unsuccessful search is not proof of priority.

## value

PASS

This is a concrete closed isomorphism-type census of immediate majority equilibria on the canonical triangular graph, including a surprising parity hole and a degree/occupation-refined polynomial. It supplements a known general half-factor classification with a nontrivial threshold graph and lattice-walk enumeration; such a small-formula family provides exact benchmarks for symmetric threshold dynamics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
