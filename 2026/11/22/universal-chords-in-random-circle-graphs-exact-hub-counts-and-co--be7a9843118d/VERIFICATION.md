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

A universal chord must leave n−1 endpoints on each side. For k specified diameters the pattern of sides changes once per selected diameter in each half-turn; its complement occurs only in the opposite sector. Thus gap populations s_i must be paired across opposite sectors independently in s_i! ways. Marking a starting selected diameter counts each k-set k times, giving n/k times the factorial composition sum divided by (2n−1)!!. If n−1 diameters are present, the remaining endpoints force the last one. In the two-arc permutation representation chord pairs cross iff their images are in the same order. An additional universal chord forces j to be a fixed point and all lesser indices to map to lesser values, i.e. the singleton direct-sum block criterion. Under that conditioning the expected excess count is (1/N) sum of reciprocals of binom(N−1,r); the two boundary terms contribute 2/N, the next terms O(N^−2), and the at most N interior terms are each O(N^−2) before the outside 1/N. Bonferroni and size bias prove the stated probabilities, including E[U−1|U≥1]=O(1/n) since U−1≤binom(U,2) on the event. Rotating the fixed diameter gives the size-biased law for X; tilting by U changes the existence-conditioned law by O(1/n) in total variation. The inversion-sequence independent discrete uniforms give the conditional mean/variance and Lindeberg CLT with n^(3/2) scaling and variance 1/36. For the unconditional density, pairing independent continuous endpoints chord-by-chord gives independence for crossing indicators with disjoint chord labels and variance O(n³). Empty permutations cover n=1. A fresh exact scan of active chord endpoints (/workspace/branches/replay_chords.py) reproduced all binomial moments through n=7, and both per-permutation identities and the conditional crossing histograms through n=8; submitted checker inspected, not run. Finite replay does not validate the limits by itself.

## originality

PASS

Credit the diameter obstruction, the marked-chord conditional mean, unconditional crossing laws and classical inversion distribution as known ingredients. The exact joint universal count, its rare-event multiplicity control and the resulting crossing law under existence conditioning constitute the supported distinct claim. No examined source covers that law or provides the full universal chord statistics; historical equivalents in permutation enumeration remain possible.

## value

PASS

The maximum possible degree is a natural global structural threshold. The factorial composition formula gives exact probabilities for all hub multiplicities, not just the expected number of diameters, and supports a sharp change in crossing density and a fluctuation law under a meaningful rare-event condition. This distinguishes a typical hub-bearing diagram from an ordinary diagram and from conditioning on a named present chord.

The dated certificate retains the supplied scientific assessment, sources and limitations.
