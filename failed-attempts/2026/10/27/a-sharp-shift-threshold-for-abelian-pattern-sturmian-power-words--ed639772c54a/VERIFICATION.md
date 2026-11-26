---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

If d<b(b−2), every layer a_j=b^j+d for j≥2 satisfies a_j>2a_{j−1}. A largest-sum cycle edge in such a layer would have both endpoints at most a_{j−1}, since each has another incident cycle edge and a given sum is a matching. That is impossible. On the first two matchings, successive left indices around any alternating cycle would change by the same nonzero amount, so these layers alone cannot contain a cycle. At and above the cutoff, t=d−b(b−2)≥0, δ=b−1; the proposed two sequences consist of b+1 distinct nonnegative labels per side, with b+1 middle-sum edges, b smallest-sum edges and one largest-sum closing edge. This includes b=2 and t=0. Theorem E of arXiv:2609.28059v2 gives the forest equivalence and all-k formula. Its Theorem 7.4 applies since the growing zero gaps put 0^∞ in the orbit closure; substituting r=b+1 gives the claimed lower bound at k=binom(b+2,2). Independent DFS on first-three-layer graphs for bases 2–14 and first-five-layer forests at the last allowed shift for bases 3–7 corroborates, but does not prove, these claims (python3 /workspace/reproductions/frozen_checks.py 5).

## originality

FAIL

The distinct October 25 Resultary record 3ec886d6644d states the identical sharp threshold and first-three-layer cycle on the larger domain c≥−1. On setting c=d, its graph is exactly the frozen graph; exchanging the two sides gives the same cycle, including the boundary. The explicit complexity gap is a direct substitution in the published cycle-to-gap theorem and uses no new witness. This is demonstrable content coverage, not an inference from chronology alone.

## value

FAIL

A sharp threshold with an explicit forbidden cycle would be valuable in this natural family, but the frozen record repeats the known classification with a narrower domain and the same witness. Its extra displayed complexity lower bound is only a parameter substitution into a published theorem. No additional mathematical contribution of value remains.

The dated certificate retains the supplied scientific assessment, sources and limitations.
