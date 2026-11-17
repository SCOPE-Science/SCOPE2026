---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

Run `python check_crossover.py` with Python 3 and SymPy. The checker computes the exact Taylor jet of the positive-magnitude map, the inverse-square constant term, and the reciprocal term by symbolic arithmetic. It verifies the rational identities \(A(8)=64/3\), \(B(8)=1024/5\), and \(B(8)/A(8)=48/5\).

The test iterates trajectories with fixed gain \(8+\theta/N\) for \(\theta=-8,-2,0,2,8\) and three initial amplitudes, at horizons \(10^4\) and \(10^5\). It checks that the residual of the proposed two-term asymptotic is finite and changes by a bounded amount at the tested horizons. These are numerical consistency checks, **not a proof of the infinite-horizon expansion**. The mathematical proof is in RESULT.md and controls all sufficiently large \(N\) via a uniform invariant interval, positive inverse-square drift, and summable remainder.

The exact fixed-critical \(\theta=0\) logarithm is already published after conjugacy, and is used solely as a consistency check. The new claim is the finite-horizon moving-gain coefficient at \(\theta\ne0\). Independent audit has not been performed.
