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

For input ones at i<j the one-deletion outputs of weight one have their one at i or j−1. They coincide exactly for adjacent ones. Thus if L selected words have adjacent ones and S do not, L+2S≤n−1. Consecutive starts for the adjacent words collide on a weight-two output, so L≤ceil((n−1)/2); taking floors gives the claimed upper bound. In the construction adjacent starts are even and spaced by two while the gap-three starts are 1 mod 4. The weight-one outputs are disjoint (one even index per adjacent word or a disjoint pair of odd indices for each gap-three word). For weight-two outputs the new first-one positions for distinct starts within either family lie in disjoint sets {i−1,i}, with unavailable positions at the boundary simply excluded. Across families the output gap is one versus two or three, so the descendants are disjoint. Counting the two families saturates the bound, including the sole word at n=2.

## originality

FAIL

Two distinct earlier public repository findings give the all-n≥2 binary exact-weight-two optimum under deletion of either symbol and the same construction. A third gives the same optimum from n≥3. The exact repository coverage suffices independently of unresolved external historical priority.

## value

FAIL

The weight-two optimum under deletion of either symbol is a natural exact invariant, but the assigned finding supplies the same formula, same range and same optimal support construction as existing findings. There is no classification of all extremizers or other distinct mathematical remainder to retain.

The dated certificate retains the supplied scientific assessment, sources and limitations.
