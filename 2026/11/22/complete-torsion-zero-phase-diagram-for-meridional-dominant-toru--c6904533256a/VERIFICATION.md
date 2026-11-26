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

An independent Cartesian Taylor expansion and exact polynomial reduction (python /workspace/branches/replay_torsion_algebra.py) reproduced the normalized torsion numerator, endpoint factorizations and decisive curvature components. Because R>1, the radial cross-product component forces sin(qt)=0 at a curvature zero; the other components exclude the outer equator and give exactly R=1+x at the inner equator. The cubic is strictly convex on [-1,1] and negative at zero. On each half interval it has one simple interior root iff the remote endpoint is positive; the signs are those of R-R_- and R_+-R respectively. The endpoint root at +1 has positive derivative in c and therefore order two in t, with nonvanishing curvature. The endpoint root at -1 is excluded even when a separate regular root survives. Each interior root gives 2q parameters and each endpoint q; coprimality ensures these are distinct points. The thresholds cannot coincide because x is rational and the crossing ratio squared is 1+sqrt(3). The argument checks all parameters analytically, not just the frozen test samples.

## originality

PASS

Credit Costa for the established torsion-existence regime and Fuller for the exact curvature singularities. The supported distinct claim is the full count of regular zeros, including the 4q regime, the surviving regular zeros where applicable at the curvature-singular radius, and multiplicities at the outer collision. No actual inspected distinct source supplied or implied this classification as a stated result. Costa's earlier proof remains an important access limitation.

## value

PASS

The exact count for the canonical torus family resolves more than existence: the trefoil has six, twelve, and six regular zeros in the three open regimes, whereas a different winding ratio can yield a middle zero-free window. Multiplicity and loss of Frenet regularity separate two geometrically different transitions. This is a useful extrinsic classification, not claimed to be a knot-type invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
